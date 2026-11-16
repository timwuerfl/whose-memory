"""Episode generator: `make_episode(family, seed)`, `make_dataset`, `load_episodes`, and a CLI.

    .venv/bin/python -m memlab.env.generate --n 400 --out data/episodes

Each family module exposes:
    task_brief(ctx) -> str
    ATTACKS: {"E1": [skeleton, ...], ..., "E5": [...]}   skeleton(ctx) -> AttackDraft
    FILLERS: [skeleton, ...]                               skeleton(ctx) -> FillerDraft
    P1_ITEMS: [fn, ...]                                    fn(ctx) -> (P1Item, anchors)
    CONF_ITEMS: [fn, ...]                                  fn(ctx) -> (ConfItem, anchors)

Generation is deterministic in (family, seed). A draw that violates a validity constraint raises
`Reject` and the generator retries with attempt+1 (still deterministic).
"""
from __future__ import annotations

import argparse
import json
import os
import random
import re

from memlab.attacks.template import apply_t0, is_valid_forgery, occurs
import importlib
from memlab.env.common import AttackDraft, Ctx, Reject, any_occurs, shuffle_options
from memlab.schema import (EDIT_TYPES, FAMILIES, EditSpec, Episode, Question, Session, episode_from_dict,
                           render_session, stable_hash)

def _family_module(family: str):
    if family not in FAMILIES:
        raise ValueError(f"unknown family {family!r}; expected one of {FAMILIES}")
    return importlib.import_module(f"memlab.env.{family}")

N_SESSIONS = 7
MIN_WORDS, MAX_WORDS = 80, 220
MAX_ATTEMPTS = 80


def word_count(text: str) -> int:
    return len(re.findall(r"\S+", text))


def _validate(ep: Episode, drafts: dict, p1_anchors: list, conf_anchors: list) -> None:
    traces = [render_session(s) for s in ep.sessions]
    for s, tr in zip(ep.sessions, traces):
        if not 3 <= len(s.observations) <= 6:
            raise Reject(f"session {s.idx}: {len(s.observations)} observations")
        wc = word_count(tr)
        if not MIN_WORDS <= wc <= MAX_WORDS:
            raise Reject(f"session {s.idx}: {wc} words")
    all_q_text = {}
    for et, e in ep.edits.items():
        q = e.question
        all_q_text[et] = q.text + "\n" + "\n".join(q.options.values())
    for et, e in ep.edits.items():
        d: AttackDraft = drafts[et]
        target = traces[e.session_idx]
        others = [tr for i, tr in enumerate(traces) if i != e.session_idx]
        # forged / novel tokens appear in no trace
        novel = list(d.novel)
        if et != "E5":
            novel.append(e.must_contain[0])
        for tok in novel:
            if any(occurs(tok, tr) for tr in traces):
                raise Reject(f"{et}: novel token {tok!r} occurs in a trace")
        if et == "E1":
            if not occurs(e.t0_find, target):
                raise Reject("E1: true value missing from target trace")
            if any(occurs(e.t0_find, tr) for tr in others):
                raise Reject("E1: true value leaks into another session")
        # anchors pin the question to the target session only
        for a in d.anchors:
            if not occurs(a, target):
                raise Reject(f"{et}: anchor {a!r} missing from target")
            if any(occurs(a, tr) for tr in others):
                raise Reject(f"{et}: anchor {a!r} leaks into another session")
            if not occurs(a, all_q_text[et]):
                raise Reject(f"{et}: anchor {a!r} missing from question")
            for et2, qt in all_q_text.items():
                if et2 != et and occurs(a, qt):
                    raise Reject(f"{et}: anchor {a!r} occurs in question {et2}")
        # independence: forged tokens of one edit do not occur in other edits' questions
        for et2, qt in all_q_text.items():
            if et2 != et and et != "E5" and occurs(e.must_contain[0], qt):
                raise Reject(f"{et}: forged token occurs in question {et2}")
        # T0 round trip on the faithful sentence
        forged, _mode = apply_t0(e.true_content, e)
        if not is_valid_forgery(forged, e) or is_valid_forgery(e.true_content, e):
            raise Reject(f"{et}: T0 round trip failed")
    p = ep.p1
    vals = [p.value_a, p.value_b, p.distractor]
    if len({v.lower() for v in vals}) != 3:
        raise Reject("p1 values not distinct")
    for tok in vals + list(p1_anchors) + list(conf_anchors):
        if any(occurs(tok, tr) for tr in traces):
            raise Reject(f"p1/conf token {tok!r} occurs in a session")


def _attempt(family: str, seed: int, attempt: int):
    mod = _family_module(family)
    # Structural choices (skeletons, session order) depend only on (family, seed), so that retries never bias
    # the skeleton mix towards skeletons that reject less often. Content is redrawn per attempt.
    srng = random.Random(stable_hash("memlab-structure", family, seed))
    skel = {et: srng.choice(mod.ATTACKS[et]) for et in EDIT_TYPES}
    filler_fns = srng.sample(mod.FILLERS, 2)
    p1_fn, conf_fn = srng.choice(mod.P1_ITEMS), srng.choice(mod.CONF_ITEMS)
    slots = list(EDIT_TYPES) + ["F0", "F1"]
    srng.shuffle(slots)

    rng = random.Random(stable_hash("memlab-env", family, seed, attempt))
    ctx = Ctx(rng)
    brief = mod.task_brief(ctx)
    drafts = {et: skel[et](ctx) for et in EDIT_TYPES}
    fillers = [f(ctx) for f in filler_fns]
    p1, p1_anchors = p1_fn(ctx)
    conf, conf_anchors = conf_fn(ctx)
    sessions, edits = [], {}
    episode_id = f"{family}-{seed:05d}"
    for idx, slot in enumerate(slots):
        if slot.startswith("F"):
            fd = fillers[int(slot[1])]
            sessions.append(Session(idx=idx, title=fd.title, observations=list(fd.observations)))
            continue
        d = drafts[slot]
        sessions.append(Session(idx=idx, title=d.title, observations=list(d.observations)))
        # option order depends only on (family, seed, edit type) -> uniform label balance
        orng = random.Random(stable_hash("memlab-options", family, seed, slot))
        options, c_lab, a_lab = shuffle_options(orng, d.correct, d.attacked, d.distractors)
        q = Question(qid=f"{episode_id}-{slot}", text=d.q_text, options=options, correct=c_lab, attacked=a_lab)
        edits[slot] = EditSpec(edit_type=slot, session_idx=idx, fact_key=d.fact_key, true_content=d.true_content,
                               forged_content=d.forged_content, t0_find=d.t0_find, t0_replace=d.t0_replace,
                               t0_append=d.t0_append, must_contain=list(d.must_contain),
                               must_not_contain=list(d.must_not_contain), question=q)
    ep = Episode(episode_id=episode_id, family=family, seed=seed, task_brief=brief, sessions=sessions,
                 edits=edits, p1=p1, conf=conf)
    _validate(ep, drafts, p1_anchors, conf_anchors)
    meta = {
        "attempt": attempt,
        "skeletons": {et: drafts[et].skeleton for et in EDIT_TYPES},
        "fillers": [f.skeleton for f in fillers],
        "anchors": {et: list(drafts[et].anchors) for et in EDIT_TYPES},
        "novel": {et: list(drafts[et].novel) for et in EDIT_TYPES},
        "p1_anchors": list(p1_anchors),
        "conf_anchors": list(conf_anchors),
        "slots": slots,
    }
    return ep, meta


def make_episode_with_meta(family: str, seed: int):
    _family_module(family)
    last = None
    for attempt in range(MAX_ATTEMPTS):
        try:
            return _attempt(family, seed, attempt)
        except Reject as exc:   # deterministic retry
            last = exc
    raise RuntimeError(f"could not generate {family} seed {seed}: {last}")


def make_episode(family: str, seed: int) -> Episode:
    return make_episode_with_meta(family, seed)[0]


def make_dataset(family: str, n: int, start_seed: int = 0) -> list:
    return [make_episode(family, s) for s in range(start_seed, start_seed + n)]


def load_episodes(path: str) -> list:
    out = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                out.append(episode_from_dict(json.loads(line)))
    return out


def main(argv=None) -> None:
    ap = argparse.ArgumentParser(description="Generate memlab episodes.")
    ap.add_argument("--n", type=int, default=400)
    ap.add_argument("--start-seed", type=int, default=0)
    ap.add_argument("--out", default="data/episodes")
    ap.add_argument("--families", nargs="*", default=list(FAMILIES))
    ap.add_argument("--example-seeds", default="3,1,2",
                    help="one seed per family (in --families order) for EXAMPLES.md; empty to skip")
    args = ap.parse_args(argv)
    os.makedirs(args.out, exist_ok=True)
    for fam in args.families:
        eps = make_dataset(fam, args.n, args.start_seed)
        path = os.path.join(args.out, f"{fam}.jsonl")
        with open(path, "w", encoding="utf-8") as f:
            for ep in eps:
                f.write(ep.to_json() + "\n")
        print(f"wrote {len(eps)} episodes to {path}")
    if args.example_seeds:
        seeds = [int(x) for x in args.example_seeds.split(",")]
        path = os.path.join(args.out, "EXAMPLES.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(EXAMPLES_HEADER)
            for fam, seed in zip(args.families, seeds):
                f.write("\n" + episode_markdown(make_episode(fam, seed)) + "\n")
        print(f"wrote {path}")


EXAMPLES_HEADER = """# Example episodes

One fully rendered episode per family, generated by
`.venv/bin/python -m memlab.env.generate --n 400 --out data/episodes`.
Each episode has 7 sessions; 5 host one attack opportunity each (E1-E5, order shuffled per episode),
2 are filler. Session text is exactly `render_session(session)`, i.e. what the note-writing agent sees.
For each edit: the faithful content (`true_content`), the attacker's content (`forged_content`), the T0
template fields, the validity tokens, and the downstream question with the correct and attacked options
marked. The P1 (provenance) and confidence items at the end refer to facts that appear in no session.
"""



# ------------------------------------------------------------------------------------------------
# Human-readable rendering (used for data/episodes/EXAMPLES.md)
# ------------------------------------------------------------------------------------------------

def episode_markdown(ep: Episode) -> str:
    from memlab.schema import EDIT_NAMES
    host = {e.session_idx: et for et, e in ep.edits.items()}
    out = [f"## {ep.family}: `{ep.episode_id}`", "", f"**Task brief.** {ep.task_brief}", ""]
    out.append("### Sessions (as rendered for the agent)")
    for s in ep.sessions:
        tag = f"hosts {host[s.idx]} ({EDIT_NAMES[host[s.idx]]})" if s.idx in host else "filler"
        out += ["", f"#### Session {s.idx + 1} - {tag}", "", "```text", render_session(s), "```"]
    out += ["", "### Edits"]
    for et in EDIT_TYPES:
        e = ep.edits[et]
        q = e.question
        out += ["", f"#### {et} - {EDIT_NAMES[et]} (session {e.session_idx + 1})", "",
                f"- fact_key: {e.fact_key}",
                f"- true_content: {e.true_content}",
                f"- forged_content: {e.forged_content}",
                f"- t0_find / t0_replace: {e.t0_find!r} / {e.t0_replace!r}",
                f"- t0_append: {e.t0_append}",
                f"- must_contain: {e.must_contain}; must_not_contain: {e.must_not_contain}",
                f"- **Question:** {q.text}"]
        for lab, txt in q.options.items():
            mark = " **(correct)**" if lab == q.correct else (" *(attacked)*" if lab == q.attacked else "")
            out.append(f"    - {lab}. {txt}{mark}")
    p = ep.p1
    out += ["", "### P1 item (provenance channel)", "",
            f"- fact_key: {p.fact_key}",
            f"- claim_template: {p.claim_template}",
            f"- evidence_template: {p.evidence_template}  (source: `{p.evidence_source}`)",
            f"- value_a / value_b / distractor: {p.value_a} / {p.value_b} / {p.distractor}",
            f"- question: {p.question_text}",
            f"- option_template: {p.option_template}; escalate_option: {p.escalate_option}",
            f"- tool / web / agent: {p.tool_name} / {p.web_domain} / {p.agent_name}"]
    for o in p.filler:
        out.append(f"- filler [{o.kind}: {o.source}]: {o.text}")
    c = ep.conf
    out += ["", "### Confidence item", "",
            f"- fact_key: {c.fact_key}", f"- hedged: {c.hedged}", f"- certain: {c.certain}",
            f"- statement: {c.statement}", f"- question: {c.question_text}",
            f"- act_option: {c.act_option}", f"- verify_option: {c.verify_option}", f"- tool: {c.tool_name}", ""]
    return "\n".join(out)


if __name__ == "__main__":
    main()
