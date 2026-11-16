"""Short machine-written summary of one analysis run: ``results/analysis/<run>/SUMMARY.md``.

Usage: ``python -m analysis.summary [--run main]`` (also called by ``analysis.reproduce``). Reads only
``hosted.json``. Percentages are of trials / entries / stores; CIs are 95% cluster-bootstrap intervals.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from .common import ANALYSIS, TIERS, short


def _pct(r, nd=1) -> str:
    if not isinstance(r, dict) or r.get("est") is None:
        return "n/a" + (f" ({r['reason']})" if isinstance(r, dict) and r.get("reason") else "")
    lo, hi = r.get("ci") or [None, None]
    ci = f" [{100 * lo:.{nd}f}, {100 * hi:.{nd}f}]" if lo is not None and hi is not None else ""
    return f"{100 * r['est']:.{nd}f}%{ci} (n={r.get('n')})"


def _num(r, nd=2) -> str:
    if not isinstance(r, dict) or r.get("est") is None:
        return "n/a"
    lo, hi = r.get("ci") or [None, None]
    ci = f" [{lo:.{nd}f}, {hi:.{nd}f}]" if lo is not None and hi is not None else ""
    return f"{r['est']:.{nd}f}{ci}"


def build(res: dict) -> str:
    run = res.get("run", "?")
    L = [f"# Analysis summary: run `{run}`", "",
         "Machine-written by `analysis/summary.py` from `hosted.json`. CIs: 95% cluster bootstrap. "
         "Pilot runs are development data only.", "", "## Primary estimands (Holm over the four)", ""]
    fmt = {"P1_self_trust_premium": lambda r: _num({**r, "est": r["est"] * 100 if r["est"] is not None else None,
                                                    "ci": [x * 100 if x is not None else None for x in r["ci"]]}, 1) + " pp",
           "P4_gate_effectiveness": lambda r: _num({**r, "est": r["est"] * 100 if r["est"] is not None else None,
                                                    "ci": [x * 100 if x is not None else None for x in r["ci"]]}, 1) + " %"}
    for k, r in (res.get("primary") or {}).items():
        val = fmt.get(k, lambda r: _num(r, 3))(r)
        extra = f", selected {r['selected_detector']}" if r.get("selected_detector") else ""
        p = "n/a" if r.get("p") is None else f"{r['p']:.4f}"
        ph = "n/a" if r.get("p_holm") is None else f"{r['p_holm']:.4f}"
        L.append(f"- **{k}**: {val}, n={r.get('n')}, n_clusters={r.get('n_clusters')}, p={p}, Holm p={ph}, "
                 f"supported={r.get('supported')}{extra}" + (f" -- {r['reason']}" if r.get("reason") else ""))
    P1, DT, P4 = res.get("p1", {}), res.get("detection", {}), res.get("p4", {})
    L += ["", "## Main secondary numbers", ""]
    # detection
    mean = {(r["detector"], r["tier"]): r["auroc"] for r in DT.get("mean_over_victims", [])
            if r["negset"] == "same_slot" and r["edit_type"] == "all"}
    for d in ("V", "C", "R"):
        L.append(f"- AUROC {d} (mean over victims, same-slot negatives): " +
                 "; ".join(f"{t} {_num(mean.get((d, t)))}" for t in TIERS))
    fl = {(r["detector"], r["store"]): r["flat_rate"] for r in DT.get("flat_audit", []) if r["group"] == "pooled"}
    for d in ("V", "C"):
        L.append(f"- Flat audits {d} (all 7 entries same score): clean {_pct(fl.get((d, 'clean')))}; "
                 f"attacked T2 {_pct(fl.get((d, 'T2')))}")
    rk = {(r["detector"], r["tier"]): r for r in DT.get("within_store_rank", []) if r["group"] == "pooled"}
    for d in ("V", "C"):
        r = rk.get((d, "T2"), {})
        L.append(f"- Forged entry most suspicious in its store, {d} T2: strictly {_pct(r.get('forged_strictly_highest'))}, "
                 f"incl. ties {_pct(r.get('forged_highest_incl_ties'))} (chance 14.3%)")
    rd = {r["group"]: r["p_altered_ge_50"] for r in DT.get("r_genuine_disagreement", [])}
    L.append(f"- R false positives (untouched notes vs re-derivation, p_altered >= 50): {_pct(rd.get('pooled'))}")
    negs = [f"{short(r['victim'])} {r['kind']} {_num(r['auroc'])}" for r in DT.get("matched_negatives", [])
            if r["kind"] != "all"]
    L.append("- Matched negatives (AUROC of V, replaced slot vs genuine): " + ("; ".join(negs) or "n/a"))
    afc = {r["tier"]: r["accuracy"] for r in DT.get("afc", []) if r["group"] == "pooled" and r["edit_type"] == "all"}
    L.append("- 2AFC accuracy (pooled): " + "; ".join(f"{t} {_pct(afc.get(t))}" for t in TIERS))
    # P4
    asr = [r for r in P4.get("asr", []) if r["group"] == "pooled" and r["edit_type"] == "all"]
    L.append("- ASR (pooled, unparsed = failed): " + ("; ".join(f"{r['condition']} {r['tier']} {_pct(r['asr'])}"
                                                               for r in asr) or "n/a"))
    cl = [r for r in P4.get("clean", []) if r["group"] == "pooled"]
    L.append("- Clean-store accuracy: " + ("; ".join(f"{r['condition']} {_pct(r['accuracy'])}" for r in cl) or "n/a"))
    # P1
    mt = [r for r in P1.get("pairs", []) if r["group"] == "pooled" and r["design"] == "pair"
          and r["ch_a"] == "memory" and r["ch_b"] == "tool"]
    if mt:
        r = mt[0]
        L.append(f"- P1 memory vs tool (n={r['n']}): follows memory {_pct(r['follows_a'])}, follows tool "
                 f"{_pct(r['follows_b'])}, flags conflict {_pct(r['escalate'])}")
    else:
        L.append("- P1 memory vs tool: n/a")
    for r in P1.get("pairs", []):
        if r["group"] == "pooled" and r["design"] == "pair" and r["ch_a"] == "memory" and r["ch_b"] != "tool":
            L.append(f"  - vs {r['ch_b']}: memory {_pct(r['follows_a'], 0)}, other {_pct(r['follows_b'], 0)}, "
                     f"flag {_pct(r['escalate'], 0)}")
    sg = [r for r in P1.get("single", []) if r["group"] == "pooled"]
    d = (P1.get("single_memory_minus_tool") or {}).get("pooled")
    L.append("- P1 single source (no conflict) adoption: " + ("; ".join(f"{r['channel']} {_pct(r['follows_a'])}" for r in sg)
                                                             or "n/a") + f"; memory - tool {_pct(d)}")
    lau = ((P1.get("laundering") or {}).get("pooled") or {}).get("confidence")
    L.append(f"- Confidence laundering (stated confidence, points): {_num(lau, 1)}")
    tot = [r for r in (res.get("cost") or {}).get("by_stage", []) if r.get("stage") == "total"]
    L.append(f"- Total cost in ledger: {tot[0]['cost']:.2f} credits, {int(tot[0]['n_calls']):,} calls" if tot else
             "- Total cost: n/a")
    return "\n".join(L) + "\n"


def main(argv=None) -> Path:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--run", default="main")
    a = ap.parse_args(argv)
    src = ANALYSIS / a.run / "hosted.json"
    res = json.loads(src.read_text()) if src.exists() else {"run": a.run}
    out = ANALYSIS / a.run / "SUMMARY.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(build(res))
    print(f"[summary] -> {out}")
    return out


if __name__ == "__main__":
    main()
