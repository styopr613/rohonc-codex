"""Print the sense the folio's own source passage uses, not always the first.

THE PROBLEM, measured before the fix. Kiraly & Tokai's entries carry several
senses for one sign, in their order. kttranslate prints the first. On folios
whose translation note cites a chapter and verse, 9437 rendered tokens have
more than one sense, and on 1628 of them the printed sense is NOT in the cited
passage while another sense of the SAME entry is. That is five times the
number of words still dark, and it is what makes a finished page read as word
salad: "somebody" where the verse says man, "each, every" where it says whole,
"Adam" where it says man, "spirit" where it says soul.

THE RULE, declared before the run.

  For one token, on a folio that cites chapter and verse:
    0. if K&T's FIRST sense has no content word in it at all -- "and", "to",
       "this", a grammatical label -- leave the sign alone and stop;
    1. take K&T's senses for the sign IN THEIR ORDER;
    2. take the content stems of the cited passage, widened one verse each way,
       from BOTH the Douay-Rheims and the King James;
    3. if the FIRST sense has a content stem in that passage, keep it -- the
       author's order wins whenever it can;
    4. otherwise, if EXACTLY ONE later sense has a content stem there, print
       that sense instead;
    5. if two or more later senses match, or none does, keep the first.

  Nothing is invented: every candidate is a sense Kiraly & Tokai published for
  that sign. The chooser is the source text, which is outside the codex, so
  this is not the book arguing with itself.

  WHAT IT CANNOT DO. It cannot fix a folio with no cited source, and there it
  is not run. It cannot fix a sign cut wrongly by the segmenter. And it makes
  the rendering fit the passage better BY CONSTRUCTION, so the fit of a page
  to its passage can never again be used as evidence for the decipherment.
  That is why gate 2 was run and recorded BEFORE this existed, and its 18.6
  sigma stands on the unfitted rendering. Rerunning gate 2 after this would be
  circular and must not be done.

    python3 ktsensefit.py            what it changes, by folio
    python3 ktsensefit.py --table    write work/rohonc/sensefit.json
"""
import json
import os
import re
import sys
from collections import Counter

import corpus
import ktaffix as A
import ktcross as K
import ktleft as L
import kttranslate as T

OUT = os.path.join(corpus.ROOT, "work", "rohonc", "sensefit.json")


def stems(gloss):
    g = re.sub(r"[<\[(][^>\])]*[>\])]", " ", gloss).translate(K.ACCENT)
    return {K.stem(w.lower()) for w in re.findall(r"[a-zA-Z]+", g)
            if len(w) > 2 and w.lower() not in K.STOP}


def build(gl, doc):
    vv, vd = L.verses(), L.verses_dr()
    cited = {}
    for p in sorted({p.page for p in doc}):
        r = L.refs_in(K.note_for(p))
        if r:
            cited[p] = r
    pas = {}
    for pg, refs in cited.items():
        txt = " ".join(t for _, t in L.passage(vv, refs, 1) + L.passage(vd, refs, 1)).lower()
        pas[pg] = {K.stem(w) for w in re.findall(r"[a-z]+", txt)}
    pick = {}
    n_seen = n_kept = n_moved = n_tie = 0
    for p in doc:
        st = pas.get(p.page)
        if not st:
            continue
        for t in p.tokens:
            b = A.strip(t)[0]
            if b not in gl:
                continue
            senses = T.ORDER.get(b) or sorted(gl[b])
            if len(senses) < 2:
                continue
            # A FIRST SENSE THAT IS A FUNCTION WORD IS NEVER MOVED. Without
            # this the rule misfires on exactly the commonest signs: "and"
            # has no content stem, so step 3 can never hold, and the sign
            # falls through to whatever later sense the passage happens to
            # contain -- "and" became "also" 87 times, "from" became "away"
            # 29 times, "this" became "thus" 12 times. A match on a word that
            # common is chance. The rule now only runs where the first sense
            # is a content word the passage fails to support.
            first = stems(senses[0])
            if not first:
                continue
            n_seen += 1
            if first & st:
                n_kept += 1
                continue
            hit = [s for s in senses[1:] if stems(s) & st]
            if len(hit) == 1:
                pick[(p.page, K.hx(b))] = hit[0]
                n_moved += 1
            else:
                n_tie += 1
    return pick, (n_seen, n_kept, n_moved, n_tie)


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    pick, (n_seen, n_kept, n_moved, n_tie) = build(gl, doc)
    print("SENSE FIT: print the sense the folio's cited passage uses")
    print(f"  tokens with more than one K&T sense, source cited   {n_seen}")
    print(f"  first sense is in the passage, kept                 {n_kept}")
    print(f"  moved to a later sense, uniquely matched            {n_moved}")
    print(f"  no match or two matches, first sense kept           {n_tie}")
    by = Counter(pg for pg, _ in pick)
    print(f"  folios changed                                      {len(by)}")
    if "--table" in argv:
        json.dump({f"{pg}|{h}": s for (pg, h), s in pick.items()},
                  open(OUT, "w"), indent=0, sort_keys=True)
        print(f"  wrote {OUT}")
    else:
        for pg, n in by.most_common(12):
            print(f"    {pg}  {n} words")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
