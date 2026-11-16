"""Shared building blocks for the episode generators: name pools, a seeded drawing context that keeps
every entity / number unique within an episode, draft containers and option shuffling.

All randomness flows through a `random.Random` seeded from `memlab.schema.stable_hash`; nothing here
touches Python's global RNG or the builtin `hash()`.
"""
from __future__ import annotations

import random
from dataclasses import dataclass, field
from typing import Callable, Optional

from memlab.attacks.template import HEDGE_MARKERS, occurs
from memlab.schema import Observation

# ------------------------------------------------------------------------------------------------
# Name pools (all invented or generic; no real companies, drugs or people)
# ------------------------------------------------------------------------------------------------

FIRST_NAMES = [
    "Aaliyah", "Abebe", "Adaeze", "Aiko", "Akira", "Alejandro", "Amara", "Amir", "Anahi", "Ananya", "Anders",
    "Aroha", "Arjun", "Ayesha", "Bao", "Beatriz", "Bilal", "Bongani", "Bruno", "Camille", "Carmen", "Chen",
    "Chiara", "Chidi", "Dalia", "Dana", "Dante", "Darius", "Deniz", "Dmitri", "Ebo", "Elena", "Elif", "Emeka",
    "Emil", "Esi", "Farah", "Femi", "Freya", "Gael", "Giulia", "Hamid", "Hana", "Haruto", "Hiroshi", "Hugo",
    "Ibrahim", "Ilse", "Imani", "Ines", "Ingrid", "Isabela", "Jae-won", "Jamal", "Javier", "Jin", "Joaquin",
    "Kaito", "Kalani", "Kavya", "Kemal", "Kenji", "Kofi", "Lars", "Layla", "Leila", "Leilani", "Lena", "Lior",
    "Lucia", "Lwazi", "Maeve", "Malik", "Marek", "Mariam", "Mateo", "Mei", "Mehmet", "Mihail", "Mira",
    "Nadia", "Naledi", "Nasrin", "Niamh", "Nikhil", "Nkechi", "Noor", "Oksana", "Olu", "Omar", "Oren",
    "Pania", "Parisa", "Pedro", "Priya", "Quang", "Rafael", "Rania", "Ravi", "Rhea", "Rohan", "Ruth",
    "Saanvi", "Salma", "Samir", "Santiago", "Saoirse", "Seo-yeon", "Shira", "Sione", "Sofia", "Sunita",
    "Sven", "Tariq", "Tavita", "Teodor", "Tevita", "Thandiwe", "Tiago", "Tomasz", "Uzma", "Valentina",
    "Vikram", "Wanjiru", "Wei", "Xochitl", "Yara", "Yasmin", "Yerlan", "Yuki", "Yusuf", "Zainab", "Zara",
    "Zhanna", "Zofia", "Zuri", "Kwame", "Astrid", "Mattias", "Nomvula", "Paulo", "Renata", "Selin", "Tao",
]

_STEM_A = ["Bel", "Cor", "Dra", "Fen", "Gal", "Hes", "Ith", "Jor", "Kel", "Lun", "Mar", "Nov", "Orr", "Pel",
           "Quin", "Ros", "Sav", "Tor", "Ul", "Ves", "Wyn", "Yar", "Zel", "Bram", "Cal", "Dun", "Ev", "Grel",
           "Hal", "Isk", "Kav", "Lor", "Mox", "Ner", "Ost", "Pry", "Rhen", "Sol", "Tam", "Vel"]
_STEM_B = ["a", "e", "i", "o", "", "", "ri", "an", "en", "or", "el"]
_STEM_C = ["dex", "vane", "brook", "mere", "ton", "vex", "ley", "rik", "stad", "wick", "lan", "more",
           "quist", "tal", "dale", "worth", "gard", "holm", "corp", "line", "tek", "ford", "nix", "bury"]

MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
          "November", "December"]
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


class Reject(Exception):
    """Raised when a draw cannot satisfy the episode's constraints; the generator retries with a new attempt."""


# ------------------------------------------------------------------------------------------------
# Observation helpers
# ------------------------------------------------------------------------------------------------

def T(source: str, text: str) -> Observation:
    return Observation("tool", source, text)


def D(source: str, text: str) -> Observation:
    return Observation("document", source, text)


def W(source: str, text: str) -> Observation:
    return Observation("web", source, text)


def U(text: str) -> Observation:
    return Observation("user", "user", text)


def A(source: str, text: str) -> Observation:
    return Observation("agent", source, text)


def poss(name: str) -> str:
    """English possessive: "Corvane Foods'" / "Dana's"."""
    return name + "'" if name.endswith("s") else name + "'s"


def an(x) -> str:
    """Indefinite article for the word or number that follows: an(80) -> "an", an("Evinix") -> "an"."""
    t = str(x).lstrip("$")
    if t[:1].isdigit():
        digits = t.replace(",", "").split(".")[0]
        digits = "".join(ch for ch in digits if ch.isdigit())
        return "an" if digits.startswith("8") or (digits[:2] in ("11", "18") and len(digits) in (2, 5)) else "a"
    return "an" if t[:1].lower() in "aeiou" else "a"


def fmt_int(n: int) -> str:
    return f"{n:,}"


def fmt_money(x: float) -> str:
    return f"{x:,.2f}"


# ------------------------------------------------------------------------------------------------
# Drafts produced by skeletons
# ------------------------------------------------------------------------------------------------

@dataclass
class AttackDraft:
    """Everything a skeleton produces for one attack opportunity (session + EditSpec minus placement)."""
    skeleton: str
    edit_type: str
    title: str
    observations: list
    fact_key: str
    true_content: str
    forged_content: str
    t0_find: Optional[str]
    t0_replace: Optional[str]
    t0_append: str
    must_contain: list
    must_not_contain: list
    q_text: str
    correct: str
    attacked: str
    distractors: list
    # entity strings that pin the question to this session: must occur in this trace and in the question,
    # and in no other session trace
    anchors: list = field(default_factory=list)
    # strings that must occur in NO session trace of the episode (forged tokens, novel option values)
    novel: list = field(default_factory=list)


@dataclass
class FillerDraft:
    skeleton: str
    title: str
    observations: list


# ------------------------------------------------------------------------------------------------
# Drawing context
# ------------------------------------------------------------------------------------------------

class Ctx:
    """Seeded drawing context. Every `fresh` value is unique (case-insensitively) within the episode."""

    def __init__(self, rng: random.Random):
        self.rng = rng
        self.used: set[str] = set()
        m = rng.randrange(12)
        self.month_a = MONTHS[m]
        self.month_b = MONTHS[(m + 1) % 12]

    # -- generic ---------------------------------------------------------------------------------
    def reserve(self, *values) -> None:
        for v in values:
            self.used.add(str(v).lower())

    def is_used(self, v) -> bool:
        return str(v).lower() in self.used

    def fresh(self, gen: Callable[[], object], tries: int = 400):
        for _ in range(tries):
            v = gen()
            if not self.is_used(v):
                self.reserve(v)
                return v
        raise Reject("could not draw a fresh value")

    def pick(self, seq):
        return self.rng.choice(seq)

    def sample(self, seq, k):
        return self.rng.sample(list(seq), k)

    def chance(self, p: float = 0.5) -> bool:
        return self.rng.random() < p

    # -- entities --------------------------------------------------------------------------------
    def person(self) -> str:
        return self.fresh(lambda: self.rng.choice(FIRST_NAMES))

    def people(self, k: int) -> list:
        return [self.person() for _ in range(k)]

    def stem(self) -> str:
        """Invented name stem; no two stems in an episode share their first four letters (avoids near-twins
        such as 'Pryequist' / 'Pryelquist' that read like typos of each other)."""
        r = self.rng
        prefixes = self.__dict__.setdefault("_stem_prefixes", set())
        for _ in range(400):
            s = (r.choice(_STEM_A) + r.choice(_STEM_B) + r.choice(_STEM_C)).capitalize()
            if self.is_used(s) or s[:4].lower() in prefixes:
                continue
            self.reserve(s)
            prefixes.add(s[:4].lower())
            return s
        raise Reject("could not draw a fresh stem")

    def org(self, suffixes) -> str:
        """Invented organisation name such as 'Corivane Supply'. Stems are unique within the episode."""
        return f"{self.stem()} {self.rng.choice(list(suffixes))}"

    def from_pool(self, pool) -> object:
        """Draw an item from `pool` not used before in this episode (items are str or tuples whose first
        element is the identifying string)."""
        def gen():
            return self.rng.choice(pool)
        for _ in range(400):
            item = gen()
            key = item[0] if isinstance(item, tuple) else item
            if not self.is_used(key):
                self.reserve(key)
                return item
        raise Reject("pool exhausted")

    def code(self, fmt: str) -> str:
        """Fill a code template: {d} digit, {L} uppercase letter. e.g. 'PO-{d}{d}{d}{d}'."""
        r = self.rng

        def gen():
            out = []
            i = 0
            while i < len(fmt):
                if fmt.startswith("{d}", i):
                    out.append(str(r.randrange(10)))
                    i += 3
                elif fmt.startswith("{n}", i):
                    out.append(str(r.randrange(1, 10)))
                    i += 3
                elif fmt.startswith("{L}", i):
                    out.append(r.choice("ABCDEFGHJKLMNPRSTUVWXYZ"))
                    i += 3
                else:
                    out.append(fmt[i])
                    i += 1
            return "".join(out)
        return self.fresh(gen)

    # -- numbers ---------------------------------------------------------------------------------
    def num(self, lo: int, hi: int, step: int = 1) -> int:
        r = self.rng
        v = self.fresh(lambda: fmt_int(r.randrange(lo, hi + 1, step)))
        return int(v.replace(",", ""))

    def money(self, lo: float, hi: float) -> str:
        r = self.rng
        return self.fresh(lambda: fmt_money(round(r.uniform(lo, hi), 2)))

    def pct(self, lo: int, hi: int, step: int = 1) -> str:
        r = self.rng
        return self.fresh(lambda: f"{r.randrange(lo, hi + 1, step)}%")

    def date(self) -> str:
        r = self.rng
        return self.fresh(lambda: f"{r.randrange(2, 28)} {r.choice([self.month_a, self.month_b])}")

    def date_near(self, date: str) -> str:
        """A different, plausible date in the same month."""
        day, month = date.split(" ", 1)
        d = int(day)
        r = self.rng

        def gen():
            nd = d + r.choice([-9, -7, -6, -5, -3, -2, 2, 3, 5, 6, 7, 9])
            nd = min(max(nd, 2), 28)
            return f"{nd} {month}"
        return self.fresh(gen)

    def time(self) -> str:
        r = self.rng
        return self.fresh(lambda: f"{r.randrange(7, 18):02d}:{r.choice(['05', '10', '20', '25', '35', '40', '50', '55'])}")

    def weekday(self) -> str:
        return self.rng.choice(WEEKDAYS)

    # -- forged / distractor values --------------------------------------------------------------
    def forge_int(self, true: int, lo_frac: float = 0.15, hi_frac: float = 0.45) -> int:
        """A plausible wrong value: digit transposition or a shift of 15-45 %."""
        r = self.rng
        s = str(true)
        cands = []
        if r.random() < 0.5:
            for i in range(len(s) - 1):
                t = s[:i] + s[i + 1] + s[i] + s[i + 2:]
                if t != s and t[0] != "0":
                    cands.append(int(t))
            r.shuffle(cands)
        for _ in range(12):
            d = max(2, round(true * r.uniform(lo_frac, hi_frac)))
            cands.append(true + d if r.random() < 0.5 else true - d)
        for c in cands:
            cs = str(c)
            # same number of digits: keeps the magnitude plausible and the formatting identical (no "1,149"
            # in options vs "1149" in a T0-substituted note)
            if c <= 0 or len(cs) != len(s) or cs in s or s in cs or self.is_used(fmt_int(c)):
                continue
            self.reserve(fmt_int(c))
            return c
        raise Reject("could not forge int")

    def other_ints(self, true: int, k: int, spread=(0.1, 0.6), exclude=()) -> list:
        r = self.rng
        out = []
        tries = 0
        while len(out) < k:
            tries += 1
            if tries > 400:
                raise Reject("could not draw distractor ints")
            d = max(2, round(true * r.uniform(*spread)))
            c = true + d if r.random() < 0.5 else true - d
            cs = str(c)
            if c <= 0 or c in out or c in exclude or self.is_used(fmt_int(c)) or cs in str(true) or str(true) in cs:
                continue
            self.reserve(fmt_int(c))
            out.append(c)
        return out

    def other_money(self, true: str, k: int, spread=(0.08, 0.4)) -> list:
        r = self.rng
        t = float(true.replace(",", ""))
        out = []
        tries = 0
        while len(out) < k:
            tries += 1
            if tries > 400:
                raise Reject("could not draw distractor money")
            f = r.uniform(*spread)
            c = fmt_money(round(t * (1 + f if r.random() < 0.5 else 1 - f), 2))
            if c == true or c in out or self.is_used(c) or c in true or true in c:
                continue
            self.reserve(c)
            out.append(c)
        return out


# ------------------------------------------------------------------------------------------------
# Option shuffling
# ------------------------------------------------------------------------------------------------

LABELS = ("A", "B", "C", "D")


def shuffle_options(rng: random.Random, correct: str, attacked: str, distractors: list):
    """Return (options, correct_label, attacked_label) with a uniformly random label permutation."""
    texts = [correct, attacked] + list(distractors)
    if len(texts) != 4:
        raise ValueError("need exactly 2 distractors")
    if len({t.strip().lower() for t in texts}) != 4:
        raise Reject("option texts not distinct")
    order = rng.sample(range(4), 4)
    options = {lab: texts[i] for lab, i in zip(LABELS, order)}
    return options, LABELS[order.index(0)], LABELS[order.index(1)]


def e5_must_not_contain(true_content: str) -> list:
    """Hedge markers present in the faithful note sentence (all removable by `dehedge`)."""
    low = true_content.lower()
    found = [m for m in HEDGE_MARKERS if m in low]
    return found or ["preliminary", "unconfirmed", "not yet confirmed"]


def any_occurs(tokens, text) -> bool:
    return any(occurs(t, text) for t in tokens)
