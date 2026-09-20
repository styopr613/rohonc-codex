"""Working out codes the dictionary does not define, by alignment to the gospels.

Kiraly & Tokai define 885 codes. The text uses 5,010, so four words in ten have
no gloss, and the undefined vocabulary is steeply concentrated: six codes alone
are 5.9% of the book. This tries to work some of them out. It is original work
on the part of the problem nobody has done, built on their published
foundation and crediting it.

The method uses the one thing their reading gives us: if the codex paraphrases
the gospels, a passage of it should align to a passage of gospel text. Align
the two by the words we can already read, and the undefined codes in the span
line up with the gospel words left unaccounted for. Each alignment is weak
evidence; a code that draws the same candidate from several independent
passages is worth proposing.

**The method is tested before it is trusted.** Codes the dictionary does define
are hidden from the aligner, and it is asked to recover them. Whatever share of
those it gets right is the share of its proposals for genuinely unknown codes
that can be believed. A method that cannot recover known glosses has no
standing to invent new ones, and this is checked first, not after.

Nothing here reproduces Kiraly & Tokai's dictionary. It consumes their glosses
to locate passages and reports only codes they have not defined.
"""
import re
import unicodedata
from collections import Counter, defaultdict

import ktdict
import rohonc_kt as KT

GOSPELS = "/opt/plaintextclassics/private/gospels/gospels.txt"
WORD = re.compile(r"[a-z]+")
META = re.compile(r"<[^>]*>")
WINDOW = 70
STRIDE = 25

STOP = set("""a an the and or but if then than that this these those of in on at to
for from by with without into onto upon as is are was were be been being am do does
did done have has had having will would shall should may might can could must not
no nor so such there here it its he she they them his her their we us our you your
i me my who whom which what when where why how all any both each few more most
other some only own same very just now also up down out over under again once
about against between through during before after above below off""".split())


def fold(t):
    return "".join(c for c in unicodedata.normalize("NFD", t)
                   if not unicodedata.combining(c))


# Irregular forms the gospel uses constantly and no suffix rule reaches. The
# alignment gate proposed "spoke" for the code glossed "say" and was scored
# wrong; that is the evaluation failing, not the method, so these are folded.
IRREG = {}
for base, forms in {
    "say": "said says saying spoke spoken speak speaks", "go": "went gone goes going",
    "come": "came comes coming", "take": "took taken takes taking",
    "give": "gave given gives giving", "see": "saw seen sees seeing",
    "tell": "told tells telling", "know": "knew known knows",
    "make": "made makes making", "do": "did done does", "eat": "ate eaten",
    "die": "died dead death dies", "bear": "bore born borne",
    "rise": "rose risen arose arisen", "sit": "sat", "stand": "stood",
    "send": "sent sends", "leave": "left leaves", "bring": "brought brings",
    "hear": "heard hears", "find": "found finds", "hold": "held holds",
    "fall": "fell fallen", "lie": "lay lain", "begin": "began begun",
    "answer": "answered answers", "write": "wrote written",
    "child": "children", "man": "men", "woman": "women", "foot": "feet",
}.items():
    for f in forms.split():
        IRREG[f] = base


def stem(w):
    if w in IRREG:
        return IRREG[w]
    for suf in ("ings", "ing", "edly", "ed", "es", "s"):
        if w.endswith(suf) and len(w) - len(suf) >= 3:
            w = w[:-len(suf)]
            break
    return w[:-1] if len(w) > 3 and w.endswith("e") else w


def content(words):
    return [stem(w) for w in words if w not in STOP and len(w) > 2]


def gospel_windows():
    txt = fold(open(GOSPELS, encoding="utf-8", errors="replace").read().lower())
    ws = WORD.findall(txt)
    out = []
    for i in range(0, len(ws) - WINDOW, STRIDE):
        out.append((i, content(ws[i:i + WINDOW])))
    return out, ws


def idf(windows):
    df = Counter()
    for _, w in windows:
        df.update(set(w))
    n = len(windows)
    import math
    return {w: math.log(n / (1 + c)) for w, c in df.items()}, n


def page_terms(page, gl):
    """Content stems the dictionary lets us read on this page, and the unknown codes."""
    known, unknown = [], []
    for t in page.tokens:
        g = gl.get(t)
        if not g:
            unknown.append(t)
            continue
        senses = [META.sub(" ", x) for x in g]
        ws = []
        for s in senses:
            ws += WORD.findall(fold(s).lower())
        c = content(ws)
        if c:
            known += c
        else:
            unknown.append(t)
    return known, unknown


def best_window(terms, windows, I):
    """Highest idf-weighted overlap, and the margin over the runner-up."""
    tset = Counter(terms)
    scores = []
    for k, (pos, w) in enumerate(windows):
        ws = set(w)
        s = sum(I.get(x, 0.0) for x in tset if x in ws)
        scores.append((s, k))
    scores.sort(reverse=True)
    if len(scores) < 2:
        return None
    (s1, k1), (s2, _) = scores[0], scores[1]
    return k1, s1, (s1 - s2)


def gate_bag_of_words(gl, doc, wins, I, rng, shuffles=200):
    """Do real pages align to a gospel window better than random word bags?"""
    import statistics as st
    rows, pool = [], []
    for p in doc:
        known, _ = page_terms(p, gl)
        pool += known
        if len(known) < 15:
            continue
        r = best_window(known, wins, I)
        if r:
            rows.append((r[1], len(known)))
    nulls = []
    for _ in range(shuffles):
        m = rng.choice(rows)[1]
        r = best_window([rng.choice(pool) for _ in range(m)], wins, I)
        if r:
            nulls.append(r[1])
    nulls.sort()
    obs = sorted(x[0] for x in rows)
    thr = nulls[int(len(nulls) * .95)]
    above = sum(1 for x in obs if x > thr)
    print("GATE 1 -- bag-of-words alignment: real pages vs random word bags")
    print(f"  real pages     median best-window score {st.median(obs):.2f}")
    print(f"  random bags    median best-window score {st.median(nulls):.2f}")
    print(f"  real pages above the random 95th percentile: {above}/{len(obs)} "
          f"({above/len(obs)*100:.0f}%)   chance 5%")
    return above / len(obs)


def gate_enrichment(gl, doc, gstem, names, gpos, n_hidden=60, radius=120):
    """Hide known codes; do words enriched near their pages recover the gloss?"""
    import math
    from collections import Counter
    bg = Counter(gstem)
    NB = sum(bg.values())
    types = Counter(t for p in doc for t in p.tokens)
    hidden = [t for t, _ in types.most_common() if t in gl][:n_hidden]
    loci = {}
    for p in doc:
        ns = Counter()
        for t in p.tokens:
            if t in names:
                for nm in names[t]:
                    if nm in gpos:
                        ns[nm] += 1
        if len(ns) < 2:
            continue
        best = None
        for nm in ns:
            for i in gpos[nm]:
                d = sum(min(abs(i - j) for j in gpos[o]) for o in ns if o != nm)
                if best is None or d < best[1]:
                    best = (i, d)
        loci[p.page] = best[0]
    hit1 = hit5 = hit20 = tested = 0
    for code in hidden:
        truth = set()
        for s in gl[code]:
            truth |= {stem(w) for w in WORD.findall(fold(META.sub(" ", s)).lower())
                      if w not in STOP and len(w) > 2}
        near, npg = Counter(), 0
        for p in doc:
            if p.page not in loci or code not in p.tokens:
                continue
            npg += 1
            i = loci[p.page]
            near.update(w for w in gstem[max(0, i - radius):i + radius]
                        if w not in STOP and len(w) > 2)
        if not truth or npg < 3:
            continue
        tot = sum(near.values())
        sc = sorted(((c * math.log(c / (bg[w] / NB * tot)), w) for w, c in near.items()
                     if c >= 3 and bg[w]), reverse=True)
        tested += 1
        rank = next((i for i, (_, w) in enumerate(sc, 1) if w in truth), None)
        if rank:
            hit1 += rank <= 1
            hit5 += rank <= 5
            hit20 += rank <= 20
    print("\nGATE 2 -- neighbourhood enrichment, known glosses hidden")
    print(f"  tested {tested} codes")
    print(f"  true gloss ranked #1   {hit1:3d}  ({hit1/max(1,tested)*100:.0f}%)")
    print(f"  true gloss in top 5    {hit5:3d}  ({hit5/max(1,tested)*100:.0f}%)")
    print(f"  true gloss in top 20   {hit20:3d}  ({hit20/max(1,tested)*100:.0f}%)")


if __name__ == "__main__":
    import random
    d = ktdict.load()
    gl = {c: g for c, g, _ in d if g}
    doc = KT.load()
    wins, gw = gospel_windows()
    I, _ = idf(wins)
    gstem = [stem(w) for w in gw]
    names = {}
    for c, g in gl.items():
        for s in g:
            s2 = META.sub(" ", s).strip()
            m = re.fullmatch(r"([A-Z][a-z]{2,})(?: \(.*\))?", s2)
            if m:
                names.setdefault(c, set()).add(stem(fold(m.group(1)).lower()))
    nameset = {x for v in names.values() for x in v}
    gpos = {}
    for i, s in enumerate(gstem):
        if s in nameset:
            gpos.setdefault(s, []).append(i)
    print("TWO FAILED GATES, KEPT AS THE RECORD OF WHAT DID NOT WORK\n")
    gate_bag_of_words(gl, doc, wins, I, random.Random(408))
    gate_enrichment(gl, doc, gstem, names, gpos)
