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
    p = os.path.join(WORK, name)
    return open(p, encoding="utf-8").read() if os.path.exists(p) else ""


def check(desc, ok, detail=""):
    print(f"  {'ok  ' if ok else 'FAIL'}  {desc:58s} {detail}")
    if not ok:
        FAILS.append(desc)


def nums(text, label, count, after=None):
    """The first `count` numbers on the line starting with `label`."""
    if after:
        i = text.find(after)
        text = text[i:] if i >= 0 else ""
    for ln in text.splitlines():
        if ln.strip().startswith(label):
            v = re.findall(r"-?\d+\.\d+|-?\d+", ln[ln.find(label) + len(label):])
            return [float(x) for x in v[:count]]
    return []


def close(a, b, tol=0.06):
    return abs(a - b) <= tol


def main():
    doc = open(DOC, encoding="utf-8").read().replace("−", "-")
    flat = " ".join(doc.split())
    print("figures quoted in ROHONC.md:\n")

    # ---- corpora ----
    st = out("corpus_stats.txt")
    m = re.search(r"(\d+) pages, (\d+) lines, (\d+) readable tokens, (\d+) types", st)
    check("2014 corpus line parses", bool(m))
    if m:
        for want, got in (("214", m.group(1)), ("4,250", f"{int(m.group(2)):,}"),
                          ("60,407", f"{int(m.group(3)):,}"), ("987", m.group(4))):
            check(f"2014 corpus {want}", want == got and want in flat, got)
    kt = out("kt_stats.txt")
    m = re.search(r"(\d+) pages, (\d+) lines, (\d+) words, (\d+) types, (\d+) glyphs", kt)
    check("K&T corpus line parses", bool(m))
    if m:
        for want, got in (("441", m.group(1)), ("4,372", f"{int(m.group(2)):,}"),
                          ("29,997", f"{int(m.group(3)):,}"), ("5,010", f"{int(m.group(4)):,}"),
                          ("72,862", f"{int(m.group(5)):,}")):
            check(f"K&T corpus {want}", want == got and want in flat, got)
        g = nums(kt, "TTR", 2)
        check("K&T 2.43 glyphs per word", len(g) == 2 and close(g[1], 2.43, 0.006) and "2.43" in flat, str(g))

    # ---- orientation ----
    o = out("orientation.txt")
    g4 = o.split("-gram inventory")[-1]
    a4 = nums(g4, "stored order (as-is)", 4)
    b4 = nums(g4, "reversed (visual->reading)", 4)
    check("orientation stored 36.39 / 19.87 / 36.2", len(a4) == 4 and close(a4[0], 36.39, .01)
          and close(a4[1], 19.87, .01) and close(a4[3], 36.2) and "36.39%" in flat and "36.2" in flat)
    check("orientation reversed 19.68 / 20.15 / -0.9", len(b4) == 4 and close(b4[0], 19.68, .01)
          and close(b4[1], 20.15, .01) and close(b4[3], -0.9) and "19.68%" in flat and "-0.9" in flat)
    check("delimiter 252 of 269; damage 126 to 77", "252 of its 269" in flat and "126 to 77" in flat)

    # ---- crossline ---- columns: straddling chance sd sigma lift headroom n
    cl = out("crossline.txt")
    two = cl.split("--- 4-gram")[0]
    six = cl.split("--- 6-gram")[1] if "--- 6-gram" in cl else ""
    rows2 = {
        "Rohonc K&T (words)": (37.14, 18.23, 39.3, 2.04, 23.1),
        "Rohonc 2014 (glyphs)": (84.37, 76.70, 15.5, 1.10, 32.9),
        "Voynich EVA (words)": (6.46, 5.85, 2.1, 1.10, 0.6),
        "Voynich v101 (words)": (6.38, 5.73, 2.3, 1.11, 0.7),
        "Italian prose (words)": (25.24, 9.64, 23.0, 2.62, 17.3),
        "Latin prose (words)": (12.41, 5.68, 16.4, 2.18, 7.1),
        "Hebrew prose (words)": (21.43, 6.79, 23.8, 3.16, 15.7),
        "five-component model": (12.01, 8.23, 6.0, 1.46, 4.1),
        "self-citation (Timm)": (14.16, 13.69, 0.9, 1.03, 0.5),
        "line-reset scribe": (8.54, 8.50, 0.1, 1.00, 0.0),
    }
    for lab, w in rows2.items():
        g = nums(two, lab, 7)
        ok = len(g) >= 6 and all(close(g[c], w[i]) for i, c in enumerate((0, 1, 3, 4, 5)))
        check(f"2-gram {lab}", ok and f"{w[0]:.2f}%" in flat and f"{w[4]:.1f}%" in flat, str(g[:6]))
    for lab, w in (("Rohonc K&T (words)", (2.06, 0.24, 37.3, 8.69)),
                   ("Rohonc 2014 (glyphs)", (15.81, 4.88, 30.2, 3.24)),
                   ("Hebrew prose (words)", (0.56, 0.09, 6.0, 6.14)),
                   ("Latin prose (words)", (0.27, 0.06, 2.6, 4.29)),
                   ("Italian prose (words)", (0.13, 0.04, 2.1, 3.58))):
        g = nums(six, lab, 7)
        ok = len(g) >= 5 and all(close(g[c], w[i]) for i, c in enumerate((0, 1, 3, 4)))
        check(f"6-gram {lab}", ok and f"{w[0]:.2f}%" in flat, str(g[:5]))
    for lab in ("Voynich EVA (words)", "Voynich v101 (words)", "five-component model",
                "self-citation (Timm)", "line-reset scribe"):
        g = nums(six, lab, 2)
        check(f"6-gram {lab} is zero", bool(g) and g[0] == 0.0, str(g[:2]))

    # ---- repeats ----
    rp = out("repeats.txt")
    cov = rp.split("THE ROHONC AT FULL LENGTH")[0]
    for lab, w in (("Rohonc K&T (words)", [37.3, 15.8, 7.5, 3.3, 1.2, 0.4, 0.0]),
                   ("Rohonc 2014 (glyphs)", [85.1, 57.7, 23.7, 10.0, 3.4, 0.8, 0.0]),
                   ("Voynich (words)", [2.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]),
                   ("italian prose (words)", [17.0, 0.7, 0.1, 0.1, 0.0, 0.0, 0.0]),
                   ("latin prose (words)", [7.7, 1.3, 0.9, 0.6, 0.6, 0.6, 0.0]),
                   ("hebrew prose (words)", [33.9, 4.6, 0.8, 0.2, 0.2, 0.0, 0.0])):
        g = nums(cov, lab, 7)
        check(f"coverage {lab}", len(g) == 7 and all(close(g[i], w[i]) for i in range(7))
              and f"{w[1]}" in flat, str(g))
    sh = [l for l in cov.splitlines() if l.strip().startswith("(shuffled)")]
    g = [float(x) for x in re.findall(r"-?\d+\.\d+", sh[0])] if sh else []
    check("K&T shuffled k=3 is 3.6", bool(g) and close(g[0], 3.6) and "3.6" in flat, str(g[:2]))
    for lab, want in (("Rohonc K&T (words)", 36), ("Rohonc 2014 (glyphs)", 44),
                      ("Voynich (words)", 4), ("italian prose", 14),
                      ("latin prose", 31), ("hebrew prose", 27)):
        g = nums(rp, lab, 1, after="longest sequence occurring")
        check(f"longest repeat {lab} = {want}", bool(g) and g[0] == want and f"| {want} |" in flat, str(g))
    check("five lines, discrepancy withdrawn", "about five lines" in flat and "discrepancy is withdrawn" in flat)

    # ---- dictionary ----
    kd = out("ktdict.txt")
    g = nums(kd, "entries", 2)
    check("dictionary 885 entries, 841 glossed", len(g) == 2 and g[0] == 885 and g[1] == 841
          and "885 codes" in flat and "841 with a gloss" in flat, str(g))
    g = nums(kd, "types covered", 3)
    check("types covered 797/5010 15.9%", len(g) == 3 and g[0] == 797 and close(g[2], 15.9) and "15.9%" in flat, str(g))
    g = nums(kd, "tokens covered", 3)
    check("tokens covered 18639/29997 62.1%", len(g) == 3 and g[0] == 18639 and close(g[2], 62.1) and "62.1%" in flat, str(g))
    g = nums(kd, "cited pages", 4)
    check("held-out split failed: 440 cited pages", bool(g) and g[0] == 440 and "440 of 441" in flat, str(g))
    g = nums(kd, "six commonest undefined", 1)
    check("six undefined codes = 4.7%", bool(g) and close(g[0], 4.7) and "4.7% of the entire text" in flat, str(g))
    for k, want in ((50, 73.1), (100, 76.0), (200, 79.1), (500, 84.1)):
        g = nums(kd, f"defining the top {k:3d}", 1)
        check(f"priority top {k} -> {want}%", len(g) == 1 and close(g[0], want) and f"{want}%" in flat, str(g))

    # ---- gospel-specificity ----
    kv = out("ktvalidate.txt")
    for k, (a, b, r) in ((25, (68.0, 88.0, 0.77)), (50, (72.0, 78.0, 0.92)), (100, (71.0, 61.0, 1.16)),
                         (200, (68.0, 50.5, 1.35)), (400, (62.5, 38.8, 1.61))):
        g = nums(kv, f"{k:20d}", 3) or nums(kv, str(k), 3, after="top k of reference")
        ok = len(g) == 3 and close(g[0], a) and close(g[1], b) and close(g[2], r, .01)
        check(f"gospel-specificity top {k}: {a}/{b}/{r}", ok and f"{r:.2f}x" in flat, str(g))

    # ---- localisation ----
    kl = out("ktlocalise.txt")
    g = nums(kl, "codes glossed as a proper name", 1)
    check("101 name codes", bool(g) and g[0] == 101 and "101 codes" in flat, str(g))
    g = nums(kl, "distinct names", 2)
    check("78 names in gospel", len(g) == 2 and g[1] == 78 and "78 of which" in flat, str(g))
    g = nums(kl, "pages carrying two or more", 2)
    check("247 of 441 pages", len(g) == 2 and g[0] == 247 and "247 pages" in flat, str(g))
    g = nums(kl, "real pages    median", 1)
    check("median 60 words", bool(g) and g[0] == 60 and "60 words apart" in flat, str(g))
    g = nums(kl, "random names  median", 1)
    check("random median 3007", bool(g) and g[0] == 3007 and "3,007" in flat, str(g))
    g = nums(kl, "real pages tighter", 3)
    check("214/247 = 87%", len(g) == 3 and g[0] == 214 and g[2] == 87 and "214 of 247 pages, 87%" in flat, str(g))

    # ---- extension gates ----
    ke = out("ktextend_gates.txt")
    g = nums(ke, "real pages     median", 1)
    h = nums(ke, "random bags    median", 1)
    check("gate 1: 23.68 vs 27.07", bool(g) and bool(h) and close(g[0], 23.68, .01) and close(h[0], 27.07, .01)
          and "23.68" in flat and "27.07" in flat, f"{g} {h}")
    g = nums(ke, "real pages above", 4)          # 95th, count, total, pct
    check("gate 1: 3% above 95th", len(g) == 4 and g[3] == 3 and "3% of real pages" in flat, str(g))
    for lab, want in (("true gloss ranked #1", 5), ("true gloss in top 5", 12), ("true gloss in top 20", 21)):
        g = nums(ke, lab, 2, after="GATE 2")
        check(f"gate 2: {lab} {want}%", len(g) == 2 and g[1] == want, str(g))
    check("gate 2 percentages quoted", "5% of the time, in the top five 12%, top twenty 21%" in flat)
    ka = out("ktalign_gate.txt")
    g = nums(ka, "tested", 1)
    check("gate 3: 13 tested", bool(g) and g[0] == 13 and "13 codes testable" in flat, str(g))
    for lab, want in (("true gloss ranked #1", 8), ("true gloss in top 5", 15), ("true gloss in top 20", 23)):
        g = nums(ka, lab, 2)
        check(f"gate 3: {lab} {want}%", len(g) == 2 and g[1] == want and f"{want}%" in flat, str(g))
    check("gate 3 FAIL at 30% bar", "FAIL" in ka and "Bar set at 30%" in flat)

    # ---- OCR ----
    oc = out("ocr_crossline.txt")
    i = oc.find("ratio 0.18"); j = oc.find("ratio 0.25")
    b18 = oc[i:j] if i >= 0 and j > i else ""
    g = nums(b18, "0.40", 5)
    check("OCR loosest: 0.61 / 0.39 / 4.7 sigma / 0.2%", len(g) == 5 and close(g[0], .61, .01)
          and close(g[1], .39, .01) and close(g[3], 4.7) and close(g[4], 0.2)
          and "0.61%" in flat and "0.39%" in flat and "4.7 sigma" in flat, str(g))
    g = nums(b18, "0.15", 2)
    check("OCR radius 0.15: nothing matches", len(g) == 2 and g[0] == 0.0 and g[1] == 0.0
          and "Below a radius of 0.20 nothing matches" in flat, str(g))
    m = re.search(r"ratio 0.18: (\d+) tokens", oc)
    check("OCR 22,225 tokens at 0.18 (in saved run)", bool(m) and m.group(1) == "22225", m.group(1) if m else "")
    check("OCR 14,301 blank runs; 0.998 TTR quoted", "14,301 blank" in flat and "0.998" in flat)
    check("OCR lines/page 10.0 vs 11.2", "10.0 lines" in flat and "11.2" in flat)

    # ---- prose claims ----
    check("unit correction stated", "unit error" in flat and "2.43 glyphs" in flat)
    check("failed orientation attempt kept", "failed and was discarded" in flat
          and os.path.exists(os.path.join(corpus.ROOT, "harness", "roho_orient.py")))
    check("missing liturgical control admitted", "still missing" in flat and "books of hours" in flat)
    # ---- mutual information ----
    lb = out("linebreak.txt")
    for lab, w in (("Rohonc K&T (words)", (0.6897, 0.3003, 0.3510, 41.2, 116.9)),
                   ("Rohonc 2014 (glyphs)", (1.4213, 1.0613, 0.2375, 17.5, 22.4)),
                   ("Voynich EVA (words)", (0.1706, 0.0435, 0.0082, 1.5, 18.9)),
                   ("Italian prose (words)", (0.3549, 0.1028, 0.0603, 10.8, 58.7)),
                   ("Latin prose (words)", (0.1403, 0.0281, 0.0108, 2.6, 38.4)),
                   ("five-component model", (0.0881, 0.0125, 0.0029, 0.5, 22.8)),
                   ("self-citation (Timm)", (0.1765, 0.0656, 0.0237, 2.3, 36.2))):
        g = nums(lb, lab, 7)
        ok = (len(g) == 7 and all(close(g[i], w[i], .0002) for i in range(3))
              and close(g[4], w[3]) and close(g[5], w[4]))
        check(f"MI row {lab}", ok and f"{w[0]:.4f}" in flat and f"{w[4]:.1f}%" in flat, str(g))
    check("MI disagreement dissolved", "no disagreement" in flat and "above 100%" in flat)

    print(f"\n{'ALL FIGURES CHECK OUT' if not FAILS else 'MISMATCHED (' + str(len(FAILS)) + '): ' + '; '.join(FAILS)}")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
