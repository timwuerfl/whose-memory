"""Offline tests for experiments/hosted_gen.py (fake client, no network)."""
from __future__ import annotations

import asyncio
import json
import re
from types import SimpleNamespace

import pytest

from experiments import hosted_gen as hg
from memlab import data
from memlab.config import T3_CALLS, T3_VERSIONS_PER_CALL, t1_forger_for
from memlab.schema import EDIT_TYPES

VICTIMS = ["deepseek-v4-flash", "gemma-4-31b-it"]
STUDY_EXTRA = {m: {"reasoning": {"effort": "low"}} for m in
               ("deepseek-v4-flash", "gemma-4-31b-it", "gemma-4-26b-a4b-it", "glm-5.3-flash")}


class FakeClient:
    """Answers by prompt type. `bad_first` makes the first T2 attempt of every episode omit E1's target
    value (invalid); `ratings` maps a candidate text to a rating (default 50)."""

    def __init__(self, bad_first=True, rating_fn=None, fail_notes=()):
        self.log = []
        self.bad_first = bad_first
        self.rating_fn = rating_fn or (lambda text: 50)
        self.fail_notes = set(fail_notes)
        self.total_concurrency = 4

    def flush_ledger(self):
        pass

    async def complete(self, model, input, instructions=None, *, max_output_tokens=1024, temperature=0.0,
                       sample_idx=0, tag="", extra=None):
        self.log.append(SimpleNamespace(model=model, input=input, temperature=temperature,
                                          sample_idx=sample_idx, tag=tag, extra=extra,
                                          max_output_tokens=max_output_tokens))
        return SimpleNamespace(text=self._answer(model, input, sample_idx), reasoning="", cost=0.0, cached=False,
                               error=None, usage={"input_tokens": 1, "output_tokens": 1, "reasoning_tokens": 0})

    def _answer(self, model, inp, sample_idx):
        if "Write your memory note" in inp:
            title = inp.splitlines()[0]
            if title in self.fail_notes:
                return "sorry"
            return json.dumps({"note": f"My note for {title} (sample {sample_idx}): nothing special happened."})
        if "Rate each candidate" in inp:
            cands = re.findall(r"\| CANDIDATE (\d+)\]\n(.*)", inp)
            return json.dumps({"ratings": {k: self.rating_fn(t) for k, t in cands}})
        if "TARGET CONTENT" in inp:
            targets = re.findall(r"TARGET CONTENT (\d+)\n(.*)", inp)
            two = "differently worded rewrites" in inp
            styled = "your own note-writing style" in inp
            notes = {}
            for k, t in targets:
                txt = f"Forged note {k}: {t}"
                if styled and not two and self.bad_first and sample_idx == 0 and k == "1":
                    txt = "Forged note without the target value, which is long enough."
                notes[k] = [txt + " (a)", txt + " (b)"] if two else txt
            return json.dumps({"notes": notes})
        raise AssertionError("unexpected prompt")


@pytest.fixture
def tmp_root(tmp_path, monkeypatch):
    monkeypatch.setattr(data, "ROOT", tmp_path)
    monkeypatch.setattr(hg, "_study_settings", lambda: (STUDY_EXTRA, 4096))
    return tmp_path


def run_stages(client, stages, victims=VICTIMS, limit=1):
    return asyncio.run(hg.run_stages("pilot", victims, stages, limit, client))


# ------------------------------------------------------------------------------------------ job construction
def test_note_jobs_construction(tmp_root):
    eps = hg.episodes_for("pilot", VICTIMS[0], "seeds", 1)
    assert [e.family for e in eps] == ["inventory", "research", "assistant"]
    jobs = hg.note_jobs("pilot", VICTIMS[0], eps, 0, "note")
    assert len(jobs) == 3 * 7 and len({j.job_id for j in jobs}) == len(jobs)
    j = jobs[0]
    assert j.job_id == f"hosted_gen|{VICTIMS[0]}|{eps[0].episode_id}|note|s0|k0"
    assert j.tag == "pilot:hosted_gen" and j.extra == STUDY_EXTRA[VICTIMS[0]] and j.max_output_tokens == 4096
    assert j.temperature == 0.7 and j.sample_idx == 0 and j.meta["pkey"] == ["note"]


def test_forge_jobs_and_request_counts(tmp_root):
    client = FakeClient(bad_first=False)
    run_stages(client, ["notes", "rederive", "forge"])
    by = lambda pred: [c for c in client.log if pred(c)]
    for v in VICTIMS:
        notes = by(lambda c: c.model == v and "Write your memory note" in c.input)
        assert len(notes) == 3 * 7 + 3 * 7 + 3 * 7          # genuine + style (limit 1) + rederived
        assert sorted({c.sample_idx for c in notes}) == [0, 1]
        t1 = by(lambda c: c.model == t1_forger_for(v) and "TARGET CONTENT" in c.input
                and c.tag == "pilot:hosted_gen")
        # T1 forger may be shared between victims? not here: deepseek -> gemma-26b, gemma-31b -> glm
        assert len(t1) == 3 and all("own note-writing style" not in c.input for c in t1)
        t2 = by(lambda c: c.model == v and "TARGET CONTENT" in c.input and "differently worded" not in c.input)
        assert len(t2) == 3 and all(c.temperature == 0.7 for c in t2)
        assert all(c.input.count("EXAMPLE ") == 3 for c in t2)
        t3 = by(lambda c: c.model == v and "differently worded" in c.input)
        assert len(t3) == 3 * T3_CALLS and all(c.temperature == 1.0 for c in t3)
        assert sorted({c.sample_idx for c in t3}) == list(range(T3_CALLS))
        rank = by(lambda c: c.model == v and "Rate each candidate" in c.input)
        assert len(rank) == 3 * 5 and all(c.temperature == 0.0 for c in rank)
        assert all(f"CANDIDATE {T3_CALLS * T3_VERSIONS_PER_CALL}]" in c.input for c in rank)
    # T1 items in EDIT_TYPES order
    ep = hg.episodes_for("pilot", VICTIMS[0], "seeds", 1)[0]
    c = by(lambda c: c.model == t1_forger_for(VICTIMS[0]) and ep.edits["E1"].forged_content in c.input)[0]
    pos = [c.input.index(ep.edits[et].forged_content) for et in EDIT_TYPES]
    assert pos == sorted(pos)


def test_forge_requires_notes(tmp_root):
    with pytest.raises(hg.StageInputMissing):
        run_stages(FakeClient(), ["forge"])


# ------------------------------------------------------------------------------------------ resume
def test_resume_costs_nothing(tmp_root):
    c1 = FakeClient()
    run_stages(c1, ["notes", "rederive", "forge"])
    c2 = FakeClient()
    run_stages(c2, ["notes", "rederive", "forge"])
    assert len(c1.log) > 0 and c2.log == []
    # the tidy outputs are rebuilt identically from the raw rows
    f = data.read_jsonl(data.proc_dir("pilot", VICTIMS[0]) / "forged.jsonl")
    assert len(f) == 3 * 5 * 4


def test_partial_resume(tmp_root):
    run_stages(FakeClient(), ["notes"], victims=VICTIMS[:1])
    c = FakeClient()
    run_stages(c, ["notes"])
    assert {x.model for x in c.log} == {VICTIMS[1]}


# ------------------------------------------------------------------------------------------ validity retry
def test_validity_retry(tmp_root):
    client = FakeClient(bad_first=True)
    out = run_stages(client, ["notes", "forge"], victims=VICTIMS[:1])
    v = VICTIMS[0]
    t2 = [c for c in client.log if c.model == v and "TARGET CONTENT" in c.input and "differently" not in c.input]
    assert sorted(c.sample_idx for c in t2) == [0, 0, 0, 1, 1, 1]       # one re-ask per episode
    rows = data.read_jsonl(data.proc_dir("pilot", v) / "forged.jsonl")
    e1 = [r for r in rows if r["tier"] == "T2" and r["edit_type"] == "E1"]
    assert all(r["valid"] and r["attempts"] == 2 for r in e1)
    others = [r for r in rows if r["tier"] == "T2" and r["edit_type"] != "E1"]
    assert all(r["valid"] and r["attempts"] == 1 for r in others)


def test_merge_attempt_keeps_valid_and_gives_up_after_retries():
    edit = SimpleNamespace(must_contain=["31.56"], must_not_contain=["24.82"])
    items = [("E1", "g", edit)]
    st = {}
    hg.merge_attempt(st, items, {1: ["price was 24.82 dollars"]}, 0)
    assert st["E1"] == {"note": "price was 24.82 dollars", "valid": False, "attempts": 1}
    hg.merge_attempt(st, items, None, 1)                               # unparseable attempt
    assert st["E1"]["note"] == "price was 24.82 dollars" and st["E1"]["attempts"] == 2
    hg.merge_attempt(st, items, {1: ["price was 31.56 dollars"]}, 2)
    assert st["E1"]["valid"] and st["E1"]["note"].endswith("31.56 dollars")
    hg.merge_attempt(st, items, {1: ["price was 24.82 dollars again"]}, 3)
    assert st["E1"]["note"] == "price was 31.56 dollars" and st["E1"]["attempts"] == 3


def test_retries_are_bounded(tmp_root, monkeypatch):
    class AlwaysBad(FakeClient):
        def _answer(self, model, inp, sample_idx):
            if "TARGET CONTENT" in inp and "differently" not in inp:
                n = len(re.findall(r"TARGET CONTENT \d+\n", inp))
                return json.dumps({"notes": {str(k): "An unrelated note that is long enough." for k in range(1, n + 1)}})
            return super()._answer(model, inp, sample_idx)
    client = AlwaysBad()
    run_stages(client, ["notes", "forge"], victims=VICTIMS[:1])
    t1 = [c for c in client.log if c.model == t1_forger_for(VICTIMS[0])]
    assert sorted(c.sample_idx for c in t1) == sorted([0, 1, 2, 3] * 3)    # 1 call + 3 re-asks per episode
    rows = data.read_jsonl(data.proc_dir("pilot", VICTIMS[0]) / "forged.jsonl")
    t1rows = [r for r in rows if r["tier"] == "T1"]
    assert all(not r["valid"] and r["attempts"] == 4 and r["note"] for r in t1rows)


# ------------------------------------------------------------------------------------------ T3 selection
def test_select_t3_highest_rating_ties_first():
    cands = [{"valid": True}, {"valid": False}, {"valid": True}, {"valid": True}]
    order = [3, 0, 2]                       # shown positions 1, 2, 3
    assert hg.select_t3(cands, {1: 40, 2: 70, 3: 60}, order) == 0
    assert hg.select_t3(cands, {1: 90, 2: 70, 3: 90}, order) == 2      # tie 2 vs 3 -> first in original order
    assert hg.select_t3(cands, {1: 80, 2: 80, 3: 80}, order) == 0
    assert hg.select_t3(cands, None, order) == 0
    assert hg.select_t3([{"valid": False}], None, []) is None


def test_t3_end_to_end_selection(tmp_root):
    # rate rewrite "(b)" higher than "(a)"; all candidates of an instance from calls 0..3 -> winner is call 0, (b)
    client = FakeClient(bad_first=False, rating_fn=lambda t: 80 if t.endswith("(b)") else 30)
    run_stages(client, ["notes", "forge"], victims=VICTIMS[:1])
    v = VICTIMS[0]
    t3 = data.read_jsonl(data.proc_dir("pilot", v) / "t3_candidates.jsonl")
    assert len(t3) == 3 * 5 * T3_CALLS * T3_VERSIONS_PER_CALL
    sel = [c for c in t3 if c["selected"]]
    assert len(sel) == 15 and all(c["call_idx"] == 0 and c["version_idx"] == 1 for c in sel)
    forged = [r for r in data.read_jsonl(data.proc_dir("pilot", v) / "forged.jsonl") if r["tier"] == "T3"]
    assert all(r["valid"] and r["n_candidates"] == 8 and r["selected_rating"] == 80 for r in forged)
    # candidate order shown to the rater is shuffled (not identical to original order everywhere)
    shown = [[c["shown_position"] for c in t3 if (c["episode_id"], c["edit_type"]) == k]
             for k in {(c["episode_id"], c["edit_type"]) for c in t3}]
    assert any(s != list(range(8)) for s in shown)


def test_invalid_candidates_excluded_from_ranking(tmp_root):
    class HalfBad(FakeClient):
        def _answer(self, model, inp, sample_idx):
            if "differently worded" in inp:
                d = json.loads(super()._answer(model, inp, sample_idx))
                for k, v in d["notes"].items():       # version (a) loses the target content
                    v[0] = "A rewrite that dropped the target content entirely."
                return json.dumps(d)
            return super()._answer(model, inp, sample_idx)
    client = HalfBad(bad_first=False)
    run_stages(client, ["notes", "forge"], victims=VICTIMS[:1])
    rank = [c for c in client.log if "Rate each candidate" in c.input]
    assert rank and all("dropped the target" not in c.input and "CANDIDATE 4]" in c.input
                        and "CANDIDATE 5]" not in c.input for c in rank)
    forged = [r for r in data.read_jsonl(data.proc_dir("pilot", VICTIMS[0]) / "forged.jsonl") if r["tier"] == "T3"]
    assert all(r["n_candidates"] == 4 for r in forged)


# ------------------------------------------------------------------------------------------ tidy outputs
def test_tidy_output_schema(tmp_root):
    fail = {"SESSION 1: " + hg.episodes_for("pilot", VICTIMS[0], "seeds", 1)[0].sessions[0].title}
    client = FakeClient(fail_notes=fail)
    summ = run_stages(client, ["notes", "rederive", "forge"], victims=VICTIMS[:1])
    v = VICTIMS[0]
    notes = json.loads((data.proc_dir("pilot", v) / "notes.json").read_text())
    assert set(notes) == {"genuine", "style", "rederived"}
    eps = hg.episodes_for("pilot", v, "seeds", 1)
    assert set(notes["genuine"]) == {e.episode_id for e in eps}
    assert all(len(x) == 7 for x in notes["genuine"].values())
    assert notes["genuine"][eps[0].episode_id][0] is None                # parse failure stays missing
    assert len(notes["style"]) == 3
    forged = data.load_forged("pilot", v)
    keys = {"episode_id", "family", "edit_type", "tier", "session_idx", "note", "valid", "mode", "forger",
            "attempts", "n_candidates", "selected_rating"}
    assert all(set(r) == keys for r in forged)
    t0 = [r for r in forged if r["tier"] == "T0"]
    assert all(r["mode"] in ("substitute", "append") for r in t0)
    assert all(r["mode"] is None for r in forged if r["tier"] != "T0")
    # session 0 of the first episode is missing -> its instance is skipped in every tier
    ed0 = [et for et in EDIT_TYPES if eps[0].edits[et].session_idx == 0]
    if ed0:
        assert not [r for r in forged if r["episode_id"] == eps[0].episode_id and r["edit_type"] == ed0[0]]
        assert len(forged) == (3 * 5 - 1) * 4
    t3 = data.read_jsonl(data.proc_dir("pilot", v) / "t3_candidates.jsonl")
    ck = {"episode_id", "family", "edit_type", "session_idx", "cand_idx", "call_idx", "version_idx", "note",
          "valid", "shown_position", "rating", "selected"}
    assert all(set(c) == ck for c in t3)
    raw = data.read_jsonl(data.raw_dir("pilot", v) / "hosted_gen.jsonl")
    assert all(r["job_id"].startswith(f"hosted_gen|{v}|") for r in raw)
    # the unparseable note was retried by the runner (parse=), then recorded with parsed None
    bad = [r for r in raw if r["parsed"] is None]
    assert bad and all(r["attempts"] == 3 for r in bad)
    assert summ[v]["notes_missing"]["genuine"] == (1, 21)


def test_limit_run_does_not_wipe_other_episodes(tmp_root):
    run_stages(FakeClient(), ["notes", "forge"], victims=VICTIMS[:1], limit=2)
    n2 = len(data.load_forged("pilot", VICTIMS[0]))
    run_stages(FakeClient(), ["notes", "forge"], victims=VICTIMS[:1], limit=1)
    assert len(data.load_forged("pilot", VICTIMS[0])) == n2
    assert len(data.load_notes("pilot", VICTIMS[0], "genuine")) == 6
