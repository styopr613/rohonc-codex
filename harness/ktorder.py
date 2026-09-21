"""TEST 6: do our readings put words in the RIGHT PLACE on folios that played
no part in choosing them?

Test 1 asks whether a gloss is present in the cited passage. That is weak
against one failure: a reading drawn from the right passage but put on the
wrong sign is still present. This test asks about ORDER. Render each cited
folio three ways -- K&T's dictionary only; K&T plus our tier A/B readings;
K&T plus the same readings with their glosses shuffled among the signs --
and score each rendering by the longest common subsequence of content stems
between the folio, line by line in order, and the cited passage, verse by
verse in order. A gloss on the right sign lengthens the match; the same
gloss on the wrong sign does not, even though it is the same word from the
same passage.

HELD OUT: a reading is applied to a folio only if that folio is not named in
the reading's evidence. What is measured is positional fit where nobody
looked.

  gain     LCS(K&T + ours) - LCS(K&T only), summed over cited folios
  control  LCS(K&T + shuffled ours) - LCS(K&T only), 20 shuffles

BAR, declared before the run: held-out gain beats the control mean by >= 5
sigma. The guesses are reported the same way but are NOT held out -- a guess
was made looking at its line and its passage -- so their figure is
descriptive, not a test.

    python3 ktorder.py
"""
import json
import random
import re
import sys
from collections import defaultdict

import ktaffix as A
import ktcross as K
import ktleft as L
import ktrederive as R
import kttranslate as T

NSHUF = 20
FOLIO = re.compile(r"\b(\d{3}[rv])\b")


def ordered_stems(text):
    g = re.sub(r"[<\[(][^>\])]*[>\])]", " ", text).translate(K.ACCENT)
    out = []
    for w in re.findall(r"[a-zA-Z]+", g):
        if w.lower() in K.STOP or len(w) < 3:
            continue
        out.append(K.stem(w))
    return out


def lcs(seq_sets, seq):
    n, m = len(seq_sets), len(seq)
    prev = [0] * (m + 1)
    for i in range(1, n + 1):
        cur = [0] * (m + 1)
        s = seq_sets[i - 1]
        for j in range(1, m + 1):
            if seq[j - 1] in s:
                cur[j] = prev[j - 1] + 1
            else:
                cur[j] = max(prev[j], cur[j - 1])
        prev = cur
    return prev[m]


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
                seq += ordered_stems(txt)
            if seq:
                passages[pgn] = seq

    def un(h):
        return "".join(chr(0xE000 + int(h[i:i + 3], 16)) for i in range(0, len(h), 3))

    ours = {}
    for h, v in p.items():
        if h.startswith('_') or not isinstance(v, dict):
            continue
        if v.get('tier') in ('A', 'B', 'G') and v.get('gloss'):
            ours[h] = (v['tier'], v['gloss'], set(FOLIO.findall(v.get('evidence', ''))))

    toks_of = {}
    for pg in doc:
        if pg.page in passages:
            toks_of.setdefault(pg.page, []).extend(
                [t for ln in pg.lines for run in ln for t in run])

    def render(pgn, propmap):
        return [R.stems(T.render_token(t, gl, seg, False, var, propmap))
                for t in toks_of[pgn]]

    base = {pgn: lcs(render(pgn, None), passages[pgn]) for pgn in toks_of}
    print("TEST 6: ORDER OF WORDS ON HELD-OUT FOLIOS")
    print(f"  cited folios {len(base)}   K&T-only LCS total {sum(base.values())}")

    def gain(tiers, held, glosses=None):
        tot = 0
        for pgn in toks_of:
            pm = {}
            for h, (tier, g, seen) in ours.items():
                if tier not in tiers or (held and pgn in seen):
                    continue
                pm[un(h)] = (glosses[h] if glosses else g, tier)
            tot += lcs(render(pgn, pm), passages[pgn]) - base[pgn]
        return tot

    rng = random.Random(R.SEED)
    for label, tiers, held in (("A+B, held out", "AB", True),
                               ("G, not held out", "G", False)):
        keys = [h for h in ours if ours[h][0] in tiers]
        obs = gain(tiers, held)
        nulls = []
        for _ in range(NSHUF):
            perm = keys[:]
            rng.shuffle(perm)
            nulls.append(gain(tiers, held, {h: ours[q][1] for h, q in zip(keys, perm)}))
        mu = sum(nulls) / len(nulls)
        sd = (sum((x - mu) ** 2 for x in nulls) / (len(nulls) - 1)) ** .5
        sig = (obs - mu) / sd if sd else 0
        print(f"  {label:18s} signs {len(keys):4d}   gain {obs:+5d}   "
              f"shuffled {mu:+7.1f} (sd {sd:.1f})   {sig:.1f} sigma")
        if held:
            print(f"  BAR: >= 5 sigma  ->  {'PASS' if sig >= 5 else 'FAIL'}")
            ok = sig >= 5
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
