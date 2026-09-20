"""Does the dependence between one token and the next survive the right margin?

The test that decided the Voynich question, restated so it can be run on any
manuscript that has a token stream and line breaks -- no alphabet, no word
spaces, no transcription convention in common required.

For the Voynich a token is a space-delimited word. For the Rohonc Codex a token
is one glyph, because Kiraly & Tokai argue each Rohonc symbol codes a whole
word. In both cases the question is the same: knowing the token at the end of a
line, how much does that tell you about the token that starts the next one,
compared with how much a token tells you about its neighbour inside a line?

Real language keeps most of it. A sentence does not stop at the margin. A
process that composes one line at a time does not.

Two controls, both necessary.

Plug-in mutual information is biased upward, and the bias grows as the sample
shrinks, so a raw comparison between many within-line pairs and few
across-break pairs would show a difference that is pure arithmetic. Every
figure here is the raw value minus the mean of shuffled surrogates at that
exact sample size, and the surrogate spread is reported as the scale against
which to read it.

The within-line figure is also computed on a random subsample matched to the
number of across-break pairs, so the two numbers being compared rest on the
same amount of evidence.

    python linebreak.py
"""
import os
import random
import sys

import corpus
import reach

SEED = 408
SURROGATES = 12
MATCHED_REPEATS = 8


def voynich_pairs(doc):
    """Word-identity pairs from a Voynich-style Document."""
    within, across = [], []
    for p in doc:
        for i, ln in enumerate(p.lines):
            for a, b in zip(ln, ln[1:]):
                within.append((a, b))
            if i + 1 < len(p.lines) and ln and p.lines[i + 1]:
                across.append((ln[-1], p.lines[i + 1][0]))
    return within, across


def assess(within, across, rng, label=""):
    w, wsd = reach.mi_corrected(within, rng, SURROGATES)
    a, asd = reach.mi_corrected(across, rng, SURROGATES)
    n = len(across)
    matched = []
    if n >= 50 and len(within) > n:
        for _ in range(MATCHED_REPEATS):
            sub = rng.sample(within, n)
            matched.append(reach.mi_corrected(sub, rng, SURROGATES)[0])
    mw = sum(matched) / len(matched) if matched else w
    keep = (a / mw * 100) if mw > 0 else float("nan")
    return {"label": label, "within": w, "within_matched": mw, "across": a,
            "across_sd": asd, "sigma": (a / asd if asd else 0.0),
            "n_within": len(within), "n_across": n, "keep_pct": keep}


def row(r):
    return (f"{r['label']:28s} {r['within']:8.4f} {r['within_matched']:9.4f} "
            f"{r['across']:8.4f} {r['across_sd']:7.4f} {r['sigma']:7.1f} "
            f"{r['keep_pct']:7.1f} {r['n_across']:8d}")


def main():
    import rohonc
    rng = random.Random(SEED)
    rows = []

    for lab, rev in (("Rohonc (as stored)", False),
                     ("Rohonc (line reversed)", True)):
        d = rohonc.load(reverse=rev)
        w, a = rohonc.pairs_by_position(d)
        rows.append(assess(w, a, rng, lab))

    ev = corpus.load()
    rows.append(assess(*voynich_pairs(ev), rng, "Voynich EVA (words)"))
    v101 = os.path.join(corpus.DATA, "GC2a-n.txt")
    if os.path.exists(v101):
        rows.append(assess(*voynich_pairs(corpus.load(v101)), rng,
                           "Voynich v101 (words)"))

    import generators
    import layout
    generators.load_all()
    train, test = corpus.split(ev)
    spec = layout.build(train, len(corpus.words(test)))
    for name, lab in (("natlang_italian", "Italian prose (words)"),
                      ("natlang_latin", "Latin prose (words)"),
                      ("fivecomp", "five-component model"),
                      ("selfcite", "self-citation (Timm)")):
        try:
            d, _ = generators.get(name)["fn"](spec, train, seed=7)
            rows.append(assess(*voynich_pairs(d), rng, lab))
        except Exception as e:
            print(f"  ({name} failed: {e})", file=sys.stderr)

    print("=" * 96)
    print("DOES TOKEN-TO-TOKEN DEPENDENCE SURVIVE THE LINE BREAK?")
    print("=" * 96)
    print("Surrogate-corrected mutual information between one token and the next,")
    print("in bits. `matched` is the within-line figure recomputed on a random")
    print("subsample the same size as the across-break set, so the two rest on")
    print("equal evidence. `keep` is across as a percentage of matched.\n")
    print(f"{'':28s} {'within':>8s} {'matched':>9s} {'across':>8s} {'sd':>7s} "
          f"{'sigma':>7s} {'keep %':>7s} {'n across':>8s}")
    print("-" * 96)
    for r in rows:
        print(row(r))
    print("\n  `sigma` is the across-break value in units of its own surrogate")
    print("  spread. Below about 2 it is not distinguishable from zero.")
    print("\n  The Rohonc is written right to left and the transcription does not")
    print("  document its storage order, so both orientations are shown. Mutual")
    print("  information is symmetric, so `within` is identical either way; only")
    print("  the across-break pair changes, and both readings are reported.")


if __name__ == "__main__":
    main()
