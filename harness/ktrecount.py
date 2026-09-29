"""Every reading's occurrence count, recomputed from the live transcription.

The gate, declared before the first run (2026-09-29): every entry in
proposals.json whose `n` is set must equal the number of whole tokens that
ARE that sign in the transcription; an entry with `n` unset fails. An entry
that occurs zero times as a whole token is allowed only if it stands inside
at least one longer token (its `inside` count), because such a sign is read
through composition and its evidence says so. Exit 1 on any failure, so
ktcommit.sh stops.

Why. Tier A means "survives every occurrence", and `n` is the number of
occurrences a reader checks that claim against. On 2026-09-29 an audit found
60 entries whose `n` no longer matched the transcription (glyph merges and
the variant rereads of 2026-09-25 moved tokens without anybody recounting),
nine of them with no whole-token occurrence at all, one of those tier A.
The counts were hand-typed at entry and nothing regenerated them. This does.

    python3 ktrecount.py            # report, exit 1 on any mismatch
    python3 ktrecount.py --write    # set n to the live whole count, keep the
                                    # old value in n_was, set inside; then report
"""
import json
import os
import sys
from collections import Counter, OrderedDict

import ktcoverage as C

HERE = os.path.dirname(os.path.abspath(__file__))
PROPOSALS = os.path.join(HERE, "proposals.json")


def unhx(h):
    return "".join(chr(0xE000 + int(h[i:i + 3], 16)) for i in range(0, len(h), 3))


def flat(x):
    out = []
    for y in x:
        out += flat(y) if isinstance(y, list) else [y]
    return out


def live_counts():
    gl, doc, seg = C.build()
    whole = Counter(t for p in doc for ln in p.lines for t in flat(ln))
    return whole


def main(argv):
    write = "--write" in argv
    raw = open(PROPOSALS, encoding="utf-8").read()
    p = json.loads(raw, object_pairs_hook=OrderedDict)
    whole = live_counts()
    types = list(whole)
    bad = []
    changed = 0
    for h, v in p.items():
        if h.startswith("_") or not isinstance(v, dict):
            continue
        c = unhx(h)
        n = whole.get(c, 0)
        inside = sum(k for t, k in whole.items() if t != c and c in t)
        if write:
            if v.get("n") != n:
                v["n_was"] = v.get("n")
                v["n"] = n
                changed += 1
            # `inside` is written only where it carries the claim: a sign
            # with no whole-token occurrence that lives inside longer ones.
            if n == 0:
                v["inside"] = inside
            else:
                v.pop("inside", None)
        if v.get("n") != n:
            bad.append((v.get("tier"), h, v.get("n"), n, inside, v.get("gloss")))
        elif n == 0 and inside == 0:
            bad.append((v.get("tier"), h, v.get("n"), n, inside, v.get("gloss") + "  NOWHERE"))
    if write:
        indent = 2 if raw.startswith('{\n  "') else 1
        json.dump(p, open(PROPOSALS, "w", encoding="utf-8"), ensure_ascii=False, indent=indent)
        if raw.endswith("\n"):
            open(PROPOSALS, "a", encoding="utf-8").write("\n")
        print(f"wrote n for {changed} entries")
    for b in bad:
        print("  MISMATCH", *b)
    total = sum(1 for h, v in p.items() if not h.startswith("_") and isinstance(v, dict))
    if bad:
        print(f"FAIL: {len(bad)} of {total} entries carry an n the transcription does not support")
        return 1
    print(f"PASS: {total} entries, every n equals its live whole-token count")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
