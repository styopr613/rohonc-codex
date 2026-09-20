"""Every unread sign that Kiraly and Tokai's own entries already name.

Their dictionary is not just a list of headwords. Each entry carries variant
spellings, aggregates, negations, suffixed forms and worked examples, and each
of those is a glyph string they have already read. A sign of ours that appears
anywhere inside an entry body is therefore a sign THEY read and this project
did not, and reading it costs no guess at all: the gloss is theirs and usually
the folio and line are theirs too.

On 2026-09-20 this pass found 370 such signs covering 577 words and standing
as the only hole on 330 lines. They had been turning up one folio at a time
for two days before anyone thought to ask the question in bulk.

    python3 ktsupply.py [N]      # the N best still unread, with their entry
    python3 ktsupply.py --count  # just the totals
"""
import json
import sys
from collections import Counter

import ktaffix as A
import ktcross as K
import ktdict


def hx(s):
    return "".join(f"{ord(c)-0xE000:03x}" for c in s)


def kt_hx(s):
    return "".join(f"{ord(c)-0xE000:03x}" for c in s if 0xE000 <= ord(c) < 0xF000)


def entries():
    raw = json.load(open(ktdict.DICT, encoding="utf-8"))
    out = []
    for e in raw:
        body = "".join(
            (f"<{kt_hx(f.get('text',''))}>" if kt_hx(f.get("text", "")) else f.get("text", ""))
            for f in e["entry"])
        out.append((kt_hx(e["code"]), body))
    return out


def main(argv):
    gl, doc, seg, var, prop, inv = K.build()
    cnt = Counter(A.strip(t)[0] for p in doc for t in p.tokens)
    solo = Counter()
    for p in doc:
        for ln in p.lines:
            miss = {A.strip(t)[0] for t in [x for run in ln for x in run]
                    if A.strip(t)[0] not in inv}
            if len(miss) == 1:
                solo[next(iter(miss))] += 1
    ents = entries()
    rows = []
    for u, k in cnt.items():
        if u in inv:
            continue
        h = hx(u)
        hit = next((b for c, b in ents if f"<{h}>" in b), None)
        if hit:
            rows.append((solo[u], k, h, hit))
    rows.sort(key=lambda r: (-r[0], -r[1]))
    print(f"{len(rows)} unread signs are named inside K&T's own entries")
    print(f"  they cover {sum(r[1] for r in rows)} words "
          f"and are the only hole on {sum(r[0] for r in rows)} lines")
    if "--count" in argv:
        return 0
    n = next((int(a) for a in argv if a.isdigit()), 30)
    print()
    for solon, k, h, body in rows[:n]:
        print(f"{solon} ln n={k:<3d} {h:26s} {body[:230]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
