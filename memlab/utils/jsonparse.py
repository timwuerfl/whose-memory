"""Robust extraction of a JSON object from LLM output, plus small field validators."""
from __future__ import annotations

import json
import re
from typing import Any, Iterable, Optional

_FENCE_RE = re.compile(r"```(?:json|JSON|javascript|js)?\s*\n?(.*?)```", re.S)
_THINK_RE = re.compile(r"<(think|thinking|reasoning)>.*?</\1>", re.S | re.I)
_TRAILING_COMMA_RE = re.compile(r",(\s*[}\]])")
_SMART = str.maketrans({"“": '"', "”": '"', "‘": "'", "’": "'"})


def _loads(s: str) -> Any:
    try:
        return json.loads(s)
    except Exception:
        pass
    fixed = _TRAILING_COMMA_RE.sub(r"\1", s)
    try:
        return json.loads(fixed)
    except Exception:
        pass
    fixed2 = fixed.translate(_SMART)
    try:
        return json.loads(fixed2)
    except Exception:
        return None


def _balanced_objects(s: str) -> Iterable[str]:
    """Yield each balanced {...} substring, in order of its opening brace (string-aware)."""
    n = len(s)
    i = 0
    while i < n:
        start = s.find("{", i)
        if start < 0:
            return
        depth = 0
        in_str = False
        esc = False
        end = -1
        for j in range(start, n):
            ch = s[j]
            if in_str:
                if esc:
                    esc = False
                elif ch == "\\":
                    esc = True
                elif ch == '"':
                    in_str = False
                continue
            if ch == '"':
                in_str = True
            elif ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    end = j
                    break
        if end < 0:
            return
        yield s[start:end + 1]
        i = start + 1


def parse_json(text: Optional[str]) -> Optional[dict]:
    """Return the first JSON object (dict) found in ``text``, or None.

    Handles code fences, prose before/after, leaked ``<think>`` blocks (or a dangling
    ``</think>``), single trailing commas, and smart quotes.
    """
    if not text or not isinstance(text, str):
        return None
    s = _THINK_RE.sub("", text)
    if "</think>" in s.lower():
        s = s[s.lower().rfind("</think>") + len("</think>"):]
    s = s.strip()
    # whole string
    v = _loads(s)
    if isinstance(v, dict):
        return v
    # fenced blocks
    for block in _FENCE_RE.findall(s):
        v = _loads(block.strip())
        if isinstance(v, dict):
            return v
        for cand in _balanced_objects(block):
            v = _loads(cand)
            if isinstance(v, dict):
                return v
    # first balanced object anywhere (outermost first)
    for cand in _balanced_objects(s):
        v = _loads(cand)
        if isinstance(v, dict):
            return v
    return None


_NUM_RE = re.compile(r"^\s*([-+]?\d+(?:\.\d+)?)\s*%?\s*$")


def get_float(d: Optional[dict], key: str, lo: float = float("-inf"),
              hi: float = float("inf")) -> Optional[float]:
    """Numeric field (accepts "85", "85%", "0.7"); None if missing, unparseable or out of range."""
    if not isinstance(d, dict) or key not in d:
        return None
    v = d[key]
    if isinstance(v, bool) or v is None:
        return None
    if isinstance(v, (int, float)):
        x = float(v)
    elif isinstance(v, str):
        m = _NUM_RE.match(v)
        if not m:
            return None
        x = float(m.group(1))
    else:
        return None
    if x != x or not (lo <= x <= hi):
        return None
    return x


def get_int(d: Optional[dict], key: str, lo: int = -(10 ** 18), hi: int = 10 ** 18) -> Optional[int]:
    """Integer field in [lo, hi]; accepts "85", "85%", 85.0. Non-integral values -> None."""
    x = get_float(d, key)
    if x is None or x != int(x):
        return None
    x = int(x)
    return x if lo <= x <= hi else None


def _norm_choice(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"^(option|answer|choice)\s*[:\-]?\s*", "", s)
    return re.sub(r"^[\s\(\[\{\"'*]+|[\s\)\]\}\"'*.,:;!?]+$", "", s)


def get_choice(d: Optional[dict], key: str, allowed: Iterable[str]) -> Optional[str]:
    """Case-insensitive choice; strips "(A)", "A)", "A.", "Option A". Returns the canonical
    member of ``allowed`` or None."""
    if not isinstance(d, dict) or key not in d or d[key] is None:
        return None
    v = d[key]
    if isinstance(v, bool):
        v = str(v).lower()
    v = str(v)
    canon = {_norm_choice(str(a)): a for a in allowed}
    n = _norm_choice(v)
    if n in canon:
        return canon[n]
    # leading token, e.g. "A) Paris" or "B - because ..."
    m = re.match(r"^[\s\(\[\"'*]*([A-Za-z0-9_\-]+)[\)\].:\s]", v + " ")
    if m and m.group(1).lower() in canon:
        return canon[m.group(1).lower()]
    return None
