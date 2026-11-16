"""Pillar 1: which provenance channel the agent follows, and confidence laundering.

Input: ``p1_pairs.jsonl`` (one row per trial; ``followed`` = chosen channel, "escalate", "distractor",
"distractor2", "other_value" in single trials, or None = no parsed answer) and ``conf.jsonl``.
Items are episode ids; pooled estimates resample items jointly across victims (see ``analysis.common``).
All shares are proportions (x100 = percent / percentage points); every share's denominator is all trials of
the cell, with unparsed trials as their own category, except where a "dropped" sensitivity is stated.
"""
from __future__ import annotations

import itertools
import warnings
from typing import Optional

import numpy as np
from scipy import optimize, stats
from scipy.special import expit

from memlab.prompts import P1_CHANNELS

from .common import (Clusters, clopper_pearson, clustered_mean, load_jsonl, missing, run_victims, seed_for,
                     summarize)

ALL_PAIRS = list(itertools.combinations(P1_CHANNELS, 2))
OTHERS = P1_CHANNELS[1:]
FRAMING_TRIALS = [("memory", "tool", "first_person", "neutral"), ("memory", "document", "first_person", "neutral"),
                  ("tool", "user", "neutral", "first_person"), ("user", "document", "first_person", "neutral")]
TURN_B = ("tool", "document")
FORCED_B = ("tool", "document", "user")
STALE_B = ("tool", "document", "user")
SINGLE_CHANNELS = ("memory", "tool")
DESIGNS = ("pair", "framing", "turn", "forced", "stale", "single")
BT_RIDGE = 0.05          # L2 penalty on Bradley-Terry abilities (keeps never-winning channels finite)
MIXED_MIN_EVENTS = 5     # mixed model only if both outcomes occur at least this often
POOLED = "pooled"


# ============================================================================ loading
def load_p1(run: str) -> tuple:
    """(trial rows, conf rows) of all victims with a ``victim`` field added; victims without files are
    absent."""
    rows, conf = [], []
    for v in run_victims(run):
        for r in load_jsonl(run, v, "p1_pairs.jsonl") or []:
            rows.append({**r, "victim": v})
        for r in load_jsonl(run, v, "conf.jsonl") or []:
            conf.append({**r, "victim": v})
    return rows, conf


def _neutral(r) -> bool:
    return r["framing_a"] == "neutral" and r.get("framing_b") in ("neutral", None)


def select(rows, design, a=None, b=None, neutral=True):
    return [r for r in rows if r["design"] == design and (a is None or r["ch_a"] == a)
            and (b is None or r.get("ch_b") == b) and (not neutral or _neutral(r))]


def groups(rows) -> dict:
    """{"pooled": rows, victim: rows, ...}; only victims with rows."""
    out = {POOLED: rows}
    for v in sorted({r["victim"] for r in rows}, key=lambda v: [r["victim"] for r in rows].index(v)):
        out[v] = [r for r in rows if r["victim"] == v]
    return out


# ============================================================================ core estimators
def net_preference(rows, side_a: str, side_b: str, drop_missing: bool = False, seed: Optional[int] = None,
                   **extra) -> dict:
    """share(followed == side_a) - share(followed == side_b) with an item-clustered bootstrap CI and a
    two-sided test against 0. Unparsed trials count as following neither side (primary) or are dropped
    (``drop_missing``)."""
    use = [r for r in rows if not (drop_missing and r["followed"] is None)]
    d = [float(r["followed"] == side_a) - float(r["followed"] == side_b) for r in use]
    rec = clustered_mean(d, [r["episode_id"] for r in use], h0=0.0,
                         seed=seed if seed is not None else seed_for("net", side_a, side_b, len(use)), **extra)
    rec["n_missing"] = sum(r["followed"] is None for r in rows)
    rec["n_dropped_missing"] = rec["n_missing"] if drop_missing else 0
    return rec


def share(rows, pred, seed_key, h0=None) -> dict:
    """Clustered share of trials satisfying ``pred`` (denominator: all trials given)."""
    return clustered_mean([float(pred(r)) for r in rows], [r["episode_id"] for r in rows], h0=h0,
                          seed=seed_for("share", *seed_key), proportion=True)


def outcome_shares(rows, a: str, b: Optional[str], key) -> dict:
    """Shares follows-a / follows-b / escalate / distractor / unparsed for one cell."""
    out = {"n": len(rows),
           "follows_a": share(rows, lambda r: r["followed"] == a, (*key, "a")),
           "escalate": share(rows, lambda r: r["followed"] == "escalate", (*key, "esc")),
           "distractor": share(rows, lambda r: r["followed"] in ("distractor", "distractor2"), (*key, "dis")),
           "unparsed": share(rows, lambda r: r["followed"] is None, (*key, "na"))}
    if b is not None:
        out["follows_b"] = share(rows, lambda r: r["followed"] == b, (*key, "b"))
        out["net_a_minus_b"] = net_preference(rows, a, b, seed=seed_for("netcell", *key))
    else:
        out["other_value"] = share(rows, lambda r: r["followed"] == "other_value", (*key, "other"))
    return out


def paired_diff(rows_x, rows_y, value, key) -> dict:
    """Mean within-(victim, item) difference value(x) - value(y) over pairs present in both sets, clustered
    by item. ``value`` maps a trial row to a number (unparsed rows map like any other row)."""
    ix = {(r["victim"], r["episode_id"]): r for r in rows_x}
    iy = {(r["victim"], r["episode_id"]): r for r in rows_y}
    common = sorted(set(ix) & set(iy))
    if not common:
        return missing("no item with both trials", n=0)
    d = [value(ix[k]) - value(iy[k]) for k in common]
    rec = clustered_mean(d, [k[1] for k in common], h0=0.0, seed=seed_for("paired", *key))
    rec["mean_x"] = float(np.mean([value(ix[k]) for k in common]))
    rec["mean_y"] = float(np.mean([value(iy[k]) for k in common]))
    return rec


# ============================================================================ model-based check
def mixed_logit(rows, a: str = "memory", b: str = "tool") -> dict:
    """Mixed-effects logistic regression of "follows a" among trials where a or b was chosen, with random
    intercepts for item and victim (variational Bayes, statsmodels ``BinomialBayesMixedGLM``); the intercept
    is tested against 0 (probability 0.5). If either outcome occurs fewer than ``MIXED_MIN_EVENTS`` times the
    model is not estimable: an exact binomial test and Clopper-Pearson interval are reported instead."""
    d = [r for r in rows if r["followed"] in (a, b)]
    n = len(d)
    k = sum(r["followed"] == a for r in d)
    if n == 0:
        return missing("no trial in which a side was chosen", n=0)
    base = {"n": n, "k": k, "share_a": k / n, "n_items": len({r["episode_id"] for r in d}),
            "n_victims": len({r["victim"] for r in d})}
    exact = {"exact_ci": clopper_pearson(k, n), "exact_p_vs_half": float(stats.binomtest(k, n, 0.5).pvalue)}
    if min(k, n - k) < MIXED_MIN_EVENTS:
        return {**base, **exact, "est": None, "ci": [None, None], "estimable": False,
                "reason": f"outcome (near-)degenerate: {k} of {n} trials follow {a} (fewer than "
                          f"{MIXED_MIN_EVENTS} of one outcome); mixed model not estimable, exact binomial "
                          f"interval and test reported instead (they ignore clustering)"}
    import pandas as pd
    from statsmodels.genmod.bayes_mixed_glm import BinomialBayesMixedGLM
    df = pd.DataFrame({"y": [float(r["followed"] == a) for r in d], "item": [r["episode_id"] for r in d],
                       "victim": [r["victim"] for r in d]})
    vc = {"item": "0 + C(item)"}
    if base["n_victims"] > 1:
        vc["victim"] = "0 + C(victim)"
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            res = BinomialBayesMixedGLM.from_formula("y ~ 1", vc, df).fit_vb()
    except Exception as e:  # numerical failure is reported, not hidden
        return {**base, **exact, "est": None, "ci": [None, None], "estimable": False,
                "reason": f"mixed model failed: {type(e).__name__}: {e}"}
    b0, sd = float(res.fe_mean[0]), float(res.fe_sd[0])
    z = b0 / sd if sd > 0 else float("nan")
    return {**base, **exact, "estimable": True, "est": float(expit(b0)),
            "ci": [float(expit(b0 - 1.96 * sd)), float(expit(b0 + 1.96 * sd))],
            "intercept_logit": b0, "intercept_sd": sd, "z": z, "p": float(2 * stats.norm.sf(abs(z))),
            "vc_sd": {name: float(np.exp(m)) for name, m in zip(vc, res.vcp_mean)},
            "method": "BinomialBayesMixedGLM.fit_vb; est = inverse-logit of the intercept (population-typical "
                      "item and victim); p from the posterior mean/sd of the intercept vs 0"}


# ============================================================================ Bradley-Terry
def _bt_fit(wins: np.ndarray, ridge: float = BT_RIDGE) -> np.ndarray:
    """Abilities (centred, log-odds scale) maximising sum_ij wins[i,j] log sigmoid(b_i - b_j) - ridge |b|^2."""
    m = wins.shape[0]

    def f(b):
        diff = b[:, None] - b[None, :]
        ll = np.sum(wins * -np.logaddexp(0, -diff))
        p = expit(diff)
        g = (wins * (1 - p)).sum(1) - (wins * (1 - p)).sum(0)
        return -ll + ridge * b @ b, -g + 2 * ridge * b

    r = optimize.minimize(f, np.zeros(m), jac=True, method="L-BFGS-B")
    return r.x - r.x.mean()


def bradley_terry(rows, key) -> dict:
    """Bradley-Terry abilities of the seven channels from neutral head-to-head trials where a side was chosen,
    with an item-clustered bootstrap (the bootstrap re-fits the model on resampled win counts)."""
    d = [r for r in rows if r["design"] == "pair" and _neutral(r) and r["followed"] in (r["ch_a"], r["ch_b"])]
    if not d:
        return missing("no head-to-head trial with a side chosen")
    ci = {c: i for i, c in enumerate(P1_CHANNELS)}
    m = len(P1_CHANNELS)
    cl = Clusters([r["episode_id"] for r in d], seed=seed_for("bt", *key))
    # per-cluster win counts: (k, m*m)
    per = np.zeros((cl.k, m * m))
    for r, c in zip(d, cl.idx):
        w, l = (r["ch_a"], r["ch_b"]) if r["followed"] == r["ch_a"] else (r["ch_b"], r["ch_a"])
        per[c, ci[w] * m + ci[l]] += 1
    wins = per.sum(0).reshape(m, m)
    est = _bt_fit(wins)
    reps = np.array([_bt_fit((w @ per).reshape(m, m)) for w in cl.W])
    n_trials = wins + wins.T
    out = {"n": len(d), "n_clusters": cl.k, "ridge": BT_RIDGE, "scale": "log-odds, centred to mean 0",
           "abilities": {}, "note": None}
    flagged = []
    for c, i in ci.items():
        won, lost = wins[i].sum(), wins[:, i].sum()
        if won == 0 or lost == 0:
            flagged.append(f"{c} ({'never won' if won == 0 else 'never lost'})")
        out["abilities"][c] = summarize(est[i], reps[:, i], int(n_trials[i].sum()), cl.k, wins=int(won),
                                        losses=int(lost))
    if flagged:
        out["note"] = ("maximum-likelihood abilities are infinite for " + ", ".join(flagged) +
                       f"; the ridge penalty {BT_RIDGE} keeps them finite, so their values reflect the "
                       "penalty and only their order is interpretable")
    return out


# ============================================================================ confidence laundering
def laundering(rows, field: str, key) -> dict:
    """(certain - hedged | memory) - (certain - hedged | tool) for ``field`` ("confidence" or "act"),
    from cell means with an item-clustered bootstrap. Rows with a missing value are dropped (counted)."""
    use = [r for r in rows if r.get(field) is not None]
    n_drop = len(rows) - len(use)
    if not use:
        return missing("no rows", n_dropped=n_drop)
    cl = Clusters([r["episode_id"] for r in use], seed=seed_for("laund", field, *key))
    x = np.array([float(r[field]) for r in use])
    cells, obs, reps, ns = {}, {}, {}, {}
    for ch in ("memory", "tool"):
        for lev in ("hedged", "certain"):
            msk = np.array([float(r["channel"] == ch and r["level"] == lev) for r in use])
            ns[(ch, lev)] = int(msk.sum())
            if msk.sum() == 0:
                return missing(f"no {ch}/{lev} trials", n=len(use), n_dropped=n_drop)
            obs[(ch, lev)] = (x * msk).sum() / msk.sum()
            with np.errstate(invalid="ignore", divide="ignore"):
                reps[(ch, lev)] = cl.boot(x * msk) / cl.boot(msk)
            cells[f"{ch}_{lev}"] = summarize(obs[(ch, lev)], reps[(ch, lev)], ns[(ch, lev)], cl.k)

    def lau(v):
        return (v[("memory", "certain")] - v[("memory", "hedged")]) - (v[("tool", "certain")] - v[("tool", "hedged")])

    rec = summarize(lau(obs), lau(reps), len(use), cl.k, 0.0, n_dropped=n_drop)
    rec["effect_memory"] = summarize(obs[("memory", "certain")] - obs[("memory", "hedged")],
                                     reps[("memory", "certain")] - reps[("memory", "hedged")], len(use), cl.k, 0.0)
    rec["effect_tool"] = summarize(obs[("tool", "certain")] - obs[("tool", "hedged")],
                                   reps[("tool", "certain")] - reps[("tool", "hedged")], len(use), cl.k, 0.0)
    rec["cells"] = cells
    return rec


# ============================================================================ full analysis
def primary(rows) -> dict:
    """Primary estimand 1 (pooled over all victims present) plus per-victim estimates and checks."""
    pr = select(rows, "pair", "memory", "tool")
    if not pr:
        return {"pooled": missing("no memory-vs-tool head-to-head trials")}
    out = {}
    for g, rs in groups(pr).items():
        out[g] = {"net": net_preference(rs, "memory", "tool", seed=seed_for("prim1", g)),
                  "net_dropping_unparsed": net_preference(rs, "memory", "tool", drop_missing=True,
                                                          seed=seed_for("prim1s", g)),
                  "share_memory": share(rs, lambda r: r["followed"] == "memory", ("prim1m", g)),
                  "share_tool": share(rs, lambda r: r["followed"] == "tool", ("prim1t", g))}
    out["mixed_model"] = mixed_logit(pr)
    out["by_family"] = {f: net_preference([r for r in pr if r["family"] == f], "memory", "tool",
                                          seed=seed_for("prim1f", f))
                        for f in sorted({r["family"] for r in pr})}
    out["by_variant"] = {str(v): net_preference([r for r in pr if r["variant"] == v], "memory", "tool",
                                                seed=seed_for("prim1v", v))
                         for v in sorted({r["variant"] for r in pr})}
    return out


SECONDARY_DESIGNS = ("turn", "forced", "single", "stale")
BALANCED_SEEDS = range(50, 70)          # 20 items per task family = 60 items
BALANCED_MIN_ITEMS = 54                 # 90% of 60


def _seed(r) -> int:
    return int(r["episode_id"].rsplit("-", 1)[1])


def secondary_scope(rows) -> tuple:
    """Scope of the four secondary trial designs (DECISIONS.md, 16 Nov). Before the outage these designs had
    run on the items reached in family-major order, which is the inventory family almost alone. After the
    core stages they were run on seeds 50-69 of every family (60 items). Rule, applied per design: if every
    model has at least 90% of those 60 items, the design is analysed on seeds 50-69 only, so that families
    and models are balanced; otherwise on all items collected. Returns (rows, {design: scope record})."""
    victims = sorted({r["victim"] for r in rows})
    scope, drop = {}, set()
    for d in SECONDARY_DESIGNS:
        rs = [r for r in rows if r["design"] == d]
        per_v = {v: len({r["episode_id"] for r in rs if r["victim"] == v and _seed(r) in BALANCED_SEEDS}) for v in victims}
        balanced = bool(rs) and min(per_v.values(), default=0) >= BALANCED_MIN_ITEMS
        if balanced:
            drop.add(d)
        kept = [r for r in rs if not balanced or _seed(r) in BALANCED_SEEDS]
        fam = {}
        for r in kept:
            fam.setdefault(r["family"], set()).add(r["episode_id"])
        scope[d] = {"balanced_seeds_50_69": balanced, "items_per_victim_in_seeds_50_69": per_v,
                    "n_trials": len(kept), "n_items": len({r["episode_id"] for r in kept}),
                    "items_per_family": {f: len(x) for f, x in sorted(fam.items())},
                    "n_trials_left_out": len(rs) - len(kept)}
    rows = [r for r in rows if r["design"] not in drop or _seed(r) in BALANCED_SEEDS]
    return rows, scope


def analyse(run: str) -> dict:
    rows, conf = load_p1(run)
    rows, scope = secondary_scope(rows)
    res = {"n_trials": len(rows), "victims": sorted({r["victim"] for r in rows}),
           "n_items": len({r["episode_id"] for r in rows}), "secondary_scope": scope}
    if not rows:
        res["reason"] = "no p1_pairs.jsonl for this run"
    # parse rates
    res["parse"] = [{"victim": v, "design": d, "n": len(rs), "parsed": sum(r["followed"] is not None for r in rs),
                     "errors_degenerate": sum(bool(r.get("error")) and "degenerate" in r["error"] for r in rs)}
                    for v, vr in groups(rows).items() for d in DESIGNS
                    for rs in [[r for r in vr if r["design"] == d]] if rs]
    res["primary"] = primary(rows) if rows else {"pooled": missing("no rows")}
    # every neutral head-to-head pair, pooled and per victim (memory vs X are the first six)
    res["pairs"] = []
    for design in ("pair", "forced", "stale"):
        for a, b in ALL_PAIRS:
            cell = select(rows, design, a, b)
            if not cell:
                continue
            for g, rs in groups(cell).items():
                res["pairs"].append({"design": design, "ch_a": a, "ch_b": b, "group": g,
                                     **outcome_shares(rs, a, b, (design, a, b, g))})
    # win matrix (neutral pair trials, side chosen)
    res["win_matrix"] = []
    for g, rs in groups(select(rows, "pair")).items():
        for x, y in itertools.permutations(P1_CHANNELS, 2):
            a, b = sorted((x, y), key=P1_CHANNELS.index)
            dec = [r for r in rs if r["ch_a"] == a and r["ch_b"] == b and r["followed"] in (a, b)]
            if dec:
                res["win_matrix"].append({"group": g, "row": x, "col": y,
                                          **share(dec, lambda r, x=x: r["followed"] == x, ("win", g, x, y))})
    res["bradley_terry"] = {g: bradley_terry(rs, (g,)) for g, rs in groups(select(rows, "pair")).items()}
    # framing (H1b), paired with the neutral pair trial of the same item
    res["framing"] = []
    for a, b, fa, fb in FRAMING_TRIALS:
        side = a if fa == "first_person" else b
        fr = [r for r in rows if r["design"] == "framing" and r["ch_a"] == a and r["ch_b"] == b
              and r["framing_a"] == fa and r["framing_b"] == fb]
        if not fr:
            continue
        nt = select(rows, "pair", a, b)
        for g in groups(fr):
            frg = fr if g == POOLED else [r for r in fr if r["victim"] == g]
            ntg = nt if g == POOLED else [r for r in nt if r["victim"] == g]
            res["framing"].append({
                "framed": side, "ch_a": a, "ch_b": b, "against": b if side == a else a, "group": g,
                "follow_framed_side": paired_diff(frg, ntg, lambda r: float(r["followed"] == side), ("fr", a, b, g)),
                "escalate": paired_diff(frg, ntg, lambda r: float(r["followed"] == "escalate"), ("fre", a, b, g))})
    # framing pooled over the two trials of each framed channel (memory: vs tool and vs document)
    res["framing_by_channel"] = {}
    for side in ("memory", "user"):
        trials = [(a, b) for a, b, fa, fb in FRAMING_TRIALS if (a if fa == "first_person" else b) == side]
        fr = [r for r in rows if r["design"] == "framing" and (r["ch_a"], r["ch_b"]) in trials]
        nt = [r for r in select(rows, "pair") if (r["ch_a"], r["ch_b"]) in trials]
        key_fr = {(r["victim"], r["episode_id"], r["ch_a"], r["ch_b"]): r for r in fr}
        key_nt = {(r["victim"], r["episode_id"], r["ch_a"], r["ch_b"]): r for r in nt}
        common = sorted(set(key_fr) & set(key_nt))
        if common:
            d = [float(key_fr[k]["followed"] == side) - float(key_nt[k]["followed"] == side) for k in common]
            res["framing_by_channel"][side] = clustered_mean(d, [k[1] for k in common], h0=0.0,
                                                             seed=seed_for("frch", side))
        else:
            res["framing_by_channel"][side] = missing("no paired framing trials")
    # turn vs labelled memory
    res["turn"] = []
    for b in TURN_B:
        tr, nt = select(rows, "turn", "memory", b), select(rows, "pair", "memory", b)
        if tr:
            for g in groups(tr):
                trg = tr if g == POOLED else [r for r in tr if r["victim"] == g]
                ntg = nt if g == POOLED else [r for r in nt if r["victim"] == g]
                res["turn"].append({"against": b, "group": g,
                                    "follow_memory": paired_diff(trg, ntg, lambda r: float(r["followed"] == "memory"), ("tu", b, g)),
                                    "escalate": paired_diff(trg, ntg, lambda r: float(r["followed"] == "escalate"), ("tue", b, g))})
    # staleness control (amendment 1): memory vs X with X also from an earlier session, vs the unmarked pair
    res["stale"] = []
    for b in STALE_B:
        st, nt = select(rows, "stale", "memory", b), select(rows, "pair", "memory", b)
        if st:
            for g in groups(st):
                stg = st if g == POOLED else [r for r in st if r["victim"] == g]
                ntg = nt if g == POOLED else [r for r in nt if r["victim"] == g]
                have = {(r["victim"], r["episode_id"]) for r in stg}
                ntm = [r for r in ntg if (r["victim"], r["episode_id"]) in have]   # unmarked trials, same items
                res["stale"].append({"against": b, "group": g,
                                     **{f"diff_{o}": paired_diff(stg, ntg, lambda r, o=o: float(r["followed"] == o), ("st", b, g, o))
                                        for o in ("memory", b, "escalate")},
                                     "net_stale": net_preference(stg, "memory", b, seed=seed_for("stnet", b, g)),
                                     "net_unmarked": net_preference(ntm, "memory", b, seed=seed_for("stnu", b, g))})
    # single-claim (no conflict) adoption
    res["single"] = []
    for ch in SINGLE_CHANNELS:
        sg = [r for r in rows if r["design"] == "single" and r["ch_a"] == ch]
        for g, rs in (groups(sg).items() if sg else []):
            res["single"].append({"channel": ch, "group": g, **outcome_shares(rs, ch, None, ("single", ch, g))})
    sm = [r for r in rows if r["design"] == "single" and r["ch_a"] == "memory"]
    stl = [r for r in rows if r["design"] == "single" and r["ch_a"] == "tool"]
    res["single_memory_minus_tool"] = {
        g: paired_diff([r for r in sm if g == POOLED or r["victim"] == g], [r for r in stl if g == POOLED or r["victim"] == g],
                       lambda r: float(r["followed"] == r["ch_a"]), ("single", g))
        for g in groups(sm + stl)} if sm and stl else {POOLED: missing("no single-claim trials")}
    # position effect: share following the first-shown claim among trials where a side was chosen
    pos = [r for r in rows if r["design"] in ("pair", "framing", "forced", "stale") and r["a_first"] is not None
           and r["followed"] in (r["ch_a"], r["ch_b"])]
    res["position_first_shown"] = {g: share(rs, lambda r: (r["followed"] == r["ch_a"]) == bool(r["a_first"]),
                                            ("pos", g), h0=0.5)
                                   for g, rs in groups(pos).items()} if pos else {POOLED: missing("no trials")}
    # escalation and stated confidence by design
    res["by_design"] = []
    for d in DESIGNS:
        dr = [r for r in rows if r["design"] == d]
        for g, rs in (groups(dr).items() if dr else []):
            chosen = [r for r in rs if r["followed"] not in (None, "escalate")]
            esc = [r for r in rs if r["followed"] == "escalate"]
            res["by_design"].append({
                "design": d, "group": g, "n": len(rs),
                "escalate": share(rs, lambda r: r["followed"] == "escalate", ("desc", d, g)),
                "confidence_all": clustered_mean([r["confidence"] for r in rs], [r["episode_id"] for r in rs],
                                                 seed=seed_for("conf", d, g)),
                "confidence_side_chosen": clustered_mean([r["confidence"] for r in chosen],
                                                         [r["episode_id"] for r in chosen], seed=seed_for("confc", d, g)),
                "confidence_escalate": clustered_mean([r["confidence"] for r in esc], [r["episode_id"] for r in esc],
                                                      seed=seed_for("confe", d, g))})
    # per-family and per-phrasing breakdown of memory against any other channel (neutral pairs)
    mx = [r for r in select(rows, "pair", "memory")]
    res["memory_vs_any"] = {}
    for dim in ("family", "variant"):
        res["memory_vs_any"][dim] = []
        for val in sorted({r[dim] for r in mx}, key=str):
            rs = [r for r in mx if r[dim] == val]
            res["memory_vs_any"][dim].append({
                dim: val, "n": len(rs),
                "follows_memory": share(rs, lambda r: r["followed"] == "memory", ("mxa", dim, val)),
                "follows_other": share(rs, lambda r: r["followed"] == r["ch_b"], ("mxo", dim, val)),
                "escalate": share(rs, lambda r: r["followed"] == "escalate", ("mxe", dim, val))})
    # confidence laundering (H1c)
    res["laundering"] = {}
    for g, cr in (groups(conf).items() if conf else []):
        res["laundering"][g] = {f: laundering(cr, f, (g,)) for f in ("confidence", "act")}
    if not conf:
        res["laundering"][POOLED] = {f: missing("no conf.jsonl for this run") for f in ("confidence", "act")}
    return res
