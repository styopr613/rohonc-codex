"""Is a word a small edit of the word before it, and does that stop at the margin?

Timm & Schinner's self-citation hypothesis says the scribe wrote each word by
copying one he had recently written and changing it slightly. They established
that Voynich words are unusually similar to their neighbours. What nobody has
done is split that by line boundary.

§4.2.2 of RESULTS.md found that statistical dependence between words is strong
inside a line and exactly zero across a line break. If the mechanism is
copy-and-mutate, the same split should show up in the *spelling*: a word should
be a small edit of the one before it while both sit on the same line, and no
closer than chance to the word that ended the previous line.

That is a sharp prediction and it is cheap to test. It is also falsifiable in a
useful way: if the similarity is the same on both sides of a line break, the
line-reset picture is wrong, whatever the statistical dependence says.

Measured as mean normalised edit distance, against a control that shuffles word
order inside the paragraph while holding every line length fixed. The control
preserves the vocabulary and the geometry exactly, so it is the chance level
for these words in these lines.

    python similarity.py
"""
import os
import random
import sys

import corpus


def edit(a, b):
    """Levenshtein distance, normalised by the longer word."""
    if a == b:
        return 0.0
    la, lb = len(a), len(b)
    if not la or not lb:
        return 1.0
    prev = list(range(lb + 1))
    for i in range(1, la + 1):
        cur = [i] + [0] * lb
        ca = a[i - 1]
        for j in range(1, lb + 1):
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1,
                         prev[j - 1] + (ca != b[j - 1]))
        prev = cur
    return prev[lb] / max(la, lb)


def pairs(doc):
    """(within-line adjacent pairs, across-line-break pairs)."""
    within, across = [], []
    for p in doc:
        for i, ln in enumerate(p.lines):
            for a, b in zip(ln, ln[1:]):
                within.append((a, b))
            if i + 1 < len(p.lines) and ln and p.lines[i + 1]:
                across.append((ln[-1], p.lines[i + 1][0]))
    return within, across


def shuffled(doc, rng):
    out = []
    for p in doc:
        ws = p.words[:]
        rng.shuffle(ws)
        lines, i = [], 0
        for ln in p.lines:
            lines.append(ws[i:i + len(ln)])
            i += len(ln)
        out.append(corpus.Para(folio=p.folio, lines=lines, section=p.section,
                               lang=p.lang, hand=p.hand))
    return out


def mean_edit(ps):
    return sum(edit(a, b) for a, b in ps) / len(ps) if ps else 0.0


def measure(doc, rng, surrogates=8):
    w, a = pairs(doc)
    mw, ma = mean_edit(w), mean_edit(a)
    nw, na = [], []
    for _ in range(surrogates):
        sw, sa = pairs(shuffled(doc, rng))
        nw.append(mean_edit(sw))
        na.append(mean_edit(sa))

    def stat(obs, nulls):
        m = sum(nulls) / len(nulls)
        sd = (sum((x - m) ** 2 for x in nulls) / max(1, len(nulls) - 1)) ** 0.5
        return obs, m, (m - obs) / sd if sd else 0.0
    return stat(mw, nw) + (len(w),), stat(ma, na) + (len(a),)


def main():
    import generators
    import layout
    generators.load_all()

    doc = corpus.load()
    train, test = corpus.split(doc)
    spec = layout.build(train, len(corpus.words(test)))

    targets = [("the manuscript (EVA)", doc),
               ("the manuscript (v101)",
                corpus.load(os.path.join(corpus.DATA, "GC2a-n.txt")))]
    for name, label in (("selfcite", "self-citation (Timm)"),
                        ("fivecomp", "five-component model"),
                        ("natlang_italian", "prose (Italian, same layout)"),
                        ("grille", "table-and-grille"),
                        ("naibbe_latin", "Naibbe cipher")):
        try:
            d, _ = generators.get(name)["fn"](spec, train, seed=7)
            targets.append((label, d))
        except Exception as e:
            print(f"  ({name} failed: {e})")

    print("=" * 86)
    print("IS A WORD A SMALL EDIT OF THE ONE BEFORE IT?")
    print("=" * 86)
    print("Mean normalised edit distance. LOWER means more similar. `chance` is the")
    print("same words in the same line lengths with the order shuffled; `sigma` is")
    print("how far below chance the real figure sits.\n")
    print(f"{'':30s} {'within line':>11s} {'chance':>8s} {'sigma':>7s} "
          f"{'| across break':>14s} {'chance':>8s} {'sigma':>7s}")
    print("-" * 86)
    for label, d in targets:
        (mw, cw, sw, nw), (ma, ca, sa, na) = measure(d, random.Random(408))
        print(f"{label:30s} {mw:11.4f} {cw:8.4f} {sw:7.1f} "
              f"{ma:14.4f} {ca:8.4f} {sa:7.1f}")

    print("\n  The line-reset picture predicts a large sigma inside the line and")
    print("  roughly zero across the break. Equal values on both sides would")
    print("  falsify it regardless of what the statistical dependence says.")


if __name__ == "__main__":
    main()
