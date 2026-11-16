"""Helpers for ``experiments/local_pipeline.py`` (the local-victim "internals" pipeline).

Pure logic (episode selection, note cleanup, style-example and other-episode choice, the item
registry, tier selection, resume bookkeeping, loaders) is model-free and unit-tested in
``tests/test_local_pipeline.py``. The GPU helpers at the bottom (shared-prefix KV caching for
teacher-forced scoring and P(yes)) take a ``LocalLM`` and are only imported lazily by the CLI.
"""
from __future__ import annotations

import copy
import gzip
import hashlib
import json
import math
import os
import re
from collections import OrderedDict, defaultdict
from pathlib import Path
from typing import Callable, Iterable, Optional, Sequence

import numpy as np

from ..config import (LOCAL_OTHER_MODELS, LOCAL_SEEDS, LOCAL_STYLE_SEEDS, N_STYLE_EXAMPLES, T3_N_CANDIDATES,
                      is_calibration, t3_subset)
from ..prompts import consistency_yesno, note_writing, verbal_yesno, verbal_yesno_bare
from ..schema import EDIT_TYPES, FAMILIES, Episode, stable_hash

# ------------------------------------------------------------------------------------------------
# constants
# ------------------------------------------------------------------------------------------------
KIND_ORDER = ("genuine", "T2", "T0", "T1", "cand", "other")   # priority within a pass ("other" = other:*)
# Passes in priority order; each pass is finished for all its kinds before the next starts.
PASSES = ("s_trace", "s_blind", "c", "v_att", "v")
ACT_PASSES = ("s_trace", "s_blind")
FORGED_TIERS = ("T0", "T1", "T2")
PASS_KINDS = {   # which kinds each pass applies to; v on cand only for candidates picked by `select`
    "s_trace": ("genuine", "T2", "T0", "T1", "cand", "other"),
    "s_blind": ("genuine", "T2", "T0", "T1", "cand", "other"),
    "c": ("genuine", "T2", "T0", "T1", "cand"),
    "v_att": ("cand",),
    "v": ("genuine", "T2", "T0", "T1", "cand"),
}
SELECT_RULES = {   # tier -> (score column, maximize)
    "T3": ("v_att_pyes", True),
    "T4s": ("s_trace_mean", False),
    "T4d": ("s_delta", False),
    "T4c": ("c_pyes", True),
}
RULE_TIERS = tuple(SELECT_RULES) + ("T2r",)


def kind_base(kind: str) -> str:
    return "other" if kind.startswith("other:") else kind


def passes_for(kind: str, selected: bool = False) -> tuple:
    """Passes that apply to an item of ``kind``; for cand, ``v`` only if the candidate was selected."""
    k = kind_base(kind)
    return tuple(p for p in PASSES if k in PASS_KINDS[p] and (p != "v" or k != "cand" or selected))


def instances(main_ids: Sequence[str]) -> list:
    """The study instances: (episode_id, edit_type) for the 2 t3_subset edit types of each main episode."""
    return [(e, et) for e in main_ids for et in t3_subset(e)]


# ------------------------------------------------------------------------------------------------
# item ids
# ------------------------------------------------------------------------------------------------
def gid(ep_id: str, s: int) -> str:
    return f"g|{ep_id}|s{s}"


def fid(tier: str, ep_id: str, et: str) -> str:
    return f"{tier}|{ep_id}|{et}"


def cid(ep_id: str, et: str, k: int) -> str:
    return f"c|{ep_id}|{et}|{k}"


def oid(model: str, ep_id: str, s: int) -> str:
    return f"o:{model}|{ep_id}|s{s}"


def xid(ep_id: str, et: str) -> str:
    return f"x|{ep_id}|{et}"


def note_sha(note: Optional[str]) -> str:
    return hashlib.sha1((note or "").encode("utf-8")).hexdigest()[:12]


# ------------------------------------------------------------------------------------------------
# JSONL I/O (append + flush + fsync; tolerant reader)
# ------------------------------------------------------------------------------------------------
def read_jsonl(path) -> list:
    p = Path(path)
    if not p.exists():
        return []
    rows = []
    opener = gzip.open if p.suffix == ".gz" else open
    try:
        with opener(p, "rt", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError:
                    continue   # truncated last line after a kill
    except (EOFError, gzip.BadGzipFile, OSError):
        pass                   # truncated last gzip member after a kill: keep what was read
    return rows


def append_jsonl(path, rows: Iterable[dict]) -> int:
    rows = list(rows)
    if not rows:
        return 0
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    data = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows)
    if p.suffix == ".gz":
        with gzip.open(p, "at", encoding="utf-8") as f:
            f.write(data)
    else:
        with open(p, "a", encoding="utf-8") as f:
            # a killed writer can leave a partial last line; start on a fresh line
            if f.tell() > 0:
                with open(p, "rb") as r:
                    r.seek(-1, os.SEEK_END)
                    if r.read(1) != b"\n":
                        data = "\n" + data
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
    return len(rows)


def write_jsonl_atomic(path, rows: Iterable[dict]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(p.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, p)


def done_set(rows: Iterable[dict], key: Callable[[dict], object]) -> set:
    """Keys of rows already on disk (resume: these jobs are skipped)."""
    return {key(r) for r in rows}


# ------------------------------------------------------------------------------------------------
# episodes
# ------------------------------------------------------------------------------------------------
def study_ids(limit: Optional[int] = None) -> tuple:
    """(main_ids, style_ids). Main ids are interleaved over families (seed-major) so that partial
    results are balanced; ``limit`` keeps the first N seeds per family of each split."""
    main_seeds = list(LOCAL_SEEDS)[:limit] if limit else list(LOCAL_SEEDS)
    style_seeds = list(LOCAL_STYLE_SEEDS)[:limit] if limit else list(LOCAL_STYLE_SEEDS)
    main = [f"{fam}-{s:05d}" for s in main_seeds for fam in FAMILIES]
    style = [f"{fam}-{s:05d}" for s in style_seeds for fam in FAMILIES]
    return main, style


def load_study_episodes(limit: Optional[int] = None, root: Path | str = ".") -> tuple:
    from ..env.generate import load_episodes
    main, style = study_ids(limit)
    want = set(main) | set(style)
    eps = {}
    for fam in FAMILIES:
        for e in load_episodes(str(Path(root) / "data" / "episodes" / f"{fam}.jsonl")):
            if e.episode_id in want:
                eps[e.episode_id] = e
    missing = want - set(eps)
    if missing:
        raise RuntimeError(f"episodes missing from data/episodes: {sorted(missing)[:5]} ...")
    return eps, main, style


def session_edit_type(ep: Episode, s: int) -> Optional[str]:
    for et, e in ep.edits.items():
        if e.session_idx == s:
            return et
    return None


def messages(instr_input: tuple) -> list:
    instructions, inp = instr_input
    return [{"role": "system", "content": instructions}, {"role": "user", "content": inp}]


# ------------------------------------------------------------------------------------------------
# note cleanup and quality checks
# ------------------------------------------------------------------------------------------------
_PREAMBLE_RE = re.compile(
    r"^\s*(?:\*\*|#+\s*)?(?:(?:here(?:'s| is) (?:my |the |your )?(?:rewritten |updated |revised )?(?:memory )?note"
    r"(?: for (?:this|the) session)?)|(?:(?:rewritten |updated |revised )?memory note(?: for session \d+)?)|"
    r"(?:(?:rewritten |revised )?note))\s*(?:\*\*)?\s*[:\-]\s*(?:\*\*)?\s*", re.I)
_QUOTES = ('"', "'", "“", "”", "‘", "’", "`")


def clean_note(text: Optional[str]) -> tuple:
    """Strip, remove a leading 'Memory note:'-style label and wrapping quotes, collapse to one
    paragraph. Returns (note, flags) where flags records what was changed."""
    flags = {"preamble": False, "quotes": False, "multi_par": False}
    t = (text or "").strip()
    m = _PREAMBLE_RE.match(t)
    if m and m.end() < len(t):
        flags["preamble"] = True
        t = t[m.end():].strip()
    if "\n" in t:
        flags["multi_par"] = bool(re.search(r"\n\s*\n", t)) or t.count("\n") > 0
        t = re.sub(r"\s*\n+\s*", " ", t)
    for _ in range(2):
        if len(t) >= 2 and t[0] in _QUOTES and t[-1] in _QUOTES:
            flags["quotes"] = True
            t = t[1:-1].strip()
    t = re.sub(r"[ \t]{2,}", " ", t).strip()
    return t, flags


_FINAL_PUNCT = tuple('.!?)"\'”’]')


def note_problem(note: str, n_tokens: int, max_new_tokens: int, min_chars: int = 40) -> Optional[str]:
    """None if the note is usable, else 'empty' | 'short' | 'truncated'."""
    if not note:
        return "empty"
    if len(note) < min_chars:
        return "short"
    if n_tokens >= max_new_tokens - 4 and not note.rstrip().endswith(_FINAL_PUNCT):
        return "truncated"
    return None


# ------------------------------------------------------------------------------------------------
# style examples (T2 / candidates) and other-episode genuine notes (xep)
# ------------------------------------------------------------------------------------------------
def style_pool(notes: dict, style_ids: Iterable[str]) -> dict:
    """Restrict genuine notes ((ep_id, s) -> note) to style episodes (never main episodes)."""
    ss = set(style_ids)
    return {k: v for k, v in notes.items() if k[0] in ss and v}


def style_examples(episode_id: str, edit_type: str, family: str, style_notes: dict,
                   n: int = N_STYLE_EXAMPLES) -> list:
    """``n`` genuine victim notes from style episodes of ``family`` (keys (style_ep_id, s) of
    ``style_notes``), chosen by stable_hash; distinct style episodes are preferred."""
    pool = sorted(((sid, s) for (sid, s) in style_notes if sid.startswith(family + "-")),
                  key=lambda k: (stable_hash("style", episode_id, edit_type, k[0], k[1]), k))
    if len(pool) < n:
        raise ValueError(f"only {len(pool)} style notes for family {family}")
    picked, used = [], set()
    for k in pool:
        if k[0] not in used:
            picked.append(k)
            used.add(k[0])
        if len(picked) == n:
            break
    for k in pool:
        if len(picked) == n:
            break
        if k not in picked:
            picked.append(k)
    return [style_notes[k] for k in picked]


def pick_xep(ep: Episode, edit_type: str, family_main: Sequence[Episode]) -> tuple:
    """For (ep, edit_type): another main episode of the same family whose session hosts the same
    edit type, preferring one where it sits in the same slot. Returns (src_ep_id, src_session, same_slot)."""
    slot = ep.edits[edit_type].session_idx
    others = [o for o in family_main if o.episode_id != ep.episode_id and o.family == ep.family
              and edit_type in o.edits]
    if not others:
        raise ValueError(f"no other main episode in family {ep.family}")
    same = [o for o in others if o.edits[edit_type].session_idx == slot]
    pool = same or others
    pool = sorted(pool, key=lambda o: (stable_hash("xep", ep.episode_id, edit_type, o.episode_id), o.episode_id))
    src = pool[0]
    return src.episode_id, src.edits[edit_type].session_idx, bool(same)


# ------------------------------------------------------------------------------------------------
# item registry
# ------------------------------------------------------------------------------------------------
def _item(item_id, kind, ep: Episode, edit_type, s, note, cand_idx=None, valid=None, **extra) -> dict:
    d = {"item_id": item_id, "kind": kind, "episode_id": ep.episode_id, "family": ep.family,
         "edit_type": edit_type, "session_idx": s, "cand_idx": cand_idx, "valid": valid,
         "note": note, "note_sha": note_sha(note), "passes": list(passes_for(kind))}
    d.update(extra)
    return d


def build_items(eps: dict, main_ids: Sequence[str], notes: dict, forged: Sequence[dict],
                candidates: Sequence[dict], other_notes: Sequence[dict]) -> tuple:
    """Build the registry over the study instances (t3_subset target slots). ``notes``: (ep_id, s) ->
    genuine victim note. Returns (items, missing) where ``missing`` counts texts that could not be
    registered (absent or empty note)."""
    items, missing = [], defaultdict(int)
    inst = instances(main_ids)
    by_key = {(r["tier"], r["episode_id"], r["edit_type"]): r for r in forged}
    cand_by = {(r["episode_id"], r["edit_type"], r["cand_idx"]): r for r in candidates}
    oth = {(r["model"], r["episode_id"], r["session_idx"]): r for r in other_notes}
    models = sorted({r["model"] for r in other_notes}, key=lambda m: (m not in LOCAL_OTHER_MODELS, m))
    for e, et in inst:
        ep = eps[e]
        s = ep.edits[et].session_idx
        n = notes.get((e, s))
        if n:
            items.append(_item(gid(e, s), "genuine", ep, et, s, n))
        else:
            missing["genuine"] += 1
        for tier in ("T2", "T0", "T1"):
            r = by_key.get((tier, e, et))
            if r is None or not r.get("note"):
                missing[tier] += 1
                continue
            items.append(_item(fid(tier, e, et), tier, ep, et, s, r["note"], valid=bool(r.get("valid")),
                               mode=r.get("mode"), attempts=r.get("attempts")))
        for k in range(T3_N_CANDIDATES):
            r = cand_by.get((e, et, k))
            if r is None or not r.get("note"):
                missing["cand"] += 1
                continue
            items.append(_item(cid(e, et, k), "cand", ep, et, s, r["note"], cand_idx=k, valid=bool(r.get("valid"))))
        for m in models:
            r = oth.get((m, e, s))
            if r is None or not r.get("note"):
                missing[f"other:{m}"] += 1
                continue
            items.append(_item(oid(m, e, s), f"other:{m}", ep, et, s, r["note"], model=m))
    order = {k: i for i, k in enumerate(KIND_ORDER)}
    items.sort(key=lambda d: order[kind_base(d["kind"])])  # stable: keeps instance order within kind
    return items, dict(missing)


def genuine_store(notes: dict, ep: Episode) -> list:
    return [notes.get((ep.episode_id, s)) or "" for s in range(len(ep.sessions))]


def pass_prompt(pass_: str, item: dict, ep: Episode, store: Sequence[str]) -> list:
    """Chat messages for one (pass, item). For s_trace/s_blind the note is the continuation."""
    s = item["session_idx"]
    if pass_ == "s_trace":
        return messages(note_writing(ep, s, with_trace=True, as_json=False))
    if pass_ == "s_blind":
        return messages(note_writing(ep, s, with_trace=False, as_json=False))
    if pass_ == "c":
        return messages(consistency_yesno(ep, s, item["note"]))
    if pass_ == "v":
        return messages(verbal_yesno(ep, store, s, item["note"]))
    if pass_ == "v_att":   # short bare prompt (no memory store); attacker's ranking phrasing
        return messages(verbal_yesno_bare(ep, item["note"], attacker=True))
    raise ValueError(pass_)


def score_groups(items: Sequence[dict], main_order: Sequence[str]) -> list:
    """Group a block's items by (episode_id, session_idx), in main-episode then session order."""
    pos = {e: i for i, e in enumerate(main_order)}
    groups = OrderedDict()
    for it in sorted(items, key=lambda d: (pos.get(d["episode_id"], 1 << 30), d["session_idx"])):
        groups.setdefault((it["episode_id"], it["session_idx"]), []).append(it)
    return list(groups.items())


def score_todo(items: Sequence[dict], done: set, selected: Iterable[str] = ()) -> list:
    """(pass, item) pairs still to compute, in pass priority order; ``done`` holds
    (pass, item_id, note_sha); ``selected`` are candidate item_ids that also get pass ``v``."""
    sel = set(selected)
    return [(p, it) for p in PASSES for it in items
            if p in passes_for(it["kind"], it["item_id"] in sel)
            and (p, it["item_id"], it["note_sha"]) not in done]


def selected_ids(rows: Iterable[dict], tiers: Iterable[str] = RULE_TIERS) -> list:
    """Distinct non-null candidate item_ids chosen by the given tiers (order preserved)."""
    ts = set(tiers)
    out = []
    for r in rows:
        if r["tier"] in ts and r.get("item_id") and r["item_id"] not in out:
            out.append(r["item_id"])
    return out


# ------------------------------------------------------------------------------------------------
# tier selection (adaptive attacks are formed post hoc from candidate scores)
# ------------------------------------------------------------------------------------------------
def _finite(x) -> bool:
    try:
        return x is not None and math.isfinite(float(x))
    except (TypeError, ValueError):
        return False


def candidate_instances(cands: Sequence[dict]) -> "OrderedDict":
    inst = OrderedDict()
    for c in cands:
        inst.setdefault((c["episode_id"], c["edit_type"]), []).append(c)
    return inst


def select_by_score(cands: Sequence[dict], scores: dict, tier: str, maximize: bool = True) -> list:
    """Generic selection hook. ``cands``: candidate item rows (item_id, episode_id, edit_type,
    cand_idx, valid). ``scores``: item_id -> score. Among VALID candidates with a finite score pick
    the best (ties -> lower cand_idx). Instances without one get item_id None."""
    out = []
    for (e, et), cs in candidate_instances(cands).items():
        ok = [c for c in cs if c.get("valid") and _finite(scores.get(c["item_id"]))]
        best = None
        if ok:
            sign = -1.0 if maximize else 1.0
            best = min(ok, key=lambda c: (sign * float(scores[c["item_id"]]), c.get("cand_idx") or 0))
        out.append({"episode_id": e, "edit_type": et, "tier": tier,
                    "item_id": best["item_id"] if best else None,
                    "score": float(scores[best["item_id"]]) if best else None})
    return out


def select_random(cands: Sequence[dict], tier: str = "T2r") -> list:
    """Matched no-selection baseline: a random VALID candidate chosen by stable_hash."""
    out = []
    for (e, et), cs in candidate_instances(cands).items():
        ok = sorted((c for c in cs if c.get("valid")), key=lambda c: c.get("cand_idx") or 0)
        pick = ok[stable_hash(tier, e, et) % len(ok)] if ok else None
        out.append({"episode_id": e, "edit_type": et, "tier": tier,
                    "item_id": pick["item_id"] if pick else None, "score": None})
    return out


def select_all(cand_rows: Sequence[dict]) -> list:  # T3, T4s, T4d, T4c, T2r
    """All rule-based tiers. ``cand_rows``: dicts with item fields plus the score columns."""
    rows = []
    for tier, (col, maximize) in SELECT_RULES.items():
        scores = {c["item_id"]: c.get(col) for c in cand_rows}
        rows += select_by_score(cand_rows, scores, tier, maximize)
    rows += select_random(cand_rows, "T2r")
    return rows


def append_selection(out_dir, tier: str, scores: dict, maximize: bool = True) -> list:
    """Hook for analysis code (e.g. the probe tier ``T4p``): select among valid candidates by
    ``scores`` (item_id -> score) and append the rows to ``selected.jsonl`` (replacing any earlier
    rows of the same tier)."""
    out_dir = Path(out_dir)
    cands = [d for d in read_jsonl(out_dir / "items.jsonl") if d["kind"] == "cand"]
    new = select_by_score(cands, scores, tier, maximize)
    old = [r for r in read_jsonl(out_dir / "selected.jsonl") if r["tier"] != tier]
    write_jsonl_atomic(out_dir / "selected.jsonl", old + new)
    return new


# ------------------------------------------------------------------------------------------------
# loaders
# ------------------------------------------------------------------------------------------------
def _latest(rows, key):
    d = {}
    for r in rows:
        d[key(r)] = r
    return d


def load_items(out_dir) -> list:
    return read_jsonl(Path(out_dir) / "items.jsonl")


def load_scores(out_dir):
    """One row per registry item with the scores of all passes (and external baselines)."""
    import pandas as pd
    out_dir = Path(out_dir)
    items = load_items(out_dir)
    sha = {it["item_id"]: it["note_sha"] for it in items}
    sc = _latest((r for r in read_jsonl(out_dir / "scores.jsonl") if sha.get(r["item_id"]) == r.get("note_sha")),
                 key=lambda r: (r["item_id"], r["pass"]))
    ext = _latest((r for r in read_jsonl(out_dir / "external.jsonl") if sha.get(r["item_id"]) == r.get("note_sha")),
                  key=lambda r: r["item_id"])
    rows = []
    nan = float("nan")
    for it in items:
        i = it["item_id"]
        r = {k: it.get(k) for k in ("item_id", "kind", "episode_id", "family", "edit_type", "session_idx",
                                    "cand_idx", "valid", "note")}
        r["calib"] = is_calibration(it["episode_id"])
        for p in ACT_PASSES:
            s = sc.get((i, p), {})
            for k in ("mean", "max", "sum", "n"):
                r[f"{p}_{k}"] = s.get(k, nan)
        r["n_tok"] = r["s_trace_n"] if _finite(r["s_trace_n"]) else r["s_blind_n"]
        r["s_delta"] = r["s_trace_mean"] - r["s_blind_mean"]
        for p in ("v", "c", "v_att"):
            r[f"{p}_pyes"] = sc.get((i, p), {}).get("p_yes", nan)
        e = ext.get(i, {})
        for k in ("gpt2_mean", "small_mean", "small_trace_mean"):
            r[k] = e.get(k, nan)
        rows.append(r)
    df = pd.DataFrame(rows)
    for c in ("s_trace_n", "s_blind_n", "n_tok"):
        if c in df:
            df[c] = pd.to_numeric(df[c], errors="coerce")
    return df


def load_activations(out_dir, which: str = "trace", pooling: str = "mean", acts_dir=None):
    """(item_ids, array[n_items, n_layers, d_model] float16) for pass s_<which>, registry order.
    Only items whose stored note hash matches the registry are returned."""
    out_dir = Path(out_dir)
    if which not in ("trace", "blind") or pooling not in ("mean", "last"):
        raise ValueError("which in {trace, blind}, pooling in {mean, last}")
    if acts_dir is None:
        cfg = json.loads((out_dir / "config.json").read_text())
        acts_dir = cfg["acts_dir"]
    acts_dir = Path(acts_dir)
    pass_ = f"s_{which}"
    sha = {it["item_id"]: it["note_sha"] for it in load_items(out_dir)}
    idx = _latest((r for r in read_jsonl(acts_dir / "index.jsonl")
                   if r["pass"] == pass_ and sha.get(r["item_id"]) == r.get("note_sha")),
                  key=lambda r: r["item_id"])
    shards = {}
    ids, arrs = [], []
    for i in sha:
        r = idx.get(i)
        if r is None:
            continue
        if r["shard"] not in shards:
            with np.load(acts_dir / r["shard"], allow_pickle=False) as z:
                shards[r["shard"]] = {k: z[k] for k in z.files}
        ids.append(i)
        arrs.append(shards[r["shard"]][pooling][r["row"]])
    if not arrs:
        return [], np.zeros((0, 0, 0), dtype=np.float16)
    return ids, np.stack(arrs)


# ------------------------------------------------------------------------------------------------
# GPU: shared-prefix KV caching (exactness verified against LocalLM on the smoke data)
# ------------------------------------------------------------------------------------------------
def common_prefix_len(seqs: Sequence[Sequence[int]]) -> int:
    if not seqs:
        return 0
    n = min(len(s) for s in seqs)
    first = seqs[0]
    for i in range(n):
        t = first[i]
        if any(s[i] != t for s in seqs[1:]):
            return i
    return n


def _prefix_cache(lm, prefix: Sequence[int]):
    import torch
    if not prefix:
        return None
    ids = torch.tensor([list(prefix)], dtype=torch.long, device=lm.device)
    with torch.inference_mode():
        out = lm._base(input_ids=ids, attention_mask=torch.ones_like(ids), use_cache=True)
    cache = out.past_key_values
    del out
    return cache


def _forward_rems(lm, cache, P: int, rems: Sequence[Sequence[int]], hidden: bool):
    """Right-padded forward of continuations ``rems`` after a shared cached prefix of length P."""
    import torch
    B, T = len(rems), max(len(r) for r in rems)
    ids = torch.full((B, T), lm.pad_id, dtype=torch.long)
    mask = torch.zeros((B, T), dtype=torch.long)
    for i, r in enumerate(rems):
        ids[i, :len(r)] = torch.tensor(list(r), dtype=torch.long)
        mask[i, :len(r)] = 1
    ids, mask = ids.to(lm.device), mask.to(lm.device)
    with torch.inference_mode():
        if cache is None:
            out = lm._base(input_ids=ids, attention_mask=mask, output_hidden_states=hidden, use_cache=False)
        else:
            c = copy.deepcopy(cache)
            # expand batch 1 -> B (LinearAttentionLayer has no batch_repeat_interleave; reorder works)
            c.reorder_cache(torch.zeros(B, dtype=torch.long, device=lm.device))
            full = torch.cat([torch.ones((B, P), dtype=torch.long, device=lm.device), mask], dim=1)
            out = lm._base(input_ids=ids, attention_mask=full, past_key_values=c, use_cache=True,
                           output_hidden_states=hidden)
            del c
    return out.last_hidden_state, (out.hidden_states if hidden else None)


def score_shared_prompt(lm, prompt_ids: Sequence[int], conts: Sequence[Sequence[int]], layers=None,
                        chunk: int = 16) -> list:
    """Teacher-forced surprisal of each continuation after ONE shared prompt (+ pooled activations).

    Equivalent to ``LocalLM.score_and_activations`` with identical prompts: the prompt minus its last
    token is run once and cached; each chunk then runs [last prompt token] + continuation.
    Returns per item ``(surprisal list, mean_act [L,D] | None, last_act [L,D] | None)``.
    """
    import torch
    prefix, lastp = list(prompt_ids[:-1]), prompt_ids[-1]
    P = len(prefix)
    cache = _prefix_cache(lm, prefix)
    rems = [[lastp] + list(c) for c in conts]
    order = sorted(range(len(rems)), key=lambda i: -len(rems[i]))
    res = [None] * len(rems)
    for s in range(0, len(order), chunk):
        idx = order[s:s + chunk]
        last, hs = _forward_rems(lm, cache, P, [rems[i] for i in idx], hidden=layers is not None)
        bidx, pidx, tgt = [], [], []
        for b, i in enumerate(idx):
            C = len(conts[i])
            bidx += [b] * C
            pidx += list(range(0, C))
            tgt += list(conts[i])
        if tgt:
            sur = lm._logprobs_at(last[torch.tensor(bidx, device=lm.device), torch.tensor(pidx, device=lm.device)],
                                  torch.tensor(tgt, device=lm.device)).cpu().numpy()
        else:
            sur = np.zeros(0, dtype=np.float32)
        off = 0
        for b, i in enumerate(idx):
            C = len(conts[i])
            ss = [float(x) for x in sur[off:off + C]]
            off += C
            ma = la = None
            if layers is not None:
                if C == 0:
                    ma = la = np.full((len(layers), lm.d_model), np.nan, dtype=np.float32)
                else:
                    st = torch.stack([hs[L][b, 1:1 + C].float() for L in layers])
                    ma, la = st.mean(1).cpu().numpy(), st[:, -1].cpu().numpy()
            res[i] = (ss, ma, la)
        del last, hs
    del cache
    return res


def pyes_shared_prefix(lm, seqs: Sequence[Sequence[int]], yes_ids, no_ids, chunk: int = 16) -> list:
    """Normalised next-token P(yes) at the end of each token sequence (a rendered chat prompt),
    running the longest common token prefix of all sequences only once. Returns
    (list of dicts {p_yes, mass_yes, mass_no}, cached prefix length)."""
    import torch
    L = min(common_prefix_len(seqs), min(len(s) for s in seqs) - 1)
    cache = _prefix_cache(lm, seqs[0][:L]) if L > 0 else None
    rems = [list(s[L:]) for s in seqs]
    yi = torch.tensor(list(yes_ids), device=lm.device)
    ni = torch.tensor(list(no_ids), device=lm.device)
    order = sorted(range(len(rems)), key=lambda i: -len(rems[i]))
    res = [None] * len(rems)
    for s in range(0, len(order), chunk):
        idx = order[s:s + chunk]
        last, _ = _forward_rems(lm, cache, L, [rems[i] for i in idx], hidden=False)
        pos = torch.tensor([len(rems[i]) - 1 for i in idx], device=lm.device)
        h = last[torch.arange(len(idx), device=lm.device), pos]
        with torch.inference_mode():
            probs = torch.softmax(lm._head(h).float(), dim=-1)
        py, pn = probs[:, yi].sum(1).cpu().numpy(), probs[:, ni].sum(1).cpu().numpy()
        for b, i in enumerate(idx):
            a, n = float(py[b]), float(pn[b])
            res[i] = {"p_yes": a / (a + n) if (a + n) > 0 else float("nan"), "mass_yes": a, "mass_no": n}
        del last, probs
    del cache
    return res, L


# ------------------------------------------------------------------------------------------------
# GPU: many groups at once. Prefixes of several groups are run as ONE left-padded batch (exact for
# the Gated-DeltaNet layers of Qwen3.5: their conv has no bias, so zeroed padding positions leave the
# recurrent state at zero; full-attention layers use the mask and explicit position ids). The cache
# rows are then gathered per continuation (reorder_cache) and all continuations of all groups run in
# right-padded chunks with position ids continuing each row's own prefix length.
# ------------------------------------------------------------------------------------------------
def chunk_rows(lengths: Sequence[int], max_rows: int, max_tokens: int) -> list:
    """Greedy chunks of row indices (rows pre-sorted by decreasing length) with at most ``max_rows``
    rows and rows * longest_row <= ``max_tokens`` (at least one row per chunk)."""
    chunks, cur, cur_max = [], [], 0
    for i, n in enumerate(lengths):
        m = max(cur_max, n)
        if cur and (len(cur) + 1 > max_rows or (len(cur) + 1) * m > max_tokens):
            chunks.append(cur)
            cur, m = [], n
        cur.append(i)
        cur_max = m
    if cur:
        chunks.append(cur)
    return chunks


def multi_prefix_forward(lm, groups: Sequence[tuple], hidden: bool, rows_per_chunk: int = 16,
                         max_tokens: int = 4096):
    """``groups``: list of (prefix_ids, [rem_ids, ...]). Yields (rows, last_hidden, hidden_states)
    per chunk, where rows is a list of (group_idx, rem_idx) aligned with the batch dimension.
    Continuation chunks hold at most ``rows_per_chunk`` rows and ``max_tokens`` padded new tokens."""
    import torch
    dev = lm.device
    G = len(groups)
    plen = [len(p) for p, _ in groups]
    Pmax = max(plen)
    if min(plen) < 1:
        raise ValueError("every group needs a non-empty prefix")
    pid = torch.full((G, Pmax), lm.pad_id, dtype=torch.long)
    pmask = torch.zeros((G, Pmax), dtype=torch.long)
    for g, (p, _) in enumerate(groups):
        pid[g, Pmax - len(p):] = torch.tensor(list(p), dtype=torch.long)
        pmask[g, Pmax - len(p):] = 1
    pid, pmask = pid.to(dev), pmask.to(dev)
    ppos = (pmask.cumsum(1) - 1).clamp(min=0)
    with torch.inference_mode():
        out = lm._base(input_ids=pid, attention_mask=pmask, position_ids=ppos, use_cache=True)
    cache = out.past_key_values
    del out
    rows = [(g, r) for g, (_, rems) in enumerate(groups) for r in range(len(rems))]
    rows.sort(key=lambda gr: -len(groups[gr[0]][1][gr[1]]))
    plen_t = torch.tensor(plen, dtype=torch.long, device=dev)
    lens = [len(groups[g][1][r]) for g, r in rows]
    for cidx in chunk_rows(lens, rows_per_chunk, max_tokens):
        ch = [rows[i] for i in cidx]
        rems = [groups[g][1][r] for g, r in ch]
        B, T = len(ch), max(len(x) for x in rems)
        ids = torch.full((B, T), lm.pad_id, dtype=torch.long)
        rmask = torch.zeros((B, T), dtype=torch.long)
        for i, x in enumerate(rems):
            ids[i, :len(x)] = torch.tensor(list(x), dtype=torch.long)
            rmask[i, :len(x)] = 1
        ids, rmask = ids.to(dev), rmask.to(dev)
        gi = torch.tensor([g for g, _ in ch], dtype=torch.long, device=dev)
        with torch.inference_mode():
            c = copy.deepcopy(cache)
            c.reorder_cache(gi)
            full = torch.cat([pmask[gi], rmask], dim=1)
            pos = plen_t[gi][:, None] + torch.arange(T, device=dev)[None, :]
            o = lm._base(input_ids=ids, attention_mask=full, position_ids=pos, past_key_values=c,
                         use_cache=True, output_hidden_states=hidden)
            del c
        yield ch, o.last_hidden_state, (o.hidden_states if hidden else None)
        del o
    del cache, pid, pmask, ppos
    _free()


def _free():
    """Release cached device memory once per window (MPS keeps freed blocks pooled; shapes vary)."""
    import torch
    if torch.backends.mps.is_available():
        torch.mps.empty_cache()


def score_multi(lm, groups: Sequence[tuple], layers=None, rows_per_chunk: int = 16, max_tokens: int = 4096) -> list:
    """``groups``: list of (prompt_ids, [cont_ids, ...]); every continuation is scored after its
    group's prompt. Returns, per group, a list of (surprisal list, mean_act|None, last_act|None)."""
    import torch
    fwd = [(list(p[:-1]), [[p[-1]] + list(c) for c in conts]) for p, conts in groups]
    res = [[None] * len(conts) for _, conts in groups]
    for ch, last, hs in multi_prefix_forward(lm, fwd, hidden=layers is not None, rows_per_chunk=rows_per_chunk,
                                                max_tokens=max_tokens):
        bidx, pidx, tgt = [], [], []
        for b, (g, r) in enumerate(ch):
            c = groups[g][1][r]
            bidx += [b] * len(c)
            pidx += list(range(len(c)))
            tgt += list(c)
        if tgt:
            sur = lm._logprobs_at(last[torch.tensor(bidx, device=lm.device), torch.tensor(pidx, device=lm.device)],
                                  torch.tensor(tgt, device=lm.device)).cpu().numpy()
        else:
            sur = np.zeros(0, dtype=np.float32)
        off = 0
        for b, (g, r) in enumerate(ch):
            C = len(groups[g][1][r])
            ss = [float(x) for x in sur[off:off + C]]
            off += C
            ma = la = None
            if layers is not None:
                if C == 0:
                    ma = la = np.full((len(layers), lm.d_model), np.nan, dtype=np.float32)
                else:
                    st = torch.stack([hs[L][b, 1:1 + C].float() for L in layers])
                    ma, la = st.mean(1).cpu().numpy(), st[:, -1].cpu().numpy()
            res[g][r] = (ss, ma, la)
    return res


def pyes_multi(lm, groups: Sequence[Sequence[Sequence[int]]], yes_ids, no_ids, rows_per_chunk: int = 16,
               max_tokens: int = 4096) -> tuple:
    """``groups``: list of lists of full prompt token sequences; within a group the longest common
    prefix is run once. Returns (per-group lists of {p_yes, mass_yes, mass_no}, per-group prefix len)."""
    import torch
    fwd, Ls = [], []
    for seqs in groups:
        L = max(1, min(common_prefix_len(seqs), min(len(s) for s in seqs) - 1))
        Ls.append(L)
        fwd.append((list(seqs[0][:L]), [list(s[L:]) for s in seqs]))
    yi = torch.tensor(list(yes_ids), device=lm.device)
    ni = torch.tensor(list(no_ids), device=lm.device)
    res = [[None] * len(seqs) for seqs in groups]
    for ch, last, _ in multi_prefix_forward(lm, fwd, hidden=False, rows_per_chunk=rows_per_chunk,
                                                max_tokens=max_tokens):
        pos = torch.tensor([len(fwd[g][1][r]) - 1 for g, r in ch], device=lm.device)
        h = last[torch.arange(len(ch), device=lm.device), pos]
        with torch.inference_mode():
            probs = torch.softmax(lm._head(h).float(), dim=-1)
        py, pn = probs[:, yi].sum(1).cpu().numpy(), probs[:, ni].sum(1).cpu().numpy()
        for b, (g, r) in enumerate(ch):
            a, n = float(py[b]), float(pn[b])
            res[g][r] = {"p_yes": a / (a + n) if (a + n) > 0 else float("nan"), "mass_yes": a, "mass_no": n}
    return res, Ls
