"""Carry the restored words up into the English prose of the translation.

The prose paragraphs in rohonc_translation.md were written while 1,087 words
of the book had no reading, so they carry an ellipsis at every one of them.
Those words now have readings or bracketed guesses. The prose is hand-made
sentence-making and cannot be regenerated, but it CAN be updated in place,
because every prose line sits directly above the gloss line it was made from
and the holes line up one for one.

THE RULE, declared before the run.

  For one line of the translation file:
    1. take the prose line and the gloss line under it;
    2. count the holes in each -- the prose writes a hole as an ellipsis or as
       a bracketed guess ending in '?', the gloss writes it as [?] or [?HEX];
    3. rewrite ONLY if THREE counts agree: the prose holes, the gloss holes as
       the line was written, and the holes the rendering has now. If any two
       disagree the alignment is not trustworthy and the line is left exactly
       as it was. Two of the three was not enough and produced a sentence
       that said "was buried" twice;
    4. replace the nth prose hole with the nth word now read for that sign,
       in brackets if the reading is a guess and plain if it is not.

  Nothing is invented here and no new reading is made. This moves words that
  are already in proposals.json from the gloss line into the sentence above
  it, and refuses whenever it cannot prove the two lines correspond.

    python3 ktprose.py --dry     what it would change
    python3 ktprose.py           write it, with a dated backup
"""
import json
import os
import re
import shutil
import sys
from datetime import date

import corpus
import ktaffix as A
import ktcross as K
import kttranslate as T

TRANS = os.path.join(corpus.ROOT, "work", "rohonc", "translation",
                     "rohonc_translation.md")
PHOLE = re.compile(r"\[[^\]]*\]|…|\[…\]")
GHOLE = re.compile(r"\[\?[0-9a-f]*\]")


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    # folio:line -> the signs that were holes, in order
    holes = {}
    for p in doc:
        for i, ln in enumerate(p.lines, 1):
            tk = [t for run in ln for t in run]
            hs = [A.strip(t)[0] for t in tk if A.strip(t)[0] not in gl
                  and A.strip(t)[0] not in seg and A.strip(t)[0] not in var]
            if hs:
                holes[(p.page, i)] = hs
    text = open(TRANS, encoding="utf-8").read()
    out, page, changed, refused = [], None, 0, 0
    lines = text.split("\n")
    k = 0
    while k < len(lines):
        ln = lines[k]
        m = re.match(r"^## (\d{3}[rv]) ", ln)
        if m:
            page = m.group(1)
        pm = re.match(r"^\*\*(\d+)\*\*\s+(.*)$", ln)
        if pm and page and k + 1 < len(lines) and lines[k + 1].startswith("`"):
            i = int(pm.group(1))
            prose, gloss = pm.group(2), lines[k + 1]
            hs = holes.get((page, i), [])
            npro = len(PHOLE.findall(prose))
            nglo = len(GHOLE.findall(gloss))
            # TRIPLE AGREEMENT. The prose hole count, the gloss hole count as
            # the line was WRITTEN, and the hole count as the rendering stands
            # now must all be equal. Two of the three were not enough: the
            # segmenter has grown since the prose was made, so the current
            # hole set is not the one the prose saw, and matching on it alone
            # put "was buried" into a sentence that already said it.
            if hs and npro == len(hs) == nglo:
                words = []
                for b in hs:
                    if b in prop:
                        g, tier = prop[b]
                        w = g.replace("_", " ")
                        words.append("[%s]" % w if tier == "G" else w)
                    else:
                        words.append("[…]")
                it = iter(words)
                prose = PHOLE.sub(lambda mm: next(it), prose)
                out.append("**%d**  %s" % (i, prose))
                changed += 1
                k += 1
                continue
            elif hs:
                refused += 1
        out.append(ln)
        k += 1
    print(f"prose lines rewritten   {changed}")
    print(f"refused, holes did not line up   {refused}")
    if "--dry" not in argv:
        bak = TRANS + ".pre-prose-" + date.today().isoformat().replace("-", "")
        n = 1
        while os.path.exists(bak):
            n += 1
            bak = TRANS + f".pre-prose-{date.today().isoformat().replace('-','')}-{n}"
        shutil.copy(TRANS, bak)
        open(TRANS, "w", encoding="utf-8").write("\n".join(out))
        print("wrote", TRANS)
        print("backup", os.path.basename(bak))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
