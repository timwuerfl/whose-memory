"""A tiny, real HMAC-SHA256 provenance layer for memory stores (defence G2s).

At write time the memory system signs each note together with its author, its session index and the
hash of the session trace it was written from. The signature binds the note to that exact slot and
trace, so a signature cannot be replayed onto another session or another trace. An attacker who edits
a note in place without the key leaves the old signature behind, and verification fails. An insider who
holds the key re-signs the edited note, and verification passes (the threat model G2s does not cover).

The key comes from ``os.urandom`` once per run and is never written to disk. Signatures never enter a
prompt: the agent only sees the verification verdict (``signature=VALID|INVALID``).
"""
from __future__ import annotations

import hashlib
import hmac
import json
import os
from dataclasses import dataclass
from typing import Optional, Sequence

from ..prompts import tag_signed

KEY_BYTES = 32


def new_key() -> bytes:
    return os.urandom(KEY_BYTES)


def _message(note: str, author: str, session_idx: int, trace_hash: str) -> bytes:
    # canonical, unambiguous encoding of all signed fields (JSON array, no whitespace variance)
    return json.dumps(["memlab-note-v1", author, int(session_idx), trace_hash, note],
                      ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def sign(note: str, author: str, session_idx: int, trace_hash: str, key: bytes) -> str:
    return hmac.new(key, _message(note, author, session_idx, trace_hash), hashlib.sha256).hexdigest()


def verify(note: str, author: str, session_idx: int, trace_hash: str, sig: Optional[str], key: bytes) -> bool:
    if not sig:
        return False
    return hmac.compare_digest(sign(note, author, session_idx, trace_hash, key), sig)


@dataclass
class Entry:
    note: Optional[str]
    author: str
    session_idx: int
    trace_hash: str
    sig: Optional[str]


class SignedStore:
    """One episode's memory store with per-entry HMAC signatures.

    `notes[i]` is the note of session i (None = no entry); `trace_hashes[i]` = `trace_hash(session i)`.
    """

    def __init__(self, notes: Sequence[Optional[str]], trace_hashes: Sequence[str], key: bytes,
                 author: str = "self"):
        if len(notes) != len(trace_hashes):
            raise ValueError("notes and trace_hashes differ in length")
        self._key = key
        self.entries = [Entry(n, author, i, th, sign(n, author, i, th, key) if n is not None else None)
                        for i, (n, th) in enumerate(zip(notes, trace_hashes))]

    # -- attacker ----------------------------------------------------------------------
    def tamper(self, slot: int, text: str, key: Optional[bytes] = None) -> None:
        """Overwrite an entry's text in place. Without a key the old signature stays (and no longer
        verifies). With a key (the insider) the entry is re-signed with that key."""
        e = self.entries[slot]
        e.note = text
        if key is not None:
            e.sig = sign(text, e.author, e.session_idx, e.trace_hash, key)

    # -- memory system ------------------------------------------------------------------
    def rewrite(self, slot: int, text: str) -> None:
        """The memory system itself replaces an entry (e.g. with a note re-derived from the trace) and signs it."""
        e = self.entries[slot]
        e.note = text
        e.sig = sign(text, e.author, e.session_idx, e.trace_hash, self._key) if text is not None else None

    # -- reading ------------------------------------------------------------------------
    def verified(self) -> list:
        """Per entry: True / False, or None for an empty slot."""
        return [None if e.note is None else verify(e.note, e.author, e.session_idx, e.trace_hash, e.sig, self._key)
                for e in self.entries]

    def invalid_slots(self) -> list:
        return [i for i, v in enumerate(self.verified()) if v is False]

    def notes(self) -> list:
        return [e.note for e in self.entries]

    def tags(self) -> list:
        """Rendered provenance tags (`tag_signed`) with the verification verdict; None for empty slots."""
        return [None if v is None else tag_signed(e.author, e.session_idx, e.trace_hash, v)
                for e, v in zip(self.entries, self.verified())]
