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

## Extending the dictionary: seventeen attempts, a ceiling, and a way in

Four words in ten have no gloss and another five in ten have several. Working
out the undefined codes is the part of the problem nobody has done. It was
tried seventeen ways. Fourteen failed outright. The tenth narrowed one code to a
grammatical class and a semantic field without naming it. The twelfth and
thirteenth passed, and between them they read 19% more of the book. The
fourteenth failed its gate and still recovered 1.2% of the book, because what
it recovered was Király and Tokai's own, not an inference. The bar
was never moved. Two evaluation bugs were fixed and the runs repeated;
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

**The rejection loop, which is what the other seven were missing.** Reading
gave one to two of six. Kiraly and Tokai's first-pass rate is probably no
better. The difference is that a guess there is carried to every occurrence of
the code and discarded if it fails at any one, and no attempt here had built
that step. `ktreject.py` built it as a distributional score and failed at 5% --
the same mistake a third time, reaching for vectors where the method calls for
reading. `ktread.positional()` builds it properly, and it works.

Run on the commonest undefined code in the book, 539 occurrences:

*Himself*, from "can show [?] in Capharnaum", "[?] truly Son of God", and
"circumcised [?] in Jerusalem". Carried to folios past 60 it reads "himself
dinner", "himself other disciples", "himself Abraham Abraham". **Rejected.**

*A determiner*, since it sits immediately before a noun again and again.
Its commonest followers are "in" (44), the numeral delimiter (39) and "and"
(33); it opens a line 72 times and closes one 70. No article behaves so.
**Rejected.**

Two confident readings, two rejections, both on internal evidence alone, in two
cycles. Three more followed on the two commonest undefined codes, with the
frame evidence `ktsolve.py` assembles. The first follows "say" 66 times and
"show" at 25x above chance, which reads as a quotative — but only 70 of its 539
occurrences sit next to a speech verb, so the 2.16x lift is real and the
absolute rate kills it. The second follows the numeral delimiter in 329 of its
468 occurrences, which reads as a digit — but it precedes a delimiter only 4
times, and a digit would appear on both sides, so it is something
sentence-initial instead. A fixed pair of undefined codes occurring together
127 times looked like a Passion formula in the folios where its contexts were
first printed; across the whole book it is spread through every band but one,
so it is grammatical, not narrative. Rejected, rejected, rejected. Rejection is cheap and reliable exactly where generation is not, which
is the asymmetry the whole method runs on. It also did not converge: after two
cycles on the single most testable code in the book, there is still no answer,
and 127 of that code's appearances sit beside one other undefined code -- a
collocation that is itself a finding and not a meaning.

**Targeting, and a ninth rejection.** Gate 2 above failed partly on method
and partly on aim: it treated every undefined code alike, and a function word
spread evenly through the book has no neighbourhood to be enriched in.
`kttopical.py` separates them by how far a code's distribution departs from the
book's own across twenty-folio bands. Of the 47 undefined codes occurring 25 or
more times, the two most concentrated sit *entirely* within folios 140–159 —
100% of 33 and of 31 occurrences — while the flattest have no band holding more
than 15%.

That is a real filter, and it surfaced a real hypothesis. Folios 144–148 are
densely about virgins, maidens, women, servants, prayer, fasting and
forgiveness, with a formula repeating four times that reads as "the kingdom of
heaven", and one line placing the target between that formula and "virgin".
Read as "like" — *the kingdom of heaven is likened unto* — it fits six of its
twenty-seven occurrences and breaks on the rest, appearing twice in a single
line on three separate folios. **Rejected.**

What survives is a finding about the codex rather than a code: that stretch is
about virgins, maidens and the kingdom of heaven, which is consistent with the
parable of the ten virgins and does not depend on any code being solved.

**A tenth attempt, and the one thing that has not broken.** `ktclass.py`
drops the attempt to name a code and asks only what *kind* of word it is,
fingerprinting it against classes built from Kiraly & Tokai's own glosses.
Gated first: held-out defined codes are classified at 57.8% against a 46.9%
majority baseline — a pass by less than a point, and *below* base rate on
grammatical words at 38%. Weak, and reported as weak.

Applied to the code that concentrates in folios 0–19 (35 occurrences, 71%
there), it returns **noun**, on a method 61% accurate for nouns. That code is
the one result of ten attempts that has survived a held-out test. Lines
containing it carry adversary vocabulary — Lucifer, Satan, demon, Antichrist,
the snake — at 10.5× the book's rate, and throne/above words at 12.6×. The
adversary association is not an artefact of the section that suggested it: in
the ten lines where the code appears *outside* folios 0–19, adversary words
still run **12.1× above chance**.

So: probably a noun, in the adversary field, with the association holding out
of sample. That is a narrowed field and not a meaning. *Devil*, *serpent*,
*dragon*, *enemy*, *pride*, *temptation* and a dozen others all still fit, and
naming one would be precisely the confident nonsense that produced "end; side"
earlier in this document. It is recorded at the strength the evidence carries
and no further.

**The ceiling.** The eighth line of attack, reading the illustrations, is how
Tokai found his entry points, and the scans make it available: folios map to
scan pages (a pencilled "42" on the left leaf of scan page 43 fixes it), and
the pictures are legible. It ran into something more basic. Of the eight
undefined codes in the picture caption on 042r, four occur exactly once in the
whole codex. A guess about them can never be carried anywhere, so it can never
be rejected -- not by this harness and not by anyone.

That is general. `ktceiling.py` measures it: 2,885 undefined codes occur exactly
once, carrying 9.6% of the book. If a code needs three occurrences to be
checked against itself, that kind of verification tops out at 86.4% coverage;
at five occurrences, 82.3%. Picture captions concentrate the one-off codes,
because a caption names what appears once — which is why Tokai read *names* off
the illustrations, names being the thing that recurs.

**That is a ceiling on self-verification, not on decipherment, and an earlier
version of this document said otherwise.** A one-off code cannot be carried to
its other occurrences because it has none, but it is still constrained by the
sentence around it, by a gospel parallel where the passage localises, and by
any picture beside it. Those constraints tighten as the rest of the dictionary
fills in, so the residue is not a wall but the last item in a sequence.
`kthapax.txt` measures the effect: today a one-off code sits in a line 60%
readable and only 4.9% sit in a fully readable sentence; solve every code with
three or more occurrences and the median goes to 83%, two thirds sit in lines
at least 80% readable, and **36.6% sit in a sentence where every other word is
known**. That is the order the work has to be done in, and it is how Linear B
finished — the one-off place names fell out once the grammar and common words
were settled.

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

## The eleventh attempt, and a corpus that was not the problem

Two things were tried after the class fingerprint, and both failed. They are
recorded because the second one was a specific prediction that turned out to
be wrong.

**Do codes inherit meaning from the codes inside them?** 84% of undefined
codes contain a shorter defined code as a contiguous substring, which is 35%
of the book by tokens, and nobody had asked whether that containment carries
meaning. It does not. Of 416 defined codes containing a defined code, 1.4%
share a content stem with the code inside them, against 0.3% for a shuffled
control: a ratio of 4.94 but only 4.7 sigma, against a bar of twice the
control and 5 sigma set before the run. **Fail**, and the absolute rate makes
it worse than the sigma does. Six real hits is not a method. Looking at the
pairs shows why: the recurring initial signs open "denarius", "sin", "body",
"blind" and "foot" alike. They are not morphemes. Code: `ktmorph.py`.

**Was the aligner pointed at the wrong book?** The third attempt, sequence
alignment, scored 15% against a 30% bar using the four canonical gospels as
its reference. Király's 2022 paper says the codex is gospel paraphrase
"intertwined with apocryphal scenes of the Virgin Mary, prayers, Old Testament
reminiscences, allegorical expositions, and stories from the lives of saints",
and names folios against specific sources: Seth at the gate of paradise (7v),
the destruction of Jerusalem (111r-112r), the Invention of the Cross
(182v-186v), Augustine and the boy on the shore (84r-v) and Barlaam's parable
(148r-149v) all come from the Golden Legend; Lucifer sitting on God's throne,
the Nativity details and the idols falling before the holy family in Egypt all
come from the mystery cycles. The bag-of-words result supported the suspicion:
real pages matched the gospels *worse* than shuffled bags of their own words,
which is what a wrong reference looks like rather than a hopeless method.

So the reference was rebuilt from the sources the paper names: the whole King
James Bible, Wake's apocryphal New Testament, the York, Towneley, Chester and
N-Town play cycles and Caxton's Golden Legend, 1,746,498 words in all. The
aligner was not touched. Its one slow step was rewritten to use bisection
instead of a linear scan, and the gospels-only run was repeated first to prove
the rewrite changed nothing: 8% / 15% / 23%, identical to the saved baseline.

On the wider corpus the same bar produced 4% first, **13% in the top five**,
13% in the top twenty, on 23 testable codes rather than 13. **Fail**, and no
better than the gospels alone. The corpus was not the problem. The prediction
was mine, it was specific, and it was wrong. What remains is the explanation
Király gives himself: the author worked from hearsay, gets biblical citations
wrong, and tells stories in variants that exist in no known source.

Code: `ktextend.py` takes the reference from `ROHONC_REF`; the corpus builder
and both runs are in `work/rohonc/ktalign_gate_wide.txt`.

## The twelfth and thirteenth: the codes are phrases

Every attempt so far treated a code as an atom — an opaque symbol with a
meaning to be guessed. That was the mistake, and the 2022 paper says so in
passing. Describing folio 137v it notes that the codex does not inflect:
instead of a pronoun or a conjugated verb, "the sign of the subject's name
consistently stands", and it prints a line as `... bűn nélkül Jézus fogan
te-Mária` — sin, without, Jesus, conceive, you-Mary — where *you-Mary* is
written as a single code.

That code is E569 E607. Both halves are in K&T's own dictionary: E569 is the
second person singular pronoun with 932 occurrences, E607 is Mary. The
compound is not in the dictionary. It is a phrase written without a space.

The construction is not rare. Name signs are the most productive final
elements in the book:

        Lord      577 alone    1038 inside longer codes
        Jesus      89 alone     558
        Mary       59 alone     137
        Christ     52 alone     111
        Satan     156 alone     100

Nearly every one of those compounds is undefined.

**The twelfth attempt tests the construction without using K&T's glosses at
all.** If a code ending in a name sign refers to that name, it should occur
where the name occurs. For every undefined compound with five or more
occurrences, all 37 candidate name signs were ranked by how well their own
page profile matched the compound's, and the rank of the name the compound
actually ends in was recorded. The control repeats the test on codes matched
on frequency that do *not* end in a name sign, holding the book's topical
structure, the profile measure and the frequency fixed.

The bar, set before the run: the true name first for at least 40% of
compounds, at least twice the control, at least 5 sigma. Result: **43.9%
against 6.3%, a ratio of 6.94 at 12.4 sigma. Pass** — the first clean pass in
twelve attempts. Code: `ktname.py`.

**The thirteenth reads them.** If the compounds are phrases, a code should cut
into a sequence of dictionary codes and read as the sequence. The first gate
for that failed: of the codes K&T define, only 32 can be cut into other
defined codes at all, and 3.1% of those have a composed gloss that hits the
true gloss, 1.4 sigma. That is a fail and it stays one, but the held-out set
is the wrong population — K&T define words, and the codes they left undefined
are precisely the phrasal ones, so almost none of the construction under test
is in the sample.

A second gate was declared before it was run and tests the same claim on the
population that matters, using distribution instead of glosses. If [A][B]
means A combined with B, the compound should sit where A and B sit. Bar: the
compound closer to its own parts than to frequency-matched stand-ins for at
least 60% of codes, at least 5 sigma. Result on 316 codes: **77.5% against
47.4%, 9.8 sigma. Pass.**

So two independent gates hold, one on names and one on parts generally.

**What it reads.** 1,282 of the 4,247 undefined code types cut cleanly into
dictionary codes. They carry 5,754 tokens — 46% of the undefined text and 19%
of the whole book. Coverage goes from 58.4% to **77.6%**.

The commonest of them are not obscure:

        534   Lord + Jesus
        301   <genitive> + Lord
        224   Lord + <divine-name suffix>
        109   holy + Word
         71   Lord + Jesus + Christ
         70   from + father + <divine-name suffix>
         62   virgin + Mary
         43   holy + Pentecost
         34   holy + Luke
         30   holy + John

Lord Jesus Christ, the Virgin Mary, Saint John, Saint Luke, God the Father,
the Holy Word. A devotional book reading as one.

The rendering picks one sense per part and sometimes picks badly — K&T list
"widow" alongside "virgin" for E870 — so the glosses above are the
construction, not a finished translation.

**Code C is resolved.** The one survivor of the first ten attempts, 35
occurrences, 71% in folios 0-19, classed as a noun in the adversary field with
a held-out association at 12.1 times chance, is E950 EB61. EB61 is K&T's sign
for angel / Lucifer / Satan. E950 is their "hide oneself". The adversary lift
was never a semantic field to be inferred; the code contains the word Lucifer.
What is left is the exact sense of the prefix, not the identity of the word.

**What is new here and what is not.** The grammar is Király and Tokai's: they
describe it, and they print the *you-Mary* example this work started from.
What is new is that the construction is confirmed independently of their
glosses, at 12.4 and 9.8 sigma against matched controls, and then applied
across the whole book to produce 1,282 readings their published dictionary
does not contain. The check that matters ran in the other direction too: the
composition rule, applied blind to folio 137v, reproduces their published line
— sin, without, Jesus, conceive, you-Mary — in order.

Code: `ktname.py`, `ktsegment.py`. Saved runs: `work/rohonc/ktname.txt`,
`work/rohonc/ktsegment.txt`.

## So how much is translated?

Not 77.6%. That figure is coverage, and coverage is the weakest of three
claims worth separating.

**Words with any reading at all: 77.6%**, up from 58.4%. That counts a token
if K&T gloss it or if it cuts into codes they gloss. 6,730 tokens, 22.4% of
the book, still have no reading of any kind.

**Words that are actually translated: 11.5%.** Most codes K&T define carry
several senses — *away / to*, *angel / Lucifer / Satan*, *believe /
misunderstand* — and choosing between them needs the grammar, which is the
paper they have not published. Only 3,456 tokens carry exactly one sense and
so need no choice made. The other 19,811, **66.0%** of the book, are located, not translated.

**Lines in which every word has a reading: 20.6%**, up from 2.8%. This is the
number that matters most, because a sentence with one unreadable word in it is
not a sentence you can read. It went up sevenfold. Lines that are at least
80% readable went from 12.9% to 50.8%, and the median line went from 57.1% to
80.0% readable.

        tokens with any reading      58.4%  ->  77.6%
        tokens with a single sense             11.5%
        lines fully readable          2.8%  ->  20.6%
        lines 80% readable           12.9%  ->  50.8%
        median line                  57.1%  ->  80.0%

The shape of the problem has changed. Before this, the obstacle was missing
vocabulary: four words in ten had no entry. Now two words in ten have no
entry, and the obstacle is that 66.0% of the book consists of words with
several candidate senses and no published rule for choosing. More dictionary
work will not fix that. The grammar will.

Code: `ktcoverage.py`. Saved run: `work/rohonc/ktcoverage.txt`.

## Can the sense be chosen, and can the grammar be abstracted?

Two more gates, both failed, and the second failure is the informative one.

**Choosing a sense from context.** Token-weighted, the average word in the
book offers 4.75 senses. `ktsense.py` scores each candidate against the words
around it using pointwise mutual information over the 1,746,498-word reference
corpus, then hides the sense of the 485 codes that carry only one and asks the
method to pick it out of five. Bar set before the run: 40% against 20% chance,
and 5 sigma. Result: **39.9%, at 22.8 sigma.** The signal is unmistakable and
the bar is missed by half a point. **Fail**, and not moved.

Two things make that worse than it looks. The judge is a bag of word
associations, which is crude. And the gate is easier than the real job: a
code's own senses sit **2.50 times** closer to each other than random senses
do, so 39.9% is an optimistic ceiling rather than a floor.

An earlier version of that script was not deterministic. K&T's gloss values
are sets, iterating a set of strings varies between processes, and the verdict
moved across the bar between runs. Every sense set is now sorted and three
hash seeds give 39.9% exactly. A gate that cannot reproduce is not a gate.

**Is there anything there to choose?** If a code's senses are not conditioned
by context, no better chooser can exist and the question is closed. For codes
with 20 or more occurrences, `ktgrammar.py` splits each code's occurrences in
two by context and measures the variance explained. Multi-sense codes explain
15.7%. Single-sense codes matched on frequency explain **16.2%**. Ratio 0.97,
sigma **-1.2**, against a bar of 1.15 and 5 sigma. **Fail**, decisively and in
the wrong direction.

**What that does and does not license saying.** The obvious reading is that
K&T's multiple senses are mostly not ambiguity at all but one concept written
in whatever English part of speech the sentence needed, which would mean the
66.0% figure overstates the problem badly. The codes that split best look
exactly like that: *Creator, create, creation, creature*; *book, scripture,
write*; *debt, debtor, indebted*; *place, put*; *fire, flame*; *Word, gospel*.

That reading was tested and the test does not support it. Counting codes whose
senses share a word stem gives 0.5% of multi-sense tokens where every sense
shares one and **68.7% where none do**. On its face that says the senses are
genuinely distinct.

But the instrument is wrong, and the same run shows it. Every one of the
non-sharing examples it prints is a set of near-synonyms: *boy, son*; *second,
the others, the rest, two*; *all, whole, each, every, wholly, completely*;
*beg, pray, prayer*. English synonyms almost never share a stem, so a stem
test cannot see synonymy, and 68.7% is measuring the English wordlist rather
than the Rohonc word. The similarity measure in `ktsense.py` is the better
instrument and points the other way at 2.50 times.

So the honest state is that the 66.0% is probably too pessimistic and it has
not been shown. What would settle it is a semantic measure rather than a
lexical one, applied to every multi-sense entry. That has not been run, and
until it has, 11.5% stands as the translated figure and 66.0% as the located
one.

Code: `ktsense.py`, `ktgrammar.py`. Saved runs: `work/rohonc/ktsense.txt`,
`work/rohonc/ktgrammar.txt`.

## The fourteenth: variant spellings

What is left unread has a shape. Of the 22.4%, 31% is words that occur once,
which no statistical method can reach and which in a real book are names,
numbers and rare words. But 53% of it sits within one glyph of a code the
dictionary defines: one glyph substituted, dropped or added. The book's
commonest unread word, 337 occurrences, differs from *and* by its last
glyph. Some of those are variant spellings. Some are different words that
share two glyphs out of three.

Király and Tokai's dictionary marks variant spellings itself, with "var."
followed by the variant code. The loader keyed entries by headword and
dropped them. 88 of the codes so marked are in the text and were unread, 356
tokens, 1.2% of the book. Those are their readings and go in without a test,
marked with a tilde on the page. *from-father ~Adam bow_down Lord* on the
opening folio is one of them.

They are also the calibration for the larger question. If a variant spelling
sits where its headword sits, the declared variants must show it first.
`ktvariant.py` tests each declared variant's page profile against its
headword and against a frequency-matched stand-in, then does the same for
every unread code with three or more occurrences that is one glyph from
exactly one defined code. Both bars set before the run: 60% wins and 5 sigma.

    BAR A  K&T's declared variants        23 tested   60.9% vs 37.9%   2.6 sigma   FAIL
    BAR B  undeclared one-glyph neighbours 98 tested   53.1% vs 34.7%   4.8 sigma   FAIL

Bar A fails, so the instrument cannot see variants at this sample size and
bar B is not a result either way. Nothing is inferred. The 98 neighbours, 926
tokens, 3.1% of the book, stay unread. The signal in both rows is real and
points the right way, and the bar is the bar.

Coverage goes from 77.6% to 78.8%, all of it theirs. Saved run:
`work/rohonc/ktvariant.txt`.

## The fifteenth and sixteenth: working backwards from the parts that are right

Once the book could be read it became possible to ask the question a
cryptanalyst would ask first. Some of the reading is certainly correct. Which
parts, decided by something other than my say-so, and what can they prove?

**The fifteenth: substitution frames.** Where the codex repeats a passage,
breaks for exactly one code, and resumes identically, the two odd codes stand
in the same slot of the same sentence. `ktanchor.py` finds those frames. The
gate was declared at a context radius of three codes either side, and it
returned **no testable case at all** — eleven frames in the whole book and
none with both codes defined. That is not a near miss, it is a gate that
cannot be run, and it is recorded as one rather than quietly re-declared at a
radius that has cases. Run afterwards at radius two, and therefore not a
pre-registered test, eighteen frames are testable and one shares a stem.

Looking at what the frames contain shows the question was wrong again, in
exactly the way `ktmorph.py` was wrong:

    tax collector ~ scribe ~ prophet ~ sheep
    Joachim ~ Satan
    who ~ that ~ and

Those are not noise. They are paradigms — the kinds of thing that can stand
in one place in one sentence. A substitution frame finds word class, not word
meaning, and asking it for synonyms was the mistake.

**The sixteenth: anchors against the reference corpus.** `ktverse.py` scores
every line of the codex against the 1,746,498-word corpus and takes the top
5% by match as anchors, which is a rank rule and not a threshold that can be
tuned afterwards. The gate, declared first: hide a defined code from an anchor
line, relocate the passage using only the remaining codes so the hidden word
plays no part in finding it, and ask whether the hidden gloss is in the window
that comes back.

    held-out codes tested                 925
    gloss found in the relocated window   15.5%
    same test against a random window      4.1%
    ratio 3.75x    sigma 18.5             BAR 40% -> FAIL

Real signal, 3.75 times the control, and nowhere near the bar. Nothing is read
from a located passage by that route, and the bar was not moved.

**The seventeenth: the refinement, done so that it could not be tuning.**
The anchors were split by rank, odd to a development half and even to a test
half. The failure was diagnosed on the development half only, three ways —
by anchor strength, by whether hiding the word moved the located window, and
by what kind of word was hidden — and a selection rule declared in advance
picked the single best cut. Then the test half was scored once, against the
same bar.

    development half, all cases          16.6%
      top 25 anchors                     24.1%
      window stable / moved              20.6% / 6.9%
      name / concrete noun / other       28.6% / 22.9% / 14.4%
    selected rule: the hidden word is a proper name

    test half under that rule: 26 cases
      recovered   30.8%    control 2.2%    13.8x    9.7 sigma
      BAR 40%  ->  FAIL

That is the answer to whether the method can be refined. Even the easiest
words, proper names in the strongest anchors, come back less than a third of
the time, and no cut on the development half reached the bar either. The
reason is not localisation, which is mostly stable, and not weak anchors. It
is that the reference corpus is not the codex's source. The book paraphrases
a text we do not have, and an English Bible and English plays share its words
only when the passage is close to verbatim. The two parables above are the
cases where it is.

**What the anchor finder did do.** It located 213 lines, and the strongest
were passages I had not reached by translating in order:

    135r   the parable of the Unmerciful Servant      Matthew 18:23-35
    119r   the parable of the Lost Sheep              Luke 15:2-5
    080v   a citation of Saint Luke, chapter two
    017v   Joachim and Anne at the Golden Gate
    007v   the creation of Adam and Eve

Two of those carry their own confirmation, independent of anything I read.
Kiraly and Tokai's dictionary contains a code they gloss "adjective of the
unmerciful servant", and it stands in 135r exactly where the fellow-servant
stands; their dictionary also has *denarius*, the coin of that parable. And
119r writes *ninety and nine* the way Luke writes it, ninety followed by nine,
with ninety spelled nine-ten — a fifth independent confirmation of the numeral
rule, from a page found by machine rather than chosen by me.

**One code read the old way.** In 119r an undefined code stands in the three
places the lost sheep belongs. It occurs four times in the whole book; the
fourth is beside the word *soul*. "Lost" works in all four. That is Kiraly and
Tokai's own method, carrying a guess to every occurrence and keeping it only
if it survives everywhere, and it is one word, not a method.

Saved runs: `work/rohonc/ktanchor.txt`, `work/rohonc/ktverse.txt`, `work/rohonc/ktverse2.txt`.

## The rendering

All of the above is put on the page. `kttranslate.py` writes the whole book
in Király and Tokai's page order, one line of the codex per line of text,
with every word rendered one of five ways and marked so the reader can see
which. A dictionary word with one sense is printed as that sense. A
dictionary word with several is printed as the sense they list first, and in
the full version every sense follows after a slash. An undefined code that
cuts into dictionary codes is printed as its parts joined by hyphens. A
variant spelling their own entry declares is printed as the headword with a
tilde. A word with no reading is printed as `[?]`, and in the full version
the glyph codes follow.

The senses are printed in the order Király and Tokai list them, because
their first sense is their headline sense. The shortest-sense rule that
`ktsegment.py` uses for its readings table picks "so" for the pronoun they
gloss "this / you", "exist" for the copula and "lord" over "Lord", and a
whole page of that does not read. Their order gives *sun and moon write*,
*Elijah prophet say angel God*, *sit on throne from-father God*.

    words                          29997
      one sense                     3440   11.5%
      several senses               14233   47.4%
      by composition                5811   19.4%
      their variant spelling         357    1.2%
      no reading                    6156   20.5%
    lines                           4372
      every word read               1041   23.8%

Those are the coverage figures of the previous sections, seen from the
page, with the declared variants and the clause terminator applied. They are
Kiraly and Tokai's dictionary alone; this project's own readings are counted
separately below. The only difference is that 52 composed words whose every part has one
sense are counted with composition here and with the single-sense words in
`ktcoverage.py`, which is where the 11.3% and 11.5% part company.

It is a rendering, not a translation. Nothing in it chooses between senses,
and the section above shows that context cannot do that choosing, so a reader
has to. What it gives that reader is the whole book on one page, with every
word that can be read, marked by how much to trust it. Folio 137v, the page
Király and Tokai published, reads on it as *healing-girl through holy-Mary
mother God*, *Mary one only_one virgin-girl this-Mary Jesus without*, *be_born-
Mary and from Lord-redeemer inside Lord*, with the author's name sign
following *this* and the genitive down the right margin.

Output: `work/rohonc/translation/rohonc_reading.txt` (first sense only) and
`rohonc_reading_full.txt` (every sense). Code: `kttranslate.py`. Both files
are built from their dictionary and stay private with the rest of the work
until they are asked.

## What the book says

With the rendering on the page it became possible to read it, and 105
folios are translated in `work/rohonc/translation/rohonc_translation.md`.
The content was not what this project assumed. It is not a gospel harmony.

The opening is the **Life of Adam and Eve**, the apocryphal one and not
Genesis, because the episode that distinguishes it is there: God commands the
angels to bow to Adam, and Lucifer refuses and falls. Then the expulsion, the
flaming sword, Cain, Abel and Seth, Adam going blind, and Seth's journey back
to Paradise for the branch, which is the Legend of the Rood. Then Noah, then
Abraham and Isaac with the ram in the thicket. Then Joachim and Anne, the
refused offering and the meeting at the Golden Gate, which is the
Protevangelium by way of the Golden Legend. Then the Annunciation, the
Nativity, the flight into Egypt, a numbered catalogue of the signs the Lord
showed, the Transfiguration, the baptism, and from folio 029r the Passion,
which the codex itself says it takes from Saint Matthew and Saint John.

The frame is a revelation: the angel of God speaks, and **Elijah the prophet**
is the one addressed by name.

Three things in it are checkable without any dictionary at all. A prophecy
passage recurs word for word at 005v, 017r and 017v, spoken to Abraham, to
Joachim and to Anne. The Nativity is told twice in the same words, at 020v and
025v. And John 18:4-8, where Jesus asks "Whom seek ye?", is asked twice in the
codex exactly as it is asked twice in John.

**The numerals resolved.** The parts add, and a `ten` after a group multiplies
it by ten. Four independent checks against a number the source supplies:
`ten-ten-ten-ten` and `two-two-ten` are both forty, at forty days and forty
nights and at the forty days of rain; `six-two` is eight, at the circumcision
on the eighth day; `six-six` is twelve, at the twelve apostles.

**A grammar rule came out of it.** The code Kiraly and Tokai gloss
"introducing the next item in a list" makes an ordinal when it stands in front
of a numeral. The book uses it to number the signs of Christ from first to
eleventh and the witnesses who confessed him. That rule was read out of the
text, not imported, and it is the second construction this project has
recovered after the name-compounds.

**More of what it is, from the Passion folios.** From 029r the book follows
Matthew and John closely -- Malchus named and his ear put back, Caiaphas's
counsel that one man should die, Peter's three denials counted first second
third with the cock, Pilate and Herod, the basin, Barabbas, the purple robe
and the crown, twelve legions of angels, the title on the cross and "what I
have written I have written", the ninth hour, the sponge on the stick. But
two passages are not gospel at all. Folios 048r-048v are the **Improperia**,
the Reproaches sung on Good Friday: *O my people, what have I done unto thee?
I brought thee out of Egypt, I divided the sea, I led thee forty years in the
wilderness, and thou hast prepared a cross.* And 052v is **Longinus**, the
blind soldier whose sight is restored by the blood from the spear wound,
which is the Golden Legend. So the book draws on the liturgy and the legendary
alongside the gospels, which is what a late-medieval devotional compilation
does and what the reference corpus was rebuilt from.

**The method that finally reads new words.** Seventeen gated attempts
produced none. What produces them is Kiraly and Tokai's own loop, written up
in `METHOD.md` and tooled as `harness/ktcontext.py`: guess a sign from a
passage whose story is known, then carry the guess to every other occurrence
in the book and keep it only if it survives all of them. 95 signs are read
this way in `harness/proposals.json`, each with the folio and line of its
decisive occurrences, graded A, B or C. 23 are tier A. They include the tally
numerals one, three and five, the ordinal third, the cross (and with it the
composition of the sign for crucified), bread, law, the subject marker, "on
the third day", Nazareth, "be saved" and "believe". Rendered into the book
with a plus sign so they can never be mistaken for Kiraly and Tokai's, they
take the share of lines where every word is read from 23.8% to **51.6%**.

Most of that last jump cost no guess at all. `ktsegment.py` cuts a compound
into pieces Kiraly and Tokai define; it was never given their own variant
spellings, this project's read signs or the clause terminator as pieces.
Cutting with the full readable inventory and repeating until nothing new
appears took fully-read lines from 36.1% to 47.4% in one step, because every
part of every compound had already been read on its own evidence.

**One of them is not a word.** E034 ends 293 words the dictionary does not
define, and 99.7% of those words are the last word of their run, against
16.7% for words in general. Nothing else in the book has that signature; the
next strongest candidate is run-final 55% of the time. So E034 is a clause
terminator, not a word, and every word carrying it is its stem plus a full
stop. That is a rule rather than a guess, it was measured rather than
supposed, and it read 134 word types at once. `harness/ktaffix.py` holds it,
and the renderer, the gap finder and the context printer all use it.

**A third engine, and there is no floor.** A sign that occurs once cannot be
checked at a second occurrence, and for a while this document treated that as
a wall. It is not one. A one-off sign is a missing word in a sentence, and it
is read the way any missing word is read, as soon as everything around it is
readable. `harness/ktgap.py` counts those lines: **1,528 lines, 35% of the
book, are currently exactly one word short**, and 585 of the missing words
occur once. A further 1,010 lines are two words short and open as soon as one
of the two is read. So translating, reading signs and filling gaps each make
the next one easier, and the limit is not a share of vocabulary but how much
of the book has been worked.

**Would another language be easier? Measured, and mostly no.** Kiraly and
Tokai serve their dictionary in Hungarian as well as English, and it was
fetched to settle a question this document has carried unresolved: whether
the multiple senses per code are an artefact of English. The reasoning was
that Hungarian is agglutinative, so *righteous, true, indeed, righteousness*
would collapse onto one root where English splits them. Counting codes whose
senses share a stem, over the multi-sense tokens of the text:

    English, stemmed            0.9% all share   35.0% some   64.1% none
    Hungarian, 3-char stem      6.3%             37.7%        56.0%
    Hungarian, 4-char stem      7.2%             26.8%        66.0%
    Hungarian, 5-char stem     10.0%             25.9%        64.1%
    Hungarian, 6-char stem     12.4%             19.2%        68.3%

Hungarian is somewhat more unified at the top -- the share where *every*
sense shares a root goes from 0.9% to between 6% and 12% -- but the bulk does
not move. Between 56% and 68% of multi-sense text has senses that share no
root in Hungarian either, against 64% in English. **That is a second wrong
prediction of mine on the same question, and it is recorded rather than
dropped.** The senses are real, not translation noise.

Where the language should still matter is the other failure. The anchor gate
recovered a hidden word 18.4% of the time even where the source passage was
verbatim, and the explanation offered was that the codex paraphrases a
non-English text while the glosses are English. That explanation is now
testable: run the same gate with the Hungarian glosses against a Hungarian
corpus of the right period. The corpus would be the Hungarian codices of the
1500s. Nothing here has done that, and until it is done the 18.4% ceiling
stands as measured.

This is a translation of their dictionary over their transcription, not their
translation, which is unpublished. Every gloss is theirs. The sentence-making
is ours and is the part most likely to be wrong: context cannot choose between
senses, as the two gates above showed, so a reader chooses, and this reader's
blind score on held-out codes was one to two right in six. Single lines are
proposals. The story-level reading rests on many lines agreeing.

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
    python ktreject.py        # the seventh, rejection scored distributionally
    python ktceiling.py       # the ceiling on self-verification
    python ktsolve.py 3       # frame evidence for the top undefined codes
    python kttopical.py       # which undefined codes are worth attacking
    python ktclass.py         # what kind of word an undefined code is
    python ktmorph.py         # the eleventh, meaning inherited from a substring
    ROHONC_REF=data/ref/rohonc/ALL.txt python ktalign.py   # the wider corpus
    python ktname.py          # the twelfth, name-final compounds
    python ktsegment.py       # the thirteenth, cutting codes into codes
    python ktcoverage.py      # how much can be read, and how much is translated
    python ktsense.py         # can context choose a sense (fails by half a point)
    python ktgrammar.py       # are the senses separable at all (no)
    python ktvariant.py       # the fourteenth, variant spellings (fails; K&T's own go in)
    python ktanchor.py        # the fifteenth, substitution frames (gate untestable)
    python ktverse.py         # the sixteenth, anchors against the corpus (gate fails)
    python ktverse2.py        # the seventeenth, the refinement on a held-out half (fails)
    python kttranslate.py     # render the whole book, marked by how far each word reads
    python ktcontext.py       # every occurrence of an unread sign, for checking a guess
    python ktgap.py           # lines that are one word short, so the gap can be read
    python ktaffix.py         # the clause terminator, used by all three above
    # the translation itself is read by hand: work/rohonc/translation/rohonc_translation.md
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
