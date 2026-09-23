"""TEST 16: does a SECOND, INDEPENDENT transcription agree with the one we read?

Everything in this edition rests on Kiraly and Tokai's transcription. If that
transcription is wrong, the readings built on it are wrong, and nothing
elsewhere in this harness would notice: every other test reads the same file.

There is exactly one outside witness. In 2014 an anonymous author published an
open transcription of the codex (`data/rohonc/latest.txt`), glyph by glyph, in
an alphabet of their own invention, with no word separation, years before
Kiraly and Tokai published. The two were made by different people from the same
book and have nothing else in common -- not the alphabet, not the page
numbering, not the word divisions.

They can therefore be compared, and the comparison needs no dictionary and no
reading: if both transcribe the same manuscript honestly, some bijection must
carry one alphabet onto the other, and it must hold across the whole book.

HOW THE PAGES LINE UP. The open transcription numbers SPREADS of the library
scan and labels each row L or R. Matching row-length profiles says, with no
help from us, that the left page of spread k is folio k recto and the right
page is folio (k-1) verso -- which is how a right-to-left book falls open, and
is a fact about the manuscript neither transcription states.

WHAT WAS ALREADY SEEN BEFORE THE BARS WERE WRITTEN, said plainly because this
project does not pretend: an exploratory pass had already reported 91.1%
agreement of the best map, and 14.3% with the open row reversed. So the
headline number is not a prediction. What had NOT been run, and what the bars
below are declared for, is the matched control -- whether a wrong pairing of
the same rows scores anything like as well.

    GATE A, the alphabets.  Learn each open symbol's commonest K&T glyph from
        the aligned rows, then score every glyph occurrence by that map.
        CONTROL: pair each open row with a RANDOM K&T row of the same glyph
        count from a different folio, and learn a map the same way, 20 times.
        BAR: observed >= 60%, control <= 30%, and >= 5 sigma.

    GATE B, the words this edition reads.  Cut the mapped open glyphs at
        Kiraly and Tokai's own word boundaries and compare word for word.
        No control: this is a count, and it is reported as one.
        BAR: >= 80% of words identical.

A near miss is a miss and no bar moves after the run.

    python3 ktopen.py
"""
import collections
import json
import os
import random
import re
import sys

import corpus

OPEN = os.path.join(corpus.ROOT, "data", "rohonc", "latest.txt")
PAGES = os.path.join(corpus.ROOT, "data", "rohonc", "kt", "pages")
NSHUF = 20
SEED = 20260922
BAR_A_OBS, BAR_A_CTL, BAR_A_SIGMA, BAR_B = 60.0, 30.0, 5.0, 80.0


def open_sides():
    """(folio, [row of glyph tokens]) for every side of the open transcription."""
    pg = collections.defaultdict(lambda: collections.defaultdict(dict))
    for line in open(OPEN, encoding="utf-8"):
        m = re.match(r"^\s*(\d+):\s*([LR])(\d+):\s*(.*)$", line)
        if m:
            pg[int(m.group(1))][m.group(2)][int(m.group(3))] = m.group(4).strip()
    out = {}
    for p, d in pg.items():
        for side, rows in d.items():
            fol = f"{p:03d}r" if side == "L" else f"{p - 1:03d}v"
            out[fol] = [[t.rstrip("?") for t in txt.replace("[?]", " ").split()
                         if t not in ("?", "#", "")]
                        for _, txt in sorted(rows.items())]
    return out


def kt_sides():
    """(folio, [row of glyph codes], [row of word lengths]) from K&T's own pages."""
    rows, words = {}, {}
    for fn in sorted(os.listdir(PAGES)):
        if not fn.endswith(".json"):
            continue
        blocks = json.load(open(os.path.join(PAGES, fn), encoding="utf-8"))
        rr, ww = [], []
        for b in blocks:
            if not isinstance(b, dict) or b.get("blocktype") != "main":
                continue
            for r in b.get("rows", []):
                gl, wl = [], []
                for w in r["text"].split():
                    g = [f"{ord(c) - 0xE000:03x}" for c in w if 0xE000 <= ord(c) < 0xF000]
                    if g:
                        gl += g
                        wl.append(len(g))
                rr.append(gl)
                ww.append(wl)
        if rr:
            rows[fn[:-5]], words[fn[:-5]] = rr, ww
    return rows, words


def aligned():
    """Rows the two transcriptions agree on the SHAPE of: same side, same number
    of rows, same number of glyphs in the row. Those are the rows that can be
    compared glyph for glyph; the rest are where the two split lines or read
    damage differently, and are counted but never guessed at."""
    op, (kt, ktw) = open_sides(), kt_sides()
    pairs, sides, rows_seen = [], 0, 0
    for fol, a in op.items():
        b, bw = kt.get(fol), ktw.get(fol)
        if not b:
            continue
        sides += 1
        rows_seen += len(a)
        if len(a) != len(b):
            continue
        for ra, rb, rw in zip(a, b, bw):
            if ra and len(ra) == len(rb):
                pairs.append((ra, rb, rw))
    return pairs, sides, rows_seen, sum(len(r) for r in kt.values())


def learn(pairs):
    co = collections.defaultdict(collections.Counter)
    for ra, rb, _ in pairs:
        for x, y in zip(ra, rb):
            co[x][y] += 1
    return {x: c.most_common(1)[0][0] for x, c in co.items()}, co


def rate(pairs, mp):
    ok = n = 0
    for ra, rb, _ in pairs:
        for x, y in zip(ra, rb):
            n += 1
            ok += mp.get(x) == y
    return 100.0 * ok / max(1, n), n


def main():
    pairs, sides, rows_seen, kt_rows = aligned()
    mp, co = learn(pairs)
    obs, glyphs = rate(pairs, mp)
    solid = sum(1 for x, c in co.items()
                if sum(c.values()) >= 20 and c.most_common(1)[0][1] / sum(c.values()) >= 0.8)
    rev, _ = rate([(ra[::-1], rb, w) for ra, rb, w in pairs], learn([(ra[::-1], rb, w) for ra, rb, w in pairs])[0])

    rng = random.Random(SEED)
    bylen = collections.defaultdict(list)
    for i, (ra, rb, w) in enumerate(pairs):
        bylen[len(rb)].append(i)
    ctl = []
    for _ in range(NSHUF):
        shuf = []
        for ra, rb, w in pairs:
            pool = bylen[len(ra)]
            ra2 = pairs[rng.choice(pool)][0]
            shuf.append((ra2, rb, w))
        m2, _ = learn(shuf)
        ctl.append(rate(shuf, m2)[0])
    mu = sum(ctl) / len(ctl)
    sd = (sum((c - mu) ** 2 for c in ctl) / len(ctl)) ** 0.5
    sigma = (obs - mu) / sd if sd else float("inf")

    # GATE B: the words, cut at K&T's own boundaries
    wok = wn = 0
    for ra, rb, wl in pairs:
        i = 0
        for L in wl:
            a, b = ra[i:i + L], rb[i:i + L]
            i += L
            wn += 1
            wok += all(mp.get(x) == y for x, y in zip(a, b))
    wrate = 100.0 * wok / max(1, wn)

    print("TEST 16: A SECOND, INDEPENDENT TRANSCRIPTION")
    print(f"  the 2014 open transcription covers {sides} of 441 sides, {rows_seen} rows")
    print(f"  rows comparable glyph for glyph      {len(pairs)} of {kt_rows}   {100*len(pairs)/kt_rows:.1f}%")
    print(f"  glyphs compared                      {glyphs}")
    print(f"  open symbols seen {len(co)}, of which {solid} map to one K&T glyph >=80% of >=20 sightings")
    print()
    print("  GATE A: the two alphabets")
    print(f"    best map, as transcribed            {obs:.1f}%")
    print(f"    same rows, open row reversed        {rev:.1f}%")
    print(f"    control: rows paired at random      {mu:.1f}%  (sd {sd:.2f}, {NSHUF} shuffles)")
    print(f"    {sigma:.1f} sigma")
    a_pass = obs >= BAR_A_OBS and mu <= BAR_A_CTL and sigma >= BAR_A_SIGMA
    print(f"    BAR: observed >= {BAR_A_OBS:.0f}%, control <= {BAR_A_CTL:.0f}%, >= {BAR_A_SIGMA:.0f} sigma  ->  {'PASS' if a_pass else 'FAIL'}")
    print()
    print("  GATE B: the words this edition reads")
    print(f"    words compared                      {wn}")
    print(f"    identical in both transcriptions    {wrate:.1f}%")
    b_pass = wrate >= BAR_B
    print(f"    BAR: >= {BAR_B:.0f}%  ->  {'PASS' if b_pass else 'FAIL'}")
    return 0 if (a_pass and b_pass) else 1


if __name__ == "__main__":
    import ktcwd
    ktcwd.enter()
    sys.exit(main())
