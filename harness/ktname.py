"""Do codes that END in a name sign refer to that name?

The eleven attempts before this one treated a code as an atom: an opaque
symbol with a meaning to be guessed. But K&T's 2022 paper describes a grammar
in which the codex does not inflect. Instead of a pronoun or a conjugated
verb, "the sign of the subject's name consistently stands" -- and they print
one line of folio 137v as `... bun nelkul Jezus fogan te-Maria`, where
"te-Maria" (you-Mary) is written as one code.

That code is E569 E607. E569 alone is in their dictionary as the 2nd person
singular pronoun, 932 occurrences. E607 alone is Mary. So the compound is
pronoun + name, exactly the construction they describe.

The construction is not rare. Name signs are the most productive final
elements in the book:

    Lord   577 alone   1038 inside longer codes
    Jesus   89 alone    558
    Mary    59 alone    137
    Christ  52 alone    111
    Satan  156 alone    100

Nearly every one of those compounds is undefined. If the final sign really
carries the name, a large block of the undefined vocabulary becomes readable
as <modifier> + <person> in one step, and the job shrinks to the modifiers.

It might not. A code could end in the Mary glyph the way "Sunday" ends in
"day" -- or the way English "carpet" contains "car", which is what the
substring test in ktmorph.py found for codes in general: 1.4% inherit
meaning, barely above a shuffled control, a failure.

So this asks the narrower question on evidence that does not come from K&T.

THE GATE, fixed before the run and not moved:

  A compound's PAGE PROFILE is where in the book it occurs. If [X][N] refers
  to N, it should occur where N occurs. For every compound of five or more
  occurrences, rank all candidate name signs by how well their own page
  profile matches the compound's, and record the rank of the name the
  compound actually ends in.

  The control is the same test run on codes matched on frequency that do NOT
  end in a name sign, each assigned the name its partner compound had. That
  holds the book's topical structure, the profile measure and the frequency
  fixed, and destroys only the containment.

  BAR: the true name must come first for at least 40% of compounds, at least
  twice the control rate, and at least 5 sigma above it. Below any of the
  three, the construction is not referential, nothing is proposed, and this
  is recorded as the twelfth failure.

    python ktname.py
"""
import random
import re
import sys
from collections import Counter, defaultdict

import ktdict
import rohonc_kt as KT

BAR_TOP1 = 0.40
BAR_RATIO = 2.0
BAR_SIGMA = 5.0
MIN_OCC = 5


def hx(s):
    return " ".join(f"{ord(c):x}" for c in s)


def name_signs(gl):
    """Codes whose gloss is a capitalised proper noun."""
    out = {}
    for c, g in gl.items():
        caps = [s for s in g
                if re.fullmatch(r"[A-Z][A-Za-zÀ-ɏ]+(?: <[^>]*>)?", s.strip())]
        if caps:
            out[c] = sorted(caps)[0].split(" <")[0]
    return out


def profiles(doc):
    """page index per token occurrence"""
    pages = [p.page for p in doc]
    idx = {pg: i for i, pg in enumerate(pages)}
    occ = defaultdict(Counter)
    for p in doc:
        for t in p.tokens:
            occ[t][idx[p.page]] += 1
    return occ, len(pages)


def smooth(c, n, band=8):
    """coarse profile: counts in bands of `band` pages, L1-normalised"""
    v = [0.0] * (n // band + 1)
    for i, k in c.items():
        v[i // band] += k
    s = sum(v)
    return [x / s for x in v] if s else v


def cosine(a, b):
    num = sum(x * y for x, y in zip(a, b))
    da = sum(x * x for x in a) ** 0.5
    db = sum(y * y for y in b) ** 0.5
    return num / (da * db) if da and db else 0.0


def main():
    d = ktdict.load()
    gl = {c: g for c, g, _ in d if g}
    doc = KT.load()
    types = Counter(t for p in doc for t in p.tokens)
    occ, npages = profiles(doc)

    NAMES = name_signs(gl)
    # candidate names must be frequent enough alone to have a usable profile
    cands = [n for n in NAMES if types.get(n, 0) >= 10]
    nprof = {n: smooth(occ[n], npages) for n in cands}

    compounds = []
    for t, k in types.items():
        if k < MIN_OCC or t in gl:
            continue
        for n in cands:
            if len(t) > len(n) and t.endswith(n):
                compounds.append((t, n, k))
                break

    print("=" * 74)
    print("DO CODES ENDING IN A NAME SIGN REFER TO THAT NAME?")
    print("=" * 74)
    print(f"candidate name signs            {len(cands)}")
    print(f"undefined compounds, {MIN_OCC}+ occurrences   {len(compounds)}")

    def rank_of(prof, truth):
        sims = sorted(((cosine(prof, nprof[n]), n) for n in cands), reverse=True)
        for i, (_, n) in enumerate(sims, 1):
            if n == truth:
                return i, sims[0][1]
        return None, sims[0][1]

    real_top1 = 0
    rows = []
    for t, n, k in compounds:
        r, best = rank_of(smooth(occ[t], npages), n)
        real_top1 += (r == 1)
        rows.append((k, t, n, r, best))
    obs = real_top1 / len(compounds) if compounds else 0.0

    # control: frequency-matched codes that do not end in any name sign
    pool = [t for t, k in types.items()
            if k >= MIN_OCC and not any(len(t) > len(n) and t.endswith(n) for n in cands)]
    rng = random.Random(408)
    nulls = []
    for _ in range(200):
        hit = 0
        for t, n, k in compounds:
            near = [x for x in pool if abs(types[x] - k) <= max(2, k * 0.35)] or pool
            c = rng.choice(near)
            r, _ = rank_of(smooth(occ[c], npages), n)
            hit += (r == 1)
        nulls.append(hit / len(compounds))
    m = sum(nulls) / len(nulls)
    sd = (sum((v - m) ** 2 for v in nulls) / max(1, len(nulls) - 1)) ** 0.5
    sig = (obs - m) / sd if sd else 0.0
    ratio = obs / m if m else float("inf")

    print()
    print(f"  true name ranked first, real compounds   {obs*100:5.1f}%")
    print(f"  true name ranked first, matched control  {m*100:5.1f}%  (sd {sd*100:.2f})")
    print(f"  ratio {ratio:.2f}x      sigma {sig:.1f}")
    ok = obs >= BAR_TOP1 and ratio >= BAR_RATIO and sig >= BAR_SIGMA
    print()
    print(f"  BAR: top-1 >= {BAR_TOP1*100:.0f}%, ratio >= {BAR_RATIO}x, sigma >= {BAR_SIGMA}"
          f"   ->  {'PASS' if ok else 'FAIL'}")

    print("\nthe compounds, most frequent first:")
    print(f"  {'n':>4s}  {'code':34s} {'ends in':10s} {'rank':>4s}  best match")
    for k, t, n, r, best in sorted(rows, reverse=True)[:25]:
        print(f"  {k:4d}  {hx(t):34s} {NAMES[n]:10s} {str(r):>4s}  {NAMES[best]}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
