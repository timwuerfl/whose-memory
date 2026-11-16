"""Model-free tests for the local pipeline logic (memlab/local/pipeline.py, experiments/local_pipeline.py)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from memlab import config as C  # noqa: E402
from memlab.local import pipeline as P  # noqa: E402
from memlab.schema import EDIT_TYPES  # noqa: E402


@pytest.fixture(scope="module")
def study():
    eps, main, style = P.load_study_episodes(4, ROOT)
    notes = {(e, s): f"I noted fact {s} of {e}. It is preliminary." for e in main + style for s in range(7)}
    return eps, main, style, notes


def _fake_inputs(eps, main):
    forged, cands, other = [], [], []
    for e in main:
        for et in EDIT_TYPES:
            s = eps[e].edits[et].session_idx
            for tier in ("T0", "T1", "T2"):
                forged.append({"tier": tier, "episode_id": e, "edit_type": et, "session_idx": s,
                               "note": f"{tier} forged {e} {et}", "valid": tier != "T1", "mode": "x", "attempts": 1})
        for et in C.t3_subset(e):
            for k in range(C.T3_N_CANDIDATES):
                cands.append({"episode_id": e, "edit_type": et, "cand_idx": k, "note": f"cand {k} {e} {et}",
                              "valid": k % 2 == 0})
        for m in C.LOCAL_OTHER_MODELS:
            for s in range(7):
                other.append({"model": m, "episode_id": e, "session_idx": s, "note": f"{m} note {s}"})
    return forged, cands, other


# ------------------------------------------------------------------------------------------- ids/episodes
def test_study_ids_interleaved_and_limited():
    main, style = P.study_ids(2)
    assert main[:3] == ["inventory-00050", "research-00050", "assistant-00050"]
    assert len(main) == 6 and len(style) == 6
    assert all(int(e.split("-")[1]) in C.LOCAL_STYLE_SEEDS for e in style)
    full_main, full_style = P.study_ids(None)
    assert len(full_main) == 150 and len(full_style) == 30
    assert not set(full_main) & set(full_style)


# ------------------------------------------------------------------------------------------- registry
def test_instances_are_t3_subset(study):
    eps, main, style, notes = study
    inst = P.instances(main)
    assert len(inst) == 2 * len(main)
    assert all(et in C.t3_subset(e) for e, et in inst)


def test_build_items_counts_and_fields(study):
    eps, main, style, notes = study
    forged, cands, other = _fake_inputs(eps, main)
    items, missing = P.build_items(eps, main, notes, forged, cands, other)
    assert not missing
    from collections import Counter
    cnt = Counter(it["kind"] for it in items)
    n_inst = 2 * len(main)
    assert cnt["genuine"] == cnt["T0"] == cnt["T1"] == cnt["T2"] == n_inst
    assert cnt["cand"] == C.T3_N_CANDIDATES * n_inst
    for m in C.LOCAL_OTHER_MODELS:
        assert cnt[f"other:{m}"] == n_inst
    assert "xep" not in cnt
    ids = [it["item_id"] for it in items]
    assert len(ids) == len(set(ids))
    order = [P.KIND_ORDER.index(P.kind_base(it["kind"])) for it in items]
    assert order == sorted(order)
    for it in items:
        ep = eps[it["episode_id"]]
        assert it["edit_type"] in C.t3_subset(it["episode_id"])
        assert it["session_idx"] == ep.edits[it["edit_type"]].session_idx
        if it["kind"] == "genuine":
            assert it["note"] == notes[(it["episode_id"], it["session_idx"])]
        k = P.kind_base(it["kind"])
        exp = {"genuine": ["s_trace", "s_blind", "c", "v"], "T0": ["s_trace", "s_blind", "c", "v"],
               "cand": ["s_trace", "s_blind", "c", "v_att"], "other": ["s_trace", "s_blind"]}
        if k in exp:
            assert it["passes"] == exp[k]
        assert it["note_sha"] == P.note_sha(it["note"])


def test_build_items_reports_missing(study):
    eps, main, style, notes = study
    forged, cands, other = _fake_inputs(eps, main)
    e0, et0 = P.instances(main)[0]
    s0 = eps[e0].edits[et0].session_idx
    notes2 = dict(notes)
    del notes2[(e0, s0)]
    forged2 = [r for r in forged if not (r["tier"] == "T1" and r["episode_id"] == e0)]
    items, missing = P.build_items(eps, main, notes2, forged2, cands, other)
    assert missing["genuine"] == 1 and missing["T1"] == 2
    assert P.gid(e0, s0) not in {it["item_id"] for it in items}


# ------------------------------------------------------------------------------------------- style examples
def test_style_examples_deterministic_and_never_main(study):
    eps, main, style, notes = study
    pool = P.style_pool(notes, style)
    assert all(k[0] in style for k in pool)
    for e in main[:6]:
        for et in EDIT_TYPES:
            a = P.style_examples(e, et, eps[e].family, pool)
            b = P.style_examples(e, et, eps[e].family, dict(reversed(list(pool.items()))))
            assert a == b and len(a) == C.N_STYLE_EXAMPLES
            assert len(set(a)) == len(a)
            for ex in a:
                src = ex.split(" of ")[1].split(".")[0]
                assert src in style and src not in main
                assert eps[src].family == eps[e].family
    # varies across instances
    sets = {tuple(P.style_examples(e, et, eps[e].family, pool)) for e in main for et in EDIT_TYPES}
    assert len(sets) > 1


def test_style_examples_prefers_distinct_episodes(study):
    eps, main, style, notes = study
    pool = P.style_pool(notes, style)
    e = main[0]
    ex = P.style_examples(e, "E1", eps[e].family, pool)
    srcs = {x.split(" of ")[1].split(".")[0] for x in ex}
    assert len(srcs) == 3   # 4 style episodes per family available


# ------------------------------------------------------------------------------------------- xep
def test_pick_xep_other_episode_same_edit(study):
    eps, main, style, notes = study
    eps_full, main_full, _ = P.load_study_episodes(None, ROOT)
    fam = {}
    for e in main_full:
        fam.setdefault(eps_full[e].family, []).append(eps_full[e])
    n_same = 0
    for e in main_full[:30]:
        ep = eps_full[e]
        for et in EDIT_TYPES:
            src, src_s, same = P.pick_xep(ep, et, fam[ep.family])
            assert src != e and eps_full[src].family == ep.family and src in main_full
            assert eps_full[src].edits[et].session_idx == src_s
            assert P.pick_xep(ep, et, list(reversed(fam[ep.family]))) == (src, src_s, same)
            if same:
                assert src_s == ep.edits[et].session_idx
            n_same += same
    assert n_same >= 0.95 * 30 * 5   # a same-slot donor almost always exists (falls back otherwise)


# ------------------------------------------------------------------------------------------- select
def _cands():
    rows = []
    # instance A: 4 candidates, cand 3 invalid but best on everything
    vals = [  # v_att, s_trace, s_delta, c, v
        (0.2, 3.0, 0.5, 0.1, 0.3),
        (0.9, 2.5, 0.1, 0.4, 0.2),
        (0.5, 1.5, 0.9, 0.8, 0.7),
        (1.0, 0.1, -9, 1.0, 1.0),
    ]
    for k, (va, st, sd, c, v) in enumerate(vals):
        rows.append({"item_id": f"c|A|E1|{k}", "episode_id": "A", "edit_type": "E1", "cand_idx": k,
                     "valid": k != 3, "v_att_pyes": va, "s_trace_mean": st, "s_delta": sd, "c_pyes": c, "v_pyes": v})
    # instance B: no valid candidate
    rows.append({"item_id": "c|B|E2|0", "episode_id": "B", "edit_type": "E2", "cand_idx": 0, "valid": False,
                 "v_att_pyes": 0.5, "s_trace_mean": 1.0, "s_delta": 0.0, "c_pyes": 0.5, "v_pyes": 0.5})
    # instance C: valid but NaN score on one candidate
    rows.append({"item_id": "c|C|E3|0", "episode_id": "C", "edit_type": "E3", "cand_idx": 0, "valid": True,
                 "v_att_pyes": float("nan"), "s_trace_mean": 2.0, "s_delta": 0.0, "c_pyes": 0.5, "v_pyes": 0.5})
    rows.append({"item_id": "c|C|E3|1", "episode_id": "C", "edit_type": "E3", "cand_idx": 1, "valid": True,
                 "v_att_pyes": 0.1, "s_trace_mean": 2.0, "s_delta": 0.0, "c_pyes": 0.5, "v_pyes": 0.5})
    return rows


def test_select_all_picks_correctly():
    sel = {(r["episode_id"], r["tier"]): r["item_id"] for r in P.select_all(_cands())}
    assert sel[("A", "T3")] == "c|A|E1|1"
    assert sel[("A", "T4s")] == "c|A|E1|2"
    assert sel[("A", "T4d")] == "c|A|E1|1"
    assert sel[("A", "T4c")] == "c|A|E1|2"
    assert ("A", "T4v") not in sel
    assert sel[("A", "T2r")] in {"c|A|E1|0", "c|A|E1|1", "c|A|E1|2"}
    for t in ("T3", "T4s", "T4d", "T4c", "T2r"):
        assert sel[("B", t)] is None
    assert sel[("C", "T3")] == "c|C|E3|1"        # NaN skipped
    assert sel[("C", "T4s")] == "c|C|E3|0"       # tie -> lower cand_idx
    assert P.select_all(_cands()) == P.select_all(_cands())


def test_append_selection_hook(tmp_path):
    cands = _cands()
    P.write_jsonl_atomic(tmp_path / "items.jsonl", [{**c, "kind": "cand"} for c in cands])
    P.write_jsonl_atomic(tmp_path / "selected.jsonl", [{"episode_id": "A", "edit_type": "E1", "tier": "T3",
                                                       "item_id": "c|A|E1|1"}])
    P.append_selection(tmp_path, "T4p", {"c|A|E1|0": 5.0, "c|A|E1|2": 1.0, "c|A|E1|3": 99.0})
    P.append_selection(tmp_path, "T4p", {"c|A|E1|0": 5.0, "c|A|E1|2": 1.0, "c|A|E1|3": 99.0})  # idempotent
    rows = P.read_jsonl(tmp_path / "selected.jsonl")
    p = [r for r in rows if r["tier"] == "T4p"]
    assert len(p) == 3 and [r for r in p if r["episode_id"] == "A"][0]["item_id"] == "c|A|E1|0"
    assert any(r["tier"] == "T3" for r in rows)


# ------------------------------------------------------------------------------------------- resume
def test_jsonl_tolerates_truncation(tmp_path):
    f = tmp_path / "x.jsonl"
    P.append_jsonl(f, [{"a": 1}, {"a": 2}])
    with open(f, "a") as h:
        h.write('{"a": 3, "b"')       # killed mid-write
    assert [r["a"] for r in P.read_jsonl(f)] == [1, 2]
    P.append_jsonl(f, [{"a": 4}])
    assert [r["a"] for r in P.read_jsonl(f)] == [1, 2, 4]
    g = tmp_path / "y.jsonl.gz"
    P.append_jsonl(g, [{"a": 1}])
    P.append_jsonl(g, [{"a": 2}])
    assert [r["a"] for r in P.read_jsonl(g)] == [1, 2]


def test_score_todo_skips_finished_and_orders_by_pass(study):
    eps, main, style, notes = study
    forged, cands, other = _fake_inputs(eps, main)
    items, _ = P.build_items(eps, main, notes, forged, cands, other)
    todo = P.score_todo(items, set())
    assert len(todo) == sum(len(it["passes"]) for it in items)
    order = [P.PASSES.index(p) for p, _ in todo]
    assert order == sorted(order)                       # pass-major
    assert not any(p == "v" and it["kind"] == "cand" for p, it in todo)
    assert not any(p in ("c", "v", "v_att") and it["kind"].startswith("other:") for p, it in todo)
    it = items[0]
    done = {("s_trace", it["item_id"], it["note_sha"]), ("v", it["item_id"], "stale-sha")}
    todo2 = P.score_todo(items, done)
    assert len(todo2) == len(todo) - 1
    assert ("s_trace", it) not in todo2 and ("v", it) in todo2
    c0 = next(x for x in items if x["kind"] == "cand")
    todo3 = P.score_todo(items, set(), selected=[c0["item_id"]])
    assert ("v", c0) in todo3 and len(todo3) == len(todo) + 1


def test_selected_ids():
    rows = P.select_all(_cands())
    ids = P.selected_ids(rows)
    assert len(ids) == len(set(ids)) and None not in ids
    assert "c|A|E1|1" in ids and "c|A|E1|2" in ids


class _FakeLM:
    def __init__(self):
        self.calls = []

    def generate(self, batch, max_new_tokens, temperature, seed, batch_size):
        self.calls.append((len(batch), seed))
        return [f"I recorded item {m[1]['content']} with seed {seed}." for m in batch]

    def _encode(self, t):
        return t.split()


def test_run_generation_resume(tmp_path):
    from experiments import local_pipeline as LP
    jobs = [{"key": f"k{i}", "messages": [{"role": "system", "content": ""}, {"role": "user", "content": str(i)}]}
            for i in range(10)]
    mk = lambda j, note, raw, flags, a, prob, seed: {"note": note, "attempts": a, "seed": seed}  # noqa: E731
    out = tmp_path / "g.jsonl"
    lm = _FakeLM()
    LP.run_generation(lm, jobs, out, tag="t", batch_size=4, temperature=0.7, check=lambda j, n, t: None,
                      max_attempts=3, make_row=mk)
    rows = P.read_jsonl(out)
    assert [r["_key"] for r in rows] == [j["key"] for j in jobs]
    assert [c[0] for c in lm.calls] == [4, 4, 2]
    first_seeds = [c[1] for c in lm.calls]
    # second run: nothing to do
    lm2 = _FakeLM()
    LP.run_generation(lm2, jobs, out, tag="t", batch_size=4, temperature=0.7, check=lambda j, n, t: None,
                      max_attempts=3, make_row=mk)
    assert lm2.calls == []
    # drop the last row of batch 1: only that batch is regenerated, with the same composition and seed
    P.write_jsonl_atomic(out, [r for r in rows if r["_key"] != "k5"])
    lm3 = _FakeLM()
    LP.run_generation(lm3, jobs, out, tag="t", batch_size=4, temperature=0.7, check=lambda j, n, t: None,
                      max_attempts=3, make_row=mk)
    assert lm3.calls == [(4, first_seeds[1])]
    assert sorted(r["_key"] for r in P.read_jsonl(out)) == sorted(j["key"] for j in jobs)


def test_run_generation_retries_bad_outputs(tmp_path):
    from experiments import local_pipeline as LP
    jobs = [{"key": f"k{i}", "messages": [{}, {"content": str(i)}]} for i in range(4)]
    lm = _FakeLM()
    seen = {}

    def check(j, note, ntok):   # job k1 fails twice, then succeeds
        seen[j["key"]] = seen.get(j["key"], 0) + 1
        return "bad" if j["key"] == "k1" and seen[j["key"]] < 3 else None

    LP.run_generation(lm, jobs, tmp_path / "g.jsonl", tag="t", batch_size=4, temperature=0.7, check=check,
                      max_attempts=4, make_row=lambda j, note, raw, flags, a, prob, seed: {"attempts": a, "problem": prob})
    rows = {r["_key"]: r for r in P.read_jsonl(tmp_path / "g.jsonl")}
    assert rows["k1"]["attempts"] == 3 and rows["k1"]["problem"] is None
    assert rows["k0"]["attempts"] == 1
    assert [c[0] for c in lm.calls] == [4, 1, 1]
    assert len({c[1] for c in lm.calls}) == 3


# ------------------------------------------------------------------------------------------- cleanup
def test_clean_note_and_problem():
    n, f = P.clean_note('  "I checked the stock.\n\nIt was 40 units."  ')
    assert n == "I checked the stock. It was 40 units." and f["quotes"] and f["multi_par"]
    n, f = P.clean_note("Memory note: I checked the stock and it was 40 units.")
    assert n.startswith("I checked") and f["preamble"]
    n, f = P.clean_note("Note that I checked the stock.")
    assert n == "Note that I checked the stock." and not f["preamble"]
    assert P.note_problem("", 0, 200) == "empty"
    assert P.note_problem("Too short.", 3, 200) == "short"
    assert P.note_problem("x" * 50 + " and then", 199, 200) == "truncated"
    assert P.note_problem("x" * 50 + ".", 199, 200) is None
    assert P.note_problem("x" * 50 + " and then", 50, 200) is None


def test_common_prefix_len():
    assert P.common_prefix_len([[1, 2, 3], [1, 2, 4], [1, 2]]) == 2
    assert P.common_prefix_len([[1, 2, 3]]) == 3
    assert P.common_prefix_len([[5], [6]]) == 0


def test_chunk_rows_budget():
    ch = P.chunk_rows([800, 700, 500, 100, 100, 100], max_rows=16, max_tokens=2000)
    assert ch == [[0, 1], [2, 3, 4, 5]]
    assert sum(len(c) for c in P.chunk_rows([5000, 10], 4, 100)) == 2   # oversize row still gets a chunk
    assert P.chunk_rows([10] * 5, max_rows=2, max_tokens=10 ** 6) == [[0, 1], [2, 3], [4]]
