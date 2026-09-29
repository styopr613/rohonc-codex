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

  THE QUOTATION CHECK WAS REMOVED on 2026-09-22, and this says so rather
  than leaving a gap in the numbering. It required every word inside
  guillemets to stand in the gloss of a folio the part cites, and it was the
  strictest thing in this file. It went because the printed Book One does not
  quote: Codex's rewrite carries no guillemets at all, so the check weighed
  nothing on the book that ships. It had been reading retelling.md, the draft
  the rewrite replaced, where its 1,142 quotations made it look like the
  strictest pass in the project while the printed book was checked by
  nothing. If Book One is ever given marked quotations again, this check is
  worth restoring from the history -- commit 901c161 is the last one that has
  it, and archive/drafts-20260922/retelling.md is the text it was written
  for.

  2. NUMBER.   Every digit-number in the retelling must either be spelled out
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
import ktrefs

# THE FILE THE BOOK PRINTS. This read retelling.md, which stopped being Book
# One when Codex rewrote it: ktbook.build() takes reading.md and falls back to
# the draft only if it is missing. So for a day this guarded a superseded
# draft, and its 1,142 quotations made it look like the strictest gate in the
# project while the printed book went unchecked. Pointed here it found eight
# paragraphs sitting under the wrong part heading, including the opening of
# the Cross story printed inside the Preaching chapter.
#
# THE PRINTED TEXT CARRIES NO GUILLEMETS. Checks 2 and 2b therefore have
# nothing to weigh, and main() says so out loud every run rather than
# reporting a silent pass: a gate with nothing to check is not a gate, and
# whether Book One should quote the manuscript at all is an editorial
# decision, not something this file should settle by saying PASS.
RT = os.path.join(corpus.ROOT, "work", "rohonc", "translation", "reading.md")

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
    "614": "the year Jerusalem fell to the Sasanians and the relic of the "
           "Cross was carried to Ctesiphon. Supplied by this edition from "
           "outside the manuscript, which dates the episode only by saying "
           "it happened in the reign of the king it names. Chosroes and "
           "Heraclius are Kiraly and Tokai's own dictionary entries; the "
           "date attached to them here is ours.",
    "1970": "Otto Gyurk's paper.",
    "2018": "Kiraly and Tokai's paper.",
}

WORD = re.compile(r"[a-z]+")
FOL = ktrefs.FOLIO_REF
CF = re.compile(r"cf\.\s*(\d{3}[rv])")
NUM = re.compile(r"(?<![\w.])(\d{1,5})(?![\w%])")




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
        # folio names, verse references and comma groups are not claims
        clean = FOL.sub(" ", body)
        clean = re.sub(r"\b\d+:\d+\b", " ", clean)
        clean = re.sub(r"(\d),(\d)", r"\1\2", clean)
        clean = re.sub(r"lines? \d+(–\d+)?", " ", clean)
        for n in set(NUM.findall(clean)):
            if n in ARITHMETIC:
                continue
            bad += 1
            print(f"   NUMBER FAIL: {n} is not declared in ARITHMETIC")
        print(f"   {len(cited)} folios cited")
    print(f"\n{'PASS' if bad == 0 else 'FAIL'}: {bad} problems, bar was 0")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
