"""Check the paper's use of number macros.

Usage: ``python -m analysis.check_numbers [paper/main.tex] [--numbers paper/numbers.tex]``.

* every macro with a number prefix (``analysis.numbers.PREFIXES``) used in the paper must be defined in
  numbers.tex or in the paper itself -- undefined macros make the exit status 1;
* macros defined but never used are listed;
* macros used whose value is "n/a" are listed (a quantity the data could not provide);
* literal numbers with a decimal point or a % sign in the prose (after ``\\begin{document}``, outside comments,
  citations, references, labels, file names and options) are listed with their line so a human can check them.

The paper is read with the files it pulls in via ``\\input``/``\\include`` (relative to its folder), except
generated tables and numbers.tex.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from .common import ROOT
from .numbers import PREFIXES

DEF_RE = re.compile(r"\\(?:re)?newcommand\{?\\([A-Za-z]+)\}?(?:\[\d\])?\{(.*)\}\s*$")
USE_RE = re.compile(r"\\([A-Za-z]+)")
INPUT_RE = re.compile(r"\\(?:input|include)\{([^}]+)\}")
STRIP_RE = re.compile(r"\\(?:cite[a-z]*|ref|eqref|autoref|cref|Cref|label|input|include|includegraphics|url|href|"
                      r"bibliography|bibliographystyle|usepackage|documentclass)\*?(?:\[[^\]]*\])*\{[^}]*\}")
OPT_RE = re.compile(r"\[[^\]]*\]")
LITERAL_RE = re.compile(r"(?<![\\A-Za-z0-9.\-])(?:\d+\.\d+\s*\\?%?|\d+\s*\\%)")


def strip_comment(line: str) -> str:
    return re.sub(r"(?<!\\)%.*$", "", line)


def read_tree(main: Path, seen=None) -> list:
    """[(file, line number, text)] of the paper and its \\input files (skipping generated ones)."""
    seen = seen if seen is not None else set()
    if main in seen or not main.exists():
        return []
    seen.add(main)
    out = []
    for i, line in enumerate(main.read_text().splitlines(), 1):
        out.append((main, i, line))
        for inc in INPUT_RE.findall(strip_comment(line)):
            p = (main.parent / inc)
            p = p if p.suffix else p.with_suffix(".tex")
            if p.name == "numbers.tex" or "tables" in p.parts:
                continue
            out += read_tree(p, seen)
    return out


def definitions(path: Path) -> dict:
    defs = {}
    if path.exists():
        for line in path.read_text().splitlines():
            m = DEF_RE.match(line.strip())
            if m:
                defs[m.group(1)] = m.group(2)
    return defs


def check(main: Path, numbers: Path) -> dict:
    lines = read_tree(main)
    defs = definitions(numbers)
    local_defs = {m.group(1) for _, _, t in lines for m in [DEF_RE.match(strip_comment(t).strip())] if m}
    used, literals, in_doc = {}, [], False
    for f, i, t in lines:
        s = strip_comment(t)
        if DEF_RE.match(s.strip()):
            continue
        for name in USE_RE.findall(s):
            if name.startswith(PREFIXES):
                used.setdefault(name, []).append(f"{f.name}:{i}")
        if "\\begin{document}" in s:
            in_doc = True
            continue
        if in_doc:
            prose = OPT_RE.sub("", STRIP_RE.sub("", s))
            for m in LITERAL_RE.finditer(prose):
                literals.append(f"{f.name}:{i}: {m.group().strip()}  | {s.strip()[:100]}")
    return {"undefined": sorted(n for n in used if n not in defs and n not in local_defs),
            "unused": sorted(n for n in defs if n not in used),
            "used_na": sorted(n for n in used if defs.get(n) == "n/a"),
            "literals": literals, "used": used, "n_defined": len(defs)}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("tex", nargs="?", default=str(ROOT / "paper" / "main.tex"))
    ap.add_argument("--numbers", default=str(ROOT / "paper" / "numbers.tex"))
    ap.add_argument("--show-unused", action="store_true", help="list every unused macro (default: count only)")
    a = ap.parse_args(argv)
    main_tex = Path(a.tex)
    if not main_tex.exists():
        print(f"[check_numbers] {main_tex} not found")
        return 2
    r = check(main_tex, Path(a.numbers))
    print(f"[check_numbers] {len(r['used'])} number macros used, {r['n_defined']} defined in {a.numbers}")
    if r["undefined"]:
        print("UNDEFINED macros (fix before compiling):")
        for n in r["undefined"]:
            print(f"  \\{n}  used at {', '.join(r['used'][n])}")
    if r["used_na"]:
        print("macros used whose value is n/a:")
        for n in r["used_na"]:
            print(f"  \\{n}  at {', '.join(r['used'][n])}")
    print(f"defined but unused: {len(r['unused'])}" + (":" if a.show_unused and r["unused"] else ""))
    if a.show_unused:
        for n in r["unused"]:
            print(f"  \\{n}")
    if r["literals"]:
        print("literal numbers in the prose (check by hand or replace by a macro):")
        for x in r["literals"]:
            print("  " + x)
    return 1 if r["undefined"] else 0


if __name__ == "__main__":
    sys.exit(main())
