"""Stage `hosted_gen`: genuine notes, re-derivations and the forger ladder T0-T3 for hosted victims.

Specification: experiments/README.md, section "Stage `hosted_gen`" and "Common rules".

    python -m experiments.hosted_gen --run pilot|main [--victims a,b] [--stages notes,rederive,forge] [--limit N]

Sub-stages
    notes     genuine notes (run seeds) and style notes (style seeds), sample_idx 0
    rederive  the same prompt at sample_idx 1, run seeds only
    forge     T0 (template), T1 (other-family forger), T2 (victim, style examples),
              T3 (victim, 4 calls x 2 rewrites, then one ranking call per instance)

Each sub-stage builds a list of `Job`s for all requested victims, runs them through the resumable
runner (one `run_jobs` per victim and parser, all victims concurrently on one client, so the global
rate limit is shared), and writes tidy outputs to `proc_dir(run, victim)`. Raw rows of all sub-stages go
to `raw_dir(run, victim) / "hosted_gen.jsonl"`; job ids encode the sub-stage.
"""
from __future__ import annotations

import argparse
import asyncio
import hashlib
import statistics
import sys
from collections import Counter, OrderedDict, defaultdict
from functools import partial
from typing import Optional

from memlab import data
from memlab.attacks.template import apply_t0, is_valid_forgery
from memlab.clients.jobs import Job, load_rows, run_jobs
from memlab.config import (FORGE_TEMPERATURE, N_STYLE_EXAMPLES, NOTE_TEMPERATURE, QUERY_TEMPERATURE, RUNS, T3_CALLS,
                           T3_TEMPERATURE, T3_VERSIONS_PER_CALL, t1_forger_for)
from memlab.prompts import (forge_packed, note_writing, parse_forged, parse_keyed_ints, parse_note,
                            rate_candidates)
from memlab.schema import EDIT_TYPES, stable_hash

STAGE = "hosted_gen"
SUBSTAGES = ("notes", "rederive", "forge")
MAX_VALIDITY_RETRIES = 3          # T1/T2: up to 3 re-asks of the episode's packed call
FORGE_TIERS = ("T0", "T1", "T2", "T3")


class StageInputMissing(RuntimeError):
    """A sub-stage needs outputs of an earlier sub-stage that do not exist."""


# ====================================================================================== study settings
def _study_settings():
    """Imported lazily so that offline tests work even before the client exports them."""
    from memlab.clients.adaption import STUDY_EXTRA, STUDY_MAX_OUTPUT_TOKENS
    return STUDY_EXTRA, STUDY_MAX_OUTPUT_TOKENS


# ====================================================================================== jobs & parsing
def jid(victim: str, episode_id: str, *parts) -> str:
    return "|".join([STAGE, victim, episode_id, *(str(p) for p in parts)])


def parser_for(pkey) -> callable:
    """pkey (stored in job meta): ["note"] | ["forged", n, n_versions] | ["ratings", n]."""
    kind = pkey[0]
    if kind == "note":
        return parse_note
    if kind == "forged":
        return partial(parse_forged, n=int(pkey[1]), n_versions=int(pkey[2]))
    if kind == "ratings":
        return partial(parse_keyed_ints, field="ratings", n=int(pkey[1]))
    raise ValueError(pkey)


def make_job(run: str, model: str, job_id: str, prompt: tuple, temperature: float, sample_idx: int,
             pkey: list, meta: dict) -> Job:
    extra, max_out = _study_settings()
    ex = extra[model]
    if pkey[0] in ("forged", "ratings"):
        # The forger pipeline (rewrites, candidate ranking) runs with reasoning off: packed rewrite calls
        # with reasoning exhausted the output budget in the pilot (DECISIONS.md, 14 Nov). The attacker is
        # free to choose its own settings; genuine notes and all judgement calls keep reasoning on.
        from memlab.clients.adaption import MODEL_DEFAULTS
        ex, max_out = MODEL_DEFAULTS[model]["extra"], 8192
    instructions, inp = prompt
    return Job(job_id=job_id, model=model, input=inp, instructions=instructions, max_output_tokens=max_out,
               temperature=temperature, sample_idx=sample_idx, tag=f"{run}:{STAGE}",
               meta={**meta, "pkey": list(pkey)}, extra=ex)


def _h(s) -> str:
    return hashlib.sha1(repr(s).encode("utf-8")).hexdigest()[:16]


def parsed_of(row: Optional[dict]):
    """`parsed` of a raw row with integer keys restored (rows read back from JSONL have string keys)."""
    p = row.get("parsed") if row else None
    if isinstance(p, dict) and p and all(str(k).isdigit() for k in p):
        return {int(k): v for k, v in p.items()}
    return p


def raw_path(run: str, victim: str):
    return data.raw_dir(run, victim) / f"{STAGE}.jsonl"


async def run_all(client, jobs_by_victim: dict, run: str, label: str) -> dict:
    """Run every victim's jobs concurrently on one client. Within a victim, jobs are grouped by parser
    (the runner takes one `parse` per call) and the groups run one after another (same raw file).
    Returns {victim: {job_id: row}}; rows that ended in an API error are left out (= missing)."""
    reg = getattr(client, "kind_of", None)
    if reg is not None:
        for js in jobs_by_victim.values():
            for j in js:
                reg[(j.model, _h(j.input), j.sample_idx)] = j.meta.get("kind", label)

    async def one(victim, jobs):
        groups: "OrderedDict[tuple, list]" = OrderedDict()
        for j in jobs:
            groups.setdefault(tuple(j.meta["pkey"]), []).append(j)
        out = {}
        for pkey, js in groups.items():
            rows = await run_jobs(client, js, raw_path(run, victim), parse=parser_for(pkey),
                                  desc=f"{label} {victim} {'/'.join(map(str, pkey))}")
            out.update({r["job_id"]: r for r in rows if not r.get("error")})
        return victim, out

    res = await asyncio.gather(*(one(v, js) for v, js in jobs_by_victim.items() if js))
    out = {v: {} for v in jobs_by_victim}
    out.update(dict(res))
    return out


# ====================================================================================== episodes
def limited(eps: list, limit: Optional[int]) -> list:
    if not limit:
        return eps
    seen = Counter()
    out = []
    for ep in eps:
        if seen[ep.family] < limit:
            out.append(ep)
            seen[ep.family] += 1
    return out


def episodes_for(run: str, victim: str, what: str, limit: Optional[int]) -> list:
    return limited(data.run_episodes(run, victim, what), limit)


# ====================================================================================== sub-stage: notes
def note_jobs(run: str, victim: str, eps: list, sample_idx: int, kind: str) -> list:
    jobs = []
    for ep in eps:
        for s in range(len(ep.sessions)):
            jobs.append(make_job(run, victim, jid(victim, ep.episode_id, "note", f"s{s}", f"k{sample_idx}"),
                                 note_writing(ep, s), NOTE_TEMPERATURE, sample_idx, ["note"],
                                 {"kind": kind, "episode_id": ep.episode_id, "session_idx": s,
                                  "sample_idx": sample_idx}))
    return jobs


def collect_notes(victim: str, eps: list, rows: dict, sample_idx: int) -> dict:
    out = {}
    for ep in eps:
        notes = []
        for s in range(len(ep.sessions)):
            r = rows.get(jid(victim, ep.episode_id, "note", f"s{s}", f"k{sample_idx}"))
            p = r.get("parsed") if r else None
            notes.append(p["note"] if p else None)
        out[ep.episode_id] = notes
    return out


def _merge_save_notes(run: str, victim: str, kind: str, notes: dict) -> None:
    try:
        existing = data.load_notes(run, victim, kind)
    except (FileNotFoundError, KeyError):
        existing = {}
    existing.update(notes)
    data.save_notes(run, victim, kind, existing)


async def stage_notes(client, run, victims, limit, rederive: bool = False) -> dict:
    plan, jobs = {}, {}
    for v in victims:
        seeds_eps = episodes_for(run, v, "seeds", limit)
        if rederive:
            plan[v] = [("rederived", seeds_eps, 1)]
        else:
            plan[v] = [("genuine", seeds_eps, 0), ("style", episodes_for(run, v, "style_seeds", limit), 0)]
        jobs[v] = [j for kind, eps, k in plan[v]
                   for j in note_jobs(run, v, eps, k, {"genuine": "note", "style": "style",
                                                       "rederived": "rederive"}[kind])]
    rows = await run_all(client, jobs, run, "rederive" if rederive else "notes")
    out = {}
    for v in victims:
        out[v] = {}
        for kind, eps, k in plan[v]:
            notes = collect_notes(v, eps, rows[v], k)
            _merge_save_notes(run, v, kind, notes)
            out[v][kind] = notes
    return out


# ====================================================================================== sub-stage: forge
def pick_style(ep, style_notes: dict, k: int = N_STYLE_EXAMPLES) -> list:
    """k genuine style notes of the episode's family, chosen by stable_hash(episode_id, ...)."""
    pool = [(seid, i, n) for seid, ns in style_notes.items() if seid.rsplit("-", 1)[0] == ep.family
            for i, n in enumerate(ns) if n]
    pool.sort(key=lambda t: stable_hash(ep.episode_id, "style-example", t[0], t[1]))
    return [n for _, _, n in pool[:k]]


def _load_inputs(run: str, victim: str, eps: list) -> tuple:
    try:
        genuine = data.load_notes(run, victim, "genuine")
        style = data.load_notes(run, victim, "style")
    except (FileNotFoundError, KeyError) as e:
        raise StageInputMissing(
            f"forge needs genuine and style notes for {victim} ({run}); run --stages notes first ({e!r})")
    missing = [ep.episode_id for ep in eps if ep.episode_id not in genuine]
    if missing:
        raise StageInputMissing(f"forge: {len(missing)} episodes of {victim} ({run}) have no genuine notes "
                                f"(e.g. {missing[:3]}); run --stages notes first")
    fams = {ep.family for ep in eps}
    nofam = [f for f in fams if not any(s.rsplit("-", 1)[0] == f for s in style)]
    if nofam:
        raise StageInputMissing(f"forge: no style notes for families {nofam} of {victim} ({run}); "
                                "run --stages notes first")
    return genuine, style


def instance_items(ep, genuine_notes: list) -> list:
    """[(edit_type, genuine target note, EditSpec)] in EDIT_TYPES order, missing targets left out."""
    out = []
    for et in EDIT_TYPES:
        e = ep.edits[et]
        g = genuine_notes[e.session_idx] if genuine_notes else None
        if g:
            out.append((et, g, e))
    return out


def forge_job(run, victim, model, ep, items, tier, sample_idx, style, n_versions, temperature, tag_part):
    pairs = [(g, e) for _, g, e in items]
    prompt = forge_packed(pairs, style if tier in ("T2", "T3") else None, n_versions=n_versions)
    return make_job(run, model, jid(victim, ep.episode_id, "forge", tier, tag_part), prompt, temperature,
                    sample_idx, ["forged", len(items), n_versions],
                    {"kind": tier if tier != "T3" else "T3gen", "episode_id": ep.episode_id, "tier": tier,
                     "edit_types": [et for et, _, _ in items], "sample_idx": sample_idx})


def merge_attempt(state: dict, items: list, parsed: Optional[dict], attempt: int) -> None:
    """Fold one T1/T2 attempt into state {edit_type: {note, valid, attempts}}. A valid note is kept;
    an invalid instance takes the new note if it is valid (the first invalid note is kept otherwise)."""
    for i, (et, _, edit) in enumerate(items):
        st = state.setdefault(et, {"note": None, "valid": False, "attempts": 0})
        if st["valid"]:
            continue
        st["attempts"] = attempt + 1
        if parsed is None:
            continue
        note = parsed[i + 1][0]
        ok = is_valid_forgery(note, edit)
        if ok or st["note"] is None:
            st["note"], st["valid"] = note, ok


def select_t3(cands: list, ratings: Optional[dict], order: list) -> Optional[int]:
    """cands: candidate dicts (original order). order: indices into cands of the valid candidates as
    shown to the rater. ratings: {shown position (1-based): rating} or None. Returns the index of the
    winner: highest rating among valid candidates; ties -> first in original candidate order. Without
    ratings (single valid candidate or unparseable ranking) the first valid candidate wins."""
    valid = [i for i, c in enumerate(cands) if c["valid"]]
    if not valid:
        return None
    if not ratings:
        return valid[0]
    rating_of = {ci: ratings[pos + 1] for pos, ci in enumerate(order)}
    best = None
    for i in valid:                       # original order -> strict '>' keeps the first on ties
        if best is None or rating_of[i] > rating_of[best]:
            best = i
    return best


def _base_row(ep, et, tier, note, valid, mode=None, forger=None, attempts=None, n_cand=None, rating=None):
    return {"episode_id": ep.episode_id, "family": ep.family, "edit_type": et, "tier": tier,
            "session_idx": ep.edits[et].session_idx, "note": note, "valid": bool(valid), "mode": mode,
            "forger": forger, "attempts": attempts, "n_candidates": n_cand, "selected_rating": rating}


async def stage_forge(client, run, victims, limit) -> dict:
    """All victims run their forge pipelines concurrently on the shared client. Each pipeline has
    dependent rounds (T1/T2 validity re-asks, then T3 candidates, then ranking); running victims
    independently keeps one victim's slow calls from stalling the others' next round."""
    inputs = {}
    for v in victims:                      # check all inputs before spending any request
        eps = episodes_for(run, v, "seeds", limit)
        inputs[v] = (eps, *_load_inputs(run, v, eps))
    parts = await asyncio.gather(*(_forge_victims(client, run, [v], {v: inputs[v]}) for v in victims))
    return {k: x for part in parts for k, x in part.items()}


async def _forge_victims(client, run, victims, inputs) -> dict:
    ctx = {}
    for v in victims:
        eps, genuine, style = inputs[v]
        ctx[v] = {"eps": eps, "genuine": genuine,
                  "items": {ep.episode_id: instance_items(ep, genuine.get(ep.episode_id)) for ep in eps},
                  "style": {ep.episode_id: pick_style(ep, style) for ep in eps}}

    # ---- T1 / T2 with validity retries (one packed call per episode and tier per attempt)
    state = {v: defaultdict(dict) for v in victims}          # (eid, tier) -> {et: {...}}
    for attempt in range(MAX_VALIDITY_RETRIES + 1):
        jobs = {}
        for v in victims:
            jobs[v] = []
            for ep in ctx[v]["eps"]:
                items = ctx[v]["items"][ep.episode_id]
                if not items:
                    continue
                for tier, model in (("T1", t1_forger_for(v)), ("T2", v)):
                    st = state[v][(ep.episode_id, tier)]
                    if attempt > 0 and all(st.get(et, {}).get("valid") for et, _, _ in items):
                        continue
                    jobs[v].append(forge_job(run, v, model, ep, items, tier, attempt, ctx[v]["style"][ep.episode_id],
                                             1, FORGE_TEMPERATURE, f"r{attempt}"))
        if not any(jobs.values()):
            break
        rows = await run_all(client, jobs, run, f"forge T1/T2 attempt {attempt}")
        for v in victims:
            for j in jobs[v]:
                eid, tier = j.meta["episode_id"], j.meta["tier"]
                r = rows[v].get(j.job_id)
                merge_attempt(state[v][(eid, tier)], ctx[v]["items"][eid], parsed_of(r), attempt)

    # ---- T3 candidate generation
    jobs = {v: [forge_job(run, v, v, ep, ctx[v]["items"][ep.episode_id], "T3", c, ctx[v]["style"][ep.episode_id],
                          T3_VERSIONS_PER_CALL, T3_TEMPERATURE, f"c{c}")
                for ep in ctx[v]["eps"] if ctx[v]["items"][ep.episode_id] for c in range(T3_CALLS)]
            for v in victims}
    rows = await run_all(client, jobs, run, "forge T3 candidates")
    cands = {v: {} for v in victims}                 # (eid, et) -> [candidate dicts]
    for v in victims:
        for ep in ctx[v]["eps"]:
            items = ctx[v]["items"][ep.episode_id]
            for i, (et, _, edit) in enumerate(items):
                lst = []
                for c in range(T3_CALLS):
                    r = rows[v].get(jid(v, ep.episode_id, "forge", "T3", f"c{c}"))
                    p = parsed_of(r)
                    if not p:
                        continue
                    for k, note in enumerate(p[i + 1]):
                        lst.append({"call_idx": c, "version_idx": k, "note": note,
                                    "valid": is_valid_forgery(note, edit)})
                cands[v][(ep.episode_id, et)] = lst

    # ---- T3 ranking: one call per instance with >= 2 valid candidates. The spec names no temperature for
    # this query; it is a rating query, so QUERY_TEMPERATURE (0.0) is used.
    orders = {v: {} for v in victims}
    jobs = {}
    for v in victims:
        jobs[v] = []
        for ep in ctx[v]["eps"]:
            gnotes = ctx[v]["genuine"][ep.episode_id]
            for et, _, edit in ctx[v]["items"][ep.episode_id]:
                lst = cands[v][(ep.episode_id, et)]
                valid = [i for i, c in enumerate(lst) if c["valid"]]
                order = sorted(valid, key=lambda i: stable_hash(ep.episode_id, et, "t3-order",
                                                                lst[i]["call_idx"], lst[i]["version_idx"]))
                orders[v][(ep.episode_id, et)] = order
                if len(order) < 2:
                    continue
                prompt = rate_candidates(ep, gnotes, edit.session_idx, [lst[i]["note"] for i in order])
                jobs[v].append(make_job(run, v, jid(v, ep.episode_id, "rank", et), prompt, QUERY_TEMPERATURE, 0,
                                        ["ratings", len(order)],
                                        {"kind": "rank", "episode_id": ep.episode_id, "edit_type": et,
                                         "n": len(order)}))
    rows = await run_all(client, jobs, run, "forge T3 ranking")

    # ---- tidy outputs
    result = {}
    for v in victims:
        forged, t3rows, skipped = [], [], Counter()
        for ep in ctx[v]["eps"]:
            gnotes = ctx[v]["genuine"][ep.episode_id]
            have = {et for et, _, _ in ctx[v]["items"][ep.episode_id]}
            for et in EDIT_TYPES:
                if et not in have:
                    skipped[et] += 1
                    continue
                edit = ep.edits[et]
                g = gnotes[edit.session_idx]
                n0, mode = apply_t0(g, edit)
                forged.append(_base_row(ep, et, "T0", n0, is_valid_forgery(n0, edit), mode=mode, forger="template"))
                for tier, model in (("T1", t1_forger_for(v)), ("T2", v)):
                    st = state[v][(ep.episode_id, tier)].get(et, {"note": None, "valid": False, "attempts": 0})
                    forged.append(_base_row(ep, et, tier, st["note"], st["valid"], forger=model,
                                            attempts=st["attempts"]))
                lst = cands[v][(ep.episode_id, et)]
                order = orders[v][(ep.episode_id, et)]
                r = rows[v].get(jid(v, ep.episode_id, "rank", et))
                ratings = parsed_of(r)
                win = select_t3(lst, ratings, order)
                pos_of = {ci: p for p, ci in enumerate(order)}
                for i, c in enumerate(lst):
                    rating = ratings[pos_of[i] + 1] if (ratings and i in pos_of) else None
                    t3rows.append({"episode_id": ep.episode_id, "family": ep.family, "edit_type": et,
                                   "session_idx": edit.session_idx, "cand_idx": i, **c,
                                   "shown_position": pos_of.get(i), "rating": rating, "selected": i == win})
                n_valid = len(order)
                if win is None:
                    first = lst[0]["note"] if lst else None
                    forged.append(_base_row(ep, et, "T3", first, False, forger=v, n_cand=0))
                else:
                    sel_rating = ratings[pos_of[win] + 1] if ratings else None
                    forged.append(_base_row(ep, et, "T3", lst[win]["note"], True, forger=v, n_cand=n_valid,
                                            rating=sel_rating))
        eids = {ep.episode_id for ep in ctx[v]["eps"]}
        _merge_save_jsonl(data.proc_dir(run, v) / "forged.jsonl", forged, eids, saver=partial(data.save_forged, run, v))
        _merge_save_jsonl(data.proc_dir(run, v) / "t3_candidates.jsonl", t3rows, eids)
        result[v] = {"forged": forged, "t3": t3rows, "skipped": dict(skipped)}
    return result


def _merge_save_jsonl(path, rows: list, eids: set, saver=None) -> None:
    """Replace the rows of the given episodes, keep rows of other episodes (a --limit run must not
    wipe a full output)."""
    old = [r for r in data.read_jsonl(path) if r["episode_id"] not in eids] if path.exists() else []
    allr = old + rows
    if saver:
        saver(allr)
    else:
        data.write_jsonl(path, allr)


# ====================================================================================== summary
def _latest_rows(run: str, victim: str) -> list:
    latest = {}
    for r in load_rows(raw_path(run, victim)):
        p = latest.get(r["job_id"])
        if p is None or p.get("error") or not r.get("error"):
            latest[r["job_id"]] = r
    return list(latest.values())


def _pct(a, b):
    return f"{100 * a / b:5.1f}%" if b else "   -  "


def summarize(run: str, victim: str, client=None, forge_result: Optional[dict] = None) -> dict:
    rows = _latest_rows(run, victim)
    calls = defaultdict(lambda: Counter())
    rtoks, otoks = defaultdict(list), defaultdict(list)
    for r in rows:
        k = (r["meta"].get("kind", "?"), r["model"])
        c = calls[k]
        c["jobs"] += 1
        if r.get("error"):
            c["error"] += 1
            continue
        if r.get("parsed") is None:
            c["parse_fail"] += 1
        if r.get("attempts", 1) == 1 and r.get("parsed") is not None:
            c["first_try_ok"] += 1
        t = (r.get("text") or "").lstrip()
        if t and not (t.startswith("{") or t.startswith("```")):
            c["text_not_json_start"] += 1
        if not r.get("cached"):
            c["requests"] += r.get("attempts", 1)
        c["cost_micro"] += int(round(1e6 * (r.get("cost") or 0)))
        u = r.get("usage") or {}
        rtoks[k].append(u.get("reasoning_tokens") or 0)
        otoks[k].append(u.get("output_tokens") or 0)

    print(f"\n=== {STAGE} summary: {victim} ({run}) ===")
    print(f"{'kind':9s} {'model':20s} {'jobs':>5s} {'pfail':>5s} {'err':>4s} {'1st-ok':>7s} {'req':>5s} "
          f"{'cost$':>8s} {'reas.med':>8s} {'out.max':>7s} {'nonJSON':>7s}")
    tot_req, tot_cost = 0, 0.0
    for k in sorted(calls):
        c = calls[k]
        tot_req += c["requests"]
        tot_cost += c["cost_micro"] / 1e6
        rt = statistics.median(rtoks[k]) if rtoks[k] else 0
        print(f"{k[0]:9s} {k[1]:20s} {c['jobs']:5d} {c['parse_fail']:5d} {c['error']:4d} "
              f"{_pct(c['first_try_ok'], c['jobs']):>7s} {c['requests']:5d} {c['cost_micro'] / 1e6:8.4f} "
              f"{rt:8.0f} {max(otoks[k] or [0]):7d} {c['text_not_json_start']:7d}")
    print(f"total requests (raw rows, uncached incl. parse retries): {tot_req}   cost ${tot_cost:.4f}")

    # notes missing
    out = {"calls": {f"{a}|{b}": dict(c) for (a, b), c in calls.items()}, "requests": tot_req, "cost": tot_cost}
    try:
        p = data.proc_dir(run, victim) / "notes.json"
        import json
        notes = json.loads(p.read_text()) if p.exists() else {}
    except Exception:
        notes = {}
    miss = {}
    for kind, d in notes.items():
        n = sum(len(v) for v in d.values())
        m = sum(x is None for v in d.values() for x in v)
        miss[kind] = (m, n)
        print(f"notes {kind:9s}: {m} missing of {n}")
    out["notes_missing"] = miss

    # forgeries
    if forge_result is None:
        fp = data.proc_dir(run, victim) / "forged.jsonl"
        tp = data.proc_dir(run, victim) / "t3_candidates.jsonl"
        if fp.exists():
            forge_result = {"forged": data.read_jsonl(fp), "t3": data.read_jsonl(tp) if tp.exists() else [],
                            "skipped": None}
    if forge_result:
        f = forge_result["forged"]
        print("validity (valid/rows) per tier x edit type:")
        print("      " + "".join(f"{et:>12s}" for et in EDIT_TYPES))
        val = {}
        for tier in FORGE_TIERS:
            cells = []
            for et in EDIT_TYPES:
                rs = [r for r in f if r["tier"] == tier and r["edit_type"] == et]
                nv = sum(r["valid"] for r in rs)
                val[(tier, et)] = (nv, len(rs))
                cells.append(f"{nv:>5d}/{len(rs):<3d}{_pct(nv, len(rs)).strip():>4s}"[:12].rjust(12))
            print(f"{tier:6s}" + "".join(cells))
        out["validity"] = {f"{a}|{b}": v for (a, b), v in val.items()}
        modes = Counter((r["edit_type"], r["mode"]) for r in f if r["tier"] == "T0")
        print("T0 modes:", ", ".join(f"{et}:{m}={n}" for (et, m), n in sorted(modes.items())))
        out["t0_modes"] = {f"{a}|{b}": n for (a, b), n in modes.items()}
        retried = Counter(r["tier"] for r in f if r["tier"] in ("T1", "T2") and (r["attempts"] or 0) > 1)
        print("T1/T2 instances needing > 1 attempt:", dict(retried))
        if forge_result.get("skipped") is not None:
            print("instances skipped (genuine target note missing):", forge_result["skipped"] or 0)
            out["skipped"] = forge_result["skipped"]
        t3 = forge_result["t3"]
        if t3:
            nv = sum(c["valid"] for c in t3)
            by_inst = defaultdict(list)
            for c in t3:
                by_inst[(c["episode_id"], c["edit_type"])].append(c)
            ranked = [cs for cs in by_inst.values() if any(c["rating"] is not None for c in cs)]
            ties = 0
            spreads = []
            for cs in ranked:
                rs = sorted([c["rating"] for c in cs if c["rating"] is not None], reverse=True)
                ties += len(rs) > 1 and rs[0] == rs[1]
                spreads.append(rs[0] - rs[-1])
            print(f"T3 candidates: {nv}/{len(t3)} valid ({_pct(nv, len(t3)).strip()}); instances ranked: "
                  f"{len(ranked)}/{len(by_inst)}; top rating tied: {ties}/{len(ranked)}; "
                  f"median max-min rating spread: {statistics.median(spreads) if spreads else '-'}")
            out["t3"] = {"valid": nv, "n": len(t3), "ranked": len(ranked), "ties": ties, "instances": len(by_inst)}

    # latency / true HTTP requests of this process
    lat = getattr(client, "calls", None)
    if lat:
        print("this process, uncached calls (latency s median/max, HTTP attempts incl. 429 retries):")
        for (kind, model), recs in sorted(lat.items()):
            if model != victim and model != t1_forger_for(victim):
                continue
            ls = [x["latency"] for x in recs]
            print(f"  {kind:9s} {model:20s} n={len(recs):4d} lat {statistics.median(ls):6.1f}/{max(ls):6.1f} "
                  f"http={sum(x['attempts'] for x in recs)}")
    return out


# ====================================================================================== client with timing
def make_client():
    from memlab.clients.adaption import AdaptionClient

    class TimedClient(AdaptionClient):
        """Records latency and HTTP attempts of uncached calls by call kind (for the summary only)."""

        def __init__(self, *a, **k):
            super().__init__(*a, **k)
            self.kind_of = {}
            self.calls = defaultdict(list)

        async def complete(self, model, input, instructions=None, **kw):
            c = await super().complete(model, input, instructions, **kw)
            if not c.cached:
                kind = self.kind_of.get((model, _h(input), kw.get("sample_idx", 0) % 1000), "?")
                self.calls[(kind, model)].append({"latency": c.latency_s, "attempts": c.attempts})
            return c

    return TimedClient()


# ====================================================================================== entry points
async def run_stages(run: str, victims: list, stages: list, limit: Optional[int], client) -> dict:
    forge_res = {}
    try:
        if "notes" in stages:
            await stage_notes(client, run, victims, limit)
        if "rederive" in stages:
            await stage_notes(client, run, victims, limit, rederive=True)
        if "forge" in stages:
            forge_res = await stage_forge(client, run, victims, limit)
    finally:
        http = getattr(client, "_http", None)
        if http is not None:
            await http.aclose()
            client._http = None
            client._loop = None
        if hasattr(client, "flush_ledger"):
            client.flush_ledger()
    return {v: summarize(run, v, client, forge_res.get(v)) for v in victims}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--run", required=True, choices=sorted(RUNS))
    ap.add_argument("--victims", default=None, help="comma-separated; default: the run's victims")
    ap.add_argument("--stages", default=",".join(SUBSTAGES), help="comma-separated subset of notes,rederive,forge")
    ap.add_argument("--limit", type=int, default=None, help="episodes per family (tests / smoke runs)")
    a = ap.parse_args(argv)
    victims = a.victims.split(",") if a.victims else list(RUNS[a.run]["victims"])
    stages = [s.strip() for s in a.stages.split(",") if s.strip()]
    bad = [s for s in stages if s not in SUBSTAGES]
    if bad:
        ap.error(f"unknown stages {bad}; choose from {SUBSTAGES}")
    try:
        asyncio.run(run_stages(a.run, victims, stages, a.limit, make_client()))
    except StageInputMissing as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
