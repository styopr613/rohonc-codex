"""Do codex pages localise to gospel passages? The one extension test that passed.

Kiraly & Tokai gloss 101 codes as proper names. Names survive paraphrase and
translation where ordinary vocabulary does not, so they are the anchors worth
trusting. For every page carrying two or more names that also occur in the
gospel text, this asks how close together those names sit in the gospel -- and
compares with the same count of names drawn at random.

This is a prediction their reading makes and did not have to come true: if the
name identifications were wrong, or the codex were not following the gospels,
a page's names would scatter across the gospel like random ones do.

    python ktlocalise.py
"""
import random
import re
import statistics as st
from collections import Counter, defaultdict

import ktdict
import ktextend as E
import rohonc_kt as KT


def main():
    d = ktdict.load()
    gl = {c: g for c, g, _ in d if g}
    doc = KT.load()
    _, gw = E.gospel_windows()
    gstem = [E.stem(w) for w in gw]
    names = {}
    for c, g in gl.items():
        for s in g:
            s2 = E.META.sub(" ", s).strip()
            m = re.fullmatch(r"([A-Z][a-z]{2,})(?: \(.*\))?", s2)
            if m:
                names.setdefault(c, set()).add(E.stem(E.fold(m.group(1)).lower()))
    nameset = {x for v in names.values() for x in v}
    gpos = {}
    for i, s in enumerate(gstem):
        if s in nameset:
            gpos.setdefault(s, []).append(i)
    # a plain dict, on purpose: with a defaultdict the membership checks below
    # created empty entries for names absent from the gospel, and the null
    # sampler then drew one and died on min() of an empty list
    print(f"codes glossed as a proper name: {len(names)}")
    print(f"distinct names: {len(nameset)}, of which also in the gospel text: {len(gpos)}")

    def spread(ns):
        best = None
        for nm in ns:
            for i in gpos[nm]:
                dd = sum(min(abs(i - j) for j in gpos[o]) for o in ns if o != nm)
                if best is None or dd < best:
                    best = dd
        return best / max(1, len(ns) - 1)

    hits = []
    for p in doc:
        ns = Counter()
        for t in p.tokens:
            if t in names:
                for nm in names[t]:
                    if nm in gpos:
                        ns[nm] += 1
        if len(ns) >= 2:
            hits.append((p.page, ns))
    print(f"pages carrying two or more gospel names: {len(hits)} of {len(doc)}")
    rng = random.Random(408)
    obs = [spread(ns) for _, ns in hits]
    allnm = list(gpos)
    nulls = []
    for _ in range(300):
        k = len(rng.choice(hits)[1])
        nulls.append(spread(Counter(rng.sample(allnm, min(k, len(allnm))))))
    print("\ndistance apart, in gospel words, of the names on one page")
    print(f"  real pages    median {st.median(obs):8.0f}")
    print(f"  random names  median {st.median(nulls):8.0f}")
    b = sum(1 for x in obs if x < st.median(nulls))
    print(f"  real pages tighter than the random median: {b}/{len(obs)} "
          f"({b/len(obs)*100:.0f}%)   chance 50%")


if __name__ == "__main__":
    main()
