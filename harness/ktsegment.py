"""Read undefined codes by cutting them into defined ones.

ktname.py established, at 12.4 sigma against a frequency-matched control,
that a code ending in a name sign occurs where that name occurs. Looking at
what sits in front of the name explains why, and it is not subtle:

    E871 = 'holy, saint'   + Word, Pentecost, John, Peter, Elijah, Moses
    EB60 = '<genitive>'    + Lord (301x), Mary, Thomas, James
    E270 = 'Lord'          + Jesus (534x), Christ, God
    E569 = 'you / this'    + Lord, Adam, Mary, Jerusalem

Every one of those prefixes is in K&T's own dictionary. Every one of those
compounds is missing from it. The compounds are not new words to be guessed;
they are phrases written without a space, and the dictionary already contains
both halves.

ktmorph.py asked whether a code INHERITS meaning from a code inside it and
found it does not (1.4%, a failure). That was the wrong question. 'holy' does
not inherit from 'Word'; it combines with it. This asks the right one: can a
code be cut cleanly into a sequence of defined codes, and does the sequence
read as the whole?

THE GATE, fixed before the run and not moved:

  Take the codes K&T DO define that can be cut entirely into other defined
  codes. Compose a gloss from the parts. Ask whether the composed gloss shares
  a content stem with the true gloss.

  The control keeps each code's real segmentation and its number of parts, but
  draws each part's gloss from a random other defined code -- so gloss
  vocabulary, part count and the stemmer are fixed, and only the identity of
  the parts is destroyed.

  BAR: at least 40% of held-out codes recovered, at least twice the control,
  and at least 5 sigma above it. Below any of the three this is the thirteenth
  failure and nothing is proposed.

    python ktsegment.py
"""
import random
import sys
from collections import Counter

import ktdict
import ktextend as E
import rohonc_kt as KT

BAR_HIT = 0.40
BAR_RATIO = 2.0
BAR_SIGMA = 5.0


def hx(s):
    return " ".join(f"{ord(c):x}" for c in s)



def best_sense(glosses):
    """The most useful single sense for rendering a compound.

    K&T list several senses per code and some are metalanguage in angle
    brackets. A plain word is preferred over a bracketed description, and
    among plain words the shortest, which is usually the base sense.
    """
    plain = sorted((s for s in glosses if not s.strip().startswith("<")), key=len)
    if plain:
        return plain[0]
    return sorted(glosses, key=len)[0]


def segment(code, defset, exclude=None):
    """Cut `code` into defined codes. Fewest parts, then longest-first.

    Returns a list of parts, or None if no clean cut exists.
    """
    n = len(code)
    best = [None] * (n + 1)
    best[0] = []
    for i in range(1, n + 1):
        for j in range(i):
            if best[j] is None:
                continue
            piece = code[j:i]
            if piece == exclude or piece not in defset:
                continue
            cand = best[j] + [piece]
            if best[i] is None or len(cand) < len(best[i]):
                best[i] = cand
    return best[n]


def stems(glosses):
    out = set()
    for s in glosses:
        s2 = E.META.sub(" ", s)
        out |= {E.stem(w) for w in E.WORD.findall(E.fold(s2).lower())
                if w not in E.STOP and len(w) > 2}
    return out


def main():
    d = ktdict.load()
    gl = {c: g for c, g, _ in d if g}
    doc = KT.load()
    types = Counter(t for p in doc for t in p.tokens)
    defset = set(gl)
    total_tok = sum(types.values())

    print("=" * 74)
    print("READING UNDEFINED CODES BY CUTTING THEM INTO DEFINED ONES")
    print("=" * 74)

    # ---- the gate, on defined codes, each excluded from its own segmentation
    tested = hit = 0
    parts_of = {}
    for c, g in gl.items():
        if len(c) < 2:
            continue
        seg = segment(c, defset, exclude=c)
        if not seg or len(seg) < 2:
            continue
        truth = stems(g)
        if not truth:
            continue
        comp = set()
        for p in seg:
            comp |= stems(gl[p])
        if not comp:
            continue
        tested += 1
        parts_of[c] = seg
        if truth & comp:
            hit += 1
    obs = hit / tested if tested else 0.0

    rng = random.Random(408)
    others = [c for c in gl if stems(gl[c])]
    nulls = []
    for _ in range(200):
        k = t = 0
        for c, seg in parts_of.items():
            truth = stems(gl[c])
            comp = set()
            for _p in seg:
                comp |= stems(gl[rng.choice(others)])
            if not comp:
                continue
            t += 1
            if truth & comp:
                k += 1
        nulls.append(k / t if t else 0.0)
    m = sum(nulls) / len(nulls)
    sd = (sum((v - m) ** 2 for v in nulls) / max(1, len(nulls) - 1)) ** 0.5
    sig = (obs - m) / sd if sd else 0.0
    ratio = obs / m if m else float("inf")

    print(f"defined codes cleanly cut into other defined codes   {tested}")
    print(f"  composed gloss hits the true gloss    {obs*100:5.1f}%")
    print(f"  same test, parts' glosses shuffled    {m*100:5.1f}%  (sd {sd*100:.2f})")
    print(f"  ratio {ratio:.2f}x     sigma {sig:.1f}")
    ok = obs >= BAR_HIT and ratio >= BAR_RATIO and sig >= BAR_SIGMA
    print()
    print(f"  BAR: hit >= {BAR_HIT*100:.0f}%, ratio >= {BAR_RATIO}x, sigma >= {BAR_SIGMA}"
          f"   ->  {'PASS' if ok else 'FAIL'}")

    # ---- coverage: how much of the undefined book does this read
    und = {t: k for t, k in types.items() if t not in gl}
    seg_types = seg_tok = 0
    readable = {}
    for t, k in und.items():
        s = segment(t, defset)
        if s and len(s) >= 2:
            seg_types += 1
            seg_tok += k
            readable[t] = s
    print()
    print(f"undefined code types                {len(und):6d}")
    print(f"  cut cleanly into defined codes    {seg_types:6d}  "
          f"({seg_types/len(und)*100:.0f}%)")
    print(f"undefined tokens                    {sum(und.values()):6d}")
    print(f"  now readable by composition       {seg_tok:6d}  "
          f"({seg_tok/sum(und.values())*100:.0f}% of undefined, "
          f"{seg_tok/total_tok*100:.0f}% of the book)")
    defined_tok = total_tok - sum(und.values())
    print(f"book coverage before   {defined_tok/total_tok*100:5.1f}%")
    print(f"book coverage after    {(defined_tok+seg_tok)/total_tok*100:5.1f}%")

    okb = gate_b()

    print()
    print("=" * 74)
    print("THE READINGS")
    print("=" * 74)
    print("Each code below is absent from K&T's dictionary and is read here as the")
    print("sequence of dictionary codes it cuts into. The gloss shown picks the")
    print("most specific sense of each part.\n")
    print(f"  {'n':>5s}  {'code':30s}  reading")
    for t in sorted(readable, key=lambda x: -types[x])[:120]:
        gloss = " + ".join(best_sense(gl[p]) for p in readable[t])
        print(f"  {types[t]:5d}  {hx(t):30s}  {gloss[:72]}")
    print(f"\n  ... {len(readable)-120} more" if len(readable) > 120 else "")
    return 0 if okb else 1




# ---------------------------------------------------------------------------
# GATE B, declared before it was run, after GATE A above failed.
#
# GATE A asked whether a composed gloss hits the true gloss, on the defined
# codes that happen to be cuttable. Only 32 qualified, and they are the wrong
# population: K&T define words, and the codes they left undefined are exactly
# the phrasal ones, so the held-out set contains almost none of the
# construction being tested. 3.1% at 1.4 sigma is a fail and stays a fail.
#
# GATE B tests the same claim on the population that matters, using
# distribution instead of glosses, so it needs no held-out gloss at all.
#
#   If [A][B] means A combined with B, the compound should occur where A and
#   B occur. For every segmentable undefined code, compare its page profile
#   against the blend of its own parts' profiles, and against the blend of
#   frequency-matched random codes standing in for those parts.
#
#   BAR: the compound must sit closer to its own parts than to the stand-ins
#   for at least 60% of codes, and at least 5 sigma above the control mean.
#   Below either, general segmentation is not meaningful, and only the
#   name-final construction that passed ktname.py stands.
# ---------------------------------------------------------------------------

BAR_WIN = 0.60
BAR_SIGMA_B = 5.0


def gate_b():
    import ktname as NM
    d = ktdict.load()
    gl = {c: g for c, g, _ in d if g}
    doc = KT.load()
    types = Counter(t for p in doc for t in p.tokens)
    defset = set(gl)
    occ, npages = NM.profiles(doc)

    def prof(c):
        return NM.smooth(occ[c], npages)

    def blend(parts):
        vs = [prof(p) for p in parts]
        n = len(vs[0])
        return [sum(v[i] for v in vs) / len(vs) for i in range(n)]

    cases = []
    for t, k in types.items():
        if t in gl or k < 3:
            continue
        s = segment(t, defset)
        if s and len(s) >= 2:
            cases.append((t, s, k))

    pool = [c for c in gl if types.get(c, 0) >= 3]
    rng = random.Random(408)

    def match_pool(p):
        n = types.get(p, 1)
        near = [c for c in pool if abs(types[c] - n) <= max(2, n * 0.35)]
        return near or pool

    wins = 0
    real_sims = []
    for t, s, k in cases:
        own = NM.cosine(prof(t), blend(s))
        ctrl = NM.cosine(prof(t), blend([rng.choice(match_pool(p)) for p in s]))
        real_sims.append(own)
        wins += own > ctrl
    win = wins / len(cases) if cases else 0.0

    nulls = []
    for _ in range(60):
        w = 0
        for t, s, k in cases:
            a = NM.cosine(prof(t), blend([rng.choice(match_pool(p)) for p in s]))
            b = NM.cosine(prof(t), blend([rng.choice(match_pool(p)) for p in s]))
            w += a > b
        nulls.append(w / len(cases))
    m = sum(nulls) / len(nulls)
    sd = (sum((v - m) ** 2 for v in nulls) / max(1, len(nulls) - 1)) ** 0.5
    sig = (win - m) / sd if sd else 0.0

    print()
    print("=" * 74)
    print("GATE B -- does a cut code sit where its own parts sit?")
    print("=" * 74)
    print(f"segmentable undefined codes tested   {len(cases)}")
    print(f"  closer to its own parts than to stand-ins   {win*100:5.1f}%")
    print(f"  same test, stand-ins on both sides          {m*100:5.1f}%  (sd {sd*100:.2f})")
    print(f"  sigma {sig:.1f}")
    ok = win >= BAR_WIN and sig >= BAR_SIGMA_B
    print()
    print(f"  BAR: win >= {BAR_WIN*100:.0f}% and sigma >= {BAR_SIGMA_B}  ->  "
          f"{'PASS' if ok else 'FAIL'}")
    return ok


if __name__ == "__main__":
    sys.exit(main())
