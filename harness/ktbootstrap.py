"""TEST 8: from a random 30% of the words, can the rest be got back?

The owner's question, and the right one: if the reading is real, a seed of
it should grow. Take a random 30% of every readable sign -- K&T's and ours
together -- hide the other 70%, and see how much of the hidden 70% the
visible 30% can recover, mechanically, in two stages.

  STAGE 1  which passage is this folio? Render each cited folio with the
           seed words only. Score every passage any folio note cites (the
           candidate set) by how many of the folio's rendered stems it
           contains, per stem of the passage. Predict the best. Accuracy is
           the fraction of cited folios whose predicted passage is the one
           its note names. Control: the seed's glosses shuffled among the
           seed's signs. Chance is one in the number of candidates.

  STAGE 2  fill the holes. For every hidden sign, on up to three of its
           lines, bracket its slot in the passage between the nearest
           matched word before it and after it (the Test 7 method). Fill
           the narrowest windows first with the rarest candidate, make each
           filled sign an anchor, and go round again until nothing changes.
           Run once with the true passages (the fill step alone) and once
           with stage 1's predicted passages (end to end). A hidden sign is
           RECOVERED when the stem it was filled with is a stem of its true
           gloss. Control: the seed's glosses shuffled.

BARS, declared before the run:
  stage 1 accuracy beats the shuffled seed by >= 5 sigma
  stage 2 recovery, true passages, beats the shuffled seed by >= 5 sigma

Read the absolute numbers with this in mind: the filler here is a machine
that only knows "between these two words". Test 7 showed that machine finds
the word one time in nine even with the whole dictionary as anchors. A
person reading the line does far better, and that person is what made the
readings. These numbers are a floor, not the method.

    python3 ktbootstrap.py    [--seed N] [--frac 0.3] [--shuf 5]
"""
import json
import random
import sys
from collections import Counter, defaultdict

import ktaffix as A
import ktcross as K
import ktleft as L
import ktrederive as R
import kttranslate as T
import ktorder as O
from ktrecover import lcs_pairs

CAP = 3
MAXWIN = 12


def main(argv):
    seedn = int(argv[argv.index('--seed') + 1]) if '--seed' in argv else R.SEED
    frac = float(argv[argv.index('--frac') + 1]) if '--frac' in argv else 0.30
    nshuf = int(argv[argv.index('--shuf') + 1]) if '--shuf' in argv else 5
    gl, doc, seg, var, prop, inv = K.build()
    p = json.load(open('proposals.json', encoding='utf-8'))
    vd = L.verses_dr()

    def un(h):
        return "".join(chr(0xE000 + int(h[i:i + 3], 16)) for i in range(0, len(h), 3))

    # every readable sign -> its stems and a display gloss
    words = {}
    for s, g in gl.items():
        st = set()
        for x in g:
            st |= R.stems(x)
        if st:
            words[s] = (st, sorted(g)[0])
    for h, v in p.items():
        if not h.startswith('_') and isinstance(v, dict) and v.get('tier') in 'ABCD':
            st = R.stems(v.get('gloss', ''))
            if st:
                words.setdefault(un(h), (st, v['gloss']))

    # passages: per folio, and the candidate set
    passages, refs_of = {}, {}
    for pgn in sorted({x.page for x in doc}):
        r = L.refs_in(K.note_for(pgn))
        if r:
            seq = []
            for k, txt in L.passage(vd, r):
                seq += O.ordered_stems(txt)
            if seq:
                passages[pgn] = seq
                refs_of[pgn] = tuple(r)
    cands = {}
    for pgn, seq in passages.items():
        cands.setdefault(refs_of[pgn], (seq, set(seq)))
    cand_list = list(cands.items())
    rarity = Counter(s for seq, _ in cands.values() for s in set(seq))

    lines_of = defaultdict(list)     # folio -> [[tokens]]
    occ = defaultdict(list)          # sign -> [(pgn, li, idx)]
    for pg in doc:
        if pg.page not in passages:
            continue
        for ln in pg.lines:
            toks = [A.strip(t)[0] for run in ln for t in run]
            lines_of[pg.page].append(toks)
            li = len(lines_of[pg.page]) - 1
            for i, s in enumerate(toks):
                if s in words and len(occ[s]) < CAP:
                    occ[s].append((pg.page, li, i))

    signs = sorted(words)
    rng = random.Random(seedn)
    rng.shuffle(signs)
    nseed = int(len(signs) * frac)
    seed, hidden = set(signs[:nseed]), signs[nseed:]
    hidden = [s for s in hidden if occ[s]]
    ntok = sum(len(l) for ls in lines_of.values() for l in ls)
    seedtok = sum(1 for ls in lines_of.values() for l in ls for s in l if s in seed)
    print(f"TEST 8: BOOTSTRAP FROM A RANDOM {frac*100:.0f}% OF THE WORDS  (seed {seedn})")
    print(f"  readable signs {len(signs)}   seed {len(seed)}   hidden {len(hidden)} "
          f"with an occurrence on a cited folio")
    print(f"  seed covers {seedtok/ntok*100:.1f}% of the tokens on cited folios")

    def stage1(glossmap):
        right = 0
        for pgn, ls in lines_of.items():
            st = Counter()
            for l in ls:
                for s in l:
                    if s in glossmap:
                        st.update(glossmap[s])
            best, arg = -1, None
            for key, (seq, sset) in cand_list:
                sc = sum(c for x, c in st.items() if x in sset) / (len(sset) ** 0.5)
                if sc > best:
                    best, arg = sc, key
            right += arg == refs_of[pgn]
        return right / len(lines_of)

    def stage2(glossmap, use_true):
        anchors = dict(glossmap)
        filled = {}
        if not use_true:
            pred = {}
            for pgn, ls in lines_of.items():
                st = Counter()
                for l in ls:
                    for s in l:
                        if s in anchors:
                            st.update(anchors[s])
                best, arg = -1, None
                for key, (seq, sset) in cand_list:
                    sc = sum(c for x, c in st.items() if x in sset) / (len(sset) ** 0.5)
                    if sc > best:
                        best, arg = sc, key
                pred[pgn] = cands[arg][0]
        for _ in range(6):
            proposals = defaultdict(Counter)
            for s in hidden:
                if s in filled:
                    continue
                for pgn, li, i in occ[s]:
                    toks = lines_of[pgn][li]
                    sets = [anchors.get(t, set()) if k != i else set() for k, t in enumerate(toks)]
                    P = passages[pgn] if use_true else pred[pgn]
                    m = lcs_pairs(sets, P)
                    before = [m[k] for k in m if k < i]
                    after = [m[k] for k in m if k > i]
                    if not before and not after:
                        continue
                    lo = max(before) + 1 if before else 0
                    hi = min(after) if after else len(P)
                    win = P[lo:hi]
                    if 0 < len(win) <= MAXWIN:
                        proposals[s][min(win, key=lambda x: rarity[x])] += 1
            new = 0
            for s, c in proposals.items():
                stem, n = c.most_common(1)[0]
                filled[s] = stem
                anchors[s] = {stem}
                new += 1
            if not new:
                break
        rec = sum(1 for s, stem in filled.items() if stem in words[s][0])
        return rec / len(hidden), len(filled) / len(hidden)

    truthmap = {s: words[s][0] for s in seed}
    a1 = stage1(truthmap)
    r_true, f_true = stage2(truthmap, True)
    r_pred, f_pred = stage2(truthmap, False)
    n1, n2 = [], []
    seedl = sorted(seed)
    for _ in range(nshuf):
        perm = seedl[:]
        rng.shuffle(perm)
        sm = {s: words[q][0] for s, q in zip(seedl, perm)}
        n1.append(stage1(sm))
        n2.append(stage2(sm, True)[0])

    def stats(xs):
        m = sum(xs) / len(xs)
        return m, (sum((x - m) ** 2 for x in xs) / max(1, len(xs) - 1)) ** .5

    m1, s1 = stats(n1); m2, s2 = stats(n2)
    g1 = (a1 - m1) / s1 if s1 else 0
    g2 = (r_true - m2) / s2 if s2 else 0
    print(f"\n  STAGE 1  which passage is this folio      cited folios {len(lines_of)}   "
          f"candidates {len(cand_list)}  (chance {100/len(cand_list):.1f}%)")
    print(f"    seed words          {a1*100:5.1f}%")
    print(f"    seed shuffled       {m1*100:5.1f}%  (sd {s1*100:.2f})   {g1:.1f} sigma")
    print(f"    BAR: >= 5 sigma  ->  {'PASS' if g1 >= 5 else 'FAIL'}")
    print(f"\n  STAGE 2  the hidden {len(hidden)} signs filled from the slot the seed brackets")
    print(f"    true passages       filled {f_true*100:5.1f}%   recovered {r_true*100:5.1f}%")
    print(f"    predicted passages  filled {f_pred*100:5.1f}%   recovered {r_pred*100:5.1f}%")
    print(f"    seed shuffled       recovered {m2*100:5.1f}%  (sd {s2*100:.2f})   {g2:.1f} sigma")
    print(f"    BAR: >= 5 sigma  ->  {'PASS' if g2 >= 5 else 'FAIL'}")
    return 0 if g1 >= 5 and g2 >= 5 else 1


if __name__ == "__main__":
    import ktcwd
    ktcwd.enter()
    sys.exit(main(sys.argv[1:]))
