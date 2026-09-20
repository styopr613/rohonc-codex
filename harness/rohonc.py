"""The Rohonc Codex as a token stream, for the line-break test.

Source: the open transcription formerly at quint.us/Roho/latest.txt, revision
2.5 (2014-09-18), recovered from the Internet Archive. It is an incomplete,
partly machine-generated transcription of a 448-page codex; 6.5% of its tokens
are marked unreadable. Treat every figure from it as provisional.

The Rohonc script has no word separators, and Kiraly & Tokai (Cryptologia 42:4,
2018) argue each symbol codes a whole WORD rather than a letter. So one glyph
id here plays the role one space-delimited word plays in the Voynich, and the
character-level metrics of the main harness do not apply at all. What does
apply is the test that decided the Voynich question, because it needs only a
token stream and the line breaks: does the dependence between one token and the
next survive the right margin?

Two cautions specific to this script.

The codex is written right to left. Whether this file stores each line in
reading order or in visual order is not documented, so `load()` takes a
`reverse` flag and callers should report both. Mutual information is symmetric,
so the within-line figure is unaffected either way; only the across-break pair
changes, and there it matters, so both are reported.

Unreadable tokens are dropped rather than bridged. Dropping a token would
otherwise manufacture an adjacency between two symbols that were never
neighbours, which is exactly the kind of artefact this measurement is
sensitive to. `load()` therefore splits a line into runs of consecutive
readable tokens and the pair functions never step across a gap.
"""
import os
import re
from dataclasses import dataclass, field

import corpus

PATH = os.path.join(corpus.DATA, "rohonc", "latest.txt")


@dataclass
class Page:
    page: str
    lines: list = field(default_factory=list)   # list[list[run]], run = list[str]

    @property
    def tokens(self):
        return [t for ln in self.lines for run in ln for t in run]


def _clean(tok):
    """Glyph id, or None if it carries no identified symbol.

    `?` alone is an unclear glyph, `#` an unidentified one, `=` a scribal mark
    rather than a symbol. A trailing `?` means the transcriber identified the
    glyph but was not certain; those are kept under their base id.
    """
    if not tok or tok in ("=", "?", "#"):
        return None
    if tok.startswith("?") or tok.startswith("#"):
        return None
    t = tok.rstrip("?")
    return t or None


def load(path=PATH, reverse=False):
    pages, cur, curp = [], [], None
    for raw in open(path, encoding="utf-8", errors="replace"):
        raw = raw.rstrip("\r\n")
        if not raw.strip() or raw.lstrip().startswith(";"):
            continue
        m = re.match(r"\s*(\S+)\s*:\s*(\S+)\s*:\s*(.*)$", raw)
        if not m:
            continue
        page, _, body = m.group(1), m.group(2), m.group(3)
        if page != curp:
            if cur:
                pages.append(Page(page=curp, lines=cur))
            cur, curp = [], page
        toks = body.replace("[?]", " ? ").split()
        if reverse:
            toks = toks[::-1]
        runs, run = [], []
        for t in toks:
            c = _clean(t)
            if c is None:
                if run:
                    runs.append(run)
                run = []
            else:
                run.append(c)
        if run:
            runs.append(run)
        if runs:
            cur.append(runs)
    if cur:
        pages.append(Page(page=curp, lines=cur))
    return pages


def pairs_by_position(doc):
    """Adjacent token pairs, split by whether a line break falls between them.

    A pair is only formed between two tokens that were actually adjacent in the
    transcription, so a run interrupted by an unreadable glyph contributes no
    pair across the gap. The across-break pair is formed only when the last
    token of one line and the first token of the next are both readable.
    """
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
    toks = [t for p in d for t in p.tokens]
    w, a = pairs_by_position(d)
    print(f"{len(d)} pages, {sum(len(p.lines) for p in d)} lines, "
          f"{len(toks)} readable tokens, {len(set(toks))} types")
    print(f"within-line pairs {len(w)}, across-break pairs {len(a)}")
