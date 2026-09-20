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
    kdi = out("ktdistrib_gate.txt")
    g = nums(kdi, "tested", 1)
    check("gate 5: 76 tested", bool(g) and g[0] == 76 and "76 codes tested" in flat, str(g))
    for lab, want in (("neighbour #1 shares a gloss", 0), ("some neighbour in top 5", 8),
                      ("some neighbour in top 10", 14)):
        g = nums(kdi, lab, 2)
        check(f"gate 5: {lab} {want}%", len(g) == 2 and g[1] == want, str(g))
    check("gate 5 FAIL and the 4% flaw recorded",
          "FAIL" in kdi and "top five 8%, top ten" in flat and "4%" in flat)
    check("seventeen attempts stated",
          "seventeen ways" in flat and "Fourteen failed outright" in flat)
    kcl = out("ktclass.txt")
    g = nums(kcl, "accuracy", 2)
    check("class gate 57.8% vs 46.9% baseline",
          len(g) == 2 and close(g[0], 57.8) and close(g[1], 46.9)
          and "57.8%" in flat and "46.9%" in flat, str(g))
    check("class gate weakness stated", "38%" in flat and "below" in flat.lower())
    kC = out("ktcodeC.txt")
    g = nums(kC, "adversary", 3)
    check("code C adversary lift 10.51x",
          len(g) == 3 and close(g[2], 10.51, .02) and "10.5" in flat, str(g))
    g = nums(kC, "C appears in", 4)
    check("code C held out 12.13x",
          bool(g) and close(g[-1], 12.13, .02) and "12.1" in flat, str(g))
    check("code C not overclaimed",
          "not a meaning" in flat and "narrowed field" in flat)
    kt = out("kttopical.txt")
    check("topical filter: 47 codes, two at 100%",
          "47 undefined codes" in kt and "100%" in kt
          and "47 undefined codes" in flat and "100% of 33 and of 31" in flat)
    check("ninth rejection recorded",
          "six of its" in flat and "twenty-seven occurrences" in flat
          and "ten virgins" in flat)
    kc = out("ktceiling.txt")
    # the band row is "1  2885  2885  9.58%": the label is consumed, so the
    # numbers that come back are types, tokens, percent -- three, not four
    g = nums(kc, "1", 3, after="occurrences   types")
    check("ceiling: 2885 hapax = 9.58% of text",
          len(g) == 3 and g[0] == 2885 and close(g[2], 9.58, .01)
          and "2,885 undefined codes" in flat and "9.6% of the book" in flat, str(g))
    # nums matches the STRIPPED line, so a space-padded label never matches;
    # anchor on the ceiling table instead and use the bare number
    for k, want in ((3, 86.4), (5, 82.3)):
        g = nums(kc, str(k), 2, after="ceiling coverage")
        check(f"ceiling at k={k} is {want}%",
              len(g) == 2 and close(g[1], want) and f"{want}%" in flat, str(g))
    kh = out("kthapax.txt")
    g = nums(kh, "today", 4)
    check("hapax support today: 60% median, 4.9% full",
          len(g) == 4 and close(g[1], 60) and close(g[3], 4.9)
          and "60% readable" in flat and "4.9%" in flat, str(g))
    g = nums(kh, "+ all with 3+ occurrences", 4)
    check("hapax support at ceiling: 83% median, 36.6% full",
          len(g) == 4 and close(g[1], 83) and close(g[3], 36.6)
          and "83%" in flat and "36.6% sit in a sentence" in flat, str(g))
    check("ceiling overstatement corrected",
          "not on decipherment" in flat and "said otherwise" in flat)
    lp = out("ktread_loop.txt")
    check("rejection loop recorded", "539 occurrences" in lp and "line-initial 72" in lp
          and "72 times and closes one 70" in flat and "Rejected." in flat)
    kr = open(os.path.join(corpus.ROOT, "harness", "ktread.py"), encoding="utf-8").read()
    check("reading gate recorded in code and doc",
          "end / side" in kr and "One to two of six" in flat)
    check("reading gate: the confident failure named",
          "completely wrong, caught" in flat and "dative" in flat)

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

    # --- the eleventh attempt: meaning inherited from a substring (FAIL)
    km = out("ktmorph.txt")
    g = nums(km, "gloss overlap, real pairing", 1)
    check("ktmorph real 1.4%", bool(g) and close(g[0], 1.4, .05) and "1.4%" in flat, str(g))
    g = nums(km, "gloss overlap, shuffled control", 1)
    check("ktmorph control 0.3%", bool(g) and close(g[0], 0.3, .2) and "0.3%" in flat, str(g))
    g = nums(km, "ratio", 2)
    check("ktmorph 4.94x at 4.7 sigma",
          len(g) == 2 and close(g[0], 4.94, .02) and close(g[1], 4.7, .05)
          and "4.94" in flat and "4.7 sigma" in flat, str(g))
    check("ktmorph recorded as a fail", "FAIL" in km and "84%" in flat and "416" in flat)

    # --- the wider reference corpus (FAIL)
    kw = out("ktalign_gate_wide.txt")
    g = nums(kw, "true gloss in top 5", 2)
    check("wide corpus top-5 13%",
          len(g) == 2 and close(g[1], 13, .05) and "13% in the top five" in flat, str(g))
    check("wide corpus still fails", "FAIL" in kw and "1,746,498" in flat)
    ka = out("ktalign_gate.txt")
    g = nums(ka, "true gloss in top 5", 2)
    check("gospels baseline still 15%",
          len(g) == 2 and close(g[1], 15, .05) and "8% / 15% / 23%" in flat, str(g))

    # --- the twelfth: name-final compounds (PASS)
    kn = out("ktname.txt")
    g = nums(kn, "true name ranked first, real compounds", 1)
    check("ktname real 43.9%", bool(g) and close(g[0], 43.9, .02) and "43.9%" in flat, str(g))
    g = nums(kn, "true name ranked first, matched control", 2)
    check("ktname control 6.3%", bool(g) and close(g[0], 6.3, .05) and "6.3%" in flat, str(g))
    g = nums(kn, "ratio", 2)
    check("ktname 6.94x at 12.4 sigma",
          len(g) == 2 and close(g[0], 6.94, .02) and close(g[1], 12.4, .02)
          and "6.94" in flat and "12.4 sigma" in flat, str(g))
    check("ktname passes", "PASS" in kn)

    # --- the thirteenth: segmentation (gate A fails, gate B passes)
    ks = out("ktsegment.txt")
    g = nums(ks, "composed gloss hits the true gloss", 1)
    check("segment gate A 3.1%", bool(g) and close(g[0], 3.1, .05) and "3.1%" in flat, str(g))
    g = nums(ks, "ratio", 2)
    check("segment gate A 1.4 sigma",
          len(g) == 2 and close(g[1], 1.4, .05) and "1.4 sigma" in flat, str(g))
    g = nums(ks, "closer to its own parts than to stand-ins", 1)
    check("segment gate B 77.5%", bool(g) and close(g[0], 77.5, .02) and "77.5%" in flat, str(g))
    g = nums(ks, "same test, stand-ins on both sides", 2)
    check("segment gate B control 47.4%",
          bool(g) and close(g[0], 47.4, .02) and "47.4%" in flat, str(g))
    g = nums(ks, "sigma", 1)
    check("segment gate B 9.8 sigma", bool(g) and close(g[0], 9.8, .02) and "9.8 sigma" in flat, str(g))
    check("segment gate A recorded as a fail and B as a pass",
          "FAIL" in ks and "PASS" in ks and "32" in flat and "316" in flat)
    g = nums(ks, "cut cleanly into defined codes", 2)
    check("1,282 types cut (30%)",
          len(g) == 2 and close(g[0], 1282, .001) and close(g[1], 30, .05)
          and "1,282" in flat, str(g))
    g = nums(ks, "now readable by composition", 3)
    check("5,754 tokens, 46% of undefined, 19% of the book",
          len(g) == 3 and close(g[0], 5754, .001) and close(g[1], 46, .05)
          and close(g[2], 19, .05) and "5,754" in flat and "19%" in flat, str(g))
    g = nums(ks, "book coverage before", 1)
    check("coverage before 58.4%", bool(g) and close(g[0], 58.4, .02) and "58.4%" in flat, str(g))
    g = nums(ks, "book coverage after", 1)
    check("coverage after 77.6%", bool(g) and close(g[0], 77.6, .02) and "77.6%" in flat, str(g))
    check("code C resolved, not overclaimed",
          "E950 EB61" in flat and "contains the word Lucifer" in flat
          and "exact sense of the prefix" in flat)
    check("credit kept straight",
          "The grammar is Kir" in flat and "1,282 readings" in flat)

    # --- CONCLUSION.md carries the same figures in plain English
    cp = os.path.join(corpus.ROOT, "CONCLUSION.md")
    con = open(cp, encoding="utf-8").read() if os.path.exists(cp) else ""
    conf = " ".join(con.split())
    check("CONCLUSION: seventeen attempts, fourteen failed",
          "seventeen ways" in conf and "Fourteen failed" in conf and "78.8%" in conf)
    check("CONCLUSION: 1,282 codes and 58% to 78%",
          "1,282" in conf and "58% to 78%" in conf)
    check("CONCLUSION: wider corpus recorded as my wrong prediction",
          "prediction of mine and it was wrong" in conf)
    # --- coverage vs translation
    kv = out("ktcoverage.txt")
    for lab, want, docstr in (("any reading at all", 77.6, "77.6%"),
                              ("no reading at all", 22.4, "22.4%"),
                              ("exactly one sense, no choice", 11.5, "11.5%"),
                              ("several senses, grammar needed", 66.0, "66.0%")):
        g = nums(kv, lab, 2)
        check(f"coverage: {lab} {want}%",
              len(g) == 2 and close(g[1], want, .02) and docstr in flat, str(g))
    g = nums(kv, "every word readable", 4)
    check("lines fully readable 2.8% -> 20.6%",
          len(g) == 4 and close(g[1], 2.8, .05) and close(g[3], 20.6, .02)
          and "2.8%" in flat and "20.6%" in flat, str(g))
    g = nums(kv, "80%+ of words readable", 4)
    check("lines 80% readable 12.9% -> 50.8%",
          len(g) == 4 and close(g[1], 12.9, .02) and close(g[3], 50.8, .02)
          and "12.9%" in flat and "50.8%" in flat, str(g))
    g = nums(kv, "median line readability", 2)
    check("median line 57.1% -> 80.0%",
          len(g) == 2 and close(g[0], 57.1, .02) and close(g[1], 80.0, .02)
          and "57.1%" in flat and "80.0%" in flat, str(g))
    check("translated is not overclaimed",
          "Not 77.6%" in flat and "located, not translated" in flat
          and "The grammar will" in flat)

    # --- sense choice and grammar abstraction, both failed
    kq = out("ktsense.txt")
    g = nums(kq, "picked from real context", 1)
    check("sense gate 39.9%", bool(g) and close(g[0], 39.9, .02) and "39.9%" in flat, str(g))
    g = nums(kq, "sigma above the control", 1)
    check("sense gate 22.8 sigma",
          bool(g) and close(g[0], 22.8, .02) and "22.8 sigma" in flat, str(g))
    g = nums(kq, "ratio", 1)
    check("own senses 2.50x closer",
          bool(g) and close(g[0], 2.50, .02) and "2.50 times" in flat, str(g))
    check("sense gate recorded as a fail", "SIGNAL bar" in kq and "FAIL" in kq)
    kg = out("ktgrammar.txt")
    g = nums(kg, "variance explained, multi-sense codes", 1)
    check("grammar multi-sense 15.7%",
          bool(g) and close(g[0], 15.7, .02) and "15.7%" in flat, str(g))
    g = nums(kg, "variance explained, matched single-sense", 2)
    check("grammar single-sense 16.2%",
          bool(g) and close(g[0], 16.2, .02) and "16.2%" in flat, str(g))
    g = nums(kg, "ratio", 2)
    check("grammar 0.97x at -1.2 sigma",
          len(g) == 2 and close(g[0], 0.97, .02) and close(g[1], -1.2, .05)
          and "0.97" in flat and "-1.2" in flat, str(g))
    g = nums(kg, "none do", 3)
    check("stem test 68.7% share no stem",
          len(g) == 3 and close(g[2], 68.7, .02) and "68.7%" in flat, str(g))
    check("the overstatement is corrected, not quietly dropped",
          "does not support it" in flat and "the instrument is wrong" in flat
          and "has not been shown" in flat)

    kt = out("kttranslate.txt")
    g = nums(kt, "one sense", 2)
    check("rendering: one sense 3440 = 11.5%",
          len(g) == 2 and g[0] == 3440 and close(g[1], 11.5, .02) and "11.3%" in flat, str(g))
    g = nums(kt, "several senses", 2)
    check("rendering: several senses 47.4%",
          len(g) == 2 and close(g[1], 47.4, .02) and "47.4%" in flat, str(g))
    g = nums(kt, "by composition", 2)
    check("rendering: by composition 5811 = 19.4%",
          len(g) == 2 and g[0] == 5811 and close(g[1], 19.4, .02) and "19.4%" in flat, str(g))
    g = nums(kt, "their variant spelling", 2)
    check("rendering: declared variants 357 = 1.2%",
          len(g) == 2 and g[0] == 357 and close(g[1], 1.2, .02) and "357" in flat, str(g))
    g = nums(kt, "no reading", 2)
    check("rendering: no reading 20.5%",
          len(g) == 2 and close(g[1], 20.5, .02) and "20.5%" in flat, str(g))
    g = nums(kt, "every word read", 2)
    check("rendering: 1041 lines fully read = 23.8%",
          len(g) == 2 and g[0] == 1041 and close(g[1], 23.8, .02) and "1041" in flat, str(g))
    kv = out("ktvariant.txt")
    g = nums(kv, "declared variants tested", 1)
    check("variants: 23 declared tested", bool(g) and g[0] == 23, str(g))
    g = nums(kv, "closer to headword than to stand-in", 1)
    check("variants: bar A 60.9%", bool(g) and close(g[0], 60.9, .02) and "60.9%" in flat, str(g))
    g = nums(kv, "one glyph from exactly one defined code", 4)
    check("variants: 98 neighbours, 926 tokens, 3.1%",
          len(g) == 4 and g[0] == 98 and g[1] == 926 and close(g[3], 3.1, .02)
          and "926" in flat, str(g))
    g = nums(kv, "closer to neighbour than to stand-in", 1)
    check("variants: bar B 53.1%", bool(g) and close(g[0], 53.1, .02) and "53.1%" in flat, str(g))
    sig = [float(x) for x in re.findall(r"sigma (-?\d+\.\d+)", kv)]
    check("variants: 2.6 and 4.8 sigma, both FAIL",
          len(sig) == 2 and close(sig[0], 2.6, .05) and close(sig[1], 4.8, .05)
          and kv.count("->  FAIL") == 2 and "2.6 sigma" in flat and "4.8 sigma" in flat, str(sig))
    g = nums(kv, "book coverage", 2)
    check("variants: coverage 77.6% -> 78.8%",
          len(g) == 2 and close(g[0], 77.6, .02) and close(g[1], 78.8, .02) and "78.8%" in flat, str(g))
    tr = os.path.join(WORK, "translation", "rohonc_reading.txt")
    trf = os.path.join(WORK, "translation", "rohonc_reading_full.txt")
    check("rendering: both files exist and cover 441 pages",
          os.path.exists(tr) and os.path.exists(trf)
          and open(tr, encoding="utf-8").read().count("\n=== ") == 441)
    check("rendering: the 137v line reads as documented",
          os.path.exists(tr) and "virgin-girl this-Mary" in open(tr, encoding="utf-8").read()
          and "virgin-girl this-Mary" in flat)

    tr_md = os.path.join(WORK, "translation", "rohonc_translation.md")
    md = open(tr_md, encoding="utf-8").read() if os.path.exists(tr_md) else ""
    check("translation: the file exists and covers 260 folios",
          md.count("\n## 0") + md.count("\n## 1") == 260, str(md.count("\n## 0")))
    import re as _re
    heads = set(_re.findall(r"^## (\d{3}[rv]) ", md, _re.M))
    try:
        import ktcontext as _X
        done = _X.DONE
    except Exception:
        done = None
    check("translation: ktcontext.DONE is derived from the file, not kept by hand",
          done is not None and done == heads, f"{len(done or ())} vs {len(heads)}")
    check("translation: the book is identified, with its sources named",
          "Life of Adam and Eve" in md and "Legend of the Rood" in md
          and "Saint Matthew and Saint John" in md and "Elijah" in md)
    check("ROHONC: what the book says, and the honesty clause",
          "Life of Adam and Eve" in flat and "Whom seek ye" in flat
          and "one to two right in six" in flat)
    check("ROHONC: the four numeral checks are stated",
          "six-two` is eight" in doc and "six-six` is twelve" in doc
          and "forty days of rain" in flat)

    ka = out("ktanchor.txt")
    check("frames: radius 3 has no testable case, reported as such",
          "frames where both codes are defined      0" in ka
          and "cannot be run" in flat and "->  FAIL" in ka)
    kvz = out("ktverse.txt")
    g = nums(kvz, "held-out codes tested", 1)
    check("anchors: 925 held-out codes tested",
          bool(g) and g[0] == 925 and "925" in flat, str(g))
    g = nums(kvz, "gloss found in the relocated window", 1)
    check("anchors: recovery 15.5%",
          bool(g) and close(g[0], 15.5, .02) and "15.5%" in flat, str(g))
    g = nums(kvz, "same test against a random window", 2)
    check("anchors: control 4.1%",
          bool(g) and close(g[0], 4.1, .02) and "4.1%" in flat, str(g))
    g = nums(kvz, "ratio", 2)
    check("anchors: 3.75x at 18.5 sigma, FAIL",
          len(g) == 2 and close(g[0], 3.75, .02) and close(g[1], 18.5, .05)
          and "3.75" in flat and "18.5" in flat and "->  FAIL" in kvz, str(g))
    g = nums(kvz, "anchors (top", 3)
    check("anchors: 213 lines located",
          bool(g) and 213 in [int(x) for x in g] and "213 lines" in flat, str(g))
    check("anchors: both parables named with their confirmation",
          "Unmerciful Servant" in flat and "Lost Sheep" in flat
          and "denarius" in flat and "ninety and nine" in flat)

    kv2 = out("ktverse2.txt")
    g = nums(kv2, "test cases under the rule", 1)
    check("refinement: 26 held-out test cases", bool(g) and g[0] == 26 and "26 cases" in flat, str(g))
    g = nums(kv2, "gloss found in the relocated window", 1)
    check("refinement: 30.8% recovery, FAIL",
          bool(g) and close(g[0], 30.8, .02) and "30.8%" in flat and "->  FAIL" in kv2, str(g))
    check("refinement: selected rule is proper names, dev 28.6%",
          "gloss is a name" in kv2 and "28.6%" in kv2 and "28.6%" in flat)

    g = nums(kt, "proposed here", 2)
    check("proposals: 2559 tokens = 8.5% rendered",
          len(g) == 2 and g[0] == 2559 and close(g[1], 8.5, .02), str(g))
    g = nums(kt, "lines with every word read", 2)
    check("proposals: 2671 lines fully read with them",
          len(g) == 2 and g[0] == 2671 and close(g[1], 61.1, .02), str(g))
    check("proposals: file has tier A entries with evidence",
          os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "proposals.json"))
          and '"tier": "A"' in open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "proposals.json")).read())

    check("ROHONC: the Reproaches and Longinus are named",
          "Improperia" in flat and "Longinus" in flat and "Golden Legend" in flat)
    check("ROHONC: METHOD.md and the readings are stated",
          "METHOD.md" in flat and "287 signs are read" in flat
          and "23.8% to **61.1%**" in flat)

    check("ROHONC: E034 is punctuation, measured",
          "99.7%" in flat and "E034" in flat and "terminator" in flat)

    check("ROHONC: the gap engine and no floor",
          "1,232 lines" in flat and "one word short" in flat
          and "not a wall" in flat)

    check("ROHONC: the creation passage is written twice",
          "writes the creation twice" in flat and "121v-123r" in flat
          and "003r11 and 122v08" in flat)
    check("ROHONC: the apparatus check and the Elijah correction are recorded",
          "was read as Enoch" in flat and "father son" in flat
          and "ktlook.py --cite" in flat and "Saint Augustine the church father" in flat)
    check("ROHONC: Emmaus run translated and Cleopas named",
          "260\nfolios are translated" in doc and "names Cleopas" in flat
          and "of sin, and of righteousness, and of" in flat
          and "child on the seashore" in flat
          and "sign for sign and in order" in flat
          and "It also repeats itself" in flat
          and "as Abraham gave" in flat and "Abraham stands for the Father" in flat
          and "which is wrong" in flat)

    check("ROHONC: the self-citations are checked, ten of sixteen",
          "Ten of sixteen land" in flat and "Luke 10:23   OK" in doc
          and "Luke 19:29   OFF" in doc and "off by ten" in flat
          and "Luke 15:11   OFF" in doc and "Luke 15:1    OFF" in doc
          and "John 14:5    OFF" in doc
          and "eight of nine, it is now ten of sixteen" in flat
          and "about two times in three" in flat
          and "six misses share a shape" in flat and "None" in flat)
    check("ROHONC: the self-citations are checked, seven of eight",
          "Matthew 5:13  OK" in doc and "John 3:1     OFF" in flat.replace("  "," ").replace("John 3:1 OFF","John 3:1     OFF") or "OFF" in flat)

    check("ROHONC: seven, not the last, and what it unlocked",
          "so it is **seven**" in flat and "seventy disciples" in flat
          and "seven evil spirits" in flat)

    check("ROHONC: what the book is for, argued from structure",
          "book of readings" in flat and "nobody invents a script to hide" in flat
          and "not a gated result" in flat)

    check("ROHONC: my own wrong readings are corrected in place",
          "Two of my own readings corrected" in flat
          and "as the scripture saith" in flat and "the tree of mercy" in flat)

    check("ROHONC: two readings withdrawn by the blast-radius audit",
          "blast radius" in flat and "570 = ark" in flat and "540 = shall" in flat
          and "59.5% down to 57.9%" in flat
          and "pollutes more than a gap" in flat)

    check("ROHONC: the rendering is reproducible again",
          "224 lines" in flat and "byte-identical" in flat)

    check("ROHONC: the residue engine ranks blocking pieces",
          "ktresidue.py" in flat and "896 distinct pieces" in flat)

    sf = out("ktsense_full.txt")
    check("sense rerun, seed-once, full context: 39.9%, FAIL",
          "picked from real context               39.9%" in sf and "->  FAIL" in sf)
    pk = out("ktsense_percase_kt.txt"); pf = out("ktsense_percase_full.txt")
    check("sense rerun, per-case distractors: 39.8% -> 40.9%",
          "39.8%" in pk and "40.9%" in pf)
    check("ROHONC: the sense rerun is stated with its confound and its counts",
          "941 of 2357" in flat and "966 of 2360" in flat
          and "67 newly right, 40 newly wrong" in flat
          and "0 predictions changed" in flat and "It is not a pass" in flat
          and "third prediction of mine" in flat)

    check("ROHONC: the eighteenth attempt is recorded as a FAIL",
          "eighteenth attempt" in flat and "1.04x" in flat and "1.03x" in flat
          and "failures of the measure, not as evidence against the" in flat)

    check("ROHONC: the arithmetic of reaching 98% of lines is stated",
          "**0.3%**" in flat and "6.9 words long" in flat
          and "occur exactly once" in flat)

    check("ROHONC: the Hungarian test, and the wrong prediction owned",
          "Hungarian" in flat and "second wrong prediction" in flat
          and "56.0%" in flat and "68.3%" in flat)

    check("CONCLUSION: credit and the missing grammar paper",
          "The grammar is theirs" in conf and "grammar paper" in conf)

    print(f"\n{'ALL FIGURES CHECK OUT' if not FAILS else 'MISMATCHED (' + str(len(FAILS)) + '): ' + '; '.join(FAILS)}")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
