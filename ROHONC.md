# The Rohonc Codex, on the same ruler

A second manuscript, run through the test that decided the Voynich question —
and then, because the data turned out to be there, a check on whether the
Rohonc has in fact been read. Written 2026-09-20, rewritten the same day after
a unit error was found. The Voynich work is in [`RESULTS.md`](RESULTS.md) and
the plain-English summary in [`CONCLUSION.md`](CONCLUSION.md). Where every data
file came from and what may be done with it is in
[`DATA_PROVENANCE.md`](DATA_PROVENANCE.md).

## Why bother

Every claim in `RESULTS.md` rests on one measurement: the dependence between
one token and the next dies at the right margin in the Voynich, where a real
language keeps most of it. That measurement had never been run on anything but
the manuscript it was designed for and a handful of prose controls laid out in
Voynich-shaped paragraphs. A test that has only ever been pointed at one book
is not a test yet. It needs a second manuscript that ought to come out the
other way.

The Rohonc Codex is the right second manuscript. It is a real 448-page codex in
an unknown script, uncracked by anyone's general agreement since 1839, with the
same reputation for possibly being meaningless. If our test can separate it
from the Voynich, the test works. If it cannot, `RESULTS.md` is weaker than it
claims.

## Three transcriptions, of which two exist

**The anonymous open transcription of 2014.** Formerly at `quint.us/Roho/`;
that domain now serves a browser game. Recovered from the Internet Archive.
Glyph-level, with no word separation: 214 pages, 4,250 lines, 60,407 readable
tokens over 987 distinct symbols, 6.5% marked unreadable and dropped.
Incomplete and partly machine-generated.

**Király and Tokai's transcription.** Made for their 2018 decipherment and
served at `rechnitzer-kodex.hu`, which Király's 2022 paper cites as the
stopgap for a dictionary too typographically awkward to print, put there so
that "our claims about the text are verifiable this way". Word-level, with the
authors' own reading order of the pages: 441 pages with body text, 4,372
lines, 29,997 words, 5,010 types, 72,862 glyphs, 2.43 glyphs per word. Only
`main` text blocks are used; headers, picture captions and the one multicolumn
block are excluded, matching the Voynich work's exclusion of labels.

**A third, from the scans, attempted here and failed.** See the section near
the end. The free scan is 100 ppi of a book 120 by 100 mm; a line of text is
sixteen pixels tall; no method separated word identities at that resolution.

## The unit error, and its correction

The first version of this document treated one glyph as one word, on the
reading that a Rohonc symbol codes a whole word. Király and Tokai's own
transcription is space-separated and its words average 2.43 glyphs, with only
a third of them a single glyph. So a Rohonc code is usually two or three
glyphs, and the 2014 glyph stream is a finer unit than the word — roughly as
letters are to words.

Every glyph-level figure in the first version was therefore being compared
with word-level figures from other manuscripts. The glyph-level rows are kept
below as a replication at a second granularity, but the Király–Tokai rows are
the ones comparable with everything else, and the conclusions are drawn from
them. The number moved when the unit was fixed. It moved *into* the
natural-language band, not out of it.

## The orientation problem, and how it was settled

The codex is written right to left. The 2014 transcription does not document
whether it stores each line in reading order or in visual order, and the whole
measurement turns on it: mutual information is symmetric, so the within-line
figure is the same either way, but the across-break pair is (end of this line,
start of the next) and reversing the storage swaps them. The two orientations
give completely different answers — 16.9 sigma one way and 2.2 the other.

External clues point both ways. The delimiter symbol that Király and Tokai
report separates sentences sits at the stored end of the line in 252 of its 269
appearances, which suits stored = reading order. The physical-damage marker
sits at the stored start more often than the stored end, 126 to 77, which suits
the opposite.

**A first attempt failed and was discarded.** `roho_orient.py` reasoned that an
incomplete bottom-of-page line has a genuine beginning and a spurious end, so
whichever stored end better fits the pool of normal line openings is the real
beginning. It returned a verdict — and its own control returned *negative* lift
on complete lines, where both ends are genuine and both should have scored
clearly positive. The pools carry no information, the measurement had no power,
and the verdict was noise on 32 lines. It is kept, with its failure recorded.

**What settled it** was the property the Rohonc has in abundance, and the one
Ottó Gyürk used in 1970: long verbatim repeats. Inside a line the two
orientations are mirror images. At a line boundary they are not: reading order
joins the tail of one line to the head of the next, the reversed reading joins
head to tail, and those are different sequences.

| 4-gram straddling a line break | found inside lines | chance | sigma |
|---|---|---|---|
| stored order as-is | 36.39% | 19.87% | **36.2** |
| reversed | 19.68% | 20.15% | −0.9 |

Reversed sits exactly on chance. The file stores reading order. Király and
Tokai's file needs no such test: its page list is their reading order.

## The result

Percentage of token n-grams straddling a line break that the same manuscript
also writes strictly inside a line. Chance shuffles which line follows which
within a page, leaving every line intact and destroying only the pairing.

`lift` is the ratio to chance and is the wrong way to compare texts with
different repeat rates: the 2014 glyph stream's chance level is already 76.70%
at n=2, so its ratio cannot exceed 1.30 however continuous the text is.
`headroom` is the share of the distance from chance to 100% that the text
actually covers, and is comparable across manuscripts.

### One token from each side of the break

| | straddling | chance | sigma | lift | headroom |
|---|---|---|---|---|---|
| **Rohonc, Király–Tokai** (words) | 37.14% | 18.23% | **39.3** | 2.04x | **23.1%** |
| Italian prose (words) | 25.24% | 9.64% | 23.0 | 2.62x | 17.3% |
| Hebrew prose (words) | 21.43% | 6.79% | 23.8 | 3.16x | 15.7% |
| Latin prose (words) | 12.41% | 5.68% | 16.4 | 2.18x | 7.1% |
| five-component model | 12.01% | 8.23% | 6.0 | 1.46x | 4.1% |
| **Voynich EVA** (words) | 6.46% | 5.85% | 2.1 | 1.10x | **0.6%** |
| **Voynich v101** (words) | 6.38% | 5.73% | 2.3 | 1.11x | **0.7%** |
| self-citation (Timm) | 14.16% | 13.69% | 0.9 | 1.03x | 0.5% |
| line-reset scribe | 8.54% | 8.50% | 0.1 | 1.00x | 0.0% |
| *Rohonc, 2014 (glyphs)* | *84.37%* | *76.70%* | *15.5* | *1.10x* | *32.9%* |

### Three tokens from each side

| | straddling | chance | sigma | lift |
|---|---|---|---|---|
| **Rohonc, Király–Tokai** (words) | 2.06% | 0.24% | **37.3** | 8.69x |
| Hebrew prose | 0.56% | 0.09% | 6.0 | 6.14x |
| Latin prose | 0.27% | 0.06% | 2.6 | 4.29x |
| Italian prose | 0.13% | 0.04% | 2.1 | 3.58x |
| **Voynich EVA / v101** | 0.00% | 0.00% | — | — |
| five-component, self-citation, line-reset | 0.00% | 0.00% | — | — |
| *Rohonc, 2014 (glyphs)* | *15.81%* | *4.88%* | *30.2* | *3.24x* |

Not one six-word sequence that straddles a Voynich line break occurs inside a
Voynich line. In the Rohonc, at the word level, one in fifty does; at the glyph
level, one in six.

## What this means

**The test works.** Pointed at a second manuscript in an unknown script, on two
transcriptions made years apart by different people by different methods, it
separates the two cleanly and in the direction it should. At the correct unit
the Rohonc sits inside the natural-language band — beside Italian and Hebrew,
above Latin — and the Voynich sits at the bottom with the meaning-free
generators. That is the positive control `RESULTS.md` never had.

**The mechanism.** The Rohonc repeats passages, and repeats them at different
positions relative to the line breaks. Text that is split across a break in
one place sits whole inside a line somewhere else. That is a direct
demonstration that the text exists independently of the lines it is written
on, which is what a real text laid out by a scribe looks like and what the
Voynich never once does.

## How much of the book is new

The cross-line result rules out tracing and line-by-line composition. It does
not rule out filling 448 pages by recycling earlier ones. So: how much occurs
only once?

Share of tokens inside a sequence of length k or more that occurs at least
twice anywhere in the book. The shuffle preserves the vocabulary exactly and
destroys only the order. All texts truncated to the shortest so the lengths
match.

| k = | 3 | 5 | 8 | 12 | 20 | 30 | 50 |
|---|---|---|---|---|---|---|---|
| **Rohonc, Király–Tokai** (words) | 37.3 | 15.8 | 7.5 | 3.3 | 1.2 | 0.4 | 0.0 |
| *shuffled* | 3.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hebrew prose | 33.9 | 4.6 | 0.8 | 0.2 | 0.2 | 0.0 | 0.0 |
| Italian prose | 17.0 | 0.7 | 0.1 | 0.1 | 0.0 | 0.0 | 0.0 |
| Latin prose | 7.7 | 1.3 | 0.9 | 0.6 | 0.6 | 0.6 | 0.0 |
| Voynich (words) | 2.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| *Rohonc, 2014 (glyphs)* | *85.1* | *57.7* | *23.7* | *10.0* | *3.4* | *0.8* | *0.0* |

At the word level the Rohonc is about three times as repetitive as Hebrew
narrative at k=5 and far more than Italian or Latin — not the tenfold the
glyph-level figures suggested, but still well outside every prose control.

### Nothing page-sized was duplicated

| longest sequence occurring twice | tokens |
|---|---|
| Rohonc, Király–Tokai (words) | 36 |
| Rohonc, 2014 (glyphs) | 44 |
| Latin prose | 31 |
| Hebrew prose | 27 |
| Italian prose | 14 |
| Voynich (words) | 4 |

A Király–Tokai line averages seven words, so the longest verbatim repeat in
the codex is about five lines. Coverage at k=50 is zero on both
transcriptions. **Bulk copying is ruled out**: a person padding a book by
recycling leaves repeats at the scale of what was recycled, and nothing here
repeats beyond five lines.

The first version of this document reported the glyph-level figure — 44
glyphs, about three lines — and called it a discrepancy with the seven-line
verbatim parallel Király and Tokai report between 133v07–134r02 and 101r04–09.
At the word level the longest repeat is five lines, and the gap is small enough
to be a difference in what counts as verbatim. The discrepancy is withdrawn.

**The missing control, still missing.** Every prose comparison here is
literary or narrative — Dante, Augustine, a Hebrew narrative — and none is the
liturgical genre the codex is claimed to be. Litanies and books of hours are
repetitive by design. Whether the Rohonc's repetition is abnormal *for what it
claims to be* cannot be said without one of those in the reference set.

## The mutual-information version, and a disagreement that dissolved

The first version of this document reported that the token-to-token
mutual-information test (`linebreak.py`) agreed with the n-gram test on
significance but disagreed on the proportion retained across a line break:
the 2014 glyph stream kept 22.4% of its length-matched within-line figure,
the Voynich 18.9% — nearly the same — while Italian kept 58.7%. Both measures
were reported because they disagreed, and the n-gram test was preferred on
sampling grounds.

At the correct unit there is no disagreement. Surrogate-corrected mutual
information in bits between one token and the next; `matched` is the
within-line figure on a random subsample the size of the across-break set.

| | within line | matched | across break | sigma | keeps |
|---|---|---|---|---|---|
| **Rohonc, Király–Tokai** (words) | 0.6897 | 0.3003 | 0.3510 | **41.2** | **116.9%** |
| Italian prose (words) | 0.3549 | 0.1028 | 0.0603 | 10.8 | 58.7% |
| Latin prose (words) | 0.1403 | 0.0281 | 0.0108 | 2.6 | 38.4% |
| self-citation (Timm) | 0.1765 | 0.0656 | 0.0237 | 2.3 | 36.2% |
| five-component model | 0.0881 | 0.0125 | 0.0029 | 0.5 | 22.8% |
| **Voynich EVA** (words) | 0.1706 | 0.0435 | 0.0082 | 1.5 | **18.9%** |
| *Rohonc, 2014 (glyphs)* | *1.4213* | *1.0613* | *0.2375* | *17.5* | *22.4%* |

At the word level the Rohonc's dependence across a line break is as strong as
inside a line — the retained share is above 100%, within the noise of a
subsampled estimate — where the Voynich retains a fifth at 1.5 sigma. The
glyph-level 22.4% was the finer unit talking: a glyph is to a Rohonc word
roughly as a letter is to a word, and letter-to-letter dependence across a
word boundary is weak in any script. Both measures now say the same thing, and
the one that had seemed to hedge was measuring the wrong unit.

## Is the decipherment real?

Király and Tokai announced a decipherment in 2018, published sample passages,
and have not published the translation. Király's 2022 paper says why: the
grammar paper is held up because "decipherment" in this case means the
dictionary and the whole text, and the dictionary is too awkward to typeset.
It is on the website instead. So it was verified — not by reading the codex,
which needs the unpublished grammar, but by the checks that come before
reading.

**Coverage.** The dictionary holds 885 codes after merging the 65 that carry
more than one homograph entry, 841 with a gloss. It covers 15.9% of the text's
word types and 62.1% of its word tokens: the common words are done, the long
tail is not. That is normal, not thin — the 979 commonest words of a real text
cover 78% of Italian, 68% of Latin and 61% of Hebrew at this length, and the
codex's own 979 commonest codes would cover 83%, so the dictionary is what
could be worked out, not what would flatter the number.

**The frequency profile, which is the evidence that convinced.** The twenty
commonest codes gloss as: and (also a place-value delimiter in numerals), this
/ he / you, and, be / there is, in / into, Lord, man, from / the, one / first,
say, come / go / send, all / every, son, disciple / teach, God (also a calendar
day), give / take, because / that, or / as / but, other / second / two,
Jew(ish). That is a function-word core in the proportions a language has, with
a gospel content vocabulary behind it. How often each code occurs is a property
of the codex its readers did not control; a wrong assignment of meanings would
not produce a Zipf-correct inventory of conjunctions, pronouns and copulas at
the top.

**A glossed page reads as doctrine.** Folio 104r, 78% covered, comes out as
Anne, born, blessed virgin, Lord, the Word, preach, miracles, Lord suffer for
man, the whole wide world, hell fire, be justified, all men be saved, be
damned, apostate — nine consecutive lines of coherent Christian content.
Király's own published example at 137v, "you bore the creator, you conceived
Jesus without sin", glosses independently to mother, God, lady, Mary, one,
only one, Jesus, without, pray, soul, forgive, amen, Hail Mary, have mercy,
Lord. It is a Marian prayer.

**Gospel-specificity, the least circular check.** The glossed vocabulary was
compared with a modern English translation of the four gospels and with a
general English corpus, by how much of each reference's top vocabulary it
recovers, after stripping grammatical metalanguage, folding accents and
stemming with a table of irregular forms. Four bugs in the first run of this
are recorded in the code: without the fixes the profile was topped by
"pronoun" and "delimiter", "Jézus" split into "j" and "zus", and "say" was
reported missing from a dictionary in which it is one of the commonest glosses.

| top k of reference | gospel | general English | ratio |
|---|---|---|---|
| 25 | 68.0% | 88.0% | 0.77x |
| 50 | 72.0% | 78.0% | 0.92x |
| 100 | 71.0% | 61.0% | 1.16x |
| 200 | 68.0% | 50.5% | 1.35x |
| 400 | 62.5% | 38.8% | 1.61x |

The commonest words of any English text are recovered by any dictionary; the
deeper into gospel-specific vocabulary the reference goes, the better the
glosses match it relative to English at large.

**Localisation, the one prediction their reading makes and did not have to
come true.** The dictionary glosses 101 codes as proper names, 78 of which
also occur in the gospel text. For each of the 247 pages carrying two or more
of them, the names sit a median of **60 words apart** in the gospel. Random
name sets of the same size sit 3,007 apart. **214 of 247 pages, 87%, are
tighter than the random median, against a 50% chance.** Codex pages localise
to gospel passages. If the name identifications were wrong, or the codex were
not following the gospels, they would scatter.

**What this does not establish.** None of it is independent confirmation of
the language. The transcription and the dictionary are theirs, and a dictionary
built by reading passages will read those passages back. A held-out split by
the folios each entry cites was attempted and failed — the citations are
"e.g." samples that cover 440 of 441 pages, so nothing was held out. The
non-circular evidence is the frequency profile and the localisation result.

**Where the remaining work is.** The undefined vocabulary is steeply
concentrated. The six commonest undefined codes are 4.7% of the entire text.
Defining the top 50 undefined codes would lift coverage from 62.1% to 73.1%;
the top 100 to 76.0%; the top 200 to 79.1%; the top 500 to 84.1%. That is a
work plan, and it is owed to the authors.

## Extending the dictionary: six attempts, six failures

Four words in ten have no gloss and another five in ten have several. Working
out the undefined codes is the part of the problem nobody has done. It was
tried six ways, each against a bar set before the run, and each failed. The
bar was never moved. Two evaluation bugs were fixed and the runs repeated;
neither fix changed a verdict. Five of the six were mechanical. The sixth was
not, and did best.

**Bag-of-words alignment.** Read each page by the words the dictionary
provides; find the gospel window it best matches. Real pages scored a median of
23.68 against 27.07 for random bags of the same words, and 3% of real pages
beat the random 95th percentile where chance is 5%. Pages align to the gospels
*worse* than noise. No signal.

**Neighbourhood enrichment.** Localise each page by its names; for a code,
collect the gospel words enriched near the pages it occurs on; hide sixty
codes the dictionary defines and try to recover them. True gloss ranked first
5% of the time, in the top five 12%, top twenty 21%. Worse than the rate, the
method returned the same candidates — lord, him, god, Jesus, son — for every
code asked about. No discriminative power.

**Sequence alignment.** Both earlier methods discarded word order. This
aligns each localised page against its gospel passage as two sequences, on the
words already readable, and reads an undefined code off the gospel words that
fall between the same two anchors. Bar set at 30% of held-out glosses in the
top five. First run: 7%. A fix to the evaluation, not the method — the aligner
proposed "spoke" for the code glossed "say" and was scored wrong, so irregular
verbs were folded — and a final run: 13 codes testable, true gloss first 8%,
top five 15%, top twenty 23%. **Fail.** Not moved.

**Distributional neighbours, gospels not used.** The first three all reached
an unknown code through the gospel text, which is the weak link: the codex
paraphrases rather than translates, draws on material the reference corpus does
not contain, and every comparison passes through two translations. So drop the
gospels and characterise a code by the codes around it, including the
picture-caption blocks excluded elsewhere, since Tokai read many codes off the
illustrations beside them. Hide a defined code, find its nearest neighbours by
context alone, ask whether a neighbour shares a gloss. First run hid the eighty
commonest codes at once and removed them from the context vocabulary too --
they are the function words that give every other code its shape, so hiding
them together destroyed the signal for all of them: 4%. Corrected to
leave-one-out, with the rest of the dictionary still standing: 76 codes tested,
nearest neighbour shares a gloss 0%, some neighbour in the top five 8%, top ten
14%. **Fail.**

There is signal in it. The code for God lands beside the codes for *god/holy*
and *father*; the code for *give/take* beside *carry/come* and *exist*. It is
real and far too weak to name anything.

**Reading the passage, which is what the other five were not.** All five
mechanical methods aligned or counted. Kiraly and Tokai do neither: they read a
passage, guess a code's meaning from what surrounds it, and check the guess
against every other place it occurs. `ktread.py` renders that evidence — every
line containing a target code, with all other codes glossed, so the target
stands as a blank in readable context — and six were read blind.

Six defined codes ranked 46th to 51st by frequency were used, deliberately
below the top forty, because the twenty commonest had been printed with their
glosses earlier in the same session and recalling them would not have been
reading. Result: one clean hit, one correct by cross-referencing an earlier
printout rather than by reading, one near miss in the right semantic field,
three wrong. **One to two of six, single-shot** — better than any mechanical
method, all of which reached 8–15% while allowed five guesses each, and still
far short of proposing anything.

The instructive failure is the one held with most confidence. A formula
repeated verbatim on two folios — glory and thanks given, then the target, then
"you" — reads unmistakably as a dative. The dictionary gives "end; side".
Clean reasoning, confident output, completely wrong, caught only by checking
against a known answer. A method whose failures are indistinguishable from its
successes must be scored on solved cases before it is pointed at unsolved ones,
which is why every attempt in this document was gated that way.

The failures are informative. The codex is a paraphrase drawing on apocrypha,
Marian prayer and material Király calls "without known parallel", glossed to
base-form English and matched against one modern translation of the canonical
gospels. Verbal overlap at the word level is genuinely weak even where the
localisation is right. What would make extension tractable is the grammar,
which chooses among a code's senses, and that is the part its authors have not
published. Whether it exists in finished form is unknown: four papers were
promised in 2018 and one has appeared, and the 2022 paper describes the grammar
paper as held up. The dictionary is demonstrably real. A written grammar is a
separate claim and nothing here bears on it.

What separates the sixth attempt from what Kiraly and Tokai do is not the
guessing — that part is shared, and unreliable for both. It is that a guess
there is carried to all seventy-five occurrences of the code and discarded if
it fails at any one of them, then made again the next day, with the
illustrations as entry points and a corpus of prayer, apocrypha and sermon
material in mind. This was one pass. Twenty years of disciplined guessing is
not an afternoon of it, and the discipline is the part that does the work.

## A third transcription from the scans: negative

The pipeline splits each scanned opening at the gutter, finds the lit page
against the dark surround, and segments lines by ink projection — 10.0 lines
per page against Király and Tokai's 11.2. It fails at word identity.

Word spacing looked separable on one line and is not: pooled over 14,301
blank runs from sixty spreads and scaled by line height, the distribution
decays smoothly with no gap anywhere, so there is no threshold the page picks
out. Two heuristics for choosing one produced plausible-looking output and
were wrong; both are recorded in `roho_ocr.py`. The threshold is swept instead.

Clustering word images into types then fails on resolution: a token is sixteen
pixels tall, the pen lands further off than that between two writings of the
same word, and no merge distance produced a vocabulary like either human
transcription's — type/token stayed at 0.998 where the human figure is 0.19.
So the labels were dropped and the cross-line test run on image similarity
directly, with the radius swept and chance measured at the same radius. Below
a radius of 0.20 nothing matches at all. At the loosest setting, 0.61%
straddling against 0.39% chance, 4.7 sigma, 0.2% headroom — a hundredfold
weaker than either human transcription, in the right direction, too close to
noise to lean on. The high-resolution colour scan exists and is restricted to
repository staff; with it, this would probably be feasible.

## Reproducing

    cd harness
    python rohonc.py          # the 2014 transcription, corpus statistics
    python rohonc_kt.py       # Kiraly & Tokai's, corpus statistics
    python roho_orient2.py    # orientation of the 2014 file
    python crossline.py       # the main result, both transcriptions
    python repeats.py         # how much of the book is new
    python linebreak.py       # the mutual-information version
    python ktdict.py          # dictionary coverage and the priority list
    python ktvalidate.py      # gospel-specificity
    python ktlocalise.py      # localisation of pages to gospel passages
    python ktextend.py        # the two failed extension gates
    python ktalign.py         # the third, sequence alignment
    python ktdistrib.py       # the fourth and fifth, distributional
    python ktread.py --hide 6 --skip 45   # the sixth, reading from context
    python ocr_crossline.py   # the scan-based attempt (slow)
    python check_rohonc.py    # every figure above, against the saved runs

Saved outputs are in `work/rohonc/`. The Voynich gate (`python gate.py`) is
unaffected by any of this and still passes.

## What this does not decide

Nothing here reads the Rohonc, and nothing here confirms Király and Tokai's
reading of any particular passage. It says the text runs across the margin the
way a real text does, that the dictionary has the shape a real one would, and
that the pages fall where a gospel paraphrase would put them. It does not say
what any page says.

It also does not close the Voynich question. It removes one doubt — that the
line-break measurement might find "the line is the unit" in any manuscript you
point it at — and that doubt is now answered on two transcriptions.

## Credit

The 2014 transcription is the work of an anonymous author who published it
openly and whose site is gone. Levente Zoltán Király and Gábor Tokai made the
transcription and dictionary this document leans on hardest, published them so
that their claims could be checked, and are owed the priority list above and
an email. Ottó Gyürk (1970) first analysed line breaks in the codex's repeated
sequences, the idea the orientation test and the main result rest on. Levente
Zoltán Király and Gábor Tokai, *Cracking the code of the Rohonc Codex*,
Cryptologia 42:4 (2018), 285–315; Levente Zoltán Király, *A Rohonci kódex
teológiai karaktere*, in *Hagyomány, Identitás, Történelem 2022*, KRE HTK,
Budapest 2023, 363–376. Benedek Láng, *The Rohonc Code: Tracing a Historical
Riddle* (Penn State Press, 2021), is the standing survey.
