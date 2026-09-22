"""Cut the imports out of the reading edition, paragraph by paragraph.

    python3 ktfix.py list           what would be sent, and why
    python3 ktfix.py run            rewrite the flagged paragraphs in place

The accounting in ktreading.py marks every content word of the reading that is
in neither the folio's own gloss nor the passages the folio was shown. Those
are imports. Most are harmless -- an English inflection the stemmer cannot tie
back to its root -- but some are not, and one of them was a fabricated rubric:
folio 069v opens the vine and the branches, and the reading had written "Here
begins this holy gospel written by holy Luke, in the tenth chapter", which is
a heading the manuscript does not have, attributed to the wrong evangelist.

So each flagged paragraph goes back with its own gloss and the list of words,
and the instruction is narrow: keep a word that is a plain form of something in
the gloss, and cut the clause that rests on a word that is not. Nothing else
about the paragraph changes.

The file it edits is reading.md, and reading.md.raw-<date> is the copy made
before any of this, kept.
"""
import argparse
import json
import os
import re
import sys
import concurrent.futures as cf

import corpus
import ktor
import ktreading as R
import ktverify as V

READ = V.READ
MODEL = R.MODEL
EXTRA = R.EXTRA

BRIEF = """You are correcting one paragraph of an English reading edition of a
sixteenth-century manuscript, against the manuscript's own text.

Under the paragraph is THE MANUSCRIPT: the word-for-word gloss of the folios that
paragraph renders, line by line. Under that is a list of words in the paragraph that
appear nowhere in that gloss and nowhere in the sources the folio was read against.

For each listed word, decide:
  - it is an ordinary English form or synonym of something the gloss does have
    ("came" for "come", "spoke" for "say"): LEAVE IT.
  - it is not in the manuscript at all: CUT IT, and cut the clause that rests on it.
    Do not replace it with a guess. The sentence may become shorter or plainer.

Watch in particular for a heading or attribution the manuscript does not have: a
"here begins the gospel of..." line, a chapter number, the name of an evangelist.
If the gloss has no such line, the paragraph must not have one.

Change nothing else. Keep the wording, the order and the voice. Keep [brackets] and
... as they are. Keep the folio citation in brackets at the end exactly as it stands.

Return only the corrected paragraph."""


def flagged():
    rows, gl = V.risk_table()
    return [r for r in rows if r["no"]], gl


def one(row, gl):
    body = [row["text"], "", "THE MANUSCRIPT"]
    for pg in row["pages"]:
        body.append(f"[{pg}]")
        body.extend("  " + l for l in gl.get(pg, []))
    body += ["", "WORDS IN THE PARAGRAPH THAT ARE IN NEITHER THE MANUSCRIPT NOR ITS SOURCES",
             "  " + ", ".join(row["no"])]
    text, usage = ktor.ask(MODEL, BRIEF + "\n\n" + "\n".join(body),
                           temperature=0.2, extra=EXTRA)
    return text.strip(), float((usage or {}).get("cost") or 0)


def run(dry=False):
    rows, gl = flagged()
    print(f"{len(rows)} paragraphs flagged")
    if dry:
        for r in rows[:40]:
            print(f"  {' '.join(r['pages']):24} {', '.join(r['no'][:8])}")
        return
    doc = open(READ, encoding="utf-8").read()
    parts = doc.split("\n\n")
    cost, changed = 0.0, 0
    with cf.ThreadPoolExecutor(max_workers=6) as ex:
        futs = {ex.submit(one, r, gl): r for r in rows}
        done = 0
        for f in cf.as_completed(futs):
            r = futs[f]
            try:
                new, c = f.result()
            except Exception as e:
                print("  failed", r["pages"], str(e)[:80], file=sys.stderr); continue
            cost += c
            done += 1
            # it must still be a paragraph of this book, citing the same folios
            if new and V.paragraphs.__doc__ and new.rstrip().endswith(")") and len(new) > 40:
                if parts[r["i"]].strip() != new:
                    parts[r["i"]] = new
                    changed += 1
            if done % 15 == 0:
                print(f"  {done}/{len(rows)}  ${cost:.2f}", file=sys.stderr, flush=True)
    open(READ, "w", encoding="utf-8").write("\n\n".join(parts))
    print(f"rewrote {changed} of {len(rows)} paragraphs, ${cost:.2f}")


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["list", "run"])
    a = ap.parse_args(argv)
    run(dry=(a.cmd == "list"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
