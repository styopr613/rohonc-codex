"""Verify every figure quoted in ROHONC.md against the saved run outputs.

Same discipline as check_results.py: the prose is hand-written and can drift,
so every number in it is checked against the file the run actually produced.

    python check_rohonc.py
"""
import os
import re
import sys

import corpus

WORK = os.path.join(corpus.ROOT, "work", "rohonc")
DOC = os.path.join(corpus.ROOT, "ROHONC.md")
FAILS = []


def out(name):
    return open(os.path.join(WORK, name), encoding="utf-8").read()


def check(desc, ok, detail=""):
    print(f"  {'ok  ' if ok else 'FAIL'}  {desc:56s} {detail}")
    if not ok:
        FAILS.append(desc)


def nums(text, label, count):
    """The first `count` numbers on the line starting with `label`."""
    for ln in text.splitlines():
        if ln.strip().startswith(label):
            v = re.findall(r"-?\d+\.\d+|-?\d+", ln[len(label):])
            return [float(x) for x in v[:count]]
    return []


def main():
    doc = open(DOC, encoding="utf-8").read()
    # the write-up uses a typographic minus; normalise before matching
    doc = doc.replace("\u2212", "-")
    cl, lb, orient, stats = (out("crossline.txt"), out("linebreak.txt"),
                             out("orientation.txt"), out("corpus_stats.txt"))
    print("figures quoted in ROHONC.md:\n")

    # corpus
    m = re.search(r"(\d+) pages, (\d+) lines, (\d+) readable tokens, (\d+) types",
                  stats)
    check("corpus line parses", bool(m), stats.strip())
    if m:
        for want, got, lab in [("214", m.group(1), "pages"),
                               ("4,250", m.group(2).replace("4250", "4,250"), "lines"),
                               ("60,407", f"{int(m.group(3)):,}", "tokens"),
                               ("987", m.group(4), "types")]:
            check(f"corpus {lab} = {want}", want in doc and want == got, got)

    # orientation: the 4-gram decision table
    a = nums(orient, "stored order (as-is)", 4)
    b = nums(orient, "reversed (visual->reading)", 4)
    # last occurrence is the 4-gram block
    blocks = orient.split("-gram inventory")
    g4 = blocks[-1]
    a4, b4 = nums(g4, "stored order (as-is)", 4), nums(g4, "reversed (visual->reading)", 4)
    check("orientation stored 4-gram 36.39%", abs(a4[0] - 36.39) < 0.01 and "36.39%" in doc, str(a4[0]))
    check("orientation stored chance 19.87%", abs(a4[1] - 19.87) < 0.01 and "19.87%" in doc, str(a4[1]))
    check("orientation stored sigma 36.2", abs(a4[3] - 36.2) < 0.05 and "36.2" in doc, str(a4[3]))
    check("orientation reversed 19.68%", abs(b4[0] - 19.68) < 0.01 and "19.68%" in doc, str(b4[0]))
    check("orientation reversed chance 20.15%", abs(b4[1] - 20.15) < 0.01 and "20.15%" in doc, str(b4[1]))
    check("orientation reversed sigma -0.9", abs(b4[3] + 0.9) < 0.05 and "-0.9" in doc, str(b4[3]))

    # crossline 2-gram block
    two = cl.split("--- 4-gram")[0]
    rows2 = {
        "Rohonc Codex (glyphs)": (84.37, 76.65, 15.4, 1.10, 33.0),
        "Voynich EVA (words)": (6.46, 5.87, 2.0, 1.10, 0.6),
        "Voynich v101 (words)": (6.38, 5.84, 1.7, 1.09, 0.6),
        "Italian prose (words)": (25.24, 9.64, 26.1, 2.62, 17.3),
        "Latin prose (words)": (12.41, 5.71, 13.7, 2.17, 7.1),
        "Hebrew prose (words)": (21.43, 6.75, 23.8, 3.18, 15.7),
        "five-component model": (12.01, 8.37, 7.8, 1.43, 4.0),
        "self-citation (Timm)": (14.16, 13.79, 0.8, 1.03, 0.4),
        "line-reset scribe": (8.54, 8.65, -0.2, 0.99, -0.1),
    }
    # output columns are: straddling, chance, sd, sigma, lift, headroom, n
    COLS = (0, 1, 3, 4, 5)
    for lab, want in rows2.items():
        got = nums(two, lab, 7)
        ok = len(got) >= 6 and all(abs(got[c] - want[i]) < 0.06
                                   for i, c in enumerate(COLS))
        inp = f"{want[0]:.2f}%" in doc and f"{want[4]:.1f}%" in doc
        check(f"2-gram {lab}", bool(ok and inp), str(got[:6]))

    # crossline 6-gram block
    six = cl.split("--- 6-gram")[1]
    for lab, want in (("Rohonc Codex (glyphs)", (15.81, 4.99, 32.2, 3.17)),
                      ("Hebrew prose (words)", (0.56, 0.09, 9.3, 6.60)),
                      ("Latin prose (words)", (0.27, 0.06, 3.7, 4.83)),
                      ("Italian prose (words)", (0.13, 0.03, 2.9, 3.95))):
        got = nums(six, lab, 7)
        ok = len(got) >= 5 and all(abs(got[c] - want[i]) < 0.06
                                   for i, c in enumerate((0, 1, 3, 4)))
        check(f"6-gram {lab}", bool(ok and f"{want[0]:.2f}%" in doc), str(got[:5]))
    for lab in ("Voynich EVA (words)", "Voynich v101 (words)",
                "five-component model", "line-reset scribe"):
        got = nums(six, lab, 2)
        check(f"6-gram {lab} is zero", bool(got) and got[0] == 0.0, str(got[:2]))

    # linebreak MI table
    for lab, want in (("Rohonc (as stored)", (1.4222, 1.0495, 0.2391, 16.9, 22.8)),
                      ("Rohonc (line reversed)", (1.4211, 1.0472, 0.0346, 2.2, 3.3)),
                      ("Voynich EVA (words)", (0.1754, 0.0455, 0.0087, 1.9, 19.2)),
                      ("Italian prose (words)", (0.3538, 0.1137, 0.0659, 8.1, 57.9)),
                      ("Latin prose (words)", (0.1391, 0.0344, 0.0117, 2.1, 34.0)),
                      ("five-component model", (0.0877, 0.0167, 0.0040, 1.3, 24.0)),
                      ("self-citation (Timm)", (0.1755, 0.0675, 0.0252, 3.9, 37.4))):
        got = nums(lb, lab, 7)
        ok = (got and abs(got[0] - want[0]) < 0.0002 and abs(got[1] - want[1]) < 0.0002
              and abs(got[2] - want[2]) < 0.0002 and abs(got[4] - want[3]) < 0.05
              and abs(got[5] - want[4]) < 0.05)
        check(f"MI row {lab}", bool(ok), str(got))

    # claims in prose
    check("delimiter 252 of 269 quoted", "252 of its 269" in doc)
    check("damage marker 126 to 77 quoted", "126 to 77" in doc)
    check("6.5% unreadable quoted", "6.5%" in doc)
    check("failed first attempt is recorded", "failed and was discarded" in doc
          and os.path.exists(os.path.join(corpus.ROOT, "harness", "roho_orient.py")))
    check("archive URL present", "web.archive.org/web/20180421091607id_" in doc)

    print(f"\n{'ALL FIGURES CHECK OUT' if not FAILS else 'MISMATCHED: ' + ', '.join(FAILS)}")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
