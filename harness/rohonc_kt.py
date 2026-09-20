"""The Rohonc Codex as Kiraly & Tokai transcribe it.

A second, independent transcription of the same codex, at a different
granularity from the anonymous 2014 one in `rohonc.py`. Kiraly & Tokai made it
for their decipherment (Cryptologia 42:4, 2018) and serve it publicly at
rechnitzer-kodex.hu, which Kiraly's 2022 paper cites as the stopgap for a
dictionary too typographically awkward to print, put there expressly so that
"our claims about the text are verifiable this way". Verifying a claim about
the text is exactly what it is used for here.

**It corrects a mistake in ROHONC.md.** That document treated one glyph as one
token, on the reading that a Rohonc symbol codes a whole word. Kiraly & Tokai's
own transcription is space-separated and its words average 2.3 glyphs, with
only a third of them a single glyph. So a Rohonc code is usually two or three
glyphs, and the glyph stream is a finer unit than the word -- roughly as
letters are to words. Every figure in ROHONC.md is a glyph-level figure and
must not be compared with a word-level figure from any other manuscript.

Encoding: glyphs sit in the private-use range E000-EFFF, spaces separate words,
and F000-F0FF plus ASCII brackets carry editorial markup. The paired markup
codes are stripped. F01B appears unpaired 217 times and is treated as an
unreadable glyph, which breaks the sequence rather than being bridged, on the
same reasoning as the gaps in `rohonc.py`.

Only `main` blocks are kept. Headers, picture captions and the one multicolumn
block are excluded, matching the Voynich work's exclusion of labels and
circular text.

Page order is Kiraly & Tokai's reading order as their page list gives it, which
is not the binding order; they established the order from the readable text.
"""
import json
import os
from dataclasses import dataclass, field

import corpus

KT = os.path.join(corpus.DATA, "rohonc", "kt")
PAGES = os.path.join(KT, "pages")
GAP = ""


@dataclass
class Page:
    page: str
    lines: list = field(default_factory=list)   # list[list[run]], run = list[str]

    @property
    def tokens(self):
        return [t for ln in self.lines for run in ln for t in run]


def _clean(word):
    """Drop editorial markup; None if nothing readable is left."""
    out = [c for c in word if 0xE000 <= ord(c) <= 0xEFFF]
    return "".join(out) or None


def load(blocktypes=("main",)):
    order = json.load(open(os.path.join(KT, "pagelist.json"), encoding="utf-8"))
    pages = []
    for name in order:
        p = os.path.join(PAGES, f"{name}.json")
        if not os.path.exists(p):
            continue
        try:
            blocks = json.load(open(p, encoding="utf-8"))
        except Exception:
            continue
        lines = []
        for b in blocks:
            if b.get("blocktype") not in blocktypes:
                continue
            for r in b.get("rows", []):
                runs, run = [], []
                for w in r["text"].split():
                    if GAP in w:
                        if run:
                            runs.append(run)
                        run = []
                        w = w.replace(GAP, "")
                    c = _clean(w)
                    if c:
                        run.append(c)
                    elif run:
                        runs.append(run)
                        run = []
                if run:
                    runs.append(run)
                if runs:
                    lines.append(runs)
        if lines:
            pages.append(Page(page=name, lines=lines))
    return pages


def pairs_by_position(doc):
    """Adjacent word pairs, split by whether a line break falls between them."""
    within, across = [], []
    for p in doc:
        for i, runs in enumerate(p.lines):
            for run in runs:
                for a, b in zip(run, run[1:]):
                    within.append((a, b))
            if i + 1 < len(p.lines):
                last = runs[-1][-1] if runs and runs[-1] else None
                nxt = p.lines[i + 1]
                first = nxt[0][0] if nxt and nxt[0] else None
                if last and first:
                    across.append((last, first))
    return within, across


if __name__ == "__main__":
    d = load()
    t = [x for p in d for x in p.tokens]
    g = sum(len(x) for x in t)
    print(f"{len(d)} pages, {sum(len(p.lines) for p in d)} lines, "
          f"{len(t)} words, {len(set(t))} types, {g} glyphs")
    print(f"  TTR {len(set(t))/len(t):.4f}, {g/len(t):.2f} glyphs per word")
    w, a = pairs_by_position(d)
    print(f"  within-line pairs {len(w)}, across-break pairs {len(a)}")
