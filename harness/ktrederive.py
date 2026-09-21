"""GATE 4: held-out rederivation. Does this pipeline find truth, or itself?

Everything measured so far tests a mechanism. Nothing tests the LOOP -- the
tool proposing candidates and a reader choosing among them -- because the
reader has had no ground truth to be scored against. There is exactly one
ground truth available: Kiraly and Tokai's own dictionary. Hide part of it
and see whether the pipeline puts it back.

All bars below are declared before any run. A near miss is a miss.

--------------------------------------------------------------------------
GATE 4a. MECHANICAL REDERIVATION.

  Mask a seeded random 10% of K&T's entries. The masked signs are then
  invisible to the tools exactly as a genuinely unread sign is. For each
  one, build the candidate set the way the pipeline does:

    * the cited-passage pool of a folio it stands on, minus every word
      already spoken for by an UNMASKED sign;
    * plus the glosses of its structural neighbours -- signs it sits
      inside, contains whole, or is one glyph from -- if any survive
      masking.

  Score PRESENCE (a content stem of the true gloss is in the candidate set)
  and TOP-1 (rarest-in-the-passage ranking puts it first).

  CONTROL: the identical procedure with the tether cut -- the folio's own
  passage replaced by a randomly chosen other cited folio's passage, and
  structural neighbours replaced by randomly chosen signs of the same
  length. 20 shuffles.

  BAR: presence must beat the control mean by 5 sigma.

  DECLARED BEFORE THE RUN, because it decided the last test of this kind:
  masked K&T signs are NOT a representative sample of the signs still
  unread. K&T glossed the words they could, which are the ones with
  relatives in their own dictionary; the 826 signs still dark occur once
  and have no such relatives. So the headline number is the one restricted
  to masked signs WITH NO SURVIVING STRUCTURAL NEIGHBOUR. The
  with-neighbour figure is reported too and is the easier population.

--------------------------------------------------------------------------
GATE 4b. THE JUDGMENT STEP, WHICH IS THE ONE NOTHING HAS MEASURED.

  A seeded sample of 25 masked signs is written to a file with everything
  the pipeline offers and NO gloss: every occurrence rendered, the chapter
  and verse each folio cites (the reference only, never this project's own
  English translation of the folio, which would leak the answer), the
  surviving pool, and any structural neighbours. A reading is committed for
  each, in writing, before anything is revealed. Then it is scored.

  Scoring: a hit is a content stem shared with K&T's gloss for that sign.
  Twenty-five is too few for a sigma, so the bar is stated as consequences
  instead, and they bind:

    >= 50%   the judgment step does real work; the 290 passage-read signs
             are calibrated by it and tier C stands as written
    30-50%   it adds something over the mechanical baseline, but tier C
             should be read as "more likely than not" and no stronger
    15-30%   it adds little; the passage-read tier C entries should be
             downgraded to D
    < 15%    the passage-read class should be withdrawn wholesale

  python ktrederive.py --gate 4a [--shuf N]
  python ktrederive.py --dump        write the blind sample for 4b
  python ktrederive.py --score FILE  reveal and score the committed readings
"""
import json
import os
import random
import re
import sys
from collections import Counter, defaultdict

import ktaffix as A
import ktcross as K
import ktleft as L
import ktnear as N

SEED = 20260921
MASK_FRACTION = 0.10
SAMPLE = 25
BAR = 5.0
BLIND = os.path.join(os.path.dirname(__file__), "..", "work", "rohonc",
                     "rederive_blind.txt")


def stems(text):
    out = set()
    g = re.sub(r"[<\[(][^>\])]*[>\])]", " ", text).translate(K.ACCENT)
    for w in re.findall(r"[a-zA-Z]+", g):
        if w.lower() in K.STOP or len(w) < 3:
            continue
        out.add(K.stem(w))
    return out


def masked_set(gl):
    hs = sorted(K.hx(c) for c in gl)
    rng = random.Random(SEED)  # module-level; ktblind.py overwrites it
    rng.shuffle(hs)
    return set(hs[:int(len(hs) * MASK_FRACTION)])


def build_world(gl, doc, mask):
    """What the tools can see once the masked entries are hidden."""
    unhex = {K.hx(c): c for c in gl}
    visible = {h: "; ".join(gl[unhex[h]]) for h in unhex if h not in mask}
    where = defaultdict(list)
    for p in doc:
        for i, ln in enumerate(p.lines, 1):
            for t in [x for run in ln for x in run]:
                where[K.hx(A.strip(t)[0])].append((p.page, i))
    refs = {}
    for p in sorted({q.page for q in doc}):
        r = L.refs_in(K.note_for(p))
        if r:
            refs[p] = r
    return unhex, visible, where, refs


def neighbours(h, visible):
    out = []
    g = N.glyphs(h)
    for hb, gb in visible.items():
        if hb == h:
            continue
        if (len(h) >= 6 and h in hb) or (len(hb) >= 6 and hb in h):
            out.append((hb, gb, "structure"))
        elif len(g) >= 3 and N.one_away(g, N.glyphs(hb)):
            out.append((hb, gb, "one glyph"))
    return out[:6]


def pool_for(page, refs, vv, vd, idx):
    if page not in refs:
        return set(), ""
    both, dro, kjo, syn = L.pools_for(vv, vd, refs[page], idx, 0)
    words = set()
    for d in (both, dro, kjo):
        for st, forms in d.items():
            words.add(st)
    return words, ", ".join(
        (f"{r[0]} {r[1]}:{r[2]}" + (f"-{r[3]}" if len(r) > 3 and r[3] != r[2]
                                    and r[3] != 999 else ""))
        for r in refs[page][:4])


def taken_index_visible(visible):
    idx = defaultdict(list)
    for h, g in visible.items():
        for st in stems(g):
            idx[st].append((h, g))
    return idx


def gate4a(gl, doc, nshuf):
    mask = masked_set(gl)
    unhex, visible, where, refs = build_world(gl, doc, mask)
    vv, vd = L.verses(), L.verses_dr()
    idx = taken_index_visible(visible)
    cited = sorted(refs)
    pools = {}
    for pg in cited:
        pools[pg] = pool_for(pg, refs, vv, vd, idx)[0]
    freq = Counter()
    for t in (vv, vd):
        for txt in t.values():
            freq.update(K.stem(w.lower()) for w in re.findall(r"[A-Za-z]+", txt))

    rng = random.Random(SEED + 7)
    byline = defaultdict(list)
    for h in visible:
        byline[len(N.glyphs(h))].append(h)

    rows = []
    for h in sorted(mask):
        truth = stems("; ".join(gl[unhex[h]]))
        if not truth:
            continue
        pgs = [pg for pg, _ in where[h] if pg in pools]
        nb = neighbours(h, visible)
        cand = set()
        for pg in pgs[:3]:
            cand |= pools[pg]
        for hb, gb, kind in nb:
            cand |= stems(gb)
        ctrl_sets = []
        for j in range(nshuf):
            r2 = random.Random(SEED + 100 + j)
            c = set()
            for _ in pgs[:3]:
                c |= pools[r2.choice(cited)]
            for hb, gb, kind in nb:
                pool_len = byline.get(len(N.glyphs(hb))) or list(visible)
                c |= stems(visible[r2.choice(pool_len)])
            ctrl_sets.append(c)
        rows.append((h, truth, cand, ctrl_sets, bool(nb), bool(pgs)))

    def report(sel, label):
        rs = [r for r in rows if sel(r)]
        if not rs:
            print(f"  {label}: no signs in this stratum")
            return None
        pres = sum(1 for r in rs if r[1] & r[2]) / len(rs)
        top1 = 0
        for h, truth, cand, cs, nb, pg in rs:
            if not cand:
                continue
            order = sorted(cand, key=lambda s: (freq.get(s, 0), s))
            if order and order[0] in truth:
                top1 += 1
        top1 /= len(rs)
        ctrl = []
        for j in range(nshuf):
            ctrl.append(sum(1 for r in rs if r[1] & r[3][j]) / len(rs))
        m = sum(ctrl) / len(ctrl)
        sd = (sum((c - m) ** 2 for c in ctrl) / max(len(ctrl) - 1, 1)) ** 0.5
        sig = (pres - m) / sd if sd else float("inf")
        print(f"  {label}")
        print(f"    signs                                     {len(rs)}")
        print(f"    true gloss present in the candidate set   {pres*100:.1f}%")
        print(f"    control, tether cut                       {m*100:.1f}%")
        print(f"    top candidate correct                     {top1*100:.1f}%")
        print(f"    {sig:.1f} sigma, beats {sum(1 for c in ctrl if pres > c)} of {len(ctrl)}")
        return sig

    print(f"GATE 4a  mechanical rederivation of {len(rows)} masked K&T entries")
    print(f"  (masked {len(mask)} of {len(gl)} entries, seed {SEED})\n")
    s_all = report(lambda r: True, "ALL masked signs")
    print()
    s_nonb = report(lambda r: not r[4], "NO surviving structural neighbour  <- THE HEADLINE")
    print()
    report(lambda r: r[4], "with a structural neighbour (the easier population)")
    print()
    ok = s_nonb is not None and s_nonb >= BAR
    print(f"  headline {s_nonb:.1f} sigma against a bar of {BAR}  -> "
          f"{'PASS' if ok else 'FAIL'}")
    return ok


def dump(gl, doc):
    mask = masked_set(gl)
    unhex, visible, where, refs = build_world(gl, doc, mask)
    vv, vd = L.verses(), L.verses_dr()
    idx = taken_index_visible(visible)
    gl2, doc2, seg2, var2, prop2, inv2 = K.build()
    rng = random.Random(SEED + 31)
    # only signs the pipeline would ever attempt: a citation or a neighbour
    pool_signs = [h for h in sorted(mask)
                  if stems("; ".join(gl[unhex[h]]))
                  and (any(pg in refs for pg, _ in where[h]) or neighbours(h, visible))]
    rng.shuffle(pool_signs)
    sample = pool_signs[:SAMPLE]
    import kttranslate as T
    os.makedirs(os.path.dirname(BLIND), exist_ok=True)
    with open(BLIND, "w", encoding="utf-8") as f:
        f.write("GATE 4b BLIND SAMPLE. %d signs, seed %d.\n" % (len(sample), SEED))
        f.write("K&T read every one of these. Their gloss is NOT in this file.\n")
        f.write("Write one reading per sign on the READING: line. Then score.\n\n")
        for h in sample:
            f.write(f"=== {h}   x{len(where[h])} occurrence(s)\n")
            seen = set()
            for pg, i in where[h][:6]:
                for p in doc:
                    if p.page != pg:
                        continue
                    ln = p.lines[i - 1]
                    tk = [x for run in ln for x in run]
                    s = " ".join(("<<MASKED %s>>" % K.hx(A.strip(t)[0]))
                                 if K.hx(A.strip(t)[0]) in mask
                                 # K&T's dictionary ONLY. This used to pass prop2 -- this
                                 # project's own readings -- so a masked sign sat in a
                                 # context that already contained our guesses, marked
                                 # ? and o, and at least one answer ("Paradise") was
                                 # handed to the reader that way. Fixed 2026-09-21.
                                 else T.render_token(t, gl2, seg2, False, var2, None)
                                 for t in tk)
                    f.write(f"  {pg}:{i:<3d} {s[:170]}\n")
                if pg in refs and pg not in seen:
                    seen.add(pg)
                    pw, ref = pool_for(pg, refs, vv, vd, idx)
                    f.write(f"      cites: {ref}\n")
                    f.write(f"      free in that passage: "
                            f"{', '.join(sorted(pw)[:40])}\n")
            for hb, gb, kind in neighbours(h, visible):
                f.write(f"      {kind}: {hb} = {gb[:60]}\n")
            f.write("  READING: \n\n")
    print(f"wrote {BLIND}")
    print("Nothing in that file contains K&T's gloss for any sampled sign.")
    return 0


def score(gl, path):
    mask = masked_set(gl)
    unhex = {K.hx(c): c for c in gl}
    text = open(path, encoding="utf-8").read()
    got = re.findall(r"^=== ([0-9a-f]+).*?^  READING:(.*?)$", text, re.M | re.S)
    hits = miss = blank = 0
    print("GATE 4b  the judgment step, scored against K&T's own dictionary\n")
    for h, rd in got:
        rd = rd.strip().splitlines()[0].strip() if rd.strip() else ""
        truth = "; ".join(gl[unhex[h]])
        if not rd:
            blank += 1
            print(f"  {h:24s} (no reading committed)   truth = {truth[:60]}")
            continue
        hit = bool(stems(rd) & stems(truth))
        hits += hit
        miss += not hit
        print(f"  {h:24s} {'HIT ' if hit else 'miss'}  read '{rd[:34]}'"
              f"   truth = {truth[:56]}")
    n = hits + miss
    print(f"\n  committed {n}, blank {blank}")
    if n:
        r = hits / n
        print(f"  recovered {hits} of {n}   {r*100:.1f}%")
        band = (">= 50%: judgment does real work, tier C stands as written"
                if r >= .5 else
                "30-50%: adds something; tier C means 'more likely than not'"
                if r >= .3 else
                "15-30%: adds little; passage-read tier C should become D"
                if r >= .15 else
                "< 15%: the passage-read class should be withdrawn wholesale")
        print(f"  declared consequence: {band}")
    return 0


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    nshuf = int(argv[argv.index("--shuf") + 1]) if "--shuf" in argv else 20
    if "--dump" in argv:
        return dump(gl, doc)
    if "--score" in argv:
        return score(gl, argv[argv.index("--score") + 1])
    print(f"Bars declared in the docstring before the run. seed {SEED}.\n")
    return 0 if gate4a(gl, doc, nshuf) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
