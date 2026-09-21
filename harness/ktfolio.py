"""Restorations that differ from folio to folio, keyed (page, sign).

proposals.json holds ONE gloss per sign, which is right for a dictionary and
wrong for five signs in this book. The chapter-number sign written as four
strokes, a mark, four strokes stands on five folios and the passage that
follows it is Matthew 16 at 195v, Matthew 18 at 134r, Matthew 22 at 202v and
Luke 14 at 071r. One sign, four chapters. Recorded as a failure in
ktqueue.json and left dark for that reason.

This file does not solve that. It only lets the READER'S EDITION print, in
brackets, the chapter the folio's own following passage shows, folio by
folio, the same way ktsensefit prints the sense the passage uses. The deposit
is untouched: nothing here is a reading, nothing here is counted, and every
entry appears as [word] like any other guess.

    {"PAGE|HEX": ["gloss", "why"]}
"""
import json
import os

import corpus

TABLE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "folio_restorations.json")


def load():
    if not os.path.exists(TABLE):
        return {}
    raw = json.load(open(TABLE, encoding="utf-8"))
    return {k: v[0] for k, v in raw.items() if not k.startswith("_")}
