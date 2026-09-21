"""ktsitecopy.py -- have an outside model write the prose of oona13.com/rohonc/.

    python3 ktsitecopy.py            # asks the model, writes ktsite_copy.json
    python3 ktsitecopy.py --show     # prints the current copy

The owner asked (2026-09-21) that the introduction and the web material be
written by DeepSeek rather than by the assistant that built the page, so the
page does not read in that assistant's voice. This script hands the model a
FACT SHEET assembled from the repository (figures parsed, never typed) and
asks for the prose only. ktsite.py then reads ktsite_copy.json and places
each piece. The figures on the page are still rendered by code from the
saved runs; the model is told which numbers it may use and must invent none.

Every piece is read back by a person before it goes up. The model is a
writer here, not a source.
"""
import argparse
import json
import os
import re
import sys

import ktor
import ktsite

MODEL = "deepseek/deepseek-v3.2"
EXTRA = {"reasoning": {"enabled": False}}
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ktsite_copy.json")

KEYS = ["tagline", "intro", "how_far", "tiers", "new_here_lead", "is_it_true",
        "card_reading", "card_dictionary", "card_tests", "card_method", "card_writeup",
        "card_data", "edition", "credit", "reading_lead", "dictionary_lead", "data_lead",
        "outside_lead", "credit_line", "card_script", "script_intro", "script_signs",
        "script_numerals", "script_phrases", "script_shuffle_lead", "script_marks",
        "script_plates"]


def fact_sheet():
    fig = ktsite.edition_figures()
    summary, ktn = ktsite.tests_summary()
    about, rows = ktsite.proposals()
    tiers = {}
    for r in rows:
        tiers[r["tier"]] = tiers.get(r["tier"], 0) + 1
    order = ktsite.folio_order()
    eng = json.load(open(os.path.join(ktsite.TR, "english.json"), encoding="utf-8"))
    n_eng = sum(1 for f, _ in order if eng.get(f, {}).get("english", "").strip())
    return f"""THE MANUSCRIPT
- The Rohonc Codex: a small paper book of the sixteenth century, about 450 leaves,
  kept at the Library of the Hungarian Academy of Sciences in Budapest.
- Written in a script that occurs in no other document. Right to left, several
  hundred signs, mostly one sign per word or phrase.
- What it contains (established by Kiraly and Tokai): the apocryphal Life of Adam
  and Eve running into the legend of the Rood; the story of Joachim and Anne; a
  Passion the codex itself says it takes from Matthew and John; sermons and
  parables for the gospels of the year; the Finding of the Cross; the Acts of the
  Apostles; and at the end a few pages of one man's diary. The frame is a
  revelation: an angel of God speaks and the prophet Elijah is the one addressed.

KIRALY AND TOKAI (credit them by name, always)
- Levente Zoltan Kiraly and Gabor Tokai, "Cracking the code of the Rohonc Codex",
  Cryptologia 42:4 (2018). A dictionary of {ktn} signs and the grammar.
- They put their transcription online at rechnitzer-kodex.hu so their claims could
  be checked. Their own translation of the codex is unpublished; nothing on this
  site is it.
- Roughly three quarters of the words this project reads are theirs or follow
  directly from theirs.

WHAT THIS PROJECT DID
- Started from their dictionary, tested it, and extended it: read signs their
  dictionary leaves undefined, checked every reading at every place the sign
  stands in the book, and rendered the whole manuscript into English with every
  word marked by how well it is known.
- The central discovery: many signs are short phrases written without a space,
  and both halves were already in the dictionary. Cutting them apart, confirmed
  independently of their glosses at 12.4 and 9.8 sigma against matched controls,
  produced 1,282 readings their published dictionary does not contain.
- The English for each folio was written from that folio's gloss alone: no
  source passage, no chapter title, no page image, so that a writer who knows
  the Bible could not simply recite it.

FIGURES (these exact numbers may be used; no others. Every percentage is a share of ALL words in the manuscript, not of the words read; restored and dark words are not read.)
- words in the manuscript {fig['words'][0]}; read {fig['read'][1]}%; read from one
  passage only {fig['soft'][1]}%; restored in brackets {fig['rest'][1]}%; dark
  {fig['dark'][1]}%.
- lines with every word read {fig['lread'][2]}%; lines complete once brackets
  are counted {fig['lall'][2]}%.
- The dictionary of added readings: tier A {tiers.get('A',0)}, B {tiers.get('B',0)},
  C {tiers.get('C',0)}, D {tiers.get('D',0)}, G {tiers.get('G',0)}, withdrawn
  {tiers.get('withdrawn',0)}. Total {len(rows)} entries.
- Tier A survives every place the sign stands in the book, or is proved by an
  identical formula or a numeral. Tier B survives most, the rest unclear rather
  than against. Tiers C and D are read from one passage with nothing inside the
  book able to refuse them. Tier G is a guess, printed in brackets, counted as
  read nowhere. Withdrawn readings stay in the file with the reason they went.
- {len(order)} folios; English was written for {n_eng} of them; the rest carry
  too little gloss to say anything true.

THE SCRIPT ITSELF (for the page about it)
- The writing runs right to left. The codex dates itself 1593.
- It is logographic: a sign stands for a word or a whole phrase, not a sound.
  Kiraly and Tokai established this. Several hundred signs are in use.
- Phrases are written WITHOUT a space. The example Kiraly and Tokai print from
  folio 137v is "sin, without, Jesus, conceive, you-Mary", where you-Mary is a
  single sign made of their sign for the second person pronoun (932 occurrences)
  joined to their sign for Mary. This project confirmed the construction
  independently of their glosses and then applied it across the book.
- Name signs are the most productive final element: Lord stands alone 577 times
  and inside longer signs 1038 times; Jesus 89 and 558; Mary 59 and 137.
- Numerals are strokes that ADD, and a "ten" written after a group multiplies
  that group by ten. Checked four times against a number the source supplies:
  ten-ten-ten-ten is forty at the forty days and forty nights; two-two-ten is
  also forty at the forty days of rain; six-two is eight at the circumcision on
  the eighth day; six-six is twelve at the twelve apostles.
- One grammar rule was recovered from the numerals: the sign Kiraly and Tokai
  gloss "introducing the next item in a list" makes an ordinal when it stands in
  front of a numeral. The book uses it to number the signs of Christ first to
  eleventh.
- Where the signs came from is NOT settled and this project does not claim to
  know. The script occurs in no other document. What can be said is structural:
  a logographic script is not tied to any one language, since a sign meaning
  "Lord" can be voiced in whatever the reader speaks. That is an argument from
  the structure of the script, not a tested result, and must be offered as such.
- The marks in the rendering: a plain word is read; a word with * was read from
  one passage with nothing in the book able to refuse it; a word in [brackets]
  is a restoration and is counted as read nowhere; a hyphen inside a word means
  one sign read as the smaller signs it is built from; a ~ marks a spelling
  their own apparatus files as a variant.
- The drawings: 26 folios carry pictures, 49 pictures in all. The plates in this
  edition were REDRAWN by an image model from the library's low-resolution scan,
  because no print-quality scan is available. They are new drawings that follow
  the scribe's composition, not reproductions, and every caption says so.

THE TESTS
- Every bar was declared in the test's own docstring before it ran, and none
  was moved. Failures are recorded beside passes.
- Nine tests were designed by the project to break its own readings. Then two
  outside reviewers, Gemini 2.5 Pro and Grok 4.7, were shown the write-up and
  asked what tests they would require; those were run as specified.
- The summary (rendered on the page by code; do not restate its numbers):
{summary}

WHAT IS ON THE SITE
- The reading page: one paragraph of English per folio, all {len(order)} folios, in
  Kiraly and Tokai's page order. Restorations are in brackets there; the full
  per-word marks are in the edition and the rendering, not on that page.
- Dictionary: the added readings, searchable by reading or sign, filterable by
  tier, with the evidence line for each. Their own {ktn} entries are NOT
  reproduced; the signs are written as glyph codes, three hexadecimal digits per
  glyph, and the drawn signs are on their site.
- Tests, Method (the loop that reads an unread sign, written as standing
  orders), the full write-up, Sources (where every file came from and what may
  be done with it), and Data (every file the pages are built from: the
  dictionary and folio English as JSON, the rendering, the reader's edition,
  every saved run, the outside readers' replies).
- The edition: the whole manuscript set as a book in two parts, a continuous
  retelling by episode and all 441 folios with their marked lines. It is being
  finished and will appear in the OONA Free Library. Nothing on the site waits
  on it.

POSITION
- The manuscript is out of copyright. Kiraly and Tokai's dictionary,
  transcription and page images are theirs: credited on every page, linked, not
  rehosted. The readings, tests, English and editorial matter are this
  project's own. Every figure on the site is read out of a saved run, never
  typed by hand.
"""


PROMPT = """You are writing the text of a small public website about a research project. Below is a fact sheet. Write ONLY from it. Do not add facts, dates, names, numbers or claims that are not on the sheet. Where the sheet gives a number you may use it; otherwise write around it.

Length matters: this is the whole text of the site, and a reader who never opens another page must learn from it what the manuscript is and contains, who Kiraly and Tokai are and what they did, what this project added and how it was checked. Carry the facts of the sheet into the prose, including the figures where they belong. Targets: intro 350 to 450 words in three paragraphs; how_far, tiers, is_it_true, edition, credit, reading_lead, data_lead and outside_lead 60 to 120 words each; dictionary_lead 120 to 180 words; each card one sentence of 10 to 20 words; new_here_lead one sentence.

Voice: plain English, sentences of ordinary length, one idea per sentence. No hype, no adjectives of praise, no rhetorical questions, no em dashes, no semicolons, no bullet lists inside the prose. Say "probably" where the sheet is cautious. Credit Kiraly and Tokai by name where their work is described. Never overstate: the project extends and tests their dictionary, it does not "crack" or "solve" the codex.

Return a single JSON object with exactly these keys, each a string of plain text (paragraphs separated by a blank line):

tagline          one line under the site title, at most 14 words, no full stop, naming Kiraly and Tokai
intro            3 paragraphs: what the manuscript is; what Kiraly and Tokai did and what they established the book contains (name the contents); what this project did
how_far          one paragraph introducing a table of the reading figures that follows it
tiers            one paragraph after the tier counts, explaining the tiers
new_here_lead    one sentence introducing a quoted paragraph titled "What is new here and what is not"
is_it_true       one paragraph introducing the test summary table that follows it
card_reading     one sentence for a link card to the folio-by-folio reading
card_dictionary  one sentence for a link card to the dictionary
card_tests       one sentence for a link card to the tests
card_method      one sentence for a link card to the method
card_writeup     one sentence for a link card to the full write-up
card_data        one sentence for a link card to the data downloads
edition          one paragraph about the book edition
credit           one paragraph on credit and position
reading_lead     one paragraph at the top of the reading page
dictionary_lead  two paragraphs at the top of the dictionary page (how the signs are written, what is and is not included)
data_lead        one paragraph at the top of the data page
outside_lead     one paragraph introducing an outside reviewer's specification, quoted whole
card_script      one sentence for a link card to a page about the script itself
script_intro     2 paragraphs opening a page about the script: what kind of writing it is, and what is not known about where it came from
script_signs     one paragraph introducing a shuffler that shows one sign's reading at a time
script_numerals  one paragraph explaining how the numerals work, using the checked examples
script_phrases   one paragraph explaining that phrases are written without a space, using the you-Mary example
script_shuffle_lead  one sentence above the shuffler's controls
script_marks     one paragraph explaining the marks used in the rendering
script_plates    one paragraph introducing the redrawn plates, saying plainly that they are redrawings and why
credit_line      one sentence, at most 35 words, for the foot of every page: whose dictionary this rests on, that their translation is unpublished, and that the readings here are this project's own

FACT SHEET
""" + "{sheet}"


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--show", action="store_true")
    a = ap.parse_args(argv)
    if a.show:
        print(open(OUT, encoding="utf-8").read())
        return 0
    sheet = fact_sheet()
    reply, usage = ktor.ask(MODEL, PROMPT.format(sheet=sheet), temperature=0.2, extra=EXTRA)
    print("usage", usage)
    m = re.search(r"\{.*\}", reply, re.S)
    if not m:
        raise SystemExit("no JSON in the reply:\n" + reply[:2000])
    copy = json.loads(m.group(0))
    missing = [k for k in KEYS if not str(copy.get(k, "")).strip()]
    if missing:
        raise SystemExit("missing keys: " + ", ".join(missing))
    extra = [k for k in copy if k not in KEYS]
    for k in extra:
        copy.pop(k)
    copy["_by"] = MODEL
    copy["_sheet_words"] = len(sheet.split())
    json.dump(copy, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", OUT)
    for k in KEYS:
        print(f"\n[{k}]\n{copy[k]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
