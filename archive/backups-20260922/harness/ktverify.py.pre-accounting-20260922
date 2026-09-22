"""Put the reading edition back beside the manuscript, worst first, to be read.

    python3 ktverify.py risk          the accounting, ranked
    python3 ktverify.py brief 12      the riskiest paragraphs, each with its gloss
    python3 ktverify.py folio 002r    one folio: its gloss and its reading

The reading edition is interpretive: it resolves the codex's broken lines
against the books it is compiled from. That freedom is the point of it, and it
is also the thing that has to be policed, so this pass puts every paragraph
back beside the manuscript's own gloss, so that a person reading the two can
answer three questions:

    KEPT      does the paragraph say what the gloss says?
    ADDED     is there a person, place, event or speech in it that is in
              neither the gloss nor the source it was shown?
    DROPPED   is there something in the gloss that the paragraph leaves out?

Of those, only ADDED can be counted by a program, and this one counts it: a
content word in neither the gloss nor the source is an import, and the list of
them is printed at the head of every paragraph. Drift and omission need a
reader. Omission is expected and is not a fault: the codex repeats a formula
six times and a readable paragraph folds it, which is editing, not loss, and
the gloss stands in full at the back.

NO MODEL JUDGES THIS. A model that wrote the paragraph is not a witness to it,
and a second model asked to mark the first one's work has no more access to the
manuscript than the first had. This file does the arithmetic -- which content
words in a paragraph are in its own gloss, which are only in the source it was
shown, which are in neither -- ranks the paragraphs by how much of them came
from somewhere other than the manuscript, and prints them next to the gloss to
be read by a person.
"""
import argparse
import json
import os
import re
import sys
import concurrent.futures as cf

import corpus
import ktbook
import ktenglish as KE
import ktsource as S

READ = os.path.join(corpus.ROOT, "work", "rohonc", "translation", "reading.md")
PLAIN = os.path.join(corpus.ROOT, "work", "rohonc", "translation", "translation.md")
OUT = os.path.join(corpus.ROOT, "work", "rohonc", "verify.json")
MODEL = "deepseek/deepseek-v4-pro-0813"
EXTRA = {"reasoning": {"enabled": False}}

def paragraphs(path):
    """Each paragraph of a reading, with the folios it cites."""
    txt = open(path, encoding="utf-8").read()
    cite = re.compile(r"\((\d{3}[rv](?:\s*[-–,]\s*\d{3}[rv])*)\)\s*$")
    order = [pg for pg, _, _, _ in ktbook.folios()]
    out = []
    for i, par in enumerate(txt.split("\n\n")):
        p = par.strip()
        if not p or p.startswith("#"):
            continue
        m = cite.search(p)
        if not m:
            continue
        pgs = []
        for bit in re.split(r"\s*,\s*", m.group(1)):
            ends = re.split(r"\s*[-–]\s*", bit)
            if len(ends) == 2 and ends[0] in order and ends[1] in order:
                a, b = order.index(ends[0]), order.index(ends[1])
                pgs.extend(order[min(a, b):max(a, b) + 1])
            else:
                pgs.extend(e for e in ends if e in order)
        out.append({"i": i, "text": p, "pages": pgs})
    return out


def gloss_map():
    return {pg: lines for pg, (_, lines) in KE.folios().items()}



def risk_table():
    """Every paragraph, with where its words came from."""
    import ktreading as R
    pars = paragraphs(READ)
    gl = gloss_map()
    src = json.load(open(S.OUT, encoding="utf-8")) if os.path.isfile(S.OUT) else {}
    bl = R.blocks()
    rows = []
    for p in pars:
        gw, sw = set(), set()
        for pg in p["pages"]:
            if pg in bl:
                a, b = R.words_of(pg, bl, src)
                gw |= a; sw |= b
        ms, sr, no = R.account(p["text"], gw, sw)
        tot = max(1, len(ms) + len(sr) + len(no))
        rows.append({"pages": p["pages"], "i": p["i"], "text": p["text"],
                     "ms": len(ms), "src": len(sr), "no": sorted(no),
                     "off": round(100.0 * (len(sr) + len(no)) / tot, 1)})
    rows.sort(key=lambda r: (-len(r["no"]), -r["off"]))
    return rows, gl


def show(row, gl, width=0):
    print("=" * 78)
    print(" ".join(row["pages"]),
          f"   from the manuscript {row['ms']}, from the source {row['src']}, "
          f"from neither {len(row['no'])}   {row['off']}% not from the codex")
    if row["no"]:
        print("  NOT IN EITHER:", ", ".join(row["no"][:20]))
    print("\nTHE READING\n" + row["text"])
    print("\nTHE MANUSCRIPT")
    for pg in row["pages"]:
        print(f"  [{pg}]")
        for l in gl.get(pg, []):
            print("    " + l)
    print()


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["risk", "brief", "folio"])
    ap.add_argument("arg", nargs="?")
    a = ap.parse_args(argv)
    rows, gl = risk_table()
    if a.cmd == "risk":
        tot_ms = sum(r["ms"] for r in rows); tot_sr = sum(r["src"] for r in rows)
        tot_no = sum(len(r["no"]) for r in rows)
        t = max(1, tot_ms + tot_sr + tot_no)
        print(f"paragraphs {len(rows)}")
        print(f"  content words from the manuscript  {tot_ms:>6}  {100.0*tot_ms/t:.1f}%")
        print(f"  only in the source it was shown    {tot_sr:>6}  {100.0*tot_sr/t:.1f}%")
        print(f"  in neither                         {tot_no:>6}  {100.0*tot_no/t:.1f}%")
        print(f"  paragraphs with a word from neither {sum(1 for r in rows if r['no'])}")
        for r in rows[:25]:
            print(f"  {' '.join(r['pages']):26} off {r['off']:>5}%  {', '.join(r['no'][:8])}")
        return 0
    if a.cmd == "folio":
        for r in rows:
            if a.arg in r["pages"]:
                show(r, gl)
        return 0
    for r in rows[:int(a.arg or 8)]:
        show(r, gl)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
