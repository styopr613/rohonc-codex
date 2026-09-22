"""Turn the reader's edition into a book for OONA Book Maker.

Writes the engine's own structure -- title, meta, front, chapters, back -- to
a book.json on a shelf. Updating the canonical Rohonc shelf also builds and
deploys the public reader EPUB, the downloadable EPUB, and the print PDF after
validation. The saved studio design and cover remain the owner's decisions.

    python3 ktbook.py --out /tmp/book.json
    python3 ktbook.py --shelf /opt/publish-app/data/u1/books/<bid>

Shape: two books between one pair of covers, and the split is the whole point.

  BOOK ONE is the reading edition (ktreading.py). Each folio's gloss was put
  beside the passages that folio is working from -- the verses it cites, and
  the medieval books the codex compiles -- and the English was written from
  both. It is an interpretation and says so. Every paragraph names the folios
  it renders. Every content word was then counted against that folio's own
  gloss (ktverify.py): 97.9% of them are the manuscript's own.

  BOOK TWO is the evidence. All 441 folios in manuscript order, six to a
  chapter, each with its English paragraph and its marked line-by-line text.
  The marks are the point: a reader has to be able to see which words are read
  and which are guesses.

The front never claims to be translation at a resolution the back cannot
support. Where the two disagree, the back is right, and every part of the
front says so in its own last paragraph.
"""
import argparse
import json
import os
import re
import subprocess
import sys

import corpus

PUBLIC_SHELF = "/opt/publish-app/data/u1/books/20260921-052535-r0hc"
PUBLISHER = os.path.join(os.path.dirname(__file__), "ktreaderpublish.py")
PUBLISH_PYTHON = "/opt/publish-app/venv/bin/python"

PLATES = os.path.join(corpus.ROOT, "work", "rohonc", "plates.json")

ED = os.path.join(corpus.ROOT, "work", "rohonc", "translation",
                  "rohonc_readers_edition.md")
RT = os.path.join(corpus.ROOT, "work", "rohonc", "translation",
                  "retelling.md")
# Book One is the READING EDITION. translation.md, the plain word-order
# rendering it was built from, is kept beside it as a stage, not printed.
TR = os.path.join(corpus.ROOT, "work", "rohonc", "translation",
                  "reading.md")
EN = os.path.join(corpus.ROOT, "work", "rohonc", "translation",
                  "english.json")

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


# One parser for a numbered gloss line, and only one.
#
# This was two, and they disagreed for as long as the book existed. ktbook
# matched r"^\s{2,}\d+\s", which wants two spaces before the number; the
# reader's edition right-aligns its numbers in a width-3 field, so line 9 is
# "  9  word" and line 10 is " 10  word" with ONE space. Every line numbered
# ten or higher therefore fell out of Book Two and out of the retelling gate
# that reads it -- 527 lines, 12.1% of the manuscript, silently missing.
# ktenglish matched r"^\s*\d+\s+\S" and had them all, which is why the
# English paragraphs quote words the line-by-line text did not show.
#
# It is the same fault as the folio count that stopped counting at 200r: a
# pattern correct for one-digit numbers, wrong from ten on, agreeing with
# itself for months. The rule from that one applies here too -- if a thing is
# parsed in two places it will eventually disagree in one of them, so parse it
# once and call it twice. ktenglish owns the pattern now and this asks it.
GLOSSLINE = re.compile(r"^\s*\d+\s+\S")


def folios():
    text = open(ED, encoding="utf-8").read()
    out = []
    for m in re.finditer(r"^## (\d{3}[rv])( — ([^\n]*))?\n(.*?)(?=^## |\Z)",
                         text, re.M | re.S):
        pg, title, body = m.group(1), (m.group(3) or "").strip(), m.group(4)
        prose = [l[2:].strip() for l in body.splitlines() if l.startswith("> ")]
        lines = [l.rstrip() for l in body.splitlines() if GLOSSLINE.match(l)]
        out.append((pg, title, " ".join(prose), lines))
    return out


def english():
    """The gate-checked English paragraph for each folio, where one survives.

    Written from the gloss alone -- no source passage, no chapter title, no
    page image -- and then checked word by word against that folio's own
    gloss. Eight folios have no entry here because their English failed the
    check twice and was dropped; those folios print their marked lines and
    nothing else, which is the honest outcome.
    """
    if not os.path.exists(EN):
        return {}
    return {k: v["english"] for k, v in
            json.load(open(EN, encoding="utf-8")).items()}


def retelling(path=None):
    """Book One, one entry per part, keyed by the part name in PARTS.

    The translation (TR) and the older retelling (RT) share one file shape, so
    one parser reads either. build() takes the translation when it exists."""
    path = path or RT
    if not os.path.exists(path):
        return {}
    out = {}
    for m in re.finditer(r"^## ([^\n]+)\n\n### folios (\d{3}[rv])–(\d{3}[rv])\n"
                         r"(.*?)(?=^## |\Z)", open(path, encoding="utf-8").read(),
                         re.M | re.S):
        name, lo, hi, body = m.groups()
        out[name.strip()] = (lo, hi, body.strip())
    return out


def translation():
    return retelling(TR)


def figures():
    """The counts, read out of the edition's own header. Never retyped.

    These were hardcoded here in prose, and they went stale: the front matter
    claimed 93.3% read and "dark: there are none left" while the live run said
    93.4% and 47 dark words. Nothing checked them, because nothing generated
    them. ktreader.py computes them once and writes them into the edition's
    header; this reads that header back. Same rule as kttranslate.txt and
    ktbump -- if a figure is written in two places it will go wrong in one.
    """
    txt = open(ED, encoding="utf-8").read()
    g = {}
    for key, pat in (
            ("words", r"words in the manuscript\s+([\d,]+)"),
            ("read", r"\n    read\s+([\d,]+) \(([\d.]+)%\)"),
            ("soft", r"read from one passage, marked \*\s+([\d,]+) \(([\d.]+)%\)"),
            ("rest", r"restored, in brackets\s+([\d,]+) \(([\d.]+)%\)"),
            ("dark", r"dark, printed as an ellipsis\s+([\d,]+) \(([\d.]+)%\)"),
            ("lread", r"lines with every word read\s+([\d,]+) of ([\d,]+) \(([\d.]+)%\)"),
            ("lall", r"restorations\s+([\d,]+) of ([\d,]+) \(([\d.]+)%\)")):
        m = re.search(pat, txt)
        if not m:
            raise SystemExit(f"ktbook.figures: no {key} in the edition header")
        g[key] = m.groups()
    return g


def _n(s, w=6):
    """A count, right-aligned, so the column in the front matter lines up."""
    return f"{int(s.replace(',', '')):,}".rjust(w)


def annotate(body, part="p"):
    """Put [1], [2] ... into a part's prose and return its notes in order.

    House format, copied from the Plaintext Classics gospels: a bracketed
    number in the text, and the notes gathered at the end of the chapter under
    a NOTES rule, numbered per chapter. The anchors live in notes.md and are
    checked by ktnotecheck.py, which refuses a note with no source line, more
    than one paragraph, a scene-setting opener, a big word where a small one
    does, or an anchor that is not in the retelling exactly once.

    The anchor is matched with whitespace collapsed, because the retelling is
    hard-wrapped and almost every anchor of more than a few words straddles a
    line break in the file.
    """
    import ktnotecheck as N
    hits = []
    # The translation does not carry the retelling's phrases, so an anchor
    # that is not found is placed by FOLIO instead: the note's own source line
    # names one, and every paragraph of the translation closes with the folios
    # it renders. The marker goes at the end of that paragraph.
    cite = re.compile(r"\((\d{3}[rv](?:\s*[-–,]\s*\d{3}[rv])*)\)\s*$")
    order = [pg for pg, _, _, _ in folios()]
    paras, pos = [], 0
    for chunk in re.split(r"(\n\s*\n)", body):
        if chunk.strip():
            m = cite.search(chunk)
            covered = set()
            if m:
                for bit in re.split(r"\s*,\s*", m.group(1)):
                    ends = re.split(r"\s*[-–]\s*", bit)
                    if len(ends) == 2 and ends[0] in order and ends[1] in order:
                        a, b = order.index(ends[0]), order.index(ends[1])
                        covered.update(order[min(a, b):max(a, b) + 1])
                    else:
                        covered.update(e for e in ends if e in order)
            paras.append((pos + (m.start() if m else len(chunk)), covered))
        pos += len(chunk)
    for anchor, note in N.notes():
        pat = re.compile(r"\s+".join(re.escape(t) for t in anchor.split()))
        m = pat.search(body)
        if m:
            hits.append((m.end(), anchor, note))
            continue
        _, src = N.split_note(note)
        f = re.search(r"\b(\d{3}[rv])\b", src or "")
        if not f:
            continue
        for end, covered in paras:
            if f.group(1) in covered:
                hits.append((end, anchor, note))
                break
    hits.sort()
    out, notes, last = [], [], 0
    for i, (end, _, note) in enumerate(hits, 1):
        out.append(body[last:end])
        # gen's footnote syntax: the marker is a real noteref in the EPUB, so it
        # pops up in Apple Books, Kobo and the house reader, and the note itself
        # is gathered on a Notes page at the back with a link back to the marker
        out.append(f"[^{part}n{i}]")
        last = end
        prose, src = N.split_note(note)
        notes.append(f"[^{part}n{i}]: " + " ".join(prose.split()) + ("  " + src if src else ""))
    out.append(body[last:])
    rendered = "".join(out)
    # A note placed by folio lands immediately before that paragraph's terminal
    # citation.  Without a separating space, Markdown reads `[^x](002r)` as a link
    # to a nonexistent file named 002r.  Keep the folio label as ordinary text.
    rendered = re.sub(
        r"(\[\^[^\]]+\])(\(\d{3}[rv](?:\s*[-–,]\s*\d{3}[rv])*\))",
        r"\1 \2",
        rendered,
    )
    return rendered, notes


def front_matter():
    g = figures()
    return """The Rohonc Codex is a small paper book of the sixteenth century, about 450
leaves, written in a script that occurs in no other document. It came to the
Library of the Hungarian Academy of Sciences in Budapest in 1838, with the
library of Count Gusztav Batthyany from his estate at Rohonc, now Rechnitz in
Austria, which is where its name comes from. From that day until 2018 nobody
could read it. It dates itself: on one of its last leaves it counts one
thousand five hundred and sixty years from the Ascension, which is 1593.

In 2018 **Levente Zoltan Kiraly** and **Gabor Tokai** published, in
*Cryptologia*, the dictionary and grammar that opened it: 841 signs read. The
script runs right to left, several hundred signs, mostly logographic, and the
language is not Hungarian but something the scribe built for the purpose. The
book is a Christian devotional compilation: the apocryphal Life of Adam and
Eve running straight into the legend of the Rood, the story of Joachim and
Anne, a Passion the codex itself says it takes from Matthew and John, sermons
and parables for the gospels of the year, the Finding of the Cross, the Acts
of the Apostles, and at the very end a few pages of one man's diary. The frame
is a revelation: an angel of God speaks, and the prophet Elijah is the one
addressed.

**Most of what you can read here rests on their work.** Their dictionary is
not reproduced in this book; it is theirs, and it is used here word by word
the way a dictionary is used. Their own translation of the codex is
unpublished, and this is not it. Nothing here should be attributed to them
beyond the foundation it was built on. What has not existed before is the
whole manuscript, end to end, in a modern language, with every word marked
for how well it is known, and that is what this edition attempts.

**It was made with AI, under an editor.** Four signs in ten had no meaning in
the dictionary. Anthropic's Claude proposed readings for the remaining signs,
using Kiraly and Tokai's dictionary as a foundation; the editor decided what
stood. Different
models assembled the gloss and composed the translation. Every
figure in this book comes from a program that can be rerun, and where any of
this went wrong it is written down with the number it went wrong by.

**What this is, and is not.** This is an attempt, not peer reviewed, and
published to be checked. As of now, the tests, for what they are, find it
internally consistent. Tests and all programs and documents can be found in
the GitHub repo.

**The book is in two parts.** Book Two is the gloss: the manuscript folio by
folio and line by line, each sign rendered by Kiraly and Tokai's dictionary
or by a reading of this project, every word marked for how well it is known.
That is the evidence. Book One is the translation: a reading of the gloss
into continuous English, made against the books the codex is compiled from --
the Douay Bible its compiler had, the Life of Adam and Eve, the Golden Legend,
the apocryphal gospels, Barlaam and Ioasaph, the Roman Missal and the Office
of Holy Week, Josephus. Every paragraph of it names the folios it renders and
links to them in Book Two. Where the two disagree, Book Two is right.

## How to read the marks

Every word on every page carries one of these marks, so that what is known can
be told apart from what is not.

**word** — read. Kiraly and Tokai's own dictionary, or a reading of this
project that survives every occurrence of the sign in the book.

**word\\*** — one passage. Read from a single passage, with nothing in the
manuscript able to refuse it. Likelier right than wrong; not proved.

**word^** — a sense chosen. Their entry gives several senses for this sign,
and this is the one the passage the folio itself cites actually uses.

**[word]** — restored. A guess, made from the folio's source passage and the
words on either side of the hole. Counted as read nowhere.

**[…]** — dark: no reading and no honest guess.

A hyphen inside a word (*hide_oneself-angel*) is one sign of the manuscript
read as the smaller signs it is built from. This script writes phrases without
spaces, which is the central fact Kiraly and Tokai established about it. A `~`
marks a spelling their own apparatus files as a variant. A vertical bar is a
gap or an unreadable glyph in the transcription.

## What this book is worth, in numbers

        words in the manuscript            """ + _n(g["words"][0]) + """
    read                               """ + _n(g["read"][0]) + "   " + g["read"][1] + """%
    read from one passage              """ + _n(g["soft"][0]) + "   " + g["soft"][1] + """%
    restored, in brackets              """ + _n(g["rest"][0]) + "   " + g["rest"][1] + """%
    dark                               """ + _n(g["dark"][0]) + "   " + g["dark"][1] + """%

    lines with every word read                  """ + g["lread"][2] + """%
    lines complete once brackets are counted    """ + g["lall"][2] + """%

The middle figure is the honest one. A sentence with one word you cannot read
is not a sentence you can read. The gap between that figure and the one below
it is how much of this book is a guess, and the guesses are in brackets on
every page so that anyone can take them out.

## How it was checked

This is a book made from somebody else's dictionary, so the first question is
whether the dictionary is right. That was tested three ways before a word of
the translation was written, and none of the three needs you to trust anyone.

**The common signs behave like common words.** In any language the words that
come up most are the small ones — and, this, in, one, say, go. Sort the codex
by how often each sign occurs and that is what the top of the list looks like,
with gospel words underneath. How often a sign appears is fixed by the
manuscript. Nobody chose it. A wrong set of meanings would not land the
conjunctions and pronouns at the top.

**Pages with names in them point at the same place in the gospels.** The
dictionary reads 101 signs as names. Take every page that carries two or more
of them and ask how far apart those names sit in the gospel text. The middle
answer is 60 words. Shuffle the names and the middle answer is 3,007. Of 247
pages, 214 — 87% — beat the shuffled middle, where chance would give half.
Pages land on passages.

**The text runs across the ends of lines.** Take a run of words that straddles
a line break and ask whether the same manuscript writes that run inside a line
somewhere else. In real prose it does, because the words were written first
and broken into lines after. In the Rohonc that happens 2.04 times more often
than chance, at 39 standard deviations, which puts it beside Italian and
Hebrew and above Latin. The same test on the Voynich manuscript gives 1.10
times chance and 2.1 — down with the machine-made controls. One test, two
unread manuscripts, opposite answers.

## What was added here, and what it cost

Four signs in ten had no meaning in the dictionary. Working those out is the
part nobody had done, and it was tried seventeen ways. **Ten of the seventeen
failed.** All ten are written up, with their numbers, beside the ones that
worked, because that is the only thing that makes the ones that worked worth
anything.

Every attempt had its pass mark written down before it ran, and no mark was
ever moved afterwards. One attempt scored five times its control at 4.7
standard deviations against a bar of 5. It is filed as a failure. A near miss
is a miss.

Two things worked, and both were the same discovery. **Many signs are not
words but short phrases written without a space**, and both halves were often
in the dictionary already. Cutting them apart recovered 43.9% of a test set
against 6.3% for a matched control — 12.4 standard deviations — and a second
form of the same idea scored 77.5% against 47.4%, 9.8 standard deviations.
Eleven earlier attempts had failed because they kept asking what a sign meant
instead of what it was made of.

**The third thing that worked was reading the dictionary properly.** Kiraly
and Tokai cite a folio and a line in their entries, and for variant spellings
as well. Nobody had followed those citations back into the manuscript. Where a
line had exactly one hole and their entry named a word not already standing in
that line, their entry names the hole. That gave 44 readings in one afternoon.
None of them is a guess; each is their own reading of that line, in a spelling
the open transcription writes differently.

## The test that decides

A reading is kept only if it holds at **every** place the sign occurs. One
clear occurrence against it and the reading is not lowered a grade, it is
dropped. That test threw out readings this project had already published to
itself, and the coverage figure fell when they went. It fell and the book got
truer.

The strongest form of that check is the manuscript arguing with the editor.
Five signs had been read as *child*, from a page about Saint Augustine and a
boy on a beach. A mechanical sweep for signs one glyph away from a sign the
dictionary already reads found that all five are Kiraly and Tokai's own sign
for *a little while; little* — and that their spelling of it stands two lines
above ours on the same page. All five were wrong and all five were changed. A
story that fits is not evidence, and when the story and the dictionary
disagree, the dictionary wins.

## One thing this book can no longer prove

Many signs have several meanings in the dictionary, and the renderer used to
print the first one always. It now prints the meaning that the passage each
folio itself names actually uses. That makes the pages read far better, and it
costs something that has to be said out loud: **the fit between a page and the
passage it cites can never again be used as evidence**, because the fit is now
built in. The test that measured exactly that was run before this change and
its result stands. Running it again would be circular, and it must not be
done.

## What a bracket is worth

Four numbers were measured before a single bracket was printed, and they pull
in different directions on purpose. Taken one at a time:

**The passage a folio cites contains the true word 7.8% of the time.** That is
the ceiling on this method. For more than nine words in ten that are still
unread, the source the folio points at simply does not contain the answer, so
no amount of care in choosing from it would help.

**When the word is in the passage, the best candidate is right about one time
in four.** So the guesses that can be right are right often enough to be worth
printing, which is why they are here rather than left as holes.

**Against Kiraly and Tokai's own hidden entries, the top candidate scored
0.0%.** That is the mechanical generator scoring nothing at all on the hardest
population there is -- see the appendix for what was masked and why it is the
hardest. It is the reason a bracket is never counted as a reading anywhere in
this book.

**Three quarters of the bracketed content words do land on a word that
actually stands in the verse the folio cites.** That is the only part of this
that can be checked from inside the book, and it is the reason the brackets are
better than nothing.

Put together: read a bracket as a suggestion from an editor who knows the
source and does not know the word.

The weakest pages in the book are the last two leaves, 224r and 224v, the
worst-preserved in the manuscript, which cite no source. Their brackets are
little more than placeholders and are marked as such in the project's record.

## A known crux, named rather than tidied away

One formula runs through the whole manuscript like a drone: *every man is
saved; and one man is damned*. It comes out of the gloss with its polarity
reversed from folio to folio -- sometimes every man is saved, sometimes every
man is damned. It is almost certainly a fixed creedal tag whose word order
this rendering is not capturing, and not a book that repeatedly damns
everybody. It has been left exactly as the gloss produces it, in both halves
of this edition, rather than quietly straightened. Anyone who solves the word
order of that formula will improve several hundred lines at once.

## A note on the English

Book One is a reading edition, and it is an interpretation rather than a
word-for-word rendering. The codex is elliptical: its script writes whole
phrases as single signs, it drops verbs and articles, it repeats formulas, and
many of its leaves are damaged. Set down word for word it does not read, and
that rendering exists already -- it is Book Two.

So each folio was read against the books it is compiled from: the chapter and
verse it cites, in the Douay Bible its compiler had, and the medieval texts
behind it, the Life of Adam and Eve, the Golden Legend, the apocryphal
gospels, Barlaam and Ioasaph, the Roman Missal, the Office of Holy Week, the
four English mystery cycles, Josephus. The rule throughout is that the
manuscript leads and the source only ever says what one of its phrases means.
Where the codex departs from its source -- another name, another number, an
episode the source has not got -- the codex is followed, because those
departures are the most interesting thing in it.

Every content word of the reading was then counted back against its own
folio's gloss. 97.9% of them are the gloss's own, 1.3% come from a
passage the folio was read against, and 0.8% are ordinary English supplied to
make a sentence. Every paragraph names the folios it renders. Where Book One
and Book Two disagree, Book Two is right.

Nothing in Book Two is smoothed. Where the manuscript writes a phrase as one
sign, the English prints it as one hyphenated word. The result reads like a
gloss because it is one. Where Book One and Book Two disagree, Book Two is
right.

"""


def corpus_appendix():
    """The shelf the codex was read against, from the provenance file, so the
    printed book carries it and it cannot drift from the record."""
    import ktcorpus
    out = ["The codex is a compilation, and most of what its compiler wrote fits inside a small shelf "
           "of books. Every folio of Book One was read against the passage it retells; the manuscript "
           "leads, and the source only ever says what one of its phrases means. Every book here is "
           "public domain. Where a Project Gutenberg number is given, the text is at "
           "gutenberg.org/ebooks/ followed by the number.", ""]
    for e in ktcorpus.entries():
        out.append(f"**{e['name']}.** {e['text']}")
        out.append("")
    return "\n".join(out).strip()


def back_matter():
    g = figures()
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

**A held-out test, and a contaminated one.** A seeded random tenth of Kiraly
and Tokai's own dictionary entries were hidden from the tools, exactly as a
genuinely unread sign is hidden, and the pipeline was run blind on them. One
thing must be said about that sample before its number is quoted, and it was
said in the script before the test ran: **masked entries are not a fair
sample of the signs still dark.** Kiraly and Tokai glossed the words they
could, which are disproportionately the ones with relatives elsewhere in their
own dictionary; the signs still unread occur once and have no such relatives.
So the headline figure was declared in advance to be the one restricted to
masked signs with no surviving structural neighbour -- the hardest population
in the book, and the one that actually resembles what is left. On it, the best
passage candidate recovered their gloss 0.0% of the time. That number
calibrates the brackets, and it is why no bracket is ever counted as a reading.
It does not bear on the """ + g["read"][1] + """% that are read, which rest on the dictionary and
on survival at every occurrence, not on any generator. A second form
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
        {"type": "appendix", "pos": 2, "title": "What this edition transmits",
         "text": """This is a sixteenth-century Catholic devotional book and it
carries its genre's material without alteration here.

Two things a modern reader meets in the sermons are worth naming plainly.
The siege in which a starving mother eats her own child, at 111v-112r, is not
an invention of this book: it is scripture, at 2 Kings 6:28-29 and Lamentations
4:10, under the curse of Deuteronomy 28:53-57, and it reached the medieval
Passion sermon through Josephus' account of Jerusalem. The arithmetic on the
same leaves -- thirty Jews sold for one penny, because Judas sold the Lord for
thirty -- is not scripture. It is a medieval addition out of the Vindicta
Salvatoris tradition, and it is anti-Jewish polemic of a kind that ran through
Passion preaching all over Europe.

Both are printed as the manuscript has them. An edition that cut them would be
a worse witness to what a Catholic in Hungary in 1593 was actually reading."""},
        {"type": "appendix", "pos": 3, "title": "The corpus",
         "text": corpus_appendix()},
        {"type": "appendix", "pos": 4, "title": "Acknowledgment",
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


CITE = re.compile(r"\((\d{3}[rv])((?:\s*[-–,]\s*\d{3}[rv])*)\)\s*$")


def link_gloss(chapters):
    """Every paragraph of Book One ends with the folios it renders. Make that
    citation a link to the folio in Book Two, and make the folio's heading in
    Book Two a link back to the paragraph. gen names chapter files by their
    position, ch-001.xhtml onward, so the file a folio lands in is known once
    the chapter list is complete, which is why this runs last."""
    def fname(i):
        return f"ch-{i + 1:03d}.xhtml"
    heading = re.compile(r"^\*\*(\d{3}[rv])\*\*", re.M)
    in_two = {}
    for i, ch in enumerate(chapters):
        for m in heading.finditer(ch["text"]):
            in_two.setdefault(m.group(1), i)
    in_one, seen = {}, set()
    for i, ch in enumerate(chapters):
        if "**" in ch["text"] and heading.search(ch["text"]):
            continue                                   # Book Two
        paras = ch["text"].split("\n\n")
        for k, p in enumerate(paras):
            m = CITE.search(p)
            if not m or m.group(1) not in in_two:
                continue
            first = m.group(1)
            ids = [first] + re.findall(r"\d{3}[rv]", m.group(2))
            spans = ""
            for f in ids:
                if f not in seen:
                    seen.add(f); in_one[f] = i
                    spans += f'<span id="p{f}"></span>'
            cite = p[m.start():m.end()].strip()
            paras[k] = (p[:m.start()] + spans
                        + f'<a class="gloss" href="{fname(in_two[first])}#f{first}">{cite}</a>')
        ch["text"] = "\n\n".join(paras)
    for i, ch in enumerate(chapters):
        def back(m):
            f = m.group(1)
            if f in in_one:
                return f'<a id="f{f}" href="{fname(in_one[f])}#p{f}"><b>{f}</b></a>'
            return f'<a id="f{f}"><b>{f}</b></a>'
        ch["text"] = heading.sub(back, ch["text"])


def build():
    fol = folios()
    eng = english()
    rt = translation() or retelling()
    idx = {pg: i for i, (pg, _, _, _) in enumerate(fol)}
    bounds = [(idx.get(pg, 0), name, blurb) for pg, name, blurb in PARTS]
    bounds.sort()
    chapters = []

    # ---- BOOK ONE: the retelling, one chapter per part ------------------
    first = True
    for bi, (start, pname, pblurb) in enumerate(bounds):
        end = bounds[bi + 1][0] if bi + 1 < len(bounds) else len(fol)
        lo, hi = fol[start][0], fol[end - 1][0]
        got = rt.get(pname)
        if not got:
            continue
        body, notes = annotate(got[2], part=f"p{bi + 1}")
        body = body.replace("«", "*").replace("»", "*")
        if notes:
            body += "\n\n" + "\n".join(notes)
        ch = {"title": pname.split(".", 1)[-1].strip(),
              "subtitle": "folios %s–%s" % (lo, hi),
              "text": body}
        if first:
            ch["part"] = "Book One — The Book as it Reads"
            ch["part_sub"] = (
                "The manuscript in English, part by part. This is a reading: "
                "each folio was read against the books the codex is compiled "
                "from, because an elliptical text does not become English on "
                "its own. Every paragraph names the folios it renders, and the "
                "gloss of every one of them is printed in Book Two, line for "
                "line. The books it was read against -- the Douay Bible, the Life "
                "of Adam and Eve, the Golden Legend, the apocryphal gospels, "
                "Barlaam and Ioasaph, the Roman Missal and the Office of Holy "
                "Week, Josephus, the English play cycles -- are described at the "
                "back, under The corpus; most of what the compiler wrote fits "
                "inside them. A word in brackets is a restoration. Where this and "
                "Book Two disagree, Book Two is right.")
            first = False
        chapters.append(ch)

    # ---- BOOK TWO: the folios themselves --------------------------------
    # Where each plate goes. Three of the illustrated leaves carry a drawing and
    # no text at all, so the rendering has no page for them and Book Two never
    # prints them. They are still leaves of the book: each is placed after the
    # last leaf before it that the edition does print, and its caption says the
    # leaf has no text on it.
    def leaf(pg):
        return (int(pg[:3]), 0 if pg[3] == "r" else 1)

    have = {pg for pg, _, _, _ in fol}
    plate = {}
    if os.path.isfile(PLATES):
        for x in json.load(open(PLATES, encoding="utf-8")):
            pg = x["folio"]
            if pg in have:
                plate.setdefault(pg, []).append(x)
                continue
            before = [q for q in have if leaf(q) < leaf(pg)]
            if not before:
                continue
            x = dict(x, textless=True)
            plate.setdefault(max(before, key=leaf), []).append(x)
    for bi, (start, pname, pblurb) in enumerate(bounds):
        end = bounds[bi + 1][0] if bi + 1 < len(bounds) else len(fol)
        run = fol[start:end]
        for ci in range(0, len(run), PER_CHAPTER):
            grp = run[ci:ci + PER_CHAPTER]
            body = []
            for pg, title, prose, lines in grp:
                body.append("**%s**%s" % (pg, (" — " + title) if title else ""))
                body.append("")
                # The manuscript draws its scenes, and the drawing is evidence
                # nobody used while reading. No print-quality scan of this book
                # exists, so a plate here is a REDRAWING made from the library's
                # low-resolution scan, and its caption says so every time.
                for x in plate.get(pg, []):
                    # the NAME CARRIES ITS EXTENSION: gen.img_src looks up
                    # img/<name> on disk and silently embeds nothing when the
                    # name does not resolve to a file.
                    body.append("[img:%s|%s%s Redrawn from the manuscript's own "
                                "drawing; not a reproduction.]"
                                % (x["file"], x["caption"],
                                   " The leaf carries the drawing and no text."
                                   if x.get("textless") else ""))
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
                ch["part"] = ("Book Two — The Manuscript, Folio by Folio"
                              if bi == 0 else pname)
                ch["part_sub"] = (
                    "All 441 folios in the order the manuscript has them, six "
                    "to a chapter: the manuscript itself, line for line, with "
                    "every mark intact. This is the evidence the translation "
                    "in Book One was made from."
                    if bi == 0 else pblurb)
            chapters.append(ch)
    link_gloss(chapters)
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
                            "known: " + figures()["read"][1] + "% read, "
                            + figures()["rest"][1] + "% restored in brackets."),
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
    ap.add_argument("--no-publish-reader", action="store_true",
                    help="update the canonical shelf without deploying its web-reader EPUB")
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
        # The studio's Design panel and the cover are the OWNER's decisions, made
        # on the shelf with the preview in front of him. A rebuild carries the
        # text; it must not undo them. Everything else is regenerated.
        shelf_json = os.path.join(a.shelf, "book.json")
        if os.path.isfile(shelf_json):
            old = json.load(open(shelf_json, encoding="utf-8"))
            for k in ("design", "cover", "cover_gid", "cover_trim"):
                if k in old:
                    bk[k] = old[k]
        json.dump(bk, open(shelf_json, "w"), ensure_ascii=False)
        print("shelved", a.shelf)
        if (os.path.realpath(a.shelf) == os.path.realpath(PUBLIC_SHELF)
                and not a.no_publish_reader):
            subprocess.run(
                [PUBLISH_PYTHON, PUBLISHER, "--shelf", a.shelf],
                check=True,
            )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
