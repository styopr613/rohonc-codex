"""Sort the folio-English leaks into the three classes that need three answers.

ktenglish.py flags every content word in the model's English that nothing in
that folio's gloss supports. The raw count is large and useless as one number,
because the flags are not one kind of problem:

  1 CONTENT      a name, a number, a place, a doctrinal specific or an event
                 the gloss does not contain. This is the dangerous class: a
                 model that knows the Vulgate and the Golden Legend completes
                 the story from the SOURCE instead of the codex, which puts
                 back at the prose layer exactly the circularity the gates
                 were built to rule out. Every one of these is fixed or cut.

  2 CONNECTIVE   a pronoun resolved, a verb of motion supplied, scaffolding.
                 Harmless in prose that is labelled editorial, which is what
                 the front matter says it is. Dismissed in bulk, counted.

  3 INTERPRETIVE the residue: naming a parable, identifying a verse, glossing
                 an allegory the codex does not state. Often true and often
                 useful, but it belongs in the editor's voice, not woven in as
                 though the manuscript said it. Hand-reviewed.

Classification is by surface form, and deliberately errs upward: a word it
cannot place goes to 3, never to 2.

    python3 ktleakaudit.py            counts, and class 1 in full
    python3 ktleakaudit.py --dump F   class 1 and 3 to a file for review
"""
import argparse
import json
import os
import re
import sys
from collections import Counter

import corpus
import ktenglish as E

NUMWORD = set("""zero one two three four five six seven eight nine ten eleven
twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty
thirty forty fifty sixty seventy eighty ninety hundred thousand million score
first second third fourth fifth sixth seventh eighth ninth tenth eleventh
twelfth twentieth thirtieth""".split())

# Light verbs and generic nouns a writer supplies to make a sentence move.
# Nothing doctrinal, nothing nameable, nothing countable.
CONNECT = set("""go goe going gone went come came coming take took taken make
made making give gave given put set sit sat stand stood turn turned look
looked speak spoke spoken tell told know knew known see saw seen hear heard
begin began begun bring brought get got become became keep kept leave left
let bear bore find found hold held call called ask asked answer answered
thing things man men people place places time times day days way ways word
words one ones other others part parts side sides end ends next then after
before while during upon into onto toward towards
this that these those who which what whose whom
be am is are was were been being have has had having do does did done
he she it they we you i him her them us me his hers their our your my
there here now thus therefore however moreover indeed also""".split())

CAPS = re.compile(r"\b([A-Z][a-z]{2,})\b")


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--dump")
    a = ap.parse_args(argv)
    fo = E.folios()
    have = E.load()
    cls = Counter()
    rows = []
    for pg in sorted(have):
        eng = have[pg]["english"]
        lines = fo.get(pg, ("", []))[1]
        if not lines:
            continue
        gl = set()
        for l in lines:
            gl |= E.stems(l)
        # proper nouns of the English, by surface form, excluding sentence starts
        proper = {w.lower() for w in CAPS.findall(re.sub(r"(^|[.!?\"“”]\s*)[A-Z]",
                                                         lambda m: m.group(0).lower(),
                                                         eng))}
        for w in E.leaks(eng, lines):
            if w in NUMWORD or any(E.norm(n) == w for n in NUMWORD):
                k = 1
            elif any(E.norm(p) == w for p in proper):
                k = 1
            elif w in CONNECT or any(E.norm(c) == w for c in CONNECT):
                k = 2
            else:
                k = 3
            cls[k] += 1
            rows.append((k, pg, w))
    tot = sum(cls.values())
    print(f"{tot} leaks over {len(have)} folios")
    print(f"  1 CONTENT       {cls[1]:>5}   fix or cut, every one")
    print(f"  2 CONNECTIVE    {cls[2]:>5}   dismissed in bulk, licensed by the front matter")
    print(f"  3 INTERPRETIVE  {cls[3]:>5}   hand-reviewed, moved to the editor's voice")
    print()
    c1 = Counter(w for k, _, w in rows if k == 1)
    print("class 1, commonest first:")
    for w, n in c1.most_common(40):
        pgs = [p for k, p, x in rows if k == 1 and x == w][:4]
        print(f"   {w:<16} {n:>3}   {' '.join(pgs)}")
    if a.dump:
        with open(a.dump, "w", encoding="utf-8") as f:
            for k in (1, 3):
                f.write(f"===== class {k}\n")
                for kk, pg, w in rows:
                    if kk == k:
                        f.write(f"{pg}\t{w}\n")
        print("\nwrote", a.dump)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
