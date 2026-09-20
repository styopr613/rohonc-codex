"""Work the top undefined codes: evidence, hypothesis, rejection, repeat.

The ceiling work showed where the effort belongs. 38 undefined codes occur 30
or more times and carry 10% of the book, and they are the only ones that can be
checked against themselves. Solving them also unlocks the rest: with every code
of three or more occurrences known, 36.6% of one-off codes land in a sentence
whose every other word is readable, against 4.9% today.

This assembles the evidence a hypothesis has to survive. For a target code it
reports the frames it appears in -- the commonest words before and after, the
commonest three-word patterns, whether it ever doubles, whether it opens or
closes lines, how it spreads across the book, and which codes it collocates
with far above chance. A meaning is proposed against that, not against one
passage, and most wrong meanings die on it without any reading at all.
"""
import math
from collections import Counter, defaultdict

import ktdict
import rohonc_kt as KT


def load():
    gl = {c: g for c, g, _ in ktdict.load() if g}
    doc = KT.load(blocktypes=("main", "picture"))
    return gl, doc


def name(gl, c, target=None, width=30):
    if c == target:
        return "[T]"
    if c in gl:
        s = "/".join(sorted(gl[c])).replace("<", "").replace(">", "")
        return s[:width]
    return "(?)"


def evidence(gl, doc, target):
    lines = [[t for run in runs for t in run] for p in doc for runs in p.lines]
    before, after, tri = Counter(), Counter(), Counter()
    li = lf = n = 0
    pages = set()
    for p in doc:
        for runs in p.lines:
            line = [t for run in runs for t in run]
            for i, t in enumerate(line):
                if t != target:
                    continue
                n += 1
                pages.add(p.page)
                if i:
                    after[line[i - 1]] += 1
                if i + 1 < len(line):
                    before[line[i + 1]] += 1
                if i and i + 1 < len(line):
                    tri[(line[i - 1], line[i + 1])] += 1
            if line and line[0] == target:
                li += 1
            if line and line[-1] == target:
                lf += 1
    # collocation lift: how far above chance each neighbour sits
    allf = Counter(t for ln in lines for t in ln)
    total = sum(allf.values())
    lift = []
    for c, k in (before + after).most_common(40):
        exp = 2 * n * allf[c] / total
        if exp > 0 and k >= 5:
            lift.append((k / exp, k, c))
    lift.sort(reverse=True)
    return {"n": n, "pages": len(pages), "before": before, "after": after,
            "tri": tri, "li": li, "lf": lf, "doubled": before[target], "lift": lift}


def report(gl, doc, target, label=""):
    e = evidence(gl, doc, target)
    print("=" * 78)
    print(f"{label}  {e['n']} occurrences on {e['pages']} pages")
    print(f"  line-initial {e['li']}   line-final {e['lf']}   doubled {e['doubled']}")
    print("=" * 78)
    print("  FOLLOWS (word before it):")
    for c, k in e["after"].most_common(6):
        print(f"     {k:4d}  {name(gl, c, target)}")
    print("  PRECEDES (word after it):")
    for c, k in e["before"].most_common(6):
        print(f"     {k:4d}  {name(gl, c, target)}")
    print("  FRAMES  x [T] y :")
    for (a, b), k in e["tri"].most_common(6):
        print(f"     {k:4d}  {name(gl, a, target, 24):24s} [T] {name(gl, b, target, 24)}")
    print("  STRONGEST COLLOCATES (times above chance):")
    for r, k, c in e["lift"][:6]:
        print(f"     {r:5.1f}x  ({k:3d})  {name(gl, c, target)}")
    print()


if __name__ == "__main__":
    import sys
    gl, doc = load()
    freq = Counter(t for p in doc for t in p.tokens)
    und = [t for t, _ in freq.most_common() if t not in gl]
    k = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    for i, t in enumerate(und[:k], 1):
        report(gl, doc, t, f"UNDEFINED #{i}")
