"""Local ("internals") experiment pipeline: the local victim (Qwen3.5-4B, MPS) as memory writer.

Instances: for each main episode (LOCAL_SEEDS, 3 families) the 2 edit types of t3_subset -> 300 instances;
everything except genuine-note writing is restricted to these instances' target slots.
Stages (each resumable: rows are appended + flushed as produced; finished items are skipped):
  notes     victim's genuine notes, all 7 sessions of main + style (LOCAL_STYLE_SEEDS) episodes -> notes.jsonl
  hosted    API: other-model notes (LOCAL_OTHER_MODELS) for the target slots -> other_notes.jsonl; T1 forgeries
            by LOCAL_T1_FORGER -> forged_t1.jsonl (raw API rows: hosted_raw_*.jsonl)
  forge     T0 (template) + T2 (victim rewrites its own note, 3 style examples) -> forged.jsonl;
            T3_N_CANDIDATES rewrites at T3_TEMPERATURE per instance -> candidates.jsonl
  items     registry of every text to score -> items.jsonl (item_id, kind, episode, session, note, ...)
  score     pass-major: s_trace, s_blind (surprisal + pooled activations; all kinds) -> c (not other)
            -> v_att (cand; bare short prompt) -> [select] -> v (memory-store prompt; genuine, T0-T2 and
            the selected candidates). Within a pass kinds in order genuine, T2, T0, T1, cand, other.
            -> scores.jsonl (one row per (item, pass)), surprisal_tokens.jsonl.gz, activations in --acts
  select    adaptive tiers among VALID candidates: T3 (max v_att), T4s (min s_trace), T4d (min s_delta),
            T4c (max c), T2r (random valid) -> selected.jsonl; hook for T4p: pipeline.append_selection
  external  GPT-2 and Qwen3.5-0.8B surprisal of the bare note (+0.8B given the raw session) -> external.jsonl
Item kinds: genuine | T0/T1/T2 (forged target notes) | cand (adaptive candidates) | other:<model>.
Loaders: memlab.local.pipeline.load_scores(out) / load_activations(out, which, pooling).
Use --limit-episodes N with a separate --out/--acts for smoke tests (enforced).
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import numpy as np  # noqa: E402

from memlab import config as C  # noqa: E402
from memlab.attacks.template import apply_t0, is_valid_forgery  # noqa: E402
from memlab.local import pipeline as P  # noqa: E402
from memlab.prompts import forge_t1, forge_t2, note_writing  # noqa: E402
from memlab.schema import EDIT_TYPES, render_session, stable_hash  # noqa: E402

DEFAULT_OUT = ROOT / "results" / "raw" / "local"
DEFAULT_ACTS = ROOT / "cache" / "local_acts"
MAX_NEW_TOKENS = 200
MAX_ATTEMPTS = 4          # 1 try + up to 3 retries (notes, T2, T1)
SEED_MOD = 2 ** 31 - 1


# =================================================================================================
# setup
# =================================================================================================
def setup(args):
    out = Path(args.out).resolve()
    acts = Path(args.acts).resolve()
    if args.limit_episodes and (out == DEFAULT_OUT.resolve() or acts == DEFAULT_ACTS.resolve()):
        sys.exit("--limit-episodes requires a separate --out and --acts (smoke data must not mix with the real run)")
    out.mkdir(parents=True, exist_ok=True)
    cfg_path = out / "config.json"
    cfg = {"limit_episodes": args.limit_episodes, "acts_dir": str(acts), "model": C.LOCAL_PRIMARY,
           "revision": C.LOCAL_PRIMARY_REVISION, "dtype": C.LOCAL_DTYPE, "gen_batch": args.gen_batch,
           "max_new_tokens": MAX_NEW_TOKENS, "max_attempts": MAX_ATTEMPTS}
    if cfg_path.exists():
        old = json.loads(cfg_path.read_text())
        for k in ("limit_episodes", "acts_dir", "model", "revision", "dtype", "gen_batch"):
            if old.get(k) != cfg[k]:
                sys.exit(f"config mismatch for {k}: on disk {old.get(k)!r}, now {cfg[k]!r} ({cfg_path})")
    else:
        cfg_path.write_text(json.dumps(cfg, indent=1))
    eps, main, style = P.load_study_episodes(args.limit_episodes, ROOT)
    return out, acts, eps, main, style


_LM = {}


def get_lm(args):
    if "lm" not in _LM:
        from memlab.local.model import LocalLM
        _LM["lm"] = LocalLM(C.LOCAL_PRIMARY, revision=C.LOCAL_PRIMARY_REVISION, dtype=C.LOCAL_DTYPE,
                            device=args.device, batch_size=args.fwd_batch)
        print(f"[lm] {C.LOCAL_PRIMARY} on {_LM['lm'].device} ({C.LOCAL_DTYPE})", flush=True)
    return _LM["lm"]


def load_notes(out) -> dict:
    return {(r["episode_id"], r["session_idx"]): r["note"] for r in P.read_jsonl(out / "notes.jsonl")}


# =================================================================================================
# batched local generation with retries (shared by notes, T2, candidates)
# =================================================================================================
def run_generation(lm, jobs, out_path, *, tag, batch_size, temperature, check, max_attempts, make_row,
                   desc=""):
    """``jobs``: ordered list of dicts with 'key' and 'messages'. Batches are fixed slices of the
    full job list (batch b = jobs[b*bs:(b+1)*bs]), so a resumed run reproduces the same batch
    composition and seed (seed = stable_hash(tag, b)). Jobs whose output fails ``check`` (returns a
    problem string) are regenerated as a group with seed stable_hash(tag, b, attempt).
    ``make_row(job, note, raw, flags, attempts, problem, seed)`` builds the output row."""
    done = {r["_key"] for r in P.read_jsonl(out_path) if "_key" in r}
    n_b = (len(jobs) + batch_size - 1) // batch_size
    t0, n_new, n_gen = time.time(), 0, 0
    for b in range(n_b):
        batch = jobs[b * batch_size:(b + 1) * batch_size]
        todo = [j for j in batch if j["key"] not in done]
        if not todo:
            continue
        state = {}
        pending = list(batch)              # first attempt: full batch (fixed composition)
        for a in range(1, max_attempts + 1):
            seed = stable_hash(tag, b) % SEED_MOD if a == 1 else stable_hash(tag, b, a) % SEED_MOD
            outs = lm.generate([j["messages"] for j in pending], max_new_tokens=MAX_NEW_TOKENS,
                               temperature=temperature, seed=seed, batch_size=batch_size)
            n_gen += len(pending)
            for j, raw in zip(pending, outs):
                note, flags = P.clean_note(raw)
                ntok = len(lm._encode(raw))
                prob = check(j, note, ntok)
                state[j["key"]] = (note, raw, flags, a, prob, seed)
            pending = [j for j in pending if state[j["key"]][4] is not None and j["key"] not in done]
            if not pending:
                break
        rows = []
        for j in todo:
            note, raw, flags, a, prob, seed = state[j["key"]]
            r = make_row(j, note, raw, flags, a, prob, seed)
            r["_key"] = j["key"]
            r["batch"] = b
            rows.append(r)
        P.append_jsonl(out_path, rows)
        n_new += len(rows)
        el = time.time() - t0
        print(f"[{desc}] batch {b + 1}/{n_b}  written {n_new}  generated {n_gen}  "
              f"{n_gen / el:.2f} gen/s  {n_new / el:.2f} rows/s", flush=True)
    return n_new, n_gen, time.time() - t0


# =================================================================================================
# stage: notes
# =================================================================================================
def stage_notes(args):
    out, _, eps, main, style = setup(args)
    lm = get_lm(args)
    jobs = []
    for e in main + style:   # main first: partial results are useful
        ep = eps[e]
        for s in range(len(ep.sessions)):
            jobs.append({"key": f"{e}|{s}", "episode_id": e, "session_idx": s,
                         "messages": P.messages(note_writing(ep, s, with_trace=True, as_json=False))})

    def check(j, note, ntok):
        return P.note_problem(note, ntok, MAX_NEW_TOKENS)

    def make_row(j, note, raw, flags, a, prob, seed):
        return {"episode_id": j["episode_id"], "session_idx": j["session_idx"], "note": note, "attempts": a,
                "problem": prob, "flags": flags, "raw": raw, "seed": seed}

    n, g, el = run_generation(lm, jobs, out / "notes.jsonl", tag="notes", batch_size=args.gen_batch,
                              temperature=C.NOTE_TEMPERATURE, check=check, max_attempts=MAX_ATTEMPTS,
                              make_row=make_row, desc="notes")
    log_timing(out, "notes", n, g, el)
    report_notes(out)


def report_notes(out):
    rows = P.read_jsonl(out / "notes.jsonl")
    if not rows:
        return
    att = Counter(r["attempts"] for r in rows)
    fl = Counter(k for r in rows for k, v in r["flags"].items() if v)
    pr = Counter(r["problem"] for r in rows if r["problem"])
    nsent = [len([x for x in __import__("re").split(r"(?<=[.!?])\s+", r["note"]) if x]) for r in rows]
    print(f"[notes] n={len(rows)} attempts={dict(att)} final_problems={dict(pr)} cleanup_flags={dict(fl)} "
          f"mean_chars={np.mean([len(r['note']) for r in rows]):.0f} sentences={dict(Counter(nsent))}")


def log_timing(out, stage, n_rows, n_items, seconds, **extra):
    P.append_jsonl(out / "timing.jsonl", [{"stage": stage, "rows": n_rows, "items": n_items, "seconds": round(seconds, 2),
                                           "items_per_s": round(n_items / seconds, 4) if seconds > 0 else None,
                                           "time": time.strftime("%Y-%m-%d %H:%M:%S"), **extra}])


# =================================================================================================
# stage: hosted (Adaption API)
# =================================================================================================
def _parse_note(text):
    from memlab.utils.jsonparse import parse_json
    d = parse_json(text)
    if isinstance(d, dict) and isinstance(d.get("note"), str) and d["note"].strip():
        return {"note": d["note"]}
    return None


def stage_hosted(args):
    from memlab.clients import AdaptionClient, Job, run
    from memlab.clients import adaption as AD   # STUDY_EXTRA / STUDY_MAX_OUTPUT_TOKENS read at run time
    out, _, eps, main, style = setup(args)
    rpm = {k: v * args.rpm_scale for k, v in AD.DEFAULT_RPM_PER_KEY.items()}
    probe = AdaptionClient(per_key_concurrency=args.api_concurrency, rpm_per_key=rpm)
    start_spend = probe.total_spend()
    cap = start_spend + args.max_spend

    def client():
        return AdaptionClient(per_key_concurrency=args.api_concurrency, rpm_per_key=rpm, budget_cap=cap)

    def mot(m):   # the study's hosted setting (reasoning off unless MEMLAB_REASONING=low)
        return AD.STUDY_EXTRA.get(m), int(getattr(AD, "STUDY_MAX_OUTPUT_TOKENS", 1024))

    inst = P.instances(main)

    t0 = time.time()
    # (a) other-model notes
    if "other" in args.parts:
        jobs = []
        for m in C.LOCAL_OTHER_MODELS:
            extra, mo = mot(m)
            for e, et in inst:   # target slots of the study instances only
                ep = eps[e]
                s = ep.edits[et].session_idx
                if True:
                    ins, inp = note_writing(ep, s, with_trace=True, as_json=True)
                    jobs.append(Job(job_id=f"other|{m}|{e}|s{s}", model=m, input=inp, instructions=ins,
                                    max_output_tokens=mo, temperature=C.NOTE_TEMPERATURE, sample_idx=0,
                                    tag="local_other_notes", meta={"episode_id": e, "session_idx": s},
                                    extra=extra))
        rows = run(client(), jobs, out / "hosted_raw_other.jsonl", parse=_parse_note, desc="other notes")
        derived, fails = [], Counter()
        for r in rows:
            if r.get("error") or not r.get("parsed"):
                fails[r["model"]] += 1
                continue
            note, flags = P.clean_note(r["parsed"]["note"])
            derived.append({"episode_id": r["meta"]["episode_id"], "session_idx": r["meta"]["session_idx"],
                            "model": r["model"], "note": note, "flags": flags})
        P.write_jsonl_atomic(out / "other_notes.jsonl", derived)
        print(f"[hosted] other notes: {len(derived)}/{len(jobs)} ok, failures {dict(fails)}")

    # (b) T1 forgeries
    if "t1" in args.parts:
        notes = load_notes(out)
        m = C.LOCAL_T1_FORGER
        extra, mo = mot(m)
        insts = [(e, et) for e, et in inst if (e, eps[e].edits[et].session_idx) in notes]
        n_skip = len(inst) - len(insts)
        if n_skip:
            print(f"[hosted] T1: {n_skip} instances skipped (victim note missing; run `notes` first, then re-run)")
        raw_path = out / "hosted_raw_t1.jsonl"
        best = {}
        for a in range(MAX_ATTEMPTS):
            jobs = []
            for (e, et) in insts:
                if best.get((e, et), {}).get("valid"):
                    continue
                edit = eps[e].edits[et]
                ins, inp = forge_t1(notes[(e, edit.session_idx)], edit, as_json=True)
                jobs.append(Job(job_id=f"t1|{e}|{et}|a{a}", model=m, input=inp, instructions=ins,
                                max_output_tokens=mo, temperature=C.FORGE_TEMPERATURE, sample_idx=a,
                                tag="local_t1", meta={"episode_id": e, "edit_type": et, "attempt": a},
                                extra=extra))
            if not jobs:
                break
            rows = run(client(), jobs, raw_path, parse=_parse_note, desc=f"T1 attempt {a + 1}")
            for r in rows:
                key = (r["meta"]["episode_id"], r["meta"]["edit_type"])
                note = P.clean_note(r["parsed"]["note"])[0] if (r.get("parsed") and not r.get("error")) else ""
                edit = eps[key[0]].edits[key[1]]
                valid = bool(note) and is_valid_forgery(note, edit)
                prev = best.get(key)
                if prev is None or (valid and not prev["valid"]) or (not prev["note"] and note):
                    best[key] = {"note": note, "valid": valid, "attempts": a + 1}
                else:
                    prev["attempts"] = a + 1
        derived = []
        for (e, et) in insts:
            b = best.get((e, et))
            if b is None:
                continue
            derived.append({"item_id": P.fid("T1", e, et), "episode_id": e, "edit_type": et,
                            "session_idx": eps[e].edits[et].session_idx, "tier": "T1", "note": b["note"],
                            "valid": b["valid"], "mode": "rewrite", "attempts": b["attempts"], "model": m})
        P.write_jsonl_atomic(out / "forged_t1.jsonl", derived)
        nv = sum(d["valid"] for d in derived)
        print(f"[hosted] T1: {nv}/{len(derived)} valid; attempts {dict(Counter(d['attempts'] for d in derived))}")
    end = AdaptionClient(per_key_concurrency=1).total_spend()
    print(f"[hosted] ledger total rose by ${end - start_spend:.4f} during this run (includes any concurrent "
          f"processes); cumulative spend of local_* tags: ${local_spend():.4f}  ({time.time() - t0:.0f}s)")


def local_spend() -> float:
    import csv
    from memlab.clients.adaption import DEFAULT_LEDGER_PATH
    tot = 0.0
    try:
        with open(DEFAULT_LEDGER_PATH) as f:
            for r in csv.reader(f):
                if len(r) > 3 and r[3].startswith("local_"):
                    try:
                        tot += float(r[-1])
                    except ValueError:
                        pass
    except FileNotFoundError:
        pass
    return tot


# =================================================================================================
# stage: forge (T0, T2, candidates)
# =================================================================================================
def stage_forge(args):
    out, _, eps, main, style = setup(args)
    notes = load_notes(out)
    need = [(e, s) for e in main + style for s in range(len(eps[e].sessions))]
    miss = [k for k in need if k not in notes]
    if miss:
        sys.exit(f"forge: {len(miss)} genuine notes missing (e.g. {miss[:3]}); finish `notes` first")
    style_notes = P.style_pool(notes, style)
    fpath = out / "forged.jsonl"
    have = {(r["tier"], r["episode_id"], r["edit_type"]) for r in P.read_jsonl(fpath)}

    # (a) T0
    rows = []
    inst = P.instances(main)
    for e, et in inst:
        if True:
            if ("T0", e, et) in have:
                continue
            edit = eps[e].edits[et]
            g = notes[(e, edit.session_idx)]
            forged, mode = apply_t0(g, edit)
            rows.append({"item_id": P.fid("T0", e, et), "episode_id": e, "edit_type": et,
                         "session_idx": edit.session_idx, "tier": "T0", "note": forged,
                         "valid": is_valid_forgery(forged, edit), "mode": mode, "attempts": 1})
    P.append_jsonl(fpath, rows)
    if rows:
        print(f"[forge] T0: {sum(r['valid'] for r in rows)}/{len(rows)} valid; modes {dict(Counter(r['mode'] for r in rows))}")

    if args.t0_only:
        return
    lm = get_lm(args)

    def t2_messages(e, et):
        ep = eps[e]
        edit = ep.edits[et]
        ex = P.style_examples(e, et, ep.family, style_notes)
        return P.messages(forge_t2(notes[(e, edit.session_idx)], edit, ex, as_json=False))

    # (b) T2 (keys reuse the forged.jsonl rows: _key = "T2|ep|et")
    jobs = [{"key": P.fid("T2", e, et), "episode_id": e, "edit_type": et, "messages": t2_messages(e, et)}
            for e, et in inst]

    def check_t2(j, note, ntok):
        p = P.note_problem(note, ntok, MAX_NEW_TOKENS)
        if p:
            return p
        return None if is_valid_forgery(note, eps[j["episode_id"]].edits[j["edit_type"]]) else "invalid"

    def row_t2(j, note, raw, flags, a, prob, seed):
        e, et = j["episode_id"], j["edit_type"]
        return {"item_id": j["key"], "episode_id": e, "edit_type": et, "session_idx": eps[e].edits[et].session_idx,
                "tier": "T2", "note": note, "valid": is_valid_forgery(note, eps[e].edits[et]) if note else False,
                "mode": "rewrite", "attempts": a, "problem": prob, "flags": flags, "raw": raw, "seed": seed}

    n, g, el = run_generation(lm, jobs, fpath, tag="T2", batch_size=args.gen_batch,
                              temperature=C.FORGE_TEMPERATURE, check=check_t2, max_attempts=MAX_ATTEMPTS,
                              make_row=row_t2, desc="T2")
    log_timing(out, "forge_T2", n, g, el)

    # (c) adaptive candidates: 8 per (episode, t3 edit type); consecutive in the job list, so an
    #     instance's candidates share a batch and each row draws its own sample (distinct RNG draws).
    jobs = []
    for e, et in inst:
        if True:
            m = t2_messages(e, et)
            for k in range(C.T3_N_CANDIDATES):
                jobs.append({"key": P.cid(e, et, k), "episode_id": e, "edit_type": et, "cand_idx": k, "messages": m})

    def row_c(j, note, raw, flags, a, prob, seed):
        e, et = j["episode_id"], j["edit_type"]
        return {"item_id": j["key"], "episode_id": e, "edit_type": et, "session_idx": eps[e].edits[et].session_idx,
                "cand_idx": j["cand_idx"], "note": note,
                "valid": bool(note) and is_valid_forgery(note, eps[e].edits[et]),
                "problem": P.note_problem(note, len(lm._encode(raw)), MAX_NEW_TOKENS), "flags": flags,
                "raw": raw, "seed": seed}

    n, g, el = run_generation(lm, jobs, out / "candidates.jsonl", tag="cand", batch_size=args.gen_batch,
                              temperature=C.T3_TEMPERATURE, check=lambda j, n_, t: None, max_attempts=1,
                              make_row=row_c, desc="cand")
    log_timing(out, "forge_cand", n, g, el)
    report_forge(out)


def report_forge(out):
    f = P.read_jsonl(out / "forged.jsonl") + P.read_jsonl(out / "forged_t1.jsonl")
    for tier in ("T0", "T1", "T2"):
        rs = [r for r in f if r["tier"] == tier]
        if rs:
            print(f"[forge] {tier}: valid {sum(bool(r['valid']) for r in rs)}/{len(rs)}  attempts "
                  f"{dict(Counter(r.get('attempts') for r in rs))}  flags "
                  f"{dict(Counter(k for r in rs for k, v in (r.get('flags') or {}).items() if v))}")
    c = P.read_jsonl(out / "candidates.jsonl")
    if c:
        print(f"[forge] cand: valid {sum(r['valid'] for r in c)}/{len(c)}  problems "
              f"{dict(Counter(r['problem'] for r in c if r['problem']))}  flags "
              f"{dict(Counter(k for r in c for k, v in (r.get('flags') or {}).items() if v))}")


# =================================================================================================
# stage: items
# =================================================================================================
def stage_items(args):
    out, _, eps, main, style = setup(args)
    notes = load_notes(out)
    forged = P.read_jsonl(out / "forged.jsonl") + P.read_jsonl(out / "forged_t1.jsonl")
    items, missing = P.build_items(eps, main, notes, forged, P.read_jsonl(out / "candidates.jsonl"),
                                   P.read_jsonl(out / "other_notes.jsonl"))
    P.write_jsonl_atomic(out / "items.jsonl", items)
    cnt = Counter(it["kind"] for it in items)
    npass = sum(len(it["passes"]) for it in items)
    print(f"[items] {len(items)} items, {npass} (item, pass) forward jobs: {dict(cnt)}")
    if missing:
        print(f"[items] NOT registered (missing/empty, re-run upstream stage then `items`): {missing}")


# =================================================================================================
# stage: score
# =================================================================================================
class ScoreBuffer:
    """Buffers rows and activations; flush order: activation shard -> act index -> tokens -> scores,
    so a score row on disk implies its activations are on disk."""

    def __init__(self, out, acts):
        self.out, self.acts = out, acts
        self.scores, self.tokens, self.act = [], [], {p: [] for p in P.ACT_PASSES}
        self.layers = None

    def __len__(self):
        return len(self.scores)

    def flush(self):
        if not self.scores:
            return
        from memlab.local.model import save_npz
        idx_rows = []
        for p, rows in self.act.items():
            if not rows:
                continue
            name = f"{p}/shard_{time.time_ns()}"
            save_npz(self.acts / name, meta={"pass": p, "layers": self.layers, "item_ids": [r[0] for r in rows]},
                     mean=np.stack([r[2] for r in rows]), last=np.stack([r[3] for r in rows]))
            idx_rows += [{"pass": p, "item_id": r[0], "note_sha": r[1], "shard": name + ".npz", "row": i}
                         for i, r in enumerate(rows)]
        P.append_jsonl(self.acts / "index.jsonl", idx_rows)
        P.append_jsonl(self.out / "surprisal_tokens.jsonl.gz", self.tokens)
        P.append_jsonl(self.out / "scores.jsonl", self.scores)
        self.scores, self.tokens, self.act = [], [], {p: [] for p in P.ACT_PASSES}


def mps_gb() -> float:
    try:
        import torch
        if torch.backends.mps.is_available():
            return torch.mps.driver_allocated_memory() / 1e9
    except Exception:
        pass
    return 0.0


class MemoryAbort(RuntimeError):
    pass


def compute_selection(out) -> list:
    """Rule-based tier selection from the scores on disk; writes selected.jsonl (keeps other tiers)."""
    df = P.load_scores(out)
    cand = df[df["kind"] == "cand"].to_dict("records")
    rows = P.select_all(cand)
    keep = [r for r in P.read_jsonl(out / "selected.jsonl") if r["tier"] not in set(P.RULE_TIERS)]
    P.write_jsonl_atomic(out / "selected.jsonl", keep + rows)
    return rows


def stage_score(args):
    """Pass-major scoring: s_trace -> s_blind -> c -> v_att -> v; within a pass kinds in KIND_ORDER.
    Before pass v, `select` runs on the scores on disk and v is computed for the selected candidates."""
    out, acts, eps, main, style = setup(args)
    items = P.load_items(out)
    if not items:
        sys.exit("score: items.jsonl missing; run `items` first")
    notes = load_notes(out)
    kinds = set(args.kinds) if args.kinds else None
    passes = [p for p in P.PASSES if not args.passes or p in args.passes]
    lm = None
    layers = yes_ids = no_ids = None
    buf = ScoreBuffer(out, acts)
    stats = defaultdict(lambda: {"n": 0, "s": 0.0, "prompt_tok": 0, "computed_tok": 0})
    t_start = time.time()
    n_done = 0
    peak = [0.0]
    budget = args.max_batch_tokens

    def record_act(p, it, sur, ma, la, plen):
        a = np.asarray(sur, dtype=np.float64)
        st = ({"mean": float(a.mean()), "max": float(a.max()), "min": float(a.min()), "sum": float(a.sum()),
               "n": int(a.size)} if a.size else {"mean": None, "max": None, "min": None, "sum": 0.0, "n": 0})
        buf.scores.append({"item_id": it["item_id"], "pass": p, "note_sha": it["note_sha"], **st, "prompt_tok": plen})
        buf.tokens.append({"item_id": it["item_id"], "pass": p, "note_sha": it["note_sha"],
                           "s": [round(float(x), 3) for x in sur]})
        buf.act[p].append((it["item_id"], it["note_sha"], np.asarray(ma, dtype=np.float16),
                           np.asarray(la, dtype=np.float16)))

    def check_mem(where):
        from memlab.local.model import free_memory
        free_memory()
        gb = mps_gb()
        peak[0] = max(peak[0], gb)
        if gb > args.max_mem_gb:
            raise MemoryAbort(f"MPS driver memory {gb:.1f} GB > {args.max_mem_gb} GB at {where}; aborting "
                              "instead of swapping (finished work is on disk; lower --max-batch-tokens / "
                              "--groups-per-batch or use --no-prefix-cache, then re-run to resume)")
        return gb

    def windows(eg_pids):
        """Split [(ep, group, prompt_ids_list)] into sub-batches with <= budget padded prefix tokens
        and <= groups_per_batch groups."""
        cur, cur_max = [], 0
        for x in eg_pids:
            L = max(len(s) for s in x[2])
            m = max(cur_max, L)
            if cur and (len(cur) + 1 > args.groups_per_batch or (len(cur) + 1) * m > budget):
                yield cur
                cur, m = [], L
            cur.append(x)
            cur_max = m
        if cur:
            yield cur

    def run_window(p, win):
        t = time.time()
        ptok = comp = n = 0
        if p in P.ACT_PASSES:
            pids = [x[2][0] for x in win]
            conts = [[lm._encode(it["note"]) for it in g] for _, g, _ in win]
            if args.no_prefix_cache:
                for (ep, g, _), pid, cs in zip(win, pids, conts):
                    msgs = P.pass_prompt(p, g[0], ep, P.genuine_store(notes, ep))
                    bs = max(1, min(args.fwd_batch, budget // max(1, len(pid) + max(len(c) for c in cs))))
                    sc, ac = lm.score_and_activations([msgs] * len(g), [it["note"] for it in g], layers=layers,
                                                      batch_size=bs)
                    for i, (it, s) in enumerate(zip(g, sc)):
                        record_act(p, it, s["surprisal"], ac["mean"][i], ac["last"][i], len(pid))
                    comp += sum(len(pid) + len(c) for c in cs)
                    del sc, ac
            else:
                res = P.score_multi(lm, list(zip(pids, conts)), layers, rows_per_chunk=args.prefix_chunk,
                                    max_tokens=budget)
                for (ep, g, _), pid, cs, rr in zip(win, pids, conts, res):
                    for it, (sur, ma, la) in zip(g, rr):
                        record_act(p, it, sur, ma, la, len(pid))
                    comp += len(pid) - 1 + sum(1 + len(c) for c in cs)
                del res
            for (ep, g, _), pid, cs in zip(win, pids, conts):
                ptok += len(pid) * len(g) + sum(len(c) for c in cs)
                n += len(g)
        else:
            seqs = [x[2] for x in win]
            if args.no_prefix_cache:
                res = []
                for (ep, g, _), ss in zip(win, seqs):
                    msgs = [P.pass_prompt(p, it, ep, P.genuine_store(notes, ep)) for it in g]
                    bs = max(1, min(args.fwd_batch, budget // max(len(x) for x in ss)))
                    res.append(lm.p_yes(msgs, return_mass=True, batch_size=bs))
                comp = sum(len(x) for ss in seqs for x in ss)
            else:
                res, Ls = P.pyes_multi(lm, seqs, yes_ids, no_ids, rows_per_chunk=args.prefix_chunk, max_tokens=budget)
                comp = sum(L + sum(len(x) - L for x in ss) for L, ss in zip(Ls, seqs))
            for (ep, g, _), rr, ss in zip(win, res, seqs):
                for it, r, x in zip(g, rr, ss):
                    buf.scores.append({"item_id": it["item_id"], "pass": p, "note_sha": it["note_sha"], **r,
                                       "prompt_tok": len(x)})
                ptok += sum(len(x) for x in ss)
                n += len(g)
        st = stats[p]
        st["n"] += n
        st["s"] += time.time() - t
        st["prompt_tok"] += ptok
        st["computed_tok"] += comp
        return n

    try:
        for p in passes:
            done = {(r["pass"], r["item_id"], r["note_sha"]) for r in P.read_jsonl(out / "scores.jsonl")}
            sel = set()
            if p == "v":
                buf.flush()
                if any(it["kind"] == "cand" for it in items):
                    rows = compute_selection(out)
                    sel = set(P.selected_ids(rows))
                    # probe-selected candidates (T4p) are appended later by analysis.local; a rerun of this
                    # pass then also scores them
                    sel |= set(P.selected_ids(P.read_jsonl(out / "selected.jsonl"), tiers=("T4p",)))
                    print(f"[score] select before pass v: {len(sel)} distinct selected candidates "
                          f"({sum(r['item_id'] is None for r in rows)} empty tier slots)", flush=True)
            todo = [it for (q, it) in P.score_todo(items, done, sel)
                    if q == p and (kinds is None or P.kind_base(it["kind"]) in kinds)]
            if not todo:
                print(f"[score] pass {p}: nothing to do", flush=True)
                continue
            if lm is None:
                lm = get_lm(args)
                layers = lm.resolve_layers("auto")
                buf.layers = layers
                yes_ids = lm._variant_ids(("Yes", "yes", " Yes"))
                no_ids = lm._variant_ids(("No", "no", " No"))
            print(f"[score] pass {p}: {len(todo)} items  (mps {check_mem('start ' + p):.1f} GB)", flush=True)
            for kind in P.KIND_ORDER:
                kit = [it for it in todo if P.kind_base(it["kind"]) == kind]
                if not kit:
                    continue
                eg = []
                for (e, s), g in P.score_groups(kit, main):
                    ep = eps[e]
                    store = P.genuine_store(notes, ep)
                    if p in P.ACT_PASSES:
                        pid = lm._prompt_ids(P.pass_prompt(p, g[0], ep, store))
                        eg.append((ep, g, [pid]))
                    else:
                        eg.append((ep, g, [lm._prompt_ids(P.pass_prompt(p, it, ep, store)) for it in g]))
                for win in windows(eg):
                    n_done += run_window(p, win)
                    if len(buf) >= args.flush_every:
                        buf.flush()
                        gb = check_mem(f"{p}/{kind}")
                        el = time.time() - t_start
                        v = stats[p]
                        print(f"[score] {p}/{kind}: {n_done} jobs  {p} {v['n'] / v['s']:.2f}/s  mps {gb:.1f} GB "
                              f"(peak {peak[0]:.1f})  {el / 60:.1f} min", flush=True)
                    if args.max_items and n_done >= args.max_items:
                        raise StopIteration
                buf.flush()
                print(f"[score] {p}/{kind} done: {len(kit)} items  mps {check_mem(p + '/' + kind):.1f} GB", flush=True)
    except StopIteration:
        print(f"[score] stopping after --max-items {args.max_items}")
    finally:
        buf.flush()
        el = time.time() - t_start
        summ = {p: {"items": v["n"], "seconds": round(v["s"], 1),
                    "items_per_s": round(v["n"] / v["s"], 3) if v["s"] else None,
                    "mean_prompt_tok": round(v["prompt_tok"] / v["n"], 1) if v["n"] else None,
                    "mean_computed_tok": round(v["computed_tok"] / v["n"], 1) if v["n"] else None}
                for p, v in stats.items()}
        log_timing(out, "score", n_done, n_done, el, passes=summ, prefix_cache=not args.no_prefix_cache,
                   peak_mps_gb=round(peak[0], 2), kinds=sorted(kinds) if kinds else None)
        print(f"[score] finished {n_done} jobs in {el:.0f}s; peak mps {peak[0]:.1f} GB; per pass: {json.dumps(summ)}",
              flush=True)


# =================================================================================================
# stage: external baselines
# =================================================================================================
def stage_external(args):
    out, _, eps, main, style = setup(args)
    from memlab.local.model import MODELS, PlainLM, free_memory
    items = [it for it in P.load_items(out) if it["kind"] != "xep"]
    done = {(r["item_id"], r["note_sha"]) for r in P.read_jsonl(out / "external.jsonl")}
    todo = [it for it in items if (it["item_id"], it["note_sha"]) not in done]
    print(f"[external] {len(todo)} items to do", flush=True)
    if not todo:
        return
    t0 = time.time()
    gpt2 = PlainLM(C.LOCAL_GPT2, revision=MODELS["gpt2"]["revision"], device="cpu", dtype="fp32", batch_size=16)
    small = PlainLM(C.LOCAL_SECONDARY, revision=C.LOCAL_SECONDARY_REVISION, device=args.device, dtype="fp16",
                    batch_size=16)
    for s in range(0, len(todo), 128):
        ch = todo[s:s + 128]
        texts = [it["note"] for it in ch]
        g = gpt2.perplexity(texts)
        a = small.perplexity(texts)
        ctx = [render_session(eps[it["episode_id"]].sessions[it["session_idx"]]) + "\n\n" for it in ch]
        b = small.perplexity(texts, contexts=ctx)
        P.append_jsonl(out / "external.jsonl", [
            {"item_id": it["item_id"], "note_sha": it["note_sha"], "gpt2_mean": x["mean"], "gpt2_n": x["n"],
             "small_mean": y["mean"], "small_n": y["n"], "small_trace_mean": z["mean"]}
            for it, x, y, z in zip(ch, g, a, b)])
        print(f"[external] {s + len(ch)}/{len(todo)}  {(s + len(ch)) / (time.time() - t0):.1f} items/s", flush=True)
        free_memory()
    log_timing(out, "external", len(todo), len(todo), time.time() - t0)


# =================================================================================================
# stage: select
# =================================================================================================
def stage_select(args):
    out, _, eps, main, style = setup(args)
    rows = compute_selection(out)   # keeps tiers added later by analysis code (e.g. T4p)
    by = defaultdict(lambda: [0, 0])
    for r in rows:
        by[r["tier"]][0] += 1
        by[r["tier"]][1] += r["item_id"] is not None
    print("[select] " + "  ".join(f"{t}: {v[1]}/{v[0]}" for t, v in by.items()))


# =================================================================================================
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("stage", choices=["notes", "hosted", "forge", "items", "score", "external", "select", "report"])
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    ap.add_argument("--acts", default=str(DEFAULT_ACTS))
    ap.add_argument("--limit-episodes", type=int, default=None, help="first N main and N style seeds per family")
    ap.add_argument("--device", default="mps")
    ap.add_argument("--gen-batch", type=int, default=16)
    ap.add_argument("--fwd-batch", type=int, default=8)
    ap.add_argument("--prefix-chunk", type=int, default=16, help="continuation rows per forward after the cached prefixes")
    ap.add_argument("--max-batch-tokens", type=int, default=6000, help="max padded tokens per forward (prefix batch or continuation chunk)")
    ap.add_argument("--max-mem-gb", type=float, default=16.0, help="abort scoring if MPS driver memory exceeds this")
    ap.add_argument("--groups-per-batch", type=int, default=8, help="prompt groups whose prefixes run as one batch")
    ap.add_argument("--no-prefix-cache", action="store_true", help="score without shared-prefix KV caching")
    ap.add_argument("--kinds", nargs="*", help="score only these kinds (genuine T0 T1 T2 cand other xep)")
    ap.add_argument("--passes", nargs="*", help="score only these passes")
    ap.add_argument("--max-items", type=int, default=0, help="score: stop after ~N (pass,item) jobs")
    ap.add_argument("--flush-every", type=int, default=64)
    ap.add_argument("--parts", nargs="*", default=["other", "t1"], help="hosted: other t1")
    ap.add_argument("--api-concurrency", type=int, default=4)
    ap.add_argument("--rpm-scale", type=float, default=1.0, help="hosted: fraction of the per-key RPM budget")
    ap.add_argument("--max-spend", type=float, default=2.0, help="hosted: USD cap for this process")
    ap.add_argument("--t0-only", action="store_true")
    args = ap.parse_args(argv)
    import signal   # SIGTERM -> SystemExit so buffered rows are flushed by the stages' finally blocks
    signal.signal(signal.SIGTERM, lambda *_: sys.exit(143))
    if args.stage == "report":
        out = Path(args.out)
        report_notes(out)
        report_forge(out)
        return
    {"notes": stage_notes, "hosted": stage_hosted, "forge": stage_forge, "items": stage_items,
     "score": stage_score, "external": stage_external, "select": stage_select}[args.stage](args)


if __name__ == "__main__":
    main()
