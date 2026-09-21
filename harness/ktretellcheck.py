"""Check the front half against the back half, and refuse it if they disagree.

The retelling is editorial prose. That is exactly why it needs a gate: the one
thing it must never do is say something at a resolution the folio text cannot
support. Three checks, and the bar for all three is declared here before any
run and is ZERO failures.

  1. RANGE.    Every folio cited inside a part must lie inside that part's own
               folio span, in manuscript order. A part that reaches into
               another part's folios is telling you the boundary is wrong or
               the sentence is. A deliberate reach elsewhere is written
               "cf. 028v" and is allowed, because it announces itself.

  2. QUOTE.    Every phrase in guillemets is a claim that the manuscript says
               this. Each of its content words must appear in the gloss of a
               folio the part cites. One word that is not there is a
               fabricated quotation, which is the worst thing this edition
               could contain. Guillemets and nothing else carry that claim --
               italics are for book titles and emphasis and are not checked,
               which is exactly why the two must not share a mark.

  3. NUMBER.   Every digit-number in the retelling must either be spelled out
               in the cited folios' gloss, or be listed in ARITHMETIC below
               as an editorial calculation, with its working. A number that is
               neither is an anchor that came from expectation.

    python3 ktretellcheck.py
"""
import os
import re
import sys

import corpus
import ktbook

RT = os.path.join(corpus.ROOT, "work", "rohonc", "translation", "retelling.md")

# Numbers the retelling states that the manuscript does not itself write.
# Each one is arithmetic this edition performed, and the working is here so a
# reader can refuse it.
ARITHMETIC = {
    "1593": "33 (traditional year of the Ascension) + 1560 (223v line 2, read) "
            "= 1593. The manuscript performs no addition; line 1 supplies the "
            "epoch, 'from the departure of the Lord Jesus Christ to the Father'.",
    "33": "the traditional year of the Ascension, supplied by this edition.",
    "13": "Revelation 13:18, a chapter-and-verse reference by this edition.",
    "18": "Revelation 13:18, a chapter-and-verse reference by this edition.",
    "5199": "the reading of 223v lines 9-10 written in digits: five thousand, "
            "and a hundred, and nine-ten, and nine.",
    "1560": "the reading of 223v line 2 written in digits: a thousand years, "
            "five hundred, and six-ten.",
    "441": "the number of folios in this edition.",
    "2": "part and folio counting.",
    "1970": "Otto Gyurk's paper.",
    "2018": "Kiraly and Tokai's paper.",
}

WORD = re.compile(r"[a-z]+")
FOL = re.compile(r"\b(\d{3}[rv])\b")
QUOTE = re.compile(r"«([^»]{4,400})»")
CF = re.compile(r"cf\.\s*(\d{3}[rv])")
NUM = re.compile(r"(?<![\w.])(\d{1,5})(?![\w%])")
STOP = set("""a an the and or but if then so that this these those there here
of to in on at by for from with into onto upon over under about as than when
while where who whom whose which what because since until before after again
also too very not no nor only own same such both each few more most other some
any all every is are was were be been being am do does did doing done have has
had having will would shall should may might must can could let it its they
them their he him his she her we us our you your i me my mine one two three
four five six seven eight nine ten thy thee thou ye unto said say says""".split())


import ktenglish as E   # ONE instrument. The retelling is checked against the
# gloss with exactly the machinery that checks the folio English against it:
# same accent folding, same alias table, same handling of Jew(ish) and of
# <suffix of divine name>. Two gates with two different stemmers would
# disagree about what the manuscript says, and then neither would mean
# anything.


def main(argv):
    fol = {pg: (pg, title, prose, lines) for pg, title, prose, lines
           in ktbook.folios()}
    order = [f[0] for f in ktbook.folios()]
    idx = {p: i for i, p in enumerate(order)}
    txt = open(RT, encoding="utf-8").read()
    bad = 0
    for m in re.finditer(r"^## ([^\n]+)\n\n### folios (\d{3}[rv])–(\d{3}[rv])\n"
                         r"(.*?)(?=^## |\Z)", txt, re.M | re.S):
        name, lo, hi, body = m.groups()
        span = range(idx[lo], idx[hi] + 1)
        print(f"== {name}")
        cited = sorted(set(FOL.findall(body)), key=lambda p: idx.get(p, 9999))
        xref = set(CF.findall(body))
        out = [p for p in cited if idx.get(p, -1) not in span and p not in xref]
        if out:
            bad += len(out)
            print(f"   RANGE FAIL: cites outside {lo}-{hi}: {' '.join(out)}")
        have = set()
        for p in cited:
            if p in fol:
                have |= E.stems(" ".join(fol[p][3]))
        for q in QUOTE.findall(body):
            miss = [w for w in sorted(E.stems(q))
                    if w not in STOP and w not in have]
            if miss:
                bad += 1
                print(f"   QUOTE FAIL: {q[:60]}...  not in gloss: {' '.join(miss)}")
        # folio names, verse references and comma groups are not claims
        clean = FOL.sub(" ", body)
        clean = re.sub(r"\b\d+:\d+\b", " ", clean)
        clean = re.sub(r"(\d),(\d)", r"\1\2", clean)
        clean = re.sub(r"lines? \d+(–\d+)?", " ", clean)
        for n in set(NUM.findall(clean)):
            if n in ARITHMETIC:
                continue
            bad += 1
            print(f"   NUMBER FAIL: {n} is neither in the gloss nor declared")
        print(f"   {len(cited)} folios cited, {len(QUOTE.findall(body))} quotations")
    print(f"\n{'PASS' if bad == 0 else 'FAIL'}: {bad} problems, bar was 0")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
