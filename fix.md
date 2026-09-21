# fix.md — what to do when the readings have been hardened

One command. Run it in `harness/`:

    python3 whatbroke.py

It answers four questions in one pass: what broke, what is exposed, what is
load-bearing, and what is left. The rest of this file is what those mean and
what to do about each.

---

## The short answer: patch it, do not scrap it

Book One quotes the gloss, so changing the readings changes some of what it
quotes. The question was whether that means rewriting the retelling. It does
not, and the reason is a count rather than an opinion:

    content words quoted inside guillemets, by where the gloss supplies them

        KT        1622   87.8%   Kiraly & Tokai's own dictionary entries
        VAR          7    0.4%   ~word, a variant their own apparatus files
        CUT        104    5.6%   word-word, our ktname/ktsegment cuts
        BRACKET    115    6.2%   [word], our restorations
        MISSING      0    0.0%

**Seven eighths of the words Book One quotes are Kiraly and Tokai's, and
hardening our readings cannot move them.** Only the 6.2% in brackets is really
at risk. Counted per quotation rather than per word, 103 of 786 quotations —
**13.1%** — rest on at least one word that nothing but a bracket supplies.

The bar was declared in `whatbroke.py`'s docstring before the count was run:
under a fifth exposed and patching wins, because the gate names every break
and each is a one-line fix; over half and the prose is resting on the guesses
and should be rewritten against the hardened gloss. It came out at 13.1%.

Part X is the outlier at 35%. That is not a defect. 221r–224v are the two
worst-preserved leaves in the manuscript and almost everything on them is a
restoration; Part X says so itself, in its own text.

---

## 1. What broke

`whatbroke.py` runs `ktretellcheck.py` on its real exit status and prints
every failure. Three kinds:

    QUOTE FAIL   a word inside guillemets is no longer anywhere in the gloss
                 of the folios that part cites
    NEAR FAIL    the word is still somewhere in the part, but not on the
                 folios named in that quotation's own paragraph
    RANGE FAIL   a folio cited outside its part's span without `cf.`
    NUMBER FAIL  a digit that is neither in the gloss nor declared in
                 ktretellcheck.ARITHMETIC

Each names itself with its own text and the missing word. Each is a one-line
fix, and there are exactly two legitimate fixes:

- **requote** what the gloss now says, or
- **drop the guillemets** and let the sentence be editorial.

There is no third option. Do not widen the gate to make prose pass.

---

## 2. What is exposed

`python3 whatbroke.py --list` prints every exposed quotation with the words
that only a bracket supplies. These are the ones a change to the restorations
can break. Everything else survives untouched.

Use it the other way round too: if you are about to withdraw a bracketed
reading, this tells you in advance which sentences of Book One will need
rewording.

---

## 3. What is load-bearing — the gate's blind spot

**This is the part that matters and the part no checker can do for you.**

A quotation is checked. The editorial sentence around it is not. So if a NAME
or a NUMBER moves, the paragraph's whole argument dies and nothing flags it.
If Longinus stops being Longinus, the sentence "Longinus blind and then
seeing is the *Golden Legend*, not the gospels" is simply false, and every
gate in this repository will still be green.

Section 3 lists every proper name the prose leans on that reaches it **only
through a bracket**. As of this writing that is five:

    Abraham    107r
    Adam       057v
    Christ     067v
    Enoch      101r
    Herod      021v

Five paragraphs for a person to read again. Every other name the prose leans
on — Longinus, Cleopas, Vespasian, Titus, Malchus, Nicodemus, Caiaphas,
Barabbas, Simeon, Hezekiah, Horeb, Emmaus, Carmel, Jericho — is a plain
dictionary entry of Kiraly and Tokai's and is safe.

**The first version of this check said seventeen and was wrong.** It counted
CUT as fragile alongside BRACKET, and a hyphen in the rendering marks two
different things: a ktname/ktsegment cut, which is ours, and an ordinary affix
like the *holy* prefix, which is theirs. They are not distinguishable from the
hyphen alone. So it flagged Adam, John, Luke, Mary and Matthew as fragile when
every one is a plain dictionary name carrying a prefix. A check that cries
wolf on twelve safe names costs a person more time than it saves them, and it
was narrowed to brackets only.

---

## 4. What is left

Book One draws on **183 of 441 folios**. 258 are not yet in the front of the
book.

    I     written              004v–006v    12 folios,   0 not drawn on
    II    written              008r–015v     6 folios,   0 not drawn on
    III   written              016r–022r    13 folios,   1 not drawn on
    IV    written              022v–028v    13 folios,   0 not drawn on
    V     written, with gaps   029r–052v    44 folios,  12 not drawn on
          gap 039r–042r   7 folios   (Pilate and Herod)
    VI    written              053r–009v    24 folios,   1 not drawn on
    VII   written, with gaps   064r–182v   235 folios, 157 not drawn on
          gap 076r–080r   7 folios
          gap 121v–182v 123 folios  (two of five stretches unwritten)
    VIII  NOT WRITTEN          183r–214v    64 folios
    IX    NOT WRITTEN          215r–220v    22 folios
    X     written              221r–224v     8 folios,   1 not drawn on

`python3 whatbroke.py --left` prints just this.

The two unwritten stretches of Part VII are **Genesis retold, Hezekiah, the
Unmerciful Servant and the Virgin cycle** (121v–147v) and **Barlaam, the
healings, the stewards and the lepers** (148r–182v). Part VII is one `##`
block with `####` sub-headings inside it, because `ktbook.retelling()` looks
each part up by its exact name in `ktbook.PARTS`.

Set pieces still to write: **Barlaam's man in the pit** with the two mice and
the lance (148v, 149r, 149v); **the prodigal told a second time** (150r,
150v); **the captive and the king** (154v–158v); **Chosroes on his gold tower
and barefoot Heraclius** (183r, 183v, 185r, 186r); **Stephen's stoning with
Saul holding the coats** (218r, 218v, 216v, 219r).

---

## How to write a part, if you are writing one

    cd harness
    python3 ktquote.py part VIII              # English + gloss, whole part
    python3 ktquote.py show 148v 149r 149v    # the folios you mean to quote
    python3 ktquote.py find shepherd 148r-182v
    ...write the prose, quoting the GLOSS, in «guillemets»...
    python3 ktretellcheck.py                  # bar is 0

**Quote the gloss, never the DeepSeek English.** The English is allowed a leak
budget and the gloss is not, which is exactly why the gate reads the gloss.
Roughly twenty quotations in Parts II–IV had been lifted from the English and
had to be rewritten: «grabbed every creature» became «grab each, every
create», «from dying» became «from die», «the beginning of the suffering»
became «this is begin suffering».

Six rules that each cost something:

- **The stemmer will not unify a doubled consonant.** grab/grabbed,
  sin/sinned, begin/beginning read as different words. That is the safe
  direction to fail in and it was NOT widened. Write the gloss's own form.
- **A digit anywhere in the prose must be declared** in
  `ktretellcheck.ARITHMETIC` or written as chapter-and-verse, which the gate
  strips. "Genesis 9" failed; "Genesis 9:21" passes and is truer.
- **Do not number sub-headings.** `#### 1. The last discourse` is a NUMBER
  FAIL.
- **A folio outside the part's span needs `cf.`**, written that way in the
  sentence.
- **Never write the word "guillemets" in guillemets.** The gate cannot tell an
  editorial mention from a claim, and it is right not to try.
- **Mark a bracket as a bracket when you quote one.** «[refused] to go» keeps
  the reader's knowledge that the word is a restoration. Silently dropping the
  brackets would make a guess look like a reading.

---

## Two defects this work found, recorded so they are not reintroduced

**The parser that dropped an eighth of the manuscript.** `ktbook.folios()`
matched `^\s{2,}\d+\s` for a numbered gloss line. The reader's edition
right-aligns its line numbers in a width-3 field, so line 9 is `  9  word` and
line 10 is ` 10  word` with ONE space. Every line numbered ten or higher fell
out of Book Two and out of the retelling gate that reads it — **527 lines,
12.1% of the manuscript**. `ktenglish` had the right pattern all along, which
is why its English paragraphs quote words the line-by-line text did not show.
Same fault as the folio count that stopped at 200r: correct for one-digit
numbers, wrong from ten on, agreeing with itself for months. One parser now,
and the two agree on all 441 folios. Fifteen of the retelling's 28 standing
failures were caused by this and not by bad prose.

**The gate that measured a 79-folio haystack.** Check 2 built its word list
from EVERY folio a part cites and then asked whether a quotation's words
appeared anywhere in it. For Part VII that is 79 folios, so a quotation could
name one leaf while borrowing a word from another eighty away. Check 2b scopes
the same test to the folios named in the quotation's own paragraph. It found
four, all real, all corrected: «a bright light from heaven» at 023v, where the
gloss has *bright* and *[from_heaven]* and no *light* at all; «end this holy
gospel» at 057r and again at 059v, neither of which carries *end*; and
«peace» at 057r, which stands on 009r.

Check 2b is declared in `ktretellcheck.py` as what it is: **a check written
after the prose, not before it.** That is weaker evidence than a pre-registered
gate, and the only honest thing to do is write down which kind it is. Its bar
is zero from now on.

---

## A claim that was wrong and is corrected in place

Part X said 222v is the only leaf in four hundred and forty-one carrying the
sign Kiraly and Tokai gloss as *the name of the author*. It stands on three:
137v, 138r and 222v. On the first two he writes himself into a prayer to the
Virgin, asking her to pray for his own sins. 222v is the only page where he
records what he **did** rather than what he asks for, and the text now says
that instead — and says it was wrong, rather than quietly amending it.
