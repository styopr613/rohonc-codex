"""Are Rohonc codes built out of smaller codes, and does the meaning follow?

Ten previous attempts treated every code as an opaque atom: a symbol with a
meaning to be guessed. But K&T's codes are sequences of glyphs, and 84% of the
4,247 undefined codes contain a shorter *defined* code as a contiguous
substring -- 35% of the book by tokens. Nobody has asked whether that
containment carries meaning.

It might not. English "carpet" contains "car". If Rohonc codes are arbitrary
word-signs whose glyph strings happen to overlap, the containment is noise and
this line is dead. So the question is settled on the codes K&T already define,
where both the container and the part have a published gloss and the answer is
checkable.

THE GATE, fixed before the run and not moved:

  For every defined code X that contains a defined code Y as a proper
  contiguous substring, take the longest such Y. Ask whether gloss(X) and
  gloss(Y) share a content stem.

  The control keeps the identical structural pairs but replaces Y's gloss with
  the gloss of a random other defined code, so vocabulary, gloss length and
  the stemmer are all held fixed and only the pairing is destroyed.

  BAR: the real share must be at least TWICE the control's and at least 5
  sigma above it. Below either, composition is not semantic, nothing is
  proposed, and the attempt is recorded as a failure like the others.

    python ktmorph.py
"""
import random
import sys
from collections import Counter, defaultdict

import ktdict
import ktextend as E
import rohonc_kt as KT

BAR_RATIO = 2.0
BAR_SIGMA = 5.0


def stems(glosses):
    """Content stems of a K&T gloss set, metalanguage stripped."""
    out = set()
    for s in glosses:
        s2 = E.META.sub(" ", s)
        out |= {E.stem(w) for w in E.WORD.findall(E.fold(s2).lower())
                if w not in E.STOP and len(w) > 2}
    return out


def longest_part(code, defset):
    """Longest defined code that is a proper contiguous substring of `code`."""
    for L in range(len(code) - 1, 0, -1):
        for i in range(len(code) - L + 1):
            sub = code[i:i + L]
            if sub in defset:
                return sub, i, L
    return None


def main():
    d = ktdict.load()
    gl = {c: g for c, g, _ in d if g}
    doc = KT.load()
    types = Counter(t for p in doc for t in p.tokens)
    defset = set(gl)

    pairs = []
    for x in gl:
        if len(x) < 2:
            continue
        r = longest_part(x, defset)
        if r:
            y, i, L = r
            pairs.append((x, y, i, L))

    print("=" * 74)
    print("DO CODES INHERIT MEANING FROM THE CODES INSIDE THEM?")
    print("=" * 74)
    print(f"defined codes            {len(gl)}")
    print(f"  of these, containing a shorter defined code   {len(pairs)}")

    real = 0
    tested = 0
    hits = []
    for x, y, i, L in pairs:
        sx, sy = stems(gl[x]), stems(gl[y])
        if not sx or not sy:
            continue
        tested += 1
        if sx & sy:
            real += 1
            hits.append((x, y, i, L, sorted(sx & sy)[:3]))

    rng = random.Random(408)
    others = [c for c in gl if stems(gl[c])]
    nulls = []
    for _ in range(200):
        k = 0
        n = 0
        for x, y, i, L in pairs:
            sx = stems(gl[x])
            if not sx:
                continue
            sy = stems(gl[rng.choice(others)])
            if not sy:
                continue
            n += 1
            if sx & sy:
                k += 1
        nulls.append(k / n if n else 0.0)
    m = sum(nulls) / len(nulls)
    sd = (sum((v - m) ** 2 for v in nulls) / max(1, len(nulls) - 1)) ** 0.5
    obs = real / tested if tested else 0.0
    sig = (obs - m) / sd if sd else 0.0
    ratio = obs / m if m else 0.0

    print(f"  testable pairs (both glossed)                 {tested}")
    print()
    print(f"  gloss overlap, real pairing       {obs*100:5.1f}%")
    print(f"  gloss overlap, shuffled control   {m*100:5.1f}%  (sd {sd*100:.2f})")
    print(f"  ratio {ratio:.2f}x     sigma {sig:.1f}")
    ok = ratio >= BAR_RATIO and sig >= BAR_SIGMA
    print()
    print(f"  BAR: ratio >= {BAR_RATIO}x and sigma >= {BAR_SIGMA}  ->  "
          f"{'PASS' if ok else 'FAIL'}")

    print("\nexamples of inherited meaning (container / part / shared):")
    for x, y, i, L, sh in hits[:14]:
        px = "".join(f"{ord(c):x} " for c in x).strip()
        py = "".join(f"{ord(c):x} " for c in y).strip()
        print(f"  [{px}]  <  [{py}]   {','.join(sh)}")

    # where does the part sit -- prefix, suffix, or inside?
    pos = Counter()
    for x, y, i, L, sh in hits:
        pos["prefix" if i == 0 else ("suffix" if i + L == len(x) else "infix")] += 1
    allpos = Counter()
    for x, y, i, L in pairs:
        allpos["prefix" if i == 0 else ("suffix" if i + L == len(x) else "infix")] += 1
    print("\nposition of the inherited part:")
    for k in ("prefix", "suffix", "infix"):
        a, b = pos[k], allpos[k]
        print(f"  {k:7s} {a:4d}/{b:4d}  ({a/b*100 if b else 0:.0f}% inherit)")

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
