"""Kiraly and Tokai's entry for a code, with every rohonc run shown as hex.

The flattened text drops which code goes with which gloss, and that is
exactly what has to be read to tell a variant from a cross-reference.

    python3 ktraw.py 5200607a2        entries whose headword is this
    python3 ktraw.py --prints 520b42  entries that print this code anywhere
"""
import json
import re
import sys

import ktdict


def hx(s):
    return "".join(f"{ord(c) - 0xE000:03x}" for c in s)


def show(e):
    out = []
    for f in e["entry"]:
        t = f.get("text", "")
        st = f.get("style", "")
        if st == "rohonc":
            out.append(" ".join("{" + hx(r) + "}"
                                for r in re.findall(r"[-]+", t)))
        elif st in ("meta", "section"):
            out.append(" " + t.strip() + " ")
        else:
            out.append(t)
    print("".join(out).replace("  ", " "))


def main(argv):
    raw = json.load(open(ktdict.DICT, encoding="utf-8"))
    pr = '--prints' in argv
    want = [a for a in argv if not a.startswith('--')]
    for e in raw:
        h = hx(e["code"])
        blob = "".join(f.get("text", "") for f in e["entry"])
        codes = {hx(r) for r in re.findall(r"[-]+", blob)}
        if pr:
            ok = any(w in codes or any(
                c.find(w) % 3 == 0 and c.find(w) != -1 and
                (c.find(w) + len(w)) % 3 == 0 for c in codes) for w in want)
        else:
            ok = h in want
        if ok:
            print(f"--- headword {h}")
            show(e)
            print()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
