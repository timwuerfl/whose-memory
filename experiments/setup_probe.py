"""Setup probe for the Adaption API: latency, reasoning control, structured output, temperature,
rate limits and cost accounting, for all 7 hosted models.

Usage:  .venv/bin/python experiments/setup_probe.py [--phases smoke,reasoning,latency,json,temperature,ratelimit,specs]

Results are merged into results/setup/probe.json (each phase overwrites its own section), and
SPECS.md is regenerated from probe.json by the ``specs`` phase. Spend is booked to the ledger with
tag ``setup_probe``. The cache is disabled for every probe call.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import statistics
import sys
import time
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from memlab.clients.adaption import MODEL_DEFAULTS, MODELS, PRICES, AdaptionClient  # noqa: E402
from memlab.utils.jsonparse import get_int, parse_json  # noqa: E402

OUT = ROOT / "results" / "setup" / "probe.json"
TAG = "setup_probe"
HARDWARE = "Apple M4 Pro, 12 cores, 24 GB unified memory, macOS 26.7.3, PyTorch 2.15.0 MPS"

JSON_INSTR = "You are a precise assistant. Reply with a single JSON object and nothing else."
def json_prompt(i: int) -> tuple[str, int]:
    a, b = 17 + i, 25 + 2 * i
    return f'What is {a} + {b}? Reply exactly as {{"answer": <integer>}}.', a + b

REASONING_VARIANTS = {
    "baseline": {},
    "reasoning.effort=none": {"reasoning": {"effort": "none"}},
    "reasoning.effort=minimal": {"reasoning": {"effort": "minimal"}},
    "reasoning.effort=low": {"reasoning": {"effort": "low"}},
    "reasoning_effort=none": {"reasoning_effort": "none"},
    "thinking.disabled": {"thinking": {"type": "disabled"}},
    "enable_thinking=false": {"enable_thinking": False},
    "chat_template_kwargs.enable_thinking=false": {"chat_template_kwargs": {"enable_thinking": False}},
}


def load() -> dict:
    return json.loads(OUT.read_text()) if OUT.exists() else {}


def save(section: str, data) -> None:
    d = load()
    d[section] = data
    d["updated_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(d, indent=2, ensure_ascii=False))


def mk_client(**kw) -> AdaptionClient:
    kw.setdefault("use_cache", False)
    kw.setdefault("cache_path", None)
    kw.setdefault("per_key_concurrency", 8)
    kw.setdefault("timeout_s", 180)
    return AdaptionClient(**kw)


def summ(c) -> dict:
    return {"status": c.status, "error": c.error, "latency_s": round(c.latency_s, 3),
            "usage": c.usage, "cost": c.cost, "text": c.text[:200],
            "reasoning_chars": len(c.reasoning), "attempts": c.attempts, "key_slot": c.key_slot}


def med(xs):
    xs = [x for x in xs if x is not None]
    return round(statistics.median(xs), 3) if xs else None


# --------------------------------------------------------------------------------- phases

async def phase_smoke():
    cl = mk_client()
    res = {}
    for slot_client in (mk_client(key_slots=[1]), mk_client(key_slots=[2])):
        p, _ = json_prompt(0)
        c = await slot_client.complete("deepseek-v4-flash", p, JSON_INSTR, max_output_tokens=512, tag=TAG)
        res[f"key{slot_client._slots[0].slot}"] = {**summ(c), "rl_headers": c.rl_headers}
        await slot_client.close()
    await cl.close()
    print(json.dumps(res, indent=1))
    save("smoke", res)


async def phase_reasoning():
    cl = mk_client(per_key_concurrency=8, max_attempts=3)
    p, ans = json_prompt(1)

    async def one(model, name, extra):
        c = await cl.complete(model, p, JSON_INSTR, max_output_tokens=2048, extra=extra or None, tag=TAG)
        d = parse_json(c.text)
        return model, name, {**summ(c), "correct": get_int(d, "answer") == ans}

    tasks = [one(m, n, e) for m in MODELS for n, e in REASONING_VARIANTS.items()]
    out = {}
    for model, name, r in await asyncio.gather(*tasks):
        out.setdefault(model, {})[name] = r
        print(f"{model:22s} {name:45s} st={r['status']:10s} rt={r['usage']['reasoning_tokens']:5d} "
              f"ok={r['correct']} err={(r['error'] or '')[:80]}")
    await cl.close()
    save("reasoning", out)


def _strict(r: dict) -> bool:
    """Accepted, correct, and the output text is *only* the JSON object (no leaked reasoning)."""
    if r.get("error") or not r.get("correct"):
        return False
    try:
        return isinstance(json.loads(r.get("text", "")), dict)
    except Exception:
        return False


def pick_recommended(reasoning: dict) -> dict:
    """Cheapest variant that (a) is accepted, correct and leak-free and (b) lowers reasoning tokens."""
    rec = {}
    for m, variants in reasoning.items():
        variants = {n: {**r, "correct": _strict(r)} for n, r in variants.items()}
        base = variants.get("baseline", {})
        base_rt = base.get("usage", {}).get("reasoning_tokens", 0)
        best_name, best_rt = "baseline", base_rt
        # prefer one uniform setting across models when it is accepted, correct and no worse
        uni = variants.get("reasoning.effort=none", {})
        if uni and not uni.get("error") and uni.get("correct") and \
                uni["usage"]["reasoning_tokens"] <= base_rt:
            best_name, best_rt = "reasoning.effort=none", uni["usage"]["reasoning_tokens"]
        for name, r in variants.items():
            if r.get("error") or not r.get("correct"):
                continue
            rt = r["usage"]["reasoning_tokens"]
            if rt < best_rt * 0.7 or (best_rt > 0 and rt == 0):
                if rt < best_rt:
                    best_name, best_rt = name, rt
        rec[m] = {"variant": best_name, "extra": REASONING_VARIANTS[best_name],
                  "baseline_reasoning_tokens": base_rt, "reasoning_tokens": best_rt}
    return rec


async def phase_latency(reps: int = 5):
    rec = load().get("recommended") or pick_recommended(load()["reasoning"])
    cl = mk_client(per_key_concurrency=8, max_attempts=4)
    out = {}
    for m in MODELS:
        for mode, extra in (("default", None), ("recommended", rec[m]["extra"] or None)):
            if mode == "recommended" and not extra:
                out.setdefault(m, {})[mode] = out[m]["default"]
                continue
            rs = []
            for i in range(reps):  # sequential -> clean latency
                p, ans = json_prompt(10 + i)
                c = await cl.complete(m, p, JSON_INSTR, max_output_tokens=2048, extra=extra, tag=TAG)
                rs.append((c, get_int(parse_json(c.text), "answer") == ans))
            out.setdefault(m, {})[mode] = {
                "n": reps,
                "median_latency_s": med([c.latency_s for c, _ in rs if not c.error]),
                "median_reasoning_tokens": med([c.usage["reasoning_tokens"] for c, _ in rs if not c.error]),
                "max_reasoning_tokens": max([c.usage["reasoning_tokens"] for c, _ in rs] or [0]),
                "median_output_tokens": med([c.usage["output_tokens"] for c, _ in rs if not c.error]),
                "median_input_tokens": med([c.usage["input_tokens"] for c, _ in rs if not c.error]),
                "n_correct_json": sum(ok for _, ok in rs),
                "n_errors": sum(1 for c, _ in rs if c.error),
                "errors": [c.error for c, _ in rs if c.error][:3],
                "mean_cost": sum(c.cost for c, _ in rs) / reps,
                "cost_check": [cost_check(m, c) for c, _ in rs[:2]],
            }
            print(m, mode, {k: v for k, v in out[m][mode].items() if k != "cost_check"})
    await cl.close()
    save("latency", out)


def cost_check(model, c) -> dict:
    pin, pout = PRICES[model]
    exp = (c.usage["input_tokens"] * pin + c.usage["output_tokens"] * pout) / 1e6
    return {"reported": c.cost, "expected_from_price_table": round(exp, 10),
            "ratio": round(c.cost / exp, 4) if exp else None}


HARD = [
    ("A shop has 3 boxes with 12 apples each. It sells 17 apples, then receives 2 more boxes of 12. "
     'How many apples does it have now? Reply exactly as {"answer": <integer>}.', 43),
    ("Alice is older than Bob. Bob is older than Carol. Dan is younger than Carol. Who is the second "
     'youngest? Reply exactly as {"answer": "<name>"}.', "carol"),
    ("A meeting was moved from Tuesday to two days later, and then moved one day earlier. On which "
     'weekday is it now? Reply exactly as {"answer": "<weekday>"}.', "wednesday"),
]


async def phase_hardcheck():
    """Do the recommended settings stay leak-free and correct on slightly harder prompts?"""
    rec = load()["recommended"]
    cl = mk_client(per_key_concurrency=8, max_attempts=4)

    async def one(m, mode, i):
        p, ans = HARD[i]
        extra = rec[m]["extra"] if mode == "recommended" else None
        c = await cl.complete(m, p, JSON_INSTR, max_output_tokens=2048, extra=extra or None, tag=TAG)
        try:
            strict = json.loads(c.text)
        except Exception:
            strict = None
        got = (parse_json(c.text) or {}).get("answer")
        correct = str(got).strip().lower() == str(ans)
        return m, mode, {**summ(c), "strict_json": isinstance(strict, dict), "correct": correct}

    tasks = [one(m, mode, i) for m in MODELS for mode in ("default", "recommended") for i in range(len(HARD))]
    out = {}
    for m, mode, r in await asyncio.gather(*tasks):
        out.setdefault(m, {}).setdefault(mode, []).append(r)
    for m in out:
        for mode, rs in out[m].items():
            print(f"{m:20s} {mode:12s} strict={sum(r['strict_json'] for r in rs)}/3 "
                  f"correct={sum(r['correct'] for r in rs)}/3 rt={[r['usage']['reasoning_tokens'] for r in rs]} "
                  f"out={[r['usage']['output_tokens'] for r in rs]}")
    await cl.close()
    save("hardcheck", out)


LONG_PROMPT = (
    'Return a JSON object of the form {"entries": ["...", "..."]} with exactly 40 strings. Entry i '
    'starts with "i. " and is one 20-30 word sentence describing a different fictional lab-notebook '
    "observation. Output only the JSON object.")


async def phase_study():
    """Study settings: effort "low" on every model, long JSON outputs, multi-turn input lists."""
    from memlab.clients.adaption import STUDY_MAX_OUTPUT_TOKENS
    cl = mk_client(per_key_concurrency=8, max_attempts=4)
    out = {"effort_low": {}, "long_output": {}, "multi_turn": {}}
    low = {"reasoning": {"effort": "low"}}
    p, ans = HARD[0]

    async def eff(m, extra, label):
        c = await cl.complete(m, p, JSON_INSTR, max_output_tokens=4096, extra=extra, tag=TAG)
        try:
            strict = json.loads(c.text)
        except Exception:
            strict = None
        r = {**summ(c), "extra": extra, "strict_json": isinstance(strict, dict),
             "correct": isinstance(strict, dict) and strict.get("answer") == ans,
             "reasoning_in_item": len(c.reasoning) > 0,
             "leaked": (not isinstance(strict, dict)) and len(c.text) > 40}
        print(f"{m:20s} {label:8s} st={c.status} err={(c.error or '')[:60]} rt={c.usage['reasoning_tokens']} "
              f"item={r['reasoning_in_item']} strict={r['strict_json']} ok={r['correct']} lat={c.latency_s:.1f}")
        return m, r

    for m, r in await asyncio.gather(*[eff(m, low, "low") for m in MODELS]):
        out["effort_low"][m] = r
    # fall back to "medium" wherever "low" was rejected or leaked
    bad = [m for m, r in out["effort_low"].items() if r["error"] or not r["strict_json"]]
    out["effort_medium_fallback"] = {}
    for m, r in await asyncio.gather(*[eff(m, {"reasoning": {"effort": "medium"}}, "medium") for m in bad]):
        out["effort_medium_fallback"][m] = r
    STUDY_EXTRA = {m: (low if m not in bad else {"reasoning": {"effort": "medium"}}) for m in MODELS}
    out["study_extra_used"] = STUDY_EXTRA
    save("study", out)

    async def long(m):
        c = await cl.complete(m, LONG_PROMPT, JSON_INSTR, max_output_tokens=STUDY_MAX_OUTPUT_TOKENS,
                              temperature=0.7, extra=STUDY_EXTRA[m], tag=TAG)
        try:
            d = json.loads(c.text)
            entries = d.get("entries") if isinstance(d, dict) else None
        except Exception:
            d, entries = None, None
        r = {**summ(c), "text": c.text[:300], "text_tail": c.text[-200:], "strict_json": d is not None,
             "n_entries": len(entries) if isinstance(entries, list) else None,
             "parse_json_ok": parse_json(c.text) is not None,
             "answer_tokens": c.usage["output_tokens"] - c.usage["reasoning_tokens"]}
        print(f"LONG {m}: st={c.status} err={c.error} lat={c.latency_s:.1f}s out={c.usage['output_tokens']} "
              f"rt={c.usage['reasoning_tokens']} strict={r['strict_json']} n={r['n_entries']}")
        return m, r

    for m, r in await asyncio.gather(*[long(m) for m in ("deepseek-v4-flash", "qwen3.5-397b")]):
        out["long_output"][m] = r
    save("study", out)

    convo = [
        {"role": "user", "content": "Let's play a memory game. Please give me a code word to remember."},
        {"role": "assistant", "content": "Here is your code word: PELICAN-47. Keep it safe."},
        {"role": "user", "content": 'What code word did you give me, and who chose it? Reply only as JSON: '
                                    '{"code_word": "...", "chosen_by": "you" or "me", "comment": "<one sentence>"}. '
                                    '"you" means the assistant (you), "me" means the user.'},
    ]

    async def mt(m):
        c = await cl.complete(m, convo, None, max_output_tokens=STUDY_MAX_OUTPUT_TOKENS,
                              extra=STUDY_EXTRA[m], tag=TAG)
        d = parse_json(c.text) or {}
        r = {**summ(c), "parsed": d, "recalls_code": "PELICAN-47" in json.dumps(d).upper(),
             "attributes_to_self": str(d.get("chosen_by", "")).strip().lower() == "you"}
        print(f"MT {m:20s} err={(c.error or '')[:60]} recall={r['recalls_code']} self={r['attributes_to_self']} {c.text[:120]!r}")
        return m, r

    for m, r in await asyncio.gather(*[mt(m) for m in MODELS]):
        out["multi_turn"][m] = r
    await cl.close()
    save("study", out)


MID_PROMPT = ("How many positive integers below 200 are divisible by 3 or 5 but not by 7? "
              'Reply exactly as {"answer": <integer>}.', 79)
BUDGET_VARIANTS = {
    "effort=low": {"reasoning": {"effort": "low"}},
    "effort=medium": {"reasoning": {"effort": "medium"}},
    "effort=high": {"reasoning": {"effort": "high"}},
    "reasoning.max_tokens=256": {"reasoning": {"effort": "low", "max_tokens": 256}},
    "reasoning.budget_tokens=256": {"reasoning": {"effort": "low", "budget_tokens": 256}},
    "thinking_budget=256": {"reasoning": {"effort": "low"}, "thinking_budget": 256},
    "max_reasoning_tokens=256": {"reasoning": {"effort": "low"}, "max_reasoning_tokens": 256},
}


async def phase_study2():
    """Does effort change anything; is there a reasoning budget; streaming on all models;
    long output on qwen3.5-397b via streaming."""
    from memlab.clients.adaption import STUDY_MAX_OUTPUT_TOKENS
    cl = mk_client(per_key_concurrency=16, max_attempts=2, stream=True)
    d = load().get("study", {})
    p, ans = MID_PROMPT

    async def one(m, name, extra):
        c = await cl.complete(m, p, JSON_INSTR, max_output_tokens=STUDY_MAX_OUTPUT_TOKENS, extra=extra, tag=TAG)
        try:
            strict = json.loads(c.text)
        except Exception:
            strict = None
        r = {**summ(c), "extra": extra, "strict_json": isinstance(strict, dict),
             "correct": isinstance(strict, dict) and strict.get("answer") == ans}
        print(f"{m:20s} {name:28s} st={c.status} err={(c.error or '')[:70]} rt={c.usage['reasoning_tokens']} "
              f"strict={r['strict_json']} ok={r['correct']} lat={c.latency_s:.1f}")
        return m, name, r

    tasks = [one(m, n, e) for m in ("qwen3.5-397b", "deepseek-v4-flash") for n, e in BUDGET_VARIANTS.items()]
    tasks += [one(m, "effort=low (stream smoke)", BUDGET_VARIANTS["effort=low"])
              for m in MODELS if m not in ("qwen3.5-397b", "deepseek-v4-flash")]
    res = {}
    for m, n, r in await asyncio.gather(*tasks):
        res.setdefault(m, {})[n] = r
    d["budget_and_stream"] = res
    save("study", d)

    c = await cl.complete("qwen3.5-397b", LONG_PROMPT, JSON_INSTR, max_output_tokens=16384, temperature=0.7,
                          extra={"reasoning": {"effort": "low"}}, tag=TAG)
    try:
        dd = json.loads(c.text)
        n = len(dd.get("entries", [])) if isinstance(dd, dict) else None
    except Exception:
        dd, n = None, None
    r = {**summ(c), "text_tail": c.text[-200:], "strict_json": dd is not None, "n_entries": n,
         "max_output_tokens": 16384, "stream": True,
         "answer_tokens": c.usage["output_tokens"] - c.usage["reasoning_tokens"]}
    print(f"LONG qwen3.5-397b stream: st={c.status} err={c.error} lat={c.latency_s:.1f}s "
          f"out={c.usage['output_tokens']} rt={c.usage['reasoning_tokens']} strict={r['strict_json']} n={n}")
    d["long_output_qwen_stream"] = r
    save("study", d)
    await cl.close()


async def phase_inflight():
    """Is there an in-flight (concurrency) limit for long-running requests? Fixed ~1k-token outputs
    without reasoning on deepseek-v4-flash: 1 alone, 6 at once on key 1, then 6 + 6 on both keys."""
    prompt = "Write the integers from 1 to 300 in order, separated by single spaces. Output nothing else."
    extra = {"reasoning": {"effort": "none"}}

    async def batch(slot_counts: dict[int, int]):
        cls = {s: mk_client(key_slots=[s], per_key_concurrency=48, max_attempts=1, adaptive=False)
               for s in slot_counts}
        t0 = time.monotonic()

        async def one(s, i):
            c = await cls[s].complete("deepseek-v4-flash", f"{prompt} (run {i}-{time.time_ns()})", None,
                                      max_output_tokens=2048, extra=extra, tag=TAG)
            return {"key": s, "latency_s": round(c.latency_s, 1), "out_tokens": c.usage["output_tokens"],
                    "error": (c.error or "")[:80] or None}
        rs = await asyncio.gather(*[one(s, i) for s, n in slot_counts.items() for i in range(n)])
        for c in cls.values():
            await c.close()
        lat = sorted(r["latency_s"] for r in rs if not r["error"])
        step = {"per_key": slot_counts, "wall_s": round(time.monotonic() - t0, 1), "latencies": lat,
                "n_err": sum(1 for r in rs if r["error"]), "errors": [r["error"] for r in rs if r["error"]][:3],
                "out_tokens": [r["out_tokens"] for r in rs]}
        print(step)
        return step

    out = {"alone": await batch({1: 1})}
    out["six_key1"] = await batch({1: 6})
    out["six_each_both_keys"] = await batch({1: 6, 2: 6})
    d = load().get("ratelimit", {})
    d["inflight"] = out
    save("ratelimit", d)


async def phase_json():
    rec = load()["recommended"]
    cl = mk_client(per_key_concurrency=8, max_attempts=3)
    schema = {"type": "object", "properties": {"answer": {"type": "integer"}},
              "required": ["answer"], "additionalProperties": False}
    fmts = {
        "json_object": {"text": {"format": {"type": "json_object"}}},
        "json_schema": {"text": {"format": {"type": "json_schema", "name": "answer",
                                            "schema": schema, "strict": True}}},
    }
    # Prompt WITHOUT the JSON instruction so we see whether the format alone enforces JSON.
    p_plain = "What is 23 + 31? Give the answer."

    async def one(m, name, fmt):
        extra = {**(rec[m]["extra"] or {}), **fmt}
        c = await cl.complete(m, p_plain, None, max_output_tokens=2048, extra=extra, tag=TAG)
        strict = None
        try:
            strict = json.loads(c.text)
        except Exception:
            pass
        return m, name, {**summ(c), "strict_json": isinstance(strict, dict),
                         "schema_ok": isinstance(strict, dict) and strict.get("answer") == 54
                         and set(strict) == {"answer"}}

    out = {}
    for m, name, r in await asyncio.gather(*[one(m, n, f) for m in MODELS for n, f in fmts.items()]):
        out.setdefault(m, {})[name] = r
        print(f"{m:22s} {name:12s} strict={r['strict_json']} schema_ok={r['schema_ok']} "
              f"err={(r['error'] or '')[:80]} text={r['text'][:60]!r}")
    await cl.close()
    save("json", out)


async def phase_temperature():
    rec = load()["recommended"]
    cl = mk_client(per_key_concurrency=8, max_attempts=4)
    prompt = "Invent a name for a fictional cat and describe it in one short sentence."

    async def one(m, t, i):
        c = await cl.complete(m, prompt, None, max_output_tokens=2048, temperature=t,
                              sample_idx=i, extra=rec[m]["extra"] or None, tag=TAG)
        return m, t, c

    tasks = [one(m, 1.0, i) for m in MODELS for i in range(5)] + \
            [one(m, 0.0, i) for m in MODELS for i in range(5)]
    res = {}
    for m, t, c in await asyncio.gather(*tasks):
        res.setdefault(m, {}).setdefault(str(t), []).append(c)
    out = {}
    for m, d in res.items():
        out[m] = {}
        for t, cs in d.items():
            texts = [c.text for c in cs if not c.error]
            out[m][f"T={t}"] = {"n": len(cs), "n_distinct": len(set(texts)),
                                "n_errors": sum(1 for c in cs if c.error),
                                "examples": texts[:3]}
        print(m, {k: (v["n_distinct"], v["n"]) for k, v in out[m].items()})
    await cl.close()
    save("temperature", out)


async def ramp(model: str, key_slots: list[int], levels: list[int], extra, per_level_mult=3,
               stop_frac=0.10, max_output_tokens=256):
    """Fire ``mult*c`` requests at concurrency ``c`` per key (no retries, no throttle, no cache)."""
    steps = []
    for c in levels:
        cl = mk_client(per_key_concurrency=c, key_slots=key_slots, max_attempts=1, adaptive=False,
                       timeout_s=120, rpm_per_key=None)
        n = per_level_mult * c * len(key_slots)
        t0 = time.monotonic()

        async def one(i):
            return await cl.complete(model, f"Reply with the single word OK. (#{i}-{time.time_ns()})",
                                     None, max_output_tokens=max_output_tokens, extra=extra, tag=TAG)
        cs = await asyncio.gather(*[one(i) for i in range(n)])
        wall = time.monotonic() - t0
        n429 = sum(1 for x in cs if x.error and "429" in x.error)
        nerr = sum(1 for x in cs if x.error)
        errs = Counter((x.error or "")[:60] for x in cs if x.error)
        hdrs = {}
        for x in cs:
            hdrs.update(x.rl_headers)
        ok = [x for x in cs if not x.error]
        step = {"concurrency_per_key": c, "keys": key_slots, "n": n, "wall_s": round(wall, 2),
                "ok": len(ok), "n_429": n429, "n_err": nerr,
                "throughput_rps": round(len(ok) / wall, 2) if wall else None,
                "median_latency_s": med([x.latency_s for x in ok]),
                "p90_latency_s": round(sorted(x.latency_s for x in ok)[int(0.9 * (len(ok) - 1))], 3) if ok else None,
                "error_kinds": dict(errs.most_common(4)), "rl_headers_seen": hdrs,
                "cost": round(sum(x.cost for x in cs), 6)}
        print(model, step)
        steps.append(step)
        await cl.close()
        if nerr / n > stop_frac:
            break
        await asyncio.sleep(3)
    return steps


async def phase_ratelimit():
    d = load()
    rec = d["recommended"]
    out = d.get("ratelimit", {})
    m0 = "deepseek-v4-flash"
    out["deepseek_key1"] = await ramp(m0, [1], [4, 8, 16, 32, 64, 128], rec[m0]["extra"] or None)
    save("ratelimit", out)
    out["deepseek_key2"] = await ramp(m0, [2], [16, 64], rec[m0]["extra"] or None)
    save("ratelimit", out)
    out["deepseek_both_keys"] = await ramp(m0, [1, 2], [32, 64], rec[m0]["extra"] or None)
    save("ratelimit", out)
    m1 = "gemma-4-26b-a4b-it"
    out["gemma26b_key1"] = await ramp(m1, [1], [8, 32, 64], rec[m1]["extra"] or None)
    save("ratelimit", out)


async def phase_window():
    """Characterise the request-count window directly with raw HTTP (sequential calls)."""
    import httpx
    from memlab.clients.adaption import load_keys
    k1, k2 = load_keys()
    url = "https://api.prod.adaptionlabs.ai/api/v1/responses"
    out = {}
    await asyncio.sleep(65)  # start from a clean window
    async with httpx.AsyncClient(timeout=120) as c:
        async def post(k, model="deepseek-v4-flash", inp="Reply OK."):
            r = await c.post(url, headers={"Authorization": "Bearer " + k}, json={
                "model": model, "input": inp, "max_output_tokens": 32, "temperature": 0,
                "reasoning": {"effort": "none"}})
            return r.status_code, r
        t0 = time.monotonic()
        n = 0
        while n < 120:
            s, r = await post(k1)
            if s != 200:
                break
            n += 1
        t_hit = time.monotonic() - t0
        out["sequential_until_429"] = {"n_ok": n, "elapsed_s": round(t_hit, 1), "status": s,
                                       "body": r.text[:200], "retry_after": r.headers.get("retry-after")}
        out["key1_other_model_while_limited"] = (await post(k1, "gemma-4-26b-a4b-it"))[0]
        out["key2_while_key1_limited"] = [(await post(k2))[0] for _ in range(5)]
        n429 = 0
        while True:
            s, _ = await post(k1)
            if s == 200 or time.monotonic() - t0 > 200:
                break
            n429 += 1
            await asyncio.sleep(1.0)
        out["recovery"] = {"recovered": s == 200, "s_since_window_start": round(time.monotonic() - t0, 1),
                           "n_429_polls_meanwhile": n429}
        burst = 0
        while burst < 80:
            s, _ = await post(k1)
            if s != 200:
                break
            burst += 1
        out["burst_after_recovery"] = {"n_ok": burst, "s_since_window_start": round(time.monotonic() - t0, 1)}
    print(json.dumps(out, indent=1))
    d = load().get("ratelimit", {})
    d["window"] = out
    save("ratelimit", d)


async def phase_capacity():
    """Sequential calls per key from a clean window until the first 429 (key 2 first)."""
    import httpx
    from memlab.clients.adaption import load_keys
    keys = load_keys()
    await asyncio.sleep(70)
    out = {}
    async with httpx.AsyncClient(timeout=120) as c:
        for slot in (2, 1):
            t0 = time.monotonic()
            n = 0
            while n < 120:
                r = await c.post("https://api.prod.adaptionlabs.ai/api/v1/responses",
                                 headers={"Authorization": "Bearer " + keys[slot - 1]},
                                 json={"model": "deepseek-v4-flash", "input": "Reply OK.",
                                       "max_output_tokens": 32, "temperature": 0,
                                       "reasoning": {"effort": "none"}})
                if r.status_code != 200:
                    break
                n += 1
            out[f"key{slot}"] = {"n_ok_before_429": n, "elapsed_s": round(time.monotonic() - t0, 1)}
    print(out)
    d = load().get("ratelimit", {})
    d["capacity_per_key"] = out
    save("ratelimit", d)


async def phase_sustained(conc: int = 8, rpm=None, seconds: float = 150.0):
    """Sustained run through the normal client path (RPM limiter, retries, adaptive throttle on)."""
    d = load()
    rec = d["recommended"]
    m0 = "deepseek-v4-flash"
    await asyncio.sleep(65)  # start from a clean window
    from memlab.clients.adaption import DEFAULT_RPM_PER_KEY
    rpm = rpm or DEFAULT_RPM_PER_KEY
    cl = mk_client(per_key_concurrency=conc, max_attempts=8, rpm_per_key=rpm)
    t0 = time.monotonic()
    results = []
    stop = t0 + seconds

    async def worker(w):
        i = 0
        while time.monotonic() < stop:
            c = await cl.complete(m0, f"Reply with the single word OK. (w{w}-{i}-{time.time_ns()})",
                                  None, max_output_tokens=256, extra=rec[m0]["extra"] or None, tag=TAG)
            results.append(c)
            i += 1
    await asyncio.gather(*[worker(w) for w in range(cl.total_concurrency)])
    wall = time.monotonic() - t0
    ok = [c for c in results if not c.error]
    out = {"model": m0, "per_key_concurrency": conc, "rpm_per_key_limit": rpm, "keys": [1, 2], "wall_s": round(wall, 1),
           "n": len(results), "ok": len(ok), "errors": len(results) - len(ok),
           "rpm": round(60 * len(ok) / wall, 1), "median_latency_s": med([c.latency_s for c in ok]),
           "http_429_seen": cl.stats["http_429"], "http_5xx_seen": cl.stats["http_5xx"],
           "timeouts": cl.stats["timeouts"], "final_effective_limits": {str(k): v for k, v in cl.effective_limits.items()},
           "cost": round(sum(c.cost for c in results), 6)}
    print(out)
    await cl.close()
    d = load().get("ratelimit", {})
    tag = "default" if isinstance(rpm, dict) else int(rpm)
    d[f"sustained_c{conc}_rpm{tag}"] = out
    save("ratelimit", d)


# ---------------------------------------------------------------------------------- specs

NOTES_MODELS = """Latency is the median of 5 sequential calls on a short JSON arithmetic prompt (max_output_tokens
2048), measured from this Mac; "rec." uses the recommended `extra`. All 7 models answered all probes
without errors. JSON columns: prompt asked for the answer *without* a JSON instruction, so "yes" means the
format alone forced JSON. `json_object` always produced JSON but not always the intended keys/types
(glm-5.3-flash and qwen3.5-397b returned `"54"` as a string, glm-5.2 used key `response`);
`json_schema` (`{"type":"json_schema","name":...,"schema":...,"strict":true}`) gave schema-valid output on
all 7. Temperature: 5 samples at T=1.0 were all distinct on every model (honoured). At T=0 only
deepseek-v4-flash, gemma-4-26b-a4b-it and glm-5.2 were deterministic (1 distinct of 5); qwen3.8-27b (4/5),
gemma-4-31b-it (5/5), qwen3.5-397b (3/5), glm-5.3-flash (2/5) are not, so T=0 is no substitute for a seed.
`usage.cost` matches the price table exactly (ratio 1.000) on 5 models; deepseek-v4-flash is billed 0.7 %
above list and gemma-4-26b-a4b-it 0.4 % below. Ledger uses the reported cost.

**Reasoning control.** Unknown request fields are silently ignored (no 400s), so "accepted" means nothing
by itself. `reasoning: {"effort": "none"}` (equivalently `reasoning_effort: "none"`) sets reasoning tokens
to 0 on deepseek-v4-flash, qwen3.8-27b, qwen3.5-397b and glm-5.2 (and on the gemmas, which do not reason
by default). **Trap: on glm-5.3-flash, effort "none" does not stop reasoning; the reasoning text is
emitted into the answer text** (e.g. `The user wants me to compute ... {"answer": 45}`), so we use
effort "low" there (reasoning stays in the separate reasoning item; ~10-15 tokens). `thinking`,
`enable_thinking` and `chat_template_kwargs` have no effect on any model. qwen3.8-27b rejects effort
"minimal" (400: supported xhigh (default), medium, low). On the gemmas, effort "low"/"minimal" turns
reasoning *on* (~50-160 tokens). Reasoning-off costs accuracy on some models: on 3 small multi-step
questions deepseek-v4-flash and qwen3.8-27b fell from 3/3 to 1/3 (others unchanged; tiny n). Decide per
experiment whether reasoning stays on. qwen3.5-397b with default reasoning spends 250-600 reasoning tokens
even on trivial prompts (~3 s); with effort none it drops to ~0.4 s.
Disabling reasoning on deepseek-v4-flash also cuts input tokens (117 → 38): the provider adds a system
prompt when reasoning is on."""

NOTES_RATELIMIT = """**The binding limit is a per-key request count over a rolling 60 s window, shared across all
models: key 1 = 50 requests/min, key 2 = 25 requests/min.** No separate concurrency limit was observed for short
requests (bursts of up to 16 in flight succeeded while under the count), **except qwen3.5-397b: 3 in
flight per key** (see Study settings). A 429 says `Inference rate limit reached for this user; retry after 60
seconds` with `Retry-After: 60`; no rate-limit headers are sent on 200s. Rejected (429) calls do not count
against the window (polling at 1 req/s during a lockout did not delay recovery, which came ~60 s after the
first request of the window). While key 1 was limited, key 2 still served requests and key 1 was limited
for other models too. No token-per-minute limit was found: 30 sequential requests of 10k input tokens
(300k tokens) in 10 s on key 1 all succeeded. The concurrency ramp (raw, no limiter, no retries) shows
what happens beyond the count: everything after ~50 (key 1) / ~25 (key 2) requests in a minute is 429ed.
The ramp steps ran back to back inside one window, so read their success counts as cumulative (key 1:
12 + 24 + 2 = 38 ok before the window filled, plus earlier probe calls). A concurrent burst of 55 large
requests on key 2 got 25 through, consistent with key 2's 25/min. The sustained run with the default
limiter (46 + 23 per minute) saw zero 429s; its 74/min average includes the first-minute burst, steady
state is the limiter's 69/min.

**Consequence: sustained throughput is ~70 requests/min (≈4,200/h) across both keys, regardless of
model.** Long prompts did not cost extra rate budget (output length was not tested beyond short
answers), so pack work into fewer, larger calls where the design allows. With reasoning off, latency (0.3-3 s) is not the bottleneck; with reasoning on, calls take 1-100 s,
hence the default of 48 in flight per key."""

NOTES_STUDY = """**Effort "low"** is accepted by all 7 models (no 400s; qwen3.5-397b and glm-5.2 included) and the
reasoning stays in the reasoning item on all 7: strict JSON answer text on an easy prompt everywhere;
the gemmas wrap the JSON in a ```json fence (fine for `parse_json`). Effort level barely matters where
reasoning is native: deepseek-v4-flash used 480 / 486 / 255 reasoning tokens at low / medium / high on
the same medium prompt (single samples), qwen3.5-397b 3.7k at medium. **No reasoning-budget field
works** (`reasoning.max_tokens`, `reasoning.budget_tokens`, `thinking_budget`, `max_reasoning_tokens`
are silently ignored; qwen3.5-397b used 2.9-3.2k with a "256" budget). "Low" is therefore not cheap on
every model: medium arithmetic prompt → qwen3.5-397b ~3-4k, gemma-4-26b 5.3k, gemma-4-31b 3.5k
reasoning tokens; glm-5.3-flash only 62 (and got it wrong). For the medium-prompt column, qwen3.5-397b's
"low" call was rejected by its in-flight cap (below); its other variants used 2.9-3.7k.

**Long outputs (40 numbered sentences ≈ 1.1k answer tokens, T=0.7).** deepseek-v4-flash: completed in
45 s, 6,011 reasoning + 1,128 answer tokens, intact JSON with 40 entries (non-streaming). qwen3.5-397b:
**non-streaming requests fail with HTTP 504 Gateway Time-out after ~60 s** (4 attempts, ~246 s, no
usage reported). With `stream: true` the same request runs fine; at `max_output_tokens=8192` it
spent all 8,192 tokens on reasoning (incomplete, no answer, $0.029); at 16,384 it completed in 100 s
with 9,370 reasoning + 1,108 answer tokens and intact JSON (40 entries), ~$0.037. The client now streams
by default (SSE; final `response.completed` object is used) and no longer retries an incomplete
response whose reason is `max_output_tokens` (it would burn the same budget again).

**Multi-turn input.** `input` accepts a list of `{"role": "user"|"assistant", "content": str}` messages
on all 7 models. Asked "What code word did you give me, and who chose it?", every model recalled the
code word stated in the assistant turn and attributed it to itself (`"chosen_by": "you"`, e.g.
"I generated the code word PELICAN-47 for you"). The cache key is canonical JSON (`sort_keys`), so list
inputs hash deterministically (dict key order ignored, message order significant).

**Other limits found while doing this (important for planning).** qwen3.5-397b has a **per-key
in-flight cap of 3**: 6 concurrent requests on one key → 3 accepted, 3 rejected instantly with the same
429 message as the window limit; 3 + 3 on the two keys all succeeded. deepseek-v4-flash (12 concurrent),
glm-5.2 (5), qwen3.8-27b (6) and gemma-4-26b (6) showed no cap at those levels; gemma-4-31b and
glm-5.3-flash are **unmeasured** (that test was 429ed wholesale while key 1 had used only ~32
requests in the past minute, so there may be a further limit, e.g. on output tokens, that I could not
pin down within the request budget). The client enforces `MODEL_INFLIGHT_CAP = {"qwen3.5-397b": 3}`
per key across processes. Also: during one ~15-minute stretch the service was heavily congested
(6 concurrent 600-token deepseek requests took 28-163 s instead of ~4.4 s; no errors); 10 minutes
later the identical test ran at normal speed (6 concurrent, 4.3 s each). Expect latency spikes."""

NOTES_RECOMMENDED = """Client defaults: `per_key_concurrency=48` (the request window is the binding limit; with reasoning on,
calls take 10-100 s), `rpm_per_key={1: 46, 2: 23}`, `stream=True`, `timeout_s=300`, `max_attempts=8`
with exponential backoff + jitter, Retry-After honoured (capped at 60 s). **The RPM window is shared
across processes** (state file per key under `cache/llm/`, `fcntl`-locked; a 429 burst lowers the shared
limit by 20 %, recovering 10 % per 30 s), and so is the qwen3.5-397b in-flight cap (lock-file tickets).
Several experiment processes can therefore run at once without exceeding the per-key limits. Nothing
else in the client caps throughput: httpx allows total concurrency + 8 connections and `run_jobs`
uses 2 × total concurrency workers.
For reasoning-off settings, a short JSON answer needs ~10 output tokens; the floors leave room for longer
answers. With reasoning on, use at least `max_output_tokens_floor_reasoning`."""

def phase_specs():
    d = load()
    from memlab.clients.adaption import total_spend
    d_spend = total_spend()
    lines = ["# SPECS — compute and API facts", "",
             f"_Generated by `experiments/setup_probe.py` from `results/setup/probe.json` "
             f"({d.get('updated_utc', '?')})._", "",
             f"**Hardware:** {HARDWARE}", "",
             "**API:** Adaption Labs, `POST https://api.prod.adaptionlabs.ai/api/v1/responses`, 2 keys, "
             "7 hosted models. No logprobs, no batch endpoint, no seed. `usage.cost` is returned per call.", "",
             "## Models", "",
             "| model | price in/out ($/1M) | median latency (s), default → rec. | reasoning tok, default → rec. | "
             "reasoning control (recommended `extra`) | `json_object` | `json_schema` | T=1 distinct / T=0 distinct |",
             "|---|---|---|---|---|---|---|---|"]
    lat, rec, js, tmp = d.get("latency", {}), d.get("recommended", {}), d.get("json", {}), d.get("temperature", {})
    for m in MODELS:
        L = lat.get(m, {})
        ld, lr = L.get("default", {}), L.get("recommended", {})
        r = rec.get(m, {})
        J = js.get(m, {})

        def jf(x):
            if not x:
                return "?"
            if x.get("error"):
                return "rejected"
            return "yes (strict JSON)" if x.get("schema_ok") or x.get("strict_json") else "accepted, not enforced"
        T = tmp.get(m, {})
        t1, t0 = T.get("T=1.0", {}), T.get("T=0.0", {})
        lines.append(
            f"| `{m}` | {PRICES[m][0]} / {PRICES[m][1]} | {ld.get('median_latency_s')} → {lr.get('median_latency_s')} | "
            f"{ld.get('median_reasoning_tokens')} → {lr.get('median_reasoning_tokens')} | "
            f"`{json.dumps(r.get('extra', {}))}` | {jf(J.get('json_object'))} | {jf(J.get('json_schema'))} | "
            f"{t1.get('n_distinct')}/{t1.get('n')} · {t0.get('n_distinct')}/{t0.get('n')} |")
    lines += ["", NOTES_MODELS, "", "## Rate limits", ""]
    rl = d.get("ratelimit", {})
    for name, steps in rl.items():
        if isinstance(steps, list):
            lines.append(f"- **{name}**: " + "; ".join(
                f"c={s['concurrency_per_key']}/key → {s['throughput_rps']} req/s, 429s {s['n_429']}/{s['n']}, "
                f"err {s['n_err']}, med lat {s['median_latency_s']}s" for s in steps))
        elif isinstance(steps, dict) and "rpm" not in steps:
            lines.append(f"- **{name}**: `{json.dumps(steps)}`")
        elif isinstance(steps, dict):
            lines.append(f"- **{name}**: {steps.get('rpm')} successful req/min with {steps.get('per_key_concurrency')}"
                         f"/key on both keys over {steps.get('wall_s')} s; 429s seen {steps.get('http_429_seen')}, "
                         f"errors {steps.get('errors')}, median latency {steps.get('median_latency_s')} s.")
    lines += ["", NOTES_RATELIMIT, "", "## Study settings (reasoning on, effort \"low\")", "",
              "`STUDY_EXTRA` (all models) = `{\"reasoning\": {\"effort\": \"low\"}}`, "
              "`STUDY_MAX_OUTPUT_TOKENS = 16384`, streaming on (client default).", "",
              "| model | effort low accepted | reasoning tok (easy / medium prompt) | reasoning kept out of answer | "
              "latency easy (s) | multi-turn list input | recalls own code word | attributes it to itself |",
              "|---|---|---|---|---|---|---|---|"]
    st = d.get("study", {})
    for m in MODELS:
        e = st.get("effort_low", {}).get(m, {})
        b = st.get("budget_and_stream", {}).get(m, {})
        mid = (b.get("effort=low") or b.get("effort=low (stream smoke)") or {})
        mt = st.get("multi_turn", {}).get(m, {})
        mid_rt = mid.get("usage", {}).get("reasoning_tokens") if not mid.get("error") else "429 (see text)"
        lines.append(f"| `{m}` | {'yes' if e and not e.get('error') else 'NO'} | "
                     f"{e.get('usage', {}).get('reasoning_tokens')} / {mid_rt} | "
                     f"{'yes' if e.get('reasoning_in_item') and e.get('strict_json') else 'no'} | "
                     f"{e.get('latency_s')} | {'accepted' if mt and not mt.get('error') else 'error'} | "
                     f"{mt.get('recalls_code')} | {mt.get('attributes_to_self')} |")
    lines += ["", NOTES_STUDY, "", "## Recommended settings", "",
              "Exported as `MODEL_DEFAULTS` in `memlab/clients/adaption.py`:", "", "```python",
              "MODEL_DEFAULTS = " + json.dumps(MODEL_DEFAULTS, indent=4).replace("false", "False")
              .replace("true", "True"), "```", "", NOTES_RECOMMENDED, "",
              f"Ledger total spend at generation time: ${d_spend:.4f} (probe tag `{TAG}`). The raw-HTTP phases "
              "(`window`, `capacity`) and a few manual checks bypass the client and are not in the ledger; "
              "their estimated cost is about $0.03 (mostly ~440k input tokens of deepseek-v4-flash).", ""]
    (ROOT / "SPECS.md").write_text("\n".join(lines))
    print("wrote SPECS.md")


async def main(phases):
    for ph in phases:
        print(f"=== {ph} ===", flush=True)
        if ph == "specs":
            phase_specs()
        elif ph == "recommend":
            save("recommended", pick_recommended(load()["reasoning"]))
            print(json.dumps(load()["recommended"], indent=1))
        elif ph.startswith("sustained"):
            parts = ph.split(":")
            conc = int(parts[1]) if len(parts) > 1 else 8
            rpm = float(parts[2]) if len(parts) > 2 else None
            await phase_sustained(conc, rpm)
        else:
            await globals()[f"phase_{ph}"]()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--phases", default="smoke,reasoning,recommend,hardcheck,latency,json,temperature,ratelimit,window,sustained,specs")
    a = ap.parse_args()
    asyncio.run(main(a.phases.split(",")))
