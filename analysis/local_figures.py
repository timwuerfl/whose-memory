"""Figures for the local-victim analysis (vector PDFs, no in-figure titles, colour-blind-safe Okabe-Ito colours).

    python -m analysis.local_figures [--json results/analysis/local.json] [--out paper/figures]

(a) ``local_auroc_by_tier.pdf``  AUROC by tier for the main local detectors (CIs, chance line);
    ``draw_local_panel(ax, local_json)`` draws the same panel into a caller's axes.
(b) ``local_transfer.pdf``       selection rule x detector: AUROC change relative to T2r.
(c) ``local_probe_layers.pdf``   probe AUROC by layer with shuffled-label and bag-of-words controls.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / "cache" / "mpl"))

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

TEXT_WIDTH = 6.5
OKABE_ITO = ["#0072B2", "#E69F00", "#009E73", "#D55E00", "#CC79A7", "#56B4E9", "#F0E442", "#000000"]
MARKERS = ["o", "s", "^", "D", "v", "P", "X", "*"]
TIER_ORDER = ("T0", "T1", "T2", "T2r", "T3", "T4s", "T4d", "T4c", "T4p")
# main local detectors in panel (a); probes are the split-half versions, valid at every tier including T4p
PANEL_DETECTORS = (("s_trace_mean", "Surprisal"), ("s_delta", "Surprisal delta"), ("v", "Verbal (logit)"),
                   ("c", "Consistency (logit)"), ("P1h", "Probe P1 (self)"), ("P2h", "Probe P2 (consistency)"))
SHORT = {"s_trace_mean": "Surprisal", "s_blind_mean": "Surprisal\n(no trace)", "s_delta": "Surprisal\ndelta",
         "c": "Consistency", "v": "Verbal", "P1h": "Probe P1", "P2h": "Probe P2", "ppl_gpt2": "GPT-2",
         "ppl_small": "Qwen-0.8B", "len_chars": "Length"}

RC = {"font.size": 8, "axes.labelsize": 8, "xtick.labelsize": 7, "ytick.labelsize": 7, "legend.fontsize": 7,
      "axes.spines.top": False, "axes.spines.right": False, "pdf.fonttype": 42, "ps.fonttype": 42,
      "axes.linewidth": 0.6, "lines.linewidth": 1.0}


def _load(p):
    if isinstance(p, dict):
        return p
    return json.loads(Path(p).read_text())


def draw_local_panel(ax, local_json, detectors=PANEL_DETECTORS, tiers=TIER_ORDER, subset="all", negset="matched",
                     legend=True):
    """AUROC (with 95% CI) by tier for the main local detectors, on ``ax``. ``local_json``: dict or path.
    Missing cells are skipped (never imputed). Returns the legend handles."""
    J = _load(local_json)
    rows = J.get("detectors", [])
    look = {(r["detector"], r["tier"]): r for r in rows if r.get("subset") == subset and r.get("negset") == negset}
    x = np.arange(len(tiers))
    k = len(detectors)
    width = 0.8
    off = (np.arange(k) - (k - 1) / 2) * (width / k)
    handles = []
    ymin = 0.5
    for i, (det, label) in enumerate(detectors):
        xs, ys, lo, hi = [], [], [], []
        for j, t in enumerate(tiers):
            r = look.get((det, t))
            if not r or r.get("auroc") is None:
                continue
            xs.append(x[j] + off[i])
            ys.append(r["auroc"])
            lo.append(r["auroc"] - (r["ci_lo"] if r.get("ci_lo") is not None else r["auroc"]))
            hi.append((r["ci_hi"] if r.get("ci_hi") is not None else r["auroc"]) - r["auroc"])
            if r.get("ci_lo") is not None:
                ymin = min(ymin, r["ci_lo"])
        if not xs:
            continue
        h = ax.errorbar(xs, ys, yerr=[lo, hi], fmt=MARKERS[i % len(MARKERS)], color=OKABE_ITO[i % len(OKABE_ITO)],
                        ms=3.5, elinewidth=0.8, capsize=0, label=label, mec="white", mew=0.3)
        for a in [h.lines[0]] + list(h.lines[2]):
            a.set_clip_on(False)
        handles.append(h)
    ax.axhline(0.5, color="0.5", lw=0.7, ls="--", zorder=0)
    for j in range(len(tiers)):
        if j % 2:
            ax.axvspan(j - 0.5, j + 0.5, color="0.94", zorder=-1, lw=0)
    ax.set_xticks(x)
    ax.set_xticklabels(tiers)
    ax.set_xlim(-0.5, len(tiers) - 0.5)
    ax.set_ylim(max(0.0, min(0.3, np.floor(ymin * 10) / 10)), 1.0)
    ax.set_ylabel("AUROC (forged vs genuine)")
    ax.set_xlabel("Forger tier")
    if legend and handles:
        ax.legend(handles=handles, ncol=min(6, len(handles)), frameon=False, loc="lower center",
                  bbox_to_anchor=(0.5, 1.0), handletextpad=0.3, columnspacing=1.0)
    return handles


def fig_auroc(J, out: Path):
    with plt.rc_context(RC):
        fig, ax = plt.subplots(figsize=(TEXT_WIDTH, 2.8))
        draw_local_panel(ax, J)
        fig.tight_layout()
        fig.savefig(out / "local_auroc_by_tier.pdf")
        plt.close(fig)


def fig_transfer(J, out: Path):
    rows = J.get("transfer", [])
    rules = [r for r in ("T3", "T4s", "T4d", "T4c", "T4p")]
    dets = []
    for r in rows:
        if r["detector"] not in dets:
            dets.append(r["detector"])
    if not dets:
        dets = list(SHORT)
    M = np.full((len(rules), len(dets)), np.nan)
    for r in rows:
        if r.get("auroc_change") is not None and r["rule"] in rules:
            M[rules.index(r["rule"]), dets.index(r["detector"])] = r["auroc_change"]
    lim = np.nanmax(np.abs(M)) if np.isfinite(M).any() else 0.1
    lim = max(lim, 0.05)
    with plt.rc_context(RC):
        fig, ax = plt.subplots(figsize=(TEXT_WIDTH, 2.4))
        cmap = plt.get_cmap("PuOr_r").with_extremes(bad="0.9")
        im = ax.imshow(np.ma.masked_invalid(M), cmap=cmap, vmin=-lim, vmax=lim, aspect="auto")
        for i in range(len(rules)):
            for j in range(len(dets)):
                v = M[i, j]
                txt = "n/a" if not np.isfinite(v) else f"{v:+.2f}"
                col = "white" if np.isfinite(v) and abs(v) > 0.6 * lim else "black"
                ax.text(j, i, txt, ha="center", va="center", fontsize=6.5, color=col)
        ax.set_xticks(range(len(dets)))
        ax.set_xticklabels([SHORT.get(d, d) for d in dets], fontsize=6.5)
        ax.set_yticks(range(len(rules)))
        ax.set_yticklabels(rules)
        ax.set_ylabel("Selection rule")
        for s in ax.spines.values():
            s.set_visible(False)
        cb = fig.colorbar(im, ax=ax, fraction=0.03, pad=0.02)
        cb.set_label("AUROC change vs T2r", fontsize=7)
        cb.ax.tick_params(labelsize=6.5)
        fig.tight_layout()
        fig.savefig(out / "local_transfer.pdf")
        plt.close(fig)


def fig_probe_layers(J, out: Path):
    pr = J.get("probes", {})
    tasks = (("P1", "P1: own vs other-model notes"), ("P2", "P2: genuine vs forged (T0-T2)"))
    with plt.rc_context(RC):
        fig, axes = plt.subplots(1, 2, figsize=(TEXT_WIDTH, 2.4), sharey=True)
        for ax, (task, ylabel) in zip(axes, tasks):
            for ci, (which, lab, ls) in enumerate((("trace", "with trace", "-"), ("blind", "no trace", "--"))):
                s = pr.get("main", {}).get(f"{task}|{which}", {})
                bl = s.get("by_layer") or {}
                if not bl:
                    continue
                layers = list(bl)
                xs = np.arange(len(layers))
                y = np.array([bl[l].get("auroc") if bl[l].get("auroc") is not None else np.nan for l in layers], float)
                lo = np.array([bl[l].get("ci_lo") if bl[l].get("ci_lo") is not None else np.nan for l in layers], float)
                hi = np.array([bl[l].get("ci_hi") if bl[l].get("ci_hi") is not None else np.nan for l in layers], float)
                col = OKABE_ITO[ci]
                ax.plot(xs, y, ls=ls, marker=MARKERS[ci], ms=3.5, color=col, label=f"probe, {lab}")
                ax.fill_between(xs, lo, hi, color=col, alpha=0.15, lw=0)
                sh = s.get("shuffled") or {}
                sm = np.array([(sh.get(l) or {}).get("mean") if (sh.get(l) or {}).get("mean") is not None else np.nan
                               for l in layers], float)
                smin = np.array([(sh.get(l) or {}).get("min") if (sh.get(l) or {}).get("min") is not None else np.nan
                                 for l in layers], float)
                smax = np.array([(sh.get(l) or {}).get("max") if (sh.get(l) or {}).get("max") is not None else np.nan
                                 for l in layers], float)
                if np.isfinite(sm).any():
                    ax.errorbar(xs + 0.08 * (ci * 2 - 1), sm, yerr=[sm - smin, smax - sm], fmt=MARKERS[ci], mfc="none",
                                color="0.45", ms=3, elinewidth=0.7, ls="none",
                                label="shuffled labels (mean, range)" if ci == 0 else None)
                ax.set_xticks(xs)
                ax.set_xticklabels(layers)
            b = (pr.get("bow", {}).get(task) or {}).get("pooled") or {}
            if b.get("auroc") is not None:
                ax.axhline(b["auroc"], color=OKABE_ITO[3], lw=1.0, ls=":", label="bag-of-words + length")
                if b.get("ci_lo") is not None:
                    ax.axhspan(b["ci_lo"], b["ci_hi"], color=OKABE_ITO[3], alpha=0.08, lw=0)
            ax.axhline(0.5, color="0.5", lw=0.6, ls="--", zorder=0)
            ax.set_xlabel("Layer")
            ax.set_ylabel(f"AUROC ({ylabel})" if task == "P1" else ylabel)
            ax.set_ylim(0.0, 1.02)
        axes[0].set_ylabel("Out-of-fold AUROC")
        axes[0].text(0.02, 0.04, tasks[0][1], transform=axes[0].transAxes, fontsize=7)
        axes[1].text(0.02, 0.04, tasks[1][1], transform=axes[1].transAxes, fontsize=7)
        axes[1].set_ylabel("")
        h, l = axes[0].get_legend_handles_labels()
        if h:
            fig.legend(h, l, ncol=4, frameon=False, loc="upper center", bbox_to_anchor=(0.5, 1.02))
        fig.tight_layout(rect=(0, 0, 1, 0.9))
        fig.savefig(out / "local_probe_layers.pdf")
        plt.close(fig)


def main(json_path=ROOT / "results" / "analysis" / "local.json", out=ROOT / "paper" / "figures"):
    J = _load(json_path)
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    fig_auroc(J, out)
    fig_transfer(J, out)
    fig_probe_layers(J, out)
    print(f"[local_figures] wrote 3 PDFs to {out}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", default=str(ROOT / "results" / "analysis" / "local.json"))
    ap.add_argument("--out", default=str(ROOT / "paper" / "figures"))
    a = ap.parse_args()
    sys.exit(main(a.json, a.out))
