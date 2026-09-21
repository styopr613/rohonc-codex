"""Guesses whose code Kiraly and Tokai print somewhere in their dictionary.

ktcited.py asked a narrow question: does their entry cite the very line the
guess sits on? That found 26. This asks the wider one: do they print this
exact code ANYWHERE -- as a headword's variant, inside an expression, as an
example -- even citing a different folio. If they do, they have read the
word, and the guess is either wrong or is a guess at something already known.

Exact codes only. Matching constituents would return almost everything,
because a code like 520 opens a third of the book.

    python3 ktprinted.py             [--summary] [--hex HEX] [--tier G]
"""
import json
import re
import sys
from collections import defaultdict

import ktcross as K
import ktdict


def hx(s):
    return "".join(f"{ord(c) - 0xE000:03x}" for c in s)


def main(argv):
    raw = json.load(open(ktdict.DICT, encoding="utf-8"))
    p = json.load(open('proposals.json', encoding='utf-8'))
    tier = argv[argv.index('--tier') + 1] if '--tier' in argv else 'G'
    one = argv[argv.index('--hex') + 1] if '--hex' in argv else None
    gl, doc, seg, var, prop, inv = K.build()
    head = {hx(e["code"]) for e in raw}

    want = {k for k, v in p.items() if not k.startswith('_')
            and isinstance(v, dict) and v.get('tier') == tier}
    if one:
        want = {one}
    # a code they already gloss as a headword is not news; the renderer has it
    want -= head

    printed = defaultdict(list)
    for e in raw:
        h = hx(e["code"])
        txt = " ".join(" ".join(f.get("text", "") for f in e["entry"]).split())
        blob = "".join(f.get("text", "") for f in e["entry"])
        for code in {hx(r) for r in re.findall(r"[-]+", blob)}:
            if code in want and code != h:
                printed[code].append((h, txt))

    for h in sorted(printed):
        if '--summary' in argv:
            continue
        v = p[h]
        print(f"=== {h}  \"{v.get('gloss','')}\"  n={v.get('n')}")
        for head_h, txt in printed[h][:3]:
            print(f"    under {head_h}: {txt[:600]}")
        print()
    print(f"-- {len(printed)} of {len(want)} tier {tier} codes are printed "
          f"somewhere in K&T's dictionary")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
