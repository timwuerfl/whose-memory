"""Offline tests for memlab.clients and memlab.utils.jsonparse (HTTP layer is mocked)."""
from __future__ import annotations

import asyncio
import csv
import json

import httpx
import pytest

from memlab.clients import adaption as ad
from memlab.clients.adaption import AdaptionClient, BudgetExceeded, cache_key, total_spend
from memlab.clients.jobs import Job, load_rows, run, run_jobs
from memlab.utils.jsonparse import get_choice, get_float, get_int, parse_json

FAKE_KEYS = ["sk-test-AAAA", "sk-test-BBBB"]


def ok_body(text="hello", cost=0.001, reasoning="thinking...", status="completed",
            reason="max_output_tokens"):
    out = []
    if reasoning:
        out.append({"type": "reasoning", "content": [{"type": "reasoning_text", "text": reasoning}]})
    if text is not None:
        out.append({"type": "message", "content": [{"type": "output_text", "text": text}]})
    return {"status": status, "output": out, "output_text": text or "",
            "incomplete_details": None if status == "completed" else {"reason": reason},
            "usage": {"input_tokens": 10, "output_tokens": 20,
                      "output_tokens_details": {"reasoning_tokens": 5}, "cost": cost}}


class Handler:
    """Scripted mock: ``script`` is a list of (status_code, body|None) consumed in order; then
    falls back to ``default`` (a function of the request body)."""

    def __init__(self, script=None, default=None):
        self.script = list(script or [])
        self.default = default or (lambda b: (200, ok_body(text=f"echo:{b['input']}")))
        self.calls = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        body = json.loads(request.content)
        self.calls.append({"body": body, "auth": request.headers.get("authorization")})
        code, payload = self.script.pop(0) if self.script else self.default(body)
        headers = {"retry-after": "0"} if code == 429 else {}
        return httpx.Response(code, json=payload if payload is not None else {"error": "x"},
                              headers=headers)


def make_client(tmp_path, handler, **kw):
    kw.setdefault("backoff_base_s", 0.001)
    kw.setdefault("backoff_max_s", 0.01)
    kw.setdefault("rate_state_dir", tmp_path / "rl")
    kw.setdefault("stream", False)
    return AdaptionClient(keys=FAKE_KEYS, cache_path=tmp_path / "c.sqlite",
                          ledger_path=tmp_path / "ledger.csv",
                          transport=httpx.MockTransport(handler), **kw)


def arun(coro):
    return asyncio.run(coro)


# ---------------------------------------------------------------------------- client

def test_cache_hit_miss_and_sample_idx(tmp_path):
    h = Handler()
    c = make_client(tmp_path, h)

    async def go():
        a = await c.complete("m", "hi", "sys")
        b = await c.complete("m", "hi", "sys")
        d = await c.complete("m", "hi", "sys", sample_idx=1)
        e = await c.complete("m", "hi", "sys", temperature=0.5)
        await c.close()
        return a, b, d, e

    a, b, d, e = arun(go())
    assert a.text == "echo:hi" and not a.cached and a.cost == 0.001
    assert a.reasoning == "thinking..." and a.usage["reasoning_tokens"] == 5
    assert b.cached and b.text == a.text
    assert not d.cached and not e.cached
    assert len(h.calls) == 3
    assert "sample_idx" not in h.calls[0]["body"]
    assert h.calls[0]["body"]["instructions"] == "sys"
    # cache hits are not in the ledger
    assert total_spend(tmp_path / "ledger.csv") == pytest.approx(0.003)
    assert cache_key("m", "s", "x", 1, 0, 0, None) != cache_key("m", "s", "x", 1, 0, 1, None)


def test_cache_persists_across_clients(tmp_path):
    h = Handler()
    c1 = make_client(tmp_path, h)
    arun(c1.complete("m", "x"))
    arun(c1.close())
    c2 = make_client(tmp_path, h)
    r = arun(c2.complete("m", "x"))
    assert r.cached and len(h.calls) == 1


def test_retry_on_429_then_success(tmp_path):
    h = Handler(script=[(429, {"error": "rate"}), (503, {"error": "busy"}), (429, None)])
    c = make_client(tmp_path, h)
    r = arun(c.complete("m", "x"))
    assert r.error is None and r.text == "echo:x" and r.attempts == 4
    assert c.stats["http_429"] == 2 and c.stats["http_5xx"] == 1
    # both keys used (round robin), and the key is not leaked in error strings
    assert {x["auth"] for x in h.calls} == {f"Bearer {k}" for k in FAKE_KEYS}


def test_final_failure_returns_error(tmp_path):
    h = Handler(default=lambda b: (500, {"error": "Bearer sk-test-AAAA boom"}))
    c = make_client(tmp_path, h, max_attempts=3)
    r = arun(c.complete("m", "x"))
    assert r.error and "http 500" in r.error and "sk-test-AAAA" not in r.error
    assert len(h.calls) == 3


def test_non_retryable_400(tmp_path):
    h = Handler(default=lambda b: (400, {"error": "unknown param"}))
    c = make_client(tmp_path, h)
    r = arun(c.complete("m", "x"))
    assert r.error.startswith("http 400") and len(h.calls) == 1


def test_incomplete_max_tokens_not_retried(tmp_path):
    h = Handler(default=lambda b: (200, ok_body(text=None, status="incomplete")))
    c = make_client(tmp_path, h)
    r = arun(c.complete("m", "x"))
    assert r.error.startswith("incomplete") and "max_output_tokens" in r.error and len(h.calls) == 1


def test_incomplete_retried_then_error(tmp_path):
    h = Handler(default=lambda b: (200, ok_body(text=None, status="incomplete", reason="other")))
    c = make_client(tmp_path, h)
    r = arun(c.complete("m", "x"))
    assert r.error.startswith("incomplete") and len(h.calls) == 3  # 1 + 2 extra
    # incomplete calls are still billed
    arun(c.close())
    assert total_spend(tmp_path / "ledger.csv") == pytest.approx(0.003)
    # and never cached
    h2 = Handler()
    c2 = make_client(tmp_path, h2)
    assert not arun(c2.complete("m", "x")).cached


def test_timeout_retry(tmp_path):
    n = {"i": 0}

    def handler(req):
        n["i"] += 1
        if n["i"] == 1:
            raise httpx.ReadTimeout("slow", request=req)
        return httpx.Response(200, json=ok_body("fine"))

    c = make_client(tmp_path, handler)
    r = arun(c.complete("m", "x"))
    assert r.text == "fine" and c.stats["timeouts"] == 1


def test_ledger_aggregation_and_budget_guard(tmp_path):
    h = Handler(default=lambda b: (200, ok_body(text="t", cost=0.4)))
    c = make_client(tmp_path, h, budget_cap=1.0)

    async def go():
        for i in range(3):
            await c.complete("m", f"x{i}", tag="t1")
        with pytest.raises(BudgetExceeded):
            await c.complete("m", "x9", tag="t1")
        # cached calls still work after the cap
        r = await c.complete("m", "x0", tag="t1")
        assert r.cached
        await c.close()

    arun(go())
    rows = list(csv.DictReader(open(tmp_path / "ledger.csv")))
    assert set(rows[0]) == set(ad.LEDGER_COLUMNS)
    assert sum(int(r["n_calls"]) for r in rows) == 3
    assert {r["key_slot"] for r in rows} <= {"1", "2"}
    assert len(rows) <= 2  # aggregated per (minute, slot, model, tag) (minute boundary aside)
    assert sum(int(r["input_tokens"]) for r in rows) == 30
    assert total_spend(tmp_path / "ledger.csv") == pytest.approx(1.2)
    # a new client sees the persisted spend and refuses immediately
    c2 = make_client(tmp_path, h, budget_cap=1.0)
    with pytest.raises(BudgetExceeded):
        arun(c2.complete("m", "new"))


def test_rpm_limiter(tmp_path):
    import time as _t
    h = Handler()
    c = AdaptionClient(
        keys=FAKE_KEYS[:1], cache_path=None, use_cache=False, ledger_path=tmp_path / "l.csv",
        rpm_per_key=3, transport=httpx.MockTransport(h), rate_state_dir=tmp_path / "rl", stream=False,
        rate_window_s=0.4)

    async def go():
        t0 = _t.monotonic()
        await asyncio.gather(*[c.complete("m", f"x{i}") for i in range(7)])
        return _t.monotonic() - t0

    dt = arun(go())
    assert len(h.calls) == 7 and dt >= 0.8  # 3 + 3 + 1 across three windows


def test_both_keys_balanced(tmp_path):
    h = Handler()
    c = make_client(tmp_path, h, use_cache=False, rpm_per_key=None)

    async def go():
        await asyncio.gather(*[c.complete("m", f"x{i}") for i in range(20)])

    arun(go())
    auths = [x["auth"] for x in h.calls]
    assert abs(auths.count(f"Bearer {FAKE_KEYS[0]}") - auths.count(f"Bearer {FAKE_KEYS[1]}")) <= 2


def test_keys_weighted_by_rpm(tmp_path):
    h = Handler()
    c = make_client(tmp_path, h, use_cache=False, rpm_per_key={1: 40, 2: 20})

    async def go():
        for i in range(30):
            await c.complete("m", f"x{i}")

    arun(go())
    auths = [x["auth"] for x in h.calls]
    assert auths.count(f"Bearer {FAKE_KEYS[0]}") == 20 and auths.count(f"Bearer {FAKE_KEYS[1]}") == 10


def test_adaptive_throttle_lowers_limit(tmp_path):
    s = ad._KeySlot(1, "k", 16, rpm=50, state_dir=tmp_path)
    for _ in range(3):
        s.on_429()
    assert s.limit == 8 and s.rpm == 40


class FakeClock:
    def __init__(self, t=1000.0):
        self.t = t

    def __call__(self):
        return self.t


def test_shared_window_fake_clock(tmp_path):
    clk = FakeClock()
    w = ad.SharedRateWindow(tmp_path / "w.json", rpm=5, window_s=60, clock=clk)
    assert [w.try_acquire() for _ in range(5)] == [0.0] * 5
    assert w.try_acquire() == pytest.approx(60.0)
    clk.t += 30
    assert w.try_acquire() == pytest.approx(30.0)
    clk.t += 30
    assert w.try_acquire() == 0.0
    # a second instance (= another process) sees the same state
    w2 = ad.SharedRateWindow(tmp_path / "w.json", rpm=5, window_s=60, clock=clk)
    assert w2.snapshot()["used"] == 1
    # 429 burst -> limit 4, recovers after 30 s by 10 %-steps
    for _ in range(3):
        w2.on_429()
    assert w.snapshot()["limit"] == 4 and w.snapshot()["factor"] == pytest.approx(0.8)
    clk.t += 31
    assert w.snapshot()["factor"] == pytest.approx(0.9)
    w.try_acquire()  # persists the recovery
    assert w._locked(w._read)["factor"] == pytest.approx(0.9)
    # corrupted state file is treated as empty
    (tmp_path / "w.json").write_text("{not json")
    assert w.try_acquire() == 0.0


def test_shared_window_async_wait_no_spin(tmp_path):
    clk = FakeClock()
    sleeps = []

    async def fake_sleep(d):
        sleeps.append(d)
        clk.t += d

    w = ad.SharedRateWindow(tmp_path / "w.json", rpm=2, window_s=10, clock=clk, sleep=fake_sleep)

    async def go():
        for _ in range(5):
            await w.acquire()

    arun(go())
    # 5 sends at 2 per 10 s -> exactly two waits of ~10 s, no spinning
    assert len(sleeps) == 2 and all(9.9 < d < 10.6 for d in sleeps)


_PROC_SCRIPT = r"""
import asyncio, json, sys, time
import httpx
sys.path.insert(0, sys.argv[1])
from memlab.clients.adaption import AdaptionClient
stamps = []
def handler(req):
    stamps.append(time.time())
    return httpx.Response(200, json={"status": "completed", "output": [{"type": "message",
        "content": [{"type": "output_text", "text": "ok"}]}], "usage": {"cost": 0.0}})
c = AdaptionClient(keys=["sk-shared"], rpm_per_key=10, stream=False, rate_window_s=0.5, rate_state_dir=sys.argv[2],
                   cache_path=None, use_cache=False, ledger_path=sys.argv[3],
                   transport=httpx.MockTransport(handler))
async def go():
    await asyncio.gather(*[c.complete("m", f"x{i}") for i in range(int(sys.argv[5]))])
    await c.close()
asyncio.run(go())
json.dump(stamps, open(sys.argv[4], "w"))
"""


def test_two_processes_share_window(tmp_path):
    import subprocess
    import sys
    root = str(ad.PROJECT_ROOT)
    script = tmp_path / "proc.py"
    script.write_text(_PROC_SCRIPT)
    procs = [subprocess.Popen([sys.executable, str(script), root, str(tmp_path / "rl"),
                               str(tmp_path / f"l{i}.csv"), str(tmp_path / f"s{i}.json"), "25"])
             for i in range(2)]
    for p in procs:
        assert p.wait(timeout=60) == 0
    stamps = sorted(json.load(open(tmp_path / "s0.json")) + json.load(open(tmp_path / "s1.json")))
    assert len(stamps) == 50
    # in any window slightly shorter than 0.5 s there are at most 10 sends across BOTH processes
    worst = max(sum(1 for u in stamps if t <= u < t + 0.45) for t in stamps)
    assert worst <= 10
    # and they did not just serialise: total time ~ 50/10 windows
    assert stamps[-1] - stamps[0] >= 1.9


def test_killed_lock_holder_does_not_deadlock(tmp_path):
    import subprocess
    import sys
    import time as _t
    w = ad.SharedRateWindow(tmp_path / "w.json", rpm=5, window_s=60)
    holder = subprocess.Popen([sys.executable, "-c", (
        "import fcntl, sys, time; f = open(sys.argv[1], 'r+'); fcntl.flock(f, fcntl.LOCK_EX); "
        "print('locked', flush=True); time.sleep(60)"), str(tmp_path / "w.json")],
        stdout=subprocess.PIPE, text=True)
    assert holder.stdout.readline().strip() == "locked"
    holder.kill()
    holder.wait()
    t0 = _t.monotonic()
    assert w.try_acquire() == 0.0
    assert _t.monotonic() - t0 < 2.0


# ------------------------------------------------------------------------------ jobs

def test_run_jobs_resumable(tmp_path):
    h = Handler(script=[(400, {"error": "bad"})])  # first job errors (non-retryable)
    c = make_client(tmp_path, h)
    jobs = [Job(job_id=f"j{i}", model="m", input=f"q{i}", meta={"i": i}) for i in range(5)]
    out = tmp_path / "out.jsonl"
    rows = run(c, jobs, out, desc="t")
    assert [r["job_id"] for r in rows] == [f"j{i}" for i in range(5)]
    assert sum(1 for r in rows if r["error"]) == 1
    assert rows[2]["meta"] == {"i": 2} and rows[2]["text"] == "echo:q2"
    n_calls = len(h.calls)
    # second run: only the errored job is re-run; returns rows in job order
    rows2 = run(c, jobs, out)
    assert len(h.calls) == n_calls + 1
    assert all(r["error"] is None for r in rows2)
    assert [r["job_id"] for r in rows2] == [j.job_id for j in jobs]
    # third run: nothing to do
    run(c, jobs, out)
    assert len(h.calls) == n_calls + 1
    assert len(load_rows(out)) == 6


def test_parse_retry_bumps_sample_idx(tmp_path):
    seq = iter(["not json", "still not", '{"a": 1}'])
    h = Handler(default=lambda b: (200, ok_body(text=next(seq))))
    c = make_client(tmp_path, h)
    rows = run(c, [Job("j", "m", "q")], tmp_path / "o.jsonl", parse=parse_json)
    assert rows[0]["parsed"] == {"a": 1} and rows[0]["attempts"] == 3
    assert rows[0]["cost"] == pytest.approx(0.003)


def test_parse_retry_exhausted(tmp_path):
    h = Handler(default=lambda b: (200, ok_body(text="nope")))
    c = make_client(tmp_path, h)
    rows = run(c, [Job("j", "m", "q")], tmp_path / "o.jsonl", parse=parse_json, max_parse_retries=1)
    assert rows[0]["parsed"] is None and rows[0]["error"] is None and rows[0]["attempts"] == 2
    # bumped sample_idx -> distinct cache keys -> 2 real calls; re-run skips (finished, no error)
    assert len(h.calls) == 2
    run(c, [Job("j", "m", "q")], tmp_path / "o.jsonl", parse=parse_json)
    assert len(h.calls) == 2


def test_run_jobs_budget_stops(tmp_path):
    h = Handler(default=lambda b: (200, ok_body(text="t", cost=1.0)))
    c = make_client(tmp_path, h, budget_cap=2.0, per_key_concurrency=1)
    jobs = [Job(f"j{i}", "m", f"q{i}") for i in range(6)]
    with pytest.raises(BudgetExceeded):
        run(c, jobs, tmp_path / "o.jsonl", n_workers=1)
    assert 2 <= len(load_rows(tmp_path / "o.jsonl")) < 6


def test_duplicate_job_ids_rejected(tmp_path):
    c = make_client(tmp_path, Handler())
    with pytest.raises(ValueError):
        arun(run_jobs(c, [Job("a", "m", "x"), Job("a", "m", "y")], tmp_path / "o.jsonl"))


# ------------------------------------------------------------------------- jsonparse

@pytest.mark.parametrize("text,expected", [
    ('{"a": 1}', {"a": 1}),
    ('```json\n{"a": 1, "b": [1,2]}\n```', {"a": 1, "b": [1, 2]}),
    ('Sure! Here is the answer:\n{"a": "x"}\nHope this helps.', {"a": "x"}),
    ('{"a": 1, "b": 2,}', {"a": 1, "b": 2}),
    ('{"a": [1, 2,], }', {"a": [1, 2]}),
    ('<think>maybe {"a": 0}?</think>\n{"a": 2}', {"a": 2}),
    ('I should answer {bad stuff}... </think> {"a": 3}', {"a": 3}),
    ('prefix {"s": "brace } inside", "n": {"x": 1}} suffix', {"s": "brace } inside", "n": {"x": 1}}),
    ('```\n{"a": 1}\n```', {"a": 1}),
    ('{“a”: 1}', {"a": 1}),
    ("no json here", None),
    ("[1, 2, 3]", None),
    ("", None),
    (None, None),
    ('{"a": 1', None),
])
def test_parse_json(text, expected):
    assert parse_json(text) == expected


def test_validators():
    d = {"c": 85, "s": "85", "p": "85%", "f": 85.5, "neg": -3, "b": True, "x": "abc",
         "A": "(A)", "B": "b)", "C": "Option C", "D": "D. Paris", "E": "maybe"}
    assert get_int(d, "c", 0, 100) == 85
    assert get_int(d, "s", 0, 100) == 85
    assert get_int(d, "p", 0, 100) == 85
    assert get_int(d, "f", 0, 100) is None
    assert get_int(d, "neg", 0, 100) is None
    assert get_int(d, "b") is None
    assert get_int(d, "x") is None
    assert get_int(d, "missing") is None
    assert get_float(d, "f", 0, 100) == 85.5
    allowed = ["A", "B", "C", "D"]
    assert get_choice(d, "A", allowed) == "A"
    assert get_choice(d, "B", allowed) == "B"
    assert get_choice(d, "C", allowed) == "C"
    assert get_choice(d, "D", allowed) == "D"
    assert get_choice(d, "E", allowed) is None
    assert get_choice({"v": "YES."}, "v", ["yes", "no"]) == "yes"
    assert get_choice(None, "v", ["yes"]) is None


def test_default_concurrency_48_in_flight(tmp_path, monkeypatch):
    import time as _t
    monkeypatch.setenv("MEMLAB_KEY_INFLIGHT", "0")   # the shared per-key in-flight pool is tested separately
    state = {"now": 0, "peak": 0}

    async def handler(req):
        state["now"] += 1
        state["peak"] = max(state["peak"], state["now"])
        await asyncio.sleep(0.3)
        state["now"] -= 1
        return httpx.Response(200, json=ok_body("ok"))

    c = AdaptionClient(keys=FAKE_KEYS, cache_path=None, use_cache=False, ledger_path=tmp_path / "l.csv",
                       rpm_per_key=1000, stream=False, rate_state_dir=tmp_path / "rl", transport=httpx.MockTransport(handler))
    assert c.per_key_concurrency == 48 and c.total_concurrency == 96

    async def go():
        t0 = _t.monotonic()
        await asyncio.gather(*[c.complete("m", f"x{i}") for i in range(96)])
        return _t.monotonic() - t0

    dt = arun(go())
    assert state["peak"] == 96 and dt < 1.5


def test_cache_key_list_inputs():
    a = [{"role": "user", "content": "hi"}, {"role": "assistant", "content": "yo"}]
    b = [{"content": "hi", "role": "user"}, {"content": "yo", "role": "assistant"}]  # key order
    c = list(reversed(a))
    k = lambda x: cache_key("m", None, x, 100, 0.0, 0, {"reasoning": {"effort": "low"}})
    assert k(a) == k(b) and k(a) != k(c) and k(a) != k("hi")


def test_list_input_sent_and_cached(tmp_path):
    h = Handler(default=lambda b: (200, ok_body(text=str(len(b["input"])))))
    c = make_client(tmp_path, h)
    msgs = [{"role": "user", "content": "a"}, {"role": "assistant", "content": "b"},
            {"role": "user", "content": "c"}]
    r1 = arun(c.complete("m", msgs))
    r2 = arun(c.complete("m", [dict(reversed(list(m.items()))) for m in msgs]))
    assert r1.text == "3" and h.calls[0]["body"]["input"] == msgs and r2.cached



def sse(events):
    return "".join(f"event: {e['type']}\ndata: {json.dumps(e)}\n\n" for e in events) + "data: [DONE]\n\n"


def test_streaming_assembles_final_response(tmp_path):
    seen = []

    def handler(req):
        body = json.loads(req.content)
        seen.append(body)
        final = ok_body(text='{"a": 1}', reasoning="r")
        evs = [{"type": "response.created", "response": {"status": "in_progress"}},
               {"type": "response.reasoning_text.delta", "delta": "r"},
               {"type": "response.output_text.delta", "delta": '{"a": 1}'},
               {"type": "response.completed", "response": final}]
        return httpx.Response(200, text=sse(evs), headers={"content-type": "text/event-stream"})

    c = make_client(tmp_path, handler, stream=True)
    r = arun(c.complete("m", "x"))
    assert seen[0]["stream"] is True
    assert r.error is None and r.text == '{"a": 1}' and r.reasoning == "r" and r.cost == 0.001


def test_streaming_without_final_event_is_retried(tmp_path):
    n = {"i": 0}

    def handler(req):
        n["i"] += 1
        if n["i"] == 1:
            return httpx.Response(200, text=sse([{"type": "response.created"}]),
                                  headers={"content-type": "text/event-stream"})
        return httpx.Response(200, text=sse([{"type": "response.completed", "response": ok_body("fine")}]),
                              headers={"content-type": "text/event-stream"})

    c = make_client(tmp_path, handler, stream=True)
    r = arun(c.complete("m", "x"))
    assert r.text == "fine" and n["i"] == 2


def test_streaming_http_error_status(tmp_path):
    h = Handler(script=[(429, {"error": "rate"})])
    c = make_client(tmp_path, h, stream=True)
    # second call returns a JSON (non-SSE) body -> no final event -> retried until the scripted
    # 429 is consumed and the default (non-SSE) answer keeps failing; just check 429 handling
    c.max_attempts = 2
    r = arun(c.complete("m", "x"))
    assert c.stats["http_429"] == 1 and r.error


def test_model_inflight_cap(tmp_path):
    state = {"now": {}, "peak": {}}

    async def handler(req):
        auth = req.headers["authorization"]
        state["now"][auth] = state["now"].get(auth, 0) + 1
        state["peak"][auth] = max(state["peak"].get(auth, 0), state["now"][auth])
        await asyncio.sleep(0.15)
        state["now"][auth] -= 1
        return httpx.Response(200, json=ok_body("ok"))

    c = make_client(tmp_path, handler, use_cache=False, rpm_per_key=None,
                    model_inflight_cap={"big": 2})

    async def go():
        await asyncio.gather(*[c.complete("big", f"x{i}") for i in range(12)])

    arun(go())
    assert max(state["peak"].values()) <= 2 and len(state["peak"]) == 2
    # tickets were released: a fresh holder can take all of them
    cap = ad.SharedInflightCap(tmp_path / "rl", FAKE_KEYS[0], "big", 2)
    t1, t2, t3 = cap.try_acquire(), cap.try_acquire(), cap.try_acquire()
    assert t1 and t2 and t3 is None
    ad.SharedInflightCap.release(t1)
    ad.SharedInflightCap.release(t2)
