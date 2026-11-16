"""Attacks on memory notes. `template` holds the T0 template forger and the forgery-validity check."""
from memlab.attacks.template import apply_t0, dehedge, is_valid_forgery, occurs

__all__ = ["apply_t0", "dehedge", "is_valid_forgery", "occurs"]
