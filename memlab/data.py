"""Shared file layout and loaders for the hosted experiments.

results/raw/{run}/{victim}/{stage}.jsonl        every model call of a stage (job rows: prompt meta, text, parsed, cost)
results/processed/{run}/{victim}/notes.json     {"genuine": {episode_id: [7 notes]}, "rederived": {...}, "style": {...}}
results/processed/{run}/{victim}/forged.jsonl   one row per forged note
results/processed/{run}/{victim}/*.jsonl        per-stage tidy outputs (one row per scored note / answered question)

`run` is "pilot" or "main" (see memlab.config.RUNS). A note that could not be produced is None.
"""
from __future__ import annotations

import functools
import json
from pathlib import Path
from typing import Iterable, Optional

from .config import RUNS, seeds_for
from .schema import EDIT_TYPES, FAMILIES, Episode, stable_hash

ROOT = Path(__file__).resolve().parents[1]
EPISODE_DIR = ROOT / "data" / "episodes"
HOSTED_TIERS = ("T0", "T1", "T2", "T3")


@functools.lru_cache(maxsize=None)
def _family(family: str) -> dict:
    from .env.generate import load_episodes
    return {ep.seed: ep for ep in load_episodes(str(EPISODE_DIR / f"{family}.jsonl"))}


def episodes(seeds: Iterable[int], families=FAMILIES) -> list:
    """Episodes for the given seeds, ordered by family then seed."""
    return [_family(f)[s] for f in families for s in seeds]


def run_episodes(run: str, victim: str, what: str = "seeds") -> list:
    return episodes(seeds_for(run, victim, what))


def episode(episode_id: str) -> Episode:
    fam, seed = episode_id.rsplit("-", 1)
    return _family(fam)[int(seed)]


def raw_dir(run: str, victim: str) -> Path:
    d = ROOT / "results" / "raw" / run / victim
    d.mkdir(parents=True, exist_ok=True)
    return d


def proc_dir(run: str, victim: str) -> Path:
    d = ROOT / "results" / "processed" / run / victim
    d.mkdir(parents=True, exist_ok=True)
    return d


# ------------------------------------------------------------------ notes
def save_notes(run: str, victim: str, kind: str, notes: dict) -> None:
    """kind: "genuine" | "rederived" | "style". notes: {episode_id: [note or None] * 7}."""
    p = proc_dir(run, victim) / "notes.json"
    allk = json.loads(p.read_text()) if p.exists() else {}
    allk[kind] = notes
    p.write_text(json.dumps(allk, ensure_ascii=False, indent=0))


def load_notes(run: str, victim: str, kind: str = "genuine") -> dict:
    return json.loads((proc_dir(run, victim) / "notes.json").read_text())[kind]


# ------------------------------------------------------------------ forgeries
def save_forged(run: str, victim: str, rows: list) -> None:
    """rows: {episode_id, edit_type, tier, session_idx, note, valid, mode, n_candidates?, selected_rating?}"""
    with open(proc_dir(run, victim) / "forged.jsonl", "w") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def load_forged(run: str, victim: str, valid_only: bool = False) -> list:
    rows = [json.loads(l) for l in open(proc_dir(run, victim) / "forged.jsonl")]
    return [r for r in rows if r["valid"]] if valid_only else rows


def forged_index(rows: list) -> dict:
    """(episode_id, edit_type, tier) -> row"""
    return {(r["episode_id"], r["edit_type"], r["tier"]): r for r in rows}


def write_jsonl(path: Path, rows: list) -> None:
    with open(path, "w") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def read_jsonl(path: Path) -> list:
    return [json.loads(l) for l in open(path)]


# ------------------------------------------------------------------ deterministic helpers
def question_order(ep: Episode) -> list:
    """Order in which an episode's five downstream questions are asked (fixed per episode)."""
    return sorted(EDIT_TYPES, key=lambda e: stable_hash("qorder", ep.episode_id, e))


def store_with(notes: list, slot: int, note: Optional[str]) -> list:
    """Copy of a memory store with one slot replaced."""
    out = list(notes)
    out[slot] = note
    return out


def slot_edit(ep: Episode) -> dict:
    """session_idx -> edit_type hosted by that session (filler sessions are absent)."""
    return {e.session_idx: k for k, e in ep.edits.items()}
