"""Read a hole from the same sentence written somewhere else in the book.

The book writes long passages twice. `ktdouble.py` finds them, but it matches
on runs of identical word types, so a word that occurs once in the manuscript
can never fall inside a match -- and words that occur once are the whole of
what is left unread. This file aligns the two copies with gaps and mismatches
allowed, so a hole in one copy lines up with whatever stands in its slot in
the other.

THE BAR, SET BEFORE THE RUN, AND THE REASON FOR IT. An alignment is only
evidence if aligned slots really do hold the same word. The test is the pairs
where the two copies differ in spelling but BOTH are read: if those carry the
same reading often, the alignment is finding the same sentence and a hole
aligned to a read word may take that word's reading. The bar is 80% agreement
over at least 50 such pairs. Below that, this file generates candidates to
check against context by hand and nothing may be graded above C on its say-so.

Identical-token alignments are excluded from the measurement. They are
trivially in agreement and would flatter the number to meaninglessness.

THE RESULT: IT FAILED. 53 passages aligned. 3,094 aligned slots hold different
tokens with both read, and 12 of them -- 0.4% -- carry the same reading. The
bar was 80%. It is not the flanks doing it either: agreement was measured
against distance from the anchor and it is 0.0% inside the matched run, 1.4%
one to three tokens outside, and 0.4% from there out to forty. So the failure
is not a tuning problem and no tighter window rescues it.

WHY IT FAILS, which is worth more than the attempt. The repeated passages were
found by matching runs of identical word types, so where the two copies AGREE
they agree exactly and there is nothing to read. Where they DIFFER, they
differ in content, not in spelling. The book is not copying itself word for
word with variant orthography; it is retelling. That is the same thing 148r
shows in the open, where the Good Samaritan is told a second time as the fall
of Adam.

So the 253 unread signs this file finds sitting opposite a read word are
candidates to check by hand against context, and nothing here may be graded
above C. The idea that the doubled passages could break the wall of
once-occurring signs is dead, and it was the largest unbuilt idea on the list.

    python3 ktpair.py            # the measurement, then the candidates
    python3 ktpair.py --show N   # the Nth aligned passage, both copies
"""
import sys
from collections import Counter, defaultdict

import ktaffix as A
import ktcross as K
import ktdouble as D

SEED = 5          # window length for the anchor search, as ktdouble uses
FLANK = 40        # tokens either side of an anchor to align
MATCH, MISS, GAP = 3, -2, -3
BAR_RATE, BAR_PAIRS = 0.80, 50


def hx(s):
    return "".join(f"{ord(c)-0xE000:03x}" for c in s)


def align(a, b):
    """Needleman-Wunsch over token types. Returns [(ia, ib)] with None for gaps."""
    n, m = len(a), len(b)
    sc = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        sc[i][0] = sc[i - 1][0] + GAP
    for j in range(1, m + 1):
        sc[0][j] = sc[0][j - 1] + GAP
    for i in range(1, n + 1):
        ai = a[i - 1]
        row, prev = sc[i], sc[i - 1]
        for j in range(1, m + 1):
            row[j] = max(prev[j - 1] + (MATCH if ai == b[j - 1] else MISS),
                         prev[j] + GAP, row[j - 1] + GAP)
    out, i, j = [], n, m
    while i > 0 or j > 0:
        if i > 0 and j > 0 and sc[i][j] == sc[i - 1][j - 1] + (
                MATCH if a[i - 1] == b[j - 1] else MISS):
            out.append((i - 1, j - 1)); i -= 1; j -= 1
        elif i > 0 and sc[i][j] == sc[i - 1][j] + GAP:
            out.append((i - 1, None)); i -= 1
        else:
            out.append((None, j - 1)); j -= 1
    return out[::-1]


def passages(seq):
    """Anchored windows: (slice a, slice b) around each repeated run."""
    out, used = [], []
    for a, b, L in D.runs(seq, SEED):
        s1 = slice(max(0, a - FLANK), min(len(seq), a + L + FLANK))
        s2 = slice(max(0, b - FLANK), min(len(seq), b + L + FLANK))
        if any(s1.start < u2.stop and u1.start < s2.stop
               and s1.stop > u1.start and s2.stop > u2.start
               for u1, u2 in used):
            continue
        used.append((s1, s2))
        out.append((s1, s2))
    return out


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    G = lambda t: K.T.render_token(t, gl, seg, False, var, prop)
    seq = D.stream(doc)
    cnt = Counter(t for _, _, t in seq)
    ps = passages(seq)

    agree = disagree = 0
    examples, cands = [], defaultdict(list)
    for s1, s2 in ps:
        wa, wb = seq[s1], seq[s2]
        pa = align([t for _, _, t in wa], [t for _, _, t in wb])
        for i, j in pa:
            if i is None or j is None:
                continue
            ta, tb = wa[i][2], wb[j][2]
            if ta == tb:
                continue
            ra, rb = ta in inv, tb in inv
            if ra and rb:
                if G(ta) == G(tb):
                    agree += 1
                    if len(examples) < 6:
                        examples.append(f"{hx(ta)} = {hx(tb)}  '{G(ta)[:28]}'")
                else:
                    disagree += 1
            elif ra != rb:
                hole, seen = (tb, ta) if ra else (ta, tb)
                where = (wb[j] if ra else wa[i])[:2]
                other = (wa[i] if ra else wb[j])[:2]
                cands[hole].append((where, other, seen))

    tot = agree + disagree
    print(f"{len(ps)} passages aligned, gaps and mismatches allowed")
    print(f"aligned slots where the two copies hold DIFFERENT tokens and both are read: {tot}")
    if tot:
        print(f"  same reading:      {agree}  ({agree/tot*100:.1f}%)")
        print(f"  different reading: {disagree}")
    print(f"  bar declared before the run: {BAR_RATE:.0%} of at least {BAR_PAIRS} pairs")
    ok = tot >= BAR_PAIRS and agree / tot >= BAR_RATE if tot else False
    print(f"  VERDICT: {'PASS -- alignment is evidence' if ok else 'FAIL -- candidates only, nothing above C'}")
    if examples:
        print("\n  agreeing pairs, for inspection:")
        for e in examples:
            print(f"    {e}")

    print(f"\n{len(cands)} unread signs sit opposite a read word in the other copy")
    print(f"  they cover {sum(cnt[h] for h in cands)} words in the book\n")
    rows = sorted(cands.items(), key=lambda kv: -len(kv[1]))
    for hole, hits in rows[:40]:
        opp = Counter(G(s) for _, _, s in hits)
        best, n = opp.most_common(1)[0]
        where = ",".join(f"{p}:{l}" for (p, l), _, _ in hits[:3])
        print(f"  {hx(hole):24s} n={cnt[hole]:<3d} at {where:22s} opposite {best[:34]}"
              + (f"  ({n}/{len(hits)} agree)" if len(hits) > 1 else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
