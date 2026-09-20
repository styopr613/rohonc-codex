"""How much of the Rohonc Codex can actually be read, and how much is translated.

Those are different numbers and the difference matters.

A token "has a reading" if K&T's dictionary glosses it, or if it cuts into
dictionary codes by the construction ktname.py and ktsegment.py gated. That is
a coverage figure, not a translation. Most codes K&T define carry several
senses -- 'away / to', 'angel / Lucifer / Satan', 'believe / misunderstand' --
and choosing between them needs the grammar, which is the paper they have not
published. A word with five candidate senses is not translated. It is located.

So this reports three things, weakest claim to strongest:

  1. tokens with any reading at all
  2. tokens with exactly ONE sense, which is the only honest "translated"
  3. LINES in which every word has a reading, which is what you would need
     before a sentence could be read at all

No gate here. Nothing is being claimed; this counts what the gated methods
left behind, and it is the number to quote when someone asks how much of the
book is readable.

    python ktcoverage.py
"""
import sys
from collections import Counter

import ktdict
import ktsegment as S
import rohonc_kt as KT


def flatten(line):
    out = []
    for x in line:
        out += x if isinstance(x, list) else [x]
    return out


def build():
    d = ktdict.load()
    gl = {c: g for c, g, _ in d if g}
    doc = KT.load()
    defset = set(gl)
    seg = {}
    for t in {t for p in doc for t in p.tokens}:
        if t in gl:
            continue
        s = S.segment(t, defset)
        if s and len(s) >= 2:
            seg[t] = s
    return gl, doc, seg


def main():
    gl, doc, seg = build()
    types = Counter(t for p in doc for t in p.tokens)

    def readable(t):
        return t in gl or t in seg

    def n_senses(t):
        if t in gl:
            return len(gl[t])
        return max(len(gl[p]) for p in seg[t]) if t in seg else 0

    tot = sum(types.values())
    dfn = sum(k for t, k in types.items() if t in gl)
    new = sum(k for t, k in types.items() if t in seg)
    non = tot - dfn - new
    one = sum(k for t, k in types.items() if readable(t) and n_senses(t) == 1)

    print("=" * 70)
    print("HOW MUCH OF THE BOOK CAN BE READ")
    print("=" * 70)
    print(f"tokens in the book                {tot:6d}")
    print(f"  K&T dictionary covers           {dfn:6d}  {dfn/tot*100:5.1f}%")
    print(f"  readable by composition         {new:6d}  {new/tot*100:5.1f}%")
    print(f"  any reading at all              {dfn+new:6d}  {(dfn+new)/tot*100:5.1f}%")
    print(f"  no reading at all               {non:6d}  {non/tot*100:5.1f}%")
    print()
    print("=" * 70)
    print("HOW MUCH IS TRANSLATED")
    print("=" * 70)
    print(f"  exactly one sense, no choice    {one:6d}  {one/tot*100:5.1f}%")
    print(f"  several senses, grammar needed  {dfn+new-one:6d}  "
          f"{(dfn+new-one)/tot*100:5.1f}%")
    print()

    lines = [f for f in (flatten(l) for p in doc for l in p.lines) if f]

    def share(l, f):
        return sum(1 for t in l if f(t)) / len(l)

    fb = sum(1 for l in lines if all(t in gl for t in l))
    fa = sum(1 for l in lines if all(readable(t) for t in l))
    eb = sum(1 for l in lines if share(l, lambda t: t in gl) >= .8)
    ea = sum(1 for l in lines if share(l, readable) >= .8)
    mb = sorted(share(l, lambda t: t in gl) for l in lines)[len(lines) // 2]
    ma = sorted(share(l, readable) for l in lines)[len(lines) // 2]
    print("=" * 70)
    print("LINES, WHICH IS WHAT YOU NEED BEFORE A SENTENCE READS")
    print("=" * 70)
    print(f"lines in the book                 {len(lines):6d}")
    print(f"  every word readable     before  {fb:5d} ({fb/len(lines)*100:4.1f}%)"
          f"    after {fa:5d} ({fa/len(lines)*100:4.1f}%)")
    print(f"  80%+ of words readable  before  {eb:5d} ({eb/len(lines)*100:4.1f}%)"
          f"    after {ea:5d} ({ea/len(lines)*100:4.1f}%)")
    print(f"  median line readability before  {mb*100:5.1f}%"
          f"            after {ma*100:5.1f}%")
    print()
    print("  The bottleneck is no longer missing vocabulary. It is that most")
    print("  covered words carry several senses and the grammar that chooses")
    print("  between them is unpublished.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
