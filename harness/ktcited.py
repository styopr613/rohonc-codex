"""Which guesses sit on a line Kiraly and Tokai already cite, and under what.

The standing lesson of this project is that K&T cite folio:line inside their
entries, so a token we have guessed at is often a token they have already
read -- under another headword, as a variant, or inside an expression. The
first guess audited this way, 520b42 "shall perish", turned out to be the
front half of a word K&T cite at exactly those lines as their own variant of
"but, however". We had split one of their words in two and invented a verb
for the front half.

This prints, for every bracketed guess, every K&T entry that cites a line the
guess occurs on, with the entry's own codes. It decides nothing: an entry can
cite a line for a different word on the same line. It says where to look.

    python3 ktcited.py                 every guess with at least one hit
    python3 ktcited.py --hex 520b42    one guess
    python3 ktcited.py --summary
"""
import json
import re
import sys
from collections import defaultdict

import ktaffix as A
import ktcross as K
import ktdict


def hx(s):
    return "".join(f"{ord(c) - 0xE000:03x}" for c in s)


def entries():
    """(headword hex, flat text, every rohonc code the entry prints)."""
    raw = json.load(open(ktdict.DICT, encoding="utf-8"))
    out = []
    for e in raw:
        txt = " ".join(" ".join(f.get("text", "") for f in e["entry"]).split())
        codes = set()
        for f in e["entry"]:
            for run in re.findall(r"[\ue000-\uf8ff]+", f.get("text", "")):
                codes.add(hx(run))
        out.append((hx(e["code"]), txt, codes))
    return out


def touches(h, codes):
    """h is one of these codes, or sits inside one on glyph boundaries."""
    for c in codes:
        if c == h:
            return c
        j = c.find(h)
        while j != -1:
            if j % 3 == 0 and (j + len(h)) % 3 == 0:
                return c
            j = c.find(h, j + 1)
    return None


REF = re.compile(r"\b(\d{3}[rv])(\d{2})\b")


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    p = json.load(open('proposals.json', encoding='utf-8'))
    guesses = {k for k, v in p.items() if not k.startswith('_')
               and isinstance(v, dict) and v.get('tier') == 'G'}
    one = argv[argv.index('--hex') + 1] if '--hex' in argv else None
    if one:
        guesses = {one}

    where = defaultdict(set)            # hex -> {"072v05", ...}
    for pg in doc:
        for i, ln in enumerate(pg.lines, 1):
            key = f"{pg.page}{i:02d}"
            for run in ln:
                for t in run:
                    h = K.hx(A.strip(t)[0])
                    if h in guesses:
                        where[h].add(key)

    byline = defaultdict(list)          # "072v05" -> [(code, text, codes)]
    for code, txt, codes in entries():
        for m in REF.finditer(txt):
            byline[m.group(0)].append((code, txt, codes))
    sharp = '--sharp' in argv

    hits = 0
    for h in sorted(guesses):
        got = []
        for key in sorted(where.get(h, ())):
            for code, txt, codes in byline.get(key, ()):
                hit = touches(h, codes)
                if sharp and not hit:
                    continue
                got.append((key, code, txt, hit))
        if not got:
            continue
        hits += 1
        if '--summary' in argv:
            continue
        v = p[h]
        print(f"=== {h}  \"{v.get('gloss','')}\"  n={v.get('n')}  "
              f"lines {','.join(sorted(where[h]))}")
        seen = set()
        for key, code, txt, hit in got:
            if (code, txt[:60]) in seen:
                continue
            seen.add((code, txt[:60]))
            star = f'   <<< entry prints {hit}' if hit else ''
            print(f"    {key}  {code:<22}{txt[:190]}{star}")
        print()
    what = ("whose entry also prints the guess's own glyphs"
            if sharp else "sit on a line K&T cite")
    print(f"-- {hits} of {len(guesses)} guesses {what}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
