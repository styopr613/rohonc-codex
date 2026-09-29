"""Carry the live figures into ROHONC.md and check_rohonc.py, from the runs.

Every batch changes four numbers: folios translated, signs read, tier A
readings, and lines fully read. They were being retyped by hand into two
files after every batch, and the checker caught a stale one more than once.
This reads each figure from where it actually lives and rewrites the
sentences that quote it, so the prose can never lag the run.

    python3 ktbump.py            # rewrite, then print what changed
    python3 ktbump.py --dry      # print only

Sources: the folio headings of the translation file; proposals.json; the
saved run work/rohonc/kttranslate.txt (regenerate it first with
`python3 kttranslate.py > ../work/rohonc/kttranslate.txt`).
"""
import json
import os
import re
import sys
from collections import Counter

import corpus

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
WORK = os.path.join(ROOT, "work", "rohonc")


def live():
    md = open(os.path.join(WORK, "translation", "rohonc_translation.md"), encoding="utf-8").read()
    folios = len(set(re.findall(r"^## (\d{3}[rv]) ", md, re.M)))
    p = json.load(open(os.path.join(HERE, "proposals.json"), encoding="utf-8"))
    tiers = Counter(v["tier"] for k, v in p.items() if not k.startswith("_"))
    kt = open(os.path.join(WORK, "kttranslate.txt"), encoding="utf-8").read()
    prop = re.findall(r"proposed here\s+(\d+)\s+([\d.]+)%", kt)[-1]
    full = re.findall(r"lines with every word read\s+(\d+)\s+([\d.]+)%", kt)[-1]
    comp = re.findall(r"lines complete incl\. guesses\s+(\d+)\s+([\d.]+)%", kt)[-1]
    # The words that have a reading which is NOT a guess. CONCLUSION.md states
    # this beside the two line figures, and it was the one of the three that
    # nothing generated: it sat at 96.7% while the run said 96.6%, and the
    # gate pinned the stale string rather than comparing it to anything.
    words = int(re.search(r"^words\s+(\d+)", kt, re.M).group(1))
    guessed = int(re.findall(r"GUESSED here \(tier G\)\s+(\d+)", kt)[-1])
    noread = int(re.findall(r"no reading\s+(\d+)", kt)[-1])
    return dict(folios=folios, signs=sum(tiers.values()), a=tiers["A"], tiers=tiers,
                ptok=int(prop[0]), ppct=float(prop[1]),
                flines=int(full[0]), fpct=float(full[1]),
                cpct=float(comp[1]),
                rpct=round(100.0 * (words - guessed - noread) / words, 1))


def prov():
    """Run ktprov.py, save it as work/rohonc/ktprov.txt, return its figures.

    Added 2026-09-29. CONCLUSION's two provenance blocks (the rendering word
    by word, and the non-guess readings by where they came from) were typed
    by hand from a ktprov run and never regenerated: they said 5 words with
    no reading where the run said 51, and 514 anchored where it said 508.
    """
    import subprocess
    out = subprocess.run([sys.executable, os.path.join(HERE, "ktprov.py")],
                         cwd=HERE, text=True, capture_output=True).stdout
    open(os.path.join(WORK, "ktprov.txt"), "w", encoding="utf-8").write(out)
    def row(label):
        m = re.search(r"^\s*" + re.escape(label) + r"\s+(\d+)\s+([\d.]+)%", out, re.M)
        return int(m.group(1)), float(m.group(2))
    def signs(label):
        m = re.search(r"^\s*" + re.escape(label) + r"\s+(\d+) signs", out, re.M)
        return int(m.group(1))
    of = re.search(r"of the KT-anchored: holds (\d+), one-glyph (\d+), inside (\d+)", out)
    judged = int(re.search(r"judgments flagged in the evidence: (\d+)", out).group(1))
    return dict(direct=row("KT-direct"), comp=row("by composition of read signs"),
                anch=row("KT-anchored"), chain=row("KT-chained"), pas=row("passage"),
                guess=row("guess"), none=row("no reading"),
                s_anch=signs("KT-anchored"), s_chain=signs("KT-chained"), s_pas=signs("passage"),
                holds=int(of.group(1)), glyph=int(of.group(2)), inside=int(of.group(3)),
                judged=judged)


def cell(line, n, pct=None):
    """Rewrite the numeric tail of a table line, keeping its column widths."""
    m = re.search(r"(\d[\d,]*)(\s+)([\d.]+%)\s*$", line) if pct is not None else re.search(r"(\d[\d,]*) signs(\s+)([\d.]+%)\s*$", line)
    if not m:
        return line
    head = line[:m.start(1)]
    num = f"{n:,}"
    head = head[:max(len(head) - (len(num) - len(m.group(1))), 0)] if len(num) > len(m.group(1)) else head + " " * (len(m.group(1)) - len(num))
    if pct is None:
        return head + num + " signs" + m.group(2) + line[m.start(3):]
    p = f"{pct:.1f}%"
    return head + num + m.group(2) + " " * max(len(m.group(3)) - len(p), 0) + p


def sub(text, pattern, repl, name, changes, fn=None):
    # A function replacement: re.sub would otherwise turn the '\\n' inside a
    # replacement into a real newline, which broke check_rohonc.py once.
    new, n = re.subn(pattern, fn if fn else (lambda m: repl), text)
    if n == 0:
        print(f"  MISSING anchor for {name}: {pattern}")
    elif new != text:
        changes.append(name)
    return new


def main(argv):
    dry = "--dry" in argv
    L = live()
    print("live:", L)
    changes = []

    p = os.path.join(ROOT, "ROHONC.md")
    s = open(p, encoding="utf-8").read()
    s = sub(s, r"and \d+\nfolios are translated", f"and {L['folios']}\nfolios are translated", "ROHONC folios", changes)
    s = sub(s, r"\d+ signs are read\nthis way", f"{L['signs']} signs are read\nthis way", "ROHONC signs", changes)
    s = sub(s, r"graded A, B, C or D\. \d+ are tier A", f"graded A, B, C or D. {L['a']} are tier A", "ROHONC tier A", changes)
    s = sub(s, r"lines where every word is read from 23\.8% to \*\*[\d.]+%\*\*",
            f"lines where every word is read from 23.8% to **{L['fpct']:.1f}%**", "ROHONC lines %", changes)
    if not dry:
        open(p, "w", encoding="utf-8").write(s)

    # CONCLUSION.md states the same three figures in plain English and nothing
    # carried them: it still said 82.3% / 99.9% / 96.7% when the run said
    # 81.5 / 98.9 / 96.6, and check_rohonc.py required those stale strings to
    # be present, so the gate was holding the wrong number in place. The dated
    # sentences ("at 82.3% that evening", "from 80.1% to 82.3%") are history
    # and are deliberately NOT touched.
    p = os.path.join(ROOT, "CONCLUSION.md")
    s = open(p, encoding="utf-8").read()
    gap = round(L["cpct"] - L["fpct"], 1)
    s = sub(s, r"\*\*[\d.]+% of the\nwords have \*a\* reading",
            f"**{L['rpct']:.1f}% of the\nwords have *a* reading".replace("\\n", "\n"),
            "CONCLUSION words %", changes)
    s = sub(s, r"; [\d.]+% of the lines have every word read; and [\d.]+% of\nthe lines are complete",
            f"; {L['fpct']:.1f}% of the lines have every word read; and {L['cpct']:.1f}% of\nthe lines are complete".replace("\\n", "\n"),
            "CONCLUSION line figures", changes)
    s = sub(s, r"\*\*What the [\d.]+% is made of\.\*\*",
            f"**What the {L['fpct']:.1f}% is made of.**", "CONCLUSION made-of", changes)
    s = sub(s, r"\*\*[\d.]+%\nread, [\d.]+% complete including guesses\*\* -- and the gap between them, [\d.]+",
            f"**{L['fpct']:.1f}%\nread, {L['cpct']:.1f}% complete including guesses** -- and the gap between them, {gap}".replace("\\n", "\n"),
            "CONCLUSION two figures", changes)
    # The tier table. It was hand-typed on 2026-09-2x and by 2026-09-29 said
    # 1,786 entries with 82 at D and 839 at G while proposals.json held 52 and
    # 847: nothing generated it and nothing checked it. Generated here now,
    # from the same Counter as the ROHONC figures, and pinned in check_rohonc.
    live_entries = sum(L["tiers"][k] for k in "ABCDG")
    s = sub(s, r"THIS PROJECT'S [\d,]+ ENTRIES, BY TIER", f"THIS PROJECT'S {live_entries:,} ENTRIES, BY TIER", "CONCLUSION entries", changes)
    for tier, label in (("A", r"formula, a numeral, or K&T's own citation"),
                        ("B", r"B  survives most occurrences"),
                        ("C", r"C  one passage, or source-checked"),
                        ("D", r"D  a single occurrence, read from one line"),
                        ("G", r"G  a guess, never counted as read")):
        s = sub(s, label + r"( +)\d+", None, f"CONCLUSION tier {tier}", changes, fn=lambda m, tier=tier, label=label: m.group(0)[:m.start(1) - m.start(0)] + m.group(1) + str(L["tiers"][tier]))
    P = prov()
    for label, key in (("K&T's dictionary, unchanged", "direct"),
                       ("by composition of signs they read", "comp"),
                       ("this project, anchored on a K&T entry", "anch"),
                       ("of its own", "chain"),
                       ("this project, read from a passage", "pas"),
                       ("a tagged guess, bracketed, never counted", "guess"),
                       ("no reading at all", "none")):
        s = sub(s, r"(?m)^( {6,8}" + re.escape(label) + r" +\d[\d,]* +[\d.]+%)[ \t]*$", None, f"CONCLUSION rendering {key}", changes,
                fn=lambda m, key=key: cell(m.group(1), P[key][0], P[key][1]))
    notg = sum(L["tiers"][k] for k in "ABCD")
    for label, key in (("anchored on a K&T entry", "s_anch"),
                       ("anchored on a reading of ours", "s_chain"),
                       ("read from a passage", "s_pas")):
        s = sub(s, r"(?m)^( {6}" + re.escape(label) + r" +)\d+ signs +[\d.]+%[ \t]*$", None, f"CONCLUSION origin {key}", changes,
                fn=lambda m, key=key: m.group(1) + f"{P[key]} signs  {100.0 * P[key] / notg:.1f}%")
    s = sub(s, r"of which: holds one of theirs whole \d+,\n\s+one glyph from one \d+, sits inside one \d+",
            f"of which: holds one of theirs whole {P['holds']},\n        one glyph from one {P['glyph']}, sits inside one {P['inside']}".replace("\\n", "\n"),
            "CONCLUSION origin of-which", changes)
    s = sub(s, r"judgments flagged as such in the evidence: \d+", f"judgments flagged as such in the evidence: {P['judged']}", "CONCLUSION judged", changes)
    s = sub(s, r"THE [\d,]+ READINGS THAT ARE NOT GUESSES", f"THE {notg:,} READINGS THAT ARE NOT GUESSES", "CONCLUSION not guesses", changes)
    s = sub(s, r"The [\d,]+ tier G entries are not readings", f"The {L['tiers']['G']:,} tier G entries are not readings", "CONCLUSION tier G prose", changes)
    s = sub(s, r"The [\d,]+ read from a passage are the", f"The {P['s_pas']:,} read from a passage are the", "CONCLUSION passage prose", changes)
    if not dry:
        open(p, "w", encoding="utf-8").write(s)

    p = os.path.join(HERE, "check_rohonc.py")
    s = open(p, encoding="utf-8").read()
    s = sub(s, r'check\("proposals: \d+ tokens = [\d.]+% rendered",\n\s+len\(g\) == 2 and g\[0\] == \d+ and close\(g\[1\], [\d.]+, \.02\)',
            f'check("proposals: {L["ptok"]} tokens = {L["ppct"]:.1f}% rendered",\n          len(g) == 2 and g[0] == {L["ptok"]} and close(g[1], {L["ppct"]:.1f}, .02)', "check tokens", changes)
    s = sub(s, r'check\("proposals: \d+ lines fully read with them",\n\s+len\(g\) == 2 and g\[0\] == \d+ and close\(g\[1\], [\d.]+, \.02\)',
            f'check("proposals: {L["flines"]} lines fully read with them",\n          len(g) == 2 and g[0] == {L["flines"]} and close(g[1], {L["fpct"]:.1f}, .02)', "check lines", changes)
    s = sub(s, r'"\d+ signs are read" in flat\n\s+and "23\.8% to \*\*[\d.]+%\*\*" in flat',
            f'"{L["signs"]} signs are read" in flat\n          and "23.8% to **{L["fpct"]:.1f}%**" in flat', "check signs", changes)
    s = sub(s, r'"\d+\\nfolios are translated" in doc', f'"{L["folios"]}\\nfolios are translated" in doc', "check folios doc", changes)
    s = sub(s, r'"[\d.]+% of the" in conf and "[\d.]+% of the lines" in conf',
            f'"{L["rpct"]:.1f}% of the" in conf and "{L["fpct"]:.1f}% of the lines" in conf',
            "check CONCLUSION figures", changes)
    s = sub(s, r'and "[\d.]+% complete including guesses" in conf',
            f'and "{L["cpct"]:.1f}% complete including guesses" in conf',
            "check CONCLUSION complete", changes)
    # Count folio headings with the SAME regex live() uses. The old form
    # counted only "## 0" and "## 1", which silently stopped counting when
    # the translation reached folio 200r -- six folios went missing and the
    # checker failed with a number nobody could explain.
    s = sub(s, r'check\("translation: the file exists and covers \d+ folios",\n\s+len\(_folios\(md\)\) == \d+',
            f'check("translation: the file exists and covers {L["folios"]} folios",\n          len(_folios(md)) == {L["folios"]}', "check folios file", changes)
    if not dry:
        open(p, "w", encoding="utf-8").write(s)
    print("changed:", changes if changes else "nothing")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
