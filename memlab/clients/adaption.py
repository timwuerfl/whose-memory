"""Async client for the Adaption Labs hosted-model API (OpenAI-Responses-like).

Features
--------
* two-key round robin, per-key concurrency limit with an adaptive throttle (429 bursts halve the
  effective limit of that key, which then recovers slowly)
* exponential backoff with jitter on 429 / 5xx / timeouts / connection errors (honours Retry-After)
* on-disk SQLite response cache (WAL), keyed by sha256 of the request identity incl. ``sample_idx``
* aggregated spend ledger (``results/spend_ledger.csv``) and a hard budget guard

Keys are read from ``<project root>/.env`` (``ADAPTION_API_KEY_1``/``_2``) or the environment.
They are never logged; every error string that leaves this module is scrubbed.
"""
from __future__ import annotations

import asyncio
import atexit
import csv
import fcntl
import hashlib
import json
import os
import random
import re
import sqlite3
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

import httpx

PROJECT_ROOT = Path(__file__).resolve().parents[2]
BASE_URL = "https://api.prod.adaptionlabs.ai"
RESPONSES_PATH = "/api/v1/responses"
DEFAULT_CACHE_PATH = PROJECT_ROOT / "cache" / "llm" / "cache.sqlite"
DEFAULT_LEDGER_PATH = PROJECT_ROOT / "results" / "spend_ledger.csv"
LEDGER_COLUMNS = ["utc_minute", "key_slot", "model", "tag", "n_calls", "input_tokens",
                  "output_tokens", "reasoning_tokens", "cost"]

MODELS = ("deepseek-v4-flash", "qwen3.8-27b", "gemma-4-26b-a4b-it", "gemma-4-31b-it",
          "glm-5.3-flash", "qwen3.5-397b", "glm-5.2")

# Credits per 1M tokens (input, output); indicative list prices.
PRICES = {
    "deepseek-v4-flash": (0.044, 0.133),
    "qwen3.8-27b": (0.039, 1.25),
    "gemma-4-26b-a4b-it": (0.077, 0.255),
    "gemma-4-31b-it": (0.09, 0.34),
    "glm-5.3-flash": (0.15, 0.50),
    "qwen3.5-397b": (0.55, 3.50),
    "glm-5.2": (1.40, 4.40),
}

# Recommended per-model request settings, established by experiments/setup_probe.py on 13 Nov 2026
# (see SPECS.md and results/setup/probe.json).
#   extra                         merged into the request body; cheapest leak-free setting found.
#                                 {"reasoning": {"effort": "none"}} gives 0 reasoning tokens on 6/7 models.
#                                 On glm-5.3-flash "none" does NOT stop reasoning: it dumps the reasoning
#                                 into the output text. Use effort "low" there (reasoning stays separated).
#                                 Gemma models do not reason by default; "low"/"minimal" switch it ON.
#   max_output_tokens_floor       smallest budget for a short JSON answer with ``extra`` applied.
#   max_output_tokens_floor_reasoning  same, with reasoning left at the default (extra = {}).
#   reasoning_off_hurts           True where turning reasoning off cost accuracy on 3 small multi-step
#                                 questions (deepseek-v4-flash, qwen3.8-27b: 1/3 vs 3/3). Small n.
#   t0_deterministic              whether 5 samples at temperature 0 were identical.
_R_OFF = {"reasoning": {"effort": "none"}}
MODEL_DEFAULTS: dict[str, dict[str, Any]] = {
    "deepseek-v4-flash": {"extra": _R_OFF, "max_output_tokens_floor": 512,
                          "max_output_tokens_floor_reasoning": 1024, "reasoning_off_hurts": True,
                          "t0_deterministic": True},
    "qwen3.8-27b": {"extra": _R_OFF, "max_output_tokens_floor": 512,
                    "max_output_tokens_floor_reasoning": 1024, "reasoning_off_hurts": True,
                    "t0_deterministic": False},
    "gemma-4-26b-a4b-it": {"extra": _R_OFF, "max_output_tokens_floor": 512,
                           "max_output_tokens_floor_reasoning": 512, "reasoning_off_hurts": False,
                           "t0_deterministic": True},
    "gemma-4-31b-it": {"extra": _R_OFF, "max_output_tokens_floor": 512,
                       "max_output_tokens_floor_reasoning": 512, "reasoning_off_hurts": False,
                       "t0_deterministic": False},
    "glm-5.3-flash": {"extra": {"reasoning": {"effort": "low"}}, "max_output_tokens_floor": 1024,
                      "max_output_tokens_floor_reasoning": 1024, "reasoning_off_hurts": False,
                      "t0_deterministic": False},
    "qwen3.5-397b": {"extra": _R_OFF, "max_output_tokens_floor": 512,
                     "max_output_tokens_floor_reasoning": 4096, "reasoning_off_hurts": False,
                     "t0_deterministic": False},
    "glm-5.2": {"extra": _R_OFF, "max_output_tokens_floor": 512,
                "max_output_tokens_floor_reasoning": 2048, "reasoning_off_hurts": False,
                "t0_deterministic": True},
}
# Per-(key, model) in-flight caps enforced by the API (measured 13 Nov): qwen3.5-397b accepts only
# 3 concurrent requests per key (more are rejected instantly with 429). deepseek-v4-flash (12),
# glm-5.2 (5), qwen3.8-27b (6) and gemma-4-26b-a4b-it (6) showed no cap at the tested level;
# gemma-4-31b-it and glm-5.3-flash were not measured.
MODEL_INFLIGHT_CAP: dict[str, int] = {"qwen3.5-397b": 3}   # measured: the 4th in flight on a key gets a 429

# Requests in flight per key, summed over all models and processes. Found on 14 Nov (00:40-01:10): with
# reasoning on, calls last 30-100 s and pile up, and the provider then answers 429 for every model on
# that key although the request window is not full. Override with the env var MEMLAB_KEY_INFLIGHT.
KEY_INFLIGHT_CAP = 12

# Study setting: reasoning ON at the lowest effort that keeps reasoning out of the answer text
# (experiments/setup_probe.py --phases study,study2; SPECS.md "Study settings"). Effort "low" is
# accepted by all 7 models and keeps reasoning in the reasoning item on all 7 (gemma wraps its JSON
# in a ```json fence; use parse_json). No reasoning-budget field works, and on several models "low"
# is not short: qwen3.5-397b used ~9.4k reasoning tokens and gemma-4-26b ~5k on medium tasks.
REASONING_LOW_EXTRA: dict[str, dict] = {m: {"reasoning": {"effort": "low"}} for m in MODELS}
REASONING_LOW_MAX_OUTPUT_TOKENS = 16384   # 8192 was not enough for reasoning plus a JSON answer

# MAIN STUDY SETTING (from 14 Nov 01:25): extended reasoning OFF. With reasoning on, the provider's
# output-token throughput (roughly 60-100k tokens/min for the account, measured in the first hour of the
# main run) limited us to about 18 calls/min, i.e. ~55 hours for the study. Reasoning off means effort
# "none" everywhere except glm-5.3-flash, where "none" leaks reasoning into the answer and "low" yields
# ~0-60 reasoning tokens. Set MEMLAB_REASONING=low for the reasoning-on robustness arm.
if os.environ.get("MEMLAB_REASONING", "").lower() == "low":
    STUDY_EXTRA: dict[str, dict] = dict(REASONING_LOW_EXTRA)
    STUDY_MAX_OUTPUT_TOKENS = REASONING_LOW_MAX_OUTPUT_TOKENS
else:
    STUDY_EXTRA = {m: {"reasoning": {"effort": "low" if m == "glm-5.3-flash" else "none"}} for m in MODELS}
    STUDY_MAX_OUTPUT_TOKENS = 4096

MODEL_DEFAULTS = {m: {**v, "extra": json.loads(json.dumps(v["extra"]))} for m, v in MODEL_DEFAULTS.items()}
RECOMMENDED = MODEL_DEFAULTS  # alias


# Measured (SPECS.md): each key has a rolling 60 s request-count window, shared across all models:
# key 1 allows 50 requests/min, key 2 only 25. 429s carry Retry-After: 60 and do not themselves count
# against the window. No token-per-minute limit was hit (300k input tokens/min on key 1 was fine).
DEFAULT_RPM_PER_KEY: dict[int, float] = {1: 46.0, 2: 23.0}


class BudgetExceeded(RuntimeError):
    """Raised when total recorded spend has reached the configured cap."""


@dataclass
class Completion:
    text: str
    reasoning: str = ""
    usage: dict = field(default_factory=lambda: {"input_tokens": 0, "output_tokens": 0,
                                                 "reasoning_tokens": 0})
    cost: float = 0.0
    cached: bool = False
    model: str = ""
    status: str = ""
    error: Optional[str] = None
    latency_s: float = 0.0
    attempts: int = 0
    key_slot: int = 0
    rl_headers: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return asdict(self)


# ----------------------------------------------------------------------------------- keys

def load_keys(root: Path = PROJECT_ROOT) -> list[str]:
    """Return [key1, key2] (those present) from the environment or ``root/.env``."""
    vals: dict[str, str] = {}
    env_file = Path(root) / ".env"
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            k = k.strip().removeprefix("export ").strip()
            vals[k] = v.strip().strip('"').strip("'")
    keys = []
    for name in ("ADAPTION_API_KEY_1", "ADAPTION_API_KEY_2"):
        v = os.environ.get(name) or vals.get(name)
        if v:
            keys.append(v)
    return keys


_BEARER_RE = re.compile(r"(?i)bearer\s+[A-Za-z0-9._\-]+")


def scrub(s: Any, keys: list[str] = ()) -> str:
    s = str(s)
    for k in keys:
        if k:
            s = s.replace(k, "<KEY>")
    return _BEARER_RE.sub("Bearer <KEY>", s)


# ---------------------------------------------------------------------------------- cache

class ResponseCache:
    """SQLite cache; WAL + busy timeout makes concurrent processes safe (sqlite locks)."""

    def __init__(self, path: Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(self.path), timeout=60, check_same_thread=False,
                                    isolation_level=None)
        self.conn.execute("PRAGMA journal_mode=WAL")
        self.conn.execute("PRAGMA synchronous=NORMAL")
        self.conn.execute("PRAGMA busy_timeout=60000")
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS responses (key TEXT PRIMARY KEY, model TEXT, text TEXT,"
            " reasoning TEXT, usage TEXT, cost REAL, status TEXT, created REAL)")

    def get(self, key: str) -> Optional[dict]:
        row = self.conn.execute(
            "SELECT model, text, reasoning, usage, cost, status FROM responses WHERE key=?",
            (key,)).fetchone()
        if row is None:
            return None
        return {"model": row[0], "text": row[1], "reasoning": row[2], "usage": json.loads(row[3]),
                "cost": row[4], "status": row[5]}

    def put(self, key: str, c: Completion) -> None:
        for i in range(5):
            try:
                self.conn.execute(
                    "INSERT OR REPLACE INTO responses VALUES (?,?,?,?,?,?,?,?)",
                    (key, c.model, c.text, c.reasoning, json.dumps(c.usage), c.cost, c.status,
                     time.time()))
                return
            except sqlite3.OperationalError:  # locked by another process beyond busy timeout
                time.sleep(0.2 * (i + 1))

    def __len__(self) -> int:
        return self.conn.execute("SELECT COUNT(*) FROM responses").fetchone()[0]

    def close(self) -> None:
        try:
            self.conn.close()
        except Exception:
            pass


def cache_key(model: str, instructions: Optional[str], input: Any, max_output_tokens: int,
              temperature: float, sample_idx: int, extra: Optional[dict]) -> str:
    payload = json.dumps([model, instructions, input, int(max_output_tokens), float(temperature),
                          int(sample_idx), extra or {}], sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


# --------------------------------------------------------------------------------- ledger

class SpendLedger:
    """Aggregates per (UTC minute, key slot, model, tag); appends to CSV under an flock.

    Rows are append-only. A (minute, slot, model, tag) group can appear in more than one row
    if it straddles a flush or two processes write it; consumers should group-by and sum.
    """

    def __init__(self, path: Path, flush_every_s: float = 30.0):
        self.path = Path(path)
        self.flush_every_s = flush_every_s
        self.pending: dict[tuple, list] = {}
        self.last_flush = time.monotonic()
        self._base = self._read_total()

    def _read_total(self) -> float:
        return total_spend(self.path)

    @property
    def pending_cost(self) -> float:
        return sum(v[4] for v in self.pending.values())

    def total(self) -> float:
        return self._base + self.pending_cost

    def record(self, key_slot: int, model: str, tag: str, usage: dict, cost: float) -> None:
        minute = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M")
        k = (minute, key_slot, model, tag or "")
        v = self.pending.setdefault(k, [0, 0, 0, 0, 0.0])
        v[0] += 1
        v[1] += int(usage.get("input_tokens") or 0)
        v[2] += int(usage.get("output_tokens") or 0)
        v[3] += int(usage.get("reasoning_tokens") or 0)
        v[4] += float(cost or 0.0)
        if time.monotonic() - self.last_flush >= self.flush_every_s:
            self.flush()

    def flush(self) -> None:
        self.last_flush = time.monotonic()
        rows = self.pending
        self.pending = {}
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.path, "a+", newline="") as f:
            fcntl.flock(f, fcntl.LOCK_EX)
            try:
                f.seek(0, os.SEEK_END)
                w = csv.writer(f)
                if f.tell() == 0:
                    w.writerow(LEDGER_COLUMNS)
                for (minute, slot, model, tag), v in sorted(rows.items()):
                    w.writerow([minute, slot, model, tag, v[0], v[1], v[2], v[3], f"{v[4]:.8f}"])
                f.flush()
                os.fsync(f.fileno())
            finally:
                fcntl.flock(f, fcntl.LOCK_UN)
        # refresh the base from disk (picks up other processes' spend too)
        self._base = self._read_total()


def total_spend(ledger_path: Path = DEFAULT_LEDGER_PATH) -> float:
    """Sum of the ``cost`` column of the ledger CSV (0.0 if missing)."""
    p = Path(ledger_path)
    if not p.exists():
        return 0.0
    tot = 0.0
    with open(p, newline="") as f:
        for row in csv.DictReader(f):
            try:
                tot += float(row.get("cost") or 0.0)
            except ValueError:
                pass
    return tot


# ------------------------------------------------------------------------------- throttle

DEFAULT_RATE_STATE_DIR = PROJECT_ROOT / "cache" / "llm"


class SharedRateWindow:
    """Requests-per-window limiter shared by every process that uses the same API key.

    State lives in a small JSON file (one per key, named by a hash of the key) guarded by an
    ``fcntl.flock`` on the open file. The lock is held only for a read-modify-write of the file
    and the OS drops it if the holder dies, so a killed process cannot deadlock the others.
    Waiting is done outside the lock with ``asyncio.sleep`` until the oldest send leaves the window
    (no busy spin). State: ``starts`` (wall-clock send times inside the window), ``factor`` (current
    fraction of ``rpm`` allowed; lowered 20 % on a 429 burst), ``changed`` (time of last factor
    change) and ``r429`` (recent 429 times).

    A corrupted or truncated state file is treated as empty (fail-open by at most one window).
    """

    BURST_N, BURST_WINDOW_S, MIN_CUT_GAP_S = 3, 10.0, 5.0
    RECOVER_AFTER_S, RECOVER_STEP, MIN_FACTOR = 30.0, 0.1, 0.2

    def __init__(self, path: Path, rpm: float, window_s: float = 60.0,
                 clock=time.time, sleep=None):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.rpm = float(rpm)
        self.window_s = float(window_s)
        self.clock = clock
        self._sleep = sleep
        self.path.touch(exist_ok=True)

    # -- file helpers (call with the lock held) --
    def _read(self, f) -> dict:
        f.seek(0)
        raw = f.read()
        try:
            st = json.loads(raw) if raw.strip() else {}
        except Exception:
            st = {}
        if not isinstance(st, dict):
            st = {}
        st.setdefault("starts", [])
        st.setdefault("factor", 1.0)
        st.setdefault("changed", 0.0)
        st.setdefault("r429", [])
        return st

    def _write(self, f, st: dict) -> None:
        f.seek(0)
        f.truncate()
        f.write(json.dumps(st))
        f.flush()

    def _locked(self, fn, exclusive: bool = True):
        with open(self.path, "r+") as f:
            fcntl.flock(f, fcntl.LOCK_EX if exclusive else fcntl.LOCK_SH)
            try:
                return fn(f)
            finally:
                fcntl.flock(f, fcntl.LOCK_UN)

    def _normalise(self, st: dict, now: float) -> None:
        st["starts"] = [t for t in st["starts"] if now - t < self.window_s and t <= now + 1.0]
        st["r429"] = [t for t in st["r429"] if now - t < self.BURST_WINDOW_S]
        if st["factor"] < 1.0 and now - st["changed"] >= self.RECOVER_AFTER_S:
            st["factor"] = min(1.0, st["factor"] + self.RECOVER_STEP)
            st["changed"] = now

    def limit_of(self, st: dict) -> int:
        return max(1, int(self.rpm * st["factor"]))

    # -- public --
    def try_acquire(self) -> float:
        """Record a send and return 0.0 if the window has room; else return seconds to wait."""
        def fn(f):
            now = self.clock()
            st = self._read(f)
            self._normalise(st, now)
            if len(st["starts"]) < self.limit_of(st):
                st["starts"].append(now)
                self._write(f, st)
                return 0.0
            self._write(f, st)
            k = len(st["starts"]) - self.limit_of(st)  # sends that must expire first
            oldest = sorted(st["starts"])[k]
            return max(0.005, oldest + self.window_s - now)
        return self._locked(fn)

    async def acquire(self) -> None:
        sleep = self._sleep or asyncio.sleep
        while True:
            wait = self.try_acquire()
            if wait <= 0.0:
                return
            await sleep(wait + random.uniform(0.0, min(0.05, 0.05 * self.window_s)))

    def on_429(self) -> bool:
        """Record a 429; on a burst lower the shared factor by 20 %. Returns True if cut."""
        def fn(f):
            now = self.clock()
            st = self._read(f)
            self._normalise(st, now)
            st["r429"].append(now)
            cut = False
            if len(st["r429"]) >= self.BURST_N and now - st["changed"] > self.MIN_CUT_GAP_S:
                st["factor"] = max(self.MIN_FACTOR, st["factor"] * 0.8)
                st["changed"] = now
                st["r429"] = []
                cut = True
            self._write(f, st)
            return cut
        return self._locked(fn)

    def snapshot(self) -> dict:
        """{"used": sends in window, "limit": current limit, "factor": ...} (shared lock)."""
        def fn(f):
            now = self.clock()
            st = self._read(f)
            self._normalise(st, now)
            return {"used": len(st["starts"]), "limit": self.limit_of(st), "factor": st["factor"]}
        return self._locked(fn, exclusive=False)


class SharedInflightCap:
    """At most ``cap`` requests in flight for one (key, model), across processes.

    ``cap`` lock files; holding an exclusive ``flock`` on one of them is a ticket. Locks are per open
    file description, so this works between coroutines of one process too, and the OS releases a
    dead process's tickets. A full cap is re-polled every ~0.5-1 s (no busy spin).
    """

    def __init__(self, state_dir: Path, key: str, model: str, cap: int, poll_s: float = 0.5):
        h = hashlib.sha256(key.encode()).hexdigest()[:16]
        safe = re.sub(r"[^A-Za-z0-9_.-]", "_", model)
        self.paths = [Path(state_dir) / f"inflight_{h}_{safe}_{i}.lock" for i in range(int(cap))]
        Path(state_dir).mkdir(parents=True, exist_ok=True)
        self.poll_s = poll_s

    def try_acquire(self):
        for pth in self.paths:
            f = open(pth, "a+")
            try:
                fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
                return f
            except OSError:
                f.close()
        return None

    @staticmethod
    def release(f) -> None:
        if f is None:
            return
        try:
            fcntl.flock(f, fcntl.LOCK_UN)
        finally:
            f.close()


def rate_state_path(state_dir: Path, key: str) -> Path:
    return Path(state_dir) / f"ratelimit_{hashlib.sha256(key.encode()).hexdigest()[:16]}.json"


class _KeySlot:
    """Per-key gate: an in-process concurrency limit plus a cross-process requests-per-window
    limit (:class:`SharedRateWindow`). On a 429 burst (>=3 within 10 s) concurrency is halved and
    the shared RPM limit cut by 20 %; both recover slowly. ``rpm=None`` disables the RPM limiter.
    """

    def __init__(self, slot: int, key: str, limit: int, adaptive: bool = True,
                 rpm: Optional[float] = None, state_dir: Path = DEFAULT_RATE_STATE_DIR,
                 window_s: float = 60.0, clock=time.time):
        self.slot = slot
        self.key = key
        self.max_limit = limit
        self.limit = limit
        self.max_rpm = rpm
        self.adaptive = adaptive
        self.in_flight = 0
        self.recent_429: list[float] = []
        self.last_change = 0.0
        self.ok_since_change = 0
        self.n_429 = 0
        self.window_s = window_s
        self.window = SharedRateWindow(rate_state_path(state_dir, key), rpm, window_s, clock) if rpm else None
        self._cond: Optional[asyncio.Condition] = None

    @property
    def rpm(self) -> Optional[float]:
        if self.window is None:
            return None
        return float(self.window.snapshot()["limit"])

    def usage_frac(self) -> float:
        if self.window is None:
            return 0.0
        snap = self.window.snapshot()
        return snap["used"] / max(1, snap["limit"])

    def bind(self) -> None:
        self._cond = asyncio.Condition()

    async def acquire(self) -> None:
        async with self._cond:
            while self.in_flight >= self.limit:
                await self._cond.wait()
            self.in_flight += 1
        if self.window is not None:
            try:
                await self.window.acquire()
            except BaseException:
                await self.release()
                raise

    async def release(self) -> None:
        async with self._cond:
            self.in_flight -= 1
            self._cond.notify_all()

    def on_429(self) -> None:
        self.n_429 += 1
        if not self.adaptive:
            return
        if self.window is not None:
            self.window.on_429()
        now = time.monotonic()
        self.recent_429 = [t for t in self.recent_429 if now - t < 10.0] + [now]
        if len(self.recent_429) >= 3 and now - self.last_change > 5.0:
            self.limit = max(1, self.limit // 2)
            self.last_change = now
            self.ok_since_change = 0
            self.recent_429.clear()

    async def on_success(self) -> None:
        if not self.adaptive or self.limit >= self.max_limit:
            return
        self.ok_since_change += 1
        now = time.monotonic()
        if self.ok_since_change >= 2 * self.limit and now - self.last_change > 30.0:
            self.limit = min(self.max_limit, self.limit + max(1, self.max_limit // 8))
            self.last_change = now
            self.ok_since_change = 0
            if self._cond is not None:
                async with self._cond:
                    self._cond.notify_all()


# --------------------------------------------------------------------------------- client

def _parse_response(data: dict) -> tuple[str, str, dict, float, str, Any]:
    text_parts, reason_parts = [], []
    for item in data.get("output") or []:
        t = item.get("type")
        if t == "reasoning":
            for c in item.get("content") or []:
                if c.get("text"):
                    reason_parts.append(c["text"])
            for c in item.get("summary") or []:
                if isinstance(c, dict) and c.get("text"):
                    reason_parts.append(c["text"])
        elif t == "message":
            for c in item.get("content") or []:
                if c.get("type") in ("output_text", "text") and c.get("text"):
                    text_parts.append(c["text"])
    text = "".join(text_parts)
    if not text and data.get("output_text"):
        text = data["output_text"]
    u = data.get("usage") or {}
    usage = {
        "input_tokens": int(u.get("input_tokens") or 0),
        "output_tokens": int(u.get("output_tokens") or 0),
        "reasoning_tokens": int((u.get("output_tokens_details") or {}).get("reasoning_tokens") or 0),
    }
    cost = float(u.get("cost") or 0.0)
    return text.strip(), "\n".join(reason_parts).strip(), usage, cost, data.get("status") or "", \
        data.get("incomplete_details")


@dataclass
class _Resp:
    status_code: int
    headers: Any
    text: str
    data: Any


_RL_HEADER_RE = re.compile(r"(?i)rate|limit|retry-after|remaining|reset|quota")


class AdaptionClient:
    def __init__(self, *, per_key_concurrency: int = 48, rpm_per_key: float | dict[int, float] | None = DEFAULT_RPM_PER_KEY,
                 keys: Optional[list[str]] = None,
                 key_slots: Optional[list[int]] = None, base_url: str = BASE_URL,
                 cache_path: Path | str | None = DEFAULT_CACHE_PATH, use_cache: bool = True,
                 ledger_path: Path | str = DEFAULT_LEDGER_PATH, budget_cap: float = 1400.0,
                 timeout_s: float = 300.0, max_attempts: int = 8, retry_after_cap_s: float = 60.0, max_incomplete_retries: int = 2,
                 backoff_base_s: float = 1.0, backoff_max_s: float = 60.0, adaptive: bool = True,
                 ledger_flush_s: float = 30.0, transport: Optional[httpx.AsyncBaseTransport] = None,
                 rate_state_dir: Path | str = DEFAULT_RATE_STATE_DIR, rate_window_s: float = 60.0,
                 clock=time.time, stream: bool = True, retry_on_max_tokens: bool = False,
                 model_inflight_cap: Optional[dict[str, int]] = None):
        all_keys = keys if keys is not None else load_keys()
        if not all_keys:
            raise RuntimeError("no Adaption API keys found (ADAPTION_API_KEY_1/2)")
        slots = key_slots or list(range(1, len(all_keys) + 1))
        self._slots = [_KeySlot(s, all_keys[s - 1], per_key_concurrency, adaptive,
                                rpm_per_key.get(s) if isinstance(rpm_per_key, dict) else rpm_per_key,
                                Path(rate_state_dir), rate_window_s, clock) for s in slots]
        self._all_keys = list(all_keys)
        self.per_key_concurrency = per_key_concurrency
        self.base_url = base_url.rstrip("/")
        self.use_cache = use_cache
        self.cache = ResponseCache(Path(cache_path)) if (cache_path and use_cache) else None
        self.ledger = SpendLedger(Path(ledger_path), flush_every_s=ledger_flush_s)
        self.budget_cap = budget_cap
        self.timeout_s = timeout_s
        self.max_attempts = max_attempts
        self.retry_after_cap_s = retry_after_cap_s
        self.stream = stream
        self.rate_state_dir = Path(rate_state_dir)
        self.model_inflight_cap = dict(MODEL_INFLIGHT_CAP if model_inflight_cap is None else model_inflight_cap)
        self._caps: dict[tuple[int, str], SharedInflightCap] = {}
        self.retry_on_max_tokens = retry_on_max_tokens
        self.max_incomplete_retries = max_incomplete_retries
        self.backoff_base_s = backoff_base_s
        self.backoff_max_s = backoff_max_s
        self._transport = transport
        self._http: Optional[httpx.AsyncClient] = None
        self._loop = None
        self._rr = 0
        self.stats = {"calls": 0, "cache_hits": 0, "http_429": 0, "http_5xx": 0, "timeouts": 0,
                      "conn_errors": 0, "failures": 0}
        atexit.register(self._atexit_flush)

    # -- plumbing ---------------------------------------------------------------------
    @property
    def total_concurrency(self) -> int:
        return sum(s.max_limit for s in self._slots)

    @property
    def effective_limits(self) -> dict[int, dict]:
        return {s.slot: {"concurrency": s.limit, "rpm": s.rpm} for s in self._slots}

    def _ensure_loop(self) -> None:
        loop = asyncio.get_running_loop()
        if loop is not self._loop:
            self._loop = loop
            for s in self._slots:
                s.bind()
                s.in_flight = 0
            limits = httpx.Limits(max_connections=self.total_concurrency + 8,
                                  max_keepalive_connections=self.total_concurrency + 8)
            self._http = httpx.AsyncClient(base_url=self.base_url, timeout=self.timeout_s,
                                           limits=limits, transport=self._transport)

    def _next_slot(self) -> _KeySlot:
        """Least-loaded key (free concurrency first, then lowest shared rate-window usage); RR tiebreak."""
        n = len(self._slots)

        def score(i):
            s = self._slots[(self._rr + i) % n]
            return (s.in_flight >= s.limit, round(s.usage_frac(), 3), s.in_flight / s.limit, i)

        best = min(range(n), key=score)
        s = self._slots[(self._rr + best) % n]
        self._rr = (self._rr + 1) % n
        return s

    async def _acquire_slot(self, model: str):
        """Pick a key and, for models with an in-flight cap, take a cross-process ticket on it."""
        cap, pool = self.model_inflight_cap.get(model), model
        if not cap:
            # every other model draws from one shared per-key pool
            cap, pool = int(os.environ.get("MEMLAB_KEY_INFLIGHT", KEY_INFLIGHT_CAP) or 0), "__all__"
        if not cap:
            return self._next_slot(), None
        while True:
            first = self._next_slot()
            order = [first] + [s for s in self._slots if s is not first]
            for s in order:
                c = self._caps.get((s.slot, pool))
                if c is None:
                    c = self._caps[(s.slot, pool)] = SharedInflightCap(self.rate_state_dir, s.key, pool, cap)
                t = c.try_acquire()
                if t is not None:
                    return s, t
            await asyncio.sleep(0.5 + 0.5 * random.random())

    def _scrub(self, s: Any) -> str:
        return scrub(s, self._all_keys)

    def total_spend(self) -> float:
        """Recorded spend: ledger CSV on disk plus this process's unflushed spend."""
        return self.ledger.total()

    def flush_ledger(self) -> None:
        self.ledger.flush()

    def _atexit_flush(self) -> None:
        try:
            if self.ledger.pending:
                self.ledger.flush()
        except Exception:
            pass

    async def close(self) -> None:
        self.ledger.flush()
        if self._http is not None:
            try:
                await self._http.aclose()
            except Exception:
                pass
            self._http = None
            self._loop = None

    async def __aenter__(self):
        return self

    async def __aexit__(self, *exc):
        await self.close()

    async def _send(self, slot: "_KeySlot", body: dict) -> "_Resp":
        """POST one request; with ``self.stream`` read the SSE stream and return the final
        ``response`` object as ``data`` (avoids the gateway's ~60 s timeout on long generations)."""
        headers = {"Authorization": f"Bearer {slot.key}", "Content-Type": "application/json"}
        if not self.stream:
            r = await self._http.post(RESPONSES_PATH, json=body, headers=headers)
            try:
                data = r.json()
            except Exception:
                data = None
            return _Resp(r.status_code, r.headers, r.text, data)
        async with self._http.stream("POST", RESPONSES_PATH, json={**body, "stream": True},
                                     headers=headers) as r:
            if r.status_code != 200:
                raw = (await r.aread()).decode("utf-8", "replace")
                return _Resp(r.status_code, r.headers, raw, None)
            final, err = None, None
            async for line in r.aiter_lines():
                if not line.startswith("data:"):
                    continue
                payload = line[5:].strip()
                if not payload or payload == "[DONE]":
                    continue
                try:
                    ev = json.loads(payload)
                except Exception:
                    continue
                et = ev.get("type", "")
                if et in ("response.completed", "response.incomplete", "response.failed"):
                    final = ev.get("response")
                elif et == "error":
                    err = ev
            if isinstance(final, dict):
                return _Resp(200, r.headers, "", final)
            return _Resp(200, r.headers, json.dumps(err)[:300] if err else "stream ended without final response", None)

    # -- main API ---------------------------------------------------------------------
    async def complete(self, model: str, input: Any, instructions: Optional[str] = None, *,
                       max_output_tokens: int = 1024, temperature: float = 0.0,
                       sample_idx: int = 0, tag: str = "", extra: Optional[dict] = None,
                       use_cache: Optional[bool] = None) -> Completion:
        """One completion. Never raises for API failures (sets ``error``); raises
        ``BudgetExceeded`` before an uncached call once spend >= ``budget_cap``."""
        self._ensure_loop()
        self.stats["calls"] += 1
        do_cache = self.cache is not None and (use_cache if use_cache is not None else True)
        key = cache_key(model, instructions, input, max_output_tokens, temperature, sample_idx, extra)
        if do_cache:
            hit = self.cache.get(key)
            if hit is not None:
                self.stats["cache_hits"] += 1
                return Completion(text=hit["text"], reasoning=hit["reasoning"], usage=hit["usage"],
                                  cost=hit["cost"], cached=True, model=hit["model"] or model,
                                  status=hit["status"] or "completed")
        if self.total_spend() >= self.budget_cap:
            raise BudgetExceeded(f"spend {self.total_spend():.2f} >= cap {self.budget_cap:.2f}")

        body: dict[str, Any] = {"model": model, "input": input,
                                "max_output_tokens": int(max_output_tokens),
                                "temperature": float(temperature)}
        if instructions is not None:
            body["instructions"] = instructions
        if extra:
            body.update(extra)

        t0 = time.monotonic()
        attempts = 0
        incomplete_tries = 0
        last_err = "unknown error"
        last: Optional[Completion] = None
        rl_headers: dict = {}
        while attempts < self.max_attempts:
            attempts += 1
            slot, ticket = await self._acquire_slot(model)
            try:
                await slot.acquire()
            except BaseException:
                SharedInflightCap.release(ticket)
                raise
            retry_after: Optional[float] = None
            try:
                try:
                    r = await self._send(slot, body)
                except httpx.TimeoutException as e:
                    self.stats["timeouts"] += 1
                    last_err = f"timeout: {type(e).__name__}"
                    r = None
                except (httpx.TransportError, OSError) as e:
                    self.stats["conn_errors"] += 1
                    last_err = self._scrub(f"connection error: {type(e).__name__}: {e}")[:300]
                    r = None
            finally:
                await slot.release()
                SharedInflightCap.release(ticket)

            if r is not None:
                rl_headers = {k: v for k, v in r.headers.items() if _RL_HEADER_RE.search(k)}
                ra = r.headers.get("retry-after")
                if ra:
                    try:
                        retry_after = float(ra)
                    except ValueError:
                        retry_after = None
                if r.status_code == 429:
                    self.stats["http_429"] += 1
                    slot.on_429()
                    try:  # diagnostic trail: which model / key draws 429s (no secrets)
                        with open(self.rate_state_dir / "http429.log", "a") as _f:
                            _f.write(f"{time.time():.1f}\t{model}\t{slot.slot}\t{tag}\n")
                    except Exception:
                        pass
                    last_err = "http 429: " + self._scrub(r.text)[:200]
                elif r.status_code >= 500:
                    self.stats["http_5xx"] += 1
                    last_err = f"http {r.status_code}: " + self._scrub(r.text)[:200]
                elif r.status_code >= 400:
                    # non-retryable client error (bad param, auth, unknown model ...)
                    self.stats["failures"] += 1
                    return Completion(text="", model=model, status=f"http_{r.status_code}",
                                      error=f"http {r.status_code}: " + self._scrub(r.text)[:500],
                                      latency_s=time.monotonic() - t0, attempts=attempts,
                                      key_slot=slot.slot, rl_headers=rl_headers)
                else:
                    data = r.data
                    if not isinstance(data, dict):
                        last_err = "bad json body: " + self._scrub(r.text)[:200]
                    else:
                        text, reasoning, usage, cost, status, inc = _parse_response(data)
                        # every 200 response is billed -> ledger
                        self.ledger.record(slot.slot, model, tag, usage, cost)
                        await slot.on_success()
                        api_err = data.get("error")
                        c = Completion(text=text, reasoning=reasoning, usage=usage, cost=cost,
                                       cached=False, model=data.get("model") or model,
                                       status=status, latency_s=time.monotonic() - t0,
                                       attempts=attempts, key_slot=slot.slot, rl_headers=rl_headers)
                        if status == "completed" and not api_err:
                            if do_cache:
                                self.cache.put(key, c)
                            return c
                        if text:  # incomplete but usable (e.g. hit max_output_tokens after text)
                            c.error = None
                            return c
                        detail = inc or api_err or status
                        c.error = self._scrub(f"incomplete: {json.dumps(detail)[:300]}")
                        last = c
                        incomplete_tries += 1
                        hit_cap = isinstance(inc, dict) and inc.get("reason") == "max_output_tokens"
                        if incomplete_tries > self.max_incomplete_retries or (
                                hit_cap and not self.retry_on_max_tokens):
                            c.latency_s = time.monotonic() - t0
                            self.stats["failures"] += 1
                            return c
                        continue  # immediate retry, no backoff

            if attempts >= self.max_attempts:
                break
            delay = min(self.backoff_max_s, self.backoff_base_s * (2 ** (attempts - 1)))
            delay = delay * (0.5 + random.random())  # jitter
            if retry_after is not None:
                delay = max(delay, min(retry_after, self.retry_after_cap_s) * (0.8 + 0.4 * random.random()))
            await asyncio.sleep(delay)

        self.stats["failures"] += 1
        if last is not None:
            last.latency_s = time.monotonic() - t0
            last.attempts = attempts
            return last
        return Completion(text="", model=model, status="failed", error=last_err,
                          latency_s=time.monotonic() - t0, attempts=attempts,
                          rl_headers=rl_headers)

    def complete_sync(self, *args, **kwargs) -> Completion:
        """Blocking convenience wrapper (not for use inside a running event loop)."""
        async def _go():
            try:
                return await self.complete(*args, **kwargs)
            finally:
                if self._http is not None:
                    await self._http.aclose()
                    self._http = None
                    self._loop = None
        return asyncio.run(_go())
