"""Paper figures (vector PDF), drawn only from the CSVs written by ``analysis.hosted``.

Usage: ``python -m analysis.figures [--run main]``. For ``main`` the PDFs go to ``paper/figures/``; for any
other run (pilot, robustness arm) to ``results/analysis/<run>/figures/`` so that development data never land
in the paper. A PNG preview of each figure is written next to the CSVs for quick inspection.

Figures: (a) ``headline_auroc`` AUROC by forger tier per detector, mean over hosted victims; (b)
``p1_conflict_behaviour`` (headline P1:
memory vs each other channel, follows memory / follows other / flags, plus the forced design), ``p1_channels``
memory vs each other channel, single-claim adoption, staleness control; (c) ``p4_asr`` attack
success by condition and tier, clean accuracy; (d) ``auroc_per_victim`` per-victim small multiples of (a);
(e) ``p1_laundering`` confidence laundering.

Optional second panel of (a): ``results/analysis/local.json`` with
``{"headline": {"label": str, "tiers": [..], "detectors": {name: {"est": [..], "lo": [..], "hi": [..]}}}}``
(one value per tier, null where missing). Without that file (a) has one panel.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from .common import ANALYSIS, FIG_DIR, ROOT, TIERS, out_dir, read_csv, short

os.environ.setdefault("MPLCONFIGDIR", str(ROOT / "cache" / "matplotlib"))
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# Okabe-Ito (colour-blind safe); every detector also has its own marker and line style
DET_STYLE = {
    "V": {"color": "#D55E00", "marker": "o", "ls": "-", "label": "V (verbal)"},
    "C": {"color": "#0072B2", "marker": "s", "ls": "-", "label": "C (consistency)"},
    "R": {"color": "#009E73", "marker": "^", "ls": "-", "label": "R (re-derivation)"},
    "r_field": {"color": "#E69F00", "marker": "D", "ls": "--", "label": "missing key tokens vs re-derived note"},
    "f_trace": {"color": "#CC79A7", "marker": "v", "ls": ":", "label": "missing key tokens vs log"},
    # local-model detectors (second panel of the headline figure, from results/analysis/local.json)
    "Surprisal": {"color": "#56B4E9", "marker": "P", "ls": "-", "label": "surprisal given log"},
    "Surprisal delta": {"color": "#7B3294", "marker": "X", "ls": "--", "label": "surprisal delta"},
    "Probe P1": {"color": "#000000", "marker": "h", "ls": "-", "label": "authorship probe"},
    "Probe P2": {"color": "#000000", "marker": "*", "ls": "--", "label": "consistency probe"},
}
HOSTED_DETS = ("V", "C", "R", "r_field", "f_trace")
OUTCOME_COLORS = {"memory": "#D55E00", "other": "#0072B2", "escalate": "#999999", "rest": "#E8E8E8"}
COND_ORDER = ["none", "no_memory", "G1", "G2u", "G2s", "G2s_insider", "G1+G2s"]
TIER_COLORS = {"T0": "#56B4E9", "T2": "#0072B2", "T3": "#003049", "-": "#999999"}
WIDTH = 6.5

plt.rcParams.update({"font.size": 8, "axes.labelsize": 8, "xtick.labelsize": 7, "ytick.labelsize": 7,
                     "legend.fontsize": 7, "axes.spines.top": False, "axes.spines.right": False,
                     "pdf.fonttype": 42, "axes.grid": True, "grid.color": "#E5E5E5", "grid.linewidth": 0.5,
                     "axes.axisbelow": True})


def fig_dir(run: str) -> Path:
    d = FIG_DIR if run == "main" else ANALYSIS / run / "figures"
    d.mkdir(parents=True, exist_ok=True)
    return d


def _save(fig, run: str, name: str) -> Path:
    p = fig_dir(run) / f"{name}.pdf"
    fig.savefig(p, bbox_inches="tight")
    fig.savefig(out_dir(run) / f"fig_{name}.png", dpi=160, bbox_inches="tight")
    plt.close(fig)
    return p


def _empty(run: str, name: str, what: str) -> Path:
    """Placeholder so that the paper still compiles while data are missing."""
    fig, ax = plt.subplots(figsize=(WIDTH, 1.2))
    ax.axis("off")
    ax.text(0.5, 0.5, f"no data yet for {what} (run {run})", ha="center", va="center", color="#666666")
    return _save(fig, run, name)


def _err(est, lo, hi):
    return [[max(0.0, est - lo) if lo is not None else 0.0], [max(0.0, hi - est) if hi is not None else 0.0]]


def _ok(r, k="est"):
    return r.get(k) is not None


# ============================================================================ (a) headline
def _auroc_panel(ax, series: dict, tiers, legend: bool):
    """series: detector -> list of (est, lo, hi) per tier (None where missing)."""
    for i, (det, vals) in enumerate(series.items()):
        st = DET_STYLE.get(det, {"color": "#333333", "marker": "o", "ls": "-", "label": det})
        dx = (i - (len(series) - 1) / 2) * 0.06
        xs = [j + dx for j, v in enumerate(vals) if v and v[0] is not None]
        ys = [v[0] for v in vals if v and v[0] is not None]
        if not xs:
            continue
        lo = [v[0] - v[1] if v[1] is not None else 0 for v in vals if v and v[0] is not None]
        hi = [v[2] - v[0] if v[2] is not None else 0 for v in vals if v and v[0] is not None]
        ax.errorbar(xs, ys, yerr=[lo, hi], color=st["color"], marker=st["marker"], ls=st["ls"], lw=1.2, ms=4,
                    capsize=2, elinewidth=0.8, label=st["label"])
    ax.axhline(0.5, color="#666666", lw=0.8, ls=(0, (4, 3)))
    ax.set_xticks(range(len(tiers)), tiers)
    ax.set_xlim(-0.4, len(tiers) - 0.6)
    ax.set_ylim(0.3, 1.02)
    ax.set_xlabel("forger tier")
    ax.set_ylabel("AUROC")
    if legend:   # below the axes, so that it never covers data
        ax.legend(frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.22), ncol=3, columnspacing=1.0,
                  handlelength=2.2)


def headline(run: str) -> Path:
    rows = [r for r in read_csv(ANALYSIS / run / "detection_mean.csv")
            if r["negset"] == "same_slot" and r["edit_type"] == "all" and _ok(r, "auroc_est")]
    if not rows:
        return _empty(run, "headline_auroc", "detection")
    series = {}
    for det in HOSTED_DETS:
        vals = []
        for t in TIERS:
            m = [r for r in rows if r["detector"] == det and r["tier"] == t]
            vals.append((m[0]["auroc_est"], m[0]["auroc_lo"], m[0]["auroc_hi"]) if m else None)
        if any(vals):
            series[det] = vals
    local = ANALYSIS / "local.json"
    loc = None
    if local.exists():
        try:
            loc = json.loads(local.read_text()).get("headline")
        except (json.JSONDecodeError, AttributeError):
            loc = None
    if loc:
        fig, axes = plt.subplots(1, 2, figsize=(WIDTH, 3.0), sharey=True)
        _auroc_panel(axes[0], series, TIERS, legend=False)
        lser = {d: list(zip(v["est"], v["lo"], v["hi"])) for d, v in loc["detectors"].items()}
        _auroc_panel(axes[1], lser, loc["tiers"], legend=False)
        axes[0].set_xlabel("forger tier (hosted victims)")
        axes[1].set_xlabel(f"forger tier ({loc.get('label', 'local model')})")
        axes[1].set_ylabel("")
        handles = {}
        for ax in axes:   # one legend for both panels; a detector in both panels appears once
            for h, lab in zip(*ax.get_legend_handles_labels()):
                handles.setdefault(lab, h)
        fig.legend(handles.values(), handles.keys(), loc="lower center", ncol=4, frameon=False,
                   bbox_to_anchor=(0.5, -0.02))
        fig.tight_layout(rect=(0, 0.14, 1, 1))
    else:
        fig, ax = plt.subplots(figsize=(4.2, 3.0))
        _auroc_panel(ax, series, TIERS, legend=True)
        fig.tight_layout()
    return _save(fig, run, "headline_auroc")


def per_victim(run: str) -> Path:
    rows = [r for r in read_csv(ANALYSIS / run / "detection_cells.csv")
            if r["negset"] == "same_slot" and r["edit_type"] == "all" and _ok(r, "auroc_est")]
    victims = list(dict.fromkeys(r["victim"] for r in rows))
    if not victims:
        return _empty(run, "auroc_per_victim", "per-victim detection")
    ncol = min(3, len(victims))
    nrow = (len(victims) + ncol - 1) // ncol
    fig, axes = plt.subplots(nrow, ncol, figsize=(WIDTH, 2.1 * nrow), sharey=True, squeeze=False)
    for i, v in enumerate(victims):
        ax = axes[i // ncol][i % ncol]
        series = {}
        for det in HOSTED_DETS:
            vals = []
            for t in TIERS:
                m = [r for r in rows if r["victim"] == v and r["detector"] == det and r["tier"] == t]
                vals.append((m[0]["auroc_est"], m[0]["auroc_lo"], m[0]["auroc_hi"]) if m else None)
            if any(vals):
                series[det] = vals
        _auroc_panel(ax, series, TIERS, legend=False)
        ax.set_xlabel(f"forger tier: {short(v)}")
        if i % ncol:
            ax.set_ylabel("")
    for j in range(len(victims), nrow * ncol):
        axes[j // ncol][j % ncol].axis("off")
    handles, labels = axes[0][0].get_legend_handles_labels()
    for ax in axes.flat:
        h, lab = ax.get_legend_handles_labels()
        if len(h) > len(handles):
            handles, labels = h, lab
    fig.legend(handles, labels, loc="lower center", ncol=5, frameon=False, bbox_to_anchor=(0.5, -0.02))
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    return _save(fig, run, "auroc_per_victim")


# ============================================================================ (b) Pillar 1
def _stack(ax, labels, parts, legend_labels):
    """Horizontal stacked bars; parts: list of lists (one per segment) of shares."""
    left = [0.0] * len(labels)
    keys = list(OUTCOME_COLORS)
    for k, seg in enumerate(parts):
        ax.barh(range(len(labels)), seg, left=left, color=OUTCOME_COLORS[keys[k]], edgecolor="white", lw=1,
                height=0.7, label=legend_labels[k])
        left = [a + b for a, b in zip(left, seg)]
    ax.set_yticks(range(len(labels)), labels)
    ax.invert_yaxis()
    ax.set_xlim(0, 1)
    ax.set_xticks([0, 0.5, 1], ["0", "50", "100"])
    ax.grid(axis="y", visible=False)


def p1_channels(run: str) -> Path:
    pairs = [r for r in read_csv(ANALYSIS / run / "p1_pairs.csv") if r["group"] == "pooled"]
    mem = [r for r in pairs if r["design"] == "pair" and r["ch_a"] == "memory"]
    if not mem:
        return _empty(run, "p1_channels", "Pillar 1")
    single = [r for r in read_csv(ANALYSIS / run / "p1_single.csv") if r["group"] == "pooled"
              and r["channel"] in ("memory", "tool")]
    stale = {r["ch_b"]: r for r in pairs if r["design"] == "stale" and r["ch_a"] == "memory"}
    fig, axes = plt.subplots(1, 3, figsize=(WIDTH, 2.3), gridspec_kw={"width_ratios": [1.5, 0.7, 1.3]})

    def segs(rs):
        a = [r["follows_a_est"] or 0 for r in rs]
        b = [r["follows_b_est"] or 0 for r in rs]
        e = [r["escalate_est"] or 0 for r in rs]
        return [a, b, e, [max(0.0, 1 - x - y - z) for x, y, z in zip(a, b, e)]]

    _stack(axes[0], [f"vs {r['ch_b']} (n={int(r['n'])})" for r in mem], segs(mem),
           ["follows memory", "follows other source", "flags conflict", "distractor / no answer"])
    axes[0].set_xlabel("share of trials (%)")
    # single-claim adoption
    ax = axes[1]
    if single:
        chs = [r["channel"] for r in single]
        for i, r in enumerate(single):
            if r["follows_a_est"] is not None:
                ax.bar(i, r["follows_a_est"], color=OUTCOME_COLORS["memory" if r["channel"] == "memory" else "other"],
                       width=0.6, yerr=_err(r["follows_a_est"], r["follows_a_lo"], r["follows_a_hi"]),
                       error_kw={"lw": 0.8, "capsize": 2})
        ax.set_xticks(range(len(chs)), [f"{c}\n(n={int(r['n'])})" for c, r in zip(chs, single)])
        ax.set_ylim(0, 1.05)
        ax.set_yticks([0, 0.5, 1], ["0", "50", "100"])
        ax.set_ylabel("claim adopted, no conflict (%)")
    else:
        ax.axis("off")
        ax.text(0.5, 0.5, "no single-claim\ntrials", ha="center", va="center", color="#666666", fontsize=7)
    # staleness control: unmarked vs stale for each X
    ax = axes[2]
    xs = [x for x in ("tool", "document", "user") if x in stale]
    if xs:
        unm = {r["ch_b"]: r for r in mem}
        rows, labels = [], []
        for x in xs:
            if x in unm:
                rows.append(unm[x])
                labels.append(f"vs {x}, unmarked")
            rows.append(stale[x])
            labels.append(f"vs {x}, both earlier")
        _stack(ax, labels, segs(rows), ["follows memory", "follows other source", "flags conflict", "rest"])
        ax.set_xlabel("share of trials (%)")
    else:
        ax.axis("off")
        ax.text(0.5, 0.5, "no staleness-control\ntrials in this run", ha="center", va="center", color="#666666",
                fontsize=7)
    h, lab = axes[0].get_legend_handles_labels()
    fig.legend(h, lab, loc="lower center", ncol=4, frameon=False, bbox_to_anchor=(0.5, -0.03))
    fig.tight_layout(rect=(0, 0.08, 1, 1))
    return _save(fig, run, "p1_channels")


def _labelled_stack(ax, rows, segments):
    """Stacked horizontal bars with direct percentage labels; ``segments``: [(field, colour, text colour)]."""
    left = [0.0] * len(rows)
    for field, col, tcol in segments:
        vals = [r.get(f"{field}_est") or 0.0 for r in rows]
        ax.barh(range(len(rows)), vals, left=left, color=col, edgecolor="white", lw=1.5, height=0.72)
        for i, (x, l0) in enumerate(zip(vals, left)):
            if x >= 0.045:   # narrow segments get a smaller label
                ax.text(l0 + x / 2, i, f"{100 * x:.0f}%", ha="center", va="center", fontsize=7 if x >= 0.1 else 5.5,
                        color=tcol)
        left = [a + b for a, b in zip(left, vals)]
    rest = [max(0.0, 1 - x) for x in left]
    ax.barh(range(len(rows)), rest, left=left, color=OUTCOME_COLORS["rest"], edgecolor="white", lw=1.5, height=0.72)
    ax.set_yticks(range(len(rows)), [f"vs {r['ch_b']} (n={int(r['n'])})" for r in rows])
    ax.invert_yaxis()
    ax.set_xlim(0, 1)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1], ["0", "25", "50", "75", "100%"])
    ax.grid(False)
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", length=0)


def p1_conflict(run: str) -> Path:
    """Headline P1 picture: what the agent does with its memory note in four situations (pooled over victims).
    Left: neutral head-to-head with an option to flag. Right: the competing source is also marked as old;
    forced choice; a single source with no conflict."""
    pairs = [r for r in read_csv(ANALYSIS / run / "p1_pairs.csv") if r["group"] == "pooled" and r["ch_a"] == "memory"]
    neutral = [r for r in pairs if r["design"] == "pair"]
    forced = [r for r in pairs if r["design"] == "forced"]
    stale = [r for r in pairs if r["design"] == "stale"]
    sp = ANALYSIS / run / "p1_single.csv"
    single = [r for r in (read_csv(sp) if sp.exists() else []) if r["group"] == "pooled" and r["channel"] in ("memory", "tool")]
    if not neutral:
        return _empty(run, "p1_conflict_behaviour", "Pillar 1 head-to-head")
    seg = [("follows_a", OUTCOME_COLORS["memory"], "white"), ("follows_b", OUTCOME_COLORS["other"], "white"),
           ("escalate", "#BBBBBB", "black")]
    right = [(k, rows) for k, rows in (("stale", stale), ("forced", forced), ("single", single)) if rows]
    fig = plt.figure(figsize=(WIDTH + 0.5, 3.1))
    gs = fig.add_gridspec(max(1, len(right)), 2 if right else 1, width_ratios=[1, 1] if right else [1],
                          height_ratios=[max(2, len(r)) for _, r in right] or [1], hspace=1.3, wspace=0.62)
    ax0 = fig.add_subplot(gs[:, 0])
    _labelled_stack(ax0, neutral, seg)
    ax0.set_title("(a) note vs. a current source; flagging allowed", fontsize=7.5, loc="left")
    titles = {"stale": "(b) other source also marked as from an earlier session",
              "forced": "(c) forced choice, no option to flag",
              "single": "(d) no conflict: only one source states the value"}
    for i, (k, rows) in enumerate(right):
        ax = fig.add_subplot(gs[i, 1])
        if k == "single":
            rr = [{"ch_b": "", "n": r["n"], "follows_a_est": r["follows_a_est"] if r["channel"] == "memory" else 0.0,
                   "follows_b_est": r["follows_a_est"] if r["channel"] == "tool" else 0.0,
                   "escalate_est": r.get("escalate_est") or 0.0} for r in rows]
            _labelled_stack(ax, rr, seg)
            ax.set_yticks(range(len(rows)), [f"{'note' if r['channel'] == 'memory' else 'tool'} alone (n={int(r['n'])})" for r in rows])
        else:
            _labelled_stack(ax, rows, seg[:2] if k == "forced" else seg)
        ax.set_title(titles[k], fontsize=7.5, loc="left")
        if i < len(right) - 1:
            ax.set_xticklabels([])
    from matplotlib.patches import Patch
    handles = [Patch(color=OUTCOME_COLORS["memory"], label="acts on the memory note"),
               Patch(color=OUTCOME_COLORS["other"], label="acts on the other source"),
               Patch(color="#BBBBBB", label="declines and flags the conflict"),
               Patch(color=OUTCOME_COLORS["rest"], label="other answer")]
    fig.legend(handles=handles, loc="lower center", ncol=4, frameon=False, bbox_to_anchor=(0.5, -0.02))
    fig.subplots_adjust(left=0.13, right=0.99, top=0.92, bottom=0.17)
    return _save(fig, run, "p1_conflict_behaviour")


def p4_asr(run: str) -> Path:
    rows = [r for r in read_csv(ANALYSIS / run / "p4_asr.csv") if r["group"] == "pooled" and r["edit_type"] == "all"
            and _ok(r, "asr_est")]
    if not rows:
        return _empty(run, "p4_asr", "Pillar 4")
    clean = [r for r in read_csv(ANALYSIS / run / "p4_clean.csv") if r["group"] == "pooled" and _ok(r, "accuracy_est")]
    rows.sort(key=lambda r: (COND_ORDER.index(r["condition"]) if r["condition"] in COND_ORDER else 99, r["tier"]))
    conds = list(dict.fromkeys(r["condition"] for r in rows))
    fig, axes = plt.subplots(1, 2, figsize=(WIDTH, 2.4), gridspec_kw={"width_ratios": [2.6, 1]})
    ax = axes[0]
    tiers = list(dict.fromkeys(r["tier"] for r in rows))
    tiers.sort(key=lambda t: list(TIER_COLORS).index(t) if t in TIER_COLORS else 9)
    w = 0.8 / max(1, len(tiers))
    for i, c in enumerate(conds):
        present = [t for t in tiers if any(r["condition"] == c and r["tier"] == t for r in rows)]
        for j, t in enumerate(present):     # bars centred on the condition, whatever tiers it has
            r = [r for r in rows if r["condition"] == c and r["tier"] == t][0]
            shown = "T2" if c == "G1+G2s" else t   # G1+G2s repairs the T2 attack (stored without a tier)
            ax.bar(i + (j - (len(present) - 1) / 2) * w, r["asr_est"], width=w * 0.9,
                   color=TIER_COLORS.get(shown, "#999"), yerr=_err(r["asr_est"], r["asr_lo"], r["asr_hi"]),
                   error_kw={"lw": 0.7, "capsize": 1.5, "ecolor": "#555555"},
                   label=("no attack (entry removed)" if shown == "-" else shown))
    h, lab = ax.get_legend_handles_labels()
    uniq = dict(zip(lab, h))
    ax.legend(uniq.values(), uniq.keys(), frameon=False, ncol=len(uniq), loc="upper right")
    ax.set_xticks(range(len(conds)), [c.replace("_", "\n") for c in conds])
    ax.set_ylim(0, 1.12)
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1], ["0", "25", "50", "75", "100"])
    ax.set_ylabel("attack success (%)")
    ax.grid(axis="x", visible=False)
    ax = axes[1]
    if clean:
        clean.sort(key=lambda r: COND_ORDER.index(r["condition"]) if r["condition"] in COND_ORDER else 99)
        for i, r in enumerate(clean):
            ax.errorbar(r["accuracy_est"], i, xerr=_err(r["accuracy_est"], r["accuracy_lo"], r["accuracy_hi"]),
                        fmt="o", color="#333333", ms=4, capsize=2, elinewidth=0.8)
        ax.set_yticks(range(len(clean)), [r["condition"] for r in clean])
        ax.invert_yaxis()
        lo = min(r["accuracy_lo"] if r["accuracy_lo"] is not None else r["accuracy_est"] for r in clean)
        ax.set_xlim(max(0, lo - 0.05), 1.01)
        ax.set_xlabel("clean-store accuracy")
        ax.grid(axis="y", visible=False)
    else:
        ax.axis("off")
    fig.tight_layout()
    return _save(fig, run, "p4_asr")


# ============================================================================ (e) laundering
def laundering(run: str) -> Path:
    rows = [r for r in read_csv(ANALYSIS / run / "p1_laundering.csv") if r["group"] == "pooled"]
    cells = {(r["field"], r["quantity"]): r for r in rows}
    if not any(k[1] == "memory_hedged" for k in cells):
        return _empty(run, "p1_laundering", "confidence laundering")
    fig, axes = plt.subplots(1, 2, figsize=(4.6, 2.2))
    for ax, field, lab, scale in ((axes[0], "confidence", "stated confidence (0-100)", 1),
                                  (axes[1], "act", "acts now (%)", 100)):
        for k, ch in enumerate(("memory", "tool")):
            pts = [cells.get((field, f"{ch}_{lev}")) for lev in ("hedged", "certain")]
            if not all(p and p["est"] is not None for p in pts):
                continue
            xs = [0 + (k - 0.5) * 0.08, 1 + (k - 0.5) * 0.08]
            ys = [p["est"] * scale for p in pts]
            err = [[(p["est"] - p["lo"]) * scale for p in pts], [(p["hi"] - p["est"]) * scale for p in pts]]
            ax.errorbar(xs, ys, yerr=err, color=OUTCOME_COLORS["memory" if ch == "memory" else "other"],
                        marker="o" if ch == "memory" else "s", ms=4, lw=1.2, capsize=2, label=f"in {ch} note"
                        if ch == "memory" else "in tool output")
        ax.set_xticks([0, 1], ["hedged", "certain"])
        ax.set_xlim(-0.4, 1.4)
        ax.set_ylim(0, 105)
        ax.set_ylabel(lab)
    axes[0].legend(frameon=False, loc="upper left")
    fig.tight_layout()
    return _save(fig, run, "p1_laundering")


def main(argv=None) -> list:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--run", default="main")
    a = ap.parse_args(argv)
    paths = [f(a.run) for f in (headline, p1_conflict, p1_channels, p4_asr, per_victim, laundering)]
    print(f"[figures] {len(paths)} figures -> {fig_dir(a.run)}")
    return paths


if __name__ == "__main__":
    main()
