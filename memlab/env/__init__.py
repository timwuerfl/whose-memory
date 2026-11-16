"""Task environment: deterministic multi-session episodes for the three families.

Public entry points live in `memlab.env.generate` (re-exported lazily here to avoid import cycles):
`make_episode`, `make_dataset`, `load_episodes`.
"""

__all__ = ["make_episode", "make_dataset", "load_episodes", "make_episode_with_meta"]


def __getattr__(name):
    if name in __all__:
        from memlab.env import generate
        return getattr(generate, name)
    raise AttributeError(name)
