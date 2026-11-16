"""Operational status of the hosted runs: throughput, limiter state, 429s by model, rows per stage.

    .venv/bin/python -m experiments.status [--minutes 10]

Reads only local files (ledger, limiter state, raw job rows); makes no API requests.
"""
from __future__ import annotations

import argparse
import collections
import csv
import glob
import json
import os
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--minutes", type=int, default=10)
    a = ap.parse_args()
    now = time.time()

    rows = list(csv.DictReader(open(ROOT / "results" / "spend_ledger.csv")))
    total = sum(float(r["cost"]) for r in rows)
    calls = sum(int(r["n_calls"]) for r in rows)
    mins = sorted({r["utc_minute"] for r in rows})[-(a.minutes + 1):-1]
    per_min = collections.Counter()
    per_tag = collections.Counter()
    per_model = collections.Counter()
    for r in rows:
        if r["utc_minute"] in mins:
            n = int(r["n_calls"])
            per_min[r["utc_minute"]] += n
            per_tag[r["tag"]] += n
            per_model[r["model"]] += n
    print(f"spend ${total:.2f} | billed calls {calls} | UTC {time.strftime('%H:%M', time.gmtime())}")
    if mins:
        print(f"billed calls/min, last {len(mins)} full minutes: {[per_min[m] for m in mins]}  mean "
              f"{sum(per_min.values()) / len(mins):.1f}")
        print("  by stage:", dict(per_tag))
        print("  by model:", dict(per_model))

    for f in sorted(glob.glob(str(ROOT / "cache" / "llm" / "ratelimit_*.json"))):
        try:
            d = json.load(open(f))
        except Exception:
            continue
        print(f"limiter {Path(f).stem[-6:]}: factor {d.get('factor', 1):.2f}, sends in last 60 s "
              f"{sum(1 for t in d.get('starts', []) if now - t < 60)}, last change {now - d.get('changed', now):.0f} s ago")

    p = ROOT / "cache" / "llm" / "http429.log"
    if p.exists():
        c = collections.Counter()
        n_all = 0
        for line in open(p):
            parts = line.rstrip("\n").split("\t")
            if len(parts) >= 3:
                n_all += 1
                if now - float(parts[0]) < a.minutes * 60:
                    c[(parts[1], parts[2])] += 1
        print(f"429s in last {a.minutes} min by (model, key): {dict(c)} | all time: {n_all}")

    print("rows per stage file (ok / error):")
    for f in sorted(glob.glob(str(ROOT / "results" / "raw" / "main" / "*" / "*.jsonl"))):
        ok = err = 0
        with open(f) as fh:
            for line in fh:
                if '"error": null' in line:
                    ok += 1
                else:
                    err += 1
        age = now - os.path.getmtime(f)
        print(f"  {Path(f).parent.name:20s} {Path(f).stem:14s} {ok:6d} / {err:4d}   last write {age:5.0f} s ago")


if __name__ == "__main__":
    main()
