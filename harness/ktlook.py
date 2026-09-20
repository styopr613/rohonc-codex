"""Kiraly & Tokai's own entry for a code, by hex, and for each of its glyphs.

    python3 ktlook.py 0600601a6 4a04a04acae0
    python3 ktlook.py --cite 100r10 099v06     # entries that cite those lines

Kiraly & Tokai cite folio:line in their entries, so a gap on a line they
cite is often already read by them under another code or as an expression.
"father son" was their word for brother at 099r04 and it was missed here
because only the headwords had been read. Check --cite before guessing.

Prints the raw entry text for the code if they define it, then the entry for
every glyph and every defined prefix inside it, so a compound can be read
from its parts without opening the dictionary by hand.
"""
import json
import sys

import ktdict


def hx(s):
    return "".join(f"{ord(c) - 0xE000:03x}" for c in s)


def unhx(h):
    return "".join(chr(0xE000 + int(h[i:i + 3], 16)) for i in range(0, len(h), 3))


def entries():
    raw = json.load(open(ktdict.DICT, encoding="utf-8"))
    out = {}
    for e in raw:
        txt = " ".join(" ".join(f.get("text", "") for f in e["entry"]).split())
        out.setdefault(e["code"], []).append(txt)
    return out


def cite(E, refs):
    for r in refs:
        print(f"=== lines cited: {r}")
        for code, txts in E.items():
            for t in txts:
                if r in t:
                    print(f"  {hx(code):>14s}: {t[:240]}")


def main(argv):
    E = entries()
    if argv and argv[0] == "--cite":
        cite(E, argv[1:])
        return 0
    for h in argv:
        code = unhx(h)
        print(f"=== {h}")
        for t in E.get(code, []):
            print(f"  WHOLE: {t[:220]}")
        n = len(code)
        seen = set()
        for i in range(n):
            for j in range(i + 1, n + 1):
                part = code[i:j]
                if part == code or part in seen or part not in E:
                    continue
                seen.add(part)
                for t in E[part]:
                    print(f"  {hx(part):>14s} [{i}:{j}]: {t[:160]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
