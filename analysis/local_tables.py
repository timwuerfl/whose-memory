"""LaTeX tables and quotable numbers for the local-victim analysis.

    python -m analysis.local_tables [--json results/analysis/local.json] [--tables paper/tables]
                                    [--numbers paper/numbers_local.tex]
                                    [--index results/analysis/numbers_local_index.md]

Tables are ``booktabs`` ``tabular`` environments (no float, no caption) in ``paper/tables/local_*.tex``.
``numbers_local.tex`` holds one ``\\newcommand`` per quotable number (prefix ``\\Loc``, camel case, no
digits); the index lists macro -> value -> meaning. Undefined values are typeset as ``n/a`` and the index
gives the reason.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TIERS = ("T0", "T1", "T2", "T2r", "T3", "T4s", "T4d", "T4c", "T4p")
TIER_WORD = {"T0": "TZero", "T1": "TOne", "T2": "TTwo", "T2r": "TTwoR", "T3": "TThree", "T4s": "TFourS",
             "T4d": "TFourD", "T4c": "TFourC", "T4p": "TFourP", "T4_pooled": "TFourPooled"}
DET_WORD = {"s_trace_mean": "Surp", "s_trace_max": "SurpMax", "s_blind_mean": "SurpBlind", "s_delta": "SurpDelta",
            "ppl_gpt2": "PplGpt", "ppl_small": "PplSmall", "ppl_small_trace": "PplSmallTrace", "v": "Verbal",
            "c": "Consist", "P1": "ProbeSelf", "P1_blind": "ProbeSelfBlind", "P2": "ProbeCons",
            "P2_blind": "ProbeConsBlind", "P1h": "ProbeSelfSplit", "P2h": "ProbeConsSplit", "bow_P1": "BowSelf",
            "bow_P2": "BowCons", "len_chars": "LenChars", "len_tokens": "LenTokens"}
DET_TEX = {"s_trace_mean": "Surprisal $\\mid$ trace (mean)", "s_trace_max": "Surprisal $\\mid$ trace (max)",
           "s_blind_mean": "Surprisal, no trace", "s_delta": "Surprisal delta", "ppl_gpt2": "GPT-2 surprisal",
           "ppl_small": "Qwen3.5-0.8B surprisal", "ppl_small_trace": "Qwen3.5-0.8B $\\mid$ session",
           "v": "Verbal $P(\\text{yes})$", "c": "Consistency $P(\\text{yes})$", "P1": "Probe P1",
           "P1_blind": "Probe P1, no trace", "P2": "Probe P2", "P2_blind": "Probe P2, no trace",
           "P1h": "Probe P1 (split-half)", "P2h": "Probe P2 (split-half)", "bow_P1": "BoW+length (P1 task)",
           "bow_P2": "BoW+length (P2 task)", "len_chars": "Length (chars)", "len_tokens": "Length (tokens)"}
MAIN_DETS = ("s_trace_mean", "s_trace_max", "s_blind_mean", "s_delta", "ppl_gpt2", "ppl_small", "ppl_small_trace",
             "v", "c", "P1", "P2", "P1h", "P2h", "bow_P2", "len_chars")
MACRO_DETS = ("s_trace_mean", "s_blind_mean", "s_delta", "v", "c", "P1", "P2", "P1h", "P2h", "ppl_gpt2",
              "ppl_small", "len_chars", "bow_P2")
NA = "\\textit{n/a}"


def _tex_escape(s: str) -> str:
    return str(s).replace("_", "\\_").replace("%", "\\%").replace("&", "\\&")


def f2(x, nd=2):
    return NA if x is None else f"{x:.{nd}f}"


def fs(x, nd=2):
    if x is None:
        return NA
    return f"$-${abs(x):.{nd}f}" if x < 0 else f"$+${x:.{nd}f}"


def fn(n):
    return NA if n is None else f"{int(n):,}".replace(",", "{,}")


def fci(r, nd=2):
    if not r or r.get("auroc") is None:
        return NA
    if r.get("ci_lo") is None:
        return f2(r["auroc"], nd)
    return f"{r['auroc']:.{nd}f} [{r['ci_lo']:.{nd}f}, {r['ci_hi']:.{nd}f}]"


def _get(rows, **kw):
    for r in rows or []:
        if all(r.get(k) == v for k, v in kw.items()):
            return r
    return None


def tabular(spec, header, body, note_rows=()):
    lines = [f"\\begin{{tabular}}{{{spec}}}", "\\toprule", " & ".join(header) + " \\\\", "\\midrule"]
    lines += [" & ".join(r) + " \\\\" for r in body]
    if note_rows:
        lines.append("\\midrule")
        lines += [" & ".join(r) + " \\\\" for r in note_rows]
    lines += ["\\bottomrule", "\\end{tabular}", ""]
    return "\n".join(lines)


# ------------------------------------------------------------------------------------------------
# tables
# ------------------------------------------------------------------------------------------------
def t_detectors(J):
    rows = J.get("detectors", [])
    body = []
    for d in MAIN_DETS:
        cells = [DET_TEX[d]]
        for t in TIERS:
            r = _get(rows, detector=d, tier=t, subset="all", negset="matched")
            cells.append(f2(r.get("auroc")) if r else NA)
        body.append(cells)
    npos = ["$n$ forged / genuine"]
    for t in TIERS:
        r = _get(rows, detector="s_trace_mean", tier=t, subset="all", negset="matched")
        npos.append(f"{fn(r.get('n_pos'))}/{fn(r.get('n_neg'))}" if r and r.get("n_pos") is not None else NA)
    return tabular("l" + "c" * len(TIERS), ["Detector"] + list(TIERS), body, [npos])


def t_detectors_ci(J):
    rows = J.get("detectors", [])
    body = []
    for d in MAIN_DETS:
        for t in TIERS:
            r = _get(rows, detector=d, tier=t, subset="all", negset="matched") or {}
            body.append([DET_TEX[d] if t == TIERS[0] else "", t, fci(r), f2(r.get("tpr_fpr01")), f2(r.get("tpr_fpr05")),
                         fn(r.get("n_pos")), fn(r.get("n_neg"))])
    return tabular("llccccc", ["Detector", "Tier", "AUROC [95\\% CI]", "TPR@1\\%", "TPR@5\\%", "$n_+$", "$n_-$"], body)


def t_selfauth(J):
    rows = J.get("self_authorship", [])
    comps = []
    for r in rows:
        c = r.get("comparison")
        if r.get("detector") and c not in comps:
            comps.append(c)
    comps = sorted(comps, key=lambda c: (c != "genuine vs other:all", c))
    dets = ("s_trace_mean", "s_blind_mean", "s_delta", "ppl_gpt2", "ppl_small", "P1", "P1_blind", "bow_P1",
            "len_chars")
    head = ["Detector"] + [_tex_escape(c.replace("genuine vs ", "").replace("other:", "")) for c in comps]
    body = [[DET_TEX[d]] + [fci(_get(rows, comparison=c, detector=d)) for c in comps] for d in dets]
    nrow = ["$n$ other / own"] + [
        (lambda r: f"{fn(r.get('n_pos'))}/{fn(r.get('n_neg'))}" if r else NA)(_get(rows, comparison=c,
                                                                                 detector="s_trace_mean"))
        for c in comps]
    return tabular("l" + "c" * len(comps), head, body, [nrow])


def t_probes(J):
    pr = J.get("probes", {})
    body = []
    fams = ("inventory", "research", "assistant")
    for task in ("P1", "P2"):
        for which in ("trace", "blind"):
            s = pr.get("main", {}).get(f"{task}|{which}") or {}
            folds = {f["family"]: f for f in s.get("folds", [])}
            cells = [f"{task}, {'with trace' if which == 'trace' else 'no trace'}", fci(s.get("pooled"))]
            for f in fams:
                fo = folds.get(f)
                cells.append(f2((fo or {}).get("auroc_heldout", {}).get("auroc")) +
                             (f" (L{fo.get('chosen')})" if fo and fo.get("chosen") is not None else ""))
            cells.append(f2((s.get("shuffled_chosen") or {}).get("mean")))
            last = (pr.get("last_token", {}).get(f"{task}|{which}") or {}).get("pooled")
            cells.append(f2((last or {}).get("auroc")))
            sh = (pr.get("split_half", {}).get(f"{task}|{which}") or {}).get("pooled")
            cells.append(f2((sh or {}).get("auroc")))
            body.append(cells)
        b = pr.get("bow", {}).get(task) or {}
        folds = {f["family"]: f for f in b.get("folds", [])}
        body.append([f"{task}, bag-of-words + length", fci(b.get("pooled"))] +
                    [f2((folds.get(f) or {}).get("auroc_heldout", {}).get("auroc")) for f in fams] + ["", "", ""])
    head = ["Probe", "Pooled OOF AUROC [95\\% CI]", "Inv.", "Res.", "Asst.", "Shuffled", "Last tok.", "Split-half"]
    return tabular("lccccccc", head, body)


def t_h4(J):
    m = J.get("h3_h4", {}).get("matrix", [])
    tiers = ("T2r", "T3", "T4s", "T4d", "T4c", "T4p")
    dets = []
    for r in m:
        if r["detector"] not in dets:
            dets.append(r["detector"])
    body = []
    for d in dets:
        cells = [DET_TEX.get(d, d)]
        for t in tiers:
            r = _get(m, detector=d, tier=t) or {}
            v = f2(r.get("auroc"))
            cells.append(f"\\textbf{{{v}}}" if r.get("targeted") and r.get("auroc") is not None else v)
        body.append(cells)
    return tabular("l" + "c" * len(tiers), ["Detector"] + list(tiers), body)


def t_gap(J):
    g = J.get("integrity_gap", {})
    body = []
    for r in g.get("by_tier", []):
        body.append([_tex_escape(r["tier"]), f2(r.get("auroc_best")), f2(r.get("auroc_v")),
                     fs(r.get("diff")) + (f" [{fs(r['ci_lo'])}, {fs(r['ci_hi'])}]" if r.get("ci_lo") is not None else ""),
                     f"{fn(r.get('n_pos'))}/{fn(r.get('n_neg'))}"])
    best = DET_TEX.get(g.get("best"), "best") if g.get("best") else "best"
    return tabular("lcccc", ["Tier", f"AUROC {best}", "AUROC verbal", "Gap [95\\% CI]", "$n_+/n_-$"], body)


def t_transfer(J):
    rows = J.get("transfer", [])
    dets = []
    for r in rows:
        if r["detector"] not in dets:
            dets.append(r["detector"])
    body = []
    for rule in ("T3", "T4s", "T4d", "T4c", "T4p"):
        body.append([rule] + [fs((_get(rows, rule=rule, detector=d) or {}).get("auroc_change")) for d in dets])
    return tabular("l" + "c" * len(dets), ["Rule"] + [DET_TEX.get(d, d) for d in dets], body)


def t_desc(J):
    D = J.get("descriptives", {})
    body = []
    for k in D.get("by_kind", []):
        body.append([_tex_escape(k["kind"]), fn(k["n"]), NA if k.get("valid_rate") is None else f"{100 * k['valid_rate']:.1f}\\%",
                     f"{f2(k.get('chars_mean'), 0)} ({f2(k.get('chars_sd'), 0)})",
                     f"{f2(k.get('tokens_mean'), 0)} ({f2(k.get('tokens_sd'), 0)})"])
    return tabular("lrrrr", ["Kind", "$n$", "Valid", "Characters, mean (SD)", "Tokens, mean (SD)"], body)


TABLES = {"local_detectors": t_detectors, "local_detectors_ci": t_detectors_ci, "local_selfauth": t_selfauth,
          "local_probes": t_probes, "local_h4": t_h4, "local_gap": t_gap, "local_transfer": t_transfer,
          "local_descriptives": t_desc}


# ------------------------------------------------------------------------------------------------
# numbers
# ------------------------------------------------------------------------------------------------
class Numbers:
    def __init__(self):
        self.items = []     # (name, tex value, meaning, reason)
        self.names = set()

    def add(self, name, value, meaning, reason=None):
        assert re.fullmatch(r"Loc[A-Za-z]+", name), name
        if name in self.names:
            raise ValueError(f"duplicate macro {name}")
        self.names.add(name)
        self.items.append((name, value, meaning, reason))

    def tex(self, header=""):
        out = ["% Auto-generated by analysis/local_tables.py -- do not edit.", header]
        out += [f"\\newcommand{{\\{n}}}{{{v}}}" for n, v, _, _ in self.items]
        return "\n".join(out) + "\n"

    def index(self, src):
        out = ["# Local-analysis macros (`paper/numbers_local.tex`)", "",
               f"Generated from `{src}` by `analysis/local_tables.py`.", "",
               "| macro | value | meaning |", "|---|---|---|"]
        for n, v, m, r in self.items:
            vv = v.replace("|", "\\|")
            out.append(f"| `\\{n}` | {vv} | {m}{' (n/a: ' + r + ')' if r else ''} |")
        return "\n".join(out) + "\n"


def build_numbers(J) -> Numbers:
    N = Numbers()
    D = J.get("descriptives", {})
    N.add("LocNEpisodes", fn(D.get("n_episodes")), "local main episodes with registry items")
    N.add("LocNInstances", fn(D.get("n_instances")), "attack instances (genuine target notes)")
    N.add("LocNItems", fn(D.get("n_items")), "registry items (all kinds)")
    for k in D.get("by_kind", []):
        if k["kind"] in ("T0", "T1", "T2"):
            N.add(f"LocValidRate{TIER_WORD[k['kind']]}", NA if k.get("valid_rate") is None else
                  f"{100 * k['valid_rate']:.1f}\\%", f"share of {k['kind']} forgeries that are valid (n={k['n']})")
    c = D.get("candidates", {})
    N.add("LocValidRateCand", NA if c.get("valid_rate") is None else f"{100 * c['valid_rate']:.1f}\\%",
          f"share of pool candidates that are valid (n={c.get('n')})", c.get("reason"))
    N.add("LocInstWithValidCand", fn(c.get("instances_with_valid")),
          f"instances with at least one valid candidate (of {c.get('n_instances')})", c.get("reason"))
    for t in TIERS:
        r = _get(J.get("detectors"), detector="s_trace_mean", tier=t, subset="all", negset="matched") or {}
        N.add(f"LocNPos{TIER_WORD[t]}", fn(r.get("n_pos")), f"valid {t} forgeries (positives, all instances)",
              r.get("reason"))
        N.add(f"LocNNeg{TIER_WORD[t]}", fn(r.get("n_neg")), f"matched genuine notes for {t}", r.get("reason"))
    for d in MACRO_DETS:
        for t in TIERS:
            r = _get(J.get("detectors"), detector=d, tier=t, subset="all", negset="matched") or {}
            base = f"LocAuc{DET_WORD[d]}{TIER_WORD[t]}"
            why = r.get("reason") if r.get("auroc") is None else None
            mean = f"AUROC of {d} for {t} vs matched genuine notes (all instances)"
            N.add(base, f2(r.get("auroc")), f"{mean}; n+={r.get('n_pos')}, n-={r.get('n_neg')}", why)
            N.add(base + "Lo", f2(r.get("ci_lo")), f"lower 95% CI bound of \\{base}", why)
            N.add(base + "Hi", f2(r.get("ci_hi")), f"upper 95% CI bound of \\{base}", why)
    # self-authorship (pooled other-model notes)
    for d in ("s_trace_mean", "s_blind_mean", "s_delta", "ppl_gpt2", "P1", "P1_blind", "bow_P1", "len_chars"):
        r = _get(J.get("self_authorship"), comparison="genuine vs other:all", detector=d) or {}
        base = f"LocSelfAuth{DET_WORD[d]}"
        why = r.get("reason") if r.get("auroc") is None else None
        N.add(base, f2(r.get("auroc")), f"AUROC own genuine vs other-model notes, {d}; n+={r.get('n_pos')}, "
                                        f"n-={r.get('n_neg')}", why)
        N.add(base + "Lo", f2(r.get("ci_lo")), f"lower CI of \\{base}", why)
        N.add(base + "Hi", f2(r.get("ci_hi")), f"upper CI of \\{base}", why)
    # probes
    pr = J.get("probes", {})
    for task, w in (("P1", "Self"), ("P2", "Cons")):
        for which, ww in (("trace", "Trace"), ("blind", "Blind")):
            s = pr.get("main", {}).get(f"{task}|{which}") or {}
            p = s.get("pooled") or {}
            why = p.get("reason") or s.get("reason")
            base = f"LocProbe{w}{ww}"
            N.add(base, f2(p.get("auroc")), f"pooled out-of-fold AUROC of {task} ({which} activations, mean-pooled, "
                                            f"LOFO); n+={p.get('n_pos')}, n-={p.get('n_neg')}", why)
            N.add(base + "Lo", f2(p.get("ci_lo")), f"lower CI of \\{base}", why)
            N.add(base + "Hi", f2(p.get("ci_hi")), f"upper CI of \\{base}", why)
            sh = s.get("shuffled_chosen") or {}
            N.add(base + "Shuf", f2(sh.get("mean")), f"mean pooled AUROC of {task} ({which}) over "
                                                     f"{sh.get('n_shuffles')} shuffled-label refits", why)
            lt = (pr.get("last_token", {}).get(f"{task}|{which}") or {}).get("pooled") or {}
            N.add(base + "Last", f2(lt.get("auroc")), f"pooled AUROC of {task} ({which}) on last-token activations",
                  lt.get("reason"))
            sp = (pr.get("split_half", {}).get(f"{task}|{which}") or {}).get("pooled") or {}
            N.add(base + "Split", f2(sp.get("auroc")), f"pooled AUROC of the split-half {task} ({which})",
                  sp.get("reason"))
        b = (pr.get("bow", {}).get(task) or {}).get("pooled") or {}
        N.add(f"LocBow{w}", f2(b.get("auroc")), f"pooled AUROC of the bag-of-words + length baseline on the {task} "
                                                f"task; n+={b.get('n_pos')}, n-={b.get('n_neg')}", b.get("reason"))
        N.add(f"LocBow{w}Lo", f2(b.get("ci_lo")), f"lower CI of \\LocBow{w}", b.get("reason"))
        N.add(f"LocBow{w}Hi", f2(b.get("ci_hi")), f"upper CI of \\LocBow{w}", b.get("reason"))
    # H4
    H = J.get("h3_h4", {})
    for r in H.get("h4_style_under_targeted_T4", []):
        base = f"LocHFour{DET_WORD[r['detector']]}{TIER_WORD[r['tier']]}"
        why = r.get("reason") if r.get("auroc") is None else None
        N.add(base, f2(r.get("auroc")), f"H4: AUROC of style signal {r['detector']} under its targeted tier "
                                        f"{r['tier']} (common instances); n+={r.get('n_pos')}, n-={r.get('n_neg')}", why)
        N.add(base + "Lo", f2(r.get("ci_lo")), f"lower CI of \\{base}", why)
        N.add(base + "Hi", f2(r.get("ci_hi")), f"upper CI of \\{base}", why)
    for w in H.get("worst_case_over_T4", []):
        N.add(f"LocWorst{DET_WORD[w['detector']]}", f2(w.get("worst_auroc")),
              f"worst-case AUROC of {w['detector']} over the T4 tiers (at {w.get('worst_tier')})",
              None if w.get("worst_auroc") is not None else "no T4 tier available")
    bt = H.get("h4_best_trace_vs_best_style_worst_case") or {}
    N.add("LocHFourBestTrace", _tex_escape(DET_TEX.get(bt.get("best_trace"), NA)) if bt.get("best_trace") else NA,
          "trace-based signal with the highest worst-case AUROC over T4 tiers", bt.get("reason"))
    N.add("LocHFourTraceMinusStyle", fs(bt.get("diff")), "worst-case AUROC, best trace minus best style signal",
          bt.get("reason"))
    N.add("LocHFourTraceMinusStyleLo", fs(bt.get("ci_lo")), "lower CI of \\LocHFourTraceMinusStyle", bt.get("reason"))
    N.add("LocHFourTraceMinusStyleHi", fs(bt.get("ci_hi")), "upper CI of \\LocHFourTraceMinusStyle", bt.get("reason"))
    # integrity gap
    G = J.get("integrity_gap", {})
    N.add("LocGapBest", _tex_escape(DET_TEX.get(G.get("best"), NA)) if G.get("best") else NA,
          "trace-based detector chosen on calibration episodes for the local integrity gap",
          (G.get("selection") or {}).get("reason"))
    for r in G.get("by_tier", []):
        base = f"LocGap{TIER_WORD.get(r['tier'], r['tier'])}"
        why = r.get("reason") if r.get("diff") is None else None
        N.add(base, fs(r.get("diff")), f"integrity gap AUROC({r['detector']}) - AUROC(verbal) at {r['tier']}, "
                                       f"evaluation episodes; n+={r.get('n_pos')}, n-={r.get('n_neg')}", why)
        N.add(base + "Lo", fs(r.get("ci_lo")), f"lower CI of \\{base}", why)
        N.add(base + "Hi", fs(r.get("ci_hi")), f"upper CI of \\{base}", why)
    # transfer
    for r in J.get("transfer", []):
        d = r["detector"]
        base = f"LocShift{TIER_WORD[r['rule']]}{DET_WORD[d]}"
        why = r.get("reason") if r.get("auroc_change") is None else None
        N.add(base, fs(r.get("auroc_change")), f"AUROC change of {d} under rule {r['rule']} relative to T2r "
                                               f"(n={r.get('n_instances')} instances)", why)
        N.add(base + "Sd", fs(r.get("mean_shift_sd_units")),
              f"mean oriented-score shift of {d} under {r['rule']} vs T2r, in genuine-SD units", why)
    return N


def main(json_path=ROOT / "results" / "analysis" / "local.json", tables=ROOT / "paper" / "tables",
         numbers=ROOT / "paper" / "numbers_local.tex", index=ROOT / "results" / "analysis" / "numbers_local_index.md"):
    J = json.loads(Path(json_path).read_text())
    tables, numbers, index = Path(tables), Path(numbers), Path(index)
    tables.mkdir(parents=True, exist_ok=True)
    for name, fn_ in TABLES.items():
        (tables / f"{name}.tex").write_text("% Auto-generated by analysis/local_tables.py from results/analysis/local.json\n" + fn_(J))
    N = build_numbers(J)
    numbers.parent.mkdir(parents=True, exist_ok=True)
    numbers.write_text(N.tex(f"% source: {J.get('meta', {}).get('dir')}"))
    index.parent.mkdir(parents=True, exist_ok=True)
    index.write_text(N.index("results/analysis/local.json"))
    print(f"[local_tables] {len(TABLES)} tables -> {tables}; {len(N.items)} macros -> {numbers}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", default=str(ROOT / "results" / "analysis" / "local.json"))
    ap.add_argument("--tables", default=str(ROOT / "paper" / "tables"))
    ap.add_argument("--numbers", default=str(ROOT / "paper" / "numbers_local.tex"))
    ap.add_argument("--index", default=str(ROOT / "results" / "analysis" / "numbers_local_index.md"))
    a = ap.parse_args()
    main(a.json, a.tables, a.numbers, a.index)
