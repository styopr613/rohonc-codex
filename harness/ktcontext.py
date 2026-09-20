"""Every occurrence of an unread sign, rendered, so a guess can be checked.

This is Kiraly & Tokai's own method made into a tool: guess a sign from one
passage where the story is known, then look at every other place it occurs
and keep the guess only if it survives all of them. A sign that occurs once
gets a guess and no check; a sign that occurs several times gets a guess and
a test. Nothing here decides anything. It prints the evidence.

    python ktcontext.py            # the unread signs worth attacking, ranked
    python ktcontext.py 574570670ae0 4a24a04a4   # every context of those signs
"""
import sys
from collections import Counter

import ktcoverage as C
import ktsegment as S
import ktaffix as A
import ktvariant as V

DONE = set("""004v 004r 002r 002v 003r 003v 001r 001v 007r 007v 006r 006v 008r 008v
005r 005v 015r 015v 016r 016v 017r 017v 018r 018v 019r 019v 020r 020v 021r 021v
022r 022v 023r 023v 024r 024v 025r 025v 026r 026v 027r 027v 028r 028v 029r 029v
030r 030v 031r 031v 032r 032v 033r 033v 034r 034v 035r 035v 137v 135r 119r
060r 060v 061r 061v 062r 062v 063r 063v 009r 009v 064r 064v 065r 065v 066r 066v 067r 067v 068r 068v 069r 069v 070r 070v 071r 071v 072r 072v 073r 073v 074r 074v 075r 075v 076r 076v 077r 077v 078r 079r 080v 081r 081v 082r 082v 083v 084r""".split())


def hx(t):
    return "".join(f"{ord(c)-0xE000:03x}" for c in t)


def unhx(h):
    return "".join(chr(0xE000 + int(h[i:i + 3], 16)) for i in range(0, len(h), 3))


PROP = {}


def load():
    """The full readable inventory, exactly as kttranslate.py renders it.

    Contexts used to be printed with Kiraly & Tokai's dictionary alone, so
    this project's own 110 readings showed as [?] in the very tool used to
    make the next reading. Reading a context was therefore harder than
    reading the rendered page. Everything readable is shown here now, with
    the same marks the page uses, so a guess is made against the best
    reading available rather than a worse one.
    """
    import kttranslate as T
    gl, doc, seg = C.build()
    var = {v: h for v, (h, _) in V.readings()[6].items()}
    prop = T.load_proposals()
    PROP.clear()
    PROP.update(prop)
    inv = set(gl) | set(seg) | set(var) | set(prop)
    types = {t for p in doc for t in p.tokens}
    while True:
        added = 0
        for t in sorted(types):
            b = A.strip(t)[0]
            if b in inv:
                continue
            cut = S.segment(b, inv)
            if cut and len(cut) >= 2:
                seg[b] = cut
                inv.add(b)
                added += 1
        if not added:
            break
    return gl, doc, seg, var


def piece(c, gl, var):
    if c in gl:
        return S.best_sense(gl[c]).replace(" ", "_")
    if c in var:
        return "~" + S.best_sense(gl[var[c]]).replace(" ", "_")
    if c in PROP:
        g, tier = PROP[c]
        return ("+" if tier in ("A", "B") else "?") + g.replace(" ", "_")
    return "[?" + hx(c) + "]"


def word(t, gl, seg, var):
    t, mark = A.strip(t)
    if t in gl:
        return S.best_sense(gl[t]).replace(" ", "_") + mark
    if t in seg:
        return "-".join(piece(p, gl, var) for p in seg[t]) + mark
    if t in var:
        return "~" + S.best_sense(gl[var[t]]).replace(" ", "_") + mark
    if t in PROP:
        g, tier = PROP[t]
        return ("+" if tier in ("A", "B") else "?") + g.replace(" ", "_") + mark
    return "[?" + hx(t) + "]" + mark


def contexts(code, doc, gl, seg, var):
    out = []
    for p in doc:
        for i, ln in enumerate(p.lines, 1):
            toks = [t for run in ln for t in run]
            if code in toks:
                s = " ".join("<<" + word(t, gl, seg, var) + ">>" if t == code
                             else word(t, gl, seg, var) for t in toks)
                out.append((p.page, i, s, p.page in DONE))
    return out


def main(argv):
    gl, doc, seg, var = load()
    types = Counter(t for p in doc for t in p.tokens)
    if argv:
        for h in argv:
            c = unhx(h)
            cs = contexts(c, doc, gl, seg, var)
            print(f"\n=== {h}   {len(cs)} occurrences ===")
            for page, i, s, done in cs:
                print(f"  {'*' if done else ' '} {page}:{i:<3d} {s[:170]}")
        return
    onpage = {t for p in doc if p.page in DONE for t in p.tokens}
    cand = [(t, k) for t, k in types.items()
            if t not in gl and t not in seg and t not in var and t not in PROP
            and k >= 3 and t in onpage]
    cand.sort(key=lambda x: -x[1])
    print(f"{len(cand)} unread signs with 3+ occurrences that sit in a translated passage")
    print(f"{'n':>5s}  {'sign':22s}  {'on translated pages':>19s}")
    for t, k in cand:
        seen = sum(1 for p in doc if p.page in DONE for x in p.tokens if x == t)
        print(f"{k:5d}  {hx(t):22s}  {seen:19d}")


if __name__ == "__main__":
    main(sys.argv[1:])
