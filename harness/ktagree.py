"""EVERY ONE OF OUR READINGS, PUT BACK TO KIRALY AND TOKAI'S DICTIONARY.

Not the flagged ones. All of them.

The two readings recovered on 2026-09-21 were both found the same way, and
not by reading lines: 9107c1 was glossed 'with all thy heart' when K&T's own
entries make it 910 (passive particle) + 7c1 (verb, LOVE) = 'be loved', and
7b2 was glossed 'son' when their relative-pronoun entry lists it as a variant
of 'who'. Both were sitting in the dictionary the whole time. So this sweeps
every reading we have against what they actually wrote.

THREE CHECKS, in descending order of force, declared before the run:

  CONFLICT  K&T gloss this EXACT sign and our gloss shares no content stem
            with theirs. A flat contradiction of the key. Nothing outranks
            this, and it should be empty.

  REBUILD   K&T do not gloss the whole sign, but their entries cover every
            glyph of it, and our gloss shares no stem with any part. The
            sign is theirs end to end and we read it as something their
            pieces do not say. This is the 9107c1 shape.

  PARTIAL   Their entries cover most of it and our gloss shares nothing with
            the covered part. Weaker: the uncovered glyphs may carry the
            sense.

  AGREES    our gloss shares a stem with theirs, whole or in part.
  UNCOVERED K&T gloss none of it. Not a fault -- these are the signs this
            project exists to read.

NO BAR. A hit is not a verdict: composition is real, and 'good shepherd' is
not required to share a stem with 'sheep'. CONFLICT and REBUILD are to be
read by hand, every one.

    python3 ktagree.py
    python3 ktagree.py --class REBUILD
"""
import json
import sys
from collections import Counter

import ktcross as K
import ktdict
import ktrederive as R

GL = 3


def kt_index():
    out = {}
    for code, glosses, folios in ktdict.load():
        h = K.hx(code)
        g = "; ".join(sorted(glosses))
        if h and g:
            out.setdefault(h, g)
    return out


def cover(h, kt):
    """Greedy longest-first decomposition into K&T-glossed pieces."""
    parts, i = [], 0
    while i < len(h):
        for j in range(len(h), i, -GL):
            if (j - i) % GL:
                continue
            if h[i:j] in kt:
                parts.append((h[i:j], kt[h[i:j]]))
                i = j
                break
        else:
            parts.append((h[i:i + GL], None))
            i += GL
    return parts


def main(argv):
    kt = kt_index()
    p = json.load(open('proposals.json', encoding='utf-8'))
    ours = {k: v for k, v in p.items()
            if not k.startswith('_') and isinstance(v, dict)
            and v.get('tier') in ('A', 'B', 'C', 'D')}

    rows = []
    for h, v in sorted(ours.items()):
        mine = R.stems(v.get('gloss', ''))
        if h in kt:
            theirs = R.stems(kt[h])
            kind = "AGREES" if (mine & theirs) or not (mine and theirs) \
                else "CONFLICT"
            rows.append((kind, h, v, kt[h], None)); continue
        parts = cover(h, kt)
        covered = [x for x in parts if x[1]]
        if not covered:
            rows.append(("UNCOVERED", h, v, "", parts)); continue
        pstems = set()
        for _, g in covered:
            pstems |= R.stems(g)
        if mine & pstems:
            rows.append(("AGREES", h, v, "", parts)); continue
        whole = all(x[1] for x in parts)
        rows.append(("REBUILD" if whole else "PARTIAL", h, v, "", parts))

    cnt = Counter(r[0] for r in rows)
    print(f"OUR {len(rows)} READINGS, AGAINST K&T'S DICTIONARY\n")
    for k in ("CONFLICT", "REBUILD", "PARTIAL", "AGREES", "UNCOVERED"):
        print(f"    {k:10s} {cnt[k]:5d}")
    want = argv[argv.index('--class') + 1] if '--class' in argv else None
    for kind in ([want] if want else ["CONFLICT", "REBUILD"]):
        sel = [r for r in rows if r[0] == kind]
        print(f"\n  {kind} ({len(sel)}):\n")
        for k, h, v, theirs, parts in sorted(
                sel, key=lambda r: -(r[2].get('n') or 0)):
            print(f"    {h:22s} {v['tier']} n={str(v.get('n')):<4} "
                  f"ours '{v['gloss'][:24]}'")
            if theirs:
                print(f"      K&T say: {theirs[:96]}")
            elif parts:
                for ph, pg in parts:
                    print(f"        {ph:12s} {(pg or '(not glossed)')[:78]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
