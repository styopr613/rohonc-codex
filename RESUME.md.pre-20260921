# Where this stopped — 2026-09-21, end of session

The manuscript is finished. What is unfinished is the **book**, and only one
part of it: Book One, the retelling.

## The shape that was agreed

Two books under one cover, and the split is the whole point.

**Book One — The Book as it Reads.** One continuous retelling per part, ten
parts, written as prose, labelled editorial on every part, citing the folios
each sentence draws on. Allowed to smooth. NOT allowed to know anything the
gloss does not contain.

**Book Two — The Manuscript, Folio by Folio.** All 441 folios, six to a
chapter, each with its gate-checked English paragraph and its marked
line-by-line text. This is the evidence. Where the two disagree, Book Two is
right, and every part of Book One says so in its own last paragraph.

`harness/ktbook.py` already builds both. It is wired and it runs.

## THE NEXT THING TO DO

Write the five missing parts of the retelling into
`work/rohonc/translation/retelling.md`, in the same voice as the five that are
there, then clear the gate, then rebuild.

    written:   I (004v-006v), II (008r-015v), III (016r-022r),
               IV (022v-028v), X (221r-224v)
    missing:   V   The Passion                 029r-052v   44 folios
               VI  Burial to Ascension         053r-009v   24 folios
               VII The Preaching               064r-182v  235 folios  <- needs
                                                          4-5 sub-sections
               VIII Finding of the Cross       183r-214v   64 folios
               IX  Acts of the Apostles        215r-220v   22 folios

Read a part's raw material like this:

    cd harness
    python3 -c "
    import json, ktbook
    d = json.load(open('../work/rohonc/translation/english.json'))
    fol = ktbook.folios(); order=[f[0] for f in fol]
    idx={p:i for i,p in enumerate(order)}
    b=sorted((idx[p],n) for p,n,_ in ktbook.PARTS)
    s=[x for x,n in b if n.startswith('V.')][0]
    e=[x for x,_ in b if x>s][0]
    for pg,t,pr,ln in fol[s:e]:
        print('---',pg,t); print(d.get(pg,{}).get('english','(refused)'))
    "

The set pieces that carry Book One, named by the outside reader and still to
be written: **Barlaam's man in the pit** with the two mice and the lance
(148v, 149r, 149v); **Augustine and the child on the seashore** (084r);
**the prodigal**, where the robe is love, mercy and righteousness (113r,
114v, 115r) — the allegorisation is the book's own voice and it is the best
writing in the codex; **Dives and Lazarus** (089v, 090r); **Chosroes on his
gold tower and barefoot Heraclius** (183r, 183v, 185r, 186r); **Stephen's
stoning with Saul holding the coats** (218r, 218v, 216v, 219r).

## THE GATE, and it currently FAILS

    cd harness && python3 ktretellcheck.py      # bar is 0, currently 28

Three checks, all declared in the file before they ran: every folio cited in a
part must lie in that part's span (write `cf. 159r` to reach elsewhere on
purpose); every phrase in «guillemets» must have all its content words in the
gloss of a cited folio; every digit-number must be in the gloss or declared in
ARITHMETIC with its working.

**The 28 failures are real and they are mine.** Writing Parts II-IV I quoted
the DeepSeek English instead of the gloss in about twenty places — «the
centurion», «Mount Tabor», «white», «barren», «kneel down». Each is a one-line
fix: either quote what the gloss actually says, or drop the guillemets and let
it be an editorial sentence. Do not widen the gate to make them pass.

Two of the 28 are not mine: Part I still uses `*italics*` for manuscript
quotations from before the convention changed, and needs its quotations
re-marked in guillemets; Part IV cites 159r for the second 666 and must write
it `cf. 159r`.

## What was finished this session

**The date, 223v — a confirmation, not a quarrel.** Line 1 says the count runs
«from the departure of the Lord Jesus Christ to the Father» — from the
Ascension, not the Nativity. Line 2 gives 1560. 33 + 1560 = **1593**, which is
Kiraly and Tokai's published date, reached by a different road. Recorded in
Part X of the retelling and in `ktretellcheck.ARITHMETIC`.

**Two manufactured anchors withdrawn.** 5199 and 1560 had each ALSO been
guessed as whole single signs from the folio note — the expectation dressed as
a finding. Both now gloss `a_numeral`, with the withdrawal written into the
entry. Backup `harness/proposals.json.pre-20260921-223v`. The anchors survive
without them: 5199 is spelled out in read signs at 223v:9-10 and matches the
Roman Martyrology; the numerals are confirmed independently by «six-six
apostle» (13 lines, 9 naming the apostles) and by 666 at 028v and 159r, both
times beside «evil» and «hell».

**Folio English for 433 of 441 folios**, written from the gloss ALONE — no
source passage, no chapter title, no page image — by DeepSeek V4-Pro on
DeepInfra, about $0.40 all in. `harness/ktenglish.py`.

**The leak gate and the triage.** 1,478 flags down to **17** in class 1
(content), none of them a name, a doctrine or an event — only numerals. Most
of the original count was the gate flagging its own text (the dictionary
spells the name *Jézus*, files words as *Jew(ish)*); the rest were three
declared allowances now listed in the file. `harness/ktleakaudit.py` sorts
every flag into content / connective / interpretive.

**The refusal bar caught two real source dumps.** Median folio flags 1.9% of
its words. 199v flagged 18.9% and was Matthew 21:31-32 verbatim — tax
collectors, prostitutes, John in the way of righteousness, none of it in the
gloss. 168v was Luke 16:5-7 verbatim. A declared bar at 3x median (5.7%) and a
retry that quotes the folio's own leaked words back at the model took 199v to
**zero** leaks. Eight folios failed twice and lost their English entirely;
they print their marked lines alone, which is the honest outcome.

**Apparatus fixes the outside reader asked for**, all in `ktbook.py`: the
marks table is no longer a markdown table (it rendered as broken pipes in the
EPUB); "What a bracket is worth" now gives each of its four numbers its own
connecting sentence; the 0.0% held-out figure now says what was masked and why
it is the hardest population; the front matter claims only "the whole of it,
end to end, in a modern language", not a first reading; the salvation-formula
polarity scramble is named as a known crux rather than tidied away; and a new
back-matter section says plainly that the siege cannibalism at 111v-112r is
scripture (2 Kings 6:28-29, Lamentations 4:10, Deuteronomy 28:53-57) while the
thirty-Jews-for-a-penny arithmetic on the same leaves is not — it is medieval
polemic out of the Vindicta Salvatoris tradition.

## The book on the shelf is STALE

    /opt/publish-app/data/u1/books/20260921-052535-r0hc/book.json

It is the one-book version from 05:25 with the old crib paragraphs. It does
NOT have Book One, the new folio English, or any of the apparatus fixes.
Rebuild it only after the gate passes:

    cd harness
    python3 ktreader.py
    python3 ktretellcheck.py                 # must print PASS
    python3 ktbook.py --shelf /opt/publish-app/data/u1/books/20260921-052535-r0hc

Backups already beside it: `book.json.pre-prose2-20260921`.

Still undesigned, unbuilt, no cover. **Built. Not read. Do not publish.**

## Files this session created or changed

    harness/ktenglish.py        NEW  folio English + the leak gate
    harness/ktleakaudit.py      NEW  the three-class triage
    harness/ktretellcheck.py    NEW  the retelling gate (currently FAILS, 28)
    harness/ktbook.py           two books, new front and back matter
                                backup ktbook.py.pre-twobooks-20260921
    harness/proposals.json      two numerals withdrawn on 223v
                                backup proposals.json.pre-20260921-223v
    work/rohonc/translation/english.json    NEW  433 folios
    work/rohonc/translation/retelling.md    NEW  5 of 10 parts

Nothing is committed yet.
