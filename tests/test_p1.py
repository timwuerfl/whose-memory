"""Offline tests for experiments/p1_self_trust.py, head-to-head design (no API calls; a fake client)."""
from __future__ import annotations

import asyncio
import json
import re
from collections import Counter

import pytest

from experiments import p1_self_trust as P
from memlab.clients.adaption import Completion
from memlab.clients.jobs import load_rows, run_jobs
from memlab.config import HOSTED_VICTIMS, P1_EXTRA_VICTIMS, P1_SEEDS
from memlab.data import episodes
from memlab.prompts import P1_CHANNELS


@pytest.fixture(scope="module")
def main_eps():
    return episodes(P1_SEEDS)          # 120 items


@pytest.fixture(scope="module")
def eps(main_eps):
    return main_eps[::8] + episodes(range(0, 6))


def _items(inp: str) -> str:
    return inp.split("\n\n---\nTASK")[0]


def _blocks(items: str) -> list:
    return re.split(r"\n\n(?=\(\d\)\n)", items)


# ---------------------------------------------------------------- trial set
def test_trials_per_item(eps):
    for ep in eps:
        ts = P.item_trials(ep)
        c = Counter(t.design for t in ts)
        assert c["pair"] == 10 and c["framing"] == 4 and c["turn"] == 2 and c["forced"] == 3 and c["stale"] == 3
        assert c["single"] == (2 if P.has_single(ep) else 0)
        pairs = [(t.ch_a, t.ch_b) for t in ts if t.design == "pair"]
        assert len(set(pairs)) == 10 and set(P.FIXED_PAIRS) <= set(pairs)
        for t in ts:
            if t.ch_b is not None:
                assert P1_CHANNELS.index(t.ch_a) < P1_CHANNELS.index(t.ch_b)   # A earlier in P1_CHANNELS
        assert len({t.key for t in ts}) == len(ts)


def test_rotating_pairs_balance(main_eps):
    c = Counter(p for ep in main_eps for p in P.rotating_pairs(ep))
    assert set(c) == set(P.ROTATING_PAIRS)
    exp = 2 * len(main_eps) / 13                       # ~18.5
    assert all(0.85 * exp <= c[p] <= 1.15 * exp for p in P.ROTATING_PAIRS), c


# ---------------------------------------------------------------- byte identity / rendering
def test_two_claims_identical_up_to_value(eps):
    for ep in eps:
        cb = P.item_cb(ep)
        tmpl = ep.p1.claim_template
        for t in P.item_trials(ep, ("pair", "forced")):
            _, inp, kinds = P.build_trial(ep, t, cb)
            items = _items(inp)
            ca, cb_ = tmpl.format(value=t.value_a), tmpl.format(value=t.value_b)
            assert ca != cb_ and items.count(ca) == 1 and items.count(cb_) == 1
            bl = _blocks(items)
            ia = [i for i, b in enumerate(bl) if ca in b][0]
            ib = [i for i, b in enumerate(bl) if cb_ in b][0]
            assert {ia, ib} == {2, 4} and (ia < ib) == t.a_first      # fixed slots, position by a_first
            # the claim line is the bare sentence in neutral framing
            assert ca in bl[ia].split("\n") and cb_ in bl[ib].split("\n")
            assert [kinds[k] for k in "ABCD"] == [("distractor2" if (k == "escalate" and t.design == "forced") else k)
                                                  for k in cb["option_order"]]


def test_value_options_and_controls(eps):
    for ep in eps:
        cb = P.item_cb(ep)
        it = ep.p1
        for t in P.item_trials(ep):
            _, inp, kinds = P.build_trial(ep, t, cb)
            text = inp if isinstance(inp, str) else inp[-1]["content"]
            opts = dict(re.findall(r"^([ABCD])\. (.*)$", text.split("Options:")[1], re.M))
            lab = {v: k for k, v in kinds.items()}
            assert opts[lab["a"]] == it.option_template.format(value=t.value_a)
            assert opts[lab["b"]] == it.option_template.format(value=t.value_b)
            assert {t.value_a, t.value_b} == {it.value_a, it.value_b}
            if t.design == "forced":
                assert opts[lab["distractor2"]] == it.option_template.format(value=P.distractor2(ep))
                assert it.escalate_option not in text
            else:
                assert opts[lab["escalate"]] == it.escalate_option
            if t.design == "turn":
                assert [m["role"] for m in inp] == ["user", "assistant", "user"]
                assert inp[1]["content"] == it.claim_template.format(value=t.value_a)
                assert it.claim_template.format(value=t.value_a) not in inp[2]["content"]
            if t.design == "single":
                assert it.claim_template.format(value=t.value_a) in text
                assert it.claim_template.format(value=t.value_b) not in text
            if t.design == "framing":
                fp_val = t.value_a if t.framing_a == "first_person" else t.value_b
                assert f"I verified this earlier: {it.claim_template.format(value=fp_val)}" in text
                assert text.count("I verified this earlier") == 1


def test_distractor2_distinct():
    for ep in episodes(range(0, 6)) + episodes(P1_SEEDS):
        assert P.distractor2(ep) not in {ep.p1.value_a, ep.p1.value_b, ep.p1.distractor}


# ---------------------------------------------------------------- counterbalancing
def test_pair_counterbalancing_reused_across_designs(eps):
    for ep in eps:
        ts = P.item_trials(ep)
        ref = {(t.ch_a, t.ch_b): (t.value_a, t.value_b, t.a_first) for t in ts if t.design == "pair"}
        for t in ts:
            if t.design in ("framing", "forced"):
                assert (t.value_a, t.value_b, t.a_first) == ref[(t.ch_a, t.ch_b)]
            if t.design == "turn":
                assert (t.value_a, t.value_b) == ref[(t.ch_a, t.ch_b)][:2]
        jobs = P.pair_jobs([ep], "deepseek-v4-flash", "pilot")
        assert len({json.dumps(j.meta["option_order"]) for j in jobs}) == 1
        assert len({j.meta["variant"] for j in jobs}) == 1


def test_balance_120(main_eps):
    assert len(main_eps) == 120
    n = len(main_eps)
    # per pair: A carries value_a about half the time, A shown first about half the time
    for a, b in P.FIXED_PAIRS:
        cbs = [P.pair_cb(ep, a, b) for ep in main_eps]
        assert 0.35 * n <= sum(c["value_a"] == ep.p1.value_a for c, ep in zip(cbs, main_eps)) <= 0.65 * n
        assert 0.35 * n <= sum(c["a_first"] for c in cbs) <= 0.65 * n
    allp = [(ep, t) for ep in main_eps for t in P.item_trials(ep, ("pair",))]
    m = len(allp)
    assert 0.45 * m <= sum(t.value_a == ep.p1.value_a for ep, t in allp) <= 0.55 * m
    assert 0.45 * m <= sum(t.a_first for _, t in allp) <= 0.55 * m
    for kind in P.KINDS:
        pos = Counter(P.item_cb(ep)["option_order"].index(kind) for ep in main_eps)
        assert all(0.15 * n <= pos[i] <= 0.35 * n for i in range(4)), (kind, pos)
    assert 0.2 * n <= sum(P.has_single(ep) for ep in main_eps) <= 0.47 * n


# ---------------------------------------------------------------- victims
def test_default_victims():
    assert P.default_victims("main") == list(HOSTED_VICTIMS) + [v for v in P1_EXTRA_VICTIMS if v not in HOSTED_VICTIMS]
    assert P.default_victims("pilot") == ["deepseek-v4-flash", "gemma-4-31b-it"]
    assert len(P.select_episodes("pilot", "deepseek-v4-flash", 3)) == 9


# ---------------------------------------------------------------- end to end with a fake client
class FakeClient:
    total_concurrency = 4

    def __init__(self):
        self.calls = []

    def flush_ledger(self):
        pass

    async def complete(self, model, input, instructions=None, **kw):
        self.calls.append((model, input, instructions, kw))
        i = len(self.calls)
        if sum(map(ord, json.dumps(input))) % 9 == 0:   # degenerate loop: text at the output cap, never parseable
            return Completion(text="our " * 50, cost=0.001, model=model, status="incomplete",
                              usage={"input_tokens": 300, "output_tokens": kw["max_output_tokens"], "reasoning_tokens": 0})
        if "<A|B>" in str(input):
            text = json.dumps({"answer": "AB"[i % 2], "confidence": 70})
        else:
            text = json.dumps({"answer": "ABCD"[i % 4], "confidence": 55})
        return Completion(text=text, reasoning="thinking...", cost=0.001, model=model, status="completed",
                          usage={"input_tokens": 300, "output_tokens": 20, "reasoning_tokens": 10})


def test_rows_schema_end_to_end(tmp_path, eps):
    from memlab.clients.adaption import STUDY_EXTRA, STUDY_MAX_OUTPUT_TOKENS
    fc = FakeClient()
    jobs = P.pair_jobs(eps[:3], "gemma-4-31b-it", "pilot")
    out = tmp_path / "raw.jsonl"
    res = asyncio.run(run_jobs(fc, jobs, out, parse=P.parse_p1, max_parse_retries=P.MAX_PARSE_RETRIES))
    assert len(fc.calls) <= 2 * len(jobs)
    rows = [P.pair_row(r, STUDY_MAX_OUTPUT_TOKENS) for r in res]
    assert len(rows) == len(jobs)
    for r in rows:
        assert list(r) == list(P.PAIR_FIELDS)
        if r["answer"] is None:
            assert r["followed"] is None and r["error"]
        else:
            assert r["answer_kind"] in ("a", "b", "distractor", "escalate", "distractor2")
            if r["answer_kind"] == "a":
                assert r["followed"] == r["ch_a"]
            elif r["answer_kind"] == "b":
                assert r["followed"] == (r["ch_b"] if r["design"] != "single" else "other_value")
            else:
                assert r["followed"] == r["answer_kind"]
    assert any(r["error"] and r["error"].startswith("degenerate") for r in rows)
    for model, inp, ins, kw in fc.calls:
        assert kw["extra"] == STUDY_EXTRA[model] and kw["max_output_tokens"] == STUDY_MAX_OUTPUT_TOKENS
        assert kw["tag"] == "pilot:p1_pairs" and kw["temperature"] == 0.0
    assert all(j.job_id.startswith("p1_pairs|") for j in jobs)
    # summary runs
    s = P.summarize(rows, "t")
    assert "HEADLINE" in s and "win matrix" in s

    # degenerate rows that ended as errors are not retried on a rerun
    out = tmp_path / "raw_degenerate.jsonl"
    with open(out, "a") as f:
        f.write(json.dumps({"job_id": jobs[0].job_id, "error": "incomplete: {\"reason\": \"max_output_tokens\"}",
                            "usage": {"output_tokens": STUDY_MAX_OUTPUT_TOKENS}, "meta": jobs[0].meta,
                            "parsed": None}) + "\n")
    todo, frozen = P.split_done_degenerate(jobs, out, STUDY_MAX_OUTPUT_TOKENS)
    assert jobs[0].job_id not in {j.job_id for j in todo} and len(frozen) == 1

    fc2 = FakeClient()
    cj = P.conf_jobs(eps[:3], "gemma-4-31b-it", "pilot")
    cres = asyncio.run(run_jobs(fc2, cj, tmp_path / "raw2.jsonl", parse=P.parse_conf, max_parse_retries=0))
    crow = [P.conf_row(r) for r in cres]
    assert len(crow) == 12
    for r in crow:
        assert set(P.CONF_FIELDS) <= set(r) and r["act"] in (True, False, None)
    assert "hedged" in P.summarize_conf(crow, "t")


# ---------------------------------------------------------------- staleness control
def test_stale_differs_only_in_b_header(eps):
    for ep in eps:
        cb = P.item_cb(ep)
        ts = P.item_trials(ep)
        ref = {(t.ch_a, t.ch_b): t for t in ts if t.design == "pair"}
        stale = [t for t in ts if t.design == "stale"]
        assert [(t.ch_a, t.ch_b) for t in stale] == [("memory", b) for b in P.STALE_B]
        for t in stale:
            n = ref[(t.ch_a, t.ch_b)]
            assert (t.value_a, t.value_b, t.a_first, t.framing_a, t.framing_b) == \
                   (n.value_a, n.value_b, n.a_first, n.framing_a, n.framing_b)       # counterbalancing reused
            ins_s, inp_s, k_s = P.build_trial(ep, t, cb)
            ins_n, inp_n, k_n = P.build_trial(ep, n, cb)
            assert ins_s == ins_n and k_s == k_n
            ls, ln = inp_s.split("\n"), inp_n.split("\n")
            assert len(ls) == len(ln)
            diff = [i for i, (x, y) in enumerate(zip(ls, ln)) if x != y]
            assert len(diff) == 1                                   # exactly one line differs ...
            i = diff[0]
            claim_b = ep.p1.claim_template.format(value=t.value_b)
            assert ls[i + 1] == claim_b and ln[i + 1] == claim_b     # ... the header right above B's claim
            assert any(w in ls[i].lower() for w in ("earlier", "previous")) and "earlier" not in ln[i].lower()


def test_stale_job_ids_distinct_and_resumable(eps):
    jobs = P.pair_jobs(eps[:2], "deepseek-v4-flash", "main")
    pair_ids = {j.job_id for j in jobs if j.meta["design"] == "pair"}
    stale_ids = {j.job_id for j in jobs if j.meta["design"] == "stale"}
    assert len(stale_ids) == 6 and not (pair_ids & stale_ids)
    assert len({j.job_id for j in jobs}) == len(jobs)
    # job ids of the earlier designs are unchanged by adding `stale` (finished main-run rows stay valid)
    old = P.pair_jobs(eps[:2], "deepseek-v4-flash", "main", ("pair", "framing", "turn", "forced", "single"))
    assert {j.job_id for j in old} == {j.job_id for j in jobs} - stale_ids
    assert {j.job_id: j.input for j in old} == {j.job_id: j.input for j in jobs if j.job_id not in stale_ids}


def test_stale_summary_block(eps):
    rows = []
    for ep in eps[:4]:
        for t in P.item_trials(ep, ("pair", "stale")):
            rows.append({"episode_id": ep.episode_id, "family": ep.family, "design": t.design, "ch_a": t.ch_a,
                         "ch_b": t.ch_b, "framing_a": t.framing_a, "framing_b": t.framing_b, "value_a": t.value_a,
                         "value_b": t.value_b, "a_first": t.a_first, "variant": 0, "option_order": [],
                         "answer": "A", "answer_kind": "b", "followed": t.ch_b, "confidence": 50, "error": None})
    s = P.summarize(rows, "t")
    assert "staleness control" in s and "vs document" in s.split("staleness control")[1]
