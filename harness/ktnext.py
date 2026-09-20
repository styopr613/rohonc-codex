"""The next batch, in one command.

Prints the next six folios that are not yet translated, in the codex's page
order, each as far as it reads with every gap marked <<hex>>, then the gaps
on those folios with how often each occurs in the whole book, and the lines
that cite a source (an evangelist and a chapter). That is a batch for the
loop in METHOD.md: identify the passage, translate the page whole, fill the
gaps from the source, check every fill at every occurrence, enter, commit.

    python3 ktnext.py            # the next six untranslated folios
    python3 ktnext.py 8          # the next eight
    python3 ktnext.py 8 110r     # eight, starting at 110r

Works from the DONE set in ktcontext.py, so it is never stale, and from the
same inventory the renderer uses, so it never disagrees with the page.
"""
import sys
from collections import Counter

import ktaffix as A
import ktcontext as X
import ktgap as G
import kttranslate as T

EVANGELISTS = ("Matthew", "Mark", "Luke", "John", "Paul", "Peter", "James")


def main(argv):
    n = int(argv[0]) if argv else 6
    start = argv[1] if len(argv) > 1 else None
    gl, doc, seg, var, prop = G.build()
    # Render exactly as the page does: K&T's first-listed sense, not the
    # shortest one, so 'apostle' does not print as 'learn' or 'Jews' as 'they'.
    T.ORDER.update(T.ordered())
    T.prop_ref.update(prop)
    pages = [p for p in doc if p.page not in X.DONE]
    if start:
        idx = next((i for i, p in enumerate(pages) if p.page == start), 0)
        pages = pages[idx:]
    batch = pages[:n]
    freq = Counter(A.strip(t)[0] for p in doc for t in p.tokens)

    print(f"{len(X.DONE)} folios translated, {len(pages)} to go. "
          f"Next {len(batch)}: {' '.join(p.page for p in batch)}")
    gaps = Counter()
    cites = []
    for p in batch:
        print()
        print("=" * 78)
        print(f"FOLIO {p.page}")
        print("=" * 78)
        for i, ln in enumerate(p.lines, 1):
            toks = [t for run in ln for t in run]
            if not toks:
                continue
            cells = []
            for t in toks:
                if G.readable(t, gl, seg, var, prop):
                    cells.append(T.render_token(t, gl, seg, False, var, prop))
                else:
                    h = X.hx(A.strip(t)[0])
                    cells.append("<<" + h + ">>")
                    gaps[h] += 1
            line = " ".join(cells)
            print(f"{i:2d}  {line}")
            if "chapter" in line and any(e in line for e in EVANGELISTS):
                cites.append((p.page, i, line))

    print()
    print("=" * 78)
    print(f"GAPS on this batch: {len(gaps)} signs, {sum(gaps.values())} tokens")
    print("  (n = occurrences in the whole book; n=1 can only reach tier C or D)")
    print("=" * 78)
    rows = sorted(gaps.items(), key=lambda kv: -freq[X.unhx(kv[0])])
    for h, k in rows:
        print(f"  n={freq[X.unhx(h)]:<4d} here={k:<3d} {h}")

    print()
    print("=" * 78)
    print("SOURCE CITATIONS on this batch")
    print("=" * 78)
    if not cites:
        print("  none; use ktpage.py FOLIO \"phrase\" to find the passage")
    for page, i, line in cites:
        print(f"  {page}:{i:<3d} {line[:120]}")
    print()
    print("Next: ktpage.py FOLIO \"phrase\"   ktcontext.py HEX   then METHOD.md step 4")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
