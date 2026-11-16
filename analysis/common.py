"""Shared loaders and statistics for the analysis.

Conventions used everywhere in ``analysis/``
------------------------------------------------
* **Result record.** Every reported quantity is a dict ``{"est", "ci": [lo, hi], "n", "n_clusters", ...}``;
  when it cannot be computed it is ``{"est": None, "reason": "..."}`` (see :func:`missing`). Nothing is
  imputed; missing files, victims or cells produce such records instead of errors.
* **Cluster bootstrap.** Clusters are resampled with replacement (``N_BOOT`` = 2,000 replicates, fixed seed
  derived from the quantity's name, percentile 95% CIs). A statistic is computed from per-cluster sums, so one
  replicate is a weighted sum with multinomial cluster counts as weights (fully vectorised).
  - *Pooled over victims* (a share or ratio over all victims' rows): clusters are the item / episode ids
    shared by all victims (the same episode is seen by every victim, so its rows are resampled together).
  - *Averaged over victims* (the mean of per-victim AUROCs): clusters are resampled within each victim with
    independent weights and the replicate is the mean of the victims' replicates.
* **Bootstrap p-value** (two-sided, against a null value ``h0``):
  ``p = min(1, 2 * (min(#{rep <= h0}, #{rep >= h0}) + 1) / (B + 1))``.
* **TPR at a fixed FPR.** Same rule as the gate (``memlab.defenses.gate``): an entry is flagged iff
  ``score > tau``; ``tau`` is the smallest negative score with ``share(neg > tau) <= FPR``. Entries tied with
  ``tau`` are not flagged, so the realised FPR (reported) can be below the nominal one.
* **AUROC** = P(pos > neg) + 0.5 P(pos = neg) (Mann-Whitney with ties counted 1/2); None if a class is empty.
* **Proportions at 0% or 100%.** The bootstrap interval degenerates to a point; such records get the exact
  Clopper-Pearson interval in ``ci`` (``ci_method`` says so; it ignores clustering) and keep the bootstrap
  interval in ``ci_bootstrap``. Wilson intervals are available via :func:`wilson`.
"""
from __future__ import annotations

import csv
import json
import math
import zlib
from pathlib import Path
from typing import Iterable, Optional, Sequence

import numpy as np
from scipy import stats

from memlab.config import HOSTED_VICTIMS, P1_EXTRA_VICTIMS, SHORT, is_calibration  # noqa: F401 (re-exported)

ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "results" / "processed"
ANALYSIS = ROOT / "results" / "analysis"
FIG_DIR = ROOT / "paper" / "figures"
TAB_DIR = ROOT / "paper" / "tables"
LEDGER = ROOT / "results" / "spend_ledger.csv"

N_BOOT = 2000
SEED = 20261114
ARM_SUFFIX = "_reasoning_low"
# files that a robustness arm (<run>_reasoning_low) does not write itself: its inputs come from <run>
INPUT_FILES = ("forged.jsonl", "t3_candidates.jsonl", "notes.json")
TIERS = ("T0", "T1", "T2", "T3")
EDIT_TYPES = ("E1", "E2", "E3", "E4", "E5")


# ============================================================================ loading
def base_run(run: str) -> str:
    """The run whose notes and forgeries a robustness arm used (``main_reasoning_low`` -> ``main``)."""
    return run[: -len(ARM_SUFFIX)] if run.endswith(ARM_SUFFIX) else run


def proc_path(run: str, victim: str, name: str) -> Path:
    """Path of a processed file; inputs of a robustness arm fall back to its base run. Never creates dirs."""
    p = PROCESSED / run / victim / name
    if not p.exists() and name in INPUT_FILES and base_run(run) != run:
        p = PROCESSED / base_run(run) / victim / name
    return p


def load_jsonl(run: str, victim: str, name: str) -> Optional[list]:
    """Rows of a processed JSONL file, or None if the file does not exist. Truncated last lines (a file being
    written right now) are skipped."""
    p = proc_path(run, victim, name)
    if not p.exists():
        return None
    rows = []
    with open(p) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return rows


def load_json(run: str, victim: str, name: str) -> Optional[dict]:
    p = proc_path(run, victim, name)
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text())
    except json.JSONDecodeError:
        return None


def run_victims(run: str) -> list:
    """Victim directories present for a run, in the study's order (hosted victims, then P1-only victims)."""
    d = PROCESSED / run
    if not d.exists():
        return []
    present = {p.name for p in d.iterdir() if p.is_dir()}
    order = list(HOSTED_VICTIMS) + list(P1_EXTRA_VICTIMS)
    return [v for v in order if v in present] + sorted(present - set(order))


def short(victim: str) -> str:
    return SHORT.get(victim, victim)


def out_dir(run: str) -> Path:
    d = ANALYSIS / run
    d.mkdir(parents=True, exist_ok=True)
    return d


def write_csv(path: Path, rows: Sequence[dict]) -> None:
    """Tidy CSV with the union of keys (first-seen order). Lists/dicts are JSON-encoded; None -> empty."""
    keys: list = []
    for r in rows:
        for k in r:
            if k not in keys:
                keys.append(k)
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        for r in rows:
            w.writerow({k: (json.dumps(v) if isinstance(v, (list, dict)) else ("" if v is None else v))
                        for k, v in r.items()})


def read_csv(path: Path) -> list:
    """Rows of a CSV written by :func:`write_csv`, numbers converted back to float; empty -> None."""
    if not path.exists():
        return []
    out = []
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            out.append({k: _from_cell(v) for k, v in r.items()})
    return out


def _from_cell(v: str):
    if v == "":
        return None
    try:
        return float(v)
    except ValueError:
        return v


def to_jsonable(x):
    """numpy scalars/arrays and non-finite floats -> plain JSON (NaN/inf -> None)."""
    if isinstance(x, dict):
        return {str(k): to_jsonable(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [to_jsonable(v) for v in x]
    if isinstance(x, np.ndarray):
        return to_jsonable(x.tolist())
    if isinstance(x, (np.bool_,)):
        return bool(x)
    if isinstance(x, (np.integer,)):
        return int(x)
    if isinstance(x, (float, np.floating)):
        x = float(x)
        return x if math.isfinite(x) else None
    return x


def write_json(path: Path, obj) -> None:
    path.write_text(json.dumps(to_jsonable(obj), indent=1))


# ============================================================================ result records
def missing(reason: str, **extra) -> dict:
    """Record for a quantity that cannot be computed."""
    return {"est": None, "ci": [None, None], "reason": reason, **extra}


def seed_for(*parts) -> int:
    """Deterministic seed for a named quantity (independent of computation order)."""
    return (SEED + zlib.crc32("|".join(map(str, parts)).encode())) % (2 ** 32)


def boot_weights(n_clusters: int, n_boot: int = N_BOOT, seed: int = SEED) -> np.ndarray:
    """(n_boot, n_clusters) multinomial counts: how often each cluster is drawn in each replicate."""
    rng = np.random.default_rng(seed)
    return rng.multinomial(n_clusters, np.full(n_clusters, 1.0 / n_clusters), size=n_boot).astype(float)


def boot_p(reps: np.ndarray, h0: float) -> Optional[float]:
    """Two-sided bootstrap p-value against h0 (percentile inversion, +1 correction)."""
    reps = reps[np.isfinite(reps)]
    if reps.size == 0:
        return None
    lo, hi = np.sum(reps <= h0), np.sum(reps >= h0)
    return float(min(1.0, 2 * (min(lo, hi) + 1) / (reps.size + 1)))


def summarize(est: Optional[float], reps: Optional[np.ndarray], n: int, n_clusters: int,
              h0: Optional[float] = None, **extra) -> dict:
    """Result record from a point estimate and bootstrap replicates (non-finite replicates are dropped and
    counted)."""
    if est is None or not np.isfinite(est):
        return missing(extra.pop("reason", "not estimable (empty cell)"), n=n, n_clusters=n_clusters, **extra)
    rec = {"est": float(est), "ci": [None, None], "n": int(n), "n_clusters": int(n_clusters)}
    if reps is not None:
        ok = reps[np.isfinite(reps)]
        rec["n_boot"] = int(ok.size)
        if ok.size:
            rec["ci"] = [float(np.percentile(ok, 2.5)), float(np.percentile(ok, 97.5))]
        if h0 is not None:
            rec["p"] = boot_p(ok, h0)
            rec["h0"] = h0
    rec.update(extra)
    return rec


def wilson(k: int, n: int, level: float = 0.95) -> list:
    if n == 0:
        return [None, None]
    z = stats.norm.ppf(0.5 + level / 2)
    p = k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return [max(0.0, c - h), min(1.0, c + h)]


def clopper_pearson(k: int, n: int, level: float = 0.95) -> list:
    if n == 0:
        return [None, None]
    a = (1 - level) / 2
    lo = 0.0 if k == 0 else float(stats.beta.ppf(a, k, n - k + 1))
    hi = 1.0 if k == n else float(stats.beta.ppf(1 - a, k + 1, n - k))
    return [lo, hi]


# ============================================================================ clustered means and ratios
class Clusters:
    """Cluster labels of a set of rows plus bootstrap weights. ``boot(x)`` gives the B replicate totals of a
    per-row quantity, ``total(x)`` its observed total."""

    def __init__(self, labels: Sequence, n_boot: int = N_BOOT, seed: int = SEED):
        labels = np.asarray([str(x) for x in labels])
        self.keys, self.idx = np.unique(labels, return_inverse=True) if labels.size else (np.array([]), np.array([], int))
        self.k = len(self.keys)
        self.n = len(labels)
        self.W = boot_weights(self.k, n_boot, seed) if self.k else np.zeros((n_boot, 0))

    def sums(self, x) -> np.ndarray:
        return np.bincount(self.idx, weights=np.asarray(x, float), minlength=self.k)

    def boot(self, x) -> np.ndarray:
        return self.W @ self.sums(x)

    def total(self, x) -> float:
        return float(np.sum(np.asarray(x, float)))


def _div(a, b):
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(np.asarray(b) > 0, np.asarray(a, float) / np.where(np.asarray(b) > 0, b, 1), np.nan)


def clustered_mean(values: Sequence, clusters: Sequence, h0: Optional[float] = None, seed: int = SEED,
                   proportion: bool = False, **extra) -> dict:
    """Mean of per-row values (None rows are dropped and counted) with a cluster bootstrap CI.
    ``proportion=True`` marks 0/1 data: at 0% or 100% the exact Clopper-Pearson interval is reported."""
    keep = [i for i, v in enumerate(values) if v is not None and not (isinstance(v, float) and math.isnan(v))]
    n_dropped = len(values) - len(keep)
    if not keep:
        return missing("no rows", n=0, n_dropped=n_dropped, **extra)
    x = np.array([float(values[i]) for i in keep])
    cl = Clusters([clusters[i] for i in keep], seed=seed)
    est = x.mean()
    reps = _div(cl.boot(x), cl.boot(np.ones_like(x)))
    rec = summarize(est, reps, len(x), cl.k, h0, **extra)
    if n_dropped:
        rec["n_dropped"] = n_dropped
    if proportion:
        k = int(round(x.sum()))
        rec["k"] = k
        if k in (0, len(x)):
            rec["ci_bootstrap"] = rec["ci"]
            rec["ci"] = clopper_pearson(k, len(x))
            rec["ci_method"] = "clopper-pearson (bootstrap degenerate at 0% or 100%; ignores clustering)"
    return rec


def clustered_ratio_diff(num_a, den_a, num_b, den_b, clusters, h0: Optional[float] = 0.0, seed: int = SEED,
                         relative: bool = False, **extra) -> dict:
    """Difference (or relative reduction 1 - A/B if ``relative``) of two ratios of per-row totals that share
    one cluster structure: ``sum(num_a)/sum(den_a) - sum(num_b)/sum(den_b)``."""
    cl = Clusters(clusters, seed=seed)
    if cl.k == 0:
        return missing("no rows", **extra)
    ta, tb = cl.total(den_a), cl.total(den_b)
    if ta == 0 or tb == 0:
        return missing("an arm has no rows", n_a=int(ta), n_b=int(tb), **extra)
    ra, rb = cl.total(num_a) / ta, cl.total(num_b) / tb
    ba, bb = _div(cl.boot(num_a), cl.boot(den_a)), _div(cl.boot(num_b), cl.boot(den_b))
    if relative:
        if rb == 0:
            return missing("reference rate is 0: relative reduction undefined", rate_a=ra, rate_b=rb,
                           n_a=int(ta), n_b=int(tb), **extra)
        est, reps = 1 - ra / rb, 1 - _div(ba, bb)
    else:
        est, reps = ra - rb, ba - bb
    return summarize(est, reps, int(ta + tb), cl.k, h0, rate_a=ra, rate_b=rb, n_a=int(ta), n_b=int(tb), **extra)


# ============================================================================ ROC statistics
def _grid_counts(scores, idx, grid, k):
    """(k, len(grid)) counts of scores per cluster at each grid value."""
    m = np.zeros((k, len(grid)))
    if len(scores):
        np.add.at(m, (idx, np.searchsorted(grid, scores)), 1.0)
    return m


def roc_stats(pos, neg, pos_cl=None, neg_cl=None, W: Optional[np.ndarray] = None,
              keys: Optional[Sequence] = None, fprs=(0.01, 0.05)) -> dict:
    """AUROC and TPR at the given FPRs, for the observed data and (if ``W`` and cluster labels are given) for
    every bootstrap replicate. ``keys`` fixes the cluster order of ``W``'s columns.
    Returns {"auroc": array, "tpr": {fpr: array}, "fpr_real": {fpr: array}} with one entry per replicate
    (a single entry without W)."""
    pos = np.asarray([x for x in pos], float)
    neg = np.asarray([x for x in neg], float)
    grid = np.unique(np.concatenate([pos, neg]))
    if W is None:
        k, pi, ni, Wm = 1, np.zeros(len(pos), int), np.zeros(len(neg), int), np.ones((1, 1))
    else:
        kidx = {c: i for i, c in enumerate(keys)}
        k = len(keys)
        pi = np.array([kidx[str(c)] for c in pos_cl], int)
        ni = np.array([kidx[str(c)] for c in neg_cl], int)
        Wm = W
    P = Wm @ _grid_counts(pos, pi, grid, k)        # (B, U)
    N = Wm @ _grid_counts(neg, ni, grid, k)
    Pt, Nt = P.sum(1), N.sum(1)
    n_below = np.cumsum(N, 1) - N                  # negatives strictly below each grid value
    with np.errstate(divide="ignore", invalid="ignore"):
        au = (P * (n_below + 0.5 * N)).sum(1) / (Pt * Nt)
        surv_n = (Nt[:, None] - np.cumsum(N, 1)) / Nt[:, None]    # share(neg > grid_j)
        surv_p = (Pt[:, None] - np.cumsum(P, 1)) / Pt[:, None]    # share(pos > grid_j)
    bad = (Pt == 0) | (Nt == 0)
    au[bad] = np.nan
    out = {"auroc": au, "tpr": {}, "fpr_real": {}}
    for f in fprs:
        # first grid value that is a negative score of the replicate and meets the FPR bound
        ok = (surv_n <= f + 1e-12) & (N > 0)
        j = np.argmax(ok, 1)
        has = ok.any(1) & ~bad
        rows = np.arange(len(j))
        out["tpr"][f] = np.where(has, surv_p[rows, j], np.nan)
        out["fpr_real"][f] = np.where(has, surv_n[rows, j], np.nan)
    return out


def auroc(pos: Iterable, neg: Iterable) -> Optional[float]:
    """AUROC with ties counted 1/2; None if a class is empty. Nones are ignored."""
    pos = [x for x in pos if x is not None]
    neg = [x for x in neg if x is not None]
    if not pos or not neg:
        return None
    return float(roc_stats(pos, neg)["auroc"][0])


def tpr_at_fpr(pos: Iterable, neg: Iterable, fpr: float) -> Optional[float]:
    """TPR at a fixed FPR (threshold rule in the module docstring); None if a class is empty."""
    pos = [x for x in pos if x is not None]
    neg = [x for x in neg if x is not None]
    if not pos or not neg:
        return None
    return float(roc_stats(pos, neg, fprs=(fpr,))["tpr"][fpr][0])


def roc_cell(pos, pos_cl, neg, neg_cl, seed: int = SEED, h0: Optional[float] = None, fprs=(0.01, 0.05),
             keys: Optional[Sequence] = None, W: Optional[np.ndarray] = None) -> tuple:
    """AUROC and TPR@FPR records for one cell with an episode-clustered bootstrap.

    Without ``keys``/``W`` the clusters are the labels present in the cell. With them (e.g. all episodes of a
    victim and one weight matrix per victim) several cells share the same replicates, which is what paired
    comparisons and victim averages need. Returns (records, auroc replicates or None)."""
    pp = [(x, str(c)) for x, c in zip(pos, pos_cl) if x is not None]
    nn = [(x, str(c)) for x, c in zip(neg, neg_cl) if x is not None]
    n_pos, n_neg = len(pp), len(nn)
    base = {"n_pos": n_pos, "n_neg": n_neg}
    if not pp or not nn:
        why = "no positives" if not pp else "no negatives"
        return {"auroc": missing(why, **base), **{f"tpr@{f}": missing(why, **base) for f in fprs}}, None
    present = {c for _, c in pp} | {c for _, c in nn}
    if keys is None:
        keys = sorted(present)
        W = boot_weights(len(keys), seed=seed)
    args = ([x for x, _ in pp], [x for x, _ in nn])
    obs = roc_stats(*args, fprs=fprs)
    bs = roc_stats(*args, [c for _, c in pp], [c for _, c in nn], W, keys, fprs=fprs)
    n_cl = len(present)
    out = {"auroc": summarize(obs["auroc"][0], bs["auroc"], n_pos + n_neg, n_cl, h0, **base)}
    for f in fprs:
        out[f"tpr@{f}"] = summarize(obs["tpr"][f][0], bs["tpr"][f], n_pos + n_neg, n_cl, None,
                                    fpr_realised=float(obs["fpr_real"][f][0]), **base)
    return out, bs["auroc"]


MIN_CELL_SHARE = 0.5


def victim_average(per_victim: dict, h0: Optional[float] = None) -> dict:
    """Mean over victims of per-victim estimates; ``per_victim`` maps victim -> (estimate, replicates[, n[,
    n_clusters]]). The per-victim replicates must come from resampling that victim's episodes; they are combined
    index-wise (independent within-victim resampling), and a replicate in which any victim's statistic is
    undefined is dropped (counted in n_boot). ``n`` and ``n_clusters`` are the sums over victims of the
    per-victim values when given (``n_clusters`` = episode clusters resampled), else the number of victims;
    ``n_victims`` is always reported."""
    items = {v: t for v, t in per_victim.items() if t[0] is not None and np.isfinite(t[0])}
    if not items:
        return missing("no victim with an estimate", victims=[], n_victims=0)
    # completeness guard (DECISIONS.md, 16 Nov): a victim whose cell holds less than half of the instances of
    # the largest victim cell in this average is left out, so that a victim cut off mid-stage does not enter a
    # mean over victims with a handful of instances and full weight
    dropped = []
    if all(len(t) > 2 for t in items.values()):
        top = max(t[2] for t in items.values())
        dropped = sorted(v for v, t in items.items() if t[2] < MIN_CELL_SHARE * top)
        items = {v: t for v, t in items.items() if v not in dropped}
    est = float(np.mean([t[0] for t in items.values()]))
    reps = np.mean(np.vstack([t[1] for t in items.values()]), 0)
    n = sum(t[2] for t in items.values()) if all(len(t) > 2 for t in items.values()) else len(items)
    k = sum(t[3] for t in items.values()) if all(len(t) > 3 for t in items.values()) else len(items)
    return summarize(est, reps, n, k, h0, n_victims=len(items), victims=sorted(items), excluded_incomplete=dropped,
                     per_victim={v: t[0] for v, t in items.items()},
                     per_victim_n_clusters={v: (t[3] if len(t) > 3 else None) for v, t in items.items()})


# ============================================================================ multiplicity
def holm(pvals: dict) -> dict:
    """Holm step-down adjusted p-values for {name: p}; None entries stay None and do not count."""
    avail = sorted(((p, k) for k, p in pvals.items() if p is not None))
    m = len(avail)
    out = {k: None for k in pvals}
    running = 0.0
    for i, (p, k) in enumerate(avail):
        running = max(running, min(1.0, (m - i) * p))
        out[k] = running
    return out
