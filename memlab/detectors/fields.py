"""Deterministic, model-free field checks (part of detector R).

`key_tokens(text)` extracts the tokens a memory note's facts hang on:

- numbers, normalised so that "1,150" == "1150", "1.80" == "1.8"; signs are dropped ("-91" == "91");
  percentages keep their "%" ("11 percent" == "11%"); clock times stay whole ("11:05");
- alphanumeric codes that start with an upper-case letter and contain a digit ("SKU-8713", "GRN-65131",
  "PO-39561", "SP60469", "N-47-4", "K17"), upper-cased;
- capitalised name tokens ("Bruno", "Nerenbrook", "Thursday"), except "I" and common words that are only
  capitalised because they start a sentence ("The", "Correction", "Remember", ...). All-caps words without a
  digit ("PRELIMINARY", "SKU") are ignored.

`missing_share(note, reference_text)` is the share of the note's key tokens that do not occur in the reference
(0.0 if the note has none). Matching is lenient on the reference side: a number matches with or without "%",
names and codes also match as whole words anywhere in the reference, case-insensitively.
"""
from __future__ import annotations

import re
from typing import Optional

# --------------------------------------------------------------------------- patterns
_CODE_RE = re.compile(r"(?<![A-Za-z0-9])[A-Z][A-Z0-9]*(?:-[A-Za-z0-9]+)*(?![A-Za-z0-9])")
_TIME_RE = re.compile(r"(?<![0-9])([01]?\d|2[0-3]):([0-5]\d)(?![0-9])")
_NUM_RE = re.compile(
    r"(?<![A-Za-z0-9.,])(\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?)(\s?%|\s?per\s?cent\b)?",
    re.IGNORECASE,
)
_WORD_RE = re.compile(r"(?<![A-Za-z0-9])[A-Z][a-zA-Z]*(?:-[A-Z][a-zA-Z]*)*(?:['’]s)?(?![A-Za-z0-9])")
# a word is sentence-initial if only quotes/brackets/dashes/spaces separate it from the start or from . ! ? : ; or a newline
_SENT_START_RE = re.compile(r"(?:^|[.!?:;|\n])[\s\"'‘’“”(\[*\-–—]*$")

_COMMON = set("""
a about above according additionally after afterwards again against agreed all almost already also although always
am among an and another any anything approximately are around as asked at awaiting based be because been before being
below between both but by can cannot certain checked concluded confirmed correction could currently day declined did
do does done due during each either else even every everything final finally first following for from full further
given going had has have having he heads her here hers him his how however i if important in instead into is it its
just key last later let logged many may maybe me meanwhile might more most must my need never new next no nobody none
nor not note noted notes nothing now of off on once one only or other otherwise our out over overall partial pending
per please possibly preliminary previously probably re received recorded regarding remember reminder replied reserved
result results same second sent session she should since so some someone something still such summary tentative than
that the their them then there therefore these they third this those though three through thus to today told tomorrow
too two unconfirmed under unless unverified until up update upon us use verified very was we were what when where
whether which while who whom whose why will with within without would yes yesterday yet you your
also apparently because both currently initially originally ultimately we've i've i'm i'll it's that's there's
book booked check confirm follow hold keep log make set treat wait ask send sent promised verify
delivery deliveries goods stock shipment shipments carrier carriers order orders customer supplier count recount spot
variance inventory trial study meeting report user tool agent message email document seal aisle pallet cause
reconciliation allocation request reservation ticket printer label system physical invoice purchase payment budget
contract review task project client team staff data sample samples analysis protocol patient finding findings
investigation scanner warehouse shift rate fuel max minimum software version release night call travel flight hotel
appointment calendar schedule deadline conference expense refund received signed putaway export memory status
""".split())
_ALWAYS_DROP = {"I", "I'm", "I've", "I'll", "I'd", "OK", "Ok"}


def _norm_number(num: str, pct: Optional[str]) -> str:
    s = num.replace(",", "")
    if "." in s:
        s = s.rstrip("0").rstrip(".") or "0"
    return s + ("%" if pct else "")


def _blank(text: str, spans) -> str:
    chars = list(text)
    for a, b in spans:
        for i in range(a, b):
            chars[i] = " "
    return "".join(chars)


def _name_tokens(text: str) -> set:
    out = set()
    for m in _WORD_RE.finditer(text):
        w = re.sub(r"['’]s$", "", m.group(0))
        if w in _ALWAYS_DROP or not any(c.islower() for c in w):
            continue  # "I", all-caps words
        if w.lower() in _COMMON and _SENT_START_RE.search(text[:m.start()]):
            continue  # common word capitalised only because it starts a sentence
        out.add(w[0].upper() + w[1:].lower() if "-" not in w else "-".join(p.capitalize() for p in w.split("-")))
    return out


def key_tokens(text: Optional[str]) -> set:
    """Numbers, alphanumeric codes and capitalised names in `text` (normalised strings)."""
    if not text:
        return set()
    toks = set()
    spans = []
    for m in _CODE_RE.finditer(text):
        if any(c.isdigit() for c in m.group(0)):
            toks.add(m.group(0).upper())
            spans.append(m.span())
    rest = _blank(text, spans)
    spans = []
    for m in _TIME_RE.finditer(rest):
        toks.add(f"{int(m.group(1)):02d}:{m.group(2)}")
        spans.append(m.span())
    rest = _blank(rest, spans)
    for m in _NUM_RE.finditer(rest):
        toks.add(_norm_number(m.group(1), m.group(2)))
    toks |= _name_tokens(rest)
    return toks


def _is_number(tok: str) -> bool:
    return bool(re.fullmatch(r"\d+(?:\.\d+)?%?", tok))


def missing_share(note: Optional[str], reference_text: Optional[str]) -> Optional[float]:
    """Share of `note`'s key tokens absent from `reference_text` (0.0 if the note has none).
    Returns None if either text is missing."""
    if note is None or reference_text is None:
        return None
    toks = key_tokens(note)
    if not toks:
        return 0.0
    ref = key_tokens(reference_text)
    ref_nums = {t.rstrip("%") for t in ref if _is_number(t)}
    missing = 0
    for t in toks:
        if t in ref:
            continue
        if _is_number(t):
            if t.rstrip("%") in ref_nums:
                continue
        elif re.search(r"(?<![A-Za-z0-9])" + re.escape(t) + r"(?![A-Za-z0-9])", reference_text, re.IGNORECASE):
            continue
        missing += 1
    return missing / len(toks)
