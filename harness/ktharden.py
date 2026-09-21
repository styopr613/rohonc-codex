"""HARDEN OUR OWN READINGS. The 947 this project added, not K&T's 841.

ktkeycheck.py validated the key on 2026-09-21: K&T's headword citations land
on the folio they name 89.2% of the time, on the exact line 97.5% of the
time they land, against a 1.9% control. That is their dictionary and our
parse of it. It says nothing about the 947 readings THIS project added on
top, and nothing has ever tested those the same way.

This does not decide anything. It ranks. Every flag below is mechanical, is
declared here before the run, and means "a human should read this line",
never "this reading is wrong".

THE FLAGS, DECLARED BEFORE THE RUN.

  SOURCE   The sign stands on two or more folios whose cited passage we can
           look up, and the reading's English stem is in NONE of those
           passages, in either translation. A reading drawn from a source
           should appear in that source. One folio is not enough to flag on,
           because a word can be the book's own and not the passage's.

  DUP      An occurrence puts the reading within three places of another
           token already rendering the same content stem. A slot that is
           already spoken for. This rule has been run once before, on the
           bracketed guesses: 46 hits on 43 signs, 40 of them real errors.
           It has never been run on our READINGS.

  COLLIDE  Another sign already carries this English stem, and this reading
           is tier C or D. K&T legitimately have many signs per English
           word, so this is not an error by itself -- it is a flag only on
           the readings that were never tested at a second occurrence.

  BLAST    The sign is under three glyphs and stands inside ten or more
           distinct word types. Two readings have already had to be
           withdrawn for this (540 'shall', 570 'ark') and both took
           coverage down with them, correctly. A short piece is read through
           the words it feeds, not its own occurrences.

  ALONE    Tier C or D, occurs once, on a folio with no citation we can look
           up. Nothing internal and nothing external can test it. Not a
           fault -- a statement of what is not knowable, kept countable.

NO BAR IS SET ON THE FLAG COUNTS, deliberately. A count of flags is not a
result and must never be reported as one. The deliverable is the worklist,
worst first, and the only thing that closes an item is a person reading the
occurrences. Do not "fix" a flag by editing the flag.

    python3 ktharden.py                  the worklist, worst first
    python3 ktharden.py --flag SOURCE    one class in full
    python3 ktharden.py --sign HEX       everything known about one reading
"""
import json
import os
import re
import sys
from collections import Counter, defaultdict

import ktaffix as A
import ktcross as K
import ktleft as L
import ktnear as N
import ktrederive as R
import kttranslate as T

OURS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "proposals.json")
TIERS = ("A", "B", "C", "D")
NEAR = 3
BLAST_GLYPHS = 3
BLAST_TYPES = 10


def load_ours():
    p = json.load(open(OURS, encoding="utf-8"))
    return {k: v for k, v in p.items()
            if not k.startswith("_") and isinstance(v, dict)
            and v.get("tier") in TIERS}


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    ours = load_ours()
    vv, vd = L.verses(), L.verses_dr()

    # where every sign stands, and what the renderer prints for each token
    where = defaultdict(list)
    rendered = {}
    types = Counter()
    for p in doc:
        for i, ln in enumerate(p.lines, 1):
            toks = [x for run in ln for x in run]
            for j, t in enumerate(toks):
                h = K.hx(A.strip(t)[0])
                where[h].append((p.page, i, j))
                types[K.hx(t)] += 1
                if K.hx(t) not in rendered:
                    rendered[K.hx(t)] = T.render_token(t, gl, seg, False, var, prop)

    # cited passages per folio
    refs, pool = {}, {}
    for pg in sorted({p.page for p in doc}):
        r = L.refs_in(K.note_for(pg))
        if r:
            refs[pg] = r
            s = set()
            for k, txt in L.passage(vv, r) + L.passage(vd, r):
                s |= R.stems(txt)
            pool[pg] = s

    # which stems another sign already carries
    carried = defaultdict(set)
    for c, gs in gl.items():
        for st in R.stems("; ".join(gs)):
            carried[st].add(K.hx(c))
    for h, v in ours.items():
        for st in R.stems(v.get("gloss", "")):
            carried[st].add(h)

    # blast radius: distinct word types a sign stands inside
    feeds = Counter()
    for ht in types:
        for h in ours:
            if len(h) > len(ht):
                continue
            j = ht.find(h)
            while j != -1:
                if j % 3 == 0 and (j + len(h)) % 3 == 0:
                    feeds[h] += 1
                    break
                j = ht.find(h, j + 1)

    rows = []
    for h, v in sorted(ours.items()):
        gloss = v.get("gloss", "")
        tier = v["tier"]
        st = R.stems(gloss)
        occ = where.get(h, [])
        flags = []

        cited = sorted({pg for pg, _, _ in occ if pg in pool})
        if len(cited) >= 2 and st and not any(st & pool[pg] for pg in cited):
            flags.append("SOURCE")

        dup = []
        for pg, i, j in occ:
            page = next((p for p in doc if p.page == pg), None)
            if not page:
                continue
            toks = [x for run in page.lines[i - 1] for x in run]
            for k2, t2 in enumerate(toks):
                if k2 == j or abs(k2 - j) > NEAR:
                    continue
                if st & R.stems(rendered.get(K.hx(t2), "")):
                    dup.append(f"{pg}:{i}")
                    break
        if dup:
            flags.append("DUP")

        if tier in ("C", "D") and any(len(carried[s] - {h}) > 0 for s in st):
            flags.append("COLLIDE")

        if len(N.glyphs(h)) < BLAST_GLYPHS and feeds[h] >= BLAST_TYPES:
            flags.append("BLAST")

        if tier in ("C", "D") and len(occ) <= 1 and not cited:
            flags.append("ALONE")

        rows.append((h, tier, gloss, len(occ), len(cited), feeds[h], flags, dup[:3]))

    flagged = [r for r in rows if r[6]]
    cnt = Counter(f for r in rows for f in r[6])
    print(f"HARDENING OUR OWN {len(rows)} READINGS (tiers A-D). "
          f"K&T's are not touched.\n")
    print(f"  {'tier':5s} {'readings':>9s} {'flagged':>8s}")
    for t in TIERS:
        rs = [r for r in rows if r[1] == t]
        print(f"  {t:5s} {len(rs):9d} {sum(1 for r in rs if r[6]):8d}")
    print(f"\n  flags raised (a reading can raise several):")
    for f in ("SOURCE", "DUP", "COLLIDE", "BLAST", "ALONE"):
        print(f"    {f:8s} {cnt[f]:5d}")
    print(f"\n  {len(flagged)} readings of {len(rows)} want a human. "
          f"{len(rows)-len(flagged)} raise nothing.")

    if "--sign" in argv:
        want = argv[argv.index("--sign") + 1]
        for r in rows:
            if r[0] == want:
                print(f"\n  {r[0]}  tier {r[1]}  '{r[2]}'")
                print(f"    occurrences {r[3]}, on cited folios {r[4]}, "
                      f"feeds {r[5]} word types")
                print(f"    flags: {', '.join(r[6]) or 'none'}")
                for pg, i, j in where.get(want, [])[:12]:
                    print(f"      {pg}:{i}")
        return 0

    if "--flag" in argv:
        want = argv[argv.index("--flag") + 1]
        print()
        for h, tier, gloss, n, nc, fd, flags, dup in flagged:
            if want in flags:
                print(f"    {h:22s} {tier}  n={n:<4d} cited={nc:<3d} "
                      f"'{gloss[:30]}'  {' '.join(dup)}")
        return 0

    print("\n  WORST FIRST (most flags, then most occurrences, "
          "because a wrong sign\n  standing in many places does the most "
          "damage):\n")
    for h, tier, gloss, n, nc, fd, flags, dup in sorted(
            flagged, key=lambda r: (-len(r[6]), -r[3]))[:40]:
        print(f"    {h:22s} {tier}  n={n:<4d} feeds={fd:<4d} "
              f"{','.join(flags):28s} '{gloss[:26]}'")
    print(f"\n  full list: --flag SOURCE | DUP | COLLIDE | BLAST | ALONE")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
