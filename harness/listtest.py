"""Is each line an entry, or just a chunk?

§4.2.2 established that the line is the unit of composition: word-level
dependence is strong inside a line and statistically zero across a line break.
That rules out flowing prose. It does not rule out meaning, because plenty of
meaningful writing is line-bounded -- a recipe book, an inventory, a table of
star positions, a list of plant names with their uses. All of those stop at the
end of a line because each line is a separate item.

So the question this asks is narrower than "does it mean anything". It is:

    given that the line is the unit, does a line behave like an ENTRY --
    a self-contained item with its own internal shape -- or like a CHUNK,
    an arbitrary run of text that happens to be one line long?

An entry has a distinct opening. A list of plants starts each line with a plant
name, drawn from a different vocabulary than the words in the middle of the
line. An entry also has internal template structure: position within the line
predicts what kind of word sits there, because entries repeat a shape.

A chunk has neither. In prose the first word of a line is simply whatever word
the previous line ran out of room for, so it is drawn from the same
distribution as every other word, and position within a line predicts nothing.

Two measurements, each against three controls:

  `prose`     a real language laid out on the manuscript's own line budgets.
              Its line breaks are arbitrary by construction, so it is what a
              chunk looks like.
  `register`  a synthetic list: each line is a headword drawn from a small
              inventory followed by body words. It is what an entry looks like.
  `fivecomp`  the best meaning-free generator, which composes by the line but
              has no notion of an entry.

Paragraph-opening lines are excluded throughout. They are already known to be
special -- they carry the gallows capital of §4.3 -- and including them would
answer a question nobody is asking.

Everything is surrogate-corrected. The control shuffles word order within the
paragraph while holding the line lengths fixed, which preserves the vocabulary
and the geometry exactly and destroys only the association between a word and
where in the line it sits.

    python listtest.py
"""
import math
import os
import random
import sys
from collections import Counter

import corpus

FP = os.path.join(corpus.ROOT, "refs", "voynich-fingerprint", "analysis")
if FP not in sys.path:
    sys.path.insert(0, FP)
from tier2_metrics import onset  # noqa: E402

SURROGATES = 12
SEED = 408
BUCKETS = 4


# --------------------------------------------------------------------------
# measurement A: is the first word of a line drawn from a different vocabulary?
# --------------------------------------------------------------------------
def _jsd(p, q):
    keys = set(p) | set(q)
    tp, tq = sum(p.values()), sum(q.values())
    if not tp or not tq:
        return 0.0
    out = 0.0
    for k in keys:
        a, b = p.get(k, 0) / tp, q.get(k, 0) / tq
        m = (a + b) / 2
        if a:
            out += 0.5 * a * math.log2(a / m)
        if b:
            out += 0.5 * b * math.log2(b / m)
    return out


def _split_words(doc, key=lambda w: w):
    """(first words of continuation lines, words elsewhere in those lines)."""
    first, rest = Counter(), Counter()
    for p in doc:
        for ln in p.lines[1:]:
            if len(ln) < 2:
                continue
            first[key(ln[0])] += 1
            for w in ln[1:]:
                rest[key(w)] += 1
    return first, rest


def opening_distinctness(doc, rng, key=lambda w: w, surrogates=SURROGATES):
    """How far the line-opening vocabulary sits from the rest of the line."""
    first, rest = _split_words(doc, key)
    raw = _jsd(first, rest)
    nulls = []
    for _ in range(surrogates):
        sh = shuffle_within_paragraph(doc, rng)
        f2, r2 = _split_words(sh, key)
        nulls.append(_jsd(f2, r2))
    m = sum(nulls) / len(nulls)
    sd = (sum((x - m) ** 2 for x in nulls) / max(1, len(nulls) - 1)) ** 0.5
    return raw - m, sd, sum(first.values())


# --------------------------------------------------------------------------
# measurement B: does position within the line predict the kind of word?
# --------------------------------------------------------------------------
def _mi(pairs):
    n = len(pairs)
    if not n:
        return 0.0
    jx, jy, j = Counter(), Counter(), Counter()
    for a, b in pairs:
        jx[a] += 1
        jy[b] += 1
        j[(a, b)] += 1
    out = 0.0
    for (a, b), c in j.items():
        p = c / n
        out += p * math.log2(p / ((jx[a] / n) * (jy[b] / n)))
    return out


def _position_pairs(doc, buckets=BUCKETS):
    out = []
    for p in doc:
        for ln in p.lines[1:]:
            if len(ln) < buckets:
                continue
            for i, w in enumerate(ln):
                out.append((min(buckets - 1, i * buckets // len(ln)), onset(w)))
    return out


def position_structure(doc, rng, surrogates=SURROGATES):
    """Mutual information between where a word sits in its line and its onset."""
    raw = _mi(_position_pairs(doc))
    nulls = []
    for _ in range(surrogates):
        nulls.append(_mi(_position_pairs(shuffle_within_paragraph(doc, rng))))
    m = sum(nulls) / len(nulls)
    sd = (sum((x - m) ** 2 for x in nulls) / max(1, len(nulls) - 1)) ** 0.5
    return raw - m, sd


def shuffle_within_paragraph(doc, rng):
    """Same words, same line lengths, word order scrambled inside the paragraph.

    This is the null: a document whose lines are demonstrably arbitrary chunks
    of their paragraph's own vocabulary.
    """
    out = []
    for p in doc:
        ws = p.words[:]
        rng.shuffle(ws)
        lines, i = [], 0
        for ln in p.lines:
            lines.append(ws[i:i + len(ln)])
            i += len(ln)
        out.append(corpus.Para(folio=p.folio, lines=lines, section=p.section,
                               lang=p.lang, hand=p.hand))
    return out


# --------------------------------------------------------------------------
# the synthetic register control: what an entry actually looks like
# --------------------------------------------------------------------------
def synthetic_register(spec, vocab, rng, n_heads=120):
    """One entry per line: a headword from a small inventory, then body words.

    Deliberately crude. It is not a model of anything; it is a positive control
    that shows what the two measurements read when a line really is an entry.
    """
    heads = [vocab[rng.randrange(len(vocab))] for _ in range(n_heads)]
    body = vocab
    out = []
    for ps in spec:
        lines = []
        for budget in ps.budgets:
            ln, used = [heads[rng.randrange(len(heads))]], 0
            used = len(ln[0])
            while True:
                w = body[rng.randrange(len(body))]
                if used + len(w) + 1 > budget:
                    break
                ln.append(w)
                used += len(w) + 1
            lines.append(ln)
        out.append(corpus.Para(folio=ps.folio, lines=lines, section=ps.section,
                               lang=ps.lang, hand=ps.hand))
    return out


# --------------------------------------------------------------------------
# the confound: the scribe chose shorter words as he approached the margin
# --------------------------------------------------------------------------
def _position_pairs_by_len(doc, buckets=BUCKETS):
    """Position/onset pairs, grouped by word length."""
    out = {}
    for p in doc:
        for ln in p.lines[1:]:
            if len(ln) < buckets:
                continue
            for i, w in enumerate(ln):
                out.setdefault(len(w), []).append(
                    (min(buckets - 1, i * buckets // len(ln)), onset(w)))
    return out


def _cond_mi(groups, minimum=200):
    """I(position ; onset | word length): the length-weighted mean of the
    within-length mutual informations.

    Word length falls as the right margin approaches -- the scribe fitted the
    word to the space left -- and onset class correlates with length, so the
    unconditional figure can be produced entirely by that physical habit.
    Holding length fixed removes it. What survives is template structure that
    is not about running out of room.
    """
    use = {k: v for k, v in groups.items() if len(v) >= minimum}
    n = sum(len(v) for v in use.values())
    if not n:
        return 0.0
    return sum(len(v) / n * _mi(v) for v in use.values())


def position_structure_by_length(doc, rng, surrogates=SURROGATES):
    raw = _cond_mi(_position_pairs_by_len(doc))
    nulls = [_cond_mi(_position_pairs_by_len(shuffle_within_paragraph(doc, rng)))
             for _ in range(surrogates)]
    m = sum(nulls) / len(nulls)
    sd = (sum((x - m) ** 2 for x in nulls) / max(1, len(nulls) - 1)) ** 0.5
    return raw - m, sd


def opening_by_length(doc, rng, surrogates=SURROGATES):
    """Opening distinctness with word length held fixed.

    Compares the onset distribution of line-opening words against mid-line
    words OF THE SAME LENGTH, so a first word that is merely longer cannot
    register as a different kind of word.
    """
    def split(d):
        f, r = {}, {}
        for p in d:
            for ln in p.lines[1:]:
                if len(ln) < 2:
                    continue
                f.setdefault(len(ln[0]), Counter())[onset(ln[0])] += 1
                for w in ln[1:]:
                    r.setdefault(len(w), Counter())[onset(w)] += 1
        return f, r

    def score(d):
        f, r = split(d)
        keys = [k for k in f if k in r and sum(f[k].values()) >= 100]
        n = sum(sum(f[k].values()) for k in keys)
        if not n:
            return 0.0
        return sum(sum(f[k].values()) / n * _jsd(f[k], r[k]) for k in keys)

    raw = score(doc)
    nulls = [score(shuffle_within_paragraph(doc, rng)) for _ in range(surrogates)]
    m = sum(nulls) / len(nulls)
    sd = (sum((x - m) ** 2 for x in nulls) / max(1, len(nulls) - 1)) ** 0.5
    return raw - m, sd


def _edge_pairs(doc, drop, buckets=3):
    out = {}
    for p in doc:
        for ln in p.lines[1:]:
            body = ln[drop:len(ln) - drop] if drop else ln
            if len(body) < buckets:
                continue
            for i, w in enumerate(body):
                out.setdefault(len(w), []).append(
                    (min(buckets - 1, i * buckets // len(body)), onset(w)))
    return out


def _edge_strip(doc, drop, rng, surrogates=SURROGATES):
    """Position structure with `drop` words removed from each end of the line.

    A real entry template has a shape across the whole entry, so stripping the
    edges should leave most of it standing. Decorated edges leave nothing.
    """
    raw = _cond_mi(_edge_pairs(doc, drop))
    nulls = [_cond_mi(_edge_pairs(shuffle_within_paragraph(doc, rng), drop))
             for _ in range(surrogates)]
    m = sum(nulls) / len(nulls)
    sd = (sum((x - m) ** 2 for x in nulls) / max(1, len(nulls) - 1)) ** 0.5
    return raw - m, sd, sum(len(v) for v in _edge_pairs(doc, drop).values())


def main():
    import generators
    import layout
    generators.load_all()

    doc = corpus.load()
    train, test = corpus.split(doc)
    spec = layout.build(train, len(corpus.words(test)))
    rng = random.Random(SEED)

    targets = [("the manuscript", doc)]
    for name, label in (("natlang_italian", "prose (Italian, same layout)"),
                        ("fivecomp", "five-component model"),
                        ("grille", "table-and-grille"),
                        ("naibbe_latin", "Naibbe cipher")):
        try:
            d, _ = generators.get(name)["fn"](spec, train, seed=7)
            targets.append((label, d))
        except Exception as e:
            print(f"  ({name} failed: {e})")

    vocab = sorted(set(corpus.words(train)))
    targets.append(("register (synthetic list)",
                    synthetic_register(spec, vocab, random.Random(5))))

    print("=" * 78)
    print("IS A LINE AN ENTRY, OR A CHUNK?")
    print("=" * 78)
    print("Both columns are surrogate-corrected: the control keeps the words and the")
    print("line lengths and scrambles only word order inside the paragraph.")
    print("Paragraph-opening lines are excluded throughout.\n")
    print(f"{'':30s} {'opening':>10s} {'sigma':>7s} {'position':>10s} {'sigma':>7s}")
    print(f"{'':30s} {'distinct':>10s} {'':>7s} {'structure':>10s} {'':>7s}")
    print("-" * 78)
    for label, d in targets:
        o, osd, n = opening_distinctness(d, random.Random(SEED))
        p, psd = position_structure(d, random.Random(SEED))
        print(f"{label:30s} {o:10.4f} {o/osd if osd else 0:7.1f} "
              f"{p:10.4f} {p/psd if psd else 0:7.1f}")

    print("\n  'opening distinct' -- how far the vocabulary that opens a line sits")
    print("  from the vocabulary in the rest of the line. A list has a headword;")
    print("  prose has whatever the previous line ran out of room for.")
    print("  'position structure' -- how much where a word sits in its line tells")
    print("  you about what kind of word it is. An entry repeats a shape.")

    print("\n" + "=" * 78)
    print("SAME TEST ON THE ONSET CLASS RATHER THAN THE WHOLE WORD")
    print("=" * 78)
    print("The whole-word version is sensitive to vocabulary size. The onset class")
    print("is a small alphabet, so this one is far less biased.\n")
    print(f"{'':30s} {'opening':>10s} {'sigma':>7s} {'n lines':>9s}")
    print("-" * 78)
    for label, d in targets:
        o, osd, n = opening_distinctness(d, random.Random(SEED), key=onset)
        print(f"{label:30s} {o:10.4f} {o/osd if osd else 0:7.1f} {n:9d}")

    print("\n" + "=" * 78)
    print("THE CONFOUND: WORD LENGTH FALLS TOWARD THE MARGIN")
    print("=" * 78)
    print("The scribe fitted the word to the space left, so words shorten as the")
    print("right margin approaches, and onset class correlates with length. Both")
    print("figures above could be produced by that habit alone. These hold word")
    print("length fixed and ask what survives.\n")
    print(f"{'':30s} {'opening':>10s} {'sigma':>7s} {'position':>10s} {'sigma':>7s}")
    print(f"{'':30s} {'| length':>10s} {'':>7s} {'| length':>10s} {'':>7s}")
    print("-" * 78)
    for label, d in targets:
        o, osd = opening_by_length(d, random.Random(SEED))
        p, psd = position_structure_by_length(d, random.Random(SEED))
        print(f"{label:30s} {o:10.4f} {o/osd if osd else 0:7.1f} "
              f"{p:10.4f} {p/psd if psd else 0:7.1f}")

    print("\n" + "=" * 78)
    print("IS IT A TEMPLATE, OR JUST THE TWO ENDS?")
    print("=" * 78)
    print("An entry has a shape across its whole length. Decorated edges do not.")
    print("Strip words off each end of every line and see what survives.\n")
    print(f"{'dropped per end':>16s}  {'EVA':>9s} {'sigma':>7s} {'pairs':>8s}"
          f"   {'v101':>9s} {'sigma':>7s}")
    v101 = corpus.load(os.path.join(corpus.DATA, "GC2a-n.txt"))
    for drop in (0, 1, 2, 3):
        a, asd, na = _edge_strip(doc, drop, random.Random(SEED))
        b, bsd, _ = _edge_strip(v101, drop, random.Random(SEED))
        print(f"{drop:>16d}  {a:9.4f} {a/asd if asd else 0:7.1f} {na:8d}"
              f"   {b:9.4f} {b/bsd if bsd else 0:7.1f}")
    print("\n  Two words off each end and there is nothing left. The structure sits")
    print("  at the edges of the line, not across it: this is not an entry template.")

    print("\n  mean word length by quarter of the line, for the manuscript:")
    import statistics
    b = {i: [] for i in range(BUCKETS)}
    for p in corpus.load():
        for ln in p.lines[1:]:
            if len(ln) < BUCKETS:
                continue
            for i, w in enumerate(ln):
                b[min(BUCKETS - 1, i * BUCKETS // len(ln))].append(len(w))
    print("    " + "  ".join(f"q{i+1} {statistics.mean(v):.2f}" for i, v in b.items()))


if __name__ == "__main__":
    main()
