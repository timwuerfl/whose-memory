"""Offline tests for analysis/local.py (+ figures/tables) on synthetic registries with planted structure."""
from __future__ import annotations

import hashlib
import json
import re
import shutil
import sys
from pathlib import Path

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from analysis import local as L  # noqa: E402
from memlab import config as C  # noqa: E402
from memlab.local import pipeline as P  # noqa: E402
from memlab.schema import EDIT_TYPES, FAMILIES  # noqa: E402

D_MODEL, N_LAYERS, LAYERS = 16, 4, [8, 16, 24, 32]
WORDS = "alpha beta gamma delta invoice supplier credit order paper review meeting budget".split()


def _note(rng, tag):
    return f"{tag} " + " ".join(rng.choice(WORDS, size=12)) + "."


def make_run(tmp: Path, seeds=range(50, 66), *, with_cands=True, with_t1=True, with_other=True, with_selected=True,
             signal=2.5, seed=0) -> Path:
    """Synthetic registry in the pipeline's file layout. Planted: other-model notes shift dim 0 at layer
    index 2 (self-authorship); valid forgeries shift dim 1 at layer index 1 (consistency); candidate k shifts
    dim 0 by +0.4*k (less 'own' for larger k)."""
    rng = np.random.default_rng(seed)
    run, acts = tmp / "run", tmp / "acts"
    run.mkdir(parents=True)
    (run / "config.json").write_text(json.dumps({"acts_dir": str(acts)}))
    items, scores, ext, idx = [], [], [], []
    mean = {"s_trace": [], "s_blind": []}
    last = {"s_trace": [], "s_blind": []}
    main = [f"{f}-{s:05d}" for s in seeds for f in FAMILIES]
    for e in main:
        fam = e.split("-")[0]
        for et in C.t3_subset(e):
            s = EDIT_TYPES.index(et)
            kinds = [("genuine", P.gid(e, s), None, None)]
            for t in ("T0", "T1", "T2"):
                if t == "T1" and not with_t1:
                    continue
                kinds.append((t, P.fid(t, e, et), None, True))
            if with_cands:
                kinds += [("cand", P.cid(e, et, k), k, k % 4 != 3) for k in range(8)]
            if with_other:
                kinds += [(f"other:{m}", P.oid(m, e, s), None, None) for m in ("mA", "mB")]
            for kind, iid, k, valid in kinds:
                note = _note(rng, kind.split(":")[0])
                sha = P.note_sha(note)
                items.append({"item_id": iid, "kind": kind, "episode_id": e, "family": fam, "edit_type": et,
                              "session_idx": s, "cand_idx": k, "valid": valid, "note": note, "note_sha": sha,
                              "passes": list(P.passes_for(kind))})
                forged = kind in ("T0", "T1", "T2", "cand")
                other = kind.startswith("other")
                for p in ("s_trace", "s_blind"):
                    m = 2.0 + rng.normal() * 0.3 + (0.5 if forged and p == "s_trace" else 0) + (0.4 if other else 0)
                    scores.append({"item_id": iid, "pass": p, "note_sha": sha, "mean": m, "max": m + 3, "sum": m * 30,
                                   "n": 30 + int(rng.integers(0, 10))})
                    a = rng.normal(size=(N_LAYERS, D_MODEL))
                    if other:
                        a[2, 0] += signal
                    if forged:
                        a[1, 1] += signal
                    if kind == "cand":
                        a[2, 0] += 0.4 * k
                    mean[p].append((iid, sha, a))
                    last[p].append((iid, sha, rng.normal(size=(N_LAYERS, D_MODEL))))
                if not other:
                    scores.append({"item_id": iid, "pass": "c", "note_sha": sha,
                                   "p_yes": float(np.clip(0.8 - 0.3 * forged + rng.normal() * 0.1, 0, 1))})
                    scores.append({"item_id": iid, "pass": "v", "note_sha": sha,
                                   "p_yes": float(np.clip(0.6 + rng.normal() * 0.1, 0, 1))})
                if kind == "cand":
                    scores.append({"item_id": iid, "pass": "v_att", "note_sha": sha, "p_yes": float(rng.random())})
                ext.append({"item_id": iid, "note_sha": sha, "gpt2_mean": 4 + rng.normal(), "small_mean": 3 + rng.normal(),
                            "small_trace_mean": 2 + rng.normal()})
    for p in ("s_trace", "s_blind"):
        (acts / p).mkdir(parents=True)
        name = f"{p}/shard_0"
        np.savez(acts / (name + ".npz"), mean=np.stack([a for _, _, a in mean[p]]).astype(np.float16),
                 last=np.stack([a for _, _, a in last[p]]).astype(np.float16))
        (acts / (name + ".json")).write_text(json.dumps({"meta": {"pass": p, "layers": LAYERS}}))
        idx += [{"pass": p, "item_id": i, "note_sha": sh, "shard": name + ".npz", "row": r}
                for r, (i, sh, _) in enumerate(mean[p])]
    P.write_jsonl_atomic(run / "items.jsonl", items)
    P.write_jsonl_atomic(run / "scores.jsonl", scores)
    P.write_jsonl_atomic(run / "external.jsonl", ext)
    P.write_jsonl_atomic(acts / "index.jsonl", idx)
    if with_selected and with_cands:
        df = P.load_scores(run)
        P.write_jsonl_atomic(run / "selected.jsonl", P.select_all(df[df["kind"] == "cand"].to_dict("records")))
    return run


def _sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else ""


# ------------------------------------------------------------------------------------------------
def test_roc_boot_matches_sklearn():
    from sklearn.metrics import roc_auc_score, roc_curve
    rng = np.random.default_rng(1)
    s = np.round(rng.normal(size=400), 1)          # many ties
    y = (rng.random(400) < 0.4).astype(int)
    s[y == 1] += 0.5
    auc, t1, t5 = L.roc_boot(s, y, np.ones((1, 400), np.float32))
    assert auc[0] == pytest.approx(roc_auc_score(y, s), abs=1e-9)
    assert auc[0] == pytest.approx(L.auc_point(s, y), abs=1e-9)
    fpr, tpr, _ = roc_curve(y, s)
    assert t5[0] == pytest.approx(tpr[fpr <= 0.05].max(), abs=1e-9)
    assert t1[0] == pytest.approx(tpr[fpr <= 0.01].max(), abs=1e-9)


def test_bootstrap_is_deterministic_and_clustered():
    eps = [f"inventory-{i:05d}" for i in range(20)]
    b1, b2 = L.Boot(eps, 100), L.Boot(eps, 100)
    assert np.array_equal(b1.counts, b2.counts)
    assert (b1.counts[1:].sum(1) == len(eps)).all()
    W = b1.W([eps[0], eps[0], eps[3]])
    assert np.array_equal(W[:, 0], W[:, 1])          # items of one episode share their weight


def _synthetic_probe_data(n_per=12, signal=3.0, seed=0):
    rng = np.random.default_rng(seed)
    eps = [f"{f}-{s:05d}" for f in FAMILIES for s in range(50, 50 + n_per)]
    rows = [(e, lab) for e in eps for lab in (0, 1, 1)]
    ep = np.array([r[0] for r in rows], object)
    y = np.array([r[1] for r in rows], float)
    fam = np.array([e.split("-")[0] for e in ep], object)
    calib = np.array([C.is_calibration(e) for e in ep])
    A = rng.normal(size=(len(rows), N_LAYERS, D_MODEL))
    A[y == 1, 2, 3] += signal
    return A.astype(np.float16), y, fam, calib, ep


def test_probe_recovers_planted_direction_and_shuffles_are_chance():
    A, y, fam, calib, ep = _synthetic_probe_data()
    feat = L.ActFeatures(A, LAYERS)
    res = L.lofo(feat, y, fam, calib, n_shuffles=5, seed_tag="t")
    assert L.auc_point(res["oof"], y) > 0.9
    assert L.auc_point(res["oof_by_key"][2], y) > 0.9            # the planted layer
    assert L.auc_point(res["oof_by_key"][0], y) < 0.75           # a layer without signal
    sh = [L.auc_point(s, y) for s in res["shuffled"][2]]
    assert abs(np.mean(sh) - 0.5) < 0.12
    assert all(f.get("chosen") == 24 for f in res["folds"] if not f.get("fallback"))


def test_lofo_never_trains_on_heldout_family():
    A, y, fam, calib, ep = _synthetic_probe_data(n_per=8)
    res = L.lofo(L.ActFeatures(A, LAYERS), y, fam, calib)
    assert len(res["folds"]) == 3
    for f in res["folds"]:
        assert not (fam[f["train_idx"]] == f["family"]).any()
        assert (fam[f["test_idx"]] == f["family"]).all()
    # every item gets exactly one out-of-fold score, from the fold that held out its family
    assert np.isfinite(res["oof"]).all()
    # bag-of-words baseline uses the same splits
    texts = np.array([("forged " if v else "genuine ") + e for v, e in zip(y, ep)], object)
    rb = L.lofo(L.BowFeatures(texts, np.array([len(t) for t in texts], float), np.full(len(texts), np.nan)),
                y, fam, calib)
    for f in rb["folds"]:
        assert not (fam[f["train_idx"]] == f["family"]).any()
    assert L.auc_point(rb["oof"], y) > 0.9


def test_hparam_choice_uses_only_training_calibration_split():
    A, y, fam, calib, ep = _synthetic_probe_data(n_per=12)
    train = fam != "research"
    hp = L.choose_hparams(L.ActFeatures(A, LAYERS), y.astype(int), train, calib)
    assert hp["n_val"] == int((train & calib).sum())
    assert hp["n_fit"] == int((train & ~calib).sum())
    hp0 = L.choose_hparams(L.ActFeatures(A, LAYERS), y.astype(int), train, np.zeros(len(y), bool))
    assert hp0["fallback"] and hp0["reason"]


@pytest.fixture(scope="module")
def full_run(tmp_path_factory):
    tmp = tmp_path_factory.mktemp("full")
    run = make_run(tmp)
    before = _sha(run / "selected.jsonl")
    rep = L.main(dir=run, out=tmp / "out", n_boot=200, n_shuffles=2, log=lambda *a: None)
    return tmp, run, rep, before


def test_main_without_flag_writes_nothing_to_dir(full_run):
    tmp, run, rep, before = full_run
    assert _sha(run / "selected.jsonl") == before
    assert not any(r["tier"] == "T4p" for r in P.read_jsonl(run / "selected.jsonl"))
    t4p = rep["headline_all"]["s_trace_mean"]["T4p"]
    assert t4p["auroc"] is None and "T4p" in t4p["reason"]
    assert (tmp / "out" / "local.json").exists()
    h = rep["headline"]
    assert h["tiers"] == list(L.TIERS) and set(h["detectors"]) >= {"V", "C"}
    assert all(len(v["est"]) == len(h["tiers"]) == len(v["lo"]) == len(v["hi"]) for v in h["detectors"].values())
    for name in ("detectors", "self_authorship", "probes", "transfer", "h4_matrix", "descriptives"):
        assert (tmp / "out" / f"local_{name}.csv").exists()


def test_main_recovers_planted_probe_signals(full_run):
    _, _, rep, _ = full_run
    assert rep["probes"]["main"]["P1|trace"]["pooled"]["auroc"] > 0.85
    assert rep["probes"]["main"]["P2|trace"]["pooled"]["auroc"] > 0.85
    assert abs(rep["probes"]["main"]["P1|trace"]["shuffled_chosen"]["mean"] - 0.5) < 0.2
    assert rep["headline_all"]["P2"]["T0"]["auroc"] > 0.8
    # every reported AUROC carries its n
    for r in rep["detectors"]:
        if r.get("auroc") is not None:
            assert r["n_pos"] > 0 and r["n_neg"] > 0 and r["ci_lo"] is not None


def test_split_half_defender_and_attacker_are_disjoint(full_run):
    tmp, run, rep, _ = full_run
    att = rep["probes"]["attacker"]
    for v in att["disjoint"].values():
        assert v["attacker_vs_defender_overlap"] == 0 and v["attacker_vs_target_overlap"] == 0
    halves = att["halves"]
    assert {h["target_half"] for h in halves} == {0, 1}
    for h in halves:
        assert all(L.tier_half(e) != h["target_half"] for e in h["train_episodes"])
        assert all(L.tier_half(e) == h["target_half"] for e in h["target_episodes"])
    sp = rep["probes"]["split_half"]["P1|trace"]
    for H in (0, 1):
        assert all(L.tier_half(e) == H for e in sp[f"half{H}"]["episodes"])
    # full-sample probes are not used against T4p
    assert all(r["auroc"] is None for r in rep["detectors"] if r["tier"] == "T4p" and r["detector"] in L.FULL_PROBES)


def test_select_t4p_picks_argmax_candidate(tmp_path):
    run = make_run(tmp_path)
    scores = L.select_t4p_scores(run, log=lambda *a: None)
    rep = L.main(dir=run, out=tmp_path / "out", select_t4p=True, n_boot=50, n_shuffles=0, log=lambda *a: None)
    sel = [r for r in P.read_jsonl(run / "selected.jsonl") if r["tier"] == "T4p"]
    other = [r for r in P.read_jsonl(run / "selected.jsonl") if r["tier"] != "T4p"]
    assert len(other) == 5 * len(sel)                          # rule tiers kept
    items = [d for d in P.load_items(run) if d["kind"] == "cand"]
    by_inst = {}
    for d in items:
        by_inst.setdefault((d["episode_id"], d["edit_type"]), []).append(d)
    assert len(sel) == len(by_inst)
    for r in sel:
        ok = [d for d in by_inst[(r["episode_id"], r["edit_type"])] if d["valid"] and d["item_id"] in scores]
        best = max(ok, key=lambda d: (scores[d["item_id"]], -d["cand_idx"]))
        assert r["item_id"] == best["item_id"]
        assert next(d for d in items if d["item_id"] == r["item_id"])["valid"]
    # the planted direction makes low-k candidates look more 'own' -> mostly k in {0, 1}
    ks = [int(r["item_id"].split("|")[-1]) for r in sel]
    assert np.mean([k <= 1 for k in ks]) > 0.6
    assert rep["probes"]["attacker"]["stored_selection"]["n_agree_with_recomputed"] == len(sel)
    assert rep["headline_all"]["P1h"]["T4p"]["auroc"] is not None


def test_empty_tiers_and_kinds_do_not_crash(tmp_path):
    run = make_run(tmp_path, seeds=range(50, 54), with_cands=False, with_t1=False, with_other=False,
                   with_selected=False)
    rep = L.main(dir=run, out=tmp_path / "out", n_boot=50, n_shuffles=1, log=lambda *a: None)
    for t in ("T1", "T2r", "T3", "T4s", "T4d", "T4c", "T4p"):
        r = rep["headline_all"]["s_trace_mean"][t]
        assert r["auroc"] is None and r["reason"]
    assert rep["headline_all"]["s_trace_mean"]["T0"]["auroc"] is not None
    assert rep["probes"]["main"]["P1|trace"]["pooled"]["auroc"] is None
    assert all(r.get("auroc") is None for r in rep["self_authorship"])
    assert all(r.get("auroc_change") is None and r.get("reason") for r in rep["transfer"])
    from analysis import local_figures, local_tables
    local_figures.main(tmp_path / "out" / "local.json", tmp_path / "fig")
    local_tables.main(tmp_path / "out" / "local.json", tmp_path / "tab", tmp_path / "tab" / "n.tex",
                      tmp_path / "tab" / "idx.md")
    assert (tmp_path / "fig" / "local_auroc_by_tier.pdf").exists()


def test_empty_registry(tmp_path):
    run = tmp_path / "run"
    run.mkdir()
    (run / "config.json").write_text(json.dumps({"acts_dir": str(tmp_path / "acts")}))
    rep = L.main(dir=run, out=tmp_path / "out", n_boot=10, log=lambda *a: None)
    assert "error" in rep


def test_tables_and_macros(full_run, tmp_path):
    tmp, _, _, _ = full_run
    from analysis import local_figures, local_tables
    js = tmp / "out" / "local.json"
    local_tables.main(js, tmp_path / "tab", tmp_path / "tab" / "numbers_local.tex", tmp_path / "tab" / "idx.md")
    tex = (tmp_path / "tab" / "numbers_local.tex").read_text()
    names = re.findall(r"\\newcommand\{\\([^}]+)\}", tex)
    assert names and len(names) == len(set(names))
    assert all(re.fullmatch(r"Loc[A-Za-z]+", n) for n in names)
    assert "\\LocAucSurpDeltaTFourD" in (tmp_path / "tab" / "idx.md").read_text()
    for t in local_tables.TABLES:
        body = (tmp_path / "tab" / f"{t}.tex").read_text()
        assert "\\toprule" in body and "\\bottomrule" in body
    local_figures.main(js, tmp_path / "fig")
    for f in ("local_auroc_by_tier.pdf", "local_transfer.pdf", "local_probe_layers.pdf"):
        assert (tmp_path / "fig" / f).read_bytes()[:4] == b"%PDF"
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    assert local_figures.draw_local_panel(ax, json.loads(js.read_text()))
    plt.close(fig)
