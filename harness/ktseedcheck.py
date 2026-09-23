"""TEST 9: the hidden 70% validated against the random 30% seed.

Test 8 asked a machine to regrow the hidden words and it barely could. The
owner's correction: we already HAVE readings for the hidden 70%. The seed
should validate them. So: keep a random 30% of every readable sign, and for
each hidden sign ask whether the gloss we already hold for it fits the slot
the seed brackets -- between the nearest seed word before it in the cited
passage and the nearest after. The seed never saw the hidden gloss; the
hidden gloss never used the seed. Five random splits, so every sign is
hidden in some of them.

  fit      a stem of the hidden sign's gloss is in the bracketed window
  rate     fits / bracketed occurrences (occurrences with no seed anchor on
           the line are counted and set aside)

Scored separately for K&T's hidden signs and ours, against the SAME seed.
Theirs are the ceiling; ours should reach it.

CONTROL: the hidden glosses shuffled among the hidden signs, 5 times per
split. A true word in the right place fits its window; a true word on the
wrong sign does not.

BARS, declared before the run:
  ours A+B beat the shuffle by >= 5 sigma and reach >= 70% of K&T's rate
  ours C+D reported

    python3 ktseedcheck.py    [--splits 5] [--frac 0.3]
"""
import json
import random
import sys
from collections import Counter, defaultdict

import ktaffix as A
import ktcross as K
import ktleft as L
import ktrederive as R
import ktorder as O
from ktrecover import lcs_pairs

CAP = 3
NSHUF = 5


def main(argv):
    nsplit = int(argv[argv.index('--splits') + 1]) if '--splits' in argv else 5
    frac = float(argv[argv.index('--frac') + 1]) if '--frac' in argv else 0.30
    gl, doc, seg, var, prop, inv = K.build()
    p = json.load(open('proposals.json', encoding='utf-8'))
    vd = L.verses_dr()

    def un(h):
        return "".join(chr(0xE000 + int(h[i:i + 3], 16)) for i in range(0, len(h), 3))

    words, src = {}, {}
    for s, g in gl.items():
        st = set()
        for x in g:
            st |= R.stems(x)
        if st:
            words[s] = st; src[s] = 'K&T'
    for h, v in p.items():
        if not h.startswith('_') and isinstance(v, dict) and v.get('tier') in 'ABCD':
            st = R.stems(v.get('gloss', ''))
            if st and un(h) not in words:
                words[un(h)] = st; src[un(h)] = 'A+B' if v['tier'] in 'AB' else 'C+D'

    passages = {}
    for pgn in sorted({x.page for x in doc}):
        r = L.refs_in(K.note_for(pgn))
        if r:
            seq = []
            for k, txt in L.passage(vd, r):
                seq += O.ordered_stems(txt)
            if seq:
                passages[pgn] = seq
    lines_of, occ = defaultdict(list), defaultdict(list)
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

    signs = sorted(s for s in words if occ[s])
    rng = random.Random(R.SEED)

    def score(seed, glossmap):
        """{source: [fit, bracketed, unanchored]} for hidden signs under glossmap."""
        out = defaultdict(lambda: [0, 0, 0])
        for s in signs:
            if s in seed:
                continue
            for pgn, li, i in occ[s]:
                toks = lines_of[pgn][li]
                sets = [words[t] if (t in seed and k != i) else set() for k, t in enumerate(toks)]
                P = passages[pgn]
                m = lcs_pairs(sets, P)
                before = [m[k] for k in m if k < i]
                after = [m[k] for k in m if k > i]
                row = out[src[s]]
                if not before and not after:
                    row[2] += 1
                    continue
                lo = max(before) + 1 if before else 0
                hi = min(after) if after else len(P)
                row[1] += 1
                row[0] += bool(glossmap[s] & set(P[lo:hi]))
        return out

    tot = defaultdict(lambda: [0, 0, 0])
    nulls = defaultdict(list)
    for k in range(nsplit):
        order = signs[:]
        rng.shuffle(order)
        seed = set(order[:int(len(order) * frac)])
        hidden = [s for s in signs if s not in seed]
        real = score(seed, words)
        for g, row in real.items():
            for j in range(3):
                tot[g][j] += row[j]
        for _ in range(NSHUF):
            perm = hidden[:]
            rng.shuffle(perm)
            sm = dict(words)
            for a, b in zip(hidden, perm):
                sm[a] = words[b]
            sh = score(seed, sm)
            for g, row in sh.items():
                nulls[g].append(row[0] / row[1] if row[1] else 0)
    print(f"TEST 9: THE HIDDEN 70% VALIDATED AGAINST A RANDOM 30% SEED  "
          f"({nsplit} splits, {NSHUF} shuffles each)")
    print(f"  {'source':8s}{'bracketed':>11s}{'unanchored':>12s}{'fit':>8s}{'shuffle':>9s}{'sd':>6s}{'sigma':>7s}")
    rates = {}
    for g in ('K&T', 'A+B', 'C+D'):
        fit, br, un_ = tot[g]
        obs = fit / br if br else 0
        xs = nulls[g]
        mu = sum(xs) / len(xs)
        sd = (sum((x - mu) ** 2 for x in xs) / max(1, len(xs) - 1)) ** .5
        sig = (obs - mu) / sd if sd else 0
        rates[g] = (obs, sig)
        print(f"  {g:8s}{br:11d}{un_:12d}{obs*100:7.1f}%{mu*100:8.1f}%{sd*100:6.2f}{sig:7.1f}")
    ceil = rates['K&T'][0]
    o, s = rates['A+B']
    ok = s >= 5 and o >= 0.7 * ceil
    print(f"\n  ours A+B reach {o/ceil*100:.0f}% of K&T's own fit rate")
    print(f"  BAR A+B: >= 5 sigma and >= 70% of K&T  ->  {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    import ktcwd
    ktcwd.enter()
    sys.exit(main(sys.argv[1:]))
