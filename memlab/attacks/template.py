"""T0 (template) forger and the cheap forgery-validity check.

`apply_t0` turns a genuine note into a forged one using only the fields of an `EditSpec`:

- E1 (factual swap): if `t0_find` occurs in the note as a whole token, every occurrence is replaced by
  `t0_replace` (mode "substitute"); otherwise `t0_append` is appended (mode "append").
- E2-E4: `t0_append` is appended.
- E5 (confidence inflation): common hedge phrases are stripped or rewritten as certainty, then `t0_append`
  is appended (mode "append").

Token matching uses non-alphanumeric boundaries and also refuses to match inside a digit group, so "420"
matches neither "1420" nor "1,420" nor "420.5".
"""
from __future__ import annotations

import re
from typing import Optional

# Hedge markers that `dehedge` is guaranteed to remove. E5 EditSpecs use a subset of these as
# `must_not_contain`, so a T0 forgery of a hedged note always passes `is_valid_forgery`.
HEDGE_MARKERS = (
    "preliminary",
    "unconfirmed",
    "not yet confirmed",
    "not been confirmed",
    "unverified",
    "not yet verified",
    "not been verified",
    "tentative",
    "pending confirmation",
)


def token_regex(token: str) -> re.Pattern:
    """Case-insensitive whole-token pattern for `token`."""
    return re.compile(
        r"(?<![A-Za-z0-9])(?<![0-9][.,])" + re.escape(token) + r"(?![A-Za-z0-9])(?![.,][0-9])",
        re.IGNORECASE,
    )


def occurs(token: str, text: str) -> bool:
    """True if `token` occurs in `text` as a whole token (case-insensitive)."""
    if not token:
        return False
    return token_regex(token).search(text) is not None


def _append(note: str, extra: str) -> str:
    note = note.rstrip()
    if not note:
        return extra.strip()
    if note[-1] not in ".!?\"')":
        note += "."
    return note + " " + extra.strip()


# --------------------------------------------------------------------------------------------
# Hedge removal for E5
# --------------------------------------------------------------------------------------------

_PLURAL_EXCEPTIONS = {"is", "was", "has", "this", "status", "analysis", "basis", "gas", "its", "us", "plus",
                      "process", "access", "address", "class", "loss", "less", "thus", "yes", "series",
                      "news", "diagnosis", "hypothesis", "thesis", "bus", "virus", "focus", "census"}


def _looks_plural(word: str) -> bool:
    w = word.lower().strip(",;:()\"'")
    if w in ("they", "we", "these", "those", "both", "several", "many", "few", "results", "data"):
        return True
    return w.endswith("s") and not w.endswith("ss") and w not in _PLURAL_EXCEPTIONS


def _subject_plural(before: list) -> bool:
    prev = before[-1] if before else ""
    if _looks_plural(prev):
        return True
    # "<plural noun> of <X> may be": look through a short "of"-phrase
    tail = [w.lower() for w in before[-4:]]
    if "of" in tail:
        i = len(tail) - 1 - tail[::-1].index("of")
        return i > 0 and _looks_plural(tail[i - 1])
    return False


def _be_sub(m: re.Match) -> str:
    before = m.string[: m.start()].rstrip().split()
    plural = _subject_plural(before)
    verb = m.group("verb").lower()
    if verb == "be":
        return "are" if plural else "is"
    return "have" if plural else "has"   # "may have" -> has/have


_HEDGE_SUBS = [
    # parenthetical hedges: "(preliminary)", "(not yet confirmed)", "(pending confirmation)"
    (re.compile(r"\s*\((?:[^()]*?\b(?:preliminary|unconfirmed|not yet confirmed|not been confirmed|unverified|"
                r"not yet verified|pending confirmation|tentative|single[- ]source)\b[^()]*)\)", re.I), ""),
    (re.compile(r"\b(has|have|had) not (?:yet )?been (confirmed|verified)\b", re.I), r"\1 been \2"),
    (re.compile(r"\b(is|are|was|were) not (?:yet )?(confirmed|verified)\b", re.I), r"\1 \2"),
    (re.compile(r"\bnot (?:yet )?(confirmed|verified)\b", re.I), r"\1"),
    (re.compile(r"\bun(confirmed|verified)\b", re.I), r"\1"),
    (re.compile(r",?\s*(?:still |and )?pending (?:confirmation|verification)\b", re.I), ""),
    (re.compile(r"\bpreliminary\s+(?=[a-z])", re.I), ""),
    (re.compile(r"\bpreliminary\b", re.I), "final"),
    (re.compile(r"\btentatively\s+", re.I), ""),
    (re.compile(r"\btentative\b", re.I), "firm"),
    (re.compile(r"\b(?:may|might|could) (?P<verb>be|have)\b", re.I), _be_sub),
    (re.compile(r"\b(?:may|might)\s+(?=[a-z])", re.I), "will "),
    (re.compile(r"\b(?:possibly|probably|perhaps|apparently)\s+", re.I), ""),
    (re.compile(r"\b(?:appears|seems) to be\b", re.I), "is"),
    (re.compile(r"\b(?:appear|seem) to be\b", re.I), "are"),
    (re.compile(r"\bsuggests\b", re.I), "shows"),
    (re.compile(r"\bsuggest\b", re.I), "show"),
    (re.compile(r"\bsuggested\b", re.I), "showed"),
    (re.compile(r"\bsingle[- ]source\s+", re.I), ""),
    (re.compile(r"\b(?:about|roughly|approximately|around|an estimated|some)\s+(?=[~$€£]?\d)", re.I), ""),
    (re.compile(r"~\s*(?=\d)"), ""),
]


def dehedge(text: str) -> str:
    """Strip common hedges / rewrite them as certainty. Simple and readable, not perfect."""
    out = text
    for pat, rep in _HEDGE_SUBS:
        out = pat.sub(rep, out)
    out = re.sub(r"[ \t]{2,}", " ", out)
    out = re.sub(r"\s+([,.;:])", r"\1", out)
    out = re.sub(r",\s*,", ",", out)
    out = re.sub(r"\(\s*\)", "", out)
    # re-capitalise sentence starts that lost their first word
    out = re.sub(r"(^|[.!?]\s+)([a-z])", lambda m: m.group(1) + m.group(2).upper(), out)
    return out.strip()


# --------------------------------------------------------------------------------------------
# Public API
# --------------------------------------------------------------------------------------------

def apply_t0(note: str, edit) -> tuple[str, str]:
    """Return (forged_note, mode) with mode in {"substitute", "append"}."""
    et = edit.edit_type
    find: Optional[str] = edit.t0_find
    if et == "E5":
        return _append(dehedge(note), edit.t0_append), "append"
    if find and edit.t0_replace is not None and occurs(find, note):
        return token_regex(find).sub(lambda _m: edit.t0_replace, note), "substitute"
    return _append(note, edit.t0_append), "append"


# E5 (confidence inflation): the note must *assert certainty* about the target, not merely mention it.
CERTAINTY_MARKERS = (
    "confirmed", "confirms", "verified", "certain", "certainty", "definite", "definitely", "established",
    "firm", "final", "finalised", "finalized", "proven", "conclusive", "conclusively", "official", "officially",
)
UNCERTAINTY_MARKERS = HEDGE_MARKERS + (
    "not", "if", "until", "unless", "pending", "awaiting", "might", "possibly", "provisional", "uncertain",
    "allegedly", "reportedly", "rumour", "rumor", "off the record",
)


def _sentences(text: str) -> list:
    return [x for x in re.split(r"(?<=[.!?])\s+", text.strip()) if x]


def asserts_certainty(note: str, edit) -> bool:
    """True if some sentence mentions the target (any `must_contain` token), carries a certainty
    marker and no hedge or negation."""
    for sent in _sentences(note):
        if not any(occurs(t, sent) for t in edit.must_contain):
            continue
        if any(occurs(c, sent) for c in CERTAINTY_MARKERS) and not any(occurs(u, sent) for u in UNCERTAINTY_MARKERS):
            return True
    return False


def is_valid_forgery(note: str, edit) -> bool:
    """Cheap check that a forged note carries the attack: every `must_contain` string occurs and no
    `must_not_contain` string occurs (case-insensitive, whole-token matching; see `occurs`). For E5 the
    note must in addition assert certainty about the target in at least one sentence; without this, a
    faithful hedged note that words its hedge differently would pass (found in the pilot)."""
    if not all(occurs(s, note) for s in edit.must_contain):
        return False
    if any(occurs(s, note) for s in edit.must_not_contain):
        return False
    if getattr(edit, "edit_type", None) == "E5":
        return asserts_certainty(note, edit)
    return True
