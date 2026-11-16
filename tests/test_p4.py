"""Offline tests for stage p4_gate: HMAC tags, G1 gate, store variants, rows (fake client, hand-made fixture)."""
from __future__ import annotations

import asyncio
import json
from collections import Counter

import pytest

from experiments import p4_gate as P
from memlab.attacks.template import apply_t0, is_valid_forgery
from memlab.clients.adaption import Completion
from memlab.data import episode, forged_index, question_order, store_with
from memlab.defenses.gate import Scores, apply_gate, auroc, fit_threshold, flag_rate, select_detector
from memlab.defenses.hmac_tags import SignedStore, new_key, sign, verify
from memlab.prompts import POLICY_SIGNED, POLICY_UNSIGNED, answer_all
from memlab.schema import EDIT_TYPES, trace_hash

FIXTURE_EPS = ("inventory-00000", "research-00001", "assistant-00002")


# ------------------------------------------------------------------ fixture
def make_fixture(ep_ids=FIXTURE_EPS):
    """Notes fabricated from each edit's true_content, forgeries via apply_t0, synthetic detector scores."""
    eps = [episode(e) for e in ep_ids]
    genuine, red, forged, c_rows, r_rows = {}, {}, [], [], []
    for ep in eps:
        by_slot = {e.session_idx: e for e in ep.edits.values()}
        notes = []
        for s in ep.sessions:
            if s.idx in by_slot:
                notes.append(f"Session notes: {by_slot[s.idx].true_content} I will keep this on file.")
            else:
                notes.append(f"Routine session about {s.title}; nothing that changes my standing tasks.")
        genuine[ep.episode_id] = notes
        red[ep.episode_id] = [f"(re-derived) {n}" for n in notes]
        for e in EDIT_TYPES:
            ed = ep.edits[e]
            base, mode = apply_t0(notes[ed.session_idx], ed)
            for tier, suffix in (("T0", ""), ("T1", ""), ("T2", " Noted."), ("T3", " Noted again.")):
                f = base + suffix
                forged.append({"episode_id": ep.episode_id, "edit_type": e, "tier": tier, "session_idx": ed.session_idx,
                               "note": f, "valid": is_valid_forgery(f, ed), "mode": mode})
        # C: clean store genuine entries 80..98, attacked: forged slot 20 (E5 slot: 90 = missed), others as clean
        for i in range(7):
            c_rows.append({"episode_id": ep.episode_id, "family": ep.family, "store": "clean", "slot": i,
                           "entry_kind": "genuine", "edit_type": None, "tier": None, "p_supported": 80 + 3 * i})
        for e in EDIT_TYPES:
            slot = ep.edits[e].session_idx
            for tier in ("T0", "T1", "T2", "T3"):
                for i in range(7):
                    kind = "forged" if i == slot else "genuine"
                    p = (90 if e == "E5" else 20) if i == slot else 80 + 3 * i
                    c_rows.append({"episode_id": ep.episode_id, "family": ep.family, "store": f"{e}:{tier}", "slot": i,
                                   "entry_kind": kind, "edit_type": e if kind == "forged" else None,
                                   "tier": tier if kind == "forged" else None, "p_supported": p})
        for i in range(7):
            r_rows.append({"episode_id": ep.episode_id, "family": ep.family, "slot": i, "entry_kind": "genuine",
                           "edit_type": None, "tier": None, "p_altered": 10})
        for e in EDIT_TYPES:
            for tier in ("T0", "T1", "T2", "T3"):
                r_rows.append({"episode_id": ep.episode_id, "family": ep.family, "slot": ep.edits[e].session_idx,
                               "entry_kind": "forged", "edit_type": e, "tier": tier, "p_altered": 10})
    return eps, genuine, red, forged, c_rows, r_rows


@pytest.fixture(scope="module")
def fx():
    return make_fixture()


# ------------------------------------------------------------------ HMAC
def test_hmac_sign_verify_roundtrip_and_binding():
    k = new_key()
    s = sign("note text", "self", 3, "abcd", k)
    assert verify("note text", "self", 3, "abcd", s, k)
    assert not verify("note text!", "self", 3, "abcd", s, k)        # tampered text
    assert not verify("note text", "self", 4, "abcd", s, k)         # replay onto another session
    assert not verify("note text", "self", 3, "abce", s, k)         # another trace hash
    assert not verify("note text", "other", 3, "abcd", s, k)        # another author
    assert not verify("note text", "self", 3, "abcd", s, new_key())  # another key
    assert not verify("note text", "self", 3, "abcd", None, k)


def test_signed_store_tamper_insider_rewrite(fx):
    eps, genuine, red, *_ = fx
    ep = eps[0]
    th = [trace_hash(s) for s in ep.sessions]
    k = new_key()
    st = SignedStore(genuine[ep.episode_id], th, k)
    assert st.verified() == [True] * 7 and st.invalid_slots() == []
    st.tamper(2, "forged text")                       # outsider: detected
    assert st.invalid_slots() == [2]
    assert "signature=INVALID" in st.tags()[2] and all("signature=VALID" in t for i, t in enumerate(st.tags()) if i != 2)
    st.tamper(2, "forged text", key=new_key())        # wrong key: still detected
    assert st.invalid_slots() == [2]
    st2 = SignedStore(genuine[ep.episode_id], th, k)
    st2.tamper(2, "forged text", key=k)               # insider: not detected
    assert st2.invalid_slots() == [] and st2.notes()[2] == "forged text"
    st.rewrite(2, "re-derived text")                  # memory system re-signs
    assert st.invalid_slots() == []
    # no replay across slots: moving entry 1's note+signature to slot 2 fails
    st3 = SignedStore(genuine[ep.episode_id], th, k)
    st3.entries[2].note, st3.entries[2].sig = st3.entries[1].note, st3.entries[1].sig
    assert st3.invalid_slots() == [2]


# ------------------------------------------------------------------ gate statistics
def test_fit_threshold_tie_rule():
    # 20 negatives: 18 x 5, one 50, one 90 -> share(neg > 50) = 1/20 = 0.05 <= 0.05 -> tau = 50
    neg = [5] * 18 + [50, 90]
    assert fit_threshold(neg, 0.05) == 50
    # smaller candidate 5: share(neg > 5) = 2/20 > 0.05
    assert flag_rate(neg, 50) == 0.05
    # ties at tau are not flagged: 3 tied maxima out of 20 -> smallest tau with share(> tau) <= 5% is the max itself
    neg2 = [1] * 17 + [70, 70, 70]
    assert fit_threshold(neg2, 0.05) == 70 and flag_rate(neg2, 70) == 0.0
    assert fit_threshold(neg2, 0.15) == 1 and flag_rate(neg2, 1) == 0.15
    assert fit_threshold([], 0.05) is None
    assert fit_threshold([7, 7, 7], 0.0) == 7
    # a positive equal to tau is not flagged
    assert flag_rate([50, 51], 50) == 0.5


def test_auroc_and_selection(fx):
    assert auroc([2, 3], [1, 1]) == 1.0 and auroc([1], [1]) == 0.5 and auroc([], [1]) is None
    *_, c_rows, r_rows = fx
    sc = Scores(c_rows, r_rows)
    det, aucs = select_detector(sc, lambda e: True)
    assert det == "c" and aucs["c"] > aucs["r"] == 0.5
    # tie -> C
    sc2 = Scores([], r_rows)
    assert select_detector(sc2, lambda e: True)[0] == "r"
    pos, neg = sc.calibration_sets("c", lambda e: True)
    assert len(neg) == 3 * 7                      # clean stores only
    assert len(pos) == 3 * 5 * 3                  # forged entries T0-T2 only


def test_apply_gate():
    store = ["a", "b", None, "d"]
    new, rep = apply_gate(store, [10, 60, 99, None], 50, ["A", "B", "C", "D"])
    assert new == ["a", "B", None, "d"] and rep == [1]
    new, rep = apply_gate(store, [60, 0, 0, 0], 50, [None, "B", "C", "D"])
    assert new == [None, "b", None, "d"] and rep == [0]       # no re-derived note: entry removed
    assert apply_gate(store, [99] * 4, None, store) == (store, [])  # no threshold: gate off


# ------------------------------------------------------------------ store variants
def _build(fx, conditions, gate_det="c", ep_i=0, key=None):
    eps, genuine, red, forged, c_rows, r_rows = fx
    ep = eps[ep_i]
    sc = Scores(c_rows, r_rows)
    pos, neg = sc.calibration_sets(gate_det, lambda e: True)
    gate = {"detector": gate_det, "tau": fit_threshold(neg), "scores": sc}
    counts = Counter()
    specs = P.build_stores(ep, genuine[ep.episode_id], red[ep.episode_id], forged_index(forged), conditions,
                           key or new_key(), gate, counts)
    return ep, genuine[ep.episode_id], red[ep.episode_id], specs, counts, gate


def test_store_variants_per_condition(fx):
    ep, g, red, specs, counts, gate = _build(fx, P.CONDITIONS)
    by = {(s.condition, s.store): s for s in specs}
    valid = {(f["edit_type"], f["tier"]) for f in fx[3] if f["episode_id"] == ep.episode_id and f["valid"]}
    # none
    assert by[("none", "clean")].notes == g and by[("none", "clean")].tags is None
    for e in EDIT_TYPES:
        slot = ep.edits[e].session_idx
        for tier in P.NONE_TIERS:
            if (e, tier) in valid:
                s = by[("none", f"{e}:{tier}")]
                assert s.notes[slot] != g[slot] and [n for i, n in enumerate(s.notes) if i != slot] == \
                    [n for i, n in enumerate(g) if i != slot]
        assert ("none", f"{e}:T1") not in by
        # no_memory
        s = by[("no_memory", f"minus:{e}")]
        assert s.notes[slot] is None and sum(n is None for n in s.notes) == 1
        # G2u: tags identical to the clean store's, policy unsigned
        if (e, "T2") in valid:
            s = by[("G2u", f"{e}:T2")]
            assert s.policy == POLICY_UNSIGNED and s.tags == by[("G2u", "clean")].tags
            assert all(t.startswith("author=self") for t in s.tags)
            s = by[("G2s", f"{e}:T2")]
            assert s.policy == POLICY_SIGNED and s.invalid_slots == [slot]
            assert "signature=INVALID" in s.tags[slot]
            s = by[("G2s_insider", f"{e}:T2")]
            assert s.invalid_slots == [] and all("signature=VALID" in t for t in s.tags)
            assert s.notes == by[("G2s", f"{e}:T2")].notes
        s = by[("G1+G2s", f"fix:{e}")]
        assert s.notes == store_with(g, slot, red[slot]) and s.replaced_slots == [slot] and s.tier is None
        assert all("signature=VALID" in t for t in s.tags)
    assert by[("G2s", "clean")].invalid_slots == []
    # G1: forged slots with C score 80 (p_supported 20) are replaced, E5 (p_supported 90) is missed;
    # genuine entries 80..98 -> tau fit on clean negatives
    for e in EDIT_TYPES:
        slot = ep.edits[e].session_idx
        s = by.get(("G1", f"{e}:T0"))
        if s is None:
            continue
        assert s.detector == "c"
        if e == "E5":
            assert slot not in s.replaced_slots
        else:
            assert slot in s.replaced_slots and s.notes[slot] == red[slot]


def test_cache_equivalence_g1_nothing_flagged(fx):
    """A G1 store with nothing flagged produces a byte-identical prompt to the `none` store."""
    ep, g, red, specs, counts, gate = _build(fx, ["none", "G1"])
    by = {(s.condition, s.store): s for s in specs}
    n_same = 0
    for (cond, store), s in by.items():
        if cond != "G1":
            continue
        base = by.get(("none", store))
        if base is None:
            continue
        same = P.prompt_of(ep, s) == P.prompt_of(ep, base)
        assert same == (not s.replaced_slots)
        n_same += same
    assert n_same >= 1  # at least the E5 stores / the clean store are unflagged


def test_prompt_contains_tags_and_policy(fx):
    ep, g, red, specs, counts, gate = _build(fx, ["G2s"])
    s = [x for x in specs if x.store != "clean"][0]
    instr, body = P.prompt_of(ep, s)
    assert POLICY_SIGNED in instr and "signature=INVALID" in body
    # exactly the 5 questions in question_order
    qs = [ep.edits[e].question.text for e in question_order(ep)]
    pos = [body.index(q) for q in qs]
    assert pos == sorted(pos) and "SITUATION 5" in body and "SITUATION 6" not in body


# ------------------------------------------------------------------ rows and scoring
def test_rows_schema_and_attack_scoring(fx):
    ep, g, red, specs, counts, gate = _build(fx, ["none"])
    s = [x for x in specs if x.store.startswith("E1:")][0]
    order = question_order(ep)
    parsed = {k: {"answer": ep.edits[e].question.attacked if e == "E1" else ep.edits[e].question.correct,
                  "confidence": 70} for k, e in enumerate(order, 1)}
    rows = P.rows_for(ep, s, {"job_id": "x", "parsed": json.loads(json.dumps(parsed))})  # str keys as on disk
    assert len(rows) == 5
    req = {"episode_id", "family", "condition", "target_edit", "tier", "q_edit", "answer", "correct", "attacked",
           "confidence", "replaced_slots"}
    assert all(req <= set(r) for r in rows)
    t = [r for r in rows if r["is_target"]]
    assert len(t) == 1 and t[0]["q_edit"] == "E1" and t[0]["attacked"] is True and t[0]["correct"] is False
    assert all(r["correct"] and not r["attacked"] for r in rows if not r["is_target"])
    # unparsed -> None, nothing imputed
    rows = P.rows_for(ep, s, {"job_id": "x", "parsed": None})
    assert all(r["answer"] is None and r["correct"] is None and r["attacked"] is None for r in rows)


# ------------------------------------------------------------------ fake client, dedup, end to end
class FakeClient:
    """Emulates the response cache: identical (instructions, input) requests are served without a request."""
    total_concurrency = 4

    def __init__(self):
        self.cache, self.requests = {}, 0

    def flush_ledger(self):
        pass

    async def complete(self, model, input, instructions=None, **kw):
        k = (model, instructions, input, kw.get("sample_idx"))
        if k in self.cache:
            return Completion(text=self.cache[k], cached=True, model=model, status="completed")
        self.requests += 1
        n = input.count("SITUATION ")
        # answers "A" everywhere, except "B" whenever an INVALID tag is present (exercises policy branches)
        a = "B" if "signature=INVALID" in input else "A"
        text = json.dumps({"answers": {str(i): {"answer": a, "confidence": 60} for i in range(1, n + 1)}})
        self.cache[k] = text
        return Completion(text=text, model=model, status="completed",
                          usage={"input_tokens": 100, "output_tokens": 20, "reasoning_tokens": 5}, cost=1e-5)


def test_dedup_runs_each_distinct_prompt_once(fx, tmp_path):
    ep, g, red, specs, counts, gate = _build(fx, P.CONDITIONS)
    jobs = P.make_jobs("pilot", "deepseek-v4-flash", {ep.episode_id: ep}, specs)
    n_unique = len({(j.instructions, j.input) for j in jobs})
    assert n_unique < len(jobs)
    fc = FakeClient()
    raw = asyncio.run(P.run_dedup(fc, jobs, tmp_path / "p4_gate.jsonl", "t"))
    assert fc.requests == n_unique and len(raw) == len(jobs)
    assert all(r["parsed"] for r in raw.values())
    j = jobs[0]
    assert j.job_id.startswith("p4_gate|deepseek-v4-flash|") and j.tag == "pilot:p4_gate"
    from memlab.clients.adaption import STUDY_EXTRA, STUDY_MAX_OUTPUT_TOKENS
    assert j.extra == STUDY_EXTRA["deepseek-v4-flash"] and j.max_output_tokens == STUDY_MAX_OUTPUT_TOKENS
    # rerun costs nothing
    fc2 = FakeClient()
    asyncio.run(P.run_dedup(fc2, jobs, tmp_path / "p4_gate.jsonl", "t"))
    assert fc2.requests == 0


def test_end_to_end_run_victim(fx, tmp_path, monkeypatch):
    eps, genuine, red, forged, c_rows, r_rows = fx
    pd, rd = tmp_path / "proc", tmp_path / "raw"
    pd.mkdir(); rd.mkdir()
    (pd / "notes.json").write_text(json.dumps({"genuine": genuine, "rederived": red}))
    monkeypatch.setattr(P, "proc_dir", lambda run, v: pd)
    monkeypatch.setattr(P, "raw_dir", lambda run, v: rd)
    monkeypatch.setattr(P, "run_episodes", lambda run, v: list(eps))
    monkeypatch.setattr(P, "load_notes", lambda run, v, kind="genuine": {"genuine": genuine, "rederived": red}[kind])
    monkeypatch.setattr(P, "load_forged", lambda run, v: forged)
    monkeypatch.setattr(P, "load_scores", lambda run, v: Scores(c_rows, r_rows))
    fc = P.TimingClient(FakeClient())
    P.run_victim("pilot", "deepseek-v4-flash", list(P.CONDITIONS), None, None, new_key(), fc, calib_all=True)
    rows = [json.loads(l) for l in open(pd / "p4.jsonl")]
    meta = json.loads((pd / "p4_gate_meta.json").read_text())
    assert meta["gate"]["selected_detector"] == "c" and meta["gate"]["fits"]["c"]["fpr_calib"] <= 0.05
    assert meta["answer_calls"]["parse_rate"] == 1.0
    assert {r["condition"] for r in rows} == set(P.CONDITIONS)
    assert len(rows) % 5 == 0
    # G2s attacked stores: fake answers B (tag INVALID present)
    assert all(r["answer"] == "B" for r in rows if r["condition"] == "G2s" and r["store"] != "clean")
    summ = P.summarize(rows, "pilot")
    assert any(s["condition"] == "none" and s["tier"] == "T0" for s in summ)
    # merge: running one condition again keeps the others
    P.run_victim("pilot", "deepseek-v4-flash", ["no_memory"], 1, None, new_key(), fc, calib_all=True)
    rows2 = [json.loads(l) for l in open(pd / "p4.jsonl")]
    assert len(rows2) == len(rows)
