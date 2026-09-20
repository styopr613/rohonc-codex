"""The crosser-off: what a hole CANNOT mean, and what is left that it can.

Every unread sign in this book was being treated as an open guess. It is not.
1,365 English words already have a sign of their own here, and a sign that has
no reading cannot mean any of them, because those words are already spoken
for. That one constraint turns "the blank could be any word" into "the blank
is a word the sources use that this book has not yet said", and the second
list is short.

The user put it plainly on 2026-09-20: give a man a sentence from a text
everyone knows with one word missing and he will guess the word. He was
right, and the test that proved it is in the git log: 213r:9 reads "and then
the apostles carried [blank] twelve, filled up", the guess was *basket*, and
Kiraly and Tokai's own entry turned out to name 775520 as *basket* at that
exact line. What had been called unreadable was only unchecked.

What this file does NOT do is decide anything. It prints two lists, the taken
and the free, and the evidence around a hole. The reading is still made by
hand and still has to survive every occurrence before it is graded above C.

    python3 ktcross.py --holes [N]     the worklist: lines with exactly one hole
    python3 ktcross.py --taken WORD... is this word already spoken for, and by whom
    python3 ktcross.py --free [N]      commonest source words with no sign yet
    python3 ktcross.py --line PAGE N   one hole: context, source note, free field
"""
import os
import re
import sys
from collections import Counter, defaultdict

import ktaffix as A
import ktcoverage as C
import ktsegment as S
import ktvariant as V
import kttranslate as T

HERE = os.path.dirname(os.path.abspath(__file__))
# Frequency is counted on the KJV alone. The rest of the reference corpus
# (Caxton's Golden Legend, the four play cycles) is the right SOURCE world for
# this book but its spelling is not standard -- hym, haue, oure, xal, schall,
# ffor -- and ranking on it fills the free list with spellings rather than
# words. The KJV is the one modern-spelt member of the set.
CORPUS = os.path.join(os.path.dirname(HERE), "data", "ref", "rohonc", "bible_kjv.txt")
TRANSLATION = os.path.join(os.path.dirname(HERE), "work", "rohonc",
                           "translation", "rohonc_translation.md")

# Words too common to carry information about a hole, and all of them are read
# already anyway. Kept explicit rather than computed so the list can be argued
# with.
STOP = set("""a an the and or but if of to in on at by for with from as that this
these those is are was were be been being am do does did done have has had not no
nor so then than when where which who whom whose what how why all any both each
few more most other some such only own same too very can will just should now
i you he she it we they me him her us them my your his its our their mine yours
theirs himself herself itself themselves myself yourself shall may might must
unto thee thou thy thine ye upon into out up down over under again further once
here there about against between during before after above below off""".split())

SUFFIX = ("iest", "ieth", "ing", "eth", "est", "ies", "ed", "es", "s", "e")

# Irregular forms the crude stemmer cannot reach. Without these the free list
# offers came, went, took, saw, said and spake as words the book has never
# said, when it has signs for all of them.
IRREG = {
    "came": "come", "come": "come", "went": "go", "gone": "go", "goeth": "go",
    "took": "take", "taken": "take", "saw": "see", "seen": "see",
    "said": "say", "saith": "say", "spake": "speak", "spoken": "speak",
    "heard": "hear", "given": "give", "gave": "give", "made": "make",
    "written": "write", "wrote": "write", "told": "tell", "knew": "know",
    "known": "know", "began": "begin", "begun": "begin", "brought": "bring",
    "sent": "send", "found": "find", "fell": "fall", "fallen": "fall",
    "held": "hold", "kept": "keep", "left": "leave", "lost": "lose",
    "met": "meet", "paid": "pay", "put": "put", "read": "read",
    "ran": "run", "rose": "rise", "risen": "rise", "sat": "sit",
    "slew": "slay", "slain": "slay", "stood": "stand", "thought": "think",
    "understood": "understand", "wept": "weep", "won": "win",
    "men": "man", "children": "child", "women": "woman", "feet": "foot",
    "teeth": "tooth", "brethren": "brother", "hath": "have", "had": "have",
    "art": "be", "wast": "be", "wert": "be", "doth": "do", "done": "do",
    "did": "do", "dost": "do",
}


def stem(w):
    """A deliberately crude stem, so bless/blessed/blesseth land together.

    Nothing here depends on the stemmer being right in general; it only has to
    stop the same English word being called free in one spelling and taken in
    another. When it is wrong it is wrong towards calling a word TAKEN, which
    is the safe direction: it withholds a candidate rather than offering one
    that is already spoken for.
    """
    w = w.lower()
    # Map the irregular form to its lemma FIRST, then stem the lemma, so that
    # took -> take -> tak matches the gloss "grab, take" -> tak. Returning the
    # lemma unstemmed here was a bug: it put took, made, hath, told and written
    # on the free list while the book had signs for all of them.
    w = IRREG.get(w, w)
    for suf in SUFFIX:
        if len(w) > len(suf) + 2 and w.endswith(suf):
            return w[: -len(suf)]
    return w


def build():
    gl, doc, seg = C.build()
    var = {v: h for v, (h, _) in V.readings()[6].items()}
    prop = T.load_proposals()
    inv = set(gl) | set(seg) | set(var) | set(prop)
    types_all = {t for p in doc for t in p.tokens}
    while True:
        added = 0
        for t in sorted(types_all):
            b = A.strip(t)[0]
            if b in inv:
                continue
            cut = S.segment(b, inv)
            if cut and len(cut) >= 2:
                seg[b] = cut
                inv.add(b)
                added += 1
        if not added:
            break
    T.ORDER.update(T.ordered())
    T.prop_ref.update(prop)
    return gl, doc, seg, var, prop, inv


def hx(s):
    return "".join(f"{ord(c)-0xE000:03x}" for c in s)


def taken_index(gl, prop):
    """{stem: [(sign, the gloss it came from)]}.

    A gloss is a phrase, not a word: "bow down", "the Most High [God]",
    "<place-value delimiter in numerals>". Every content word of every gloss
    counts as spoken for. Bracketed and angled material is dropped, because
    that is K&T's editorial comment rather than the word itself.
    """
    idx = defaultdict(list)

    def add(sign, gloss):
        g = re.sub(r"[<\[(][^>\])]*[>\])]", " ", gloss)
        for w in re.findall(r"[a-zA-Z]+", g):
            if w.lower() in STOP:
                continue
            idx[stem(w)].append((sign, gloss.strip()))

    for c, senses in gl.items():
        for g in senses:
            add(hx(c), g)
    for c, (g, tier) in prop.items():
        add(hx(c), g.replace("_", " "))
    return idx


def corpus_freq():
    if not os.path.exists(CORPUS):
        return Counter()
    text = open(CORPUS, encoding="utf-8", errors="ignore").read().lower()
    # Filter on the STEM, not the surface form. Filtering on the surface let
    # hath, art and doth through as words the book had never said, when have,
    # be and do are in the stop list precisely because every book says them.
    stopstem = {stem(w) for w in STOP}
    return Counter(w for w in re.findall(r"[a-z]+", text)
                   if len(w) > 2 and w not in STOP and stem(w) not in stopstem)


def holes(gl, doc, seg, var, prop, inv, only_hapax=True):
    """Lines carrying exactly one unread word. The worklist."""
    cnt = Counter(A.strip(t)[0] for p in doc for t in p.tokens)
    out = []
    for p in doc:
        for i, ln in enumerate(p.lines, 1):
            tk = [t for run in ln for t in run]
            miss = [A.strip(t)[0] for t in tk if A.strip(t)[0] not in inv]
            if len(miss) != 1:
                continue
            if only_hapax and cnt[miss[0]] != 1:
                continue
            s = " ".join("<<___>>" if A.strip(t)[0] == miss[0]
                         else T.render_token(t, gl, seg, False, var, prop)
                         for t in tk)
            out.append((p.page, i, hx(miss[0]), cnt[miss[0]], s))
    return out


def note_for(page):
    """The line of this project's own translation that names the source."""
    if not os.path.exists(TRANSLATION):
        return ""
    text = open(TRANSLATION, encoding="utf-8").read()
    m = re.search(r"^## %s [^\n]*\n(.*?)(?=^## |\Z)" % page, text, re.M | re.S)
    if not m:
        return ""
    notes = [l[2:].strip() for l in m.group(1).splitlines() if l.startswith("> ")]
    return " ".join(notes)


def main(argv):
    gl, doc, seg, var, prop, inv = build()

    if "--taken" in argv:
        idx = taken_index(gl, prop)
        for w in argv[argv.index("--taken") + 1:]:
            # A stop word is not indexed, so it would report "free" and mean
            # the opposite: from, before, have, be and the rest are function
            # words that every sign inventory already carries. Say so.
            if w.lower() in STOP or stem(w) in {stem(x) for x in STOP}:
                print(f"  STOP   {w:16s} function word, not indexed -- these are all read already")
                continue
            hits = idx.get(stem(w), [])
            if hits:
                who = "; ".join(f"{s} {g!r}" for s, g in hits[:4])
                print(f"  TAKEN  {w:16s} {who}")
            else:
                print(f"  free   {w:16s} -")
        return 0

    if "--free" in argv:
        k = argv.index("--free")
        n = int(argv[k + 1]) if len(argv) > k + 1 and argv[k + 1].isdigit() else 60
        idx = taken_index(gl, prop)
        freq = corpus_freq()
        free = [(w, c) for w, c in freq.most_common(4000) if stem(w) not in idx]
        print(f"the {n} commonest words of the source corpus that no sign carries yet")
        print("(frequency counted on the KJV; the legend and the plays are the same")
        print(" source world but their spelling is not standard enough to rank on)")
        for w, c in free[:n]:
            print(f"  {c:7d}  {w}")
        return 0

    if "--line" in argv:
        k = argv.index("--line")
        page, num = argv[k + 1], int(argv[k + 2])
        idx = taken_index(gl, prop)
        for p in doc:
            if p.page != page:
                continue
            for i, ln in enumerate(p.lines, 1):
                if abs(i - num) > 2:
                    continue
                tk = [t for run in ln for t in run]
                miss = [A.strip(t)[0] for t in tk if A.strip(t)[0] not in inv]
                s = " ".join(("<<___%s___>>" % hx(A.strip(t)[0]))
                             if A.strip(t)[0] in miss
                             else T.render_token(t, gl, seg, False, var, prop)
                             for t in tk)
                print(f"  {i:2d}{'*' if i == num else ' '} {s}")
        note = note_for(page)
        if note:
            print(f"\n  source note for {page}: {note}")
        return 0

    n = 40
    for a in argv:
        if a.isdigit():
            n = int(a)
    hs = holes(gl, doc, seg, var, prop, inv)
    print(f"{len(hs)} lines have exactly one unread word and that word occurs once")
    print("each is one reading away from a fully read line\n")
    for page, i, h, k, s in hs[:n]:
        print(f"{page}:{i:<3d} {h:24s} {s[:120]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
