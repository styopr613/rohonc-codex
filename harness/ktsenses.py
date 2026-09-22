"""Every word of a folio with Kiraly and Tokai's WHOLE entry under it.

    python3 ktsenses.py 004v            one folio, for reading
    python3 ktsenses.py --json 004v     the same, as data for a prompt
    python3 ktsenses.py --all           every folio to work/rohonc/senses.json

WHY THIS FILE EXISTS. The reading edition was written from a gloss that carried
only the FIRST sense of every sign. K&T's entries carry several senses, in
their order, with their own worked examples and folio citations, and the sense
that makes a sentence is very often not the first one. Two examples, both of
which reached the printed book as nonsense:

  the numeral sign  "I. numeral a) one b) first c) (some)one; NOT ONE e.g.
                    094r05; 'he did not make one single wonder' 043r04"
  the somebody sign "c) expressions ... 019r03 every(body); (with negation)
                    019r03, 04 NOBODY"

Read with sense (a) every time, the codex's commonest sentence came out as
"every man is saved, and one man is damned", which is gibberish and is also
the opposite of what K&T's own example says it means. The entries were in the
repo the whole time; nothing joined them to a folio. This joins them.

A LOOKUP TRAP, worth stating because it cost an hour. Do NOT search the
dictionary for an English word. K&T's entries quote their own translations, so
the entry for "kneel down" contains the word "before" inside its example, and
the entry for "speak" contains "angel". Searching for "before" returns the
kneeling sign. Look up by CODE, always, which is what this file does.

Codes not in the dictionary are broken into their defined parts, longest
first, the same way ktlook.py does it; about a third of this manuscript's
signs are phrases written without a space.
"""
import argparse
import json
import os
import sys

import corpus
import ktdict
import ktlook

PAGES = os.path.join(corpus.ROOT, "data", "rohonc", "kt", "pages")
OUT = os.path.join(corpus.ROOT, "work", "rohonc", "senses.json")


def rows(pg):
    """The folio's lines, each a list of codes, in the manuscript's order."""
    p = os.path.join(PAGES, pg + ".json")
    if not os.path.isfile(p):
        return []
    out = []
    for block in json.load(open(p, encoding="utf-8")):
        for r in block.get("rows", []):
            codes = [c for c in r.get("text", "").split(" ") if c]
            if codes:
                out.append((r.get("rownumber") or "", codes))
    return out


def parts_of(code, E):
    """Defined pieces inside an undefined code, longest first, left to right."""
    out, i, n = [], 0, len(code)
    while i < n:
        for j in range(n, i, -1):
            seg = code[i:j]
            if seg in E:
                out.append((ktlook.hx(seg), E[seg]))
                i = j
                break
        else:
            i += 1
    return out


def folio(pg, E, cap=340):
    """One folio: every line, every code, with the entries that define it."""
    out = []
    for num, codes in rows(pg):
        line = []
        for c in codes:
            item = {"hex": ktlook.hx(c)}
            if c in E:
                item["entry"] = [t[:cap] for t in E[c]]
            else:
                pieces = parts_of(c, E)
                if pieces:
                    item["parts"] = [{"hex": h, "entry": [t[:cap] for t in ts]}
                                     for h, ts in pieces]
            line.append(item)
        out.append({"line": num, "words": line})
    return out


def show(pg, E):
    data = folio(pg, E)
    if not data:
        print(f"{pg}: no transcription", file=sys.stderr)
        return
    print(f"=== {pg}")
    for ln in data:
        print(f"\n{ln['line']:>3}")
        for w in ln["words"]:
            if w.get("entry"):
                for t in w["entry"]:
                    print(f"     {t}")
            elif w.get("parts"):
                for p in w["parts"]:
                    for t in p["entry"]:
                        print(f"     . {t}")
            else:
                print(f"     [{w['hex']}] not in the dictionary")


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("folios", nargs="*")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args(argv)
    E = ktlook.entries()
    if a.all:
        import ktbook
        out = {}
        for pg, _, _, _ in ktbook.folios():
            d = folio(pg, E)
            if d:
                out[pg] = d
        json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False)
        print(f"wrote {OUT}: {len(out)} folios")
        return 0
    if a.json:
        print(json.dumps({pg: folio(pg, E) for pg in a.folios},
                         ensure_ascii=False, indent=1))
        return 0
    for pg in a.folios:
        show(pg, E)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
