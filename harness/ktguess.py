"""Guess the unread words, and MEASURE how often a guess of this kind is right.

The question this answers is the one that matters before any mass guessing
is done: on a folio whose source passage is known, how often does the best
candidate turn out to be the true word? Not an opinion about it -- a number,
got by hiding words the project already knows and seeing whether they come
back.

THE TEST, declared before the run.

  Leave-one-out over every word that is ALREADY READ and stands on a folio
  whose translation note cites a chapter and verse. For each such word:

    1. hide it -- take its sign out of the inventory AND take its own gloss
       out of the taken-word index, so nothing about it is visible;
    2. rebuild the folio's candidate pool from the Douay-Rheims (the source
       tradition the book's author had) and the King James, minus every word
       still spoken for by some other sign;
    3. rank the candidates: rarer words in the passage first, since a common
       word is likelier to be somewhere else in the dictionary already;
    4. score a hit if the hidden word's own gloss is the top candidate, and
       separately if it is anywhere in the top three.

  Only words whose true gloss is IN the passage at all can be recovered, so
  two rates are reported and both matter: the rate over every hidden word
  (what mass guessing would actually achieve) and the rate over the subset
  whose answer was present to be found (how good the ranking is once the
  answer is there).

  No bar gates the work -- the user has asked for every line rendered either
  way. The measured rate is what the guess tag has to carry, so that a
  reader knows exactly how much a marked guess is worth.

    python ktguess.py --test        # the leave-one-out measurement
    python ktguess.py --test 300    # a faster sample of 300
    python ktguess.py PAGE          # candidates for that folio's holes
"""
import os
import random
import re
import sys
from collections import Counter, defaultdict

import ktaffix as A
import ktcross as K
import ktleft as L
import kttranslate as T

SEED = 20260921


def stem_of(gloss):
    """The content stems a K&T gloss contains."""
    g = re.sub(r"[<\[(][^>\])]*[>\])]", " ", gloss).translate(K.ACCENT)
    out = set()
    for w in re.findall(r"[a-zA-Z]+", g):
        if w.lower() in K.STOP or len(w) < 3:
            continue
        out.add(K.stem(w))
    return out


def rank(pool, work_freq):
    """Candidates, rarest-in-the-passage first.

    A word that is common across the whole source corpus is more likely to
    be carried by some sign already, and the pool has only removed the ones
    this project can see. Ranking by rarity puts the distinctive words of
    the passage first, which is where an unread sign is likeliest to sit.
    """
    return sorted(pool, key=lambda s: (work_freq.get(s, 0), s))


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    vv, vd = L.verses(), L.verses_dr()
    cited = {}
    for p in sorted({p.page for p in doc}):
        r = L.refs_in(K.note_for(p))
        if r:
            cited[p] = r

    freq = Counter()
    for t in (vv, vd):
        for txt in t.values():
            freq.update(K.stem(w.lower()) for w in re.findall(r"[A-Za-z]+", txt))

    if "--test" not in argv:
        want = [a for a in argv if re.fullmatch(r"\d{3}[rv]", a)]
        idx = K.taken_index(gl, prop)
        for pg in want:
            if pg not in cited:
                print(f"\n=== {pg}: no chapter and verse cited, no pool")
                continue
            both, dro, kjo, syn = L.pools_for(vv, vd, cited[pg], idx, 0)
            cand = rank({**both, **dro}, freq)
            print(f"\n=== {pg}  {len(cand)} candidates, rarest first")
            print("    " + ", ".join("/".join(sorted({**both, **dro}[s])) for s in cand))
            for p in doc:
                if p.page != pg:
                    continue
                for i, ln in enumerate(p.lines, 1):
                    tk = [t for run in ln for t in run]
                    miss = [A.strip(t)[0] for t in tk if A.strip(t)[0] not in inv]
                    if not miss:
                        continue
                    s = " ".join(("<<%s>>" % K.hx(A.strip(t)[0]))
                                 if A.strip(t)[0] in miss
                                 else T.render_token(t, gl, seg, False, var, prop)
                                 for t in tk)
                    print(f"  {pg}:{i:<3d} {s[:150]}")
        return 0

    # ---- leave-one-out
    # Strip --wide N from the argument list BEFORE looking for a sample size:
    # the first version read the N of "--wide 3" as "test 3 words", so the
    # widened runs reported on three trials and looked like a total collapse.
    argv = list(argv)
    wide = 0
    if "--wide" in argv:
        i = argv.index("--wide")
        wide = int(argv[i + 1])
        del argv[i:i + 2]
    n_sample = next((int(a) for a in argv if a.isdigit()), 0)
    known = {}
    for c, senses in gl.items():
        st = set()
        for g in senses:
            st |= stem_of(g)
        if st:
            known[c] = st
    for c, (g, tier) in prop.items():
        st = stem_of(g.replace("_", " "))
        if st:
            known[c] = st

    # --rare restricts the trial set to words as rare as the ones actually
    # left unread: the remaining holes are not random words, they are words
    # that occur once or twice, so testing on "Lord" and "say" understates
    # what guessing could do on the real population. Declared before the run.
    rare_only = "--rare" in argv
    occ = Counter(A.strip(t)[0] for p in doc for t in p.tokens)
    trials = []
    for p in doc:
        if p.page not in cited:
            continue
        for ln in p.lines:
            for t in [x for run in ln for x in run]:
                b = A.strip(t)[0]
                if b in known and (not rare_only or occ[b] <= 3):
                    trials.append((p.page, b))
    trials = sorted(set(trials))
    random.Random(SEED).shuffle(trials)
    if n_sample:
        trials = trials[:n_sample]

    base_idx = K.taken_index(gl, prop)
    # which signs put each stem into the index, so one sign can be withdrawn
    owners = defaultdict(set)
    for st, hits in base_idx.items():
        for sign, _ in hits:
            owners[st].add(sign)

    top1 = top3 = present = present_top1 = present_top3 = 0
    pools_cache = {}
    for pg, sign in trials:
        h = K.hx(sign)
        truth = known[sign]
        idx = {st: v for st, v in base_idx.items()
               if not (st in truth and owners[st] <= {h})}
        key = (pg, frozenset(st for st in truth if st not in idx))
        if key not in pools_cache:
            both, dro, kjo, syn = L.pools_for(vv, vd, cited[pg], idx, wide)
            pools_cache[key] = rank({**both, **dro}, freq)
        cand = pools_cache[key]
        if not cand:
            continue
        hit_any = [i for i, s in enumerate(cand) if s in truth]
        if hit_any:
            present += 1
            if hit_any[0] == 0:
                present_top1 += 1
                top1 += 1
            if hit_any[0] < 3:
                present_top3 += 1
                top3 += 1

    n = len(trials)
    print("LEAVE-ONE-OUT: can the guess procedure recover words the book already reads?")
    print(f"  trial set: {'rare words only (<=3 occurrences)' if rare_only else 'every read word'}, passage widened by {wide}")
    print(f"  hidden words tested                      {n}")
    print(f"  answer was present in the passage pool   {present}  ({present/n*100:.1f}%)")
    print()
    print(f"  top candidate correct, over ALL trials   {top1}  ({top1/n*100:.1f}%)")
    print(f"  in top three, over ALL trials            {top3}  ({top3/n*100:.1f}%)")
    print()
    print(f"  top candidate correct, when present      {present_top1}  "
          f"({present_top1/max(present,1)*100:.1f}%)")
    print(f"  in top three, when present               {present_top3}  "
          f"({present_top3/max(present,1)*100:.1f}%)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
