"""Side-by-side comparison of a run with its reasoning-on robustness arm on the common items.

Usage: ``python -m analysis.compare [--a main] [--b main_reasoning_low]``. Restricted to (victim, item) units
present in both runs: P1 memory-vs-tool trials, detector entries (V, C, R at T0, T2, T3, same-slot negatives),
and P4 ``none`` answers. Each quantity is reported for both runs and as the difference b - a with a paired
cluster bootstrap (items / episodes resampled once for both runs). Writes
``results/analysis/<b>/comparison_vs_<a>.json`` and ``.csv``.
"""
from __future__ import annotations

import argparse

from memlab.config import HOSTED_VICTIMS

from . import detection, p1, p4
from .common import (boot_weights, clustered_mean, clustered_ratio_diff, missing, out_dir, seed_for,
                     summarize, victim_average, write_csv, write_json)
from .hosted import flat

DET_TIERS = ("T0", "T2", "T3")


def _p1(run_a: str, run_b: str) -> list:
    ra = {(r["victim"], r["episode_id"]): r for r in p1.select(p1.load_p1(run_a)[0], "pair", "memory", "tool")}
    rb = {(r["victim"], r["episode_id"]): r for r in p1.select(p1.load_p1(run_b)[0], "pair", "memory", "tool")}
    common = sorted(set(ra) & set(rb))
    out = []
    for g in ["pooled"] + sorted({k[0] for k in common}):
        ks = [k for k in common if g == "pooled" or k[0] == g]
        if not ks:
            continue
        net = lambda r: float(r["followed"] == "memory") - float(r["followed"] == "tool")  # noqa: E731
        cl = [k[1] for k in ks]
        out.append({"quantity": "P1 net memory - tool", "group": g,
                    "a": clustered_mean([net(ra[k]) for k in ks], cl, seed=seed_for("cmp1a", g)),
                    "b": clustered_mean([net(rb[k]) for k in ks], cl, seed=seed_for("cmp1b", g)),
                    "diff": clustered_mean([net(rb[k]) - net(ra[k]) for k in ks], cl, h0=0.0, seed=seed_for("cmp1d", g))})
    return out or [{"quantity": "P1 net memory - tool", "group": "pooled", "a": missing("no common items"),
                    "b": missing("no common items"), "diff": missing("no common items")}]


def _detection(run_a: str, run_b: str) -> list:
    out, per = [], {}
    for v in HOSTED_VICTIMS:
        da, db = detection.load_victim(run_a, v), detection.load_victim(run_b, v)
        for det in ("V", "C", "R"):
            ea, eb = da["entries"].get(det), db["entries"].get(det)
            if not ea or not eb:
                continue
            common = {e["episode_id"] for e in ea} & {e["episode_id"] for e in eb}
            if not common:
                continue
            keys = sorted(common)
            W = boot_weights(len(keys), seed=seed_for("cmpdet", v, det))
            for tier in DET_TIERS:
                ca, ra = detection._roc(*detection.cell_sets(ea, tier, None, "same_slot", common), keys, W)
                cb, rb = detection._roc(*detection.cell_sets(eb, tier, None, "same_slot", common), keys, W)
                a, b = ca["auroc"], cb["auroc"]
                if a["est"] is None or b["est"] is None:
                    diff = missing("a cell is empty in one run")
                else:
                    diff = summarize(b["est"] - a["est"], rb - ra, a["n"] + b["n"], len(keys), 0.0)
                    per.setdefault((det, tier), {})[v] = (b["est"] - a["est"], rb - ra)
                out.append({"quantity": f"AUROC {det} {tier}", "group": v, "a": a, "b": b, "diff": diff})
    for (det, tier), pv in sorted(per.items()):
        out.append({"quantity": f"AUROC {det} {tier}", "group": "mean over victims", "a": None, "b": None,
                    "diff": victim_average(pv, h0=0.0)})
    return out


def _p4(run_a: str, run_b: str) -> list:
    def index(run):
        return {(r["victim"], r["episode_id"], r["store"], r["q_edit"]): r for r in p4.load_p4(run)
                if r["condition"] == "none"}
    ia, ib = index(run_a), index(run_b)
    common = sorted(set(ia) & set(ib))
    out = []
    for name, sel, field in [(f"ASR none {t}", lambda k, r, t=t: r["tier"] == t and r["is_target"], "attacked")
                             for t in ("T0", "T2", "T3")] + [("clean accuracy none", lambda k, r: k[2] == "clean", "correct")]:
        ks = [k for k in common if sel(k, ia[k])]
        if not ks:
            continue
        # primary rule for ASR (unparsed = failed); accuracy drops unparsed in both runs
        if field == "correct":
            ks = [k for k in ks if ia[k]["correct"] is not None and ib[k]["correct"] is not None]
        val = lambda r: float(bool(r[field]))  # noqa: E731
        n = len(ks)
        cl = [k[1] for k in ks] * 2
        rec = clustered_ratio_diff([val(ib[k]) for k in ks] + [0.0] * n, [1.0] * n + [0.0] * n,
                                   [0.0] * n + [val(ia[k]) for k in ks], [0.0] * n + [1.0] * n, cl,
                                   seed=seed_for("cmp4", name))
        out.append({"quantity": name, "group": "pooled",
                    "a": clustered_mean([val(ia[k]) for k in ks], [k[1] for k in ks], proportion=True,
                                        seed=seed_for("cmp4a", name)),
                    "b": clustered_mean([val(ib[k]) for k in ks], [k[1] for k in ks], proportion=True,
                                        seed=seed_for("cmp4b", name)),
                    "diff": rec})
    return out


def compare(run_a: str, run_b: str) -> dict:
    res = {"a": run_a, "b": run_b, "note": "differences are b - a on units present in both runs",
           "rows": _p1(run_a, run_b) + _detection(run_a, run_b) + _p4(run_a, run_b)}
    d = out_dir(run_b)
    write_json(d / f"comparison_vs_{run_a}.json", res)
    write_csv(d / f"comparison_vs_{run_a}.csv",
              [{"quantity": r["quantity"], "group": r["group"], **flat(r["a"] or {}, "a_"), **flat(r["b"] or {}, "b_"),
                **flat(r["diff"], "diff_")} for r in res["rows"]])
    return res


def main(argv=None) -> dict:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--a", default="main")
    ap.add_argument("--b", default=None, help="default: <a>_reasoning_low")
    x = ap.parse_args(argv)
    res = compare(x.a, x.b or x.a + "_reasoning_low")
    print(f"[compare] {res['a']} vs {res['b']}: {len(res['rows'])} quantities")
    for r in res["rows"]:
        d = r["diff"]
        if r["group"] in ("pooled", "mean over victims"):
            print(f"  {r['quantity']:24s} {r['group']:18s} diff={d.get('est')} ci={d.get('ci')}")
    return res


if __name__ == "__main__":
    main()
