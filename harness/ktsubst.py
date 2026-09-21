"""K&T's glyph substitution rules, applied.

Some of their entries do not list variant spellings one by one. They state a
rule instead: "[var. {670} ~ {520}, {540}; {ae0} ~ {060}, o]" means that
inside this word 670 may be written 520 or 540, and ae0 may be written 060 or
dropped. Our variant apparatus reads explicit variant codes and cannot read a
rule, so every spelling covered only by a rule went unread -- and two of them
were read here as "as" when the word is their PRAY.

This expands every rule into the spellings it licenses and reports which of
those spellings occur in the book and are not yet read from the headword.

Nothing is decided here. A rule tells you the shape of a word, not which of
its senses is meant on a given line.

    python3 ktsubst.py               [--summary] [--all]
"""
import itertools
import json
import re
import sys
from collections import Counter

import ktaffix as A
import ktcross as K
import ktdict

PUA = re.compile(r"[-]+")


def hx(s):
    """Hex of the PUA characters in s. The dictionary's rohonc fragments
    carry <u> markup inside them to group glyphs, so anything that is not a
    private-use character is dropped."""
    return "".join(f"{ord(c) - 0xE000:03x}" for c in s
                   if 0xE000 <= ord(c) <= 0xF8FF)


def glyphs(h):
    return [h[i:i + 3] for i in range(0, len(h), 3)]


def rules_of(e):
    """(headword hex, [(from_glyph, [to_glyph or ''])]) from one entry."""
    head, rules = [], []
    seen_bracket = False
    frs = e["entry"]
    # headword: the rohonc runs before the first '[' in the text
    for f in frs:
        t = f.get("text", "")
        if f.get("style") == "rohonc" and not seen_bracket:
            head.append(hx(t.strip()))
        if "[" in t:
            seen_bracket = True
            break
    # rules: "<rohonc> ~ <rohonc>, <rohonc>" inside the bracket
    flat = []
    for f in frs:
        t = f.get("text", "")
        flat.append(("R", hx(t.strip())) if f.get("style") == "rohonc"
                    else ("T", t))
    # "<glyph> ~ <glyph>, <glyph>, o" -- a rule replaces ONE glyph, so a
    # target longer than three hex characters ends the rule; that is an
    # explicit variant spelling being listed next, not a substitution.
    i = 0
    while i < len(flat):
        if (flat[i][0] == "R" and len(flat[i][1]) == 3
                and i + 1 < len(flat) and "~" in flat[i + 1][1]):
            src, tos, j = flat[i][1], [], i + 1
            while j + 1 < len(flat):
                sep = flat[j][1]
                if "\u00f8" in sep:
                    tos.append("")
                if flat[j + 1][0] != "R" or len(flat[j + 1][1]) != 3:
                    break
                if not ("~" in sep or sep.strip().startswith(",")):
                    break
                tos.append(flat[j + 1][1])
                j += 2
            if src and tos:
                rules.append((src, tos))
            i = j
        i += 1
    return "".join(head), rules


def expand(head, rules, cap=400):
    """Every spelling the rules license, the headword included."""
    g = glyphs(head)
    slots = []
    for x in g:
        alts = {x}
        for src, tos in rules:
            if src == x:
                alts |= set(tos)
        slots.append(sorted(alts))
    total = 1
    for s in slots:
        total *= len(s)
        if total > cap:
            return {head}
    return {"".join(c) for c in itertools.product(*slots)}


def main(argv):
    raw = json.load(open(ktdict.DICT, encoding="utf-8"))
    p = json.load(open('proposals.json', encoding='utf-8'))
    gl, doc, seg, var, prop, inv = K.build()
    counts = Counter()
    for pg in doc:
        for ln in pg.lines:
            for run in ln:
                for t in run:
                    counts[K.hx(A.strip(t)[0])] += 1
    head_hex = {hx(e["code"]) for e in raw}

    nrules = 0
    rows = []
    for e in raw:
        head, rules = rules_of(e)
        if not rules or not head:
            continue
        nrules += 1
        txt = " ".join(" ".join(f.get("text", "") for f in e["entry"]).split())
        for spell in sorted(expand(head, rules)):
            if spell == head or spell in head_hex or not counts.get(spell):
                continue
            v = p.get(spell)
            cur = (f"{v['tier']} {v.get('gloss')}"
                   if isinstance(v, dict) and v.get('gloss') else '')
            if cur and '--all' not in argv:
                pass
            rows.append((counts[spell], spell, head, cur, txt))
    rows.sort(reverse=True)
    if '--summary' in argv:
        print(f"{nrules} entries state a substitution rule")
        print(f"{len(rows)} spellings they license occur in the book and are "
              f"not themselves headwords")
        print(f"  of those, already read here: "
              f"{sum(1 for r in rows if r[3])}")
        print(f"  unread: {sum(1 for r in rows if not r[3])}")
        print(f"  total occurrences unread: "
              f"{sum(r[0] for r in rows if not r[3])}")
        return 0
    for n, spell, head, cur, txt in rows:
        print(f"{n:>5}x  {spell:<34}<- {head:<26}{cur:<22}{txt[:90]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
