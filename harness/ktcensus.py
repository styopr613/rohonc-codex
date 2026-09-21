"""TEST 13: the underdetermination census. Does the keep-rule identify a
gloss, or merely license one?

Grok's objection: "consistent at every occurrence" is satisfied by any
word that happens to be in every passage the sign's folios cite. If most
tier A/B signs have a SECOND such word, not a form of the chosen one, the
rule licensed the readings rather than identifying them.

THE COUNT, declared before the run:
  * every tier A or B reading whose gloss has a content stem and whose
    sign stands on folios citing >= 3 DISTINCT chapters (a chapter counted
    once however many folios cite it);
  * the pool of a chapter is its content stems, Douay and King James,
    minus every stem K&T's own glosses carry;
  * survivors = the stems present in every one of the sign's chapters;
  * the chosen gloss SURVIVES if one of its stems is a survivor;
  * a RIVAL is a survivor that is not a stem of the chosen gloss and does
    not share its first four letters with one (declared as the variant
    rule: bless/blessing, judg/judgment);
  * chance: for each sign, 20 draws of a random stem whose frequency over
    both Bibles is within a factor of two of the chosen stem's, counting
    how often such a stem survives all the sign's chapters.

Also reported, no bar: the same count at the scale the notes actually cite
(usually a single verse), and the companion Mad-Libs count -- the fraction
of A/B signs that stand, on at least one line of a folio named in their
evidence, as the ONLY sign K&T did not read.

BAR, declared before the run, not moved (Grok's, verbatim):
  FAIL if more than 40% of the counted A/B signs have a rival that also
  satisfies the keep-rule. Such signs are licensed, not identified.

    python3 ktcensus.py
"""
import json
import random
import re
import sys
from collections import Counter, defaultdict

import ktaffix as A
import ktcross as K
import ktleft as L
import ktrederive as R
import kttestlib as TL

SEED = 20260921
NDRAW = 20
FOLIO = re.compile(r"\b(\d{3}[rv])\b")


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    p = json.load(open('proposals.json', encoding='utf-8'))
    vv, vd = L.verses(), L.verses_dr()
    refs = TL.cited(doc)
    taken = TL.kt_taken(gl)
    freq = TL.corpus_freq(vv, vd)
    chap = defaultdict(set)
    for t in (vv, vd):
        for (b, c, v), txt in t.items():
            chap[(b, c)] |= TL.content(txt)
    cpool = {k: s - taken for k, s in chap.items()}
    vpool = TL.free_pools(doc, gl, vv, vd, refs)
    folio_ch = {f: sorted({(b, c) for b, c, _, _ in r if (b, c) in cpool}) for f, r in refs.items()}
    fs = TL.folio_signs(doc)
    sf = defaultdict(set)
    for f, ss in fs.items():
        for s in ss:
            sf[s].add(f)
    un = lambda h: "".join(chr(0xE000 + int(h[i:i + 3], 16)) for i in range(0, len(h), 3))
    by_freq = sorted(freq, key=lambda s: freq[s])
    rng = random.Random(SEED)

    def rival(s, chosen):
        return s not in chosen and not any(s[:4] == c[:4] for c in chosen)

    def census(pool_of, units_of, label):
        n = surv = riv = 0
        chance_hits = chance_tot = 0
        rivals_listed = []
        for h, v in sorted(p.items()):
            if not isinstance(v, dict) or v.get('tier') not in 'AB':
                continue
            chosen = TL.content(v['gloss'].replace('_', ' '))
            if not chosen:
                continue
            units = sorted({u for f in sf.get(un(h), ()) for u in units_of.get(f, ())})
            if len(units) < 3:
                continue
            n += 1
            sv = None
            for u in units:
                sv = set(pool_of[u]) if sv is None else sv & pool_of[u]
            sv = sv or set()
            if sv & chosen:
                surv += 1
            rv = sorted(s for s in sv if rival(s, chosen))
            if rv:
                riv += 1
                rivals_listed.append((h, v['gloss'], len(units), rv[:5]))
            # chance
            cs = min(chosen, key=lambda s: freq.get(s, 0))
            f0 = max(1, freq.get(cs, 1))
            band = [s for s in by_freq if f0 / 2 <= freq[s] <= f0 * 2]
            for _ in range(NDRAW):
                s = rng.choice(band)
                chance_tot += 1
                chance_hits += all(s in pool_of[u] for u in units)
        print(f"  {label}")
        print(f"    A/B signs counted (>= 3 distinct units)     {n}")
        print(f"    chosen gloss survives every unit            {surv:4d}   {surv/max(1,n)*100:5.1f}%")
        print(f"    a rival stem also survives                  {riv:4d}   {riv/max(1,n)*100:5.1f}%")
        print(f"    chance: matched-frequency stem survives     {chance_hits/max(1,chance_tot)*100:5.1f}%")
        return n, surv, riv, rivals_listed

    print("TEST 13: UNDERDETERMINATION CENSUS OF TIER A/B")
    print(f"  chapters with a pool {len(cpool)}; seed {SEED}\n")
    n, surv, riv, lst = census(cpool, folio_ch, "chapter scale (the count the bar is on)")
    for h, g, k, rv in lst[:40]:
        print(f"      {h:22s} {g[:18]:18s} {k} chapters   rivals: {', '.join(rv)}")
    print()
    census(vpool, {f: [f] for f in vpool}, "verse scale, as the notes cite (reported, no bar)")
    print()
    # companion: Mad-Libs count
    unread_line = defaultdict(set)   # folio -> set of signs that are the only unread sign on a line
    for pg in doc:
        for ln in pg.lines:
            toks = [A.strip(t)[0] for run in ln for t in run]
            miss = [s for s in toks if s not in gl and s not in var]
            if len(miss) == 1:
                unread_line[pg.page].add(miss[0])
    madlib = tot = 0
    for h, v in p.items():
        if not isinstance(v, dict) or v.get('tier') not in 'AB':
            continue
        tot += 1
        ev = set(FOLIO.findall(v.get('evidence', '')))
        if any(un(h) in unread_line.get(f, ()) for f in ev):
            madlib += 1
    print(f"  companion: A/B signs that are the only K&T-unread sign on some line of an "
          f"evidence folio   {madlib} of {tot}   {madlib/tot*100:.1f}%   (reported, no bar)")
    print()
    ok = riv / max(1, n) <= 0.40
    print(f"  BAR: rivals in <= 40% of counted signs  ->  {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
