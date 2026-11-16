"""Local open-weight language models for the "internals" side of the study.

Two classes:

* ``LocalLM``  -- a chat model. Prompts are lists of ``{"role", "content"}`` dicts rendered with the
  tokenizer's chat template (thinking/reasoning mode always disabled). Provides greedy/sampled
  generation, teacher-forced surprisal of a given assistant answer, pooled residual-stream
  activations over that answer, and a normalised next-token P(Yes).
* ``PlainLM``  -- a raw language model (no chat template) for external-perplexity baselines
  (GPT-2, or a chat model used as a plain LM).

Conventions
-----------
* Surprisal is ``-log p(token | prefix)`` in nats, computed in float32 from the model's logits.
* Layer index ``L`` refers to ``hidden_states[L]`` as returned by Hugging Face with
  ``output_hidden_states=True``: ``0`` is the embedding output, ``L`` (1..n_layers) is the residual
  stream after decoder block ``L``. NOTE: in transformers 5 the last entry (``L == n_layers``) is the
  output AFTER the final RMSNorm (it equals ``last_hidden_state``; verified for Qwen3.5), while
  all earlier entries are raw (un-normalised) residual-stream states.
* dtype: use "fp16" for Qwen3.5 on MPS. bf16 works (no NaNs) but its rounding makes results depend
  on batch shape (per-token surprisal differs by up to ~0.14 nats between batched and unbatched
  runs, p_yes by up to ~0.03-0.05); fp16 cuts this ~8x at the same speed. See LOCAL_SPECS.md.
* Scoring/activations/p_yes run with RIGHT padding (positions of real tokens are then identical
  to the unbatched case, for both attention and linear-attention/recurrent layers); generation
  runs with LEFT padding.
* All public methods take arbitrarily long lists and split them into chunks of ``batch_size``
  (sorted by length to minimise padding, results returned in input order). Device caches are
  emptied after every chunk. On an out-of-memory error the chunk is retried at half size.
"""
from __future__ import annotations

import gc
import json
import math
import os
import re
import warnings
from pathlib import Path
from typing import Iterable, Sequence

import numpy as np
import torch

os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

# Verified model ids and revisions (Hugging Face, checked Fri 13 Nov 2026). See results/setup/LOCAL_SPECS.md.
MODELS = {
    "primary": {"id": "Qwen/Qwen3.5-4B", "revision": "851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a"},
    "secondary": {"id": "Qwen/Qwen3.5-0.8B", "revision": "2fc06364715b967f1860aea9cf38778875588b17"},
    "gpt2": {"id": "openai-community/gpt2", "revision": "607a30d783dfa663caf39e06633721c8d4cfcd7e"},
}

_DTYPES = {
    "bf16": torch.bfloat16, "bfloat16": torch.bfloat16,
    "fp16": torch.float16, "float16": torch.float16,
    "fp32": torch.float32, "float32": torch.float32,
}

# End-of-turn markers of common chat templates; any of these that exist in the vocabulary stop generation.
_EOT_TOKENS = ("<|im_end|>", "<|endoftext|>", "<|eot_id|>", "<|end_of_text|>", "<end_of_turn>", "</s>", "<|end|>")

_THINK_RE = re.compile(r"<think>.*?</think>", re.DOTALL)


# ----------------------------------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------------------------------
def pick_device(device: str | None = None) -> str:
    """Return ``device`` if usable, else the best available ("mps" > "cpu")."""
    if device in (None, "auto"):
        return "mps" if torch.backends.mps.is_available() else "cpu"
    if device == "mps" and not torch.backends.mps.is_available():
        warnings.warn("MPS requested but not available (sandboxed process?); falling back to CPU.")
        return "cpu"
    if device.startswith("cuda") and not torch.cuda.is_available():
        warnings.warn("CUDA requested but not available; falling back to CPU.")
        return "cpu"
    return device


def free_memory() -> None:
    """Run the garbage collector and release cached device memory."""
    gc.collect()
    if torch.backends.mps.is_available():
        torch.mps.empty_cache()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()


def _is_oom(err: BaseException) -> bool:
    msg = str(err).lower()
    return isinstance(err, torch.OutOfMemoryError) or "out of memory" in msg or "mps backend out of memory" in msg


def _stats(surprisal: list[float]) -> dict:
    if not surprisal:
        nan = float("nan")
        return {"mean": nan, "max": nan, "min": nan, "sum": 0.0, "n": 0}
    a = np.asarray(surprisal, dtype=np.float64)
    return {"mean": float(a.mean()), "max": float(a.max()), "min": float(a.min()), "sum": float(a.sum()), "n": int(a.size)}


def strip_thinking(text: str) -> str:
    """Remove ``<think>...</think>`` blocks (and an unterminated leading ``<think>``) and strip."""
    text = _THINK_RE.sub("", text)
    if "<think>" in text:  # unterminated block: everything after it is reasoning
        text = text.split("<think>", 1)[0]
    return text.replace("</think>", "").strip()


def save_npz(path: str | os.PathLike, meta: dict | None = None, **arrays) -> Path:
    """Save arrays to a compressed ``.npz`` (floating arrays stored as float16) plus a JSON sidecar.

    The sidecar ``<path>.json`` holds ``{"meta": meta, "arrays": {name: {"shape", "dtype"}}}``.
    Returns the ``.npz`` path.
    """
    path = Path(path)
    if path.suffix != ".npz":
        path = path.with_suffix(path.suffix + ".npz") if path.suffix else path.with_suffix(".npz")
    path.parent.mkdir(parents=True, exist_ok=True)
    out = {}
    for k, v in arrays.items():
        a = v.detach().float().cpu().numpy() if isinstance(v, torch.Tensor) else np.asarray(v)
        if np.issubdtype(a.dtype, np.floating):
            a = a.astype(np.float16)
        out[k] = a
    np.savez_compressed(path, **out)
    side = {"meta": meta or {}, "arrays": {k: {"shape": list(a.shape), "dtype": str(a.dtype)} for k, a in out.items()}}
    path.with_suffix(".json").write_text(json.dumps(side, indent=1, default=str))
    return path


def load_npz(path: str | os.PathLike) -> tuple[dict[str, np.ndarray], dict]:
    """Load what ``save_npz`` wrote. Returns ``(arrays, meta)``; ``meta`` is ``{}`` without a sidecar."""
    path = Path(path)
    if path.suffix != ".npz":
        path = path.with_suffix(".npz")
    with np.load(path, allow_pickle=False) as z:
        arrays = {k: z[k] for k in z.files}
    side = path.with_suffix(".json")
    meta = json.loads(side.read_text()).get("meta", {}) if side.exists() else {}
    return arrays, meta


# ----------------------------------------------------------------------------------------------
# shared base
# ----------------------------------------------------------------------------------------------
class _Base:
    def __init__(self, hf_id: str, device: str | None = "mps", dtype: str = "bf16", revision: str | None = None,
                 batch_size: int = 8, max_length: int | None = None):
        from transformers import AutoModelForCausalLM, AutoTokenizer

        if dtype not in _DTYPES:
            raise ValueError(f"dtype must be one of {sorted(_DTYPES)}")
        self.hf_id, self.revision = hf_id, revision
        self.device = pick_device(device)
        self.dtype_name = dtype
        self.torch_dtype = _DTYPES[dtype]
        self.batch_size = int(batch_size)

        self.tokenizer = AutoTokenizer.from_pretrained(hf_id, revision=revision)
        self.model = AutoModelForCausalLM.from_pretrained(hf_id, revision=revision, dtype=self.torch_dtype)
        self.model.to(self.device).eval()
        self.model.requires_grad_(False)

        cfg = self.model.config.get_text_config() if hasattr(self.model.config, "get_text_config") else self.model.config
        self.n_layers = int(cfg.num_hidden_layers)
        self.d_model = int(cfg.hidden_size)
        win = getattr(cfg, "max_position_embeddings", None) or getattr(cfg, "n_positions", None) or 2048
        self.max_length = int(min(win, max_length)) if max_length else int(min(win, 32768))

        self._base = self.model.base_model           # decoder stack incl. final norm
        self._head = self.model.get_output_embeddings()
        tok = self.tokenizer
        self.pad_id = tok.pad_token_id if tok.pad_token_id is not None else tok.eos_token_id
        if self.pad_id is None:
            self.pad_id = 0
        if tok.pad_token is None and tok.eos_token is not None:
            tok.pad_token = tok.eos_token

    # -- tokenisation ------------------------------------------------------------------------
    def _encode(self, text: str) -> list[int]:
        return self.tokenizer(text, add_special_tokens=False)["input_ids"]

    def _decode_each(self, ids: Sequence[int]) -> list[str]:
        return [self.tokenizer.decode([i]) for i in ids]

    # -- batched forward (right padding) -----------------------------------------------------
    def _forward(self, seqs: list[list[int]], hidden: bool):
        """Right-padded forward through the decoder. Returns (last_hidden [B,T,D], hidden_states|None, lengths)."""
        lens = [len(s) for s in seqs]
        T = max(lens)
        ids = torch.full((len(seqs), T), self.pad_id, dtype=torch.long)
        mask = torch.zeros((len(seqs), T), dtype=torch.long)
        for i, s in enumerate(seqs):
            ids[i, : len(s)] = torch.tensor(s, dtype=torch.long)
            mask[i, : len(s)] = 1
        ids, mask = ids.to(self.device), mask.to(self.device)
        with torch.inference_mode():
            out = self._base(input_ids=ids, attention_mask=mask, output_hidden_states=hidden, use_cache=False)
        return out.last_hidden_state, (out.hidden_states if hidden else None), lens

    def _logprobs_at(self, h: torch.Tensor, targets: torch.Tensor, rows: int = 1024) -> torch.Tensor:
        """Surprisal (nats, float32) of ``targets`` [N] given final hidden states ``h`` [N,D]; chunked over rows."""
        outs = []
        with torch.inference_mode():
            for s in range(0, h.shape[0], rows):
                logits = self._head(h[s : s + rows]).float()
                lp = torch.log_softmax(logits, dim=-1)
                outs.append(-lp.gather(1, targets[s : s + rows, None]).squeeze(1))
                del logits, lp
        return torch.cat(outs) if outs else torch.zeros(0, device=h.device)

    def _batched(self, n_items: int, lengths: Sequence[int], fn, batch_size: int | None):
        """Run ``fn(indices) -> list`` over length-sorted chunks; returns results in input order.

        On OOM the chunk size is halved and the chunk retried.
        """
        bs = int(batch_size or self.batch_size)
        order = sorted(range(n_items), key=lambda i: -lengths[i])
        results: list = [None] * n_items
        pos = 0
        while pos < n_items:
            idx = order[pos : pos + bs]
            try:
                res = fn(idx)
            except RuntimeError as e:  # includes torch.OutOfMemoryError
                if _is_oom(e) and bs > 1:
                    free_memory()
                    bs = max(1, bs // 2)
                    warnings.warn(f"OOM; retrying with batch_size={bs}")
                    continue
                raise
            for i, r in zip(idx, res):
                results[i] = r
            pos += len(idx)
            free_memory()
        return results


# ----------------------------------------------------------------------------------------------
# chat model
# ----------------------------------------------------------------------------------------------
class LocalLM(_Base):
    """A local chat model on MPS/CPU.

    Parameters
    ----------
    hf_id, revision : Hugging Face model id and commit hash.
    device : "mps" (default; falls back to CPU with a warning if unavailable), "cpu", or "auto".
    dtype : "fp16" (default; recommended on MPS), "bf16" or "fp32".
    batch_size : default chunk size for all batched methods (override per call).
    max_length : maximum total tokens per sequence (default: model window capped at 32768).
    """

    def __init__(self, hf_id: str, device: str | None = "mps", dtype: str = "fp16", revision: str | None = None,
                 batch_size: int = 8, max_length: int | None = None):
        super().__init__(hf_id, device=device, dtype=dtype, revision=revision, batch_size=batch_size,
                         max_length=max_length)
        if not getattr(self.tokenizer, "chat_template", None):
            raise ValueError(f"{hf_id} has no chat template; use PlainLM instead.")
        vocab = self.tokenizer.get_vocab()
        eos = {self.tokenizer.eos_token_id} if self.tokenizer.eos_token_id is not None else set()
        gc_eos = getattr(self.model.generation_config, "eos_token_id", None)
        if gc_eos is not None:
            eos |= set(gc_eos if isinstance(gc_eos, (list, tuple)) else [gc_eos])
        eos |= {vocab[t] for t in _EOT_TOKENS if t in vocab}
        self.eos_ids = sorted(eos)

    # -- prompt rendering --------------------------------------------------------------------
    def render(self, messages: list[dict], add_generation_prompt: bool = True) -> str:
        """Render a chat with the model's template; thinking mode is disabled."""
        return self.tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=add_generation_prompt, enable_thinking=False
        )

    def _prompt_ids(self, messages: list[dict]) -> list[int]:
        # The rendered template already contains any BOS / special tokens it needs.
        return self._encode(self.render(messages, add_generation_prompt=True))

    def _check_len(self, n: int) -> None:
        if n > self.max_length:
            raise ValueError(f"sequence of {n} tokens exceeds max_length={self.max_length}")

    # -- layers ------------------------------------------------------------------------------
    def resolve_layers(self, layers: str | int | Iterable[int] = "auto") -> list[int]:
        """``"auto"`` -> 4 evenly spaced layers from 25% depth to the final layer (hidden_states indices).

        Negative indices count from the end (-1 == n_layers).
        """
        if isinstance(layers, str):
            if layers != "auto":
                raise ValueError("layers must be 'auto' or a list of ints")
            out = np.unique(np.rint(np.linspace(0.25 * self.n_layers, self.n_layers, 4)).astype(int)).tolist()
            return [int(x) for x in out]
        if isinstance(layers, int):
            layers = [layers]
        res = []
        for L in layers:
            L = int(L)
            if L < 0:
                L = self.n_layers + 1 + L
            if not 0 <= L <= self.n_layers:
                raise ValueError(f"layer {L} out of range 0..{self.n_layers}")
            res.append(L)
        return res

    # -- 1. generation -----------------------------------------------------------------------
    def generate(self, batch_messages: list[list[dict]], max_new_tokens: int = 160, temperature: float = 0.0,
                 top_p: float = 1.0, seed: int = 0, top_k: int | None = None,
                 batch_size: int | None = None, min_new_tokens: int | None = None) -> list[str]:
        """Generate an assistant reply per chat. Greedy if ``temperature == 0``, else seeded sampling
        (``top_k=None`` disables top-k). Returns the stripped new text with any thinking block removed.

        Note: sampled outputs depend on the seed *and* on the chunk composition (batch_size).
        """
        from transformers import GenerationConfig

        prompts = [self.render(m, add_generation_prompt=True) for m in batch_messages]
        lens = [len(self._encode(p)) for p in prompts]
        for n in lens:
            self._check_len(n + max_new_tokens)
        do_sample = temperature > 0
        gcfg = GenerationConfig(
            max_new_tokens=max_new_tokens, min_new_tokens=min_new_tokens, do_sample=do_sample,
            temperature=float(temperature) if do_sample else None,
            top_p=float(top_p) if do_sample else None,
            top_k=(int(top_k) if top_k else 0) if do_sample else None,
            eos_token_id=self.eos_ids, pad_token_id=self.pad_id,
        )
        tok = self.tokenizer
        torch.manual_seed(seed)

        def run(idx):
            old = tok.padding_side
            tok.padding_side = "left"
            try:
                enc = tok([prompts[i] for i in idx], return_tensors="pt", padding=True, add_special_tokens=False)
            finally:
                tok.padding_side = old
            enc = {k: v.to(self.device) for k, v in enc.items()}
            with torch.inference_mode():
                out = self.model.generate(**enc, generation_config=gcfg)
            new = out[:, enc["input_ids"].shape[1]:].cpu()
            texts = tok.batch_decode(new, skip_special_tokens=True)
            del out, enc
            return [strip_thinking(t) for t in texts]

        return self._batched(len(prompts), lens, run, batch_size)

    # -- 2-4. teacher-forced scoring and activations -------------------------------------------
    def _prep(self, batch_messages, continuations):
        if len(batch_messages) != len(continuations):
            raise ValueError("batch_messages and continuations must have the same length")
        items = []
        for msgs, cont in zip(batch_messages, continuations):
            p = self._prompt_ids(msgs)
            c = self._encode(cont)
            self._check_len(len(p) + len(c))
            items.append((p, c))
        return items

    def _score_chunk(self, items, want_scores: bool, layers: list[int] | None):
        seqs = [p + c for p, c in items]
        last, hs, _ = self._forward(seqs, hidden=layers is not None)
        B = len(items)
        scores = [None] * B
        if want_scores:
            # position t predicts token t+1, so the first continuation token is predicted at len(p)-1
            bidx, pidx, tgt = [], [], []
            for b, (p, c) in enumerate(items):
                P, C = len(p), len(c)
                bidx += [b] * C
                pidx += list(range(P - 1, P + C - 1))
                tgt += c
            if tgt:
                bi = torch.tensor(bidx, device=self.device)
                pi = torch.tensor(pidx, device=self.device)
                s = self._logprobs_at(last[bi, pi], torch.tensor(tgt, device=self.device)).cpu().numpy()
            else:
                s = np.zeros(0, dtype=np.float32)
            off = 0
            for b, (p, c) in enumerate(items):
                sur = [float(x) for x in s[off : off + len(c)]]
                off += len(c)
                scores[b] = {"tokens": self._decode_each(c), "surprisal": sur, **_stats(sur)}
        acts = [None] * B
        if layers is not None:
            for b, (p, c) in enumerate(items):
                P, C = len(p), len(c)
                if C == 0:
                    nanv = np.full((len(layers), self.d_model), np.nan, dtype=np.float32)
                    acts[b] = (nanv, nanv)
                    continue
                stack = torch.stack([hs[L][b, P : P + C].float() for L in layers])  # [L, C, D]
                acts[b] = (stack.mean(1).cpu().numpy(), stack[:, -1].cpu().numpy())
        del last, hs
        return list(zip(scores, acts))

    def _score_impl(self, batch_messages, continuations, want_scores, layers, batch_size):
        items = self._prep(batch_messages, continuations)
        lens = [len(p) + len(c) for p, c in items]
        res = self._batched(len(items), lens, lambda idx: self._score_chunk([items[i] for i in idx], want_scores, layers),
                            batch_size)
        scores = [r[0] for r in res]
        acts = None
        if layers is not None:
            if res:
                mean = np.stack([r[1][0] for r in res]).astype(np.float16)
                last = np.stack([r[1][1] for r in res]).astype(np.float16)
            else:
                mean = last = np.zeros((0, len(layers), self.d_model), dtype=np.float16)
            acts = {"layers": list(layers), "mean": mean, "last": last,
                    "n_tokens": np.array([len(c) for _, c in items], dtype=np.int32)}
        return scores, acts

    def score_continuation(self, batch_messages: list[list[dict]], continuations: list[str],
                           batch_size: int | None = None) -> list[dict]:
        """Teacher-forced surprisal (nats) of each continuation as the assistant's answer.

        Each item: ``{"tokens", "surprisal", "mean", "max", "min", "sum", "n"}``. Only the continuation
        tokens are scored (the first one from the last prompt position); no template tokens and no
        end-of-turn token are counted. ``n == len(tokenizer(continuation, add_special_tokens=False))``.
        """
        return self._score_impl(batch_messages, continuations, True, None, batch_size)[0]

    def activations(self, batch_messages: list[list[dict]], continuations: list[str],
                    layers: str | Iterable[int] = "auto", batch_size: int | None = None) -> dict:
        """Residual-stream activations pooled over the continuation tokens.

        Returns ``{"layers": [...], "mean": f16[B, L, D], "last": f16[B, L, D], "n_tokens": i32[B]}``
        (``mean`` = mean over continuation positions, ``last`` = last continuation token; NaN if empty).
        """
        return self._score_impl(batch_messages, continuations, False, self.resolve_layers(layers), batch_size)[1]

    def score_and_activations(self, batch_messages: list[list[dict]], continuations: list[str],
                              layers: str | Iterable[int] = "auto",
                              batch_size: int | None = None) -> tuple[list[dict], dict]:
        """One forward pass returning ``(score_continuation(...), activations(...))``."""
        return self._score_impl(batch_messages, continuations, True, self.resolve_layers(layers), batch_size)

    # -- 5. yes/no probability -----------------------------------------------------------------
    def _variant_ids(self, variants: Sequence[str]) -> list[int]:
        ids = []
        for v in variants:
            t = self._encode(v)
            if t and t[0] not in ids:
                ids.append(t[0])
        return ids

    def p_yes(self, batch_messages: list[list[dict]], yes_variants=("Yes", "yes", " Yes"),
              no_variants=("No", "no", " No"), batch_size: int | None = None,
              return_mass: bool = False) -> list[float]:
        """Next-token P(yes)/(P(yes)+P(no)) right after the generation prompt (thinking disabled).

        Each variant contributes the probability of its FIRST token; duplicate token ids are counted once.
        With ``return_mass=True`` returns dicts ``{"p_yes", "mass_yes", "mass_no"}`` instead of floats
        (the raw masses tell you whether the model wanted to answer Yes/No at all).
        """
        yes_ids, no_ids = self._variant_ids(yes_variants), self._variant_ids(no_variants)
        if set(yes_ids) & set(no_ids):
            raise ValueError("yes and no variants share a first token")
        prompts = [self._prompt_ids(m) for m in batch_messages]
        for p in prompts:
            self._check_len(len(p))
        yi = torch.tensor(yes_ids, device=self.device)
        ni = torch.tensor(no_ids, device=self.device)

        def run(idx):
            seqs = [prompts[i] for i in idx]
            last, _, lens = self._forward(seqs, hidden=False)
            h = last[torch.arange(len(seqs), device=self.device), torch.tensor(lens, device=self.device) - 1]
            with torch.inference_mode():
                probs = torch.softmax(self._head(h).float(), dim=-1)
            py, pn = probs[:, yi].sum(1).cpu().numpy(), probs[:, ni].sum(1).cpu().numpy()
            del last, probs
            out = []
            for a, b in zip(py, pn):
                p = float(a / (a + b)) if (a + b) > 0 else float("nan")
                out.append({"p_yes": p, "mass_yes": float(a), "mass_no": float(b)} if return_mass else p)
            return out

        return self._batched(len(prompts), [len(p) for p in prompts], run, batch_size)


# ----------------------------------------------------------------------------------------------
# plain LM
# ----------------------------------------------------------------------------------------------
class PlainLM(_Base):
    """A raw causal LM for external-perplexity baselines (no chat template).

    The text is preceded by the tokenizer's BOS token (or EOS as a document separator if there is no
    BOS) so that its first token is scored. Defaults: fp32 on CPU for GPT-2-sized models is fine; use
    ``device="mps", dtype="bf16"`` for larger ones.
    """

    def __init__(self, hf_id: str, device: str | None = "auto", dtype: str = "fp32", revision: str | None = None,
                 batch_size: int = 16, max_length: int | None = 4096):
        super().__init__(hf_id, device=device, dtype=dtype, revision=revision, batch_size=batch_size,
                         max_length=max_length)
        tok = self.tokenizer
        self.prefix_id = tok.bos_token_id if tok.bos_token_id is not None else tok.eos_token_id

    def perplexity(self, texts: list[str], contexts: list[str | None] | None = None,
                   batch_size: int | None = None) -> list[dict]:
        """Token surprisal of each text, optionally conditioned on a raw-text context prefix.

        Context and text are tokenised separately and concatenated (include any separating space /
        newline yourself). Contexts are truncated from the LEFT to fit the window; a text longer than
        the window is truncated from the right (with a warning). Each item:
        ``{"tokens", "surprisal", "mean", "max", "min", "sum", "n", "ppl", "context_tokens"}``.
        """
        if contexts is not None and len(contexts) != len(texts):
            raise ValueError("contexts must align with texts")
        items = []
        pre = [self.prefix_id] if self.prefix_id is not None else []
        for i, t in enumerate(texts):
            tid = self._encode(t)
            budget = self.max_length - len(pre)
            if len(tid) > budget:
                warnings.warn(f"text {i} has {len(tid)} tokens; truncated to {budget}")
                tid = tid[:budget]
            ctx = self._encode(contexts[i]) if contexts is not None and contexts[i] else []
            room = budget - len(tid)
            ctx = ctx[max(0, len(ctx) - room):] if room > 0 else []
            items.append((pre + ctx, tid))

        def run(idx):
            chunk = [items[i] for i in idx]
            last, _, _ = self._forward([p + c for p, c in chunk], hidden=False)
            out = []
            for b, (p, c) in enumerate(chunk):
                P, C = len(p), len(c)
                if C == 0:
                    out.append({"tokens": [], "surprisal": [], **_stats([]), "ppl": float("nan"),
                                "context_tokens": P - len(pre)})
                    continue
                if P == 0:  # no prefix token available: first token cannot be scored
                    pos, tgt, toks = list(range(0, C - 1)), c[1:], c[1:]
                else:
                    pos, tgt, toks = list(range(P - 1, P + C - 1)), c, c
                s = self._logprobs_at(last[b, pos], torch.tensor(tgt, device=self.device)).cpu().numpy().tolist()
                st = _stats(s)
                out.append({"tokens": self._decode_each(toks), "surprisal": s, **st,
                            "ppl": float(math.exp(st["mean"])) if st["n"] else float("nan"),
                            "context_tokens": P - len(pre)})
            del last
            return out

        return self._batched(len(items), [len(p) + len(c) for p, c in items], run, batch_size)
