"""Document loader for the hypothesis-ranking harness.

Produces the same paragraph/line/word structure as voynich-fingerprint's
`tune_artgen.split_by_folio()` -- verified byte-for-byte by `gate.py` -- but keeps
the folio metadata (section, Currier language, scribal hand, quire) that the
line-level metric block needs and that the fingerprint repo discards.

A Document is a list of Para objects. `plain(doc)` returns the nested
list-of-lines-of-words shape the fingerprint's own functions expect.
"""
import os
import re
import sys
from dataclasses import dataclass, field

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FP = os.path.join(ROOT, "refs", "voynich-fingerprint", "analysis")


def version():
    """(number, date) of the edition, from VERSION at the repository root.

    One file, bumped by /release before the tag, read by the book's copyright
    page and the site's front page, so the printed version is the tagged one."""
    num, date = open(os.path.join(ROOT, "VERSION"), encoding="utf-8").read().split()[:2]
    return num, date


if FP not in sys.path:
    sys.path.insert(0, FP)

import voynich_lib as V  # noqa: E402

DATA = os.path.join(ROOT, "data")
PRIMARY = os.path.join(DATA, "IT2a-n.txt")


@dataclass
class Para:
    folio: str
    lines: list = field(default_factory=list)   # list[list[str]]
    section: str = "?"                          # $I illustration type
    lang: str = "?"                             # $L Currier language A/B
    hand: str = "?"                             # $H Davis scribal hand
    quire: str = "?"                            # $Q

    @property
    def words(self):
        return [w for ln in self.lines for w in ln]


def folio_num(f):
    """Leaf number, or None for a folio whose name carries no number.

    The v101 transliteration includes the Rosettes foldout as `fRos`, which has
    no leaf number and therefore no parity. It is excluded from both halves of
    the split rather than being forced into one; `split()` reports how many
    paragraphs that costs. The EVA file used for the main results has no such
    folio, so the main split is unaffected.
    """
    m = re.match(r"f?(\d+)", f or "")
    return int(m.group(1)) if m else None


def load(path=PRIMARY):
    """Parse the transcription into paragraphs of lines of words.

    Paragraph boundaries come from the manuscript's own <%> / <$> marks, exactly
    as tune_artgen.split_by_folio does. Only body-text loci (type P) are kept;
    labels (L*) and circular/radial text (R*) are excluded.
    """
    paras, cur, curf, curm = [], [], [], None
    open_para = False

    def close():
        nonlocal cur, curf, curm
        if cur:
            m = curm or {}
            paras.append(Para(folio=curf[0], lines=cur,
                              section=m.get("I", "?"), lang=m.get("L", "?"),
                              hand=m.get("H", "?"), quire=m.get("Q", "?")))
        cur, curf, curm = [], [], None

    for folio, locus, ltype, raw, meta in V.parse_ivtff(path):
        code = re.sub(r"\d+$", "", ltype)
        if code.lstrip("@+*&=")[:1] != "P":
            continue
        starts = raw.lstrip().startswith("<%>")
        ends = raw.rstrip().endswith("<$>")
        t = V.strip_markup(raw).replace("<%>", "").replace("<$>", "")
        ws = []
        for tok in re.split(r"[.,\s]+", t):
            tok = tok.strip("-")
            if not tok or re.search(r"[?!]", tok) or any(c in tok for c in "[]{}()"):
                continue
            ws.append(tok)
        if starts and open_para and cur:
            close()
        if not ws:
            continue
        open_para = True
        cur.append(ws)
        curf.append(folio)
        if curm is None:
            curm = meta
        if ends:
            close()
            open_para = False
    close()
    return paras


def split(doc, reverse=False):
    """Train/test split by leaf parity.

    Default (reverse=False): train = even-numbered leaves, test = odd, matching
    the fingerprint repo. reverse=True swaps them; both are always reported, so
    that a configuration chosen on one split is arbitrated by the other.
    """
    numbered = [(p, folio_num(p.folio)) for p in doc]
    even = [p for p, n in numbered if n is not None and n % 2 == 0]
    odd = [p for p, n in numbered if n is not None and n % 2 == 1]
    return (odd, even) if reverse else (even, odd)


def unnumbered(doc):
    """Paragraphs excluded from the split for having no leaf number."""
    return [p for p in doc if folio_num(p.folio) is None]


def plain(doc):
    """Document -> the nested list shape the fingerprint's functions consume."""
    return [p.lines for p in doc]


def words(doc):
    return [w for p in doc for ln in p.lines for w in ln]


if __name__ == "__main__":
    d = load()
    tr, te = split(d)
    print(f"{len(d)} paragraphs, {len(words(d))} words")
    print(f"train {len(tr)} paras / {len(words(tr))} words | "
          f"test {len(te)} paras / {len(words(te))} words")
    from collections import Counter
    print("sections:", dict(Counter(p.section for p in d)))
    print("langs:   ", dict(Counter(p.lang for p in d)))
    print("hands:   ", dict(Counter(p.hand for p in d)))
