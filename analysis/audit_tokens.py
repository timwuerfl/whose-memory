"""Token cost of the store-level audits, from the raw job rows.

Reads ``results/raw/<run>/<victim>/hosted_detect.jsonl`` and writes
``results/processed/<run>/audit_tokens.json``: mean input and output tokens per call for each part of the
detector stage (v: verbal audit without logs, c: consistency audit with the seven session logs, r: judge calls),
pooled over victims and per victim. ``analysis/numbers.py`` turns the pooled means into macros. The file is
committed with the processed data, so ``analysis.reproduce`` does not need the raw rows.

Usage: ``python -m analysis.audit_tokens [--run main]``
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict

from .common import PROCESSED, ROOT


def audit_tokens(run: str = "main") -> dict:
    agg: dict = defaultdict(lambda: [0, 0, 0])
    for f in sorted((ROOT / "results" / "raw" / run).glob("*/hosted_detect.jsonl")):
        victim = f.parent.name
        for line in f.open():
            r = json.loads(line)
            u = r.get("usage") or {}
            if r.get("error") or r.get("cached") or not u.get("input_tokens"):
                continue
            part = (r.get("meta") or {}).get("part") or r["job_id"].split("|")[3]
            for key in (("pooled", part), (victim, part)):
                a = agg[key]
                a[0] += 1
                a[1] += u["input_tokens"]
                a[2] += u.get("output_tokens") or 0
    out: dict = {}
    for (g, part), (n, i, o) in sorted(agg.items()):
        out.setdefault(g, {})[part] = {"calls": n, "mean_input_tokens": i / n, "mean_output_tokens": o / n}
    dst = PROCESSED / run / "audit_tokens.json"
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(json.dumps(out, indent=1))
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", default="main")
    for part, v in audit_tokens(ap.parse_args().run).get("pooled", {}).items():
        print(f"{part}: {v['calls']} calls, {v['mean_input_tokens']:.0f} in, {v['mean_output_tokens']:.0f} out")
