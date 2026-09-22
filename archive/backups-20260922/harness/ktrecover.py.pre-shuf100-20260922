"""TEST 7: take K&T's words away. Does the text still read from ours alone,
and can ours give K&T's words back?

Part 1, coverage. Hide every one of K&T's 841 glosses and render the book
from this project's readings only. How much of it still reads.

Part 2, recovery. For each K&T headword that stands on a line whose folio
cites a passage: hide it, render the line with OUR readings only, align the
line to the cited passage by longest common subsequence, and take as
candidates the passage words that fall between the nearest matched word
before the hidden sign and the nearest after. Our readings are the anchors;
the hidden sign's slot is what they bracket. Then reveal K&T's gloss.

  presence   K&T's word is among the bracketed candidates
  top-1      the rarest bracketed candidate is K&T's word
  no anchor  nothing of ours on the line matched the passage; no candidates

CONDITIONS
  ours A+B      anchors are this project's tier A and B readings only
  ours A-D      tiers A to D
  K&T + ours    anchors are K&T's other words plus ours: the ceiling, what
                the same method does with the whole dictionary
  shuffled      ours A-D with the glosses shuffled among the signs, 10 times:
                anchors that are the right words in the wrong places

BARS, declared before the run:
  ours A-D presence beats shuffled by >= 5 sigma.
  Reported, no bar: presence and top-1 as a fraction of the ceiling.

Occurrences are capped at three lines per sign so the commonest signs do not
decide the number.

    python3 ktrecover.py
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
import kttranslate as T
import ktorder as O

NSHUF = 10
CAP = 3


def lcs_pairs(seq_sets, seq):
    n, m = len(seq_sets), len(seq)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        s = seq_sets[i - 1]
        for j in range(1, m + 1):
            dp[i][j] = dp[i - 1][j - 1] + 1 if seq[j - 1] in s else max(dp[i - 1][j], dp[i][j - 1])
    i, j, out = n, m, []
    while i and j:
        if seq[j - 1] in seq_sets[i - 1] and dp[i][j] == dp[i - 1][j - 1] + 1:
            out.append((i - 1, j - 1)); i -= 1; j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return dict(out[::-1])


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    p = json.load(open('proposals.json', encoding='utf-8'))
    vd = L.verses_dr()
    passages = {}
    for pgn in sorted({x.page for x in doc}):
        r = L.refs_in(K.note_for(pgn))
        if r:
            seq = []
            for k, txt in L.passage(vd, r):
                seq += O.ordered_stems(txt)
            if seq:
                passages[pgn] = seq
    rarity = Counter(s for seq in passages.values() for s in set(seq))

    def un(h):
        return "".join(chr(0xE000 + int(h[i:i + 3], 16)) for i in range(0, len(h), 3))

    ours = {}
    for h, v in p.items():
        if h.startswith('_') or not isinstance(v, dict):
            continue
        if v.get('tier') in 'ABCD' and v.get('gloss'):
            ours[h] = (v['tier'], v['gloss'])

    # ---- part 1: coverage from ours alone
    tot = read = 0
    lines = full = some = 0
    pm_all = {un(h): (g, t) for h, (t, g) in ours.items()}
    for pg in doc:
        for ln in pg.lines:
            toks = [t for run in ln for t in run]
            r = [T.render_token(t, {}, {}, False, {}, pm_all) for t in toks]
            got = [x for x in r if not x.startswith('[?]')]
            tot += len(toks); read += len(got)
            lines += 1; full += len(got) == len(toks); some += bool(got)
    print("TEST 7: WITHOUT K&T'S WORDS")
    print(f"  part 1, coverage from this project's readings alone (tiers A-D)")
    print(f"    words read        {read:6d} / {tot}   {read/tot*100:5.1f}%")
    print(f"    lines touched     {some:6d} / {lines}  {some/lines*100:5.1f}%")
    print(f"    lines fully read  {full:6d} / {lines}  {full/lines*100:5.1f}%")

    # ---- part 2: recovery
    ktst = {}
    for s, g in gl.items():
        st = set()
        for x in g:
            st |= R.stems(x)
        if st:
            ktst[s] = st
    cases = defaultdict(list)     # kt sign -> [(pgn, toks, idx)]
    for pg in doc:
        if pg.page not in passages:
            continue
        for ln in pg.lines:
            toks = [t for run in ln for t in run]
            for i, t in enumerate(toks):
                s = A.strip(t)[0]
                if s in ktst and len(cases[s]) < CAP:
                    cases[s].append((pg.page, toks, i))
    print(f"\n  part 2, recovering K&T's words from the slot our readings bracket")
    print(f"    K&T signs tested {len(cases)}   occurrences {sum(len(v) for v in cases.values())}")

    def run(anchor_prop, gl_use, seg_use, var_use, hide):
        pres = top = noanc = n = 0
        width = 0
        for s, occs in cases.items():
            truth = ktst[s]
            for pgn, toks, i in occs:
                g2, seg2, var2 = gl_use, seg_use, var_use
                if hide:
                    # hide the sign everywhere K&T's apparatus could give it back:
                    # its own entry, variant spellings that point to it, and
                    # segmentations of other tokens that contain it
                    g2 = dict(gl_use); g2.pop(s, None)
                    var2 = {k: v for k, v in var_use.items() if v != s}
                    seg2 = {k: v for k, v in seg_use.items() if s not in v}
                sets = []
                for k, t in enumerate(toks):
                    if k == i:
                        sets.append(set())
                    else:
                        sets.append(R.stems(T.render_token(t, g2, seg2, False, var2, anchor_prop)))
                P = passages[pgn]
                m = lcs_pairs(sets, P)
                before = [m[k] for k in m if k < i]
                after = [m[k] for k in m if k > i]
                n += 1
                if not before and not after:
                    noanc += 1
                    continue
                lo = max(before) + 1 if before else 0
                hi = min(after) if after else len(P)
                cand = P[lo:hi]
                width += len(cand)
                if truth & set(cand):
                    pres += 1
                    if cand and min(cand, key=lambda x: rarity[x]) in truth:
                        top += 1
        return pres, top, noanc, n, width

    def pm(tiers, glosses=None):
        return {un(h): ((glosses[h] if glosses else g), t)
                for h, (t, g) in ours.items() if t in tiers}

    rows = {}
    rows['ours A+B'] = run(pm('AB'), {}, {}, {}, False)
    rows['ours A-D'] = run(pm('ABCD'), {}, {}, {}, False)
    rows['K&T + ours'] = run(pm('ABCD'), gl, seg, var, True)
    rng = random.Random(R.SEED)
    keys = sorted(ours)
    nulls = []
    for _ in range(NSHUF):
        perm = keys[:]
        rng.shuffle(perm)
        nulls.append(run(pm('ABCD', {h: ours[q][1] for h, q in zip(keys, perm)}), {}, {}, {}, False))
    print(f"\n    {'condition':12s}{'presence':>10s}{'top-1':>8s}{'no anchor':>11s}{'window':>8s}")
    for name, (pres, top, noanc, n, width) in rows.items():
        print(f"    {name:12s}{pres/n*100:9.1f}%{top/n*100:7.1f}%{noanc/n*100:10.1f}%"
              f"{width/max(1,n-noanc):8.1f}")
    ps = [x[0] / x[3] for x in nulls]
    mu = sum(ps) / len(ps); sd = (sum((x - mu) ** 2 for x in ps) / (len(ps) - 1)) ** .5
    tops = sum(x[1] / x[3] for x in nulls) / len(nulls)
    print(f"    {'shuffled':12s}{mu*100:9.1f}%{tops*100:7.1f}%   (sd {sd*100:.2f}, {NSHUF} shuffles)")
    obs = rows['ours A-D'][0] / rows['ours A-D'][3]
    sig = (obs - mu) / sd if sd else 0
    ceil = rows['K&T + ours'][0] / rows['K&T + ours'][3]
    print(f"\n    ours A-D presence {obs*100:.1f}% vs shuffled {mu*100:.1f}%   {sig:.1f} sigma")
    print(f"    ours A-D reaches {obs/ceil*100:.0f}% of what the whole dictionary reaches "
          f"({ceil*100:.1f}%)")
    print(f"    BAR: >= 5 sigma  ->  {'PASS' if sig >= 5 else 'FAIL'}")
    return 0 if sig >= 5 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
