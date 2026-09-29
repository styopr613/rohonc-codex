"""Parse manuscript references embedded in free-form evidence notes.

Evidence uses a three-digit folio plus ``r`` or ``v``, followed variously by
``:line``, a two-digit line number, or a column/part marker such as
``013vc1:03``.  A word boundary after the side letter is therefore wrong:
both the side letter and a following digit are word characters.
"""
import re


FOLIO_REF = re.compile(r"(?<![0-9A-Za-z])(\d{3}[rv])")


def evidence_folios(text, valid=None):
    """Return folios cited in an evidence note.

    If *valid* is supplied, discard candidates that are not folios in the
    caller's manuscript.  That validation is preferable whenever the caller
    already has the document loaded.
    """
    found = set(FOLIO_REF.findall(text or ""))
    return found if valid is None else found & set(valid)
