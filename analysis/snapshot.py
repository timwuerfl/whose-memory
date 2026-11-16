"""Interim snapshot of Pillar 1 trial rows while the runner is still going.

The Pillar 1 runner writes ``results/processed/<run>/<victim>/p1_pairs.jsonl`` only when it ends. This helper
derives the same tidy rows from the raw job rows collected so far, with the runner's own functions, so that the
analysis can be developed and the paper drafted on partial data. Rows whose latest state is a retryable error
(for example a connection error) are left out, because the runner will retry them. The runner's final write
replaces the file; nothing here is needed to reproduce the paper.

Usage: ``python -m analysis.snapshot [--run main]``
"""
from __future__ import annotations

import argparse

from experiments import p1_self_trust as P
from memlab.data import proc_dir, raw_dir, write_jsonl


def snapshot(run: str = "main") -> dict:
    _, mot = P._study()
    counts = {}
    for v in P.default_victims(run):
        raw = raw_dir(run, v) / f"{P.STAGE}.jsonl"
        if not raw.exists():
            continue
        eps = P.select_episodes(run, v, None)
        have = P.latest_rows(raw)
        rows = []
        for j in P.pair_jobs(eps, v, run, P.DESIGNS):
            r = have.get(j.job_id)
            if r is None or (r.get("error") and not P._degenerate(r, mot)):
                continue
            rows.append(P.pair_row(r, mot))
        write_jsonl(proc_dir(run, v) / "p1_pairs.jsonl", rows)
        counts[v] = len(rows)
    return counts


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", default="main")
    for v, n in snapshot(ap.parse_args().run).items():
        print(f"{v}: {n} trial rows")
