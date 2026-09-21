"""READINGS BUILT FROM A PASSAGE THE FOLIO DOES NOT CITE.

Four of the errors found on 2026-09-21 failed the same way, and it is a way
that can be tested without reading anything:

  9107c1 'with all thy heart'  its evidence cites Deuteronomy 6:5.
                               075v cites Acts 1:11.
  060520444520ae0 'was accused' evidence cites Luke 16:1.
                               169r cites Luke 16:8.
  7b2670ae0520 'sons'          evidence cites Matthew 21:28 / Luke 15:11.
                               064r cites John 10:11. It was SHEPHERD.
  5202da2da 'creatures'        read off the crucifixion, refused by Luke 19.

So: take the scripture reference written in a reading's OWN evidence, take
what the folios it stands on actually cite, and compare. A reading whose
evidence names a book nobody cites at any of its occurrences was made from a
passage the manuscript does not claim to be telling there.

THE BAR, DECLARED BEFORE THE RUN. None. This is a detector for one known
failure shape, not a gate, and its output is a reading list ordered by how
far the miss goes:

  BOOK    the evidence names a book that NO folio of this sign cites.
          The strongest signal: all four errors above are here.
  CHAPTER the book matches somewhere but no folio cites that chapter.
  VERSE   book and chapter match, the verse does not.
  OK      the evidence's reference is among what its folios cite.
  NONE    the evidence names no scripture, or no folio carries a citation.
          Not a fault. Most readings are argued from the book itself.

A hit is not a verdict. K&T's apparatus, a parallel passage elsewhere and
the book's own formulas are all legitimate evidence that will land here.
Read the line before touching it -- 'crucified' is BOOK and is correct.

    python3 ktmiscite.py            the list, worst first
    python3 ktmiscite.py --class BOOK
"""
import json
import re
import sys
from collections import Counter, defaultdict

import ktaffix as A
import ktcross as K
import ktleft as L

BOOKRE = re.compile(
    r"\b((?:[123]\s*)?(?:Kings|Samuel|Chronicles|Corinthians|Thessalonians|"
    r"Timothy|Peter|John|Maccabees|Machabees|Esdras)|Genesis|Exodus|Leviticus|"
    r"Numbers|Deuteronomy|Joshua|Judges|Ruth|Esther|Job|Psalms?|Proverbs|"
    r"Ecclesiastes|Isaiah|Isaias|Jeremiah|Jeremias|Ezekiel|Daniel|Hosea|Joel|"
    r"Amos|Obadiah|Jonah|Micah|Nahum|Habakkuk|Zephaniah|Haggai|Zechariah|"
    r"Malachi|Matthew|Mark|Luke|Acts|Romans|Galatians|Ephesians|Philippians|"
    r"Colossians|Titus|Philemon|Hebrews|James|Jude|Revelation|Apocalypse|"
    r"Tobias|Judith|Wisdom|Ecclesiasticus|Baruch)\s*(\d+)\s*[:.]\s*(\d+)")

ALIAS = {"Isaias": "Isaiah", "Jeremias": "Jeremiah", "Apocalypse": "Revelation",
         "Machabees": "Maccabees", "Psalm": "Psalms"}


def norm(b):
    b = re.sub(r"\s+", "", b)
    for k, v in ALIAS.items():
        if b.endswith(k):
            b = b.replace(k, v)
    return b


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    p = json.load(open('proposals.json', encoding='utf-8'))
    ours = {k: v for k, v in p.items()
            if not k.startswith('_') and isinstance(v, dict)
            and v.get('tier') in ('A', 'B', 'C', 'D')}

    where = defaultdict(set)
    for pg in doc:
        for ln in pg.lines:
            for t in [x for run in ln for x in run]:
                where[K.hx(A.strip(t)[0])].add(pg.page)
    refs = {}
    for pg in sorted({x.page for x in doc}):
        r = L.refs_in(K.note_for(pg))
        if r:
            refs[pg] = r

    rows = []
    for h, v in sorted(ours.items()):
        claimed = [(norm(m.group(1)), int(m.group(2)), int(m.group(3)))
                   for m in BOOKRE.finditer(v.get('evidence', ''))]
        cites = []
        for pg in where.get(h, ()):
            for b, c, a, z in refs.get(pg, ()):
                cites.append((norm(b), c, a, z))
        if not claimed or not cites:
            rows.append((h, v, "NONE", claimed, cites)); continue
        best = "BOOK"
        for cb, cc, cv in claimed:
            for b, c, a, z in cites:
                if b != cb:
                    continue
                best = "CHAPTER" if best == "BOOK" else best
                if c != cc:
                    continue
                best = "VERSE" if best in ("BOOK", "CHAPTER") else best
                if a <= cv <= (z if z != 999 else 999):
                    best = "OK"
        rows.append((h, v, best, claimed, cites))

    cnt = Counter(r[2] for r in rows)
    print("READINGS WHOSE EVIDENCE NAMES A PASSAGE THEIR FOLIOS DO NOT CITE\n")
    for k in ("BOOK", "CHAPTER", "VERSE", "OK", "NONE"):
        print(f"    {k:8s} {cnt[k]:5d}")
    want = argv[argv.index('--class') + 1] if '--class' in argv else "BOOK"
    print(f"\n  class {want}, worst first by occurrences:\n")
    sel = [r for r in rows if r[2] == want]
    for h, v, k, claimed, cites in sorted(sel, key=lambda r: -len(where.get(r[0], ()))):
        cl = ", ".join(f"{b} {c}:{d}" for b, c, d in claimed[:2])
        ct = ", ".join(sorted({b for b, _, _, _ in cites}))[:46]
        print(f"    {h:22s} {v['tier']} n={v.get('n'):<4} '{v['gloss'][:22]:22s}' "
              f"says {cl[:26]:26s} folios cite {ct}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
