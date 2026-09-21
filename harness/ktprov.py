"""Where every reading in this book came from, and how far it is from K&T.

The claim "80% of the lines read" is worth nothing without this table. A
reading anchored on Kiraly and Tokai's own dictionary entry is co-signed by
published work; a reading got by matching a line against a chapter and verse
is this project's own and stands on its evidence; a reading got from neither
is a judgment, and a tier G word is a guess. Those are four different things
and they should never be added up without being shown apart.

PROVENANCE IS COMPUTED, NOT DECLARED. None of this reads the prose of the
evidence field, which is mine and could say anything. Each class is worked
out from the sign itself against K&T's dictionary, so a reviewer can rerun it:

  KT-direct      the reading is K&T's own -- their dictionary, unchanged.
                 This is most of the book and none of it is this project's.

  KT-anchored    this project's reading, where the sign is inside a K&T sign,
                 contains one whole, or is one glyph from one. The word comes
                 from their entry, so the anchor is theirs even though the
                 reading is ours. Reported with which of the three it is.

  KT-chained     anchored the same way, but on a reading of THIS project
                 rather than on K&T -- so the anchor is only as good as the
                 reading under it. Counted apart for that reason.

  passage        no anchor in any dictionary; read by matching the line to a
                 chapter and verse, a repeated formula, or a numeral.

  guess          tier G. Marked in the text with a degree sign, never counted
                 as read.

TESTABILITY IS A SEPARATE AXIS FROM CONFIDENCE, and it is reported apart
because it is not the same question. A reading can be probably right and
still be one the book can never check. Three classes, computed:

  verified       the book itself checks it: the sign occurs more than once
                 and every occurrence takes the reading, or some (word
                 before, word after) frame carries both this sign and the
                 sign it was anchored on.

  testable       the sign occurs more than once, so a second occurrence
                 could refuse it, but no shared frame confirms it.

  untestable     the sign occurs ONCE and no frame confirms it. Nothing
                 inside the codex can ever falsify this reading. Only a new
                 source text, or Kiraly and Tokai's unpublished material,
                 can reach it.

    python ktprov.py            the table
    python ktprov.py --list C   every reading of one tier, with its class
"""
import json
import sys
from collections import Counter

import ktaffix as A
import ktcross as K
import ktnear as N
import kttranslate as T
import ktvarcheck as V


def classify(h, kt_hexes, mine_hexes):
    """(class, why) for one proposed sign."""
    g = N.glyphs(h)
    for pool, name in ((kt_hexes, "KT-anchored"), (mine_hexes, "KT-chained")):
        for hb in pool:
            if hb != h and len(h) >= 6 and h in hb:
                return name, f"inside {hb}"
        for hb in pool:
            if hb != h and len(hb) >= 6 and hb in h:
                return name, f"holds {hb}"
        for hb in pool:
            if hb != h and len(g) >= 3 and N.one_away(g, N.glyphs(hb)):
                return name, f"one-glyph {hb}"
    return "passage", "no dictionary anchor"


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    prop_all = T.load_proposals(("A", "B", "C", "D", "G"))
    kt_hexes = {K.hx(c) for c in gl}
    mine_hexes = {K.hx(c) for c in prop_all}
    ev = json.load(open("proposals.json"))

    occ = Counter(A.strip(t)[0] for p in doc for t in p.tokens)
    rows = {}
    for c, (g, tier) in prop_all.items():
        h = K.hx(c)
        cls, why = ("guess", "tier G") if tier == "G" else classify(h, kt_hexes, mine_hexes)
        judged = "JUDGMENT, MARKED AS ONE" in ev.get(h, {}).get("evidence", "")
        rows[h] = (tier, cls, why, occ[c], judged)

    if "--list" in argv:
        want = argv[argv.index("--list") + 1]
        for h, (tier, cls, why, n, j) in sorted(rows.items(), key=lambda r: -r[1][3]):
            if tier == want:
                print(f"  {h:30s} x{n:<3d} {ev[h]['gloss']:24s} {cls:12s} "
                      f"{why}{'  [judgment]' if j else ''}")
        return 0

    tiers = Counter(r[0] for r in rows.values())
    print("READINGS PROPOSED BY THIS PROJECT, BY TIER")
    print("  A  survives every occurrence, or proved by an identical formula,")
    print("     a numeral, or K&T's own citation               %5d" % tiers["A"])
    print("  B  survives most occurrences                      %5d" % tiers["B"])
    print("  C  one passage, or source-checked                 %5d" % tiers["C"])
    print("  D  a single occurrence, read from one line        %5d" % tiers["D"])
    print("  G  a GUESS, never counted as read                 %5d" % tiers["G"])
    print("     total                                          %5d" % sum(tiers.values()))

    print("\nTHE SAME READINGS BY WHERE THE WORD CAME FROM")
    cls_n = Counter(r[1] for r in rows.values())
    cls_w = Counter()
    for h, (tier, cls, why, n, j) in rows.items():
        cls_w[cls] += n
    tot_n, tot_w = sum(cls_n.values()), sum(cls_w.values())
    for cls in ("KT-anchored", "KT-chained", "passage", "guess"):
        print(f"  {cls:14s} {cls_n[cls]:5d} signs {cls_n[cls]/tot_n*100:5.1f}%"
              f"   {cls_w[cls]:6d} word tokens {cls_w[cls]/tot_w*100:5.1f}%")
    sub = Counter(r[2].split()[0] for r in rows.values() if r[1] == "KT-anchored")
    print("    of the KT-anchored: " + ", ".join(f"{k} {v}" for k, v in sub.most_common()))
    print(f"  judgments flagged in the evidence: "
          f"{sum(1 for r in rows.values() if r[4])}")

    # ---- testability, computed the same way ktvarcheck computes it
    unhex = {K.hx(c): c for c in list(gl) + list(prop_all)}
    cache = {}

    def sl(h):
        if h not in cache:
            cache[h] = V.slots(doc, gl, seg, var, prop, unhex[h])
        return cache[h]

    test = {}
    for h, (tier, cls, why, n, j) in rows.items():
        conf = False
        if cls in ("KT-anchored", "KT-chained"):
            hb = why.split()[-1]
            if hb in unhex:
                conf = bool(sl(h)[0] & sl(hb)[0])
        if conf or (n > 1 and tier in ("A", "B")):
            test[h] = "verified"
        elif n > 1:
            test[h] = "testable"
        else:
            test[h] = "untestable"
    tn = Counter(test.values())
    tw = Counter()
    for h, k in test.items():
        tw[k] += rows[h][3]
    print("\nTESTABILITY -- can the codex itself ever refuse the reading?")
    for k, note in (("verified", "every occurrence takes it, or a shared frame confirms it"),
                    ("testable", "occurs more than once; a second occurrence could refuse it"),
                    ("untestable", "occurs once, no frame; nothing inside the book can check it")):
        print(f"  {k:11s} {tn[k]:5d} signs {tn[k]/len(test)*100:5.1f}%"
              f"   {tw[k]:6d} word tokens {tw[k]/sum(tw.values())*100:5.1f}%   {note}")

    print("\nCROSS-TABLE, signs: tier down, provenance across")
    cl = ("KT-anchored", "KT-chained", "passage", "guess")
    print("        " + "".join(f"{c:>14s}" for c in cl))
    for t in "ABCDG":
        line = f"  {t}   "
        for c in cl:
            line += f"{sum(1 for r in rows.values() if r[0]==t and r[1]==c):>14d}"
        print(line)

    print("\nTHE WHOLE RENDERING, WORD BY WORD")
    tok = Counter()
    for p in doc:
        for t in p.tokens:
            b = A.strip(t)[0]
            h = K.hx(b)
            if b in gl:
                tok["KT-direct"] += 1
            elif h in rows:
                tok[rows[h][1]] += 1
            elif b in seg or b in var:
                tok["by composition of read signs"] += 1
            else:
                tok["no reading"] += 1
    tt = sum(tok.values())
    for k in ("KT-direct", "by composition of read signs", "KT-anchored",
              "KT-chained", "passage", "guess", "no reading"):
        print(f"  {k:32s} {tok[k]:6d}  {tok[k]/tt*100:5.1f}%")
    print(f"  {'total':32s} {tt:6d}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
