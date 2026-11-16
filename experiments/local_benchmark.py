"""Benchmark and sanity-check the local models on this machine (MPS).

Writes results/setup/local_benchmark.json and results/setup/LOCAL_SPECS.md.

Run OUTSIDE the sandbox (MPS is not visible inside it):
    HF_HOME="$PWD/cache/hf" TOKENIZERS_PARALLELISM=false .venv/bin/python experiments/local_benchmark.py
Options: --models primary secondary   --quick (fewer repeats, for smoke tests)
"""
from __future__ import annotations

import argparse
import json
import platform
import random
import sys
import threading
import time
from pathlib import Path

import numpy as np
import torch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from memlab.local.model import MODELS, LocalLM, PlainLM, free_memory  # noqa: E402

OUT_DIR = ROOT / "results" / "setup"
MEM_BUDGET_GB = 18.0  # "safe" = peak driver memory below this on a 24 GB machine

WORDS = ("widget gear bolt shelf aisle restock order pallet supplier invoice count audit trial sample "
         "report meeting deadline budget review note memory session observation customer request delay "
         "shipment warehouse ledger update confirm cancel verify check record entry total missing extra").split()


# ---------------------------------------------------------------------------------------------- utils
class PeakMem:
    """Polls torch.mps.driver_allocated_memory() in a thread; .peak in bytes."""

    def __init__(self, interval=0.02):
        self.interval, self.peak, self._stop = interval, 0, threading.Event()

    def _run(self):
        while not self._stop.is_set():
            self.peak = max(self.peak, torch.mps.driver_allocated_memory())
            time.sleep(self.interval)

    def __enter__(self):
        self.peak = torch.mps.driver_allocated_memory()
        self._t = threading.Thread(target=self._run, daemon=True)
        self._t.start()
        return self

    def __exit__(self, *a):
        self._stop.set()
        self._t.join()
        self.peak = max(self.peak, torch.mps.driver_allocated_memory())


def gb(x):
    return round(x / 2**30, 2)


def filler(rng: random.Random, n_tokens: int, tok) -> str:
    """Deterministic log-like text of roughly n_tokens tokens."""
    lines, text = [], ""
    while len(tok(text, add_special_tokens=False)["input_ids"]) < n_tokens:
        lines.append(f"[{len(lines):03d}] " + " ".join(rng.choice(WORDS) for _ in range(12)) + f" = {rng.randint(0, 999)}.")
        text = "\n".join(lines)
    return text


def make_chats(lm: LocalLM, n: int, prompt_tokens: int, seed=0):
    rng = random.Random(seed)
    chats = []
    for i in range(n):
        body = filler(rng, prompt_tokens - 60, lm.tokenizer)
        chats.append([
            {"role": "system", "content": "You are an inventory agent. After each session you write one short memory note."},
            {"role": "user", "content": f"Session {i} trace:\n{body}\n\nWrite your memory note for this session."},
        ])
    return chats


def make_conts(lm: LocalLM, n: int, cont_tokens: int, seed=1):
    rng = random.Random(seed)
    return [filler(rng, cont_tokens, lm.tokenizer) for _ in range(n)]


def sync():
    if torch.backends.mps.is_available():
        torch.mps.synchronize()


# ---------------------------------------------------------------------------------------------- checks
def dtype_check(lm: LocalLM) -> dict:
    """NaN/inf check on short and ~500-token inputs over ALL layers, plus the largest |activation| seen
    (fp16 overflows at 65504)."""
    chats = [[{"role": "user", "content": "Write one sentence about warehouses."}]] + make_chats(lm, 3, 420, seed=99)
    conts = ["Warehouses store goods until they are shipped to customers."] + make_conts(lm, 3, 80, seed=98)
    s = lm.score_continuation(chats, conts, batch_size=4)
    finite = all(np.isfinite(x["surprisal"]).all() for x in s)
    max_abs = 0.0
    for m, c in zip(chats, conts):  # raw hidden states at every position
        ids = lm._prompt_ids(m) + lm._encode(c)
        with torch.inference_mode():
            o = lm._base(input_ids=torch.tensor([ids], device=lm.device), output_hidden_states=True, use_cache=False)
        for h in o.hidden_states:
            finite &= bool(torch.isfinite(h).all())
            max_abs = max(max_abs, float(h.abs().max()))
        del o
    free_memory()
    return {"finite": bool(finite), "mean_surprisal": float(np.mean([x["mean"] for x in s])), "max_abs_hidden": max_abs}


def sanity(lm: LocalLM) -> dict:
    out = {}
    # 1) thinking disabled
    chat = [{"role": "user", "content": "In one sentence, what does a warehouse manager do?"}]
    rendered = lm.render(chat)
    enc = lm.tokenizer([rendered], return_tensors="pt", add_special_tokens=False).to(lm.device)
    with torch.inference_mode():
        g = lm.model.generate(**enc, max_new_tokens=60, do_sample=False, eos_token_id=lm.eos_ids, pad_token_id=lm.pad_id)
    raw = lm.tokenizer.decode(g[0, enc["input_ids"].shape[1]:], skip_special_tokens=False)
    out["prompt_tail"] = rendered[-60:]
    out["raw_generation_contains_think"] = "<think>" in raw or "</think>" in raw
    out["raw_generation"] = raw[:300]

    # 2) own greedy sentence vs shuffled words
    prompts = [
        "In one sentence, what does a warehouse manager do?",
        "Describe a sunrise in one sentence.",
        "In one sentence, why do people keep diaries?",
        "Give one sentence of advice for a new programmer.",
        "In one sentence, explain what a memory note is.",
        "Summarise in one sentence: 14 widgets were counted, 3 gears are missing, a restock was ordered.",
    ]
    chats = [[{"role": "user", "content": p}] for p in prompts]
    gens = lm.generate(chats, max_new_tokens=60)
    rng = random.Random(0)
    shuf = []
    for t in gens:
        w = t.split()
        rng.shuffle(w)
        shuf.append(" ".join(w))
    s_own = lm.score_continuation(chats, gens)
    s_shuf = lm.score_continuation(chats, shuf)
    pairs = [{"text": t, "own_mean": a["mean"], "shuffled_mean": b["mean"]} for t, a, b in zip(gens, s_own, s_shuf)]
    out["own_vs_shuffled"] = pairs
    out["own_lower_than_shuffled_all"] = all(p["own_mean"] < p["shuffled_mean"] for p in pairs)

    # 3) p_yes
    qs = {
        "paris_capital_france": "Is Paris the capital of France? Answer Yes or No.",
        "seven_even": "Is 7 an even number? Answer Yes or No.",
        "water_wet": "Is water wet? Answer Yes or No.",
        "sun_cold": "Is the Sun colder than ice? Answer Yes or No.",
    }
    res = lm.p_yes([[{"role": "user", "content": q}] for q in qs.values()], return_mass=True)
    out["p_yes"] = dict(zip(qs, res))
    out["p_yes_paris_gt_0.5"] = res[0]["p_yes"] > 0.5

    # 4) batched vs unbatched on the real model
    chats3 = make_chats(lm, 4, 150, seed=5)
    conts3 = make_conts(lm, 4, 40, seed=6)
    conts3[1] = conts3[1][: len(conts3[1]) // 3]  # unequal lengths -> real padding
    b = lm.score_continuation(chats3, conts3, batch_size=4)
    u = [lm.score_continuation([m], [c], batch_size=1)[0] for m, c in zip(chats3, conts3)]
    out["score_batched_vs_unbatched_max_abs_diff"] = float(max(np.max(np.abs(np.array(x["surprisal"]) - np.array(y["surprisal"]))) for x, y in zip(b, u)))
    out["score_batched_vs_unbatched_mean_abs_diff_of_means"] = float(np.mean([abs(x["mean"] - y["mean"]) for x, y in zip(b, u)]))
    gb_ = lm.generate(chats[:4], max_new_tokens=40, batch_size=4)
    gu = [lm.generate([c], max_new_tokens=40)[0] for c in chats[:4]]
    out["greedy_batched_equals_unbatched"] = [x == y for x, y in zip(gb_, gu)]
    pa = lm.p_yes([[{"role": "user", "content": q}] for q in qs.values()], batch_size=4)
    pu = [lm.p_yes([[{"role": "user", "content": q}]])[0] for q in qs.values()]
    out["p_yes_batched_vs_unbatched_max_abs_diff"] = float(np.max(np.abs(np.array(pa) - np.array(pu))))

    # 5) hidden-state convention: is hidden_states[n_layers] the pre-final-norm residual?
    ids = torch.tensor([lm._prompt_ids(chat)], device=lm.device)
    with torch.inference_mode():
        o = lm._base(input_ids=ids, output_hidden_states=True, use_cache=False)
    out["n_hidden_states"] = len(o.hidden_states)
    out["last_hidden_state_equals_hidden_states[-1]"] = bool(torch.allclose(o.hidden_states[-1].float(), o.last_hidden_state.float(), atol=1e-3))
    free_memory()
    return out


# ---------------------------------------------------------------------------------------------- benchmarks
def bench_generate(lm: LocalLM, sizes, repeats: int) -> list[dict]:
    rows = []
    chats_all = make_chats(lm, max(sizes) * repeats, 400, seed=11)
    lm.generate(chats_all[:1], max_new_tokens=8)  # warm-up
    for bs in sizes:
        free_memory()
        chats = chats_all[: bs * repeats]
        try:
            with PeakMem() as pm:
                sync(); t0 = time.perf_counter()
                lm.generate(chats, max_new_tokens=80, min_new_tokens=80, batch_size=bs)
                sync(); dt = time.perf_counter() - t0
            n_tok = 80 * len(chats)
            rows.append({"batch_size": bs, "n_items": len(chats), "seconds": round(dt, 2),
                         "new_tokens_per_s": round(n_tok / dt, 1), "items_per_s": round(len(chats) / dt, 3),
                         "peak_driver_gb": gb(pm.peak), "ok": True})
        except RuntimeError as e:
            rows.append({"batch_size": bs, "ok": False, "error": str(e)[:200]})
        print("  gen", rows[-1], flush=True)
    return rows


def bench_forward(lm: LocalLM, sizes, repeats: int) -> list[dict]:
    rows = []
    n = max(sizes) * repeats
    chats = make_chats(lm, n, 420, seed=21)
    conts = make_conts(lm, n, 80, seed=22)
    lm.score_and_activations(chats[:2], conts[:2], batch_size=2)  # warm-up
    for bs in sizes:
        free_memory()
        k = bs * repeats
        try:
            with PeakMem() as pm:
                sync(); t0 = time.perf_counter()
                sc, ac = lm.score_and_activations(chats[:k], conts[:k], layers="auto", batch_size=bs)
                sync(); dt = time.perf_counter() - t0
            finite = bool(all(np.isfinite(x["surprisal"]).all() for x in sc) and np.isfinite(ac["mean"]).all()
                          and np.isfinite(ac["last"]).all())
            rows.append({"batch_size": bs, "n_items": k, "seconds": round(dt, 2), "items_per_s": round(k / dt, 2),
                         "peak_driver_gb": gb(pm.peak), "ok": finite, "finite": finite,
                         "mean_surprisal": round(float(np.mean([x["mean"] for x in sc])), 4)})
        except RuntimeError as e:
            rows.append({"batch_size": bs, "ok": False, "error": str(e)[:200]})
        print("  fwd", rows[-1], flush=True)
    return rows


def best(rows, key):
    ok = [r for r in rows if r.get("ok") and r["peak_driver_gb"] < MEM_BUDGET_GB]
    if not ok:
        return None
    return max(ok, key=lambda r: r[key])


def bench_model(name: str, quick: bool, dtype_pref: str = "bf16") -> dict:
    spec = MODELS[name]
    rec = {"name": name, "hf_id": spec["id"], "revision": spec["revision"], "dtype_requested": dtype_pref}
    for dtype in dict.fromkeys((dtype_pref, "fp16", "bf16")):
        free_memory()
        t0 = time.perf_counter()
        lm = LocalLM(spec["id"], revision=spec["revision"], device="mps", dtype=dtype, batch_size=8)
        sync()
        rec["load_seconds"] = round(time.perf_counter() - t0, 1)
        chk = dtype_check(lm)
        rec.setdefault("dtype_checks", {})[dtype] = chk
        if chk["finite"]:
            rec["dtype"] = dtype
            break
        print(f"  {dtype} produced non-finite values; trying next dtype", flush=True)
        del lm
    else:
        raise RuntimeError("no dtype produced finite outputs")
    rec["weights_driver_gb"] = gb(torch.mps.driver_allocated_memory())
    rec["n_layers"], rec["d_model"] = lm.n_layers, lm.d_model
    rec["auto_layers"] = lm.resolve_layers("auto")
    rec["n_params"] = int(sum(p.numel() for p in lm.model.parameters()))
    rec["model_class"] = type(lm.model).__name__
    rec["eos_ids"] = lm.eos_ids
    print(f"[{name}] loaded {spec['id']} in {rec['load_seconds']}s dtype={rec['dtype']}", flush=True)

    rec["sanity"] = sanity(lm)
    print("  sanity:", {k: v for k, v in rec["sanity"].items() if k not in ("own_vs_shuffled", "raw_generation")}, flush=True)
    reps = 1 if quick else 2
    rec["generate"] = bench_generate(lm, [1, 4, 8, 16], reps)
    rec["forward"] = bench_forward(lm, [4, 8, 16, 32], reps)
    rec["peak_driver_gb"] = max([r.get("peak_driver_gb", 0) for r in rec["generate"] + rec["forward"]] + [rec["weights_driver_gb"]])

    g, f = best(rec["generate"], "items_per_s"), best(rec["forward"], "items_per_s")
    rec["recommended"] = {
        "generate_batch_size": g and g["batch_size"],
        "forward_batch_size": f and f["batch_size"],
        "largest_safe_generate_batch": max([r["batch_size"] for r in rec["generate"] if r.get("ok") and r["peak_driver_gb"] < MEM_BUDGET_GB], default=None),
        "largest_safe_forward_batch": max([r["batch_size"] for r in rec["forward"] if r.get("ok") and r["peak_driver_gb"] < MEM_BUDGET_GB], default=None),
    }
    if g and f:
        gps, fps = g["items_per_s"], f["items_per_s"]
        rec["estimates_hours"] = {
            "a_generate_2100_notes_80tok": round(2100 / gps / 3600, 2),
            "b_generate_8x600_rewrites_80tok": round(4800 / gps / 3600, 2),
            "c_score_12000_pairs_twice": round(24000 / fps / 3600, 2),
        }
    del lm
    free_memory()
    return rec


def bench_plain() -> dict:
    out = {}
    text = "The warehouse manager counted fourteen widgets and ordered a restock of gears."
    shuffled = "gears restock The of counted widgets manager fourteen a ordered and warehouse."
    for key, kw in [("gpt2", {"device": "cpu", "dtype": "fp32"}), ("secondary", {"device": "mps", "dtype": "bf16"})]:
        spec = MODELS[key]
        t0 = time.perf_counter()
        lm = PlainLM(spec["id"], revision=spec["revision"], **kw)
        load = time.perf_counter() - t0
        texts = [text, shuffled] * 16
        t0 = time.perf_counter()
        r = lm.perplexity(texts, contexts=["Inventory log, Monday. "] * len(texts), batch_size=16)
        dt = time.perf_counter() - t0
        out[key] = {"hf_id": spec["id"], "revision": spec["revision"], **kw, "load_seconds": round(load, 1),
                    "texts_per_s": round(len(texts) / dt, 1), "max_length": lm.max_length,
                    "mean_surprisal_sentence": r[0]["mean"], "mean_surprisal_shuffled": r[1]["mean"],
                    "sentence_lower": r[0]["mean"] < r[1]["mean"]}
        print("  plain", key, out[key], flush=True)
        del lm
        free_memory()
    return out


# ---------------------------------------------------------------------------------------------- report
def write_md(res: dict, path: Path):
    L = ["# Local models — specs and benchmark", "",
         f"Measured {res['timestamp']} on {res['machine']} (torch {res['torch']}, transformers {res['transformers']}, MPS).",
         "Generated by `experiments/local_benchmark.py`; raw numbers in `local_benchmark.json`.", "",
         "## Models", "", "| role | HF id | revision | dtype | layers | d_model | auto layers | params | load s | weights GB |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    for m in res["models"]:
        L.append(f"| {m['name']} ({m['dtype']}) | `{m['hf_id']}` | `{m['revision'][:12]}` | {m['dtype']} | {m['n_layers']} | {m['d_model']} | "
                 f"{m['auto_layers']} | {m['n_params']/1e9:.2f}B | {m['load_seconds']} | {m['weights_driver_gb']} |")
    for k, p in res.get("plain", {}).items():
        L.append(f"| plain/{k} | `{p['hf_id']}` | `{p['revision'][:12]}` | {p['dtype']} ({p['device']}) | | | | | {p['load_seconds']} | |")
    L += ["", "Thinking mode is disabled everywhere (`enable_thinking=False`; the template then appends an empty "
          "`<think></think>` block to the generation prompt, so scored continuations follow it).", ""]
    for m in res["models"]:
        s = m["sanity"]
        L += [f"## {m['name']}: `{m['hf_id']}` in {m['dtype']}", "",
              f"- dtype checks: {json.dumps(m['dtype_checks'])}",
              f"- peak driver memory over all runs: {m['peak_driver_gb']} GB",
              f"- no `<think>` in raw greedy output: {not s['raw_generation_contains_think']}",
              f"- own greedy sentence lower surprisal than its word-shuffle (all {len(s['own_vs_shuffled'])}): {s['own_lower_than_shuffled_all']} "
              f"(mean own {np.mean([p['own_mean'] for p in s['own_vs_shuffled']]):.2f} vs shuffled {np.mean([p['shuffled_mean'] for p in s['own_vs_shuffled']]):.2f} nats/token)",
              f"- p_yes: " + ", ".join(f"{k}={v['p_yes']:.3f} (yes+no mass {v['mass_yes']+v['mass_no']:.2f})" for k, v in s["p_yes"].items()),
              f"- batched vs unbatched: surprisal max |diff| {s['score_batched_vs_unbatched_max_abs_diff']:.4f} nats, "
              f"greedy equal {s['greedy_batched_equals_unbatched']}, p_yes max |diff| {s['p_yes_batched_vs_unbatched_max_abs_diff']:.4f}",
              f"- hidden_states: {s['n_hidden_states']} entries; last equals post-norm last_hidden_state: {s['last_hidden_state_equals_hidden_states[-1]']}",
              "", "Generation (~400-token prompt, exactly 80 new tokens):", "",
              "| batch | items | s | new tok/s | items/s | peak GB |", "|---|---|---|---|---|---|"]
        for r in m["generate"]:
            L.append(f"| {r['batch_size']} | {r.get('n_items','')} | {r.get('seconds','')} | {r.get('new_tokens_per_s','')} | {r.get('items_per_s','')} | {r.get('peak_driver_gb', 'FAIL')} |")
        L += ["", "`score_and_activations` (~420-token prompt + ~80-token continuation, 4 auto layers):", "",
              "| batch | items | s | items/s | peak GB |", "|---|---|---|---|---|"]
        for r in m["forward"]:
            L.append(f"| {r['batch_size']} | {r.get('n_items','')} | {r.get('seconds','')} | {r.get('items_per_s','')} | {r.get('peak_driver_gb', 'FAIL')} |")
        L += ["", f"Recommended: {json.dumps(m['recommended'])}", ""]
        if "estimates_hours" in m:
            e = m["estimates_hours"]
            L += ["Wall-clock estimates at the recommended batch sizes (single process, model already loaded):", "",
                  f"- (a) 2,100 notes × ~80 tokens: **{e['a_generate_2100_notes_80tok']} h**",
                  f"- (b) 8 rewrites × 600 notes (4,800 × ~80 tokens): **{e['b_generate_8x600_rewrites_80tok']} h**",
                  f"- (c) 12,000 (prompt, note) pairs scored twice (24,000 forward items): **{e['c_score_12000_pairs_twice']} h**", ""]
    if res.get("plain"):
        L += ["## External-perplexity scorers (PlainLM)", ""]
        for k, p in res["plain"].items():
            L.append(f"- {k}: {p['texts_per_s']} texts/s (short texts, batch 16, {p['device']}); sentence {p['mean_surprisal_sentence']:.2f} "
                     f"vs shuffled {p['mean_surprisal_shuffled']:.2f} nats/token; window {p['max_length']}")
    L += ["", NOTES]
    path.write_text("\n".join(L) + "\n")


NOTES = """## Notes (hand-written, Fri 13 Nov)

- **Model choice.** `Qwen/Qwen3.5-4B` and `Qwen/Qwen3.5-0.8B` exist, are ungated, Apache-2.0, and are the
  post-trained (instruct/thinking hybrid) checkpoints; the `-Base` variants are separate repos. The Qwen3.5
  small family has 0.8B, 2B, 4B, 9B. No fallback was needed. The repos are vision-language checkpoints
  (`Qwen3_5ForConditionalGeneration`); `AutoModelForCausalLM` loads the text-only `Qwen3_5ForCausalLM`
  (vision tower and MTP head weights are ignored). Architecture is hybrid: 3 of every 4 layers are Gated
  DeltaNet linear attention, every 4th is full attention.
- **Thinking disabled.** `apply_chat_template(..., enable_thinking=False)` appends an empty
  `<think>\\n\\n</think>\\n\\n` to the generation prompt; generated text never contained `<think>`.
  Teacher-forced continuations are scored after that empty think block (i.e. as the model would emit them).
- **dtype.** Both bf16 and fp16 run on MPS without NaNs/inf (all layers checked, see `max_abs_hidden`,
  well below the fp16 limit 65504). bf16, however, is numerically noisy in a way that depends on batch
  shape: in a direct test on the 4B model, the *same* item scored alone vs. inside a batch of 4 identical
  items differed by up to 0.13 nats on one token in bf16 vs 0.015 in fp16; p_yes batched vs unbatched
  differed by 0.025 (bf16) vs 0.002 (fp16). Same speed. **Use fp16** (now the `LocalLM` default).
  The implementation itself is exact: in fp32 on CPU (0.8B), batched vs unbatched surprisal agree to 3e-5.
- **Greedy generation** in bf16 can diverge between batched and unbatched runs after a few tokens
  (tiny logit differences flip an argmax); this is expected, not a padding bug (fp32 CPU tests agree exactly).
  Sampled generations depend on seed *and* on chunk composition.
- **Speed.** No fused kernels on MPS (`flash-linear-attention`/`causal-conv1d` need CUDA/Triton), so the
  linear-attention layers use the reference PyTorch implementation: in a 4B forward (8 x 500 tokens)
  ~40% of time is Gated DeltaNet, ~48% MLP, ~8% full attention. Forward throughput is compute-bound and
  flat in batch size >= 4, so batch size mainly trades memory.
- **hidden_states convention** (transformers 5.23): 33 entries for the 4B model; entry 32 equals the
  post-final-norm `last_hidden_state`; entries 0..31 are raw residual stream. `layers="auto"` = [8, 16, 24, 32]
  (4B) / [6, 12, 18, 24] (0.8B).
- **Downloads inside the Claude sandbox** need `SSL_CERT_FILE=$(python -c 'import certifi;print(certifi.where())')`
  (macOS trust store is blocked) and `HF_HUB_DISABLE_XET=1` (the Xet client hangs behind the proxy); LFS files
  come from `us.aws.cdn.hf.co`. With the cache populated, use `HF_HUB_OFFLINE=1`.
- **Cost-saving idea for (c).** If the same ~420-token prompt is scored against many notes, the prompt
  dominates the forward cost; prefix caching would cut (c) several-fold but is not implemented.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", nargs="+", default=["primary", "secondary"])
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--no-plain", action="store_true")
    ap.add_argument("--dtypes", nargs="+", default=["fp16", "bf16"],
                    help="benchmark each model in each dtype (falls back if non-finite)")
    args = ap.parse_args()
    assert torch.backends.mps.is_available(), "MPS not available -- run outside the sandbox"
    import transformers
    res = {"timestamp": time.strftime("%Y-%m-%d %H:%M"), "machine": f"{platform.machine()} macOS {platform.mac_ver()[0]}",
           "torch": torch.__version__, "transformers": transformers.__version__, "mem_budget_gb": MEM_BUDGET_GB,
           "models": []}
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for name in args.models:
        for dt in args.dtypes:
            res["models"].append(bench_model(name, args.quick, dt))
        (OUT_DIR / "local_benchmark.json").write_text(json.dumps(res, indent=1, default=str))
    if not args.no_plain:
        res["plain"] = bench_plain()
    (OUT_DIR / "local_benchmark.json").write_text(json.dumps(res, indent=1, default=str))
    write_md(res, OUT_DIR / "LOCAL_SPECS.md")
    print("wrote", OUT_DIR / "local_benchmark.json", flush=True)


if __name__ == "__main__":
    main()
