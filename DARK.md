# THE DARK WORDS — done, and what was learned

**Status: complete.** There are no dark words left. This file was the handoff
for the last 3.6% of the Rohonc Codex; that work is finished and what follows
is the record of how, kept because the method transferred better than the
result did.

    at the start          1,087 words with no reading   3.6%
    at the end                0                          0.0%

    of the 1,087:
      read properly, tiers A to D       ~110
      restored as bracketed guesses      975
      still with no reading at all         5  (one sign, five folios,
                                               four different chapters)

The five are the chapter-number sign. It stands in the citation slot on five
folios and the passage that follows it is Matthew 16, Matthew 18, Matthew 22
and Luke 14. One sign cannot be four chapters, so it is not read. `ktfolio.py`
prints the chapter each folio's own following text shows, in brackets, without
claiming the sign is read.

## The three things that actually worked

**1. Follow K&T's own citations back into the manuscript.** Their entries cite
folio and line, including for variant spellings. 398 dark lines are cited
somewhere in their dictionary. Where a line has ONE hole and the word their
entry names is not already rendered elsewhere in that line, their entry names
the hole, and the reading is tier A. 44 readings, eleven at tier A. This is
the single best instrument found in the whole project and it had been sitting
unused for six years, because the variant reader keyed on headwords and never
matched a form carrying a prefix.

**2. Read the folio, not the sign.** Attacking one sign at a time yielded
about eight readings per seventy signs. Reading a whole folio against its
cited passage, with all its holes visible at once, was better: the passage
constrains several slots together and the words that are already placed rule
out the ones that are left.

**3. Look at the page.** The scans are in `data/rohonc/scan/`. `ktfill.py page
FOLIO` crops the right half-spread. Note the mapping: the leaf number is
written on the LEFT page, which is the recto, because the book reads right to
left. The first version of that tool had it backwards and served the wrong
folio for an hour.

## The three things that did not work, with their numbers

Measured, declared in advance, failed:

    neighbours + the whole 1.7M-word corpus     top-1  0.5%
    the cited passage, positionally             top-1  1.0%
    a fusion of both                            top-1  1.8%
    bar declared before the run                        6.0%

All three lost to simply reading the line. The passage pool contains the true
word only 7.8% of the time for a word this rare. There is no ranker here; the
reader is the ranker.

## What a bracket is worth

Three quarters of the content guesses land on a word that actually stands in
the verse the folio cites -- the only part that can be checked from inside the
book. Against K&T's hidden entries the top candidate scored 0.0%. Read a
bracket as a suggestion from an editor who knows the source and does not know
the word.

Two of the guesses were caught and corrected by reading the finished pages:
one folio said "blessed" twice and one said "table" twice. Both are fixed in
place with the mistake named in the entry. That is the loop that matters -- if
a page does not read, the guess is wrong, so go back to the verse.

## The tools, if any of this is ever rerun

    python3 ktdark.py dossier          every unread sign, ranked, with its
                                       lines, its passage and its structure
    python3 ktdark.py apply FILE.json  write decisions in, dated backup
    python3 ktqueue.py pass HEX why    park one, with the reason written down
    python3 ktlook.py --cite 100r10    K&T's entries that cite a line
    python3 ktsensefit.py              the sense the passage uses
    python3 ktfill.py page 052r        the page image
    python3 ktreader.py                rebuild the reader's edition
    ./ktcommit.sh "message"            the only way to commit

419 signs carry a written reason for having been left dark at the point the
strict pass stopped; those reasons are in `work/rohonc/queue.json` and they
are the honest record of where reading ran out and guessing began.
