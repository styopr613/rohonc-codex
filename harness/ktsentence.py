"""TEST 5: our readings against sentences Király and Tokai translated whole.

External ground truth that was never used to make a reading. Their
dictionary quotes example sentences from the codex -- a run of codes, then
their English, then the folio and line -- and those sentences contain signs
they never glossed on their own. Their sentence translation says what such
a sign means there, in their words, written before this project existed.
If one of OUR readings stands in such a sentence, its gloss should be in
their English.

  hit      a content stem of our gloss is in the stems of their translation
           of a sentence the sign stands in
  rate     hits / (our sign, their sentence) pairs, per tier

EXCLUDED: any reading whose evidence mentions Kiraly, Király or K&T. Some of
today's corrections were taken straight from these very sentences, and some
older readings cite their entries; all of those are circular here and are
left out, at the cost of sample size.

CONTROL, matched: the same pairs, our glosses shuffled among the tested
readings, 20 times.

CEILING: K&T's own glossed headwords standing in the same sentences,
measured the same way. A true word is not always echoed in a free
translation -- 'went across' for a verbal prefix -- so this is what a true
reading can be expected to reach.

BARS, declared before the run, not moved:

  A+B   >= 5 sigma over the shuffle and >= 70% of the ceiling
  C+D   >= 3 sigma
  G     reported

    python3 ktsentence.py
"""
import json
import random
import re
import sys
from collections import defaultdict

import ktcross as K
import ktdict
import ktrederive as R

NSHUF = 20
REF = re.compile(r"\d{3}[rv]\d{2}")
CIRC = re.compile(r"Kiraly|Király|K&T", re.I)


def hx(s):
    return "".join(f"{ord(c) - 0xE000:03x}" for c in s
                   if 0xE000 <= ord(c) <= 0xF8FF)


def sentences():
    raw = json.load(open(ktdict.DICT, encoding="utf-8"))
    out = []
    for e in raw:
        fr = e["entry"]
        for i, f in enumerate(fr[:-1]):
            if f.get("style") != "rohonc":
                continue
            codes = [hx(w) for w in f["text"].split()]
            codes = [c for c in codes if c]
            if len(codes) < 3:
                continue
            t = fr[i + 1].get("text", "")
            m = REF.search(t)
            if not m:
                continue
            eng = t[:m.start()]
            if not re.search(r"[a-zA-Z]{3,}", eng):
                continue
            out.append((hx(e["code"]), codes, eng.strip(), m.group(0)))
    return out


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    p = json.load(open('proposals.json', encoding='utf-8'))
    sents = sentences()
    print("TEST 5: OUR READINGS IN SENTENCES K&T TRANSLATED WHOLE")
    print(f"  sentences with a translation and a cite   {len(sents)}")

    ktst = {}
    for s, g in gl.items():
        st = set()
        for x in g:
            st |= R.stems(x)
        if st:
            ktst[hx(s)] = st
    ours, skipped = {}, 0
    for h, v in p.items():
        if h.startswith('_') or not isinstance(v, dict) or v.get('tier') not in 'ABCDG':
            continue
        if CIRC.search(v.get('evidence', '')):
            skipped += 1
            continue
        st = R.stems(v.get('gloss', ''))
        if st:
            ours[h] = (v['tier'], st)
    print(f"  our readings excluded as circular          {skipped}")

    kpairs, opairs = [], defaultdict(list)
    for head, codes, eng, ref in sents:
        est = R.stems(eng)
        if not est:
            continue
        for c in set(codes):
            if c in ktst and c != head:
                kpairs.append((ktst[c], est))
            if c in ours:
                opairs[ours[c][0]].append((c, ours[c][1], est))

    def rate(pairs):
        return sum(bool(a & b) for a, b in pairs), len(pairs)

    kh, kn = rate(kpairs)
    ceil = kh / kn if kn else 0
    print(f"  K&T ceiling   {kh}/{kn} pairs   {ceil*100:.1f}%")
    print()
    print(f"  {'tier':6s}{'signs':>6s}{'pairs':>7s}{'hit':>5s}{'rate':>8s}"
          f"{'shuffle':>9s}{'sd':>6s}{'sigma':>7s}{'vs ceiling':>12s}")
    rng = random.Random(R.SEED)
    res = {}
    for group, tiers in (('A+B', 'AB'), ('C+D', 'CD'), ('G', 'G')):
        rows = [r for t in tiers for r in opairs[t]]
        if not rows:
            print(f"  {group:6s}     0")
            continue
        hit, n = rate([(a, b) for _, a, b in rows])
        obs = hit / n
        # shuffle glosses among the distinct signs tested
        signs = sorted({c for c, _, _ in rows})
        gl_of = {c: a for c, a, _ in rows}
        nulls = []
        for _ in range(NSHUF):
            perm = signs[:]
            rng.shuffle(perm)
            m = dict(zip(signs, perm))
            h2, _ = rate([(gl_of[m[c]], b) for c, _, b in rows])
            nulls.append(h2 / n)
        mu = sum(nulls) / len(nulls)
        sd = (sum((x - mu) ** 2 for x in nulls) / (len(nulls) - 1)) ** .5
        sig = (obs - mu) / sd if sd else 0
        res[group] = (obs, sig, n)
        print(f"  {group:6s}{len(signs):6d}{n:7d}{hit:5d}{obs*100:7.1f}%"
              f"{mu*100:8.1f}%{sd*100:6.2f}{sig:7.1f}{obs/ceil*100 if ceil else 0:11.0f}%")
        miss = [(c, sorted(a)) for c, a, b in rows if not (a & b)]
        if miss and group != 'G':
            print("         misses: " + ", ".join(f"{c}({'/'.join(a)})" for c, a in miss)[:300])
    print()
    ok = True
    if 'A+B' in res:
        o, s, n = res['A+B']
        a = s >= 5 and o >= 0.7 * ceil
        print(f"  BAR A+B: >= 5 sigma and >= 70% of ceiling  ->  {'PASS' if a else 'FAIL'}")
        ok &= a
    if 'C+D' in res:
        c = res['C+D'][1] >= 3
        print(f"  BAR C+D: >= 3 sigma  ->  {'PASS' if c else 'FAIL'}")
        ok &= c
    return 0 if ok else 1


if __name__ == "__main__":
    import ktcwd
    ktcwd.enter()
    sys.exit(main(sys.argv[1:]))
