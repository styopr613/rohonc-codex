"""Shared pieces for the outside-review tests (Tests 10-13).

Nothing here decides a result. It builds the objects every test needs the
same way, so that two tests cannot disagree about what a folio cites or
what a passage contains.

  cited(doc)             {folio: [(book, ch, v_from, v_to)]} from the
                         translation notes, biblical citations only
  kt_taken(gl)           the content stems K&T's 841 glosses carry
  free_pools(...)        {folio: set of content stems of its cited passage,
                         Douay and King James, minus the stems K&T carry}
  corpus_freq(vv, vd)    Counter of stems over every verse of both Bibles
  folio_signs(doc)       {folio: [base sign, ...]} in reading order
"""
import re
from collections import Counter, defaultdict

import ktaffix as A
import ktcross as K
import ktleft as L
import ktrederive as R

# The stop list is checked on the surface form, so "hath", "goeth", "wilt"
# and "therefore" reach the stem stage and come out as hav, go, wilt,
# therefor -- and then survive every chapter of every book, real or null.
# The first run of Tests 10, 10b and 13 (saved as *_v1_stopleak.txt) had
# those in every pool. A content stem is one whose STEM is not the stem of
# a stop word or of one of these auxiliary and adverb forms, declared here
# before the rerun and not tuned to any result.
AUX = set("""hath hast doth dost art wilt shalt wast wert therefore wherefore
yet cannot neither nothing also even ever never let ought ye yea nay lest
whether either thereof therein thereby whereof wherein whereby hereby thus
whence thence hence whither thither hither""".split())
STOPSTEM = {K.stem(w) for w in K.STOP | AUX}


def content(text):
    """R.stems minus anything whose stem is a stop or auxiliary stem."""
    return {s for s in R.stems(text) if s not in STOPSTEM and len(s) >= 3}


def cited(doc):
    out = {}
    for pg in sorted({x.page for x in doc}):
        r = L.refs_in(K.note_for(pg))
        if r:
            out[pg] = r
    return out


def kt_taken(gl):
    st = set()
    for s, g in gl.items():
        for x in g:
            st |= content(x)
    return st


def passage_stems(vv, vd, refs):
    s = set()
    for k, txt in L.passage(vv, refs) + L.passage(vd, refs):
        s |= content(txt)
    return s


def free_pools(doc, gl, vv, vd, refs=None):
    refs = refs if refs is not None else cited(doc)
    taken = kt_taken(gl)
    return {pg: passage_stems(vv, vd, r) - taken for pg, r in refs.items()}


def corpus_freq(vv, vd):
    freq = Counter()
    for t in (vv, vd):
        for txt in t.values():
            freq.update(content(txt))
    return freq


def folio_signs(doc):
    out = defaultdict(list)
    for pg in doc:
        for ln in pg.lines:
            for run in ln:
                for t in run:
                    out[pg.page].append(A.strip(t)[0])
    return out


def sigma(obs, nulls):
    m = sum(nulls) / len(nulls)
    sd = (sum((x - m) ** 2 for x in nulls) / max(1, len(nulls) - 1)) ** .5
    return m, sd, ((obs - m) / sd if sd else 0.0)
