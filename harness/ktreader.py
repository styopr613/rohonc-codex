"""THE READER'S EDITION: the whole manuscript as continuous marked text.

Two documents, two jobs. The deposit -- proposals.json, ktprov.py,
ktvarcheck.py, ktnull.py, ktrederive.py -- is strict: every reading typed,
sourced and attackable. This is the other one. A book with holes in it is not
a book, and a reader needs the text, so this prints every line of all 441
folios with the standard apparatus of a fragmentary edition.

THE MARKS, and they follow the convention every damaged classical text uses.

    word      read. Kiraly and Tokai's dictionary, a composition of their
              signs, a variant spelling their own apparatus records, or a
              reading this project checked at every occurrence.

    word*     read from one passage, with nothing in the book able to refuse
              it. Tier C and D. True more often than not; not proved.

    [word]    RESTORED. A guess, made from the folio's source passage and the
              words on either side of the hole. Tier G. Bracketed the way an
              epigrapher brackets a restored letter, and for the same reason.

    [...]     dark. No reading and no honest guess.

WHY THE DARK WORDS ARE NOT FILLED IN. It would be easy to print the best
candidate from the folio's cited passage in brackets and call the text
complete. Gate 4a in ktrederive.py measured what that candidate is worth:
against Kiraly and Tokai's own hidden entries, the top candidate from the
passage pool was correct 0.0% of the time, and the true word was anywhere in
the pool 5.4% of the time against a 4.6% control. A bracket filled from a
generator that is at chance is not a restoration, it is a decoration. So
those places get an ellipsis, which is what an editor prints when the papyrus
is gone.

    python ktreader.py            write the reader's edition
"""
import os
import re
import sys
from collections import Counter

import corpus
import ktaffix as A
import ktcross as K
import kttranslate as T

OUT = os.path.join(os.path.dirname(corpus.DATA), "work", "rohonc",
                   "translation", "rohonc_readers_edition.md")
TRANS = os.path.join(os.path.dirname(corpus.DATA), "work", "rohonc",
                     "translation", "rohonc_translation.md")

HEAD = """# The Rohonc Codex

### a reader's edition

Every line of all {folios} folios, in the order the manuscript has them.

The script is undeciphered. The dictionary that makes this possible is
**Levente Kiraly and Gabor Tokai's**, published at rechnitzer-kodex.hu, and
roughly three quarters of the words below are theirs or follow directly from
theirs. Their grammar paper is unpublished, so nothing here chooses between
the senses of a word that has several; the first sense is printed. This is not
their translation, which has never been published.

## How to read the marks

| mark | meaning |
|---|---|
| `word` | read |
| `word*` | read from one passage, with nothing in the book able to refuse it |
| `[word]` | **restored** -- a guess from the folio's source and its neighbours |
| `[...]` | dark: no reading, and no honest guess |

A hyphen inside a word (`hide_oneself-angel`) is one sign of the manuscript
read as the smaller signs it is built from -- this script writes phrases
without spaces, which is the central fact Kiraly and Tokai established about
it. A `~` marks a spelling their own apparatus files as a variant. A `|` is a
gap or an unreadable glyph in the transcription.

**Why the dark places are not filled in.** It would be easy to print a
plausible word in every bracket. The project measured what such a word is
worth: against Kiraly and Tokai's own hidden dictionary entries, the best
candidate drawn from a folio's cited passage was right **0.0%** of the time.
So the ellipsis stays. An edition that guesses everywhere is not more complete
than one that does not; it is only harder to check.

## What this edition is worth, in numbers

    words in the manuscript            {words}
    read                               {read} ({readpc:.1f}%)
    read from one passage, marked *    {soft} ({softpc:.1f}%)
    restored, in brackets              {rest} ({restpc:.1f}%)
    dark, printed as an ellipsis       {dark} ({darkpc:.1f}%)

    lines with every word read         {lread} of {lines} ({lreadpc:.1f}%)
    lines complete including
      restorations                     {lall} of {lines} ({lallpc:.1f}%)

The evidence for every single word is in `harness/proposals.json`, one entry
per sign, with its tier and the argument in full. `harness/ktprov.py` prints
where each reading came from and whether the manuscript itself can ever refuse
it. `harness/ktnull.py` and `harness/ktrederive.py` are the controls,
including the two that failed.

**Brackets are the measure of what is left to do.** Every time a source text
enters the corpus, or a formula turns up twice, some of them become plain
words. There are {rest} of them now.

---

"""


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    T.prop_ref.update(prop)
    prose = {}
    if os.path.exists(TRANS):
        txt = open(TRANS, encoding="utf-8").read()
        for m in re.finditer(r"^## (\d{3}[rv]) — ([^\n]*)\n(.*?)(?=^## |\Z)",
                             txt, re.M | re.S):
            pg, title, body = m.groups()
            para = [l.strip() for l in body.splitlines()
                    if l.startswith("**") and l.strip()]
            prose[pg] = (title, para)

    n = Counter()
    pages = []
    for p in doc:
        lines = []
        for i, ln in enumerate(p.lines, 1):
            out = []
            for run in ln:
                for t in run:
                    b = A.strip(t)[0]
                    k = T.kind(t, gl, seg, var, prop)
                    w = T.render_token(t, gl, seg, False, var, prop)
                    if k == "none":
                        out.append("[...]")
                        n["dark"] += 1
                    elif k == "guess":
                        out.append("[" + w.lstrip("°") + "]")
                        n["rest"] += 1
                    elif k == "prop" and prop[b][1] in ("C", "D"):
                        out.append(w.lstrip("?+") + "*")
                        n["soft"] += 1
                    else:
                        out.append(w.lstrip("+?"))
                        n["read"] += 1
                out.append("|")
            if out and out[-1] == "|":
                out.pop()
            s = " ".join(out)
            lines.append((i, s))
            ks = [T.kind(t, gl, seg, var, prop) for t in
                  [x for r in ln for x in r]]
            n["lines"] += 1
            n["lread"] += all(k not in ("none", "guess") for k in ks)
            n["lall"] += all(k != "none" for k in ks)
        pages.append((p.page, lines))

    w = n["read"] + n["soft"] + n["rest"] + n["dark"]
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(HEAD.format(
            folios=len(pages), words=w,
            read=n["read"], readpc=n["read"] / w * 100,
            soft=n["soft"], softpc=n["soft"] / w * 100,
            rest=n["rest"], restpc=n["rest"] / w * 100,
            dark=n["dark"], darkpc=n["dark"] / w * 100,
            lines=n["lines"], lread=n["lread"],
            lreadpc=n["lread"] / n["lines"] * 100,
            lall=n["lall"], lallpc=n["lall"] / n["lines"] * 100))
        for pg, lines in pages:
            title = prose.get(pg, ("", []))[0]
            f.write(f"\n## {pg}" + (f" — {title}" if title else "") + "\n\n")
            para = prose.get(pg, ("", []))[1]
            if para:
                f.write("> " + " ".join(
                    re.sub(r"\*\*\d+\*\*\s*", "", x) for x in para)[:1400] + "\n\n")
            for i, s in lines:
                f.write(f"{i:>3}  {s}\n")
    print(f"wrote {OUT}")
    print(f"  {len(pages)} folios, {w} words")
    print(f"  read {n['read']} ({n['read']/w*100:.1f}%), "
          f"one-passage {n['soft']} ({n['soft']/w*100:.1f}%), "
          f"restored {n['rest']}, dark {n['dark']} ({n['dark']/w*100:.1f}%)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
