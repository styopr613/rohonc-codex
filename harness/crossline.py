"""Does a sequence that straddles a line break also occur inside a line?

The sharpest form of the line-break test, and the one that needs least from a
transcription: no alphabet, no word spaces, no entropy estimate, no shared
convention between manuscripts. Only a token stream and the line breaks.

Take every token n-gram the manuscript writes strictly inside a line. Then take
the n-grams that straddle a line break, half from the end of one line and half
from the start of the next, and ask how often such a sequence is one the
manuscript also writes inside a line.

If the text is continuous -- if a sentence simply carries on over the margin --
a straddling sequence is an ordinary piece of text that happens to be split,
and it should turn up inside lines at the same sort of rate as any other
sequence. If instead each line is composed as its own unit, a straddling
sequence is a join between two things that were never meant to meet, and it
should be no commoner than chance.

Chance is measured by shuffling which line follows which inside each page. That
leaves every line intact and destroys only the pairing, so it is the rate of
accidental matches for these exact lines against this exact inventory.

One token means one space-delimited word in the Voynich and one glyph in the
Rohonc Codex, following Kiraly & Tokai's reading that a Rohonc symbol codes a
whole word.

    python crossline.py
"""
import os
import random
import sys
from collections import Counter

import corpus

SEED = 408
SHUFFLES = 20


def from_voynich(doc):
    """[[line, ...], ...] grouped by paragraph."""
    return [[ln for ln in p.lines if ln] for p in doc]


def from_rohonc(doc):
    out = []
    for p in doc:
        ls = [[t for run in runs for t in run] for runs in p.lines]
        out.append([l for l in ls if l])
    return out


def inventory(groups, n):
    inv = Counter()
    for ls in groups:
        for l in ls:
            for i in range(len(l) - n + 1):
                inv[tuple(l[i:i + n])] += 1
    return inv


def boundary(groups, n, order=None):
    h = n // 2
    out = []
    for gi, ls in enumerate(groups):
        idx = order[gi] if order else list(range(len(ls)))
        for a, b in zip(idx, idx[1:]):
            x, y = ls[a], ls[b]
            if len(x) >= h and len(y) >= n - h:
                out.append(tuple(x[-h:]) + tuple(y[:n - h]))
    return out


def rate(grams, inv):
    return sum(1 for g in grams if inv.get(g, 0) > 0) / len(grams) * 100 if grams else 0.0


def assess(groups, n, rng):
    inv = inventory(groups, n)
    grams = boundary(groups, n)
    obs = rate(grams, inv)
    nulls = []
    for _ in range(SHUFFLES):
        order = []
        for ls in groups:
            idx = list(range(len(ls)))
            rng.shuffle(idx)
            order.append(idx)
        nulls.append(rate(boundary(groups, n, order), inv))
    m = sum(nulls) / len(nulls)
    sd = (sum((x - m) ** 2 for x in nulls) / max(1, len(nulls) - 1)) ** 0.5
    return obs, m, sd, ((obs - m) / sd if sd else 0.0), len(grams)


def main():
    import rohonc
    rng = random.Random(SEED)
    targets = [("Rohonc Codex (glyphs)", from_rohonc(rohonc.load()))]
    ev = corpus.load()
    targets.append(("Voynich EVA (words)", from_voynich(ev)))
    v101 = os.path.join(corpus.DATA, "GC2a-n.txt")
    if os.path.exists(v101):
        targets.append(("Voynich v101 (words)", from_voynich(corpus.load(v101))))

    import generators
    import layout
    generators.load_all()
    train, test = corpus.split(ev)
    spec = layout.build(train, len(corpus.words(test)))
    for name, lab in (("natlang_italian", "Italian prose (words)"),
                      ("natlang_latin", "Latin prose (words)"),
                      ("natlang_hebrew", "Hebrew prose (words)"),
                      ("fivecomp", "five-component model"),
                      ("selfcite", "self-citation (Timm)"),
                      ("linereset", "line-reset scribe")):
        try:
            d, _ = generators.get(name)["fn"](spec, train, seed=7)
            targets.append((lab, from_voynich(d)))
        except Exception as e:
            print(f"  ({name} failed: {e})", file=sys.stderr)

    print("=" * 92)
    print("DO SEQUENCES THAT STRADDLE A LINE BREAK ALSO OCCUR INSIDE LINES?")
    print("=" * 92)
    print("Percentage of straddling token n-grams that the same manuscript also")
    print("writes strictly inside a line. `chance` shuffles which line follows")
    print("which within a page, leaving every line intact.\n")
    for n in (2, 4, 6):
        print(f"--- {n}-gram ({n//2} token{'s' if n//2>1 else ''} from each side) "
              + "-" * 40)
        print(f"{'':26s} {'straddling':>11s} {'chance':>9s} {'sd':>6s} "
              f"{'sigma':>7s} {'lift':>7s} {'headroom':>9s} {'n':>8s}")
        for lab, g in targets:
            obs, m, sd, sig, nn = assess(g, n, rng)
            lift = (obs / m) if m else float("nan")
            head = (obs - m) / (100.0 - m) * 100 if m < 100 else float("nan")
            print(f"{lab:26s} {obs:10.2f}% {m:8.2f}% {sd:6.2f} {sig:7.1f} "
                  f"{lift:6.2f}x {head:8.1f}% {nn:8d}")
        print()
    print("  Above chance means the text carries on over the margin. At chance")
    print("  means the line is composed as a unit.")
    print()
    print("  `lift` is the ratio to chance and is the wrong way to compare texts")
    print("  here: the Rohonc's chance level is already 77% at n=2, so its ratio")
    print("  cannot exceed 1.30 however continuous the text is, while a text with")
    print("  a 6% chance level has room for 17x. `headroom` is the share of the")
    print("  distance from chance to 100% that the text actually covers, which is")
    print("  comparable across manuscripts with very different repeat rates.")


if __name__ == "__main__":
    main()
