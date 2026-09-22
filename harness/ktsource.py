"""For every folio, the passages it is actually working from.

    python3 ktsource.py build          index the corpus (cached)
    python3 ktsource.py show 052v      what this folio draws on, and why
    python3 ktsource.py run            write work/rohonc/sources.json

Two ways a folio gets its sources, and both are kept:

  CITED.     Kiraly and Tokai's notes, and this project's, name a chapter and
             verse for most folios. Those verses are taken from the Douay,
             which is the text the compiler had, widened two verses each way.

  RETRIEVED. Everything else the manuscript draws on has no citation: the
             Life of Adam and Eve, the Golden Legend, the Rood legend, the
             mystery plays, the missal, Barlaam, Josephus. Each is cut into
             overlapping windows and indexed; a folio is scored against every
             window by the rare words they share, and the best few are kept.

What this file does NOT do is decide anything. It gathers. The reading pass
(ktreading.py) is shown what is gathered and writes the English; the gloss in
Book Two remains the evidence, and a source is a suggestion about what a
broken line was reaching for, never a licence to print the source instead.
"""
import argparse
import json
import math
import os
import pickle
import re
import sys
from collections import Counter, defaultdict

import corpus
import kttestlib as T
import ktcross as K
import ktleft as L

REF = os.path.join(corpus.ROOT, "data", "ref", "rohonc")
TRANS = os.path.join(corpus.ROOT, "work", "rohonc", "translation",
                     "rohonc_translation.md")
INDEX = os.path.join(corpus.ROOT, "work", "rohonc", "source_index.pkl")
OUT = os.path.join(corpus.ROOT, "work", "rohonc", "sources.json")

# What the manuscript is made of, as far as it is known. Left out: ALL.txt (a
# concatenation of the others), the KJV (a translation the compiler could not
# have had), and the whole of Charles's Pseudepigrapha -- four fifths of that
# volume is critical apparatus, and its dense rare vocabulary outscored every
# real hit. The part of it the codex actually uses, the Life of Adam and Eve,
# is extracted into its own file and kept.
BOOKS = [
    ("Life of Adam and Eve", "adam_and_eve.txt"),
    ("Golden Legend", "golden_legend.txt"),
    ("Apocryphal New Testament", "apocrypha_wake.txt"),
    ("Barlaam and Ioasaph", "barlaam.txt"),
    ("Roman Missal", "missal_roman_1865.txt"),
    ("Office of Holy Week", "office_holy_week_1875.txt"),
    ("York plays", "plays_york.txt"),
    ("Towneley plays", "plays_towneley.txt"),
    ("Chester plays", "plays_chester.txt"),
    ("N-town plays", "plays_ntown.txt"),
    ("Josephus, The Wars of the Jews", "josephus_wars.txt"),
]

WIN, STEP = 130, 65          # words per window, and how far the window moves

# Which book each part of the codex is mainly working from. Retrieval by rare
# words alone is weak exactly where a folio is a list of abstract nouns -- the
# fall of Lucifer, the Trinity -- and those are the pages that read worst. So
# the part's own source is weighted up, which is not a guess: it is what the
# project's own write-up established about each part.
PART_SOURCE = {
    "I":    ["Life of Adam and Eve", "Chester plays", "York plays"],
    "II":   ["Life of Adam and Eve", "Golden Legend"],
    "III":  ["Apocryphal New Testament", "Golden Legend"],
    "IV":   ["Golden Legend", "Apocryphal New Testament"],
    "V":    ["Office of Holy Week", "Roman Missal", "Apocryphal New Testament"],
    "VI":   ["Apocryphal New Testament", "Office of Holy Week"],
    "VII":  ["Golden Legend", "Barlaam and Ioasaph", "Josephus, The Wars of the Jews"],
    "VIII": ["Golden Legend"],
    "IX":   ["Apocryphal New Testament", "Golden Legend"],
    "X":    ["Golden Legend", "Chester plays"],
}
BOOST = 1.7


def part_of(pg, order):
    """Which part a folio falls in, by the manuscript's own reading order."""
    import ktbook
    idx = {p: i for i, p in enumerate(order)}
    bounds = sorted((idx.get(a, 0), n.split(".", 1)[0].strip())
                    for a, n, _ in ktbook.PARTS)
    here = idx.get(pg, 0)
    name = bounds[0][1]
    for start, num in bounds:
        if here >= start:
            name = num
    return name


def windows():
    """Every book cut into overlapping windows of words."""
    out = []
    for label, fn in BOOKS:
        p = os.path.join(REF, fn)
        if not os.path.isfile(p):
            print("  (missing)", fn, file=sys.stderr)
            continue
        text = open(p, encoding="utf-8", errors="replace").read()
        text = re.sub(r"\s+", " ", text)
        w = text.split(" ")
        for i in range(0, max(1, len(w) - WIN // 2), STEP):
            chunk = " ".join(w[i:i + WIN]).strip()
            if len(chunk) > 200:
                out.append((label, i, chunk))
        print(f"  {label:32} {len(w):>8} words", file=sys.stderr)
    return out


def build():
    wins = windows()
    df = Counter()
    stems = []
    for _, _, chunk in wins:
        s = T.content(chunk)
        stems.append(s)
        df.update(s)
    n = len(wins)
    idf = {w: math.log(n / (1 + c)) for w, c in df.items()}
    inv = defaultdict(list)
    for i, s in enumerate(stems):
        for w in s:
            if df[w] < n * 0.08:        # a word in a twelfth of the corpus says nothing
                inv[w].append(i)
    pickle.dump({"wins": wins, "idf": idf, "inv": dict(inv), "n": n,
                 "size": [len(x) for x in stems]}, open(INDEX, "wb"))
    print(f"indexed {n} windows, {len(idf)} stems -> {INDEX}")


def load():
    if not os.path.isfile(INDEX):
        build()
    return pickle.load(open(INDEX, "rb"))


def hand():
    """The line-by-line English already made for each folio, by hand, against
    the sources. It is the best description of what a folio is about."""
    out = {}
    txt = open(TRANS, encoding="utf-8").read()
    for m in re.finditer(r"^## (\d{3}[rv])[^\n]*\n(.*?)(?=^## |\Z)", txt, re.M | re.S):
        pg, body = m.groups()
        eng = [re.sub(r"^\*\*\d+\*\*\s+", "", l).strip()
               for l in body.splitlines() if l.startswith("**")]
        out[pg] = " ".join(eng)
    return out


def retrieve(ix, text, k=3, prefer=()):
    """The windows that share the most unusual vocabulary with this folio."""
    s = T.content(text)
    score = Counter()
    for w in s:
        if w in ix["inv"]:
            hit = ix["inv"][w]
            if len(hit) > 400:          # too common to point anywhere
                continue
            g = ix["idf"].get(w, 0.0)
            for i in hit:
                score[i] += g
    # a window packed with rare words scores high on vocabulary alone; divide
    # by its own size so a real parallel beats a dense page of footnotes
    for i in list(score):
        score[i] /= math.sqrt(max(4, ix["size"][i]))
        if prefer and ix["wins"][i][0] in prefer:
            score[i] *= BOOST
    best, seen = [], set()
    for i, sc in score.most_common(60):
        label, pos, chunk = ix["wins"][i]
        key = (label, pos // (STEP * 6))        # one window per neighbourhood
        if key in seen:
            continue
        seen.add(key)
        best.append({"source": label, "score": round(sc, 1), "text": chunk})
        if len(best) >= k:
            break
    return best


def cited_verses(pg, vd, wide=2):
    note = K.note_for(pg)
    refs = L.refs_in(note) if note else []
    if not refs:
        return [], None
    out = []
    for (bk, ch, v), txt in L.passage(vd, refs, wide=wide):
        out.append({"ref": f"{bk} {ch}:{v}", "text": txt})
    return out, note


def run(only=None):
    import ktbook
    ix = load()
    vd = L.verses_dr()
    hd = hand()
    order = [p for p, _, _, _ in ktbook.folios()]
    pages = order if not only else [only]
    out = {}
    for i, pg in enumerate(pages, 1):
        cv, note = cited_verses(pg, vd)
        # the folio and its neighbours: one page of abstract nouns gives the
        # index almost nothing to go on, and the story runs across the leaves
        j = order.index(pg) if pg in order else -1
        ctx = " ".join(hd.get(order[x], "") for x in range(max(0, j - 1), min(len(order), j + 2))) \
            if j >= 0 else hd.get(pg, "")
        ret = retrieve(ix, ctx, k=4, prefer=PART_SOURCE.get(part_of(pg, order), ()))
        out[pg] = {"cited": cv, "retrieved": ret,
                   "note": (note or "").strip()[:400]}
        if i % 40 == 0:
            print(f"  {i}/{len(pages)}", file=sys.stderr, flush=True)
    if only:
        return out
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False)
    withc = sum(1 for v in out.values() if v["cited"])
    print(f"wrote {OUT}: {len(out)} folios, {withc} with a cited passage, "
          f"{len(out) - withc} on retrieval alone")


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["build", "show", "run"])
    ap.add_argument("folio", nargs="?")
    a = ap.parse_args(argv)
    if a.cmd == "build":
        build(); return 0
    if a.cmd == "show":
        d = run(only=a.folio)[a.folio]
        print("NOTE:", d["note"][:300], "\n")
        for c in d["cited"][:6]:
            print(f"  CITED  {c['ref']:22} {c['text'][:110]}")
        print()
        for r in d["retrieved"]:
            print(f"  {r['source']} ({r['score']})\n    {r['text'][:400]}\n")
        return 0
    run(); return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
