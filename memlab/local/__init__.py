"""Local open-weight model utilities (surprisal, activations, yes/no probabilities, generation).

Typical use::

    from memlab.local import LocalLM, PlainLM, MODELS
    lm = LocalLM(MODELS["primary"]["id"], revision=MODELS["primary"]["revision"])
    scores, acts = lm.score_and_activations(batch_messages, notes, layers="auto")
"""
from .model import (
    MODELS,
    LocalLM,
    PlainLM,
    free_memory,
    load_npz,
    pick_device,
    save_npz,
)

__all__ = ["MODELS", "LocalLM", "PlainLM", "free_memory", "load_npz", "pick_device", "save_npz"]
