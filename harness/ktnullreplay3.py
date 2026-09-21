"""TEST 10c: the search replayed on null books, at the scale the loop
actually worked -- the line and the verse it retells.

Tests 10 and 10b ran Grok's proxy at two scales and it had no power at
either: at the verse the notes cite it keeps 7 signs of 316 on the real
book and 6 on a null; at chapter scale it keeps 215 of 377 and more on
every null, and never once picks the stem this project picked. Neither is
the procedure METHOD.md describes, which was: render the line in K&T's
words, find the verse it retells, take the gap's word from that verse, and
check the word at every occurrence. This is that procedure as an
algorithm, written before the run:

  THE LINE RULE
  For every sign K&T did not read, at every line it stands on whose folio
  cites a chapter:
    anchors     the content stems of the OTHER tokens on the line that K&T
                read (their glosses and listed variants; nothing of ours,
                no segmentation);
    the verse   among all verses of the folio's cited chapter(s), Douay and
                King James together, the one holding the most anchor stems;
                the line is EVIDENCED only if that verse holds >= 2 of them;
    candidates  that verse's content stems, minus K&T's own stems, minus
                the anchors.
  Keep the sign if it has >= 3 evidenced lines on >= 2 distinct folios and
  some stem is a candidate at EVERY evidenced line. Reading = the rarest
  such stem, rarity over both Bibles.

  HELD-OUT SCORE
  For each kept-or-not sign with >= 3 evidenced lines, each line in turn:
  derive from the other lines; if a reading results it is a trial, a hit
  if the stem is a candidate at the held-out line. Control: derived stems
  permuted among the trials, 20 times.

NULL BOOKS, seeded:  global (tokens permuted across the book) and rotated
(cited folio i receives cited folio i+17's chapters), as in Tests 10/10b.

REPORTED, no bar: how many real-book kept readings this project also read,
and how many with the same stem.

BARS, the same as Test 10, declared before the run, not moved:
  FAIL if either null yields at least half as many kept readings as the
  real book, or if readings from either null beat their own shuffled
  glosses by >= 5 sigma held-out.

    python3 ktnullreplay3.py [--shuf N]
"""
import json
import random
import sys
from collections import defaultdict

import ktaffix as A
import ktcross as K
import ktleft as L
import kttestlib as TL

SEED = 20260921
OFFSET = 17
MIN_LINES = 3
MIN_ANCH = 2


def main(argv):
    nshuf = int(argv[argv.index('--shuf') + 1]) if '--shuf' in argv else 20
    gl, doc, seg, var, prop, inv = K.build()
    vv, vd = L.verses(), L.verses_dr()
    refs = TL.cited(doc)
    taken = TL.kt_taken(gl)
    freq = TL.corpus_freq(vv, vd)
    verses = defaultdict(dict)          # chapter -> {verse: stems}
    for t in (vv, vd):
        for (b, c, v), txt in t.items():
            verses[(b, c)][v] = verses[(b, c)].get(v, set()) | TL.content(txt)
    folio_ch = {f: sorted({(b, c) for b, c, _, _ in r if (b, c) in verses}) for f, r in refs.items()}
    folio_ch = {f: v for f, v in folio_ch.items() if v}
    ktst = {}
    for s, g in gl.items():
        st = set()
        for x in g:
            st |= TL.content(x)
        ktst[s] = st
    unread = lambda s: s not in gl and s not in var

    def stems_of(s):
        s = var.get(s, s)
        return ktst.get(s, set())

    # lines as lists of base signs, keyed by folio
    lines = defaultdict(list)
    for pg in doc:
        for ln in pg.lines:
            lines[pg.page].append([A.strip(t)[0] for run in ln for t in run])

    def evidence(lines_, fch):
        """{sign: [(folio, line no, candidate stems)]} for every evidenced line."""
        out = defaultdict(list)
        for f, lns in lines_.items():
            if f not in fch:
                continue
            vs = [st for ch in fch[f] for st in verses[ch].values()]
            for i, toks in enumerate(lns):
                targets = [k for k, s in enumerate(toks) if unread(s)]
                if not targets:
                    continue
                anchors = set()
                for k, s in enumerate(toks):
                    if not unread(s):
                        anchors |= stems_of(s)
                if len(anchors) < MIN_ANCH:
                    continue
                best = max(vs, key=lambda st: len(st & anchors))
                if len(best & anchors) < MIN_ANCH:
                    continue
                cand = frozenset(best - taken - anchors)
                for k in targets:
                    out[toks[k]].append((f, i, cand))
        return out

    def derive(rows):
        cand = None
        for _, _, c in rows:
            cand = set(c) if cand is None else cand & c
            if not cand:
                return None
        return min(cand, key=lambda s: (freq.get(s, 0), s))

    def replay(ev, rng):
        kept, trials, tested = {}, [], 0
        for s, rows in sorted(ev.items(), key=lambda kv: K.hx(kv[0])):
            if len(rows) < MIN_LINES or len({f for f, _, _ in rows}) < 2:
                continue
            tested += 1
            d = derive(rows)
            if d:
                kept[s] = d
            for j in range(len(rows)):
                d2 = derive(rows[:j] + rows[j + 1:])
                if d2:
                    trials.append((d2, rows[j][2]))
        n = len(trials)
        obs = sum(1 for d, c in trials if d in c) / n if n else 0
        stems = [d for d, _ in trials]
        nulls = []
        for _ in range(nshuf):
            p = stems[:]
            rng.shuffle(p)
            nulls.append(sum(1 for d, (_, c) in zip(p, trials) if d in c) / n if n else 0)
        m, sd, sig = TL.sigma(obs, nulls)
        return tested, kept, n, obs, m, sd, sig

    books = {'real': (lines, folio_ch)}
    r2 = random.Random(SEED + 2)
    order = sorted(lines)
    alltok = [s for f in order for ln in lines[f] for s in ln]
    r2.shuffle(alltok)
    lg, k = {}, 0
    for f in order:
        lg[f] = []
        for ln in lines[f]:
            lg[f].append(alltok[k:k + len(ln)])
            k += len(ln)
    books['global'] = (lg, folio_ch)
    cited = sorted(folio_ch)
    rot = {cited[i]: folio_ch[cited[(i + OFFSET) % len(cited)]] for i in range(len(cited))}
    books['rotated'] = (lines, rot)

    print("TEST 10c: THE LINE RULE REPLAYED ON NULL BOOKS")
    print(f"  cited folios {len(folio_ch)}; anchors >= {MIN_ANCH}; evidenced lines >= {MIN_LINES} "
          f"on >= 2 folios; offset {OFFSET}; seed {SEED}\n")
    print(f"  {'book':10s}{'evid.lines':>11s}{'signs':>7s}{'kept':>7s}{'trials':>8s}{'held-out':>10s}"
          f"{'shuffle':>9s}{'sd':>6s}{'sigma':>7s}")
    rng = random.Random(SEED)
    res = {}
    for name, (lns, fch) in books.items():
        ev = evidence(lns, fch)
        nl = sum(len(v) for v in ev.values())
        tested, kept, n, obs, m, sd, sig = replay(ev, rng)
        res[name] = (len(kept), sig, kept)
        print(f"  {name:10s}{nl:11d}{tested:7d}{len(kept):7d}{n:8d}{obs*100:9.1f}%{m*100:8.1f}%"
              f"{sd*100:6.2f}{sig:7.1f}")
    real = res['real'][0]
    p = json.load(open('proposals.json', encoding='utf-8'))
    un = lambda h: "".join(chr(0xE000 + int(h[i:i + 3], 16)) for i in range(0, len(h), 3))
    ours = {un(h): (v['tier'], v['gloss']) for h, v in p.items()
            if isinstance(v, dict) and v.get('tier') in 'ABCDG'}
    agree = tot = 0
    print()
    for s, d in sorted(res['real'][2].items(), key=lambda kv: K.hx(kv[0])):
        o = ours.get(s)
        same = bool(o) and d in TL.content(o[1].replace('_', ' '))
        tot += bool(o)
        agree += same
        print(f"    {K.hx(s):24s} rule: {d:14s} this project: "
              f"{(o[0] + ' ' + o[1]) if o else '-':30s} {'SAME' if same else ''}")
    print(f"\n  real-book kept readings this project also read: {tot} of {real}; same stem {agree}"
          f"  (reported, no bar)")
    print()
    ok = True
    for name in ('global', 'rotated'):
        kept, sig, _ = res[name]
        a = kept < 0.5 * real
        b = sig < 5
        print(f"  {name:9s} kept {kept} vs real {real}: {'under' if a else 'AT OR OVER'} half"
              f"   held-out {sig:.1f} sigma: {'under' if b else 'AT OR OVER'} 5")
        ok &= a and b
    print(f"  BAR: both nulls under half the real count and under 5 sigma  ->  "
          f"{'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
