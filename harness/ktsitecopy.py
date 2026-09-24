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
        "outside_lead", "card_script", "script_intro", "script_signs",
        "script_numerals", "script_phrases", "script_shuffle_lead", "script_marks",
        "script_plates", "method_intro", "method_loop", "method_bars", "method_mistakes",
        "method_code", "tests_intro", "tests_after", "sources_intro", "docs_lead",
        "read_lead", "strip_note", "tests_note", "code_lead", "sources_not_here",
        "method_steps", "method_mistakes_list", "sources_cites", "reading_what",
        "reading_how", "reading_limits"]


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
- The Rohonc Codex: a small paper book of the sixteenth century, 224 leaves and about 450 pages,
  kept at the Library of the Hungarian Academy of Sciences in Budapest.
- Written in a script that occurs in no other document. Right to left, several
  hundred signs, mostly one sign per word or phrase.
- What it contains (established by Király and Tokai): the apocryphal Life of Adam
  and Eve running into the legend of the Rood; the story of Joachim and Anne; a
  Passion the codex itself says it takes from Matthew and John; sermons and
  parables for the gospels of the year; the Finding of the Cross; the Acts of the
  Apostles; and at the end a few pages of one man's diary. The frame is a
  revelation: an angel of God speaks and the prophet Elijah is the one addressed.

KIRALY AND TOKAI (credit them by name, always)
- Levente Zoltán Király and Gábor Tokai, "Cracking the code of the Rohonc Codex",
  Cryptologia 42:4 (2018). A dictionary of {ktn} signs; their grammar paper is
  unpublished.
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
- CAREFUL, THERE ARE TWO DIFFERENT LAYERS AND THEIR RULES ARE OPPOSITE.
  (a) THE LITERAL LAYER, one paragraph per folio: written from that folio's
  gloss ALONE, with no source passage, no chapter title and no page image, so
  that a writer who knows the Bible could not simply recite it. It is a check,
  and it does not read.
  (b) THE READING EDITION, which is the front half of the book: written from
  the gloss AND from the passages the folio is working from, on purpose,
  because that is the only way an elliptical text becomes English. Never
  describe the reading edition as made from the gloss alone.

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

THE METHOD (for the page about it) -- the loop that reads one unread sign
- 1. Take the folio's own citation. K&T's notes cite a chapter and verse for
  most folios; the source passage is the only outside evidence there is.
- 2. Look at every line where the unread sign stands, not just the one in hand.
- 3. Guess from the passage: the word the verse supplies for that slot.
- 4. CHECK THE GUESS AT EVERY OTHER OCCURRENCE in the book. A reading that fits
  where it was found and fails elsewhere is thrown away, not softened.
- 5. Grade it: tier A fits everywhere checked, B fits most, C or D was read
  from one passage with nothing able to refuse it, G is a guess in brackets.
- 6. Write the evidence line into proposals.json with the folios and lines, so
  anyone can repeat the check or overturn it.
- The bar for every test is written into the test's own file BEFORE it runs,
  and is never moved afterwards. A near miss is a miss. Failed attempts are
  kept and written up with the number they failed by.
- Seventeen attempts were made to extend the dictionary. Ten failed. The two
  that worked were the same discovery: the signs are phrases, and cutting them
  apart recovers readings from parts already in the dictionary.

THE MISTAKES THAT COST THE MOST TIME (name them plainly; they are the useful part)
- Treating a sign as an atom. Eleven attempts assumed one sign meant one word
  with a meaning to guess. Many signs are short phrases written without a
  space, and both halves were already in the dictionary. That was the whole
  game, and the 2022 paper says so in passing.
- Inheritance versus composition. Asking whether "Holy Word" inherits meaning
  from "Word" gave a true negative that looked like a dead end. The right
  question was whether signs COMBINE.
- A unit error. Figures were computed per glyph when a word averages 2.43
  glyphs. Every number moved when it was fixed. Always confirm what one row of
  the transcription is before measuring it.
- Homograph collision. Keying a scraped dictionary by code and keeping the
  last entry made the book's commonest word read "eleven" when it is "and";
  65 codes had to be merged.
- Blaming the corpus. A failed aligner was predicted to be failing because it
  used only the four gospels; 1.75 million words of the wider sources were
  fetched and it scored no better. Test the cheap version of a corpus
  hypothesis first.
- Reading only the headword. K&T's entries carry variant spellings in their
  own apparatus; keying by headword silently dropped 88 signs, 1.2% of the
  book, that they had already read.
- Three versions of the arithmetic of "what is left to read" were wrong,
  including one that counted a line as reached while an unread word still
  stood in it. The current figures are measured and the wrong ones are kept on
  the page beside them.

THE SCRIPT ITSELF (for the page about it)
- The writing runs right to left. The codex dates itself 1593.
- It is logographic: a sign stands for a word or a whole phrase, not a sound.
  Király and Tokai established this. Several hundred signs are in use.
- Phrases are written WITHOUT a space. The example Király and Tokai print from
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
- One grammar rule was recovered from the numerals: the sign Király and Tokai
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

CITATIONS OWED (quote each exactly as written here)
- Levente Zoltán Király and Gábor Tokai, "Cracking the code of the Rohonc Codex",
  Cryptologia 42:4 (2018), 285-315. -- the dictionary.
- Levente Zoltán Király, "A Rohonci kódex teológiai karaktere", in Hagyomany,
  Identitas, Tortenelem 2022, KRE HTK, Budapest 2023, 363-376. -- it explains why
  their site exists: so their claims about the text can be checked.
- Ottó Gyürk (1970), on line breaks in the codex's repeated sequences. -- the idea
  the orientation test and the main measurement both rest on.
- Benedek Láng, The Rohonc Code: Tracing a Historical Riddle, Penn State Press,
  2021. -- the standing survey of the manuscript and of everyone who has attacked it.
- The anonymous author of the 2014 open transcription. -- published openly; the site
  is gone and permission cannot be asked.
- Library of the Hungarian Academy of Sciences, the page scans. -- free for academic
  use, not to be passed on; used locally, and the plates are redrawings made from
  them rather than the scans themselves.

THE READING EDITION (2026-09-22)
- The book's front half is a READING EDITION, and it is interpretive on purpose.
  The codex is elliptical: its script writes whole phrases as single signs, it
  drops verbs and articles, it repeats formulas, and many leaves are damaged.
  A word-for-word rendering of it does not read, and the project has one of
  those already.
- So each folio was read against the books it is compiled from: the verses it
  cites, from the Douay Bible the compiler had, and the medieval texts behind
  it -- the Life of Adam and Eve, the Golden Legend, the apocryphal gospels,
  Barlaam and Ioasaph, the Roman Missal, the Office of Holy Week, the four
  English mystery play cycles, Josephus. Those are found for each folio by
  searching the corpus for the passage that shares its rare vocabulary.
- The rule throughout: the manuscript leads and the source only ever says what
  a phrase MEANS. Where the codex departs from the source -- a different name,
  a different number, an episode the source does not have -- the codex is
  followed, because those departures are the most interesting thing in it.
- The English is plain modern English, the same house voice as every other
  edition on this imprint. No archaic Bible cadence.
- NO "WE", "OUR" OR "US" ANYWHERE IN THE EDITORIAL VOICE. There is no "we" --
  one person and the programs he ran. Write "this edition", "this project",
  "the AI agent", or the plain third person; write "I" only where the owner is
  speaking for himself. A "we" in the manuscript's own narrative -- the codex
  saying "we have seen the Lord", the Our Father -- is the codex talking and
  is left exactly as it stands. (Owner, 2026-09-23.)
- Every paragraph names the folios it renders. The gloss of all 441 written pages is
  printed in full in the second half of the book, line for line, with every
  mark. Where the two disagree the gloss is right.
- Every paragraph was then put back beside its own gloss and checked: does it
  still say what the manuscript says, does it add a person or an event the
  manuscript does not have, what does it leave out. The figures from that
  check are published with the edition.

THE WORKING DOCUMENTS (described on the site; METHOD.md is also published whole, unedited, at orders.html)
- They are working files: written for whoever runs the project next, not for a
  reader. They are kept accurate rather than tidy. Anyone who wants one can ask
  for it at info@oona13.com.
- ROHONC.md, the full account: the line-break measurement, the dictionary, all
  seventeen attempts to extend it, what the book says, and what is not decided.
- METHOD.md, the standing orders: the loop, and the arithmetic of what is left
  to read, with three earlier versions of that arithmetic that were wrong.
- TESTS.md: every test with its bar, its control and its saved run.
- DATA_PROVENANCE.md: where each file came from and what may be done with it.
- FINALPASS.md, BLINDFOLD.md, DARK.md: the vocabulary check before the guesses,
  the one check the project cannot run on itself, and the last unread words.

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
  Király and Tokai's page order. Restorations are in brackets there; the full
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
- The edition: the whole manuscript set as a book in two parts. Book One is a
  TRANSLATION: the gloss of every folio put into English by a language model
  working from the gloss and a glossary of the script's formulas, then proofed
  into plain prose by a second pass; every paragraph closes with the folios it
  renders; a gap is printed as three dots and a restored word keeps its
  brackets. Book Two is the gloss itself, all 441 written pages line for line with
  every mark, the evidence the translation was made from. Where they disagree,
  Book Two is right.
- A read page: that whole book opened in the browser, page by page, with the
  same book downloadable as an EPUB or as the interior print PDF.

POSITION
- The manuscript is out of copyright. Király and Tokai's dictionary
  and transcription are theirs: credited on every page, linked, not
  rehosted. The readings, tests, English and editorial matter are this
  project's own. Every figure on the site is read out of a saved run, never
  typed by hand.
"""


PROMPT = """You are writing the text of a small public website about a research project. Below is a fact sheet. Write ONLY from it. Do not add facts, dates, names, numbers or claims that are not on the sheet. Where the sheet gives a number you may use it; otherwise write around it.

Length matters: this is the whole text of the site, and a reader who never opens another page must learn from it what the manuscript is and contains, who Király and Tokai are and what they did, what this project added and how it was checked. Carry the facts of the sheet into the prose, including the figures where they belong. Targets: intro 350 to 450 words in three paragraphs; how_far, tiers, is_it_true, edition, credit, reading_lead, data_lead and outside_lead 60 to 120 words each; dictionary_lead 120 to 180 words; each card one sentence of 10 to 20 words; new_here_lead one sentence.

Voice: plain English, sentences of ordinary length, one idea per sentence. No hype, no adjectives of praise, no rhetorical questions, no em dashes, no semicolons, no bullet lists inside the prose. Say "probably" where the sheet is cautious. Credit Király and Tokai by name where their work is described. Never overstate: the project extends and tests their dictionary, it does not "crack" or "solve" the codex. NEVER state a licence, a permission, or that anything "may be used freely": say who owns what and nothing further. Do not write any sentence granting or implying rights.

Return a single JSON object with exactly these keys, each a string of plain text (paragraphs separated by a blank line):

tagline          the fixed line 'Using AI to extend and test the Király and Tokai dictionary', verbatim; the owner set it
intro            3 paragraphs: what the manuscript is; what Király and Tokai did, in these words: 'Levente Zoltán Király and Gábor Tokai established what the book LIKELY contains, as this essay largely validates.' -- likely, and largely; this project does not ratify them and does not overstate them (then name the contents); what this project did; then ONE paragraph, in these words: this was done with AI, under an editor; Anthropic's Claude decoded the remaining signs using the Király and Tokai dictionary as a foundation; different models assembled the gloss and composed the translation. Name no other model; then ONE paragraph on the two parts: Book Two the gloss and the evidence, Book One the translation read against the sources, and where they disagree Book Two is right; the paragraph on what the project did must NOT say it read undefined signs, checked every occurrence, or marked every word -- the AI paragraph and the two-parts paragraph already cover that; Claude PROPOSED readings, never 'decoded' or 'cracked'; and a LAST paragraph, VERBATIM, the owner's own: 'This is an attempt, not peer reviewed, and published to be checked. As of now, the tests, for what they are, find it internally consistent. Tests and all programs and documents are in the repository at https://github.com/styopr613/rohonc-codex.'; and IMMEDIATELY BEFORE that last paragraph, one paragraph, opening VERBATIM with the owner's words 'One test, in particular, uses a source outside the project -- and offers substantial validation.': everything here reads Kiraly and Tokai's transcription so no test of this project's could catch an error in it, and the anonymous 2014 open transcription -- different person, different glyph alphabet, no word division, four years earlier -- agrees with it on 91.1% of comparable glyphs against a 12.9% random-pairing control and on 83.8% of the words. Say only that the two ARE TAKEN TO share no common root but the book: independence is inferred, not established, and must not be stated as proved
how_far          one paragraph introducing a table of the reading figures that follows it; say the project HAS A READING FOR the percentage, not that it reads it
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
credit           MUST state the three licences and why: the programs MIT and the data CC BY 4.0 so that checking is unrestricted, the translation and editorial prose CC BY-NC-ND 4.0 with the commercial rights to the English reserved. Do NOT say any edition is sold: none is. one paragraph on credit and position
reading_lead     one paragraph at the top of the reading page
dictionary_lead  2 paragraphs opening the dictionary page: whose readings these are, that K&T's own 841 entries are in their 2018 publication, not here, and their drawn signs are on their site (the page adds the edition's wording note itself; do not paraphrase it), how a sign is written, and that the table is searchable and filterable. Do NOT define the tiers -- a legend on the page does that -- and do NOT give a total: the page prints the split
data_lead        one or two sentences: the data is in the repository at https://github.com/styopr613/rohonc-codex; this page names the reference corpus and says where everything else goes. No file links
outside_lead     one paragraph introducing a reviewer's specification, quoted whole; the reviewers are two frontier models from other labs, Gemini 2.5 Pro and Grok 4.7, and the paragraph must say so in its own words, never 'outside reviewers' alone
card_script      one sentence for a link card to a page about the script itself
script_intro     2 paragraphs opening a page about the script: what kind of writing it is, and what is not known about where it came from
script_signs     one paragraph introducing a shuffler that shows one sign's reading at a time
script_numerals  one paragraph explaining how the numerals work, using the checked examples
script_phrases   one paragraph explaining that phrases are written without a space, using the you-Mary example
script_shuffle_lead  one sentence above the shuffler's controls
script_marks     one paragraph explaining the marks used in the rendering
script_plates    one paragraph introducing the redrawn plates, saying plainly that they are redrawings and why
method_intro     ONE paragraph opening a page about the method: what problem it solves and what makes it checkable; do not state the bar rule here, it has its own section below; say the method is this project's attempt, never that it solves anything
method_loop      one paragraph introducing the numbered steps of the loop, which are listed after it
method_bars      one paragraph on declaring the bar before the run and keeping failures
method_mistakes  one paragraph introducing the list of mistakes that cost the most time, which follows it
method_code      one sentence introducing links to the programs themselves
tests_intro      2 paragraphs opening a page about the tests: what was being tested and why the bar is declared first; where it mentions the outside review it names the reviewers as two frontier models from other labs, Gemini 2.5 Pro and Grok 4.7
tests_after      one paragraph after the summary table saying what the passes and failures add up to, without restating numbers; it must say a checked ATTEMPT, not a settled result, checked by the project's own tests and two models and not yet by anyone who reads the manuscript independently
sources_intro    2 paragraphs opening a page about sources and credit: whose work each source is and what may be done with it
docs_lead        one paragraph introducing a list of the project's own working documents, which are described rather than published, and can be asked for
read_lead        one paragraph at the top of a page whose only job is to open the book in the OONA reader at /read/rohonc.php, the same reader the Free Library uses; mention that the same book can be taken away as an EPUB. The page itself does NOT contain a reader
strip_note       one sentence under a moving strip of signs, saying what the strip shows and that the script runs right to left
tests_note       one paragraph after the test summary, starting straight on the first fact with no framing sentence, saying that the passage map can be recovered from Király and Tokai's words alone so it does not depend on anything this project read, and that the two instruments an outside reviewer specified for the search itself gave no verdict either way because they do not model the search as it was run
code_lead        one paragraph making one claim: the programs behind every number are runnable and this page says where; each test on the results page names its program and each program states its bar in its first lines; the repository is not public and the programs are served as plain text. Do not say they run on the published data: the dictionary and the transcription are not served
sources_not_here one paragraph saying what is NOT on the site and why: their dictionary, transcription, page records and the library scans; and that the one thing of theirs used is the shape of the signs, drawn from the outlines in their font, the font file itself never served, the shapes being the sixteenth-century scribe's
method_steps     a JSON ARRAY of exactly 6 objects {"t": short title, "d": one or two sentences} for the six numbered steps of the loop, in order; d must not repeat the words of t; the grading step must say that tiers C and D are where the sign occurs too rarely for the everywhere check to bite
method_mistakes_list  a JSON ARRAY of exactly 7 objects {"t": short title, "d": one or two sentences} for the mistakes that cost the most time, in the order the sheet gives them
reading_what     2 paragraphs for the first page of the book and for the site, saying what the reading edition is: an interpretation, not a word-for-word rendering, made by reading the manuscript against the books it is compiled from
reading_how      one paragraph on how the READING EDITION was made, which is layer (b) and NOT layer (a): each folio's gloss was put beside the passages that folio is working from, and the English was written from both; the manuscript leads and the source only says what a phrase means; every paragraph names the folios it renders. Do not say it was made from the gloss alone.
reading_limits   one paragraph saying plainly what it is not and where a reader should go instead: the gloss printed in full at the back is the evidence, and where the two disagree the gloss is right
sources_cites    a JSON ARRAY of exactly 6 strings, one sentence each, saying what each of the six citations listed under CITATIONS OWED is to this project, in the same order. Do NOT repeat the citation itself.

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
    # .replace, never .format: the brief now contains literal JSON braces, and
    # str.format reads those as fields and raises before a call is made.
    reply, usage = ktor.ask(MODEL, PROMPT.replace("{sheet}", sheet),
                            temperature=0.2, extra=EXTRA)
    print("usage", usage)
    m = re.search(r"\{.*\}", reply, re.S)
    if not m:
        raise SystemExit("no JSON in the reply:\n" + reply[:2000])
    copy = json.loads(m.group(0))
    missing = [k for k in KEYS if not (copy.get(k) if isinstance(copy.get(k), list)
                                       else str(copy.get(k, "")).strip())]
    if missing:
        raise SystemExit("missing keys: " + ", ".join(missing))
    # A list key sometimes comes back as a JSON STRING rather than an array.
    # Parse it here so the stored file is one shape and the site never has to ask.
    for k, v in list(copy.items()):
        if isinstance(v, str) and v.lstrip().startswith("["):
            try:
                copy[k] = json.loads(v)
            except ValueError:
                pass
    extra = [k for k in copy if k not in KEYS]
    for k in extra:
        copy.pop(k)
    copy["_by"] = MODEL
    copy["_sheet_words"] = len(sheet.split())
    json.dump(copy, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", OUT)
    for k in KEYS:
        v = copy[k]
        print(f"\n[{k}]\n" + (json.dumps(v, indent=1, ensure_ascii=False)
                              if isinstance(v, list) else str(v)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
