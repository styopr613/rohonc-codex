# The rewrite: making Book One read

A brief for whoever does this next. It is self-contained. You do not need to
have worked on this project before, and you should not need to read the other
documents to start, though `METHOD.md` is the standing order for the project as
a whole and its rules about bars apply here too.

## What the book is

The Rohonc Codex is a 16th-century manuscript in an undeciphered script. Király
and Tokai published a dictionary of 841 signs and a transcription. Working from
those, this project has an English rendering of all 441 folios.

The book that comes out of it has two halves.

    Book One   a reading edition: the codex in continuous English prose
    Book Two   the gloss, folio by folio, line by line. This is the evidence.

Book Two is finished and correct. **Book One does not read.** Not part of it:
the whole of it. Here is folio 120v as currently printed:

    from this the Lord would begin the tenth order of angels; and from the
    leaving of the Lord until the day of judgment the Lord would, of the Lord,
    from the Father God, the tenth from the order, in the place shall stand
    empty there is the Lord

and here is folio 004v, which is the first page of the book and opens Part I,
one of the parts that tells a story:

    In the beginning there was the Lord God, and the earth. The sun and the
    moon, as the scripture says. Elijah the prophet. The angel of God said:
    the forefather, before the heart of man. The Father; Adam bowed down
    before the Lord.

Those look like different problems and they are the same problem. Measured
against this imprint's own published editions:

    Rohonc Book One       3.84 semicolons/100 words    3.97 ", and"/100 words
    Metamorphosis         0.87                         0.90
    the Gospels           0.76 - 0.98                  0.71 - 1.12

Sentence length is fine: 23 words against 29 in Metamorphosis. The sentences
are not too long. They are chains of verbless fragments strung together on
semicolons. The best part of the book, the Resurrection, still sits at 2.7,
which is three times the baseline. The parts that tell a story only feel
better because the content is recognisable; the construction is identical.

So this is not a cleanup of bad pages. **The whole of Book One is rewritten.**

## The diagnosis, which is the important part of this document

The reading pass was fed the wrong gloss.

Every sign in K&T's dictionary has several senses, in their order, with worked
examples and folio citations. The pipeline built a **first-sense-only** gloss
and handed the reading pass that. So every ambiguous sign got sense (a),
regardless of context, and a page whose sense is carried by sense (c) came out
as noise.

The proof is the sentence the codex repeats most often, roughly forty times.
Book One currently prints it as:

    Every man is saved, and one man is damned; and the Lord does not believe,
    and one is saved, but he who does not believe, a man is damned.

Three separate entries in K&T's own dictionary say that is backwards:

    the numeral sign   "I. numeral a) one  b) first  c) (some)one; NOT ONE
                        e.g. 094r05; 'he did not make one single wonder' 043r04"

    the sin sign       "II. sinner — 'not one sinner is saved, but all are
                        damned' 077r06"

    the 'somebody' sign "c) expressions ... 019r03 every(body); (with negation)
                        019r03, 04 NOBODY"

The third of those cites folio 019r lines 3 and 4, which is this exact formula.
K&T mark the negation. The first-sense gloss dropped it. So the book prints the
opposite of what the manuscript says, in its most repeated sentence, and
prints it as gibberish besides.

**The full entries were already in the repo.** Nothing joined them to a folio.
`harness/ktsenses.py` now does, and `work/rohonc/senses.json` has all 441
folios. That is the whole bug and the join is already built.

One lookup trap, because it cost an hour: DO NOT search the dictionary for an
English word. K&T quote their own translations inside their entries, so the
entry for the sign meaning "kneel down" contains the word "before" in its
example, and the sign meaning "speak" contains "angel". Search by CODE only.

## The files

    data/rohonc/kt/dict_en.json
        K&T's dictionary. 979 entries. Each is {code, entry}, where entry is a
        list of runs with styles. Join the "text" of the runs to get the entry
        as printed: all senses, in K&T's order, with their examples and folio
        citations. THIS IS THE FILE THAT WAS NOT BEING USED.

    work/rohonc/translation/rohonc_reading_full.txt
        All 441 folios with the FULL sense list under every word. Sections are
        marked "=== 004v ===". `harness/page.sh 004v` prints one.
        This already exists. Look at it before you write any code.

    work/rohonc/translation/rohonc_translation.md
        The hand-made English per folio, with a first-sense gloss under each
        line. This is what the reading pass was given. It is not wrong, it is
        just not enough to choose a sense from.

    work/rohonc/sources.json
        Per folio: the verses it cites, and the passages retrieved from the
        medieval books the codex compiles (Life of Adam and Eve, Golden Legend,
        the apocryphal gospels, Barlaam, the missal, the mystery plays,
        Josephus). Built by harness/ktsource.py.

    work/rohonc/translation/reading.md
        The current Book One. What you are rewriting. 396 paragraphs.

    work/rohonc/senses.json
        EVERY folio, every line, every word, with K&T's WHOLE entry: all
        senses, their examples, their folio citations. Built by
        harness/ktsenses.py, which is new and was written for this job.
        `python3 ktsenses.py 004v` prints one folio to read.
        THIS IS THE INPUT THE REWRITE NEEDS. It did not exist before.

    harness/ktsenses.py     the folio-to-full-entries join (new)
    harness/ktreading.py    the pass that writes reading.md
    harness/ktverify.py     the word-source accounting, and the reader's view
    harness/ktfix.py        the targeted paragraph rewriter

Keep every intermediate file. Nothing is deleted. The convention is a
`.pre-<what>-<date>` suffix on a copy made before any edit, and a filename is
never reused.

## The job, in four steps

All of it, all 441 folios. Do not filter to the worst pages: the whole book is
built the same way and the whole book is rewritten. The last full run cost
$0.42, so cost is not a reason to do less.

### 1. The formula table

The unreadable pages are a preacher's notes built from a small stock of
repeated phrases. Render each one ONCE, by hand, from K&T's full entry, and
give the pass that table as fixed English.

Count them first. A 3-to-6 word window over every folio's gloss, dropping
windows that cross a line break, finds about forty phrases occurring six times
or more. The commonest, with counts from the current gloss:

    44   end this holy-gospel
    33   begins this holy-gospel
    19   chapter-oh chapter-oh amen
    19   son living God
    15   each,_every somebody be_saved
     9   each,_every somebody be_damned

For each, open the dictionary entry for every sign in it, and write the English
that K&T's senses and examples actually support. The belief formula is the
first one to do, and it is the single biggest win in the book.

Record the table in a file with, for each formula, the gloss, the English, and
the dictionary evidence for the sense chosen. It must be auditable. Someone
will ask why a sign was read as "not one" and the answer has to be a citation,
not a preference.

### 2. Feed the reading pass the full senses

`harness/ktreading.py` builds its prompt in `folio_prompt()` from
`blocks()`, which reads the first-sense file. Give it the full sense list for
the folio as well, and the formula table, and say plainly in the brief: **choose
the sense that makes a sentence, and K&T's example translations are the guide.**

This is the change that makes the book readable. Everything else is
supporting work around it.

### 3. The readability bar, declared before you run

There is already a fidelity bar, and it does not move:

    fidelity    every content word of a paragraph is either in that folio's own
                gloss, or in a source the folio was shown, or in neither. The
                third class is an import and is printed. The last run scored
                97.9% from the manuscript, 1.3% source only, 0.8% neither.

The fidelity bar cannot see this problem at all. A paragraph that merely
re-punctuates the gloss scores perfectly on it. That is exactly how the current
Book One passed every check while being unreadable.

So declare a second bar, from the imprint's own published editions, BEFORE the
run. The measurements are above. The targets:

    semicolons per 100 words          at or below 1.2   (now 3.84, ours 0.87)
    ", and" chains per 100 words      at or below 1.3   (now 3.97, ours 0.90)
    paragraphs with a verbless run of 3+ noun phrases   zero
    leftover apparatus words          zero
        "in turn", "exist", "why in turn", "somebody", "O chapter"

Those numbers come from Metamorphosis and the Gospels, which are finished books
on this imprint, so the bar is not invented: it is what our own prose does.
Print both bars side by side, per part and for the book. A paragraph must not
pass one by failing the other.

If the rewrite lands above the bar, the brief is wrong and the brief gets
fixed. Do not relax the bar. That rule has held for thirteen earlier
experiments and it holds here.

### 4. Rewrite the book, then read it

Rewrite every folio, with a brief that says: these are a preacher's notes, and
you are writing them out as continuous English. Supply the syntax. Choose the
sense from the full entry that makes a sentence. Keep the manuscript's order.
Invent nothing.

Then read it. Worst first by the readability score.
`python3 ktverify.py folio 120v` puts a paragraph beside its own gloss. No
program can tell you whether a sentence means what the gloss means. Only
reading can, and the last round of errors, a fabricated gospel heading and
three mangled numbers, were all caught by reading and none by a checker.

Start with folio 004v, which is the first page a buyer sees, and do not scale
up until that one page reads as well as the opening page of any other book on
this imprint.

## The worked example: folio 004v, the first page of the book

This was done by hand from `python3 ktsenses.py 004v`, and it is the standard.
Nothing here is invented. Every choice below is a sense K&T print, and four of
them are senses K&T illustrate WITH THIS VERY FOLIO.

What the full entries gave that the first-sense gloss did not:

    line 1   the opening sign: "adverb of time a) AT THE BEGINNING OF A STORY,
             'once upon a time' e.g. 004v01" -- K&T cite this line itself
    line 5   the 'somebody' sign: "b) WE 004v05" -- so it is "before we were
             made", not "before the heart of man"
    line 6   the father sign: "father, forefather e.g. OUR (FORE)FATHER, ADAM
             004v05-06" -- K&T cite these two lines as that exact phrase
    line 9   two + half + hundred + seven is 257, not "two hundred and fifty
             years and seven"
    line 11  "numeral ten expr. 40 DAYS AND 40 NIGHTS 004v11" -- cited here
    line 12  the hell sign: "hell e.g. 004v12" -- cited here
    line 15  the throne sign: "a) throne e.g. 004v15" -- cited here

As currently printed in the book:

    In the beginning there was the Lord God, and the earth. The sun and the
    moon, as the scripture says. Elijah the prophet. The angel of God said:
    the forefather, before the heart of man. The Father; Adam bowed down
    before the Lord. God in heaven eternal, and the brethren. Many angels;
    and God the Father had many angels about him. Among the angels, two
    hundred and fifty years and seven before the heart of man. The Father,
    Adam, and the angels; there was Lucifer, and the other angels. And the
    angels prayed, and for forty days and forty nights Lucifer among the
    brethren, in hell. And again the angel said to Elijah: Elijah, when there
    is as Lucifer, who did this -- Lucifer, when he was seated on the throne
    of God the Father. God the Father went. (004v)

And rewritten from the full entries:

    At the beginning there was the Lord God, and he made heaven and earth,
    the sun and the moon, as it is written.

    The angel of God said to Elijah the prophet: before we were made, our
    forefather Adam bowed down before the Lord. God is eternal in heaven, and
    the brethren are with him. There were many angels, and God the Father had
    many angels about him. Among those angels, two hundred and fifty-seven
    years before we were made, before our forefather Adam, there was one
    brother by name, and he was Lucifer, and the other angels were with him.
    And the angels prayed forty days and forty nights, until Lucifer was cast
    down into hell, and the rest of the brethren with him.

    And a second time the angel of God said to Elijah: Elijah, this is how it
    was with Lucifer, who did it, on the day he sat upon the throne of God the
    Father. And God the Father went out. (004v)

Count the semicolons: eight in the first, none in the second. Nothing was
added. Two outright errors were removed, the year and "the heart of man". The
sentences have verbs. That is the whole job, 441 times.

## The rules that do not bend

- **The manuscript leads.** A source only ever tells you what a phrase in the
  manuscript MEANS. It never adds an episode, a person, a speech or a detail
  the manuscript does not have.
- **Where the codex departs from its source, follow the codex.** Different
  name, different number, an episode the source lacks: those departures are the
  most interesting thing in the book and must survive.
- **Numerals add, and a "ten" after a group multiplies that group by ten.**
  six-six is twelve. two-two-ten is forty. six-two is eight. ten-ten-two-nine
  is thirty-one. Never copy a numeral string into the English, and never
  shorten a count: "six-hundred and six-thousand and six-ten and six" is six
  hundred, and six thousand, and sixty, and six, and all four parts stay. This
  rule exists because all three of those were got wrong once.
- **Plain modern English.** No thee, thou, thy, thine, ye. No -eth or -est. No
  "unto", "whither", "behold", "verily", "lo". The sources are in 17th-century
  Bible English and their cadence must not leak. Say "you", "has", "says",
  "to", "where", "look". Plain words a twelve-year-old reads easily.
- **Do not sanitise.** Where the manuscript is harsh or strange, so is the
  English.
- **No commentary.** You are writing the book out, not writing about it. Never
  use the words "manuscript", "folio", "source", "passage" or "text" in the
  prose itself.
- **Never move a bar after seeing a result.** A near miss is a miss. This is
  the project's oldest rule and ten of thirteen earlier experiments are written
  up as failures because of it.

## Things that have already gone wrong here

Do not repeat these. Each cost real time or reached the printed book.

- A fabricated rubric. Folio 069v was given the heading "Here begins this holy
  gospel written by holy Luke, in the tenth chapter". The page has no heading,
  and the passage is John 15. The word accounting is what caught it.
- The fix pass once returned its own working: the gloss block, the word list
  and a note to itself. It was printed in the book. Any reply that is not
  exactly one paragraph must now be rejected.
- Charles's full Pseudepigrapha was indexed as a source. Four fifths of that
  volume is critical apparatus, and its dense rare vocabulary outscored every
  real parallel. Only the Life of Adam and Eve is extracted and kept.
- The word accounting reported "came", "gave" and "spoke" as inventions,
  because the stemmer cannot reach an irregular verb. That buried the real
  faults under noise until an irregular-verb map was added.
- Fourteen paragraphs carry no folio citation and so escape the accounting
  entirely. One of them is a dangling fragment that stops mid-sentence: "She
  carried the woman, within". Find them and fix them.

## How to check you are done

    cd harness
    python3 gate.py            # the harness gates
    python3 check_results.py   # every figure in RESULTS.md prose
    python3 check_rohonc.py    # every figure in ROHONC.md prose

All three must be green before any commit, and commits go through
`./ktcommit.sh "message"`, which runs them.

Never hand-type a figure into a document. Every number in the prose is checked
against a saved run. If you write a new number, add a check for it.

## What success looks like

Read twenty paragraphs at random. If a person who knows nothing about this
manuscript can follow all twenty straight through, it is done. If three of them
are lists of nouns, it is not.

Then read folio 004v beside the opening page of Metamorphosis or the Gospels on
this imprint. It has to survive that comparison, because that is the comparison
a buyer makes.

The fidelity number WILL FALL when this is done properly, because supplying
syntax means supplying words. That is expected, and it is the correct trade. It
is not a licence to invent: a supplied verb or article is not a supplied fact,
and the rules above still hold absolutely. Say plainly in the book's front
matter what the new figure is, and that the edition is interpretive.
