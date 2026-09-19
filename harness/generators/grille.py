"""Rugg's table-and-grille (2004), at corpus scale.

A table of word fragments in prefix / core / suffix columns; a card with holes
laid over it; the words that show through the holes are written down; the card
is slid along and the next words are read. Rugg's point in 2004 was that this
device, available in the fifteenth century, produces Voynich-like gibberish by
hand, which removed "too complex to be a hoax" from the argument.

Two departures from voynich-toolkit's implementation, both to give the method
its best shot rather than its weakest:

  * the table is not fixed at 40 rows. A 40-row table can only ever produce a
    few hundred distinct words, so the vocabulary-size failure the toolkit
    reports is a property of that choice, not of the method. Table height is a
    tuned parameter here, on the same budget every other process gets.
  * the grille slides. Successive words come from consecutive rows of the
    table, as a physical card moving over a page would give, rather than from
    independent random rows. That is both more faithful to the device and the
    only way it can produce local repetition.

One table per Currier language, which is how the hoax hypothesis accounts for
the A/B split.
"""
import random
from collections import Counter

import corpus
import layout
from . import register

SUFFIXES = ("aiin", "iin", "ain", "dy", "in", "y", "m", "n", "s", "g")
GRILLES = (("prefix", "core", "suffix"), ("core", "suffix"), ("prefix", "core"))

DEFAULTS = {"rows": 400, "tables": 3, "stride": 1, "p_jump": 0.35}


def decompose(words):
    """Stolfi-style prefix / core / suffix split of the training vocabulary."""
    pfx, core, sfx = Counter(), Counter(), Counter()
    for w in words:
        if w.startswith("qo"):
            pfx["qo"] += 1
            w = w[2:]
        elif w.startswith("q") and len(w) > 1:
            pfx["q"] += 1
            w = w[1:]
        else:
            pfx[""] += 1
        if not w:
            core[""] += 1
            sfx[""] += 1
            continue
        found = ""
        for s in SUFFIXES:
            if w.endswith(s) and len(w) > len(s):
                found = s
                break
        if found:
            sfx[found] += 1
            w = w[:-len(found)]
        else:
            sfx[""] += 1
        core[w if w else ""] += 1
    return pfx, core, sfx


def _column(counts, n, rng):
    vals = list(counts)
    wts = [counts[v] for v in vals]
    return rng.choices(vals, weights=wts, k=n)


def build_tables(train_words, cfg, rng):
    pfx, core, sfx = decompose(train_words)
    tables = []
    for _ in range(cfg["tables"]):
        p = _column(pfx, cfg["rows"], rng)
        c = _column(core, cfg["rows"], rng)
        s = _column(sfx, cfg["rows"], rng)
        tables.append([{"prefix": p[i], "core": c[i], "suffix": s[i]}
                       for i in range(cfg["rows"])])
    return tables


def make_writer(tables, cfg, rng):
    """A sliding grille over one of the tables, chosen by Currier language."""
    state = {"row": 0, "grille": 0}

    def write(lang):
        t = tables[0 if lang == "A" else 1 if lang == "B" else 2 % len(tables)]
        if rng.random() < cfg["p_jump"]:
            state["row"] = rng.randrange(len(t))
            state["grille"] = rng.randrange(len(GRILLES))
        row = t[state["row"] % len(t)]
        w = "".join(row[col] for col in GRILLES[state["grille"]])
        state["row"] += cfg["stride"]
        return w or "o"
    return write


def _run(spec, train, seed, cfg):
    rng = random.Random(seed + 5)
    tables = build_tables(corpus.words(train), cfg, rng)
    write = make_writer(tables, cfg, rng)
    doc = []
    for ps in spec:
        lines = []
        for budget in ps.budgets:
            ln, used = [], 0
            while True:
                w = write(ps.lang)
                cost = len(w) + (1 if ln else 0)
                if ln and used + cost > budget:
                    break
                ln.append(w)
                used += cost
            lines.append(ln)
        doc.append(corpus.Para(folio=ps.folio, lines=lines, section=ps.section,
                               lang=ps.lang, hand=ps.hand))
    return doc, {"cfg": cfg, "cite": "Rugg (2004); Rugg & Taylor (2017); Zandbergen (2021)"}


@register("grille", kind="stream", label="table-and-grille (Rugg)",
          note="sliding grille, table height tuned on TRAIN")
def generate(spec, train, seed=0, cfg=None):
    return _run(spec, train, seed, {**DEFAULTS, **(cfg or {})})


@register("grille_bigtable", kind="stream",
          label="table-and-grille, large table",
          note="table pinned at 8000 rows to show the vocabulary/dependence trade-off")
def generate_big(spec, train, seed=0, cfg=None):
    fixed = {**DEFAULTS, **(cfg or {}), "rows": 8000, "tables": 4}
    return _run(spec, train, seed, fixed)
