"""Fast CPU tests for memlab.local on tiny models.

Run: HF_HOME="$PWD/cache/hf" .venv/bin/python -m pytest tests/test_local.py -q
Model-dependent tests are skipped if the tiny models cannot be loaded (no network and no cache).
"""
from __future__ import annotations

import math

import numpy as np
import pytest
import torch

from memlab.local.model import LocalLM, PlainLM, load_npz, save_npz, strip_thinking

TINY_PLAIN = "sshleifer/tiny-gpt2"
TINY_CHAT = "HuggingFaceTB/SmolLM2-135M-Instruct"


def _load(cls, hf_id, **kw):
    try:
        return cls(hf_id, device="cpu", dtype="fp32", **kw)
    except Exception as e:  # download / cache problems -> skip, not fail
        pytest.skip(f"cannot load {hf_id}: {type(e).__name__}: {e}")


@pytest.fixture(scope="module")
def plain():
    return _load(PlainLM, TINY_PLAIN)


@pytest.fixture(scope="module")
def chat():
    torch.manual_seed(0)
    return _load(LocalLM, TINY_CHAT)


def _chats():
    return [
        [{"role": "user", "content": "What is the capital of France?"}],
        [{"role": "system", "content": "You are a careful inventory assistant."},
         {"role": "user", "content": "Summarise today's stock check in one sentence. Widgets: 14, gears: 3."}],
        [{"role": "user", "content": "Say hi."}],
    ]


CONTS = [
    "The capital of France is Paris.",
    "Stock check: 14 widgets and 3 gears on hand; gears are running low.",
    "Hi!",
]


# ---------------------------------------------------------------- no model needed
def test_strip_thinking():
    assert strip_thinking("<think>\nhmm\n</think>\n\nAnswer.") == "Answer."
    assert strip_thinking("Answer. <think>unterminated") == "Answer."
    assert strip_thinking("  plain  ") == "plain"


def test_npz_roundtrip(tmp_path):
    a = np.random.randn(3, 4, 5).astype(np.float32)
    ids = np.arange(3)
    p = save_npz(tmp_path / "acts", meta={"model": "x", "layers": [1, 2]}, acts=a, ids=ids)
    assert p.suffix == ".npz" and p.with_suffix(".json").exists()
    arrays, meta = load_npz(p)
    assert arrays["acts"].dtype == np.float16 and arrays["acts"].shape == (3, 4, 5)
    assert np.allclose(arrays["acts"], a, atol=1e-2)
    assert arrays["ids"].dtype.kind == "i"
    assert meta == {"model": "x", "layers": [1, 2]}


# ---------------------------------------------------------------- PlainLM
def test_plain_batched_equals_unbatched(plain):
    texts = ["The cat sat on the mat.", "A considerably longer sentence about inventory, widgets and gears.", "Hi"]
    batched = plain.perplexity(texts, batch_size=3)
    for t, b in zip(texts, batched):
        u = plain.perplexity([t], batch_size=1)[0]
        assert u["n"] == b["n"] == len(plain.tokenizer(t, add_special_tokens=False)["input_ids"])
        assert np.allclose(u["surprisal"], b["surprisal"], atol=1e-3)
        assert math.isfinite(b["mean"]) and b["max"] >= b["mean"] >= b["min"]


def test_plain_context_left_truncation(plain):
    plain_small = plain.max_length
    try:
        plain.max_length = 32
        ctx = " ".join(f"word{i}" for i in range(200))
        r = plain.perplexity(["the end"], contexts=[ctx])[0]
        assert r["n"] == len(plain.tokenizer("the end", add_special_tokens=False)["input_ids"])
        assert r["context_tokens"] + r["n"] + 1 == 32
        r2 = plain.perplexity(["the end"], contexts=["short context "])[0]
        assert r2["context_tokens"] == len(plain.tokenizer("short context ", add_special_tokens=False)["input_ids"])
    finally:
        plain.max_length = plain_small


# ---------------------------------------------------------------- LocalLM
def test_score_batched_equals_unbatched(chat):
    chats = _chats()
    batched = chat.score_continuation(chats, CONTS, batch_size=3)
    for m, c, b in zip(chats, CONTS, batched):
        u = chat.score_continuation([m], [c], batch_size=1)[0]
        assert u["n"] == b["n"]
        assert np.allclose(u["surprisal"], b["surprisal"], atol=1e-3)


def test_score_token_count_and_first_token(chat):
    chats = _chats()
    res = chat.score_continuation(chats, CONTS)
    for m, c, r in zip(chats, CONTS, res):
        ids = chat.tokenizer(c, add_special_tokens=False)["input_ids"]
        assert r["n"] == len(ids) == len(r["surprisal"]) == len(r["tokens"])
        assert "".join(r["tokens"]) == c
        # independent reference: full forward, manual indexing
        p = chat.tokenizer(chat.render(m), add_special_tokens=False)["input_ids"]
        with torch.inference_mode():
            logits = chat.model(torch.tensor([p + ids])).logits[0].float()
        lp = torch.log_softmax(logits, -1)
        ref = [-lp[len(p) - 1 + j, t].item() for j, t in enumerate(ids)]
        assert np.allclose(ref, r["surprisal"], atol=1e-3)
        assert r["sum"] == pytest.approx(sum(ref), abs=1e-2)


def test_activations_shapes(chat):
    chats = _chats()
    acts = chat.activations(chats, CONTS, layers="auto")
    L = chat.resolve_layers("auto")
    assert len(L) == 4 and L[-1] == chat.n_layers and L[0] == round(0.25 * chat.n_layers)
    for k in ("mean", "last"):
        assert acts[k].shape == (3, 4, chat.d_model) and acts[k].dtype == np.float16
        assert np.isfinite(acts[k]).all()
    acts2 = chat.activations(chats, CONTS, layers=[0, -1])
    assert acts2["layers"] == [0, chat.n_layers] and acts2["mean"].shape == (3, 2, chat.d_model)


def test_score_and_activations_consistent(chat):
    chats = _chats()
    s, a = chat.score_and_activations(chats, CONTS, layers=[2, 5], batch_size=2)
    s_ref = chat.score_continuation(chats, CONTS, batch_size=1)
    a_ref = chat.activations(chats, CONTS, layers=[2, 5], batch_size=1)
    for x, y in zip(s, s_ref):
        assert np.allclose(x["surprisal"], y["surprisal"], atol=1e-3)
    assert np.allclose(a["mean"].astype(np.float32), a_ref["mean"].astype(np.float32), atol=2e-2)
    assert np.allclose(a["last"].astype(np.float32), a_ref["last"].astype(np.float32), atol=2e-2)


def test_p_yes_range(chat):
    q = [[{"role": "user", "content": "Is Paris the capital of France? Answer Yes or No."}],
         [{"role": "user", "content": "Is 7 an even number? Answer Yes or No."}]]
    ps = chat.p_yes(q)
    assert all(0.0 <= p <= 1.0 for p in ps)
    detail = chat.p_yes(q[:1], return_mass=True)[0]
    assert detail["p_yes"] == pytest.approx(ps[0], abs=1e-5)
    assert ps == pytest.approx(chat.p_yes(q, batch_size=1), abs=1e-4)


def test_generate_deterministic_and_batch_invariant(chat):
    chats = _chats()
    g1 = chat.generate(chats, max_new_tokens=12, temperature=0.0, batch_size=3)
    g2 = chat.generate(chats, max_new_tokens=12, temperature=0.0, batch_size=3)
    assert g1 == g2 and all(isinstance(t, str) for t in g1)
    single = [chat.generate([m], max_new_tokens=12, temperature=0.0)[0] for m in chats]
    assert single == g1  # left padding does not change greedy output
    s1 = chat.generate(chats, max_new_tokens=8, temperature=0.8, seed=3, batch_size=3)
    s2 = chat.generate(chats, max_new_tokens=8, temperature=0.8, seed=3, batch_size=3)
    assert s1 == s2
