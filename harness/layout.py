"""The layout spec every generator is handed, built from TRAIN only.

The fingerprint repo generates `n_paragraphs = <test paragraph count>` and takes
its line budgets from the held-out document. Its own LIMITATIONS.md records that
an earlier revision leaked layout constants that way and that the leak inflated
the result. So this harness is stricter: paragraph shapes and line budgets are
*sampled* from the TRAIN half with a seeded RNG, and the only number taken from
the TEST half is a single scalar, its token count, which is just "how much text
to make".

Consequence to state in the write-up: the layout-given metrics (line geometry,
paragraph shape, and the section / Currier labels the metadata carries) are
handed to every process identically. They are not evidence about any process.
What the layout does is put every generator under the same physical constraints
as the scribe, so the metrics that *are* earned -- entropy, vocabulary, onsets,
repetition, section-specificity -- are measured under matched conditions.
"""
import random
from dataclasses import dataclass, field

import corpus


@dataclass
class ParaSpec:
    folio: str
    section: str
    lang: str
    hand: str
    budgets: list = field(default_factory=list)   # characters per line

    @property
    def n_lines(self):
        return len(self.budgets)


def build(train, token_budget, seed=408):
    """Sample paragraph shapes from TRAIN until the token budget is reached.

    Each sampled paragraph carries the metadata of the TRAIN paragraph it was
    drawn from, so section / Currier / hand labels stay coherent with the shape.
    """
    rng = random.Random(seed)
    pool = [p for p in train if p.lines]
    spec, tokens = [], 0
    while tokens < token_budget:
        p = pool[rng.randrange(len(pool))]
        budgets = [sum(len(w) for w in ln) for ln in p.lines if ln]
        if not budgets:
            continue
        spec.append(ParaSpec(folio=p.folio, section=p.section, lang=p.lang,
                             hand=p.hand, budgets=budgets))
        tokens += sum(len(ln) for ln in p.lines if ln)
    return spec


def total_tokens(train, spec):
    """Rough token count the spec implies, using TRAIN's mean word length."""
    ws = corpus.words(train)
    mean_len = sum(len(w) for w in ws) / len(ws)
    chars = sum(sum(p.budgets) for p in spec)
    return int(round(chars / (mean_len + 1)))


def lay_out(stream, spec, cycle=True):
    """Chop a flat word stream into the spec's paragraphs and lines.

    For generators that produce a stream rather than fitting lines themselves
    (the ciphers, the natural-language controls). A line takes words until
    adding the next one would overshoot its character budget; a line always
    takes at least one word.

    cycle=True restarts a stream that runs short and records it as a shortfall.
    cycle=False stops instead, producing a shorter document: right for a source
    that simply does not have more text, where cycling would invent repetition
    the source does not contain.
    """
    it = iter(stream)
    exhausted = False

    class Done(Exception):
        pass

    def nxt():
        nonlocal it, exhausted
        try:
            return next(it)
        except StopIteration:
            exhausted = True
            if not cycle:
                raise Done
            it = iter(stream)
            return next(it)

    doc, pending = [], None
    for ps in spec:
        lines = []
        try:
            for budget in ps.budgets:
                ln, used = [], 0
                while True:
                    w = pending if pending is not None else nxt()
                    pending = None
                    cost = len(w) + (1 if ln else 0)
                    if ln and used + cost > budget:
                        pending = w
                        break
                    ln.append(w)
                    used += cost
                lines.append(ln)
        except Done:
            if lines:
                doc.append(corpus.Para(folio=ps.folio, lines=lines, section=ps.section,
                                       lang=ps.lang, hand=ps.hand))
            break
        doc.append(corpus.Para(folio=ps.folio, lines=lines, section=ps.section,
                               lang=ps.lang, hand=ps.hand))
    return doc, exhausted


def from_paras(spec, paras_of_lines):
    """Attach spec metadata to a document a generator produced itself.

    `paras_of_lines` is a list of paragraphs, each a list of lines of words, as
    the fingerprint's ArtGenerator emits. Metadata comes from the spec entry of
    the same index so the section-level metrics are defined.
    """
    out = []
    for ps, lines in zip(spec, paras_of_lines):
        out.append(corpus.Para(folio=ps.folio, lines=[ln for ln in lines if ln],
                               section=ps.section, lang=ps.lang, hand=ps.hand))
    return [p for p in out if p.lines]


def group_lines(lines, spec):
    """Group a generator's own lines into the spec's paragraphs.

    For processes that model the line but not the paragraph (the self-citation
    jar, the grille, the Llull machine). Their line structure is preserved
    exactly; only the paragraph breaks and the metadata come from the spec.
    """
    out, i = [], 0
    for ps in spec:
        take = lines[i:i + ps.n_lines]
        i += ps.n_lines
        take = [ln for ln in take if ln]
        if not take:
            break
        out.append(corpus.Para(folio=ps.folio, lines=take, section=ps.section,
                               lang=ps.lang, hand=ps.hand))
        if i >= len(lines):
            break
    return out


if __name__ == "__main__":
    d = corpus.load()
    tr, te = corpus.split(d)
    spec = build(tr, len(corpus.words(te)))
    print(f"test tokens {len(corpus.words(te))}")
    print(f"spec: {len(spec)} paragraphs, {sum(p.n_lines for p in spec)} lines, "
          f"{sum(sum(p.budgets) for p in spec)} chars")
    from collections import Counter
    print("spec sections:", dict(Counter(p.section for p in spec)))
