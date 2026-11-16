"""Study configuration: models, splits, sampling settings. One source of truth for all runners."""
from __future__ import annotations

from .schema import EDIT_TYPES, FAMILIES, stable_hash

# ---------------------------------------------------------------- models
HOSTED_VICTIMS = (
    "deepseek-v4-flash",
    "qwen3.8-27b",
    "gemma-4-31b-it",
    "glm-5.3-flash",
    "glm-5.2",           # the large model (reduced sample)
)
# qwen3.5-397b accepts only 3 requests in flight per key and reasons for ~100 s per call, so it cannot run the
# full chain inside the weekend; it joins Pillar 1 only (single short calls).
P1_EXTRA_VICTIMS = ("qwen3.5-397b",)

MODEL_FAMILY = {
    "deepseek-v4-flash": "deepseek",
    "qwen3.8-27b": "qwen",
    "qwen3.5-397b": "qwen",
    "gemma-4-31b-it": "gemma",
    "gemma-4-26b-a4b-it": "gemma",
    "glm-5.3-flash": "glm",
    "glm-5.2": "glm",
}

SHORT = {
    "deepseek-v4-flash": "DeepSeek-V4-Flash",
    "qwen3.8-27b": "Qwen3.8-27B",
    "qwen3.5-397b": "Qwen3.5-397B",
    "gemma-4-31b-it": "Gemma-4-31B",
    "gemma-4-26b-a4b-it": "Gemma-4-26B",
    "glm-5.3-flash": "GLM-5.3-Flash",
    "glm-5.2": "GLM-5.2",
}


def judge_for(victim: str) -> str:
    """Cross-family judge for the re-derivation comparison (never the victim's family)."""
    return "gemma-4-31b-it" if MODEL_FAMILY.get(victim) == "deepseek" else "deepseek-v4-flash"


def t1_forger_for(victim: str) -> str:
    """Other-family forger (T1). Default is a model that is not a victim at all."""
    return "glm-5.3-flash" if MODEL_FAMILY.get(victim) == "gemma" else "gemma-4-26b-a4b-it"


def other_model_for(victim: str, key: str, pool=HOSTED_VICTIMS) -> str:
    """Which other-family victim supplies the 'other-model note' negative for a given item."""
    cands = [m for m in pool if MODEL_FAMILY[m] != MODEL_FAMILY.get(victim, "local")]
    return cands[stable_hash("other-model", victim, key) % len(cands)]


# ---------------------------------------------------------------- data splits (seeds per family)
# The hosted API allows ~70 requests/min in total (SPECS.md), so sample sizes are set by request count.
MAIN_SEEDS = range(50, 84)          # 34 episodes per family -> 102 episodes, 510 attack instances per tier per victim
LARGE_MODEL_SEEDS = range(50, 70)   # the large model: 60 episodes, 300 instances per tier
P1_SEEDS = range(50, 90)            # Pillar 1 / confidence items: 120 per victim (independent of notes)
STYLE_SEEDS = range(300, 305)       # episodes whose genuine notes serve only as style examples for T2/T3 forgers
LOCAL_SEEDS = range(50, 100)        # local victim: 50 episodes per family (GPU time is the limit)
LOCAL_STYLE_SEEDS = range(300, 310) # style-example episodes for the local T2-T4 forgers

LARGE_MODEL = "glm-5.2"

RUNS = {
    # the pilot never enters the main analysis
    "pilot": {"seeds": range(0, 4), "p1_seeds": range(0, 6), "style_seeds": range(20, 23),
              "victims": ("deepseek-v4-flash", "gemma-4-31b-it")},
    "main": {"seeds": MAIN_SEEDS, "p1_seeds": P1_SEEDS, "style_seeds": STYLE_SEEDS, "victims": HOSTED_VICTIMS},
}


def seeds_for(run: str, victim: str, what: str = "seeds"):
    """Seeds (per family) of a run for one victim. what: "seeds" | "p1_seeds" | "style_seeds"."""
    r = RUNS[run]
    if run == "main" and what == "seeds" and victim == LARGE_MODEL:
        return LARGE_MODEL_SEEDS
    return r[what]


def is_calibration(episode_id: str) -> bool:
    """25% of main episodes form the calibration split (gate thresholds, probe model selection)."""
    return stable_hash("calib", episode_id) % 4 == 0


def variant_for(episode_id: str, edit_type: str = "") -> int:
    """Prompt phrasing (0-2) assigned to an item; identical across tiers and detectors for that item."""
    return stable_hash("variant", episode_id, edit_type) % 3


def t3_subset(episode_id: str) -> tuple:
    """The two edit types per episode that get the (expensive) adaptive T3/T4 forger. Balanced over types."""
    k = stable_hash("t3", episode_id) % len(EDIT_TYPES)
    return (EDIT_TYPES[k], EDIT_TYPES[(k + 2) % len(EDIT_TYPES)])


# ---------------------------------------------------------------- sampling settings
NOTE_TEMPERATURE = 0.7       # genuine notes (sample_idx 0) and re-derivations (sample_idx 1, 2)
N_REDERIVE = 1               # one independent re-derivation per session (sample_idx 1)
FORGE_TEMPERATURE = 0.7      # T1, T2
T3_N_CANDIDATES = 8          # adaptive best-of-N (hosted: 4 calls x 2 rewrites per note; local: 8 samples)
T3_CALLS = 4
T3_VERSIONS_PER_CALL = 2
T3_TEMPERATURE = 1.0
JUDGE_TEMPERATURE = 0.0
QUERY_TEMPERATURE = 0.0      # all detector queries and downstream answers
N_STYLE_EXAMPLES = 3

# ---------------------------------------------------------------- local models (filled in after verification)
LOCAL_PRIMARY = "Qwen/Qwen3.5-4B"
LOCAL_PRIMARY_REVISION = "851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a"
LOCAL_SECONDARY = "Qwen/Qwen3.5-0.8B"          # external-perplexity scorer
LOCAL_SECONDARY_REVISION = "2fc06364715b967f1860aea9cf38778875588b17"
LOCAL_GPT2 = "openai-community/gpt2"
LOCAL_DTYPE = "fp16"                           # bf16 results depend on batch shape on MPS; fp16 does not
LOCAL_OTHER_MODELS = ("deepseek-v4-flash", "gemma-4-31b-it")   # write 'other-model' notes for the local episodes
LOCAL_T1_FORGER = "gemma-4-26b-a4b-it"

__all__ = [n for n in dir() if not n.startswith("_")]
