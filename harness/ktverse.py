"""Finding the lines that are certainly right, and solving backwards from them.

The translation in work/rohonc/translation/ identifies passage after passage
with a named chapter and verse -- over the brook Cedron, a stone's cast, the
sweat, "Whom seek ye", the earth quaking and the rocks splitting. If those
identifications are real then the source text is KNOWN PLAINTEXT sitting
beside unknown ciphertext, which is the position every classical decipherment
works from.

But an identification I made by reading is worth nothing as evidence for
itself. So this does not use my list. It scores EVERY line of the codex
against the whole reference corpus -- the Bible, the apocryphal infancy and
Nicodemus gospels, the four English mystery cycles, Caxton's Golden Legend,
1,746,498 words -- and lets the strongest matches name themselves. Those are
the anchors: the parts the book itself says are right.

Then the anchors are made to prove they carry information, by a test with a
known answer.

THE GATE, fixed before the run and not moved.

  ANCHORS are the top 5% of lines by match score. That is a rank rule, not a
  threshold I can tune after seeing the numbers.

  For each anchor line, hide one defined code at a time. Find the best window
  again using ONLY THE REMAINING codes, so the hidden word plays no part in
  locating the passage. Then ask whether the hidden code's gloss appears in
  the window that was found.

  The control asks the same question of a random window of the same corpus,
  which fixes the gloss, the stemmer and the corpus and destroys only the
  localisation.

  BAR: recovery at least 40%, at least twice the control, and at least
  5 sigma above it.

  Below any of the three, a located passage does not predict its own words,
  no undefined code is read from one, and the anchors stand only as evidence
  about what the book is, not as a way into its vocabulary.

    python ktverse.py
"""
import math
import os
import random
import sys
from collections import Counter, defaultdict

import corpus
import ktdict
import ktextend as E
import ktsegment as S
import rohonc_kt as KT

REF = os.path.join(corpus.DATA, "ref", "rohonc", "ALL.txt")
WIN = 30              # words per window
STRIDE = 10
DF_MAX = 4000         # a stem in more windows than this carries no location
ANCHOR_PCT = 0.05     # top 5% of lines by score are the anchors
BAR_HIT = 0.40
BAR_RATIO = 2.0
BAR_SIGMA = 5.0


def load_windows():
    txt = E.fold(open(REF, encoding="utf-8", errors="replace").read().lower())
    ws = [E.stem(w) for w in E.WORD.findall(txt)]
    wins = []
    for i in range(0, len(ws) - WIN, STRIDE):
        wins.append(frozenset(w for w in ws[i:i + WIN]
                              if w not in E.STOP and len(w) > 2))
    return wins, ws


def build_index(wins):
    df = Counter()
    for w in wins:
        df.update(w)
    idf = {}
    index = defaultdict(list)
    n = len(wins)
    for s, c in df.items():
        if c > DF_MAX:
            continue
        idf[s] = math.log(n / c)
    for k, w in enumerate(wins):
        for s in w:
            if s in idf:
                index[s].append(k)
    return index, idf


def best(query, index, idf):
    """(score, window id, margin) for the highest idf-weighted overlap."""
    acc = defaultdict(float)
    for s in query:
        w = idf.get(s)
        if w is None:
            continue
        for k in index[s]:
            acc[k] += w
    if not acc:
        return 0.0, -1, 0.0
    ranked = sorted(acc.items(), key=lambda x: -x[1])
    s1 = ranked[0][1]
    s2 = ranked[1][1] if len(ranked) > 1 else 0.0
    return s1, ranked[0][0], s1 - s2


def line_stems(toks, gl, seg, skip=None):
    """Content stems of the readable codes on a line, one code optionally hidden."""
    out = set()
    for t in toks:
        if t == skip:
            continue
        parts = [t] if t in gl else seg.get(t, [])
        for p in parts:
            if p in gl:
                out |= S.stems(gl[p])
    return out


def main():
    d = ktdict.load()
    gl = {c: g for c, g, _ in d if g}
    doc = KT.load()
    defset = set(gl)
    seg = {}
    for t in {t for p in doc for t in p.tokens}:
        if t not in gl:
            s = S.segment(t, defset)
            if s and len(s) >= 2:
                seg[t] = s

    print("=" * 76)
    print("ANCHORS: THE LINES THAT MATCH A KNOWN PASSAGE")
    print("=" * 76)
    wins, ws = load_windows()
    index, idf = build_index(wins)
    print(f"reference corpus {len(ws)} words, {len(wins)} windows of {WIN}, "
          f"{len(idf)} located stems")

    lines = []
    for p in doc:
        for i, ln in enumerate(p.lines, 1):
            toks = [t for run in ln for t in run]
            if toks:
                lines.append((p.page, i, toks))

    scored = []
    for page, i, toks in lines:
        q = line_stems(toks, gl, seg)
        if len(q) < 3:
            continue
        s, k, marg = best(q, index, idf)
        scored.append((s, marg, page, i, toks, k, q))
    scored.sort(key=lambda x: -x[0])
    n_anchor = max(1, int(len(scored) * ANCHOR_PCT))
    anchors = scored[:n_anchor]
    print(f"lines with 3+ readable content stems   {len(scored)} of {len(lines)}")
    print(f"anchors (top {ANCHOR_PCT*100:.0f}% by score)             {len(anchors)}")
    print(f"  score range  {anchors[-1][0]:.1f} .. {anchors[0][0]:.1f}"
          f"   (all lines median {scored[len(scored)//2][0]:.1f})")

    def show(k):
        i = k * STRIDE
        return " ".join(ws[i:i + WIN])

    print("\n  the ten strongest, with the passage they land on:")
    for s, marg, page, i, toks, k, q in anchors[:10]:
        print(f"\n   {page}:{i:<3d} score {s:6.1f}")
        print(f"     codex   {' '.join(S.best_sense(gl[t]) if t in gl else ('-'.join(S.best_sense(gl[x]) for x in seg[t]) if t in seg else '[?]') for t in toks)[:150]}")
        print(f"     source  {show(k)[:150]}")

    # ---------------- the gate
    rng = random.Random(408)
    tested = hit = 0
    ctrl_hit = 0
    per_case = []
    for s, marg, page, i, toks, k, q in anchors:
        for t in set(toks):
            if t not in gl:
                continue
            truth = S.stems(gl[t])
            if not truth:
                continue
            rest = line_stems(toks, gl, seg, skip=t)
            if len(rest) < 3:
                continue
            s2, k2, _ = best(rest, index, idf)
            if k2 < 0:
                continue
            tested += 1
            got = bool(truth & wins[k2])
            hit += got
            per_case.append((truth, got))
    obs = hit / tested if tested else 0.0

    nulls = []
    for _ in range(200):
        c = 0
        for truth, _got in per_case:
            c += bool(truth & wins[rng.randrange(len(wins))])
        nulls.append(c / len(per_case) if per_case else 0.0)
    m = sum(nulls) / len(nulls)
    sd = (sum((v - m) ** 2 for v in nulls) / max(1, len(nulls) - 1)) ** 0.5
    sig = (obs - m) / sd if sd else 0.0
    ratio = obs / m if m else float("inf")

    print()
    print("=" * 76)
    print("THE GATE -- can a located passage recover a word hidden from it?")
    print("=" * 76)
    print(f"  held-out codes tested                    {tested}")
    print(f"  gloss found in the relocated window      {obs*100:5.1f}%")
    print(f"  same test against a random window        {m*100:5.1f}%  (sd {sd*100:.2f})")
    print(f"  ratio {ratio:.2f}x     sigma {sig:.1f}")
    ok = obs >= BAR_HIT and ratio >= BAR_RATIO and sig >= BAR_SIGMA
    print()
    print(f"  BAR: hit >= {BAR_HIT*100:.0f}%, ratio >= {BAR_RATIO}x, "
          f"sigma >= {BAR_SIGMA}  ->  {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
