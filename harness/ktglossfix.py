"""THE GLOSS, CORRECTED BY HAND WHERE KIRÁLY AND TOKAI NAME THE WORD.

Their entries cite folio and line for their examples. Where an entry cites a
line and our gloss printed something else there, the line was read by hand
against the entry and the word decided one at a time. glossfix.json holds the
decisions: "FOLIO+LINE HEX" -> the English printed for that sign on that line,
in this edition's own wording. Nothing else is in it; the reasons, which quote
their entries, stay out of the repository.

ktlinecite.py finds the candidates. It no longer decides them: run as a rule
it kept picking the wrong sense (2026-09-28) and was replaced by this table.

The rules the decisions follow:
  1. Their word for a line beats our own reading, our cut of the sign, a
     variant mapping, or the sense-fit pick.
  2. Where their entry names the sense for that line, that sense prints, not
     the entry's first sense.
  3. A citation they mark "?" beats our readings and any sense of theirs that
     cites no line of this sign; it does not replace a sense they cite for
     that line. A citation marked "??" replaces only our readings.
  4. Where they list the whole sign as a spelling of one word, that word
     prints alone (then, not then-exist). Where their own analysis splits it
     (to-go, their example of the prefix "to"), the split stays.
  5. A sign inside one of their set phrases (ktexpr.json) is left to the
     phrase.
"""
import json
import os

FIX = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                  "glossfix.json"), encoding="utf-8"))


def word(page, line, raw_hex, base_hex):
    """The hand-decided English for this sign on this line, or None."""
    for h in (raw_hex, base_hex):
        w = FIX.get(f"{page}{line:02d} {h}")
        if w is not None:
            return w.replace(" ", "_")
    return None
