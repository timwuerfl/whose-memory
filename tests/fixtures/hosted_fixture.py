"""Hand-made stand-in for the `hosted_gen` outputs (notes.json, forged.jsonl), in memlab.data's formats.

Genuine note of a session = its title plus the hosting edit's `true_content` (filler sessions get a routine
sentence); the re-derived note is a lightly reworded copy. T0 forgeries come from `apply_t0`; "T1"-"T3"
replace the true content by the edit's `forged_content` with a tier-specific lead-in. Validity is checked
with `is_valid_forgery`, exactly as hosted_gen does.
"""
from __future__ import annotations

from memlab import data as D
from memlab.attacks import apply_t0, is_valid_forgery
from memlab.data import HOSTED_TIERS, save_forged, save_notes
from memlab.schema import EDIT_TYPES

_LEAD = {"T1": "Session recap.", "T2": "Note to self.", "T3": "For my records."}


_VOICE = ("", " Logged for follow-up.")  # victim-specific style, so that notes differ between victims


def genuine_notes(ep, voice: int = 0) -> list:
    se = D.slot_edit(ep)
    out = []
    for s, sess in enumerate(ep.sessions):
        if s in se:
            out.append(f"{sess.title}: {ep.edits[se[s]].true_content}{_VOICE[voice % 2]}")
        else:
            out.append(f"{sess.title}: routine session, nothing to carry forward.{_VOICE[voice % 2]}")
    return out


def rederived_notes(ep, voice: int = 0) -> list:
    return [f"In this session ({n.split(':', 1)[0]}):{n.split(':', 1)[1]}" for n in genuine_notes(ep, voice)]


def forged_rows(ep, genuine: list, invalid: set = frozenset()) -> list:
    rows = []
    for et in EDIT_TYPES:
        e = ep.edits[et]
        g = genuine[e.session_idx]
        for tier in HOSTED_TIERS:
            if tier == "T0":
                note, mode = apply_t0(g, e)
            else:
                note, mode = f"{_LEAD[tier]} {ep.sessions[e.session_idx].title}: {e.forged_content}", "rewrite"
            valid = is_valid_forgery(note, e) and (ep.episode_id, et, tier) not in invalid
            rows.append({"episode_id": ep.episode_id, "edit_type": et, "tier": tier, "session_idx": e.session_idx,
                         "note": note if valid else None, "valid": valid, "mode": mode})
    return rows


def build(run: str, victims, missing: dict = None, invalid: set = frozenset(), with_style: bool = False) -> dict:
    """Write notes.json and forged.jsonl for every victim of `run` (memlab.config.RUNS) under
    memlab.data.ROOT. `missing`: {victim: [(episode_id, slot), ...]} genuine notes set to None.
    `invalid`: {(episode_id, edit_type, tier)} forgeries marked invalid. Returns {victim: forged rows}."""
    missing = missing or {}
    out = {}
    for i, v in enumerate(victims):
        eps = D.run_episodes(run, v)
        gen = {ep.episode_id: genuine_notes(ep, i) for ep in eps}
        red = {ep.episode_id: rederived_notes(ep, i) for ep in eps}
        forged = []
        for ep in eps:
            forged += forged_rows(ep, gen[ep.episode_id], invalid)
        for eid, s in missing.get(v, []):
            gen[eid][s] = None
        save_notes(run, v, "genuine", gen)
        save_notes(run, v, "rederived", red)
        save_forged(run, v, forged)
        out[v] = forged
    return out
