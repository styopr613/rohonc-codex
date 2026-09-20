"""Self-citation with a hard reset at every line break.

Timm & Schinner (2019) proposed that the scribe wrote each word by copying one
he had recently written and changing it slightly, and built a generator for it.
Their version draws from a buffer of everything recently written, which spreads
the dependence across the whole page. It reaches about a tenth of the
within-line word dependence the manuscript has.

§4.2.2 and similarity.py together suggest what is missing. The manuscript's
dependence is strong inside a line and exactly zero across a line break, and
the same split shows in the spelling: a word is a smaller edit of its
line-neighbour than chance (+7.9 sigma), while the word ending a line and the
word starting the next are *further apart* than chance (-19.1 sigma).

So the loop modelled here is:

  1. start a line from a small stock of opener words, used by habit
  2. write each next word by copying the previous one and mutating it
  3. fit the last word to the space left and finish it with a flourish
  4. go back to the left margin and start again WITHOUT looking at how the
     previous line ended

Everything is learned from the training half. The mutation operations are
Timm's: substitute, insert, delete, and swap the ending. What is new here is
only step 4, and the two pools that step 1 and step 3 draw on.

This is a model of a process, not a claim that this is what happened. It exists
to answer one question: can a copying process with a line reset produce the
within-line / across-line signature that no other meaning-free process does?
"""
import random
from collections import Counter, defaultdict

import corpus
from . import register

DEFAULTS = {
    "p_copy": 0.0,         # copy-and-mutate. ZERO after the ablation in
                           # RESULTS.md 4.2.4: copying makes every measure
                           # worse, including the spelling similarity it was
                           # introduced to explain.
    "n_mut": 1.35,         # mean number of edits applied to a copy
    "opener_frac": 0.30,   # share of the line-opening vocabulary kept as a stock
    "p_flourish": 0.68,    # line-final r written as m
    "p_fresh_decay": 0.0,  # extra chance of a fresh word later in the line
}

SUFFIXES = ("aiin", "iin", "ain", "edy", "eey", "dy", "ey", "ol", "or",
            "ar", "al", "y", "n", "r", "l", "s", "m")


class Scribe:
    """Everything the process knows, learned from TRAIN."""

    def __init__(self, train):
        ws = corpus.words(train)
        self.freq = Counter(ws)
        self.words = list(self.freq)
        self.wts = [self.freq[w] for w in self.words]
        self.chars = Counter(c for w in ws for c in w)
        self.charset = list(self.chars)
        self.charwts = [self.chars[c] for c in self.charset]
        # what starts a continuation line
        op = Counter()
        for p in train:
            for ln in p.lines[1:]:
                if ln:
                    op[ln[0]] += 1
        keep = max(1, int(len(op) * DEFAULTS["opener_frac"]))
        self.openers = [w for w, _ in op.most_common(keep)]
        self.opener_wts = [op[w] for w in self.openers]
        # endings available for a suffix swap
        self.suffixes = [s for s in SUFFIXES
                         if sum(1 for w in ws if w.endswith(s)) > 20]
        # P(next word | last character of the previous word). Currier's
        # observation that words ending in `y` precede words beginning `qo-`.
        # Added after the first version of this generator failed: copy-and-
        # mutate preserves the START of a word, so it cannot produce a
        # dependence between one word's END and the next word's START. Those
        # are two different phenomena and the first version conflated them.
        self.byprev = defaultdict(Counter)
        for p_ in train:
            for ln in p_.lines:
                for a, b in zip(ln, ln[1:]):
                    self.byprev[a[-1]][b] += 1
        self.byprev_lists = {k: (list(c), [c[w] for w in c])
                             for k, c in self.byprev.items()}

    def fresh(self, rng, prev=None):
        if prev:
            t = self.byprev_lists.get(prev[-1])
            if t and len(t[0]) > 30:
                return rng.choices(t[0], weights=t[1])[0]
        return rng.choices(self.words, weights=self.wts)[0]

    def opener(self, rng):
        return rng.choices(self.openers, weights=self.opener_wts)[0]

    def mutate(self, w, rng, n):
        for _ in range(n):
            if not w:
                return self.fresh(rng)
            op = rng.random()
            if op < 0.34:                                   # substitute
                i = rng.randrange(len(w))
                w = w[:i] + rng.choices(self.charset, weights=self.charwts)[0] + w[i + 1:]
            elif op < 0.58:                                 # insert
                i = rng.randrange(len(w) + 1)
                w = w[:i] + rng.choices(self.charset, weights=self.charwts)[0] + w[i:]
            elif op < 0.78:                                 # delete
                if len(w) > 1:
                    i = rng.randrange(len(w))
                    w = w[:i] + w[i + 1:]
            else:                                           # swap the ending
                for s in self.suffixes:
                    if w.endswith(s) and len(w) > len(s):
                        w = w[:-len(s)] + rng.choice(self.suffixes)
                        break
                else:
                    w = w + rng.choice(self.suffixes)
        return w or self.fresh(rng)


def write_line(sc, budget, rng, cfg):
    """One line: an opener, then copy-and-mutate, then a fitted flourished end."""
    w = sc.opener(rng)
    line, used = [w], len(w)
    while True:
        p_copy = max(0.0, cfg["p_copy"] - cfg["p_fresh_decay"] * len(line))
        if rng.random() < p_copy:
            nxt = sc.mutate(line[-1], rng, 1 + (rng.random() < cfg["n_mut"] - 1))
        else:
            nxt = sc.fresh(rng, prev=line[-1])
        if used + len(nxt) + 1 > budget:
            break
        line.append(nxt)
        used += len(nxt) + 1
    if line and line[-1].endswith("r") and rng.random() < cfg["p_flourish"]:
        line[-1] = line[-1][:-1] + "m"
    return line


@register("linereset", kind="self",
          label="self-citation with a line reset",
          note="NEW: Timm's copy-and-mutate, restarted at every line break")
def generate(spec, train, seed=0, cfg=None):
    cfg = {**DEFAULTS, **(cfg or {})}
    rng = random.Random(seed + 23)
    sc = Scribe(train)
    doc = []
    for ps in spec:
        lines = [write_line(sc, b, rng, cfg) for b in ps.budgets]
        doc.append(corpus.Para(folio=ps.folio, lines=[l for l in lines if l],
                               section=ps.section, lang=ps.lang, hand=ps.hand))
    return [p for p in doc if p.lines], {"cfg": cfg,
                                         "cite": "after Timm & Schinner (2019); line reset new"}
