"""Checks that must pass after every change. Green here is not correctness;
it is only the absence of the specific mistakes that would silently invalidate
the table.

    python gate.py

1. leak       no generator reads the held-out transcription or the TEST split
2. split      our loader reproduces voynich-fingerprint's split exactly
3. ruler      our text and struct blocks reproduce the fingerprint's published
              held-out values, so the two sets of numbers remain comparable
4. floor      the noise-floor row exists and sits below every hypothesis row
5. rows       every registered process produced a row on both splits
6. splits     both the main and the reversed split are present
7. determin.  rerunning a process with the same seed gives the same numbers
"""
import json
import os
import re
import subprocess
import sys

import corpus
import profile as prof
import generators

WORK = os.path.join(corpus.ROOT, "work")
GEN = os.path.join(os.path.dirname(os.path.abspath(__file__)), "generators")

# the fingerprint repo's own published held-out figures, for the ruler check
PUBLISHED = {
    ("text", "h2 (char)"): 1.842,
    ("text", "cross-word MI"): 0.068,
    ("text", "final-y %"): 40.3,
    ("text", "top-10 word share %"): 12.8,
    ("text", "hapax %"): 19.7,
    ("struct", "qo- onset %"): 15.2,
    ("struct", "len>=10 %"): 1.76,
    ("struct", "adjacent identical words %"): 0.87,
    ("struct", "line chars sd"): 16.05,
    ("struct", "len>=8 %"): 8.3,
}

FAILS = []


def check(name, ok, detail=""):
    print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))
    if not ok:
        FAILS.append(name)
    return ok


def gate_leak():
    """No generator may open the transcription or touch the TEST split."""
    bad = []
    for fn in sorted(os.listdir(GEN)):
        if not fn.endswith(".py"):
            continue
        src = open(os.path.join(GEN, fn), encoding="utf-8").read()
        # strip docstrings and comments before searching, so prose may discuss it
        code = re.sub(r'"""(?:.|\n)*?"""', "", src)
        code = re.sub(r"(?m)#.*$", "", code)
        for pat in (r"IT2a", r"GC2a", r"ZL3b", r"corpus\.load\s*\(",
                    r"\btest\b", r"corpus\.split\s*\("):
            if re.search(pat, code):
                bad.append(f"{fn}:{pat}")
    return check("leak: no generator reads the manuscript or the TEST split",
                 not bad, ", ".join(bad))


def gate_split():
    sys.path.insert(0, os.path.join(corpus.ROOT, "refs", "voynich-fingerprint", "analysis"))
    from tune_artgen import split_by_folio
    tr_ref, te_ref = split_by_folio()
    d = corpus.load()
    tr, te = corpus.split(d)
    ok = corpus.plain(tr) == tr_ref and corpus.plain(te) == te_ref
    return check("split: identical to voynich-fingerprint's split_by_folio", ok,
                 f"{len(tr)} train / {len(te)} test paragraphs")


def gate_ruler(res):
    ref = res["reference"]
    worst, where = 0.0, ""
    for (blk, m), want in PUBLISHED.items():
        got = ref[blk][m]
        d = abs(got - want) / abs(want) * 100
        if d > worst:
            worst, where = d, f"{m} {got:.3f} vs published {want}"
    return check("ruler: reproduces the fingerprint's published held-out values",
                 worst < 1.0, f"worst {worst:.2f}%  ({where})")


def gate_floor(res):
    ps = res["processes"]
    if "noise_floor" not in ps:
        return check("floor: noise-floor row present", False)
    nf = ps["noise_floor"]["floor_medians"]["overall"]
    above = [n for n, r in ps.items()
             if n != "noise_floor" and "floor_medians" in r
             and r["floor_medians"]["overall"] < nf]
    return check("floor: no hypothesis row beats the manuscript's own other half",
                 not above, f"floor {nf:.2f}x" + (f", beaten by {above}" if above else ""))


def gate_rows(res, split):
    generators.load_all()
    want = set(generators.names())
    got = {n for n, r in res["processes"].items() if "means" in r}
    missing = want - got
    return check(f"rows: every registered process has a row ({split})",
                 not missing, f"{len(got)}/{len(want)}" + (f", missing {missing}" if missing else ""))


def gate_determinism():
    r = subprocess.run([sys.executable, os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "score.py"), "--verify",
        "--only", "grille,llull,abbrev,naibbe_latin,natlang_latin"],
        capture_output=True, text=True, cwd=os.path.dirname(os.path.abspath(__file__)))
    out = r.stdout + r.stderr
    ok = "DETERMINISTIC" in out and "NON-DETERMINISTIC" not in out
    line = [l for l in out.splitlines() if "drift" in l]
    return check("determinism: same seed, same numbers", ok,
                 line[-1].strip() if line else out[-200:])


def main():
    print("gate:")
    gate_leak()
    gate_split()
    paths = {s: os.path.join(WORK, f"results_{s}.json") for s in ("main", "reverse")}
    have = {s: os.path.exists(p) for s, p in paths.items()}
    check("splits: both the main and the reversed split have been scored",
          all(have.values()), ", ".join(f"{s}={'yes' if v else 'no'}" for s, v in have.items()))
    for s, p in paths.items():
        if not have[s]:
            continue
        res = json.load(open(p, encoding="utf-8"))
        if s == "main":
            gate_ruler(res)
        gate_floor(res)
        gate_rows(res, s)
    gate_determinism()
    print(f"\n{'ALL GATES PASS' if not FAILS else 'FAILED: ' + ', '.join(FAILS)}")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
