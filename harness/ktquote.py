"""Quotation clerk for Book One. Ask the gloss what it actually says.

This was the other half of the retelling gate's quotation check: that gate
refused a «quotation» whose content words were not in the gloss of a cited
folio, and this said what to write instead. The check was removed on
2026-09-22 -- the printed Book One carries no guillemets, so it weighed
nothing -- and this stayed, because asking the gloss what it actually says is
the job whether or not the answer ends up in quotation marks. It uses
ktenglish.stems, the same instrument the rest of the edition is checked with.

    python3 ktquote.py show 029r 029v ...        gloss lines + English
    python3 ktquote.py part V                    every folio of a part
    python3 ktquote.py check 029r 029v -- phrase  which stems are missing
    python3 ktquote.py find word 029r-052v       lines carrying that stem
"""
import re
import sys

import ktbook
import ktenglish as E


def _fol():
    return {pg: (pg, t, pr, ln) for pg, t, pr, ln in ktbook.folios()}


def _order():
    return [f[0] for f in ktbook.folios()]


def _span(lo, hi):
    o = _order()
    return o[o.index(lo):o.index(hi) + 1]


def _expand(args):
    """004v 029r-052v V  ->  a flat list of folio ids."""
    out = []
    for a in args:
        if re.fullmatch(r"\d{3}[rv]-\d{3}[rv]", a):
            lo, hi = a.split("-")
            out += _span(lo, hi)
        elif re.fullmatch(r"\d{3}[rv]", a):
            out.append(a)
        else:
            out += part_span(a)
    return out


def part_span(name):
    """The folio ids of a part, named by its roman numeral or its title."""
    o = _order()
    idx = {p: i for i, p in enumerate(o)}
    b = sorted((idx[p], n) for p, n, _ in ktbook.PARTS)
    for k, (i, n) in enumerate(b):
        if n.split(".")[0].strip().lower() == name.strip().lower() \
           or n.lower().startswith(name.lower()):
            end = b[k + 1][0] if k + 1 < len(b) else len(o)
            return o[i:end]
    raise SystemExit(f"no part {name!r}; have "
                     + ", ".join(n.split('.')[0] for _, n in b))


def show(pages):
    fol, en = _fol(), ktbook.english()
    for pg in pages:
        if pg not in fol:
            print(f"--- {pg}  (no such folio)")
            continue
        _, title, _, lines = fol[pg]
        print(f"\n--- {pg} {'— ' + title if title else ''}")
        if pg in en:
            print(f"    EN: {en[pg]}")
        for l in lines:
            print(l)


def check(pages, phrase):
    have = set()
    fol = _fol()
    for pg in pages:
        if pg in fol:
            have |= E.stems(" ".join(fol[pg][3]))
    miss = [w for w in sorted(E.stems(phrase)) if w not in have]
    print(f"«{phrase}»")
    print("  OK" if not miss else "  MISSING: " + " ".join(miss))
    return 1 if miss else 0


def find(word, pages):
    fol = _fol()
    want = E.stems(word)
    for pg in pages:
        if pg not in fol:
            continue
        for l in fol[pg][3]:
            if want & E.stems(l):
                print(f"{pg}  {l.strip()}")


def main(argv):
    if not argv:
        print(__doc__)
        return 0
    cmd, rest = argv[0], argv[1:]
    if cmd == "show":
        show(_expand(rest))
    elif cmd == "part":
        show(part_span(rest[0]))
    elif cmd == "check":
        i = rest.index("--")
        return check(_expand(rest[:i]), " ".join(rest[i + 1:]))
    elif cmd == "find":
        find(rest[0], _expand(rest[1:]))
    else:
        print(__doc__)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
