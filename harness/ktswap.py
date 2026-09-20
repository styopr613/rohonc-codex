"""Is a sign one glyph away from a read sign a variant of it? Mostly no.

All day on 2026-09-20 readings were being made by noticing that an unread
sign is Kiraly and Tokai's word with one glyph changed -- Rome, grape,
exorcise, mouth, grab, lose, kiss -- and the swap felt like a rule. It is not
a rule, and this file is the test that says so.

THE BAR, SET BEFORE THE RUN. Take every pair of signs that are BOTH read and
differ in exactly one glyph. If the two members of such a pair usually carry
the same reading, then one-glyph distance is evidence of a variant spelling,
and an unread sign one glyph from a read sign may inherit its reading. Call a
swap class usable if it preserves the reading in at least 80% of at least 10
pairs. Anything less is not evidence and must not be graded above C.

THE RESULT. 4,824 pairs of read signs lie one glyph apart. 103 of them, 2.1%,
mean the same thing. One glyph of distance is therefore almost always a
different word, not a different spelling. Broken down by which glyph swaps:

    520/521   89% of 18 pairs   usable
    520/670   18% of 92 pairs   NOT usable
    520/540   29% of 28 pairs   NOT usable
    540/670   27% of 11 pairs   NOT usable
    ae0/ae1   21% of 19 pairs   NOT usable
    060/ae0    3% of 32 pairs   NOT usable

520/670 is the swap this project leaned on hardest, and it is wrong four
times in five. The readings it produced survive anyway, but not because of
the swap: every one of them is a line Kiraly and Tokai cite in their own
apparatus, and it was their citation doing the work the whole time. Two
readings that had no citation behind them were downgraded when this ran:
5400607a2 "that" from A to B, and 520ae0701 "bless" from B to C.

What the swap IS good for is generating candidates. 543 of the 924 unread
signs of three or more glyphs lie one glyph from a read sign, 438 of them
occurring once in the book. That is a shortlist to check against context, not
a set of readings.

    python3 ktswap.py            # the measurement
    python3 ktswap.py --near     # unread signs one glyph from a read sign
"""
import sys
from collections import Counter, defaultdict

import ktaffix as A
import ktcross as K

USABLE_RATE = 0.80
USABLE_PAIRS = 10


def load():
    gl, doc, seg, var, prop, inv = K.build()
    cnt = Counter(A.strip(t)[0] for p in doc for t in p.tokens)
    return gl, doc, seg, var, prop, inv, cnt


def hx(s):
    return "".join(f"{ord(c)-0xE000:03x}" for c in s)


def sense(t, gl, seg, var, prop):
    return K.T.render_token(t, gl, seg, False, var, prop).strip("+?~.").lower()


def measure(gl, doc, seg, var, prop, inv, cnt):
    read = [t for t in cnt if t in inv and len(t) >= 3]
    bylen = defaultdict(list)
    for t in read:
        bylen[len(t)].append(t)
    swap = defaultdict(lambda: [0, 0])
    for a in read:
        for b in bylen[len(a)]:
            if b <= a:
                continue
            d = [(x, y) for x, y in zip(a, b) if x != y]
            if len(d) != 1:
                continue
            key = tuple(sorted((hx(d[0][0]), hx(d[0][1]))))
            swap[key][1] += 1
            swap[key][0] += sense(a, gl, seg, var, prop) == sense(b, gl, seg, var, prop)
    return swap


def main(argv):
    gl, doc, seg, var, prop, inv, cnt = load()
    swap = measure(gl, doc, seg, var, prop, inv, cnt)
    tot = sum(v[1] for v in swap.values())
    same = sum(v[0] for v in swap.values())
    print(f"pairs of READ signs one glyph apart: {tot}")
    print(f"  carrying the same reading:          {same}  ({same/tot*100:.1f}%)")
    print(f"  bar: a swap is usable at >= {USABLE_RATE:.0%} of >= {USABLE_PAIRS} pairs\n")
    print(f"{'swap':12s} {'same':>5s} {'pairs':>6s} {'rate':>6s}  verdict")
    ok = 0
    for key, (s, n) in sorted(swap.items(), key=lambda kv: -kv[1][0]):
        if n < 3:
            continue
        good = n >= USABLE_PAIRS and s / n >= USABLE_RATE
        ok += good
        print(f"{key[0]}/{key[1]:7s} {s:5d} {n:6d} {s/n*100:5.0f}%  {'USABLE' if good else 'not evidence'}")
    print(f"\n{ok} swap class(es) clear the bar.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
