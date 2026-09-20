"""Does the glossed Rohonc vocabulary look like a gospel, or just like a text?

Kiraly & Tokai read the codex as a New Testament paraphrase with apocryphal
Marian material, prayers and saints' lives. That is a claim about content, and
content is testable without reading a word of the codex: if the reading is
right, the meanings their dictionary assigns should be distributed like a
gospel's vocabulary and not like prose in general.

The test weighs both. For every word token the dictionary covers, its glosses
are counted, each sense sharing the token's weight so no arbitrary choice of
primary sense is made. The resulting content-word profile is compared with a
gospel text and with a general English corpus, by how much of each reference's
top vocabulary it recovers.

The comparison is not circular in the way the glossing itself is. Kiraly &
Tokai built the dictionary by working out what codes mean from context, so of
course the glossed text reads coherently on the passages they worked on. What
they did not control is how often each code occurs. The frequency profile is a
property of the codex; matching a gospel's profile is a prediction their
reading makes and could have failed.

    python ktvalidate.py
"""
import os
import re
import unicodedata
from collections import Counter

import ktdict
import rohonc_kt as KT

GOSPELS = "/opt/plaintextclassics/private/gospels/gospels.txt"
ENGLISH = os.path.join(os.path.dirname(ktdict.DICT), "..", "..", "ref",
                       "english.conllu")

STOP = set("""a an the and or but if then than that this these those of in on at to
for from by with without into onto upon as is are was were be been being am do does
did done have has had having will would shall should may might can could must not
no nor so such there here it its it's he she they them his her their we us our you
your i me my who whom which what when where why how all any both each few more most
other some only own same very s t just now also one two three up down out over
under again further once about against between through during before after above
below off why said say says thee thou thy ye unto shall""".split())

WORD = re.compile(r"[a-z]+")
META = re.compile(r"<[^>]*>")


def fold(t):
    """Strip accents so Hungarian spellings in the glosses tokenise as English.

    The dictionary writes Jezus with an accent. The word pattern is ASCII, so
    it split that into "j" and "zus", and the comparison then reported that the
    glosses never mention Jesus.
    """
    return "".join(c for c in unicodedata.normalize("NFD", t)
                   if not unicodedata.combining(c))


def stem(w):
    """Crude suffix stripping, so glosses in base form match inflected text.

    The dictionary glosses verbs as "say", "come", "give"; a gospel text writes
    "said", "came", "gave", "saying". Without this the comparison measures
    English morphology rather than vocabulary: the first run reported that the
    glosses never mention came, went, told, saying, took or gave, all of which
    are in the dictionary as come, go, tell, say, take, give.
    """
    for suf in ("ings", "ing", "edly", "ed", "es", "s"):
        if w.endswith(suf) and len(w) - len(suf) >= 3:
            w = w[:-len(suf)]
            break
    # and a trailing e, so disciple and disciples both reach discipl; without
    # this the two stemmed differently and counted as separate words
    return w[:-1] if len(w) > 3 and w.endswith("e") else w


def content(counter):
    out = Counter()
    for w, n in counter.items():
        # stem BEFORE the stop check, or the two sides disagree: the gospel's
        # "saying" stemmed to "say" and was kept, while the glosses' literal
        # "say" was dropped as a stopword, so "say" was reported as a word the
        # dictionary never mentions when it is one of its commonest glosses.
        st = stem(w)
        if st not in STOP and w not in STOP and len(st) > 2:
            out[st] += n
    return out


def gospel_words():
    txt = open(GOSPELS, encoding="utf-8", errors="replace").read().lower()
    txt = re.sub(r"<[^>]+>", " ", txt)
    return Counter(WORD.findall(fold(txt)))


def english_words(limit=400000):
    c = Counter()
    n = 0
    with open(ENGLISH, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            if not line or line.startswith("#"):
                continue
            p = line.rstrip("\n").split("\t")
            if len(p) < 3:
                continue
            w = fold(p[1]).lower()
            if WORD.fullmatch(w):
                c[w] += 1
                n += 1
                if n >= limit:
                    break
    return c


def glossed_profile():
    d = ktdict.load()
    gl = {c: g for c, g, _ in d if g}
    doc = KT.load()
    types = Counter(t for p in doc for t in p.tokens)
    prof = Counter()
    for t, n in types.items():
        g = gl.get(t)
        if not g:
            continue
        # drop the grammatical metalanguage: "<2nd person singular personal
        # pronoun>", "<copula>", "<place-value delimiter in numerals>". Left in,
        # it dominated the profile with pronoun, singular, delimiter, numerals
        # and copula, none of which is a word of the codex.
        senses = [META.sub(" ", x) for x in g]
        senses = [x for x in senses if WORD.findall(x.lower())]
        if not senses:
            continue
        share = n / len(senses)
        for sense in senses:
            for w in WORD.findall(fold(sense).lower()):
                prof[w] += share
    return prof


def recall(prof, ref, k):
    top = [w for w, _ in ref.most_common(k)]
    have = set(prof)
    return sum(1 for w in top if w in have) / k * 100


def main():
    prof = content(glossed_profile())
    gos = content(gospel_words())
    eng = content(english_words())
    print("=" * 74)
    print("DOES THE GLOSSED VOCABULARY LOOK SPECIFICALLY LIKE A GOSPEL?")
    print("=" * 74)
    print(f"glossed content vocabulary: {len(prof)} words")
    print(f"gospel reference: {sum(gos.values()):.0f} content tokens, "
          f"{len(gos)} types")
    print(f"general English reference: {sum(eng.values()):.0f} content tokens, "
          f"{len(eng)} types\n")
    print(f"{'top k of reference':>20s} {'gospel':>9s} {'English':>9s} {'ratio':>7s}")
    for k in (25, 50, 100, 200, 400):
        a, b = recall(prof, gos, k), recall(prof, eng, k)
        r = a / b if b else float("nan")
        print(f"{k:20d} {a:8.1f}% {b:8.1f}% {r:7.2f}x")
    print("\ntop 25 content words of the glossed codex, by weight:")
    for w, n in prof.most_common(25):
        mark = "  (in gospel top 100)" if w in [x for x, _ in gos.most_common(100)] else ""
        print(f"   {w:18s} {n:8.0f}{mark}")
    print("\ngospel top 25 the glosses never mention:")
    miss = [w for w, _ in gos.most_common(100) if w not in prof][:25]
    print("   " + ", ".join(miss) if miss else "   (none)")


if __name__ == "__main__":
    main()
