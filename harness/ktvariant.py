"""Reading unread codes as variant spellings of defined ones.

Of the 22.4% of the book with no reading, 31% is words that occur once and
no statistical method can reach. But 53% of it sits within ONE glyph of a
code Kiraly & Tokai define: one glyph substituted, dropped or added. Some of
those are variant spellings. Some are different words that happen to share
two glyphs out of three. This decides which, with a gate that has a known
answer.

K&T's dictionary marks variant spellings itself, with "var." followed by the
variant code, and 91 of the codes so marked are in the text and currently
unread (the loader keyed entries by headword and dropped them). Those are
their readings, and they are taken as read without any test. They are also
the calibration: if variant spellings sit where their headword sits, the
declared variants must show it first. If they do not, the instrument cannot
see variants and nothing below is interpretable.

THE GATE, fixed before the run and not moved:

  For every unread code with 3+ occurrences that is one glyph from EXACTLY
  ONE defined code with 3+ occurrences, compare its page profile with the
  defined code's, against a frequency-matched random defined code standing
  in. Win = closer to the neighbour than to the stand-in. Null = two
  stand-ins.

  BAR A (calibration): K&T's declared variants must win >= 60% at >= 5 sigma.
  BAR B (the claim):   undeclared one-glyph neighbours must win >= 60% at
                       >= 5 sigma.

  Below bar A the instrument is blind and bar B is not reported as a result.
  Below bar B, neighbours are not variants and nothing is read from them;
  only K&T's declared variants are added, because those are theirs.

    python ktvariant.py
"""
import json
import random
import sys
from collections import Counter

import ktdict
import ktname as NM
import ktsegment as S
import rohonc_kt as KT

BAR_WIN = 0.60
BAR_SIGMA = 5.0
MIN_OCC = 3


def declared():
    """{variant code: head code} for K&T's own 'var.' marks, unique heads only.

    A 'var.' inside an entry can refer to a compound listed in that entry
    rather than the headword, and a single glyph turns up as 'var.' under
    three different heads. A variant with more than one head is dropped
    rather than guessed.
    """
    raw = json.load(open(ktdict.DICT, encoding="utf-8"))
    vm = {}
    for e in raw:
        fr = e["entry"]
        for i, f in enumerate(fr):
            if f.get("style") == "meta" and f["text"].strip() == "var.":
                for g in fr[i + 1:i + 4]:
                    if g.get("style") == "rohonc":
                        for w in g["text"].split():
                            w = "".join(c for c in w if 0xE000 <= ord(c) <= 0xEFFF)
                            if w and w != e["code"]:
                                vm.setdefault(w, set()).add(e["code"])
                        break
    return {v: next(iter(h)) for v, h in vm.items() if len(h) == 1}


def by_rule():
    """{variant code: head code} for K&T's variants stated as a RULE.

    declared() reads the explicit variant codes after a "var." mark. Some
    entries do not list spellings one by one; they state a substitution
    instead -- "[var. {670} ~ {520}, {540}; {ae0} ~ {060}, o]" means that
    inside this word 670 may be written 520 or 540, and ae0 may be written
    060 or dropped. Those spellings are K&T's readings just as much as the
    listed ones, and every one of them was unread here: two of them, 20
    occurrences of their word for PRAY, had been read as "as".

    A rule replaces ONE glyph, so a target longer than one glyph ends the
    rule -- that is an explicit variant being listed next, not a
    substitution. The headword is the rohonc text before the bracket.

    This does not touch declared(), and so does not touch BAR A or BAR B.
    """
    import itertools
    raw = json.load(open(ktdict.DICT, encoding="utf-8"))
    out = {}
    for e in raw:
        fr = e["entry"]
        flat, head, seen = [], [], False
        for f in fr:
            t = f.get("text", "")
            pua = "".join(c for c in t if 0xE000 <= ord(c) <= 0xEFFF)
            flat.append(("R", pua) if f.get("style") == "rohonc" else ("T", t))
            if not seen and f.get("style") == "rohonc":
                head.append(pua)
            if "[" in t:
                seen = True
        head = "".join(head)
        if not head:
            continue
        rules, i = [], 0
        while i < len(flat):
            if (flat[i][0] == "R" and len(flat[i][1]) == 1
                    and i + 1 < len(flat) and "~" in flat[i + 1][1]):
                src, tos, j = flat[i][1], [], i + 1
                while j + 1 < len(flat):
                    sep = flat[j][1]
                    if "\u00f8" in sep:
                        tos.append("")
                    if flat[j + 1][0] != "R" or len(flat[j + 1][1]) != 1:
                        break
                    if not ("~" in sep or sep.strip().startswith(",")):
                        break
                    tos.append(flat[j + 1][1])
                    j += 2
                if tos:
                    rules.append((src, tos))
                i = j
            i += 1
        if not rules:
            continue
        slots, total = [], 1
        for c in head:
            alts = {c}
            for src, tos in rules:
                if src == c:
                    alts |= set(tos)
            slots.append(sorted(alts))
            total *= len(alts)
        if total > 400:
            continue
        for combo in itertools.product(*slots):
            v = "".join(combo)
            if v and v != head and v != e["code"]:
                out.setdefault(v, set()).add(e["code"])
    return {v: next(iter(h)) for v, h in out.items() if len(h) == 1}


def one_edit(a, b):
    if a == b:
        return False
    if len(a) == len(b):
        return sum(x != y for x, y in zip(a, b)) == 1
    if abs(len(a) - len(b)) != 1:
        return False
    s, l = (a, b) if len(a) < len(b) else (b, a)
    return any(l[:i] + l[i + 1:] == s for i in range(len(l)))


def neighbours(unread, defset, types):
    """{unread code: the one defined code within one glyph}, unique only.

    Sorted, because the caller passes a set and the rng downstream consumes
    draws in whatever order this returns. Unsorted, BAR B moved between 53%
    and 61% from run to run on the same data -- across its own bar -- purely
    on Python's per-process string hashing. Sorting pins it.
    """
    pool = [c for c in defset if types.get(c, 0) >= MIN_OCC]
    out = {}
    for t in sorted(unread):
        if len(t) < 2:
            continue
        near = [c for c in pool if one_edit(t, c)]
        if len(near) == 1:
            out[t] = near[0]
    return out


def win_rate(cases, gl, types, occ, npages, rng):
    prof = {}

    def P(c):
        if c not in prof:
            prof[c] = NM.smooth(occ[c], npages)
        return prof[c]

    pool = [c for c in gl if types.get(c, 0) >= MIN_OCC]

    def match(c):
        n = types.get(c, 1)
        near = [x for x in pool if abs(types[x] - n) <= max(2, n * 0.35) and x != c]
        return near or pool

    wins = 0
    for v, h in cases:
        own = NM.cosine(P(v), P(h))
        ctrl = NM.cosine(P(v), P(rng.choice(match(h))))
        wins += own > ctrl
    win = wins / len(cases) if cases else 0.0
    nulls = []
    for _ in range(60):
        w = 0
        for v, h in cases:
            a = NM.cosine(P(v), P(rng.choice(match(h))))
            b = NM.cosine(P(v), P(rng.choice(match(h))))
            w += a > b
        nulls.append(w / len(cases) if cases else 0.0)
    m = sum(nulls) / len(nulls)
    sd = (sum((x - m) ** 2 for x in nulls) / max(1, len(nulls) - 1)) ** 0.5
    return win, m, sd, (win - m) / sd if sd else 0.0


def readings():
    """What this module licenses: {code: (head, 'kt'|'inferred')}."""
    d = ktdict.load()
    gl = {c: g for c, g, _ in d if g}
    doc = KT.load()
    types = Counter(t for p in doc for t in p.tokens)
    defset = set(gl)
    seg = {}
    for t in types:
        if t not in gl:
            s = S.segment(t, defset)
            if s and len(s) >= 2:
                seg[t] = s
    unread = {t for t in types if t not in gl and t not in seg}
    dec = {v: h for v, h in declared().items() if v in unread and h in gl}
    out = {v: (h, "kt") for v, h in dec.items()}
    # K&T's variants stated as a substitution rule rather than listed. Added
    # to what the renderer may read, and deliberately NOT to dec, so that
    # BAR A and BAR B keep measuring exactly what they measured before.
    for v, h in by_rule().items():
        if v in unread and h in gl and v not in out:
            out[v] = (h, "kt-rule")
    return gl, doc, types, seg, unread, dec, out


def main():
    gl, doc, types, seg, unread, dec, out = readings()
    tot = sum(types.values())
    U = sum(types[t] for t in unread)
    occ, npages = NM.profiles(doc)
    rng = random.Random(408)

    print("=" * 74)
    print("VARIANT SPELLINGS OF DEFINED CODES")
    print("=" * 74)
    print(f"unread tokens {U} ({U/tot*100:.1f}% of the book), {len(unread)} types")
    dtok = sum(types[v] for v in dec)
    print(f"K&T's own 'var.' marks reach {len(dec)} unread types, {dtok} tokens "
          f"({dtok/U*100:.1f}% of unread, {dtok/tot*100:.1f}% of the book)")

    # ---- BAR A: the declared variants, tested as if unknown
    casesA = sorted((v, h) for v, h in dec.items()
                    if types[v] >= MIN_OCC and types[h] >= MIN_OCC)
    wA, mA, sdA, sA = win_rate(casesA, gl, types, occ, npages, rng)
    print()
    print(f"BAR A -- do K&T's declared variants sit where their headword sits?")
    print(f"  declared variants tested                    {len(casesA)}")
    print(f"  closer to headword than to stand-in         {wA*100:5.1f}%")
    print(f"  same test, stand-ins on both sides          {mA*100:5.1f}%  (sd {sdA*100:.2f})")
    print(f"  sigma {sA:.1f}")
    okA = wA >= BAR_WIN and sA >= BAR_SIGMA
    print(f"  BAR: win >= {BAR_WIN*100:.0f}% and sigma >= {BAR_SIGMA}  ->  "
          f"{'PASS' if okA else 'FAIL'}")

    # ---- BAR B: undeclared one-glyph neighbours
    cand = {t for t in unread if t not in dec and types[t] >= MIN_OCC}
    nb = neighbours(cand, set(gl), types)
    ntok = sum(types[v] for v in nb)
    casesB = sorted(nb.items())
    wB, mB, sdB, sB = win_rate(casesB, gl, types, occ, npages, rng)
    print()
    print(f"BAR B -- do undeclared one-glyph neighbours sit where the defined code sits?")
    print(f"  unread codes with 3+ occurrences            {len(cand)}")
    print(f"  one glyph from exactly one defined code     {len(nb)}  ({ntok} tokens, "
          f"{ntok/U*100:.1f}% of unread, {ntok/tot*100:.1f}% of the book)")
    print(f"  closer to neighbour than to stand-in        {wB*100:5.1f}%")
    print(f"  same test, stand-ins on both sides          {mB*100:5.1f}%  (sd {sdB*100:.2f})")
    print(f"  sigma {sB:.1f}")
    okB = wB >= BAR_WIN and sB >= BAR_SIGMA
    if not okA:
        print(f"  BAR A failed: the instrument cannot see variants; B is NOT a result.")
    print(f"  BAR: win >= {BAR_WIN*100:.0f}% and sigma >= {BAR_SIGMA}  ->  "
          f"{'PASS' if okB else 'FAIL'}")

    print()
    print("=" * 74)
    print("WHAT IS READ")
    print("=" * 74)
    rule = {v: h for v, (h, tag) in out.items() if tag == "kt-rule"}
    rtok = sum(types[v] for v in rule)
    print(f"  K&T's declared variants (theirs, no test)   {len(dec):5d} types  {dtok:5d} tokens")
    print(f"  K&T's variants stated as a rule (theirs)    {len(rule):5d} types  {rtok:5d} tokens")
    if okA and okB:
        print(f"  inferred one-glyph variants                 {len(nb):5d} types  {ntok:5d} tokens")
        added = dtok + rtok + ntok
    else:
        print(f"  inferred one-glyph variants                     0 types      0 tokens  (gate failed)")
        added = dtok + rtok
    print(f"  book coverage  {(tot-U)/tot*100:5.1f}%  ->  {(tot-U+added)/tot*100:5.1f}%")
    print()
    print(f"  {'n':>5s}  {'code':24s}  read as")
    show = sorted(dec.items(), key=lambda x: (-types[x[0]], x[0]))[:12]
    for v, h in show:
        print(f"  {types[v]:5d}  {S.hx(v):24s}  "
              f"{S.best_sense(sorted(gl[h]))}   [K&T var.]")
    for v, h in sorted(rule.items(), key=lambda x: (-types[x[0]], x[0]))[:14]:
        print(f"  {types[v]:5d}  {S.hx(v):24s}  "
              f"{S.best_sense(sorted(gl[h]))}   [K&T var. by rule]")
    if okA and okB:
        for v, h in sorted(nb.items(), key=lambda x: -types[x[0]])[:20]:
            print(f"  {types[v]:5d}  {S.hx(v):24s}  ~{S.best_sense(gl[h])}")
    return 0 if okA and okB else 1


if __name__ == "__main__":
    sys.exit(main())
