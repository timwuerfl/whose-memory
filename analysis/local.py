"""Local-victim analysis (PREREGISTRATION.md §6; local counterparts of §1 H3/H4 and §3 item 3).

Reads the output of ``experiments/local_pipeline.py`` (``--dir``, default ``results/raw/local``) and its
activation directory (``config.json: acts_dir``) and writes ``<out>/local.json`` plus tidy CSVs
``<out>/local_*.csv``. Model-free: numpy / scikit-learn on saved arrays only.

    python -m analysis.local [--dir results/raw/local] [--out results/analysis] [--select-t4p]

``--select-t4p`` first computes the attacker's self-authorship probe scores for every pool candidate and
appends the T4p selection to ``<dir>/selected.jsonl`` (``pipeline.append_selection``); then it runs the
full analysis. Without the flag nothing is written to ``--dir``.

Design (decided before looking at real-run data; see also ``DESIGN`` in the JSON output)
-------------------------------------------------------------------------------------------
* Positives: VALID forged target notes of a tier (T0/T1/T2 from the registry; pool tiers from
  ``selected.jsonl``). Negatives: "matched" = genuine notes of the same slots (instances that have a
  positive in this comparison); "all_genuine" = every genuine note in the registry. (The hosted third
  negative set, genuine entries inside attacked stores, does not exist locally: single-entry scoring.)
* Instance subsets: "all" = every instance with a valid positive for that tier; "common" = instances with a
  valid positive for every tier present (so tiers are compared on identical instances). In the local design
  every instance is one of the 2 pre-assigned edit types per episode, so "all" for T0-T2 already is the
  pool-instance set; the two subsets differ only where a pool tier has no valid candidate (or a forgery is
  invalid).
* Orientation (a priori, from the construct; higher = more likely forged), see ``DETECTORS``.
* CIs: percentile, episode-clustered bootstrap, 2,000 replicates, one resampling matrix shared by every
  comparison (so differences between detectors/tiers are paired), fixed seed.
* Probes: L2 logistic regression (standardised on the training fold only, class_weight balanced) on
  mean-pooled residual activations over the note tokens. Leave-one-family-out. Within the training
  families, (layer, C) are chosen by fitting on the non-calibration episodes and scoring AUROC on the
  calibration episodes (``is_calibration``); the chosen model is refitted on all training-family episodes.
  If the calibration split of the training families lacks a class, a fixed default (layer index
  ``len(layers)//2``, C = ``DEFAULT_C``) is used and the fold records why.
* T4p: episodes are split by ``stable_hash("t4p-half", episode_id) % 2`` into halves A/B. The attacker's
  P1-type probe (with-trace mean activations; (layer, C) chosen on its own half's calibration episodes)
  is trained on one half and scores the candidates of the other half; then the halves swap. The defender
  probes used against T4p (``P1h``/``P2h``) are trained and evaluated leave-one-family-out *within* one
  half, so no episode used by the attacker is ever used to train or evaluate the defender probe that
  judges that attacker's selections. The full-sample LOFO probes ``P1``/``P2`` are reported for all tiers
  except T4p (null, leakage).
"""
from __future__ import annotations

import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(_v, "2")   # the machine is shared: at most 2 BLAS threads

import argparse  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402
import sys  # noqa: E402
import warnings  # noqa: E402
from collections import OrderedDict, defaultdict  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from memlab.config import is_calibration  # noqa: E402
from memlab.local import pipeline as P  # noqa: E402
from memlab.schema import EDIT_TYPES, stable_hash  # noqa: E402

DEFAULT_DIR = ROOT / "results" / "raw" / "local"
DEFAULT_OUT = ROOT / "results" / "analysis"
N_BOOT = 2000
SEED = 20261114
N_SHUFFLES = 5
CS = (1e-4, 1e-3, 1e-2, 1e-1, 1.0)
DEFAULT_C = 1e-2
MAX_ITER = 2000

FORGED_TIERS = ("T0", "T1", "T2")
POOL_TIERS = ("T2r", "T3", "T4s", "T4d", "T4c", "T4p")
TIERS = FORGED_TIERS + POOL_TIERS
RULES = ("T3", "T4s", "T4d", "T4c", "T4p")          # selection rules compared with T2r
T4_TIERS = ("T4s", "T4d", "T4c", "T4p")

# name -> (column, orientation, group, label). Orientation fixed a priori: higher oriented score = more
# likely forged.
#   surprisal / perplexity: text the victim did not write (or that contradicts the trace) is less expected
#     -> +1.  s_delta = s(note|trace) - s(note|no trace): a genuine note is made *more* expected by its
#     trace (very negative delta); forged content gains less -> +1.
#   v, c are P("Yes") to "did you write this" / "is this consistent with the session" -> -1.
#   P1 outputs the logit of "other-model note" (not self) -> +1; P2 the logit of "forged" -> +1.
#   bag-of-words baselines are trained like P1/P2 -> +1. Length: +1 (a confound check; values far from 0.5
#     in either direction indicate a length difference).
DETECTORS = OrderedDict([
    ("s_trace_mean", ("s_trace_mean", +1, "style", "Surprisal | trace (mean)")),
    ("s_trace_max", ("s_trace_max", +1, "style", "Surprisal | trace (max)")),
    ("s_blind_mean", ("s_blind_mean", +1, "style", "Surprisal | no trace (mean)")),
    ("s_delta", ("s_delta", +1, "trace", "Surprisal delta")),
    ("ppl_gpt2", ("gpt2_mean", +1, "external", "GPT-2 surprisal")),
    ("ppl_small", ("small_mean", +1, "external", "Qwen3.5-0.8B surprisal")),
    ("ppl_small_trace", ("small_trace_mean", +1, "external", "Qwen3.5-0.8B surprisal | session")),
    ("v", ("v_pyes", -1, "verbal", "Verbal P(yes) (logit)")),
    ("c", ("c_pyes", -1, "trace", "Consistency P(yes) (logit)")),
    ("P1", ("p1_trace", +1, "style", "Probe P1 (self-authorship)")),
    ("P1_blind", ("p1_blind", +1, "style", "Probe P1, no-trace activations")),
    ("P2", ("p2_trace", +1, "trace", "Probe P2 (consistency)")),
    ("P2_blind", ("p2_blind", +1, "trace", "Probe P2, no-trace activations")),
    ("P1h", ("p1h_trace", +1, "style", "Probe P1 (split-half)")),
    ("P2h", ("p2h_trace", +1, "trace", "Probe P2 (split-half)")),
    ("bow_P1", ("bow_p1", +1, "baseline", "Bag-of-words+length, P1 task")),
    ("bow_P2", ("bow_p2", +1, "baseline", "Bag-of-words+length, P2 task")),
    ("len_chars", ("n_chars", +1, "confound", "Note length (characters)")),
    ("len_tokens", ("n_tok", +1, "confound", "Note length (tokens)")),
])
FULL_PROBES = ("P1", "P1_blind", "P2", "P2_blind", "bow_P1", "bow_P2")   # leak against T4p
STYLE_DETS = ("s_trace_mean", "P1h")
TRACE_DETS = ("s_delta", "c", "P2h")
TARGETED = OrderedDict([("s_trace_mean", "T4s"), ("P1h", "T4p"), ("s_delta", "T4d"), ("c", "T4c"), ("v", "T3")])
H4_DETS = ("s_trace_mean", "P1h", "s_delta", "c", "P2h", "v")
TRANSFER_DETS = ("s_trace_mean", "s_blind_mean", "s_delta", "c", "v", "P1h", "P2h", "ppl_gpt2", "ppl_small",
                 "len_chars")
GAP_CANDIDATES = ("s_delta", "c", "P2h")


# ================================================================================================
# small utilities
# ================================================================================================
def _r(x, nd=4):
    if x is None:
        return None
    try:
        x = float(x)
    except (TypeError, ValueError):
        return None
    return round(x, nd) if math.isfinite(x) else None


def null(reason: str, **extra) -> dict:
    d = {"auroc": None, "reason": reason}
    d.update(extra)
    return d


def tier_half(episode_id: str) -> int:
    """Attacker/defender half for T4p (stable, independent of the calibration hash)."""
    return stable_hash("t4p-half", episode_id) % 2


def auc_point(s, y) -> float:
    """AUROC with ties counted 1/2 (nan if a class is missing)."""
    s, y = np.asarray(s, float), np.asarray(y).astype(bool)
    ok = np.isfinite(s)
    s, y = s[ok], y[ok]
    n1, n0 = int(y.sum()), int((~y).sum())
    if n1 == 0 or n0 == 0:
        return float("nan")
    from scipy.stats import rankdata
    r = rankdata(s)
    return float((r[y].sum() - n1 * (n1 + 1) / 2) / (n1 * n0))


# ================================================================================================
# episode-clustered bootstrap
# ================================================================================================
class Boot:
    """One episode-resampling matrix shared by all comparisons (row 0 = the original sample)."""

    def __init__(self, episodes, n_boot: int = N_BOOT, seed: int = SEED):
        self.eps = sorted(set(episodes))
        self.idx = {e: i for i, e in enumerate(self.eps)}
        self.n_boot = n_boot
        n = len(self.eps)
        rng = np.random.default_rng(seed)
        if n:
            c = rng.multinomial(n, np.full(n, 1.0 / n), size=n_boot).astype(np.float32)
        else:
            c = np.zeros((n_boot, 0), np.float32)
        self.counts = np.vstack([np.ones((1, n), np.float32), c])

    def W(self, ep_ids) -> np.ndarray:
        return self.counts[:, [self.idx[e] for e in ep_ids]]


def roc_boot(s: np.ndarray, y: np.ndarray, W: np.ndarray) -> tuple:
    """Weighted ROC for every row of W (B x n). Returns (auc, tpr@1%fpr, tpr@5%fpr), each length B; nan
    where a class has zero weight. Ties are grouped (trapezoid = Mann-Whitney with ties 1/2)."""
    order = np.argsort(-s, kind="mergesort")
    s, y, W = s[order], y[order].astype(np.float64), W[:, order].astype(np.float64)
    starts = np.r_[0, np.flatnonzero(np.diff(s) != 0) + 1]
    Pw = np.add.reduceat(W * y, starts, axis=1)
    Nw = np.add.reduceat(W * (1 - y), starts, axis=1)
    tp, fp = np.cumsum(Pw, 1), np.cumsum(Nw, 1)
    TP, FP = tp[:, -1:], fp[:, -1:]
    with np.errstate(divide="ignore", invalid="ignore"):
        tpr = np.hstack([np.zeros_like(TP), tp / TP])
        fpr = np.hstack([np.zeros_like(FP), fp / FP])
    auc = np.sum((fpr[:, 1:] - fpr[:, :-1]) * (tpr[:, 1:] + tpr[:, :-1]) / 2, axis=1)

    def at(x):
        return np.max(np.where(fpr <= x + 1e-9, tpr, -np.inf), axis=1)

    t1, t5 = at(0.01), at(0.05)
    bad = (TP[:, 0] <= 0) | (FP[:, 0] <= 0)
    for a in (auc, t1, t5):
        a[bad] = np.nan
    return auc, t1, t5


def _ci(reps: np.ndarray) -> tuple:
    r = reps[np.isfinite(reps)]
    if r.size < 2:
        return None, None, int(r.size)
    lo, hi = np.percentile(r, [2.5, 97.5])
    return float(lo), float(hi), int(r.size)


def compare(pos_s, pos_ep, neg_s, neg_ep, boot: Boot, return_reps: bool = False):
    """AUROC + TPR at 1%/5% FPR, positives vs negatives, episode-clustered bootstrap CIs."""
    pos_s, neg_s = np.asarray(pos_s, float), np.asarray(neg_s, float)
    pos_ep, neg_ep = np.asarray(pos_ep, object), np.asarray(neg_ep, object)
    pm, nm = np.isfinite(pos_s), np.isfinite(neg_s)
    base = {"n_pos": int(pm.sum()), "n_neg": int(nm.sum()), "n_pos_missing": int((~pm).sum()),
            "n_neg_missing": int((~nm).sum())}
    if base["n_pos"] == 0 or base["n_neg"] == 0:
        why = ("no positives" if len(pos_s) == 0 else "no finite score for any positive") if base["n_pos"] == 0 \
            else ("no negatives" if len(neg_s) == 0 else "no finite score for any negative")
        out = null(why, **base)
        return (out, None) if return_reps else out
    s = np.r_[pos_s[pm], neg_s[nm]]
    y = np.r_[np.ones(pm.sum()), np.zeros(nm.sum())]
    eps = list(pos_ep[pm]) + list(neg_ep[nm])
    auc, t1, t5 = roc_boot(s, y, boot.W(eps))
    lo, hi, nb = _ci(auc[1:])
    out = {"auroc": _r(auc[0]), "ci_lo": _r(lo), "ci_hi": _r(hi),
           "tpr_fpr01": _r(t1[0]), "tpr_fpr01_ci": [_r(x) for x in _ci(t1[1:])[:2]],
           "tpr_fpr05": _r(t5[0]), "tpr_fpr05_ci": [_r(x) for x in _ci(t5[1:])[:2]],
           **base, "n_episodes": len(set(eps)), "n_boot_valid": nb,
           "fpr_resolution": _r(1.0 / base["n_neg"])}
    return (out, auc) if return_reps else out


def diff_summary(a: np.ndarray, b: np.ndarray, **extra) -> dict:
    """Paired difference of two replicate arrays (row 0 = point estimate)."""
    if a is None or b is None or not np.isfinite(a[0]) or not np.isfinite(b[0]):
        extra = dict(extra)
        why = extra.pop("reason", None) or "a component AUROC is undefined"
        return null(why, **extra) | {"diff": None}
    d = a - b
    lo, hi, nb = _ci(d[1:])
    r = d[1:][np.isfinite(d[1:])]
    p = float(min(1.0, 2 * min((r <= 0).mean(), (r >= 0).mean()))) if r.size else None
    extra = {k: v for k, v in extra.items() if not (k == "reason" and v is None)}
    return {"diff": _r(d[0]), "ci_lo": _r(lo), "ci_hi": _r(hi), "p_boot_two_sided": _r(p), "n_boot_valid": nb,
            **extra}


# ================================================================================================
# data
# ================================================================================================
def rel(p) -> str:
    """Path relative to the repository root where possible (no machine-specific prefix in outputs)."""
    try:
        return str(Path(p).resolve().relative_to(ROOT))
    except (ValueError, TypeError):
        return str(p)


def acts_dir_of(d: Path):
    """Activation directory of a pipeline run. ``config.json`` records the path used on the machine that ran
    the pipeline; if that path does not exist here, fall back to ``cache/local_acts`` in this checkout."""
    cfg = d / "config.json"
    if not cfg.exists():
        return None
    a = json.loads(cfg.read_text()).get("acts_dir")
    if a and not Path(a).exists() and (ROOT / "cache" / "local_acts").exists():
        return str(ROOT / "cache" / "local_acts")
    return a


def has_activations(d: Path = ROOT / "results" / "raw" / "local") -> bool:
    a = acts_dir_of(Path(d))
    return bool(a) and (Path(a) / "index.jsonl").exists()


def load_frame(d: Path) -> pd.DataFrame:
    df = P.load_scores(d)
    if df.empty:
        return df
    df = df.reset_index(drop=True)
    df["kind_base"] = df["kind"].map(P.kind_base)
    df["n_chars"] = df["note"].fillna("").str.len().astype(float)
    df["n_tok"] = pd.to_numeric(df["n_tok"], errors="coerce")
    df["half"] = df["episode_id"].map(tier_half)
    df["calib"] = df["episode_id"].map(is_calibration).astype(bool)
    df["valid_b"] = df["valid"].map(lambda v: bool(v) if v is not None and v == v else False)
    df["inst"] = list(zip(df["episode_id"], df["edit_type"]))
    return df


def load_acts(d: Path, df: pd.DataFrame, which: str, pooling: str, acts_dir=None):
    """(array[n_items, L, D] float16 aligned with df rows (nan where missing), layers) or (None, reason)."""
    acts_dir = acts_dir or acts_dir_of(d)
    if not acts_dir or not (Path(acts_dir) / "index.jsonl").exists():
        return None, f"no activation index under {acts_dir!r}"
    ids, arr = P.load_activations(d, which, pooling, acts_dir=acts_dir)
    if not ids:
        return None, f"no s_{which} activations with matching note hashes"
    pos = {i: k for k, i in enumerate(df["item_id"])}
    A = np.full((len(df),) + arr.shape[1:], np.nan, np.float16)
    for i, a in zip(ids, arr):
        if i in pos:
            A[pos[i]] = a
    layers = list(range(arr.shape[1]))
    try:
        r = next(r for r in P.read_jsonl(Path(acts_dir) / "index.jsonl") if r["pass"] == f"s_{which}")
        meta = json.loads((Path(acts_dir) / r["shard"]).with_suffix(".json").read_text())["meta"]
        if len(meta.get("layers", [])) == arr.shape[1]:
            layers = list(meta["layers"])
    except (StopIteration, OSError, KeyError, ValueError):
        pass
    return (A, layers), None


def read_selected(d: Path) -> list:
    return P.read_jsonl(Path(d) / "selected.jsonl")


def tier_positives(df: pd.DataFrame, sel: list) -> tuple:
    """tier -> DataFrame of valid positives (one row per instance), and per-tier bookkeeping."""
    pos, info = {}, {}
    for t in FORGED_TIERS:
        k = df[df["kind"] == t]
        pos[t] = k[k["valid_b"]].copy()
        info[t] = {"n_items": int(len(k)), "n_valid": int(k["valid_b"].sum())}
    by_id = df.set_index("item_id")
    for t in POOL_TIERS:
        rows = [r for r in sel if r.get("tier") == t]
        if not rows:
            pos[t] = df.iloc[0:0].copy()
            info[t] = {"n_instances": 0, "n_selected": 0, "reason": f"tier {t} not in selected.jsonl"}
            continue
        ids = [r["item_id"] for r in rows if r.get("item_id") and r["item_id"] in by_id.index]
        p = by_id.loc[ids].reset_index()
        p = p[p["valid_b"]]
        pos[t] = p
        info[t] = {"n_instances": len(rows), "n_selected": int(len(p)),
                   "n_empty": int(sum(1 for r in rows if not r.get("item_id")))}
    return pos, info


# ================================================================================================
# probes
# ================================================================================================
class ActFeatures:
    def __init__(self, A: np.ndarray, layers):
        self.A = A
        self.keys = list(range(A.shape[1]))
        self.labels = list(layers)
        self.rowok = np.isfinite(A.reshape(len(A), -1).astype(np.float32)).all(1) if len(A) else np.zeros(0, bool)
        self.sparse = False

    def get(self, key, fit_idx, apply_idx):
        return (self.A[fit_idx, key, :].astype(np.float32), self.A[apply_idx, key, :].astype(np.float32))


class BowFeatures:
    """TF-IDF over word 1-2-grams (vocabulary fitted on the training fold only) + log characters + log tokens."""

    def __init__(self, texts, n_chars, n_tok):
        self.texts = np.asarray([t or "" for t in texts], object)
        nt = np.where(np.isfinite(n_tok), n_tok, [len(t.split()) for t in self.texts])
        self.len = np.c_[np.log1p(n_chars), np.log1p(nt)].astype(np.float64)
        self.keys, self.labels = ["bow"], ["bow"]
        self.rowok = np.ones(len(self.texts), bool)
        self.sparse = True

    def get(self, key, fit_idx, apply_idx):
        from scipy.sparse import csr_matrix, hstack
        from sklearn.feature_extraction.text import TfidfVectorizer
        try:
            vec = TfidfVectorizer(ngram_range=(1, 2), min_df=2, sublinear_tf=True, max_features=20000)
            Xf = vec.fit_transform(self.texts[fit_idx])
        except ValueError:   # tiny training fold: no term in >= 2 documents
            vec = TfidfVectorizer(ngram_range=(1, 2), min_df=1, sublinear_tf=True, max_features=20000)
            Xf = vec.fit_transform(self.texts[fit_idx])
        Xa = vec.transform(self.texts[apply_idx])
        return (hstack([Xf, csr_matrix(self.len[fit_idx])]).tocsr(),
                hstack([Xa, csr_matrix(self.len[apply_idx])]).tocsr())


def _fit(X, y, C, sparse):
    from sklearn.exceptions import ConvergenceWarning
    from sklearn.linear_model import LogisticRegression
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    if sparse:
        m = make_pipeline(StandardScaler(with_mean=False),
                          LogisticRegression(C=C, solver="liblinear", max_iter=MAX_ITER, class_weight="balanced",
                                             random_state=0))
    else:
        m = make_pipeline(StandardScaler(),
                          LogisticRegression(C=C, solver="lbfgs", max_iter=MAX_ITER, class_weight="balanced"))
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always", ConvergenceWarning)
        m.fit(X, y)
    return m, sum(issubclass(x.category, ConvergenceWarning) for x in w)


def _both(y):
    y = np.asarray(y)
    return len(y) > 0 and (y == 1).any() and (y == 0).any()


def choose_hparams(feat, y, train, calib, Cs=CS, default_key=None) -> dict:
    """Pick (key, C): fit on train & ~calib, AUROC on train & calib. Fallback to a fixed default."""
    fit_m, val_m = train & ~calib, train & calib
    default_key = feat.keys[len(feat.keys) // 2] if default_key is None else default_key
    res = {"n_fit": int(fit_m.sum()), "n_val": int(val_m.sum()), "grid": {}, "conv_warnings": 0}
    if not (_both(y[fit_m]) and _both(y[val_m])):
        res.update(key=default_key, best_C={k: DEFAULT_C for k in feat.keys}, fallback=True,
                   reason="calibration split of the training data lacks a class "
                          f"(fit n={res['n_fit']}, val n={res['n_val']}): fixed default layer/C")
        return res
    fi, vi = np.flatnonzero(fit_m), np.flatnonzero(val_m)
    best_C, best_auc = {}, {}
    for k in feat.keys:
        Xf, Xv = feat.get(k, fi, vi)
        for C in Cs:
            m, nw = _fit(Xf, y[fi], C, feat.sparse)
            res["conv_warnings"] += nw
            res["grid"][f"{feat.labels[feat.keys.index(k)]}|{C:g}"] = _r(auc_point(m.decision_function(Xv), y[vi]))
        aucs = [res["grid"][f"{feat.labels[feat.keys.index(k)]}|{C:g}"] for C in Cs]
        aucs = [a if a is not None else -1 for a in aucs]
        j = int(np.argmax(aucs))               # first maximum = smallest C (strongest regularisation)
        best_C[k], best_auc[k] = Cs[j], aucs[j]
    key = max(feat.keys, key=lambda k: (best_auc[k], -feat.keys.index(k)))
    res.update(key=key, best_C=best_C, fallback=False, reason=None)
    return res


def lofo(feat, y, fam, calib, scope=None, n_shuffles=0, seed_tag="", Cs=CS) -> dict:
    """Leave-one-family-out probe. ``y``: 1/0 labels (nan = not part of the training task). Every item of
    the held-out family inside ``scope`` (labelled or not) receives an out-of-fold score.
    Returns oof (chosen key per fold), oof_by_key, shuffled oof per key, and per-fold records (with the
    training indices, for auditing)."""
    n = len(y)
    scope = np.ones(n, bool) if scope is None else scope
    ok = feat.rowok & scope
    lab = ok & np.isfinite(y)
    oof = np.full(n, np.nan)
    by_key = {k: np.full(n, np.nan) for k in feat.keys}
    shuf = {k: [np.full(n, np.nan) for _ in range(n_shuffles)] for k in feat.keys}
    folds = []
    yy = np.where(np.isfinite(y), y, -1).astype(int)
    for f in sorted(set(fam[lab])):
        test = ok & (fam == f)
        train = lab & (fam != f)
        rec = {"family": f, "n_train": int(train.sum()), "n_train_pos": int((yy[train] == 1).sum()),
               "n_test_labelled": int((lab & test).sum()), "train_idx": np.flatnonzero(train),
               "test_idx": np.flatnonzero(test)}
        if not _both(yy[train]):
            rec["reason"] = "training families lack a class"
            folds.append(rec)
            continue
        hp = choose_hparams(feat, yy, train, calib, Cs)
        rec.update(chosen=feat.labels[feat.keys.index(hp["key"])], best_C={feat.labels[feat.keys.index(k)]: c
                                                                        for k, c in hp["best_C"].items()},
                   fallback=hp["fallback"], selection_reason=hp["reason"], grid=hp["grid"],
                   n_select_fit=hp["n_fit"], n_select_val=hp["n_val"], conv_warnings=hp["conv_warnings"])
        ti, si = np.flatnonzero(train), np.flatnonzero(test)
        for k in feat.keys:
            Xtr, Xte = feat.get(k, ti, si)
            m, nw = _fit(Xtr, yy[ti], hp["best_C"][k], feat.sparse)
            rec["conv_warnings"] += nw
            by_key[k][si] = m.decision_function(Xte)
            for r in range(n_shuffles):
                rng = np.random.default_rng(stable_hash("shuffle", seed_tag, f, k, r) % (2 ** 32))
                ms, nw = _fit(Xtr, rng.permutation(yy[ti]), hp["best_C"][k], feat.sparse)
                rec["conv_warnings"] += nw
                shuf[k][r][si] = ms.decision_function(Xte)
        oof[si] = by_key[hp["key"]][si]
        folds.append(rec)
    return {"oof": oof, "oof_by_key": by_key, "shuffled": shuf, "folds": folds, "labels": feat.labels,
            "keys": feat.keys}


def probe_labels(df: pd.DataFrame) -> dict:
    kb = df["kind_base"].values
    y1 = np.full(len(df), np.nan)
    y1[kb == "genuine"] = 0
    y1[kb == "other"] = 1                               # P1: 1 = other-model note (not self)
    y2 = np.full(len(df), np.nan)
    y2[kb == "genuine"] = 0
    y2[np.isin(df["kind"].values, FORGED_TIERS) & df["valid_b"].values] = 1   # P2: valid T0-T2 forgeries
    return {"P1": y1, "P2": y2}


def summarize_lofo(res, y, fam, ep, boot, scope=None) -> dict:
    """Per-fold and pooled out-of-fold AUROC on the labelled items, per chosen layer, per layer, shuffles."""
    lab = np.isfinite(y) & (np.ones(len(y), bool) if scope is None else scope)
    yy = np.where(lab, y, 0)

    def cmp(s, mask):
        return compare(s[mask & (yy == 1)], ep[mask & (yy == 1)], s[mask & (yy == 0)], ep[mask & (yy == 0)], boot)

    out = {"pooled": cmp(res["oof"], lab), "folds": [], "by_layer": {}, "shuffled": {}}
    for rec in res["folds"]:
        f = rec["family"]
        r = {k: v for k, v in rec.items() if k not in ("train_idx", "test_idx")}
        r["auroc_heldout"] = cmp(res["oof"], lab & (fam == f))
        out["folds"].append(r)
    for k, lbl in zip(res["keys"], res["labels"]):
        out["by_layer"][str(lbl)] = cmp(res["oof_by_key"][k], lab)
        sh = [auc_point(s[lab], yy[lab]) for s in res["shuffled"][k]]
        sh = [x for x in sh if np.isfinite(x)]
        out["shuffled"][str(lbl)] = {"aurocs": [_r(x) for x in sh], "mean": _r(np.mean(sh)) if sh else None,
                                     "min": _r(min(sh)) if sh else None, "max": _r(max(sh)) if sh else None,
                                     "n_shuffles": len(sh)}
    # shuffled at the per-fold chosen layer
    sel = np.full((len(next(iter(res["shuffled"].values()))) if res["shuffled"] else 0, len(y)), np.nan)
    for rec in res["folds"]:
        if "chosen" not in rec:
            continue
        k = res["keys"][res["labels"].index(rec["chosen"])]
        for r, s in enumerate(res["shuffled"][k]):
            sel[r, rec["test_idx"]] = s[rec["test_idx"]]
    sh = [auc_point(s[lab], yy[lab]) for s in sel]
    sh = [x for x in sh if np.isfinite(x)]
    out["shuffled_chosen"] = {"aurocs": [_r(x) for x in sh], "mean": _r(np.mean(sh)) if sh else None,
                              "n_shuffles": len(sh)}
    return out


def attacker_t4p(feat, df, y1, Cs=CS) -> tuple:
    """Attacker's self-authorship probe: trained on one half, scores the other half's candidates (and swap).
    Returns ({cand item_id: self-authorship score (higher = more 'own')}, records)."""
    half = df["half"].values
    calib = df["calib"].values
    is_cand = (df["kind"] == "cand").values
    scores, recs = {}, []
    yy = np.where(np.isfinite(y1), y1, -1).astype(int)
    for H in (0, 1):
        train = feat.rowok & np.isfinite(y1) & (half != H)
        target = feat.rowok & is_cand & (half == H)
        rec = {"target_half": H, "n_train": int(train.sum()), "n_target_candidates": int(target.sum()),
               "train_episodes": sorted(set(df["episode_id"][train])),
               "target_episodes": sorted(set(df["episode_id"][target]))}
        if not _both(yy[train]) or not target.any():
            rec["reason"] = "attacker half lacks a class" if target.any() else "no candidates in target half"
            recs.append(rec)
            continue
        hp = choose_hparams(feat, yy, train, calib, Cs)
        k = hp["key"]
        Xtr, Xte = feat.get(k, np.flatnonzero(train), np.flatnonzero(target))
        m, nw = _fit(Xtr, yy[train], hp["best_C"][k], feat.sparse)
        s = -m.decision_function(Xte)                    # self-authorship = - logit(other-model)
        for i, v in zip(df["item_id"].values[target], s):
            scores[i] = float(v)
        rec.update(layer=feat.labels[feat.keys.index(k)], C=hp["best_C"][k], fallback=hp["fallback"],
                   selection_reason=hp["reason"], grid=hp["grid"], conv_warnings=hp["conv_warnings"] + nw)
        recs.append(rec)
    return scores, recs


def run_probes(d, df, boot, n_shuffles, acts_dir=None, log=print) -> dict:
    """Fit every probe; adds out-of-fold score columns to df; returns the probe report and T4p scores."""
    fam, ep, calib = df["family"].values, df["episode_id"].values, df["calib"].values
    half = df["half"].values
    Y = probe_labels(df)
    rep = {"design": {"Cs": list(CS), "default_C": DEFAULT_C, "n_shuffles": n_shuffles, "max_iter": MAX_ITER,
                      "class_weight": "balanced", "standardise": "training fold only",
                      "selection": "fit on training-family non-calibration episodes, AUROC on training-family "
                                   "calibration episodes; refit on all training-family episodes"},
           "main": {}, "last_token": {}, "split_half": {}, "bow": {}, "attacker": None}
    t4p_scores = None
    for which in ("trace", "blind"):
        for pooling in ("mean", "last"):
            got, why = load_acts(d, df, which, pooling, acts_dir)
            for task in ("P1", "P2"):
                col = f"{task.lower()}_{which}" if pooling == "mean" else f"{task.lower()}_{which}_last"
                df[col] = np.nan
                dest = rep["main"] if pooling == "mean" else rep["last_token"]
                if got is None:
                    dest[f"{task}|{which}"] = null(why)
                    continue
                A, layers = got
                feat = ActFeatures(A, layers)
                log(f"[probes] {task} {which}/{pooling}: {int((feat.rowok & np.isfinite(Y[task])).sum())} labelled")
                res = lofo(feat, Y[task], fam, calib, n_shuffles=n_shuffles if pooling == "mean" else 0,
                           seed_tag=f"{task}|{which}|{pooling}")
                df[col] = res["oof"]
                dest[f"{task}|{which}"] = summarize_lofo(res, Y[task], fam, ep, boot)
                dest[f"{task}|{which}"]["layers"] = layers
                if pooling == "mean":
                    # split-half defender probes (used against T4p): LOFO within each half
                    hcol = f"{task.lower()}h_{which}"
                    df[hcol] = np.nan
                    hrep = {}
                    for H in (0, 1):
                        sc = half == H
                        hr = lofo(feat, Y[task], fam, calib, scope=sc, seed_tag=f"{task}|{which}|half{H}")
                        df.loc[sc, hcol] = hr["oof"][sc]
                        hrep[f"half{H}"] = summarize_lofo(hr, Y[task], fam, ep, boot, scope=sc)
                        hrep[f"half{H}"]["episodes"] = sorted(set(ep[sc]))
                    hrep["pooled"] = summarize_lofo({"oof": df[hcol].values, "oof_by_key": {}, "shuffled": {},
                                                     "folds": [], "keys": [], "labels": []},
                                                    Y[task], fam, ep, boot)["pooled"]
                    rep["split_half"][f"{task}|{which}"] = hrep
                if task == "P1" and which == "trace" and pooling == "mean":
                    t4p_scores, recs = attacker_t4p(feat, df, Y["P1"])
                    rep["attacker"] = {"features": "with-trace mean-pooled activations", "halves": recs,
                                       "n_scored_candidates": len(t4p_scores),
                                       "disjoint": _halves_disjoint(recs, df)}
                del feat
            del got
    bow = BowFeatures(df["note"].values, df["n_chars"].values, df["n_tok"].values.astype(float))
    for task in ("P1", "P2"):
        log(f"[probes] bag-of-words {task}")
        res = lofo(bow, Y[task], fam, calib, seed_tag=f"bow|{task}")
        df[f"bow_{task.lower()}"] = res["oof"]
        rep["bow"][task] = summarize_lofo(res, Y[task], fam, ep, boot)
    return rep, t4p_scores


def _halves_disjoint(recs, df) -> dict:
    """Audit: attacker training episodes vs defender (split-half) training/evaluation episodes."""
    out = {}
    for r in recs:
        tr = set(r.get("train_episodes", []))
        tg = set(r.get("target_episodes", []))
        defender = set(df["episode_id"][df["half"] == r["target_half"]])
        out[f"target_half{r['target_half']}"] = {"attacker_vs_defender_overlap": len(tr & defender),
                                                 "attacker_vs_target_overlap": len(tr & tg)}
    return out


# ================================================================================================
# detector table and derived blocks
# ================================================================================================
def oriented(frame: pd.DataFrame, det: str) -> np.ndarray:
    col, o, _, _ = DETECTORS[det]
    if col not in frame:
        return np.full(len(frame), np.nan)
    return o * pd.to_numeric(frame[col], errors="coerce").values.astype(float)


def _common_instances(pos: dict) -> tuple:
    present = [t for t in TIERS if len(pos[t])]
    if not present:
        return set(), present
    s = set(pos[present[0]]["inst"])
    for t in present[1:]:
        s &= set(pos[t]["inst"])
    return s, present


def detector_table(df, pos, boot, reps_store) -> tuple:
    gen = df[df["kind"] == "genuine"]
    common, present = _common_instances(pos)
    rows, by_edit = [], []
    for t in TIERS:
        p_all = pos[t]
        for subset in ("all", "common"):
            p = p_all if subset == "all" else p_all[p_all["inst"].isin(common)]
            for negset in ("matched", "all_genuine"):
                n = gen[gen["inst"].isin(set(p["inst"]))] if negset == "matched" else gen
                for det in DETECTORS:
                    meta = {"detector": det, "tier": t, "subset": subset, "negset": negset}
                    if t == "T4p" and det in FULL_PROBES:
                        rows.append({**meta, **null("full-sample LOFO probe shares training episodes with the "
                                                    "T4p attacker; use the split-half probe")})
                        continue
                    if not len(p_all):
                        rows.append({**meta, **null(f"no valid positives for {t}")})
                        continue
                    r, a = compare(oriented(p, det), p["episode_id"].values, oriented(n, det), n["episode_id"].values,
                                   boot, return_reps=True)
                    reps_store[(det, t, subset, negset)] = a
                    rows.append({**meta, **r})
        # per edit type (all instances, matched negatives)
        for et in EDIT_TYPES:
            p = p_all[p_all["edit_type"] == et]
            n = gen[gen["inst"].isin(set(p["inst"]))]
            for det in DETECTORS:
                meta = {"detector": det, "tier": t, "edit_type": et}
                if t == "T4p" and det in FULL_PROBES:
                    by_edit.append({**meta, **null("leakage (see main table)")})
                    continue
                by_edit.append({**meta, **compare(oriented(p, det), p["episode_id"].values, oriented(n, det),
                                                  n["episode_id"].values, boot)})
    return rows, by_edit, {"n_common_instances": len(common), "tiers_defining_common": present}


def self_authorship(df, boot) -> list:
    gen = df[df["kind"] == "genuine"]
    oth = df[df["kind_base"] == "other"]
    xep = df[df["kind_base"].str.startswith("xep")]
    rows = []
    groups = [("other:all", oth)] + [(k, g) for k, g in oth.groupby("kind")]
    for name, g in groups:
        sess = set(zip(g["episode_id"], g["session_idx"]))
        n = gen[[k in sess for k in zip(gen["episode_id"], gen["session_idx"])]]
        for det in DETECTORS:
            r = compare(oriented(g, det), g["episode_id"].values, oriented(n, det), n["episode_id"].values, boot)
            if r.get("auroc") is None and len(g) and r["n_pos"] == 0:
                r["reason"] = "score not computed for this kind (pipeline PASS_KINDS) or missing"
            rows.append({"comparison": f"genuine vs {name}", "detector": det, **r})
    if not len(oth):
        rows.append({"comparison": "genuine vs other-model", "detector": None,
                     **null("no other-model notes in the registry")})
    if len(xep):
        for det in DETECTORS:
            rows.append({"comparison": "genuine vs xep", "detector": det,
                         **compare(oriented(xep, det), xep["episode_id"].values, oriented(gen, det),
                                   gen["episode_id"].values, boot)})
    else:
        rows.append({"comparison": "genuine vs own notes from other episodes", "detector": None,
                     **null("not computable: the pipeline registers no other-episode ('xep') items "
                            "(tests/test_local_pipeline.py asserts their absence), so no trace-conditioned "
                            "score or activation exists for an other-episode note placed in the slot; "
                            "context-free scores would compare genuine notes with genuine notes")})
    return rows


def _get(rows, **kw):
    for r in rows:
        if all(r.get(k) == v for k, v in kw.items()):
            return r
    return None


def h3_h4(det_rows, reps, df, pos, boot) -> dict:
    out = {"definitions": {
        "style_signals": list(STYLE_DETS), "trace_signals": list(TRACE_DETS), "verbal": "v",
        "targeted_tier": dict(TARGETED),
        "subset": "common instances, matched negatives (identical instances across tiers)",
        "h4_criterion": "style-based AUROC < 0.60 under the T4 tier aimed at it (point estimate; the CI upper "
                        "bound < 0.60 is reported as the strict version); trace-based signal with the highest "
                        "worst-case AUROC over the T4 tiers keeps the most signal",
        "note": "P2 has no tier aimed at it; P1/P2 here are the split-half probes (needed for T4p)."}}
    tiers = ("T0", "T1", "T2", "T2r", "T3") + T4_TIERS
    mat = []
    for det in H4_DETS:
        for t in tiers:
            r = _get(det_rows, detector=det, tier=t, subset="common", negset="matched") or {}
            mat.append({"detector": det, "tier": t, "targeted": TARGETED.get(det) == t,
                        **{k: r.get(k) for k in ("auroc", "ci_lo", "ci_hi", "n_pos", "n_neg", "reason")}})
    out["matrix"] = mat
    crit = []
    for det in STYLE_DETS:
        t = TARGETED[det]
        r = _get(mat, detector=det, tier=t)
        a = r.get("auroc") if r else None
        crit.append({"detector": det, "tier": t, "auroc": a, "ci_lo": r.get("ci_lo"), "ci_hi": r.get("ci_hi"),
                     "n_pos": r.get("n_pos"), "n_neg": r.get("n_neg"),
                     "below_0.60": None if a is None else bool(a < 0.60),
                     "ci_hi_below_0.60": None if r.get("ci_hi") is None else bool(r["ci_hi"] < 0.60),
                     "reason": r.get("reason")})
    out["h4_style_under_targeted_T4"] = crit

    def worst(det):
        vals = [(t, reps.get((det, t, "common", "matched"))) for t in T4_TIERS]
        vals = [(t, a) for t, a in vals if a is not None and np.isfinite(a[0])]
        if not vals:
            return None, None
        t, a = min(vals, key=lambda x: x[1][0])
        return t, a

    wc = []
    for det in TRACE_DETS + STYLE_DETS:
        t, a = worst(det)
        wc.append({"detector": det, "group": "trace" if det in TRACE_DETS else "style", "worst_tier": t,
                   "worst_auroc": _r(a[0]) if a is not None else None,
                   "ci": [_r(x) for x in _ci(a[1:])[:2]] if a is not None else None,
                   "n_tiers": sum(1 for x in T4_TIERS if reps.get((det, x, "common", "matched")) is not None)})
    out["worst_case_over_T4"] = wc
    tr = [w for w in wc if w["group"] == "trace" and w["worst_auroc"] is not None]
    st = [w for w in wc if w["group"] == "style" and w["worst_auroc"] is not None]
    if tr and st:
        bt, bs = max(tr, key=lambda w: w["worst_auroc"]), max(st, key=lambda w: w["worst_auroc"])
        a, b = worst(bt["detector"])[1], worst(bs["detector"])[1]
        out["h4_best_trace_vs_best_style_worst_case"] = {
            "best_trace": bt["detector"], "best_style": bs["detector"],
            **diff_summary(a, b, note="difference of worst-case AUROCs; the worst tier is chosen on the point "
                                      "estimate and held fixed in the bootstrap")}
    else:
        out["h4_best_trace_vs_best_style_worst_case"] = null("worst-case AUROC unavailable for a group")
    # H3 (a): trace-based minus verbal at T0-T2, on items with both scores
    h3 = []
    gen = df[df["kind"] == "genuine"]
    for t in FORGED_TIERS:
        p = pos[t]
        n = gen[gen["inst"].isin(set(p["inst"]))]
        for det in ("s_delta", "c", "P2"):
            pm = np.isfinite(oriented(p, det)) & np.isfinite(oriented(p, "v"))
            nm = np.isfinite(oriented(n, det)) & np.isfinite(oriented(n, "v"))
            pp, nn = p[pm], n[nm]
            r1, a = compare(oriented(pp, det), pp["episode_id"].values, oriented(nn, det), nn["episode_id"].values,
                            boot, True)
            r2, b = compare(oriented(pp, "v"), pp["episode_id"].values, oriented(nn, "v"), nn["episode_id"].values,
                            boot, True)
            h3.append({"tier": t, "detector": det, "auroc_det": r1.get("auroc"), "auroc_v": r2.get("auroc"),
                       "n_pos": r1.get("n_pos"), "n_neg": r1.get("n_neg"), **diff_summary(a, b)})
    out["h3_trace_minus_verbal"] = h3
    return out


def integrity_gap(df, pos, boot) -> dict:
    """Local counterpart of §3 item 3: best trace-based detector (chosen by pooled T0-T2 AUROC on the
    calibration episodes) minus verbal V, evaluated on the non-calibration episodes."""
    gen = df[df["kind"] == "genuine"]
    sel = {}
    pc = pd.concat([pos[t] for t in FORGED_TIERS]) if any(len(pos[t]) for t in FORGED_TIERS) else df.iloc[0:0]
    pc = pc[pc["calib"]]
    nc = gen[gen["calib"] & gen["inst"].isin(set(pc["inst"]))]
    for det in GAP_CANDIDATES:
        sel[det] = _r(auc_point(np.r_[oriented(pc, det), oriented(nc, det)], np.r_[np.ones(len(pc)), np.zeros(len(nc))]))
    ok = {k: v for k, v in sel.items() if v is not None}
    out = {"selection": {"candidates": list(GAP_CANDIDATES), "calib_auroc_T0_T2": sel,
                         "n_pos_calib": int(len(pc)), "n_neg_calib": int(len(nc))}}
    if not ok:
        out["selection"]["reason"] = "no calibration-episode AUROC computable"
        out["best"] = None
        out["by_tier"] = []
        return out
    best = max(ok, key=lambda k: (ok[k], -GAP_CANDIDATES.index(k)))
    out["best"] = best
    rows = []
    tiers = ["T3"] + list(T4_TIERS) + ["T4_pooled"]
    for t in tiers:
        if t == "T4_pooled":
            p = pd.concat([pos[x] for x in T4_TIERS if len(pos[x])]) if any(len(pos[x]) for x in T4_TIERS) \
                else df.iloc[0:0]
        else:
            p = pos[t]
        p = p[~p["calib"]]
        n = gen[~gen["calib"] & gen["inst"].isin(set(p["inst"]))]
        pm = np.isfinite(oriented(p, best)) & np.isfinite(oriented(p, "v"))
        nm = np.isfinite(oriented(n, best)) & np.isfinite(oriented(n, "v"))
        pp, nn = p[pm], n[nm]
        r1, a = compare(oriented(pp, best), pp["episode_id"].values, oriented(nn, best), nn["episode_id"].values,
                        boot, True)
        r2, b = compare(oriented(pp, "v"), pp["episode_id"].values, oriented(nn, "v"), nn["episode_id"].values,
                        boot, True)
        rows.append({"tier": t, "detector": best, "auroc_best": r1.get("auroc"), "auroc_v": r2.get("auroc"),
                     "n_pos": r1.get("n_pos"), "n_neg": r1.get("n_neg"), "n_pos_dropped_missing": int((~pm).sum()),
                     "n_neg_dropped_missing": int((~nm).sum()),
                     **diff_summary(a, b, reason=r1.get("reason") or r2.get("reason"))})
    out["by_tier"] = rows
    out["note"] = ("T4_pooled stacks the positives of T4s/T4d/T4c/T4p (a candidate chosen by several rules "
                   "counts once per rule). Items lacking either score are dropped from both detectors.")
    return out


def transfer(df, pos, boot) -> list:
    """Attack cost of selection: each rule vs the random-candidate baseline T2r, on shared instances."""
    gen = df[df["kind"] == "genuine"]
    base = pos["T2r"]
    rows = []
    for rule in RULES:
        pr = pos[rule]
        for det in TRANSFER_DETS:
            meta = {"rule": rule, "detector": det}
            if not len(pr) or not len(base):
                rows.append({**meta, **null(f"no selections for {rule if not len(pr) else 'T2r'}")})
                continue
            m = pr[["inst", "episode_id"]].assign(sr=oriented(pr, det)).merge(
                base[["inst"]].assign(sb=oriented(base, det)), on="inst")
            m = m[np.isfinite(m["sr"]) & np.isfinite(m["sb"])]
            if not len(m):
                rows.append({**meta, **null("no instance with finite scores under both rules")})
                continue
            dlt = (m["sr"] - m["sb"]).values
            W = boot.W(m["episode_id"].values)
            with np.errstate(invalid="ignore", divide="ignore"):
                means = (W @ dlt) / W.sum(1)
            lo, hi, nb = _ci(means[1:])
            g = oriented(gen, det)
            sd = float(np.nanstd(g, ddof=1)) if np.isfinite(g).sum() > 1 else float("nan")
            inst = set(m["inst"])
            pr2, b2 = pr[pr["inst"].isin(inst)], base[base["inst"].isin(inst)]
            n = gen[gen["inst"].isin(inst)]
            _, a = compare(oriented(pr2, det), pr2["episode_id"].values, oriented(n, det), n["episode_id"].values,
                           boot, True)
            _, b = compare(oriented(b2, det), b2["episode_id"].values, oriented(n, det), n["episode_id"].values,
                           boot, True)
            dd = diff_summary(a, b)
            rows.append({**meta, "n_instances": int(len(m)), "n_episodes": int(m["episode_id"].nunique()),
                         "mean_shift": _r(means[0]), "mean_shift_ci": [_r(lo), _r(hi)],
                         "mean_shift_sd_units": _r(means[0] / sd) if sd and np.isfinite(sd) and sd > 0 else None,
                         "sd_genuine": _r(sd), "share_identical_pick": _r(float(np.mean(
                             pr.set_index("inst").reindex(list(inst))["item_id"].values ==
                             base.set_index("inst").reindex(list(inst))["item_id"].values))),
                         "auroc_rule": _r(a[0]) if a is not None else None,
                         "auroc_T2r": _r(b[0]) if b is not None else None,
                         "auroc_change": dd.get("diff"), "auroc_change_ci": [dd.get("ci_lo"), dd.get("ci_hi")],
                         "n_boot_valid": nb})
    return rows


def descriptives(df, pos, info, sel) -> dict:
    out = {"n_items": int(len(df)), "n_episodes": int(df["episode_id"].nunique()) if len(df) else 0,
           "n_instances": int(df[df["kind"] == "genuine"]["inst"].nunique()) if len(df) else 0}
    out["episodes_per_family"] = {f: int(g["episode_id"].nunique()) for f, g in df.groupby("family")}
    out["calibration_episodes_per_family"] = {f: int(g[g["calib"]]["episode_id"].nunique())
                                              for f, g in df.groupby("family")}
    out["episodes_per_half"] = {str(h): int(g["episode_id"].nunique()) for h, g in df.groupby("half")}
    kinds = []
    for k, g in df.groupby("kind"):
        v = g["valid"].dropna()
        kinds.append({"kind": k, "n": int(len(g)), "n_valid": int(g["valid_b"].sum()) if len(v) else None,
                      "valid_rate": _r(g["valid_b"].mean()) if len(v) else None,
                      "chars_mean": _r(g["n_chars"].mean(), 1), "chars_sd": _r(g["n_chars"].std(ddof=1), 1),
                      "tokens_mean": _r(g["n_tok"].mean(), 1), "tokens_sd": _r(g["n_tok"].std(ddof=1), 1),
                      "n_episodes": int(g["episode_id"].nunique())})
    out["by_kind"] = kinds
    c = df[df["kind"] == "cand"]
    if len(c):
        per = c.groupby("inst")["valid_b"].sum()
        out["candidates"] = {"n": int(len(c)), "n_valid": int(c["valid_b"].sum()), "valid_rate": _r(c["valid_b"].mean()),
                             "n_instances": int(len(per)), "instances_with_valid": int((per > 0).sum()),
                             "valid_per_instance_mean": _r(per.mean(), 2)}
    else:
        out["candidates"] = {"n": 0, "reason": "no candidates in the registry"}
    out["tiers"] = {t: {**info[t], "n_positives": int(len(pos[t]))} for t in TIERS}
    score_cov = {}
    for det, (col, _, _, _) in DETECTORS.items():
        if col in df:
            score_cov[det] = {k: int(np.isfinite(pd.to_numeric(g[col], errors="coerce")).sum())
                              for k, g in df.groupby("kind")}
    out["finite_scores_by_kind"] = score_cov
    # coverage of v for selected candidates (v is scored for candidates chosen by the rule tiers only)
    vcov = {}
    for t in POOL_TIERS:
        p = pos[t]
        vcov[t] = {"n": int(len(p)), "n_with_v": int(np.isfinite(pd.to_numeric(p.get("v_pyes", pd.Series(dtype=float)),
                                                                           errors="coerce")).sum()) if len(p) else 0}
    out["v_coverage_selected"] = vcov
    return out


# ================================================================================================
# main
# ================================================================================================
def _clean(o):
    if isinstance(o, dict):
        return {str(k): _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_clean(v) for v in o]
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating, float)):
        return _r(o, 6)
    if isinstance(o, np.bool_):
        return bool(o)
    if isinstance(o, np.ndarray):
        return [_clean(v) for v in o.tolist()]
    return o


def select_t4p_scores(d, acts_dir=None, log=print) -> dict:
    """Attacker scores only (no defender probes): {candidate item_id: self-authorship score}."""
    df = load_frame(Path(d))
    got, why = load_acts(Path(d), df, "trace", "mean", acts_dir)
    if got is None:
        raise RuntimeError(f"T4p: {why}")
    feat = ActFeatures(*got)
    scores, recs = attacker_t4p(feat, df, probe_labels(df)["P1"])
    log(f"[t4p] scored {len(scores)} candidates; halves: "
        + "; ".join(f"half {r['target_half']}: train n={r['n_train']} layer={r.get('layer')} C={r.get('C')}"
                    for r in recs))
    return scores


def main(dir=DEFAULT_DIR, out=DEFAULT_OUT, select_t4p: bool = False, n_boot: int = N_BOOT,
         n_shuffles: int = N_SHUFFLES, acts_dir=None, log=print) -> dict:
    d, out = Path(dir), Path(out)
    report = {"meta": {"dir": rel(d), "acts_dir": rel(acts_dir or acts_dir_of(d)), "n_boot": n_boot, "seed": SEED,
                       "n_shuffles": n_shuffles, "tiers": list(TIERS),
                       "orientation": {k: v[1] for k, v in DETECTORS.items()},
                       "detector_columns": {k: v[0] for k, v in DETECTORS.items()},
                       "detector_groups": {k: v[2] for k, v in DETECTORS.items()},
                       "detector_labels": {k: v[3] for k, v in DETECTORS.items()},
                       "design": (__doc__ or "").split("Design")[1] if "Design" in (__doc__ or "") else ""}}
    df = load_frame(d)
    if df.empty:
        report["error"] = f"no items in {d / 'items.jsonl'}"
        _write(report, {}, out)
        return report
    if select_t4p:
        scores = select_t4p_scores(d, acts_dir, log)
        new = P.append_selection(d, "T4p", scores, maximize=True)
        log(f"[t4p] appended {sum(r['item_id'] is not None for r in new)}/{len(new)} T4p selections to "
            f"{d / 'selected.jsonl'}")
        report["meta"]["t4p_written"] = True
    boot = Boot(df["episode_id"].unique(), n_boot)
    probes, t4p_scores = run_probes(d, df, boot, n_shuffles, acts_dir, log)
    sel = read_selected(d)
    # consistency of the stored T4p selection with the attacker scores recomputed now
    if t4p_scores is not None:
        cands = df[df["kind"] == "cand"][["item_id", "episode_id", "edit_type", "cand_idx", "valid"]].to_dict("records")
        recomputed = {(r["episode_id"], r["edit_type"]): r["item_id"]
                      for r in P.select_by_score(cands, t4p_scores, "T4p", True)}
        stored = {(r["episode_id"], r["edit_type"]): r["item_id"] for r in sel if r.get("tier") == "T4p"}
        probes["attacker"]["stored_selection"] = (
            {"n": len(stored), "n_agree_with_recomputed": sum(stored.get(k) == v for k, v in recomputed.items())}
            if stored else {"n": 0, "reason": "T4p not in selected.jsonl (run with --select-t4p)"})
    pos, info = tier_positives(df, sel)
    reps = {}
    log("[detectors] bootstrap tables")
    det_rows, by_edit, common = detector_table(df, pos, boot, reps)
    report["descriptives"] = descriptives(df, pos, info, sel)
    report["descriptives"]["common_subset"] = common
    report["detectors"] = det_rows
    report["detectors_by_edit"] = by_edit
    report["self_authorship"] = self_authorship(df, boot)
    report["probes"] = probes
    report["h3_h4"] = h3_h4(det_rows, reps, df, pos, boot)
    report["integrity_gap"] = integrity_gap(df, pos, boot)
    report["transfer"] = transfer(df, pos, boot)
    report["headline_all"] = {det: {t: {k: (_get(det_rows, detector=det, tier=t, subset="all", negset="matched")
                                            or {}).get(k) for k in ("auroc", "ci_lo", "ci_hi", "n_pos", "n_neg", "reason")}
                                    for t in TIERS} for det in DETECTORS}
    report["headline"] = headline_contract(report["headline_all"])
    _write(report, {"detectors": det_rows, "detectors_by_edit": by_edit, "self_authorship": report["self_authorship"],
                    "probes": _probe_rows(probes), "h4_matrix": report["h3_h4"]["matrix"],
                    "integrity_gap": report["integrity_gap"].get("by_tier", []), "transfer": report["transfer"],
                    "descriptives": report["descriptives"]["by_kind"]}, out)
    log(f"[local] wrote {out / 'local.json'}")
    return report


# Detectors of the local panel of the paper's headline figure (keys V and C reuse the hosted styles in
# analysis/figures.py). Probes are the split-half versions, which are valid at every tier including T4p.
HEADLINE = OrderedDict([("Surprisal", "s_trace_mean"), ("Surprisal delta", "s_delta"), ("V", "v"), ("C", "c"),
                        ("Probe P1", "P1h"), ("Probe P2", "P2h")])


def headline_contract(h: dict) -> dict:
    """``{"label", "tiers", "detectors": {name: {"est": [..], "lo": [..], "hi": [..], "n_pos", "n_neg", "reason"}}}``
    (one value per tier, null where missing): the format read by analysis/figures.py."""
    dets = OrderedDict()
    for name, det in HEADLINE.items():
        cells = [h[det][t] for t in TIERS]
        dets[name] = {"detector": det, "est": [c["auroc"] for c in cells], "lo": [c["ci_lo"] for c in cells],
                      "hi": [c["ci_hi"] for c in cells], "n_pos": [c["n_pos"] for c in cells],
                      "n_neg": [c["n_neg"] for c in cells], "reason": [c["reason"] for c in cells]}
    return {"label": "Qwen3.5-4B, local", "tiers": list(TIERS), "subset": "all instances",
            "negset": "matched genuine notes", "detectors": dets}


def _probe_rows(probes) -> list:
    rows = []

    def add(name, acts, pooling, variant, s):
        if not isinstance(s, dict):
            return
        if s.get("auroc", 0) is None and "pooled" not in s:
            rows.append({"probe": name, "acts": acts, "pooling": pooling, "variant": variant, "scope": "pooled",
                         "reason": s.get("reason")})
            return
        p = s.get("pooled", {})
        rows.append({"probe": name, "acts": acts, "pooling": pooling, "variant": variant, "scope": "pooled",
                     "layer": "chosen", **{k: p.get(k) for k in ("auroc", "ci_lo", "ci_hi", "n_pos", "n_neg", "reason")},
                     "shuffled_mean": (s.get("shuffled_chosen") or {}).get("mean")})
        for f in s.get("folds", []):
            a = f.get("auroc_heldout", {})
            rows.append({"probe": name, "acts": acts, "pooling": pooling, "variant": variant,
                         "scope": f"heldout:{f['family']}", "layer": f.get("chosen"),
                         "C": (f.get("best_C") or {}).get(f.get("chosen")), "fallback": f.get("fallback"),
                         **{k: a.get(k) for k in ("auroc", "ci_lo", "ci_hi", "n_pos", "n_neg")},
                         "reason": f.get("reason") or f.get("selection_reason")})
        for lbl, a in (s.get("by_layer") or {}).items():
            sh = (s.get("shuffled") or {}).get(lbl, {})
            rows.append({"probe": name, "acts": acts, "pooling": pooling, "variant": variant, "scope": "pooled",
                         "layer": lbl, **{k: a.get(k) for k in ("auroc", "ci_lo", "ci_hi", "n_pos", "n_neg", "reason")},
                         "shuffled_mean": sh.get("mean"), "shuffled_min": sh.get("min"), "shuffled_max": sh.get("max")})

    for key, s in probes.get("main", {}).items():
        t, w = key.split("|")
        add(t, w, "mean", "lofo", s)
    for key, s in probes.get("last_token", {}).items():
        t, w = key.split("|")
        add(t, w, "last", "lofo", s)
    for key, s in probes.get("bow", {}).items():
        add(key, "text", "-", "bow+length", s)
    for key, h in probes.get("split_half", {}).items():
        t, w = key.split("|")
        p = h.get("pooled", {})
        rows.append({"probe": t, "acts": w, "pooling": "mean", "variant": "split-half", "scope": "pooled",
                     "layer": "chosen", **{k: p.get(k) for k in ("auroc", "ci_lo", "ci_hi", "n_pos", "n_neg", "reason")}})
    return rows


def _write(report, tables, out: Path):
    out.mkdir(parents=True, exist_ok=True)
    tmp = out / "local.json.tmp"
    tmp.write_text(json.dumps(_clean(report), indent=1))
    os.replace(tmp, out / "local.json")
    for name, rows in tables.items():
        flat = []
        for r in rows:
            f = {}
            for k, v in r.items():
                if isinstance(v, (list, tuple)) and len(v) == 2 and k.endswith("_ci"):
                    f[k + "_lo"], f[k + "_hi"] = v
                elif isinstance(v, (dict, list)):
                    f[k] = json.dumps(_clean(v))
                else:
                    f[k] = v
            flat.append(f)
        pd.DataFrame(flat).to_csv(out / f"local_{name}.csv", index=False)


def cli(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dir", default=str(DEFAULT_DIR))
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    ap.add_argument("--acts", default=None, help="activation directory (default: config.json acts_dir)")
    ap.add_argument("--select-t4p", action="store_true",
                    help="append the attacker-probe T4p selection to <dir>/selected.jsonl before the analysis")
    ap.add_argument("--n-boot", type=int, default=N_BOOT)
    ap.add_argument("--n-shuffles", type=int, default=N_SHUFFLES)
    a = ap.parse_args(argv)
    main(dir=a.dir, out=a.out, select_t4p=a.select_t4p, n_boot=a.n_boot, n_shuffles=a.n_shuffles, acts_dir=a.acts)


if __name__ == "__main__":
    cli()
