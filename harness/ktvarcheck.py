"""Does "one glyph apart" mean "the same word"? The test that can say no.

ktnear.py assumes a scribe copying a long compilation spells one word several
ways. That assumption has a symmetric failure and it has to be tested rather
than trusted: two genuinely different words one glyph apart get merged into
one, and nothing in the rendering would show it. A rule that only ever fires
in one direction is not a rule.

THE TEST, declared before it was run.

  For each reading this project made on a near-match or a containment
  argument, take the sign H and the sign B it was anchored on, and compare
  the slots they stand in. A "slot" is the pair (word before, word after) as
  the rendering prints them.

    SAME SLOT      some (before, after) pair occurs with BOTH H and B, in
                   different places in the book. Two spellings doing the
                   same job in the same frame. This is positive evidence
                   that they are one word -- it is how 7e6 was proved to be
                   K&T's 7e8 'say', by the codex writing "miracle _ which-
                   mouth" twice, once with each.

    CO-OCCUR       H and B stand on the same LINE and share no slot. Weak
                   evidence that they are DIFFERENT words, and only weak:
                   this book demonstrably writes one word two ways in one
                   line -- 055r:10 has K&T's form of "the three Marys" and
                   the prefixed form together, and 144v:1 and 144v:7 do the
                   same with "queen". So this class is for review by hand,
                   not a verdict.

    UNTESTED       neither. Usually because one of the two occurs once, so
                   the book contains nothing that could decide. This is the
                   honest size of the exposure and it is printed as such.

  No reading is deleted by this script. It prints what each one rests on.

    python ktvarcheck.py            the three classes, with counts
    python ktvarcheck.py --show X   every reading in class X, in full
"""
import json
import sys
from collections import defaultdict

import ktaffix as A
import ktcross as K
import ktprov as P
import kttranslate as T


def slots(doc, gl, seg, var, prop, target):
    """{(before, after)} and {(page, line)} for one sign."""
    sl, lines = set(), set()
    for p in doc:
        for i, ln in enumerate(p.lines, 1):
            tk = [t for run in ln for t in run]
            for j, t in enumerate(tk):
                if A.strip(t)[0] != target:
                    continue
                lines.add((p.page, i))
                b = T.render_token(tk[j - 1], gl, seg, False, var, prop) if j else "^"
                a = (T.render_token(tk[j + 1], gl, seg, False, var, prop)
                     if j + 1 < len(tk) else "$")
                sl.add((b, a))
    return sl, lines


def _same_word(a, b):
    """Does this reading claim the same word as the sign it was anchored on?"""
    wa = {w for w in a.lower().replace("_", " ").split()}
    wb = set()
    for part in b.lower().replace("_", " ").split(";"):
        wb |= set(part.split())
    drop = {"the", "a", "an", "of", "to", "his", "her", "and"}
    return bool((wa - drop) & (wb - drop))


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    prop_all = T.load_proposals(("A", "B", "C", "D", "G"))
    kt_hexes = {K.hx(c) for c in gl}
    mine_hexes = {K.hx(c) for c in prop_all}
    ev = json.load(open("proposals.json"))
    unhex = {K.hx(c): c for c in list(gl) + list(prop_all)}

    cache = {}

    def get(h):
        if h not in cache:
            cache[h] = slots(doc, gl, seg, var, prop, unhex[h])
        return cache[h]

    out = defaultdict(list)
    for c, (g, tier) in prop_all.items():
        h = K.hx(c)
        if tier == "G":
            continue
        cls, why = P.classify(h, kt_hexes, mine_hexes)
        if cls not in ("KT-anchored", "KT-chained"):
            continue
        kind, hb = why.split()
        if hb not in unhex:
            continue
        sh, lh = get(h)
        sb, lb = get(hb)
        shared = sh & sb
        both = lh & lb
        # A MERGE CLAIM is a reading that gives this sign the SAME word as the
        # sign it was anchored on -- that is where two distinct signs could be
        # collapsed into one. Where the glosses differ, the reading has already
        # said the two are different words and there is nothing to merge; those
        # are reported apart so they do not pad the risk set.
        gb_txt = (ev.get(hb, {}).get("gloss")
                  or "; ".join(gl.get(unhex[hb], ["?"])))
        merge = _same_word(g, gb_txt)
        if shared:
            state = "SAME SLOT"
        elif both:
            state = "CO-OCCUR"
        else:
            state = "UNTESTED"
        if not merge:
            state = "NOT A MERGE"
        out[state].append((h, ev[h]["gloss"], tier, kind, hb,
                           ev.get(hb, {}).get("gloss") or "; ".join(gl.get(unhex[hb], ["?"]))[:34],
                           sorted(shared)[:2], sorted(both)[:3], len(lh), len(lb)))

    if "--show" in argv:
        want = " ".join(argv[argv.index("--show") + 1:]).upper()
        for r in sorted(out.get(want, ()), key=lambda r: -r[8]):
            h, g, tier, kind, hb, gb, shared, both, nh, nb = r
            print(f"\n  {h}  = {g}  (tier {tier}, {nh} line(s))")
            print(f"    anchored {kind} on {hb} = {gb}  ({nb} line(s))")
            if shared:
                print(f"    same slot: {shared}")
            if both:
                print(f"    both on:   {', '.join(f'{p}:{i}' for p, i in both)}")
        return 0

    tot = sum(len(v) for v in out.values())
    merges = tot - len(out["NOT A MERGE"])
    print("READINGS MADE ON A NEAR-MATCH OR A CONTAINMENT ARGUMENT: %d" % tot)
    print(f"  of those, {len(out['NOT A MERGE'])} give the sign a DIFFERENT word from the")
    print("  one they were anchored on, so they claim no merge and cannot cause one.")
    print(f"  The risk set is the other {merges}, which say the two are one word:")
    print()
    for state, note in (
            ("SAME SLOT", "the book writes both forms in the same frame -- one word"),
            ("CO-OCCUR", "both on one line, no shared frame -- review by hand"),
            ("UNTESTED", "nothing in the book can decide; this is the exposure")):
        v = out[state]
        print(f"  {state:10s} {len(v):5d}  {len(v)/max(merges,1)*100:5.1f}%   {note}")
    print()
    print("  Of the UNTESTED, how many have a one-occurrence sign on one side:")
    thin = sum(1 for r in out["UNTESTED"] if r[8] == 1 or r[9] == 1)
    print(f"    {thin} of {len(out['UNTESTED'])}")
    print()
    print("  CO-OCCUR is NOT a refutation. This book writes one word two ways in")
    print("  one line: 055r:10 carries K&T's form of 'the three Marys' and the")
    print("  prefixed form together, and 144v does the same with 'queen'. Use")
    print("  --show CO-OCCUR and read them.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
