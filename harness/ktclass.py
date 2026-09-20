"""What kind of word is an undefined code? Fingerprint it against known classes.

Naming a code's meaning has failed nine times here. Naming its grammatical
class is a smaller claim and a testable one, and it narrows the field any
hypothesis has to come from.

Kiraly & Tokai's glosses carry their own part-of-speech evidence: an entry
reading "Lucifer/Satan/angel" is a noun, one reading "say/speech" is a verb,
one reading "<auxiliary>" or "because/in order that" is grammatical. Codes are
sorted into classes on that basis, each class's positional behaviour is
measured, and an undefined code is compared with the classes rather than with
a guess.

The features are all things a class determines and a meaning does not: where in
a line a code falls, whether it repeats within a line, and what kinds of word
sit either side of it.
"""
from collections import Counter

import ktsolve

NOUNY = ("lucifer", "satan", "angel", "lord", "god", "son", "man", "mother",
         "father", "king", "kingdom", "disciple", "apostle", "virgin", "soul",
         "heaven", "house", "book", "silver", "throne", "cup", "servant")
VERBY = ("say", "speak", "come", "go", "give", "take", "show", "pray", "see",
         "hear", "bring", "carry", "believe", "forgive", "die", "kill",
         "resurrect", "bow", "hide", "eat", "write", "arrest", "crucify")
GRAMMY = ("auxiliary", "copula", "pronoun", "delimiter", "marker", "particle",
          "conjunction", "preposition", "article", "tense", "genitive",
          "dative", "because", "in order that", "meaningless sign")


def classify(gl):
    out = {}
    for c, g in gl.items():
        txt = " ".join(g).lower()
        if any(w in txt for w in GRAMMY):
            out[c] = "grammatical"
        elif any(w in txt for w in VERBY):
            out[c] = "verb"
        elif any(w in txt for w in NOUNY):
            out[c] = "noun"
    return out


def features(gl, doc, target, cls):
    lines = [[t for run in runs for t in run] for p in doc for runs in p.lines]
    n = li = lf = rep = 0
    nb = Counter()
    for l in lines:
        k = sum(1 for t in l if t == target)
        if not k:
            continue
        n += k
        if k > 1:
            rep += 1
        if l[0] == target:
            li += 1
        if l[-1] == target:
            lf += 1
        for i, t in enumerate(l):
            if t != target:
                continue
            for j in (i - 1, i + 1):
                if 0 <= j < len(l):
                    nb[cls.get(l[j], "unknown")] += 1
    tot = sum(nb.values()) or 1
    return {"n": n, "line_initial": li / max(1, n), "line_final": lf / max(1, n),
            "repeats_in_line": rep / max(1, n),
            "nbr_noun": nb["noun"] / tot, "nbr_verb": nb["verb"] / tot,
            "nbr_gram": nb["grammatical"] / tot}


def class_profile(gl, doc, cls, want, min_occ=20, max_codes=60):
    freq = Counter(t for p in doc for t in p.tokens)
    codes = [c for c, k in freq.most_common() if cls.get(c) == want and k >= min_occ]
    codes = codes[:max_codes]
    acc = Counter()
    for c in codes:
        f = features(gl, doc, c, cls)
        for k, v in f.items():
            if k != "n":
                acc[k] += v
    return {k: v / max(1, len(codes)) for k, v in acc.items()}, len(codes)


def distance(a, b):
    keys = [k for k in a if k in b]
    return sum(abs(a[k] - b[k]) for k in keys) / len(keys)


if __name__ == "__main__":
    import kttopical
    gl, doc = ktsolve.load()
    cls = classify(gl)
    print(f"defined codes classified: {dict(Counter(cls.values()))}\n")
    profs = {}
    for w in ("noun", "verb", "grammatical"):
        profs[w], k = class_profile(gl, doc, cls, w)
        print(f"{w:12s} (n={k:2d})  " +
              "  ".join(f"{a}={b:.2f}" for a, b in sorted(profs[w].items())))
    rows = kttopical.concentration(gl, doc)
    print("\nundefined codes, nearest class (lower distance = closer):")
    print(f"{'n':>5s} {'peak band':>11s}  {'nearest':>12s}  {'noun':>7s} {'verb':>7s} {'gram':>7s}")
    for r in rows[:10]:
        f = features(gl, doc, r["code"], cls)
        d = {w: distance(f, p) for w, p in profs.items()}
        best = min(d, key=d.get)
        print(f"{r['n']:5d} {r['peak']:4d}-{r['peak']+19:<4d} {best:>12s}  " +
              "  ".join(f"{d[w]:7.3f}" for w in ("noun", "verb", "grammatical")))
