"""Turn the reader's edition into a book for OONA Book Maker.

Writes the engine's own structure -- title, meta, front, chapters, back -- to
a book.json on a shelf. It does not build, design or publish anything; the
studio does that, with a person looking at the preview.

    python3 ktbook.py --out /tmp/book.json
    python3 ktbook.py --shelf /opt/publish-app/data/u1/books/<bid>

Shape: 441 folios in their manuscript order, gathered into chapters of six,
under named parts. Each folio keeps its heading, its English paragraph and its
marked text, because the marks are the point -- a reader has to be able to see
which words are read and which are guesses.
"""
import argparse
import json
import os
import re
import sys

import corpus

ED = os.path.join(corpus.ROOT, "work", "rohonc", "translation",
                  "rohonc_readers_edition.md")

# Part boundaries, by the folio each part opens on, in manuscript order.
PARTS = [
    ("004v", "I. The Fall of Lucifer, and the Life of Adam and Eve",
     "The book does not open with a gospel. It opens with the apocryphal "
     "Life of Adam and Eve, and the episode that identifies it is here: God "
     "commands the angels to bow to Adam, and Lucifer refuses."),
    ("008r", "II. From the Flood to the House of David",
     "Noah, Abraham and Isaac, and the count of the years down to David."),
    ("016r", "III. Joachim and Anne, and the Birth of Christ",
     "The Protevangelium and the Golden Legend: the offering refused, the "
     "angel in the wilderness, the golden gate, the Annunciation, the manger."),
    ("022v", "IV. The Twelve Signs of His Coming",
     "A numbered list of the signs that attended the Nativity, told twice."),
    ("029r", "V. The Passion",
     "The longest section of the book, and the one whose sources it names: "
     "Matthew and John, with the supper, the garden, Pilate, Herod, the "
     "crown of thorns, the cross, and Longinus."),
    ("053r", "VI. The Burial, the Resurrection, and the Forty Days",
     "The three Marys, the empty tomb, the road to Emmaus, Thomas, and the "
     "Ascension."),
    ("064r", "VII. The Preaching: the Sermons and the Parables",
     "The largest part of the manuscript by far. Sermons on the gospels of "
     "the year, with the parables told at length: the good Samaritan, the "
     "prodigal son, the rich man and Lazarus, the unjust steward, the "
     "talents, the lost sheep and the lost coin."),
    ("183r", "VIII. The Finding and the Exaltation of the Cross",
     "The legend as the Golden Legend tells it: Chosroes on his tower of "
     "gold, and Heraclius turned back at the gate of Jerusalem until he "
     "puts off his purple and his shoes and carries the Cross barefoot."),
    ("215r", "IX. The Acts of the Apostles",
     "Stephen's testimony and his stoning, Gamaliel and Nicodemus, and the "
     "road to Damascus."),
    ("221r", "X. The Last Things, and the Writer's Own Days",
     "A table of portents by weekday; two dates, one of them the age of the "
     "world at the Nativity as the Roman Martyrology gives it; and on 222v "
     "a calendar in which the sign Kiraly and Tokai gloss as 'the name of "
     "the author' stands six times. It is the only page in the book about "
     "the man who made it."),
]
PER_CHAPTER = 6


def folios():
    text = open(ED, encoding="utf-8").read()
    out = []
    for m in re.finditer(r"^## (\d{3}[rv])( — ([^\n]*))?\n(.*?)(?=^## |\Z)",
                         text, re.M | re.S):
        pg, title, body = m.group(1), (m.group(3) or "").strip(), m.group(4)
        prose = [l[2:].strip() for l in body.splitlines() if l.startswith("> ")]
        lines = [l.rstrip() for l in body.splitlines()
                 if re.match(r"^\s{2,}\d+\s", l)]
        out.append((pg, title, " ".join(prose), lines))
    return out


def front_matter():
    return """The Rohonc Codex is a book of about 450 leaves in an unknown
script, in the library of the Hungarian Academy of Sciences. Nobody could read
it for two hundred years.

In 2018 **Levente Zoltan Kiraly** and **Gabor Tokai** published, in
*Cryptologia*, the dictionary and grammar that broke it. The script is a
right-to-left system of several hundred signs, mostly logographic, and the
language is not Hungarian but something the scribe built for the purpose. The
book is a Christian devotional compilation of the sixteenth century: the
apocryphal Life of Adam and Eve, the legend of the Rood, the story of Joachim
and Anne, a Passion, sermons and parables for the gospels of the year, the
Finding of the Cross, and the Acts of the Apostles.

**Everything you can read here rests on their work.** Roughly three quarters
of the words below are theirs or follow directly from theirs. Their own
translation of the manuscript has never been published; this is not it, and
nothing here should be attributed to them except the dictionary and the
grammar, which are entirely theirs.

## How to read the marks

Every word on every page carries one of four marks, so that what is known can
be told apart from what is not.

| mark | meaning |
|---|---|
| `word` | **read.** Kiraly and Tokai's own dictionary, or a reading of this project that survives every occurrence in the book. |
| `word*` | **one passage.** Read from a single passage, with nothing in the manuscript able to refuse it. |
| `word^` | **a sense chosen.** Their entry gives several senses for this sign; this is the one the passage the folio itself cites actually uses. |
| `[word]` | **restored.** A guess, made from the folio's source passage and the words on either side. Counted as read nowhere. |
| `[…]` | dark. There are none left. |

A hyphen inside a word (`hide_oneself-angel`) is one sign of the manuscript
read as the smaller signs it is built from. This script writes phrases without
spaces, which is the central fact Kiraly and Tokai established about it. A `~`
marks a spelling their own apparatus files as a variant. A `|` is a gap or an
unreadable glyph in the transcription.

## What this book is worth, in numbers

    words in the manuscript            29,997
    read                               27,997   93.3%
    read from one passage                1,020    3.4%
    restored, in brackets                  980    3.3%
    dark                                     0    0.0%

    lines with every word read                  82.3%
    lines complete once brackets are counted    99.9%

The middle figure is the honest one. A sentence with one unreadable word in it
is not a sentence you can read, and 82.3% of the lines of this manuscript have
every word read. The gap between that and 99.9% is exactly how much of this
book is guesswork, and it is printed in brackets on every page so that anyone
can strip it out.

**What a bracket is worth, measured before any were printed.** On words as
rare as the ones left over, the passage a folio cites contains the true word
7.8% of the time, and when it is there the best candidate is right about one
time in four. Against Kiraly and Tokai's own hidden dictionary entries the top
candidate was right 0.0% of the time. What can be checked from inside the book
is that three quarters of the bracketed content words land on a word that
actually stands in the verse the folio cites. Read a bracket as a suggestion
from an editor who knows the source and does not know the word.

The weakest pages in the book are the last two leaves, 224r and 224v, the
worst-preserved in the manuscript, which cite no source. Their brackets are
little more than placeholders and are marked as such in the project's record.

## A note on the English

Nothing here is smoothed. Where the manuscript writes a phrase as one sign,
the English prints it as one hyphenated word. Where a sign has several senses
and the passage cannot choose between them, the first sense is printed. The
result reads like a gloss because it is one. The paragraph at the head of each
folio is a reading of that page into sentences; the numbered lines under it
are the manuscript itself, line for line, with the marks intact.
"""


def back_matter():
    return [
        {"type": "appendix", "pos": 0, "title": "How this was checked",
         "text": """Every figure in this book comes from a program that can be
rerun, and every claim that failed a test is written down with the number it
failed by.

**The method, in one paragraph.** Guess a sign from one passage where the
story is known, then look at every other place in the manuscript it occurs and
keep the guess only if it survives all of them. That is Kiraly and Tokai's own
method, and it is the only thing here that produces a reading rather than an
opinion. A sign that occurs once gets a guess and no test; a sign that occurs
often gets a guess and a real test. The rule written over the whole of it is:
**a story that fits is not evidence.**

**The control, because a method that cannot fail proves nothing.** Three
gates, each with its bar written down before it ran. The first two passed. The
third failed at 2.3 sigma against a declared bar of 5, and the bar was not
moved: the weaker claim it would have supported, that the rendering "reads
like the Bible", was withdrawn. A frequency-matched shuffle of this dictionary
already scores 70.6% on that test, so reading like the Bible is nearly free.

**What survives.** That the rendering reads like *the particular passage each
folio cites* — not the Bible in general — at 18.6 sigma against a control
where the folios are shuffled against their passages. That is the result the
whole book stands on.

**A held-out test, and a contaminated one.** A tenth of Kiraly and Tokai's own
dictionary entries were hidden and the full pipeline run blind on them. The
best passage candidate recovered their gloss 0.0% of the time. A second form
of the test had to be thrown away: the reader running it had spent the day
reading the dictionary, and flagged twelve of twenty-five sampled signs as
already seen. Those twelve scored 75%; the thirteen genuinely unseen scored
23.1%. A blind test run by someone who has read the dictionary is not blind.
The declared consequence was applied anyway, and sixty-nine readings were
downgraded a tier.

**Four of this project's own readings were overturned by its own tools**, and
each is corrected in place with the mistake named rather than quietly amended.
Forty more restorations were corrected by a sweep that looks for a guessed
word repeating a word already standing beside it in the line."""},
        {"type": "appendix", "pos": 1, "title": "What would prove this wrong",
         "text": """Three things could falsify large parts of this book, and
none of them is in the project's own hands.

**The source texts.** Half of the manuscript's sentences are close paraphrase
of a passage that exists in print. Anyone with the Douay-Rheims, the Golden
Legend, the Roman Missal and the mystery plays can take a folio, read the
passage it cites, and say whether the rendering is that passage or not. Where
it is not, the reading is wrong.

**Kiraly and Tokai's unpublished material.** Their grammar paper is not
published and their translation has never appeared. Either would settle a
large number of the choices made here, and would very likely overturn some of
them.

**A blind rederivation.** The judgment step in this work — a person looking at
a line and deciding what a sign means — has never been measured by anyone who
had not already read the dictionary. The project prepared that test, named it,
and could not run it honestly on itself. It is the cheapest and most damaging
external check available, and anyone may run it."""},
        {"type": "appendix", "pos": 2, "title": "Acknowledgment",
         "text": """The dictionary and the grammar of the Rohonc Codex are the
work of **Levente Zoltan Kiraly** and **Gabor Tokai**, published as "Cracking
the code of the Rohonc Codex", *Cryptologia* 42:4 (2018), 285-315, with
Kiraly's later paper on the book's theological character (2023). The
observation that the manuscript's repeated sequences break at the line, on
which the whole reading rests, is **Otto Gyurk's**, from 1970. **Benedek
Lang's** *The Rohonc Code: Tracing a Historical Riddle* (Penn State Press,
2021) is the history of the problem.

The transcription used here is the anonymous open transcription of 2014. The
page images are the Hungarian Academy of Sciences' own scan, used under its
terms for academic and educational purposes and not redistributed.

None of these people are responsible for anything in this edition."""},
    ]


def build():
    fol = folios()
    idx = {pg: i for i, (pg, _, _, _) in enumerate(fol)}
    bounds = [(idx.get(pg, 0), name, blurb) for pg, name, blurb in PARTS]
    bounds.sort()
    chapters = []
    for bi, (start, pname, pblurb) in enumerate(bounds):
        end = bounds[bi + 1][0] if bi + 1 < len(bounds) else len(fol)
        run = fol[start:end]
        for ci in range(0, len(run), PER_CHAPTER):
            grp = run[ci:ci + PER_CHAPTER]
            body = []
            for pg, title, prose, lines in grp:
                body.append("**%s**%s" % (pg, (" — " + title) if title else ""))
                body.append("")
                if prose:
                    # The paragraph was made into sentences while 1,087 words
                    # of the book still had no reading, and it keeps a gap at
                    # each of them. The lines below it do not. Print the gap
                    # as a plain ellipsis rather than the edition's [...],
                    # which means something stricter, and say so in the front
                    # matter rather than pretending the two agree.
                    body.append(prose.replace("[…]", "…"))
                    body.append("")
                if lines:
                    body.append("<pre>")
                    body.extend(l.replace("&", "&amp;").replace("<", "&lt;")
                                for l in lines)
                    body.append("</pre>")
                    body.append("")
            ch = {"title": "%s–%s" % (grp[0][0], grp[-1][0]),
                  "subtitle": grp[0][1] or "",
                  "text": "\n".join(body).strip()}
            if ci == 0:
                ch["part"] = pname
                ch["part_sub"] = pblurb
            chapters.append(ch)
    return {
        "title": "The Rohonc Codex",
        "subtitle": "The whole manuscript in English, folio by folio",
        "author": "an unknown hand, Hungary, sixteenth century",
        "design": {"theme": "classic", "dingus": "· · ·",
                   "note_marker": "bracket", "indent_first": False},
        "meta": {
            "notes_placement": "back", "notes_numbering": "book",
            "description": ("The Rohonc Codex rendered into English, all 441 "
                            "folios, on the dictionary and grammar Levente "
                            "Zoltan Kiraly and Gabor Tokai published in 2018. "
                            "Every word carries a mark saying how well it is "
                            "known: 93.3% read, 3.3% restored in brackets, "
                            "none left dark."),
            "rights": ("The manuscript is of the sixteenth century and is not "
                       "in copyright. The dictionary and grammar on which this "
                       "rendering depends are the work of Levente Zoltan "
                       "Kiraly and Gabor Tokai and are theirs; their own "
                       "translation of the codex is unpublished and this is "
                       "not it. The editorial matter and the English are this "
                       "edition's own."),
            "edition": "First edition",
        },
        "front": [{"type": "introduction", "pos": 0,
                   "title": "What this book is", "text": front_matter()}],
        "chapters": chapters,
        "back": back_matter(),
    }


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out")
    ap.add_argument("--shelf")
    a = ap.parse_args(argv)
    bk = build()
    nw = sum(len(c["text"].split()) for c in bk["chapters"])
    print(f"chapters {len(bk['chapters'])}   words {nw}   "
          f"parts {len({c.get('part') for c in bk['chapters'] if c.get('part')})}")
    for c in bk["chapters"][:3]:
        print("  ", c["title"], "|", c["subtitle"][:48], "|", c.get("part", ""))
    if a.out:
        json.dump(bk, open(a.out, "w"), ensure_ascii=False)
        print("wrote", a.out)
    if a.shelf:
        os.makedirs(os.path.join(a.shelf, "img"), exist_ok=True)
        json.dump(bk, open(os.path.join(a.shelf, "book.json"), "w"),
                  ensure_ascii=False)
        print("shelved", a.shelf)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
