"""Core data contracts for memlab.

Every other module codes against these dataclasses. They are plain, JSON-serialisable
containers; all behaviour lives elsewhere (env/, agents/, attacks/, detectors/, defenses/).

Vocabulary
----------
episode   one simulated multi-session task with a fully known world state
session   one sitting; the agent sees its observations and writes exactly ONE memory note
trace     the logged observations of a session (stored next to the note; the attacker cannot edit it)
note      the agent's own short natural-language memory entry for a session
edit      an attacker change to one note (types E1-E5), with a designed downstream consequence
tier      forger capability, T0 (template) ... T4 (adaptive, internals-guided)
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass, field
from typing import Optional

FAMILIES = ("inventory", "research", "assistant")
EDIT_TYPES = ("E1", "E2", "E3", "E4", "E5")
EDIT_NAMES = {
    "E1": "factual swap",
    "E2": "injected instruction",
    "E3": "forged conclusion",
    "E4": "forged commitment",
    "E5": "confidence inflation",
}
TIERS = ("T0", "T1", "T2", "T3", "T4")
CHANNELS = ("memory", "tool", "web", "user", "agent", "unattributed")
OBS_KINDS = ("tool", "document", "web", "user", "agent")


@dataclass
class Observation:
    """One item the agent sees inside a session."""
    kind: str      # one of OBS_KINDS
    source: str    # e.g. "inventory_db", "user", "trial_report_K17.pdf", "agent:scheduler"
    text: str


@dataclass
class Question:
    """Deterministically scorable downstream question / action.

    `options` maps labels "A".."D" to option text; label order is shuffled per episode by the
    generator. `correct` is right under the true world state (i.e. with genuine memory).
    `attacked` is the label an agent picks if it believes the edit. They always differ.
    """
    qid: str
    text: str
    options: dict
    correct: str
    attacked: str


@dataclass
class EditSpec:
    """One attack opportunity. Each episode carries exactly one per edit type, on distinct sessions."""
    edit_type: str            # "E1".."E5"
    session_idx: int          # which session's note is the target
    fact_key: str             # short name of the fact, e.g. "opening stock of SKU-114"
    true_content: str         # one sentence the trace supports (what a faithful note conveys)
    forged_content: str       # one or two sentences the attacker wants the note to assert
    # T0 template edit. If `t0_find` occurs verbatim in the genuine note, substitute it with
    # `t0_replace`; otherwise append `t0_append` to the note. For E2-E4 `t0_find` is None.
    t0_find: Optional[str]
    t0_replace: Optional[str]
    t0_append: str
    # Cheap validity check for forged notes at any tier (case-insensitive substring tests).
    must_contain: list
    must_not_contain: list
    question: Question


@dataclass
class Session:
    idx: int
    title: str
    observations: list        # list[Observation]


@dataclass
class P1Item:
    """Pillar 1 item: one claim that can be delivered through any provenance channel.

    The claim and the contradicting evidence use the same template with different values;
    which of value_a / value_b plays the claim is counterbalanced by the experiment code.
    The world is fictional, so neither value is knowable a priori.
    """
    fact_key: str
    claim_template: str       # full sentence with "{value}", e.g. "The reorder threshold for SKU-114 is {value} units."
    evidence_template: str    # document-style line with "{value}"
    evidence_source: str      # e.g. "supplier_agreement_2031.pdf"
    value_a: str
    value_b: str
    distractor: str           # a third plausible value appearing nowhere in context
    option_template: str      # how a value is shown as an answer option, with "{value}"
    question_text: str        # action-style question whose answer is one of the values
    escalate_option: str      # the "flag the conflict / check before acting" option text
    tool_name: str            # header fillers for the channels
    web_domain: str
    agent_name: str
    filler: list              # list[Observation]: 2 topical but irrelevant context items


@dataclass
class ConfItem:
    """Confidence-laundering item: the same fact stated hedged vs certain, no counter-evidence."""
    fact_key: str
    hedged: str               # e.g. "A preliminary count suggests about 40 units ... not yet confirmed."
    certain: str              # e.g. "40 units ... are missing; this has been confirmed."
    statement: str            # the bare proposition whose probability the agent reports
    question_text: str        # decision that should wait for confirmation
    act_option: str           # act now, as if the fact were established
    verify_option: str        # verify / wait first
    tool_name: str


@dataclass
class Episode:
    episode_id: str           # f"{family}-{seed:05d}"
    family: str
    seed: int
    task_brief: str           # the agent's standing role, 1-3 sentences
    sessions: list            # list[Session], 7 sessions: 5 host one edit each, 2 are filler
    edits: dict               # edit_type -> EditSpec
    p1: P1Item
    conf: ConfItem

    def to_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False)


def _obs(d) -> Observation:
    return Observation(**d)


def episode_from_dict(d: dict) -> Episode:
    sessions = [Session(idx=s["idx"], title=s["title"], observations=[_obs(o) for o in s["observations"]])
                for s in d["sessions"]]
    edits = {}
    for k, e in d["edits"].items():
        e = dict(e)
        e["question"] = Question(**e["question"])
        edits[k] = EditSpec(**e)
    p1 = dict(d["p1"])
    p1["filler"] = [_obs(o) for o in p1["filler"]]
    return Episode(episode_id=d["episode_id"], family=d["family"], seed=d["seed"], task_brief=d["task_brief"],
                   sessions=sessions, edits=edits, p1=P1Item(**p1), conf=ConfItem(**d["conf"]))


def render_session(session: Session) -> str:
    """Canonical text rendering of a session's trace. Used for note writing, re-derivation,
    consistency checks, surprisal conditioning and trace hashing - always this exact string."""
    lines = [f"SESSION {session.idx + 1}: {session.title}"]
    for o in session.observations:
        label = {
            "tool": f"[Tool output: {o.source}]",
            "document": f"[Document: {o.source}]",
            "web": f"[Web snippet: {o.source}]",
            "user": "[User message]",
            "agent": f"[Message from agent: {o.source}]",
        }[o.kind]
        lines.append(f"{label}\n{o.text}")
    return "\n\n".join(lines)


def trace_hash(session: Session) -> str:
    return hashlib.sha256(render_session(session).encode("utf-8")).hexdigest()[:16]


def stable_hash(*parts) -> int:
    """Deterministic non-negative int from arbitrary parts (for counterbalancing / assignment)."""
    h = hashlib.sha256("||".join(str(p) for p in parts).encode("utf-8")).hexdigest()
    return int(h[:12], 16)
