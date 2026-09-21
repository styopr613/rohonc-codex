"""How much of Book One would a change to the readings break?

Book One quotes the gloss. Harden the readings and some of those words move,
and the question "scrap it or patch it" is not a matter of taste -- it is a
count, and this makes the count.

Every quotation in the retelling is a set of content stems. Each stem is
looked for in the gloss of the folios that quotation's part cites, and
classified by the strongest place it is found:

    KT        a plain dictionary word. Kiraly & Tokai's. Hardening our own
              readings cannot move it.
    VAR       ~word, a spelling their own apparatus files as a variant.
              Theirs as well.
    CUT       word-word, cut into dictionary codes by ktname/ktsegment.
              Ours, but gated at 12.4 and 9.8 sigma.
    BRACKET   [word], a restoration. Ours, never counted as a reading, and
              the class most likely to change under hardening.

A quotation is EXPOSED when at least one of its stems is available ONLY from
a bracketed token -- nothing else in the cited gloss supplies that word. Those
are the quotations a change can break. Everything else survives a change to
the brackets untouched.

The bar this reports against, declared before the run: if fewer than a fifth
of quotations are exposed, patching beats rewriting, because the gate names
every broken quotation by its own text and each is a one-line fix. If more
than half are exposed, the prose is resting on the guesses and should be
rewritten against the hardened gloss instead.

    python3 ktexpose.py             # the counts, per part
    python3 ktexpose.py --list      # every exposed quotation, with its stems
    python3 ktexpose.py --folio     # which folios carry the exposure
"""
import collections
import os
import re
import sys

import corpus
import ktbook
import ktenglish as E
import ktretellcheck as R

BRACKET = re.compile(r"\[([^\]]+)\]")


def classify(lines):
    """stem -> the strongest class it is available in, over these gloss lines."""
    out = {}

    def put(s, cls, rank):
        if s not in out or rank > out[s][1]:
            out[s] = (cls, rank)

    for l in lines:
        body = re.sub(r"^\s*\d+\s+", "", l)
        for tok in body.split():
            br = bool(BRACKET.search(tok))
            bare = BRACKET.sub(r"\1", tok)
            var = bare.startswith("~") or "~" in bare
            cut = "-" in bare.strip("-")
            for s in E.stems(bare):
                if br:
                    put(s, "BRACKET", 0)
                elif cut:
                    put(s, "CUT", 1)
                elif var:
                    put(s, "VAR", 2)
                else:
                    put(s, "KT", 3)
    return {k: v[0] for k, v in out.items()}


def main(argv):
    want_list = "--list" in argv
    want_fol = "--folio" in argv
    fol = {pg: (pg, t, pr, ln) for pg, t, pr, ln in ktbook.folios()}
    txt = open(R.RT, encoding="utf-8").read()
    tot = collections.Counter()
    folio_hits = collections.Counter()
    exposed_rows = []

    for m in re.finditer(r"^## ([^\n]+)\n\n### folios (\d{3}[rv])–(\d{3}[rv])\n"
                         r"(.*?)(?=^## |\Z)", txt, re.M | re.S):
        name, _, _, body = m.groups()
        cited = sorted(set(R.FOL.findall(body)))
        lines = []
        for p in cited:
            if p in fol:
                lines += fol[p][3]
        cls = classify(lines)
        n = exp = 0
        for q in R.QUOTE.findall(body):
            n += 1
            stems = [w for w in sorted(E.stems(q)) if w not in R.STOP]
            only_br = [w for w in stems if cls.get(w) == "BRACKET"]
            for w in stems:
                tot[cls.get(w, "MISSING")] += 1
            if only_br:
                exp += 1
                exposed_rows.append((name.split(".")[0], q, only_br))
                for p in cited:
                    if p in fol and any(
                            w in classify(fol[p][3]) for w in only_br):
                        folio_hits[p] += 1
        pct = 100.0 * exp / n if n else 0.0
        print(f"  {name.split('.')[0]:<5} {n:4d} quotations   "
              f"{exp:3d} exposed  {pct:5.1f}%")
        tot["quotations"] += n
        tot["exposed"] += exp

    q, x = tot["quotations"], tot["exposed"]
    print(f"\n  {'TOTAL':<5} {q:4d} quotations   {x:3d} exposed  "
          f"{100.0*x/q if q else 0:5.1f}%")
    print("\n  content words quoted, by where the gloss supplies them:")
    body = sum(tot[k] for k in ("KT", "VAR", "CUT", "BRACKET", "MISSING"))
    for k in ("KT", "VAR", "CUT", "BRACKET", "MISSING"):
        print(f"    {k:<8} {tot[k]:5d}  {100.0*tot[k]/body if body else 0:5.1f}%")

    if want_list:
        print("\n  exposed quotations:")
        for part, quote, stems in exposed_rows:
            print(f"    {part:<5} «{quote[:58]}»")
            print(f"          only from a bracket: {' '.join(stems)}")
    if want_fol:
        print("\n  folios carrying the exposure, most first:")
        for pg, c in folio_hits.most_common(20):
            print(f"    {pg}  {c}")

    verdict = ("PATCH: the gate names every break and each is a one-line fix"
               if 100.0 * x / q < 20 else
               "REWRITE: the prose is resting on the guesses"
               if 100.0 * x / q > 50 else
               "MIXED: patch the quotations, re-argue the paragraphs that "
               "rest on a name or a number")
    print(f"\n  {verdict}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
