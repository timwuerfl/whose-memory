"""Offline tests of the analysis code on synthetic data with known answers."""
from __future__ import annotations

import numpy as np
import pytest

from analysis import common as C
from analysis import detection, hosted, p1, p4
from analysis.check_numbers import check
from analysis.numbers import mname


# ------------------------------------------------------------------ AUROC and TPR at fixed FPR
def test_auroc_known_value_with_ties():
    # pairs: 1>0 (1), 1=1 (0.5), 2 and 3 beat both (4) -> 5.5 / 6
    assert C.auroc([1, 2, 3], [0, 1]) == pytest.approx(5.5 / 6)
    assert C.auroc([1, None], [0]) == 1.0


def test_auroc_matches_mann_whitney():
    rng = np.random.default_rng(0)
    pos, neg = rng.integers(0, 10, 40), rng.integers(0, 8, 55)
    brute = np.mean([(p > q) + 0.5 * (p == q) for p in pos for q in neg])
    assert C.auroc(pos, neg) == pytest.approx(brute)


def test_auroc_empty_class_is_none():
    assert C.auroc([], [1, 2]) is None
    assert C.auroc([1], [None]) is None


def test_tpr_at_fpr_threshold_rule():
    neg, pos = list(range(100)), list(range(50, 150))
    # tau = 94 (5 negatives above it), TPR = share(pos > 94) = 55/100
    assert C.tpr_at_fpr(pos, neg, 0.05) == pytest.approx(0.55)
    # ties at tau are not flagged
    assert C.tpr_at_fpr([1, 2], [1, 1, 1], 0.05) == pytest.approx(0.5)
    assert C.tpr_at_fpr([], [1], 0.05) is None


def test_roc_cell_records_and_replicates():
    rng = np.random.default_rng(1)
    eps = [f"e{i}" for i in range(30)]
    pos = rng.normal(1, 1, 30)
    neg = rng.normal(0, 1, 60)
    rec, reps = C.roc_cell(pos, eps, neg, eps * 2, seed=3, h0=0.5)
    a = rec["auroc"]
    assert a["n"] == 90 and a["n_clusters"] == 30 and reps.shape == (C.N_BOOT,)
    assert a["ci"][0] < a["est"] < a["ci"][1]
    assert a["p"] < 0.05
    assert rec["tpr@0.05"]["fpr_realised"] <= 0.05
    empty, r = C.roc_cell([], [], [1.0], ["e"])
    assert empty["auroc"]["est"] is None and r is None


# ------------------------------------------------------------------ bootstrap, p-values, intervals
def test_cluster_bootstrap_coverage_toy():
    """95% CI of a clustered mean covers the true mean in roughly 95% of simulated data sets."""
    rng = np.random.default_rng(2)
    hits, sims = 0, 120
    for s in range(sims):
        k, m = 30, 6
        u = rng.normal(0, 1, k)                                   # cluster effects
        x = (u[:, None] + rng.normal(0, 1, (k, m))).ravel()       # true mean 0
        cl = np.repeat(np.arange(k), m)
        rec = C.clustered_mean(list(x), list(cl), seed=s)
        hits += rec["ci"][0] <= 0 <= rec["ci"][1]
    assert 0.85 <= hits / sims <= 0.995


def test_boot_p_and_holm():
    assert C.boot_p(np.full(1999, 1.0), 0.0) == pytest.approx(2 / 2000)
    assert C.boot_p(np.array([-1.0, 1.0] * 500), 0.0) == pytest.approx(1.0)
    adj = C.holm({"a": 0.01, "b": 0.04, "c": 0.03, "d": None})
    assert adj["a"] == pytest.approx(0.03) and adj["c"] == pytest.approx(0.06)
    assert adj["b"] == pytest.approx(0.06) and adj["d"] is None


def test_exact_intervals_at_zero():
    lo, hi = C.clopper_pearson(0, 10)
    assert lo == 0 and hi == pytest.approx(1 - 0.025 ** 0.1)
    rec = C.clustered_mean([0.0] * 10, list(range(10)), proportion=True)
    assert rec["est"] == 0 and rec["ci"][1] == pytest.approx(hi) and "clopper" in rec["ci_method"]
    w = C.wilson(5, 10)
    assert w[0] < 0.5 < w[1]


def test_victim_average_and_empty():
    r1, r2 = np.full(C.N_BOOT, 0.6), np.full(C.N_BOOT, 0.8)
    rec = C.victim_average({"a": (0.6, r1, 10), "b": (0.8, r2, 20)})
    assert rec["est"] == pytest.approx(0.7) and rec["n"] == 30 and rec["n_victims"] == 2
    assert C.victim_average({})["est"] is None
    assert C.clustered_mean([], [])["est"] is None


# ------------------------------------------------------------------ Pillar 1
def _trial(eid, followed, victim="v1", **kw):
    return {"episode_id": eid, "victim": victim, "followed": followed, "design": "pair", "ch_a": "memory",
            "ch_b": "tool", "framing_a": "neutral", "framing_b": "neutral", **kw}


def test_net_preference_primary_and_sensitivity():
    rows = [_trial("e1", "memory"), _trial("e2", "tool"), _trial("e3", "tool"), _trial("e4", None)]
    rec = p1.net_preference(rows, "memory", "tool")
    assert rec["est"] == pytest.approx((1 - 2) / 4) and rec["n"] == 4 and rec["n_missing"] == 1
    sens = p1.net_preference(rows, "memory", "tool", drop_missing=True)
    assert sens["est"] == pytest.approx(-1 / 3) and sens["n"] == 3


def test_mixed_logit_degenerate_reports_exact():
    rows = [_trial(f"e{i}", "tool") for i in range(12)]
    rec = p1.mixed_logit(rows)
    assert rec["estimable"] is False and rec["est"] is None
    assert rec["exact_ci"][0] == 0 and rec["exact_p_vs_half"] < 0.001


def test_laundering_known_value():
    rows = []
    for i in range(10):
        for ch, h, c in (("memory", 20, 90), ("tool", 30, 80)):
            rows.append({"episode_id": f"e{i}", "channel": ch, "level": "hedged", "confidence": h, "act": False})
            rows.append({"episode_id": f"e{i}", "channel": ch, "level": "certain", "confidence": c, "act": True})
    rec = p1.laundering(rows, "confidence", ("t",))
    assert rec["est"] == pytest.approx((90 - 20) - (80 - 30))
    assert p1.laundering([], "act", ("t",))["est"] is None


def test_bradley_terry_orders_channels():
    rows = []
    for i in range(20):
        rows.append(_trial(f"e{i}", "tool"))                                  # tool beats memory
        rows.append(_trial(f"e{i}", "document", ch_a="tool", ch_b="document"))   # document beats tool
    bt = p1.bradley_terry(rows, ("t",))
    ab = {c: a["est"] for c, a in bt["abilities"].items()}
    assert ab["document"] > ab["tool"] > ab["memory"]
    assert "memory" in bt["note"]


# ------------------------------------------------------------------ Pillar 4
def _p4(eid, cond, attacked, tier="T2", victim="v1", edit="E1"):
    return {"episode_id": eid, "victim": victim, "condition": cond, "tier": tier, "target_edit": edit,
            "is_target": True, "store": f"{edit}:{tier}", "attacked": attacked, "correct": None if attacked is None else not attacked}


def test_relative_asr_reduction():
    none = [_p4(f"e{i}", "none", i < 8) for i in range(10)]          # ASR 0.8
    g1 = [_p4(f"e{i}", "G1", i < 2) for i in range(10)]              # ASR 0.2
    red = p4.reduction(g1, none, ("t",))
    assert red["relative"]["est"] == pytest.approx(0.75)
    assert red["absolute"]["est"] == pytest.approx(-0.6)
    # unparsed counts as failed in the primary, dropped in the sensitivity analysis
    g1u = g1[:-1] + [_p4("e9", "G1", None)]
    assert p4.reduction(g1u, none, ("t",))["relative"]["est"] == pytest.approx(0.75)
    assert p4.reduction(g1u, none, ("t",), drop_unparsed=True)["relative"]["est"] == pytest.approx(1 - (2 / 9) / 0.8)


def test_relative_reduction_undefined_when_reference_zero():
    none = [_p4(f"e{i}", "none", False) for i in range(5)]
    g1 = [_p4(f"e{i}", "G1", False) for i in range(5)]
    assert p4.reduction(g1, none, ("t",))["relative"]["est"] is None


# ------------------------------------------------------------------ graceful handling of missing data
def test_empty_run_does_not_crash():
    run = "no_such_run_for_tests"
    a, d, b = p1.analyse(run), detection.analyse(run), p4.analyse(run)
    assert a["n_trials"] == 0 and d["victims"] == [] and b["n_rows"] == 0
    block = hosted.primary_block(a, d, b)
    assert all(v["est"] is None and v["supported"] is None for v in block.values())
    assert b["primary4"]["est"] is None and "G1" in b["primary4"]["reason"]


# ------------------------------------------------------------------ numbers and the checker
def test_macro_names_have_no_digits():
    assert mname("Det", "DeepSeek-V4-Flash", "T2") == "DetDeepSeekVFourFlashTTwo"
    assert not any(ch.isdigit() for ch in mname("G1+G2s", "T0"))


def test_check_numbers(tmp_path):
    (tmp_path / "numbers.tex").write_text("\\newcommand{\\PrimSelfTrust}{1.0}\n\\newcommand{\\PrimGate}{n/a}\n"
                                          "\\newcommand{\\DetUnused}{0.5}\n")
    (tmp_path / "main.tex").write_text("\\documentclass{article}\n\\begin{document}\n"
                                       "Net \\PrimSelfTrust{} and \\PrimGate{} and \\PoneMissing{}.\n"
                                       "A literal 12.5 and 40\\% here, \\cite{x2.1}.\n\\end{document}\n")
    r = check(tmp_path / "main.tex", tmp_path / "numbers.tex")
    assert r["undefined"] == ["PoneMissing"]
    assert r["unused"] == ["DetUnused"] and r["used_na"] == ["PrimGate"]
    assert len(r["literals"]) == 2


def test_mixed_logit_fits_when_both_outcomes_occur():
    rng = np.random.default_rng(4)
    rows = [_trial(f"e{i}", "memory" if rng.random() < 0.3 else "tool", victim=v)
            for i in range(40) for v in ("v1", "v2")]
    rec = p1.mixed_logit(rows)
    assert rec["estimable"] is True
    assert 0.1 < rec["est"] < 0.5 and rec["ci"][0] < rec["est"] < rec["ci"][1] and 0 <= rec["p"] <= 1


# ------------------------------------------------------------------ detection: episode clusters, store audits
def _entries(eid, store, scores, forged_slot=None, tier=None):
    return [{"episode_id": eid, "slot": s, "kind": "forged" if s == forged_slot else "genuine", "store": store,
             "tier": tier if s == forged_slot else None, "edit_type": "E1" if s == forged_slot else None,
             "raw": 100 - x, "score": float(x)} for s, x in enumerate(scores)]


def _synthetic_victim(rng, n_eps=10):
    ents = []
    for i in range(n_eps):
        eid = f"inventory-{i:05d}"
        ents += _entries(eid, "clean", list(rng.integers(0, 5, 7)))
        ents += _entries(eid, "E1:T2", list(rng.integers(0, 5, 6)) + [int(rng.integers(0, 10))], forged_slot=6, tier="T2")
    return {"entries": {"V": ents}, "validity_check": {}, "forged_jsonl": True}


def test_victim_average_reports_episode_clusters(monkeypatch):
    rng = np.random.default_rng(5)
    data = {"deepseek-v4-flash": _synthetic_victim(rng), "gemma-4-31b-it": _synthetic_victim(rng, 8)}
    monkeypatch.setattr(detection, "run_victims", lambda run: list(data))
    monkeypatch.setattr(detection, "load_victim", lambda run, v: data[v])
    res = detection.analyse("synthetic")
    p2 = res["primary2"]["T2"]
    assert p2["n_victims"] == 2 and p2["n_clusters"] == 18          # episodes, not victims
    assert p2["per_victim_n_clusters"] == {"deepseek-v4-flash": 10, "gemma-4-31b-it": 8}
    assert p2["ci"][0] < p2["ci"][1]                                 # replicates vary: episodes are resampled
    # the per-victim weight matrix has one column per episode of that victim
    keys, W = detection.victim_weights("gemma-4-31b-it", data["gemma-4-31b-it"])
    assert len(keys) == 8 and W.shape == (C.N_BOOT, 8) and np.all(W.sum(1) == 8)


def test_flat_audit_and_within_store_rank():
    ents = (_entries("e1", "clean", [3] * 7) + _entries("e2", "clean", [1, 2, 3, 4, 5, 6, 7])
            + _entries("e1", "E1:T2", [1, 1, 1, 1, 1, 1, 9], forged_slot=6, tier="T2")     # strictly highest
            + _entries("e2", "E1:T2", [1, 1, 9, 1, 1, 1, 9], forged_slot=6, tier="T2")     # tied highest
            + _entries("e3", "E1:T2", [1, 1, 9, 1, 1, 1, 2], forged_slot=6, tier="T2")     # not highest
            + _entries("e4", "E1:T2", [5] * 7, forged_slot=6, tier="T2"))                  # flat store
    flat, rank = detection.store_audits({"v": {"entries": {"V": ents}}})
    f = {(r["group"], r["store"]): r["flat_rate"]["est"] for r in flat if r["detector"] == "V"}
    assert f[("pooled", "clean")] == pytest.approx(0.5) and f[("pooled", "T2")] == pytest.approx(0.25)
    rk = [r for r in rank if r["group"] == "pooled" and r["tier"] == "T2"][0]
    assert rk["forged_strictly_highest"]["est"] == pytest.approx(0.25)
    assert rk["forged_highest_incl_ties"]["est"] == pytest.approx(0.75)
    assert rk["chance"] == pytest.approx(1 / 7)


def test_r_genuine_disagreement():
    ents = [{"episode_id": f"e{i}", "slot": 0, "kind": "genuine", "store": "pairwise", "tier": None,
             "edit_type": None, "raw": x, "score": float(x)} for i, x in enumerate([0, 50, 100, 10])]
    out = detection.r_genuine_disagreement({"v": {"entries": {"R": ents}}})
    assert out[0]["group"] == "pooled" and out[0]["p_altered_ge_50"]["est"] == pytest.approx(0.5)
