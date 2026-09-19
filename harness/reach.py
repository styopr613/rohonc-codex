"""Two tests that could kill this project's most interesting claim.

RESULTS.md §4.2 reports that the manuscript has dependence between the end of
one word and the start of the next, at a strength above either natural language
in the reference set, and that no meaning-free process reproduces it except the
one whose author built it in deliberately. That is the loose thread. Before
anyone pulls on it, two things have to be ruled out.

**The reach test.** Memory is not meaning. A scribe copying a word he wrote a
line ago, or a hand falling into a habit, produces dependence between
*neighbouring* words and nothing beyond. Grammar reaches further: a word near
the start of a clause constrains one several words later. So: measure the
dependence at lag 1, 2, 3 ... and see whether it dies immediately or decays.
If it dies at lag 1, the mindless side of the argument is much stronger and
this project's claim should be weakened accordingly.

**The pen test.** The dependence might not be about words at all. Some glyph
shapes flow naturally into others, so what looks like word-to-word structure
could be the mechanics of a quill. Two ways to check. First, replicate on
v101, an independent transliteration by a different hand that groups the shapes
differently. Second, and sharper: compare word pairs *within* a line against
word pairs that straddle a line break. At a line break the pen lifts, travels
back across the page and starts again, so a purely mechanical flow effect
should weaken there. A linguistic one should not care.

Every figure is surrogate-corrected. Plug-in mutual information is biased
upward, badly so at small sample sizes, and the bias is what a naive version of
this test would measure. The control shuffles the order of the second element
of each pair, which preserves both marginal distributions exactly and destroys
only the association; the shuffled value *is* the estimator's bias at that
sample size, so no formula is assumed.

    python reach.py
"""
import math
import os
import random
import sys
from collections import Counter, defaultdict

import corpus

FP = os.path.join(corpus.ROOT, "refs", "voynich-fingerprint", "analysis")
if FP not in sys.path:
    sys.path.insert(0, FP)
from tier2_metrics import onset  # noqa: E402

SURROGATES = 12
SEED = 408


def _mi(pairs):
    if not pairs:
        return 0.0
    n = len(pairs)
    jx, jy, j = Counter(), Counter(), Counter()
    for a, b in pairs:
        jx[a] += 1
        jy[b] += 1
        j[(a, b)] += 1
    mi = 0.0
    for (a, b), c in j.items():
        p = c / n
        mi += p * math.log2(p / ((jx[a] / n) * (jy[b] / n)))
    return mi


def mi_corrected(pairs, rng, surrogates=SURROGATES):
    """MI minus the mean of a shuffled control. Returns (value, sd of control)."""
    if len(pairs) < 50:
        return 0.0, 0.0
    raw = _mi(pairs)
    xs = [a for a, _ in pairs]
    ys = [b for _, b in pairs]
    nulls = []
    for _ in range(surrogates):
        sh = ys[:]
        rng.shuffle(sh)
        nulls.append(_mi(list(zip(xs, sh))))
    m = sum(nulls) / len(nulls)
    sd = (sum((x - m) ** 2 for x in nulls) / max(1, len(nulls) - 1)) ** 0.5
    return raw - m, sd


# --------------------------------------------------------------------------
# the reach test
# --------------------------------------------------------------------------
def pairs_at_lag(doc, lag, mode="char"):
    """Word pairs `lag` apart, never crossing a paragraph boundary.

    mode "char": last character of word i against first character of word i+lag
    mode "onset": onset class of word i against onset class of word i+lag
    """
    out = []
    for p in doc:
        ws = p.words
        for i in range(len(ws) - lag):
            a, b = ws[i], ws[i + lag]
            if not a or not b:
                continue
            if mode == "char":
                out.append((a[-1], b[0]))
            else:
                out.append((onset(a), onset(b)))
    return out


def reach(doc, lags=range(1, 9), mode="char", seed=SEED):
    rng = random.Random(seed)
    return {k: mi_corrected(pairs_at_lag(doc, k, mode), rng) for k in lags}


# --------------------------------------------------------------------------
# the pen test
# --------------------------------------------------------------------------
def pairs_by_position(doc):
    """Adjacent word pairs, split by whether a line break falls between them.

    `within`: both words on the same line.
    `across`: the last word of one line and the first word of the next, same
    paragraph. The pen lifts and travels between these two.
    """
    within, across = [], []
    for p in doc:
        for li, ln in enumerate(p.lines):
            for a, b in zip(ln, ln[1:]):
                if a and b:
                    within.append((a[-1], b[0]))
            if li + 1 < len(p.lines) and ln and p.lines[li + 1]:
                across.append((ln[-1], p.lines[li + 1][0]))
    across = [(a, b[0]) for a, b in across if a and b]
    within = [(a, b) for a, b in within]
    return within, across


def pen_test(doc, seed=SEED):
    rng = random.Random(seed)
    within, across = pairs_by_position(doc)
    w, wsd = mi_corrected(within, rng)
    a, asd = mi_corrected(across, rng)
    return {"within": (w, wsd, len(within)), "across": (a, asd, len(across))}


def main():
    import generators
    import layout
    generators.load_all()

    doc = corpus.load()
    train, test = corpus.split(doc)
    print("=" * 74)
    print("REACH TEST -- how far does the dependence between words extend?")
    print("=" * 74)
    print("Surrogate-corrected mutual information in bits, by how many words apart.")
    print("A habit or a copying process should die at lag 1. Grammar should decay.\n")

    spec = layout.build(train, len(corpus.words(test)))
    targets = [("the manuscript", test), ("its own other half", train)]
    for name in ("fivecomp", "selfcite", "grille", "natlang_italian",
                 "natlang_latin", "naibbe_latin"):
        try:
            d, _ = generators.get(name)["fn"](spec, train, seed=7)
            targets.append((name, d))
        except Exception as e:
            print(f"  ({name} failed: {e})")

    lags = list(range(1, 9))
    print(f"{'':22s}" + "".join(f"{('lag ' + str(k)):>9s}" for k in lags))
    for label, d in targets:
        r = reach(d, lags)
        row = "".join(f"{r[k][0]:9.4f}" for k in lags)
        print(f"{label:22s}{row}")
    print("\nsd of the shuffled control, for the manuscript (a value below about")
    print("two of these is not distinguishable from zero):")
    r = reach(test, lags)
    print(f"{'':22s}" + "".join(f"{r[k][1]:9.4f}" for k in lags))

    print("\n" + "=" * 74)
    print("PEN TEST -- is it words, or is it how a quill moves?")
    print("=" * 74)
    print("Adjacent word pairs inside a line, against pairs straddling a line")
    print("break. At a line break the pen lifts and travels. A mechanical flow")
    print("effect should weaken there; a linguistic one should not care.\n")
    print(f"{'':26s} {'within line':>13s} {'across break':>13s} {'across, sd':>11s} "
          f"{'sigma':>7s} {'n across':>9s}")
    for label, d in targets:
        t = pen_test(d)
        w, a, asd, n = t["within"][0], t["across"][0], t["across"][1], t["across"][2]
        sig = a / asd if asd else 0.0
        print(f"{label:26s} {w:13.4f} {a:13.4f} {asd:11.4f} {sig:7.1f} {n:9d}")
    print("\n  `sigma` is the across-break value in units of its own shuffled")
    print("  control's spread. Below about 2 it is not distinguishable from zero.")

    print("\n  the manuscript, whole book and each half separately:")
    whole = corpus.load()
    for lab, d in (("whole book", whole), ("odd leaves (held out)", test),
                   ("even leaves (train)", train)):
        t = pen_test(d)
        a, asd, n = t["across"][0], t["across"][1], t["across"][2]
        print(f"    {lab:24s} within {t['within'][0]:.4f}   across {a:7.4f} "
              f"+- {asd:.4f}  ({a/asd if asd else 0:.1f} sigma, n={n})")

    print("\n" + "=" * 74)
    print("PEN TEST 2 -- does it survive an independent transliteration?")
    print("=" * 74)
    v101 = os.path.join(corpus.DATA, "GC2a-n.txt")
    if not os.path.exists(v101):
        print("  v101 file missing")
        return
    d2 = corpus.load(v101)
    _, te2 = corpus.split(d2)
    print(f"  v101: {len(d2)} paragraphs, {len(corpus.words(d2))} words, "
          f"{len(set(corpus.words(d2)))} types")
    r1 = reach(test, [1, 2, 3])
    r2 = reach(te2, [1, 2, 3])
    print(f"\n{'':16s}{'lag 1':>10s}{'lag 2':>10s}{'lag 3':>10s}")
    print(f"{'EVA (Takahashi)':16s}" + "".join(f"{r1[k][0]:10.4f}" for k in (1, 2, 3)))
    print(f"{'v101 (Currier)':16s}" + "".join(f"{r2[k][0]:10.4f}" for k in (1, 2, 3)))
    t1, t2 = pen_test(test), pen_test(d2)
    print(f"\n{'':16s}{'within':>10s}{'across':>10s}")
    print(f"{'EVA':16s}{t1['within'][0]:10.4f}{t1['across'][0]:10.4f}")
    print(f"{'v101':16s}{t2['within'][0]:10.4f}{t2['across'][0]:10.4f}")


if __name__ == "__main__":
    main()
