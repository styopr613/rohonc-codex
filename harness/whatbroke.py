"""whatbroke — the one command to run when the readings have been hardened.

Book One quotes the gloss. Harden the readings and some of those words move.
This answers, in one run, the four questions that follow:

  1. WHAT BROKE.     Runs the retelling gate on its real exit status. Every
                     fabricated or stale quotation names itself, with the
                     missing word, and each is a one-line fix.

  2. WHAT IS EXPOSED. Every quotation is a set of content stems, and each stem
                     is classified by the strongest place the cited gloss
                     supplies it:

                       KT        a plain dictionary word -- Kiraly & Tokai's.
                                 Hardening our readings cannot move it.
                       VAR       ~word, a spelling their own apparatus files
                                 as a variant. Theirs as well.
                       CUT       word-word, cut into dictionary codes by
                                 ktname/ktsegment, gated at 12.4 and 9.8 sigma.
                       BRACKET   [word], a restoration. Ours, never counted as
                                 a reading, and the class most likely to move.

                     A quotation is EXPOSED when one of its stems is available
                     ONLY from a bracket. The bar, declared before the first
                     run: under a fifth exposed and patching beats rewriting,
                     because the gate names every break; over half and the
                     prose is resting on the guesses and should be rewritten
                     against the hardened gloss. It came out at 13.1%.

  3. WHAT IS LOAD-BEARING.  The gate's blind spot, and the reason this section
                     exists. A quotation is checked; the editorial sentence
                     around it is not. So if a NAME or a NUMBER moves --
                     Longinus, Cleopas, Vespasian, the age of the world --
                     the paragraph's whole argument dies and nothing flags it.
                     This lists every proper name and numeral the retelling
                     leans on that reaches the prose ONLY through a bracket.
                     A name Kiraly & Tokai supply is safe and needs no one's
                     time, and so is a name carrying an affix -- the hyphen in
                     "holy-John" is not a cut of ours. The first version of
                     this section did not make that distinction and flagged
                     seventeen names where five are real.

  4. WHAT IS LEFT.   Which parts have no retelling yet, and inside the parts
                     that do, which folios Book One has not drawn on. A folio
                     nobody cited is a folio nobody has read into the front of
                     the book.

    python3 whatbroke.py              all four
    python3 whatbroke.py --list       every exposed quotation, with its stems
    python3 whatbroke.py --left       only what is still unwritten
"""
import collections
import re
import subprocess
import sys

import ktbook
import ktenglish as E
import ktretellcheck as R

BRACKET = re.compile(r"\[([^\]]+)\]")
# A proper name in the gloss: capitalised, not a sign-category in angle
# brackets, not the all-caps marks the renderer uses.
NAME = re.compile(r"\b([A-Z][a-z]{2,}(?:_[A-Za-z]+)*)\b")
SKIP_NAME = {"Lord", "God", "Sun", "Saturday", "Sunday", "Monday", "Friday",
             "Wednesday", "Tuesday", "Thursday", "Master", "Easter"}


def classify(lines):
    """stem -> the strongest class the gloss supplies it in."""
    out = {}

    def put(s, cls, rank):
        if s not in out or rank > out[s][1]:
            out[s] = (cls, rank)

    for l in lines:
        body = re.sub(r"^\s*\d+\s+", "", l)
        for tok in body.split():
            br = bool(BRACKET.search(tok))
            bare = BRACKET.sub(r"\1", tok)
            var = "~" in bare
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


def parts(txt):
    for m in re.finditer(r"^## ([^\n]+)\n\n### folios (\d{3}[rv])–(\d{3}[rv])\n"
                         r"(.*?)(?=^## |\Z)", txt, re.M | re.S):
        yield m.groups()


def section_one():
    print("=" * 74)
    print("1. WHAT BROKE")
    print("=" * 74)
    r = subprocess.run([sys.executable, "ktretellcheck.py"],
                       capture_output=True, text=True)
    fails = [l for l in r.stdout.splitlines() if "FAIL" in l]
    if r.returncode == 0:
        print("   nothing. The retelling gate passes at its bar of zero.")
    else:
        for l in fails:
            print("  ", l.strip())
        print("\n   Each is a one-line fix: requote what the gloss now says,")
        print("   or drop the guillemets and let the sentence be editorial.")
    return r.returncode


def section_two(txt, fol, want_list):
    print()
    print("=" * 74)
    print("2. WHAT IS EXPOSED")
    print("=" * 74)
    tot = collections.Counter()
    rows = []
    for name, _, _, body in parts(txt):
        cited = sorted(set(R.FOL.findall(body)))
        lines = [l for p in cited if p in fol for l in fol[p]]
        cls = classify(lines)
        n = exp = 0
        for q in R.QUOTE.findall(body):
            n += 1
            stems = [w for w in sorted(E.stems(q)) if w not in R.STOP]
            for w in stems:
                tot[cls.get(w, "MISSING")] += 1
            only = [w for w in stems if cls.get(w) == "BRACKET"]
            if only:
                exp += 1
                rows.append((name.split(".")[0], q, only))
        tot["quotations"] += n
        tot["exposed"] += exp
        print(f"   {name.split('.')[0]:<5} {n:4d} quotations   {exp:3d} exposed"
              f"  {100.0*exp/n if n else 0:5.1f}%")
    q, x = tot["quotations"], tot["exposed"]
    pct = 100.0 * x / q if q else 0.0
    print(f"\n   {'TOTAL':<5} {q:4d} quotations   {x:3d} exposed  {pct:5.1f}%")
    print("\n   content words quoted, by where the gloss supplies them:")
    body = sum(tot[k] for k in ("KT", "VAR", "CUT", "BRACKET", "MISSING"))
    for k in ("KT", "VAR", "CUT", "BRACKET", "MISSING"):
        print(f"     {k:<8} {tot[k]:5d}  "
              f"{100.0*tot[k]/body if body else 0:5.1f}%")
    print("\n   " + ("PATCH: the gate names every break and each is a "
                     "one-line fix" if pct < 20 else
                     "REWRITE: the prose is resting on the guesses"
                     if pct > 50 else
                     "MIXED: patch the quotations, re-argue the paragraphs "
                     "that rest on a name or a number"))
    if want_list:
        print("\n   exposed quotations:")
        for part, quote, stems in rows:
            print(f"     {part:<5} «{quote[:56]}»")
            print(f"           only from a bracket: {' '.join(stems)}")


def section_three(txt, fol):
    print()
    print("=" * 74)
    print("3. WHAT IS LOAD-BEARING  (the gate does not check these)")
    print("=" * 74)
    # ONLY brackets count here, and the first version of this was wrong to
    # count CUT as well. A hyphen in the rendering marks two different
    # things: a ktname/ktsegment cut, which is ours, and an ordinary affix
    # like the "holy" prefix, which is Kiraly & Tokai's. The two are not
    # distinguishable from the hyphen alone, so counting CUT flagged Adam,
    # John, Luke, Mary and Matthew as fragile when every one of them is a
    # plain dictionary name carrying a prefix. Seventeen names became five.
    # A check that cries wolf on twelve safe names costs a person more time
    # than it saves them.
    flagged = collections.defaultdict(set)
    for name, _, _, body in parts(txt):
        cited = sorted(set(R.FOL.findall(body)))
        prose = R.QUOTE.sub(" ", body)          # editorial sentences only
        for p in cited:
            if p not in fol:
                continue
            cls = classify(fol[p])
            for l in fol[p]:
                for nm in NAME.findall(l):
                    head = nm.split("_")[0]
                    if head in SKIP_NAME or len(head) < 3:
                        continue
                    if not re.search(r"\b" + re.escape(head) + r"\b", prose):
                        continue
                    st = E.stems(head)
                    if not st:          # the stemmer folds it to nothing
                        continue
                    worst = min((cls.get(s, "KT") for s in st),
                                key=lambda c: ["BRACKET", "CUT", "VAR",
                                               "KT"].index(c))
                    if worst == "BRACKET":
                        flagged[head].add(p)
    if not flagged:
        print("   every proper name the prose leans on is Kiraly & Tokai's "
              "own.\n   Nothing here needs a person.")
    else:
        print("   these names reach the prose only through a BRACKET -- a")
        print("   restoration of ours, never counted as a reading. Change one")
        print("   and the paragraph around it claims something else:\n")
        for nm in sorted(flagged):
            print(f"     {nm:<22} {' '.join(sorted(flagged[nm])[:8])}")
        print(f"\n   {len(flagged)} names to read by hand. Every other name the "
              "prose leans on\n   is a plain dictionary word of Kiraly and "
              "Tokai's and is safe.")


def section_four(txt, fol):
    print()
    print("=" * 74)
    print("4. WHAT IS LEFT")
    print("=" * 74)
    order = [p for p, _, _, _ in ktbook.folios()]
    idx = {p: i for i, p in enumerate(order)}
    bounds = sorted((idx[p], n) for p, n, _ in ktbook.PARTS)
    written = {n: (lo, hi, b) for n, lo, hi, b in parts(txt)}
    todo = drawn = total = 0
    for k, (i, pname) in enumerate(bounds):
        end = bounds[k + 1][0] if k + 1 < len(bounds) else len(order)
        span = order[i:end]
        total += len(span)
        got = written.get(pname)
        if not got:
            todo += len(span)
            print(f"   {pname.split('.')[0]:<5} NOT WRITTEN          "
                  f"{span[0]}–{span[-1]}  {len(span):3d} folios")
            continue
        cited = set(R.FOL.findall(got[2]))
        miss = [p for p in span if p not in cited]
        drawn += len(span) - len(miss)
        todo += len(miss)
        runs, cur = [], []
        for p in span:
            if p in miss:
                cur.append(p)
            elif cur:
                runs.append(cur)
                cur = []
        if cur:
            runs.append(cur)
        big = [r for r in runs if len(r) >= 6]
        tag = "written" if not big else "written, with gaps"
        print(f"   {pname.split('.')[0]:<5} {tag:<20} {span[0]}–{span[-1]}  "
              f"{len(span):3d} folios, {len(miss):3d} not drawn on")
        for r in big[:6]:
            print(f"         gap {r[0]}–{r[-1]}  {len(r)} folios")
    print(f"\n   Book One draws on {drawn} of {total} folios; "
          f"{todo} are not yet in the front of the book.")


def main(argv):
    txt = open(R.RT, encoding="utf-8").read()
    fol = {pg: ln for pg, _, _, ln in ktbook.folios()}
    if "--left" in argv:
        section_four(txt, fol)
        return 0
    rc = section_one()
    section_two(txt, fol, "--list" in argv)
    section_three(txt, fol)
    section_four(txt, fol)
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
