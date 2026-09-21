"""WHY THE CANDIDATE LIST MISSES. A diagnostic, declared before it ran.

The blind test (ktblind.py, seed 1789991853, 2026-09-21) split cleanly: when
the true word was in the candidate list the reader got 7 of 9; when it was
not, 2 of 16. So the reader is not the weak part of the judgment step. The
LIST is. Gate 4a puts the true gloss in the list 16-18% of the time.

This script masks every K&T entry ONE AT A TIME (leave-one-out, so all 676
entries on a cited folio are measured, not a 10% sample) and files each miss
under the first reason that explains it, in this order:

    HIT        in the list the pipeline builds today (cited verses, both
               translations, minus words another visible sign already means)
    TAKEN      in those verses, but filtered out because another sign already
               carries that stem. K&T have many signs for one English word.
    NARROW     within +-3 verses of the cite. The cite is one passage per
               folio; a folio has a dozen lines.
    CHAPTER    somewhere in a cited chapter
    BIBLE      somewhere in the King James or Douay at all
    OUTSIDE    in neither Bible. Apocrypha, sermon, or a function word.

Nothing is optimised here. The output is a table of reasons, and the bar
for any later change to the list builder is declared now so it cannot be
fitted to the result:

    an improved list builder must raise HIT (leave-one-out, all 676) by at
    least 10 points over the baseline this script prints first, with its
    mean list size no more than twice the baseline's, and it must beat the
    tether-cut control (the same builder on a random other cited folio) by
    5 sigma over 20 shuffles. Presence bought by a longer list is not an
    improvement; the reader pays for every extra word.

    python3 ktrecall.py            baseline + reasons
"""
import random
import re
import sys
from collections import Counter, defaultdict

import ktaffix as A
import ktcross as K
import ktleft as L
import ktrederive as R

NSHUF = 20


def all_stems(vv, vd):
    s = set()
    for t in (vv, vd):
        for txt in t.values():
            s |= R.stems(txt)
    return s


def passage_stems(vv, vd, refs, wide):
    s = set()
    for k, txt in L.passage(vv, refs, wide) + L.passage(vd, refs, wide):
        s |= R.stems(txt)
    return s


def chapter_stems(vv, vd, refs):
    s = set()
    chs = {(b, c) for b, c, _, _ in refs}
    for t in (vv, vd):
        for (b, c, v), txt in t.items():
            if (b, c) in chs:
                s |= R.stems(txt)
    return s


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    unhex, visible, where, refs = R.build_world(gl, doc, set())
    vv, vd = L.verses(), L.verses_dr()
    idx = R.taken_index_visible(visible)
    bible = all_stems(vv, vd)
    cited = sorted(refs)

    # today's list for a folio, with entry h masked: the pipeline's pool
    # minus nothing else, since a stem is "taken" only if a sign OTHER than
    # h carries it.
    def today(pg, h):
        raw = passage_stems(vv, vd, refs[pg], 0)
        return {s for s in raw if not any(hb != h for hb, _ in idx.get(s, []))}

    rows = []
    sizes = []
    rng = random.Random(R.SEED + 11)
    ctrl = [0] * NSHUF
    for h in sorted(visible):
        truth = R.stems(visible[h])
        if not truth:
            continue
        pgs = sorted({pg for pg, _ in where[h] if pg in refs})
        if not pgs:
            rows.append((h, "NOCITE"))
            continue
        lst = set()
        for pg in pgs:
            lst |= today(pg, h)
        sizes.append(len(lst))
        for j in range(NSHUF):
            r2 = random.Random(R.SEED + 200 + j)
            c = set()
            for _ in pgs:
                c |= today(r2.choice(cited), h)
            ctrl[j] += bool(truth & c)
        if truth & lst:
            rows.append((h, "HIT")); continue
        raw = set()
        for pg in pgs:
            raw |= passage_stems(vv, vd, refs[pg], 0)
        if truth & raw:
            rows.append((h, "TAKEN")); continue
        wide = set()
        for pg in pgs:
            wide |= passage_stems(vv, vd, refs[pg], 3)
        if truth & wide:
            rows.append((h, "NARROW")); continue
        chap = set()
        for pg in pgs:
            chap |= chapter_stems(vv, vd, refs[pg])
        if truth & chap:
            rows.append((h, "CHAPTER")); continue
        if truth & bible:
            rows.append((h, "BIBLE")); continue
        rows.append((h, "OUTSIDE"))

    n = sum(1 for _, r in rows if r != "NOCITE")
    cnt = Counter(r for _, r in rows)
    print(f"CANDIDATE-LIST RECALL, leave-one-out over {len(rows)} K&T entries"
          f" ({n} on a cited folio, {cnt['NOCITE']} on none)\n")
    hit = cnt["HIT"] / n
    m = sum(ctrl) / NSHUF / n
    sd = (sum((c / n - m) ** 2 for c in ctrl) / (NSHUF - 1)) ** 0.5
    print(f"  BASELINE  true gloss in today's list   {hit*100:.1f}%   "
          f"mean list size {sum(sizes)/len(sizes):.1f} words")
    print(f"            tether-cut control           {m*100:.1f}%   "
          f"{(hit-m)/sd if sd else float('inf'):.1f} sigma\n")
    print("  why the rest miss (first reason that explains it):")
    for k in ("HIT", "TAKEN", "NARROW", "CHAPTER", "BIBLE", "OUTSIDE"):
        print(f"    {k:8s} {cnt[k]:4d}   {cnt[k]/n*100:5.1f}%")
    if "--show" in argv:
        want = argv[argv.index("--show") + 1]
        print(f"\n  examples, {want}:")
        for h, r in rows:
            if r == want:
                print(f"    {h:22s} {visible[h][:50]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
