"""Kiraly & Tokai's dictionary, and whether it covers the text it decodes.

Their decipherment has been announced since 2018 and the full translation has
never appeared. Kiraly's 2022 paper says why: the grammar paper is held up
because "decipherment" in this case means the dictionary and the whole text,
and the dictionary is too typographically awkward to print. So they put it on
rechnitzer-kodex.hu instead, in his words "so that our claims about the text
are verifiable this way".

This verifies them. Not by reading the codex -- that needs the grammar, which
is the unpublished part, and Kiraly says plainly that with the dictionary alone
the text is still very hard to read. It asks the question that comes before
reading: how much of the book does the dictionary actually reach, and does it
reach the parts it was not built from?

That second question is the real one. A dictionary assembled by working out
what codes mean from context will always fit the passages it was assembled on.
Each entry cites the folios that justify it. Those citations mark the training
set, and every other page is held out -- the same split this project uses
everywhere else, here handed to us by the authors' own apparatus.

Entries are styled fragments: `lemma` carries a gloss, `rohonc` carries codes,
`meta` carries grammatical labels, and plain fragments carry folio references.

    python ktdict.py
"""
import json
import os
import re
from collections import Counter, defaultdict

import corpus

DICT = os.path.join(corpus.DATA, "rohonc", "kt", "dict_en.json")
FOLIO = re.compile(r"(\d{3}[rv])(\d{2})?")


def load():
    """[(code, {glosses}, {folios cited})]"""
    raw = json.load(open(DICT, encoding="utf-8"))
    # 65 codes carry more than one entry -- homographs, marked (1), (2) in the
    # printed form. Keying by code alone silently kept the last and produced a
    # nonsense result: the book's commonest word, 1601 occurrences, came out as
    # "eleven" when its first entry glosses it "and". Entries sharing a code
    # are merged.
    merged = {}
    for e in raw:
        merged.setdefault(e["code"], []).extend(e["entry"])
    raw = [{"code": c, "entry": v} for c, v in merged.items()]
    out = []
    for e in raw:
        glosses, folios, last = set(), set(), None
        for frag in e["entry"]:
            t = frag.get("text", "")
            st = frag.get("style")
            if st == "lemma":
                g = t.strip()
                if g:
                    glosses.add(g)
            elif st is None:
                for m in FOLIO.finditer(t):
                    folios.add(m.group(1))
                    last = m.group(1)
                # bare continuation numbers: "044v01, 10, 049v03"
                if last:
                    for m in re.finditer(r"(?<![0-9rv])(\d{2})(?![0-9rv])", t):
                        folios.add(last)
        out.append((e["code"], glosses, folios))
    return out


def main():
    import rohonc_kt as KT
    d = load()
    codes = {c for c, _, _ in d}
    withgloss = {c for c, g, _ in d if g}
    cited = set()
    for _, _, f in d:
        cited |= f
    print("=" * 78)
    print("KIRALY & TOKAI'S DICTIONARY, AGAINST THE TEXT IT DECODES")
    print("=" * 78)
    print(f"entries {len(d)}, of which {len(withgloss)} carry a gloss")
    print(f"distinct folios cited as evidence: {len(cited)}")

    doc = KT.load()
    toks = [t for p in doc for t in p.tokens]
    types = Counter(toks)
    print(f"\ntext: {len(toks)} word tokens, {len(types)} types, "
          f"{len(doc)} pages")

    cov_types = sum(1 for t in types if t in codes)
    cov_toks = sum(c for t, c in types.items() if t in codes)
    print(f"\nCOVERAGE")
    print(f"  types covered  {cov_types:6d} / {len(types):6d}  "
          f"{cov_types/len(types)*100:5.1f}%")
    print(f"  tokens covered {cov_toks:6d} / {len(toks):6d}  "
          f"{cov_toks/len(toks)*100:5.1f}%")

    # what the uncovered tokens look like
    unc = [(t, c) for t, c in types.most_common() if t not in codes]
    print(f"  commonest uncovered types: {[c for _, c in unc[:10]]}")
    print(f"  uncovered types occurring once: "
          f"{sum(1 for t, c in unc if c == 1)} of {len(unc)}")

    # held out: pages the dictionary never cites
    print(f"\nHELD OUT: pages the dictionary cites as evidence, against the rest")
    tr_t = tr_c = te_t = te_c = 0
    tr_p = te_p = 0
    for p in doc:
        name = p.page
        on_train = name in cited
        tr_p += on_train
        te_p += not on_train
        for t in p.tokens:
            hit = t in codes
            if on_train:
                tr_t += 1
                tr_c += hit
            else:
                te_t += 1
                te_c += hit
    print(f"  cited pages     {tr_p:4d}   tokens {tr_t:6d}   covered "
          f"{tr_c/max(1,tr_t)*100:5.1f}%")
    print(f"  uncited pages   {te_p:4d}   tokens {te_t:6d}   covered "
          f"{te_c/max(1,te_t)*100:5.1f}%")
    if te_t and tr_t:
        print(f"  drop from cited to uncited: "
              f"{(tr_c/tr_t - te_c/te_t)*100:.1f} points")

    print("\nPRIORITY: the undefined codes that would buy most coverage")
    und = [(c, t) for t, c in types.most_common() if t not in codes]
    base = cov_toks
    print(f"  six commonest undefined codes are {sum(c for c,_ in und[:6])/len(toks)*100:.1f}% of the text")
    for k in (50, 100, 200, 500):
        r = base + sum(c for c, _ in und[:k])
        print(f"  defining the top {k:3d} undefined codes -> {r/len(toks)*100:.1f}% coverage")

    print("\n  A dictionary built by reading context will fit the passages it")
    print("  was built on. The question is whether it reaches the others.")


if __name__ == "__main__":
    main()
