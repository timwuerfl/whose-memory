"""Reproduce every analysis output from the processed data, without any model request.

Usage: ``python -m analysis.reproduce [--run main]``

Steps: hosted analysis -> local analysis (``analysis/local.py``, if present) -> reasoning-on robustness arm and
its comparison (if ``results/processed/<run>_reasoning_low/`` exists) -> figures -> tables -> numbers -> SUMMARY.md.
Reads only ``results/processed/``, ``results/raw/local/`` (through ``analysis.local``) and
``results/spend_ledger.csv``.
"""
from __future__ import annotations

import argparse
import importlib
import time

from . import compare, figures, hosted, numbers, summary, suspicion, tables
from .common import ARM_SUFFIX, PROCESSED


def run_local() -> str:
    try:
        local = importlib.import_module("analysis.local")
    except ImportError as e:
        return f"skipped (analysis.local not importable: {e})"
    if not local.has_activations():
        # the pooled activations behind the probes (about 300 MB) are not in the repository; without them the
        # local analysis cannot be recomputed in full, so the committed results/analysis/local.json is kept
        return ("kept committed results/analysis/local.json (activations not present; regenerate them with "
                "`python -m experiments.local_pipeline score` to recompute)")
    local.main()
    return "done"


def main(argv=None) -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--run", default="main")
    a = ap.parse_args(argv)
    t0 = time.time()
    hosted.main(["--run", a.run])
    print(f"[local] {run_local()}")
    arm = a.run + ARM_SUFFIX
    if not a.run.endswith(ARM_SUFFIX) and (PROCESSED / arm).exists():
        hosted.main(["--run", arm])
        compare.main(["--a", a.run, "--b", arm])
    suspicion.main(["--run", a.run])
    figures.main(["--run", a.run])
    tables.main(["--run", a.run])
    numbers.main(["--run", a.run])
    summary.main(["--run", a.run])
    print(f"[reproduce] run={a.run} finished in {time.time() - t0:.0f} s")


if __name__ == "__main__":
    main()
