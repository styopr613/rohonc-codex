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
    return dict(folios=folios, signs=sum(tiers.values()), a=tiers["A"],
                ptok=int(prop[0]), ppct=float(prop[1]),
                flines=int(full[0]), fpct=float(full[1]))


def sub(text, pattern, repl, name, changes):
    # A function replacement: re.sub would otherwise turn the '\\n' inside a
    # replacement into a real newline, which broke check_rohonc.py once.
    new, n = re.subn(pattern, lambda m: repl, text)
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

    p = os.path.join(HERE, "check_rohonc.py")
    s = open(p, encoding="utf-8").read()
    s = sub(s, r'check\("proposals: \d+ tokens = [\d.]+% rendered",\n\s+len\(g\) == 2 and g\[0\] == \d+ and close\(g\[1\], [\d.]+, \.02\)',
            f'check("proposals: {L["ptok"]} tokens = {L["ppct"]:.1f}% rendered",\n          len(g) == 2 and g[0] == {L["ptok"]} and close(g[1], {L["ppct"]:.1f}, .02)', "check tokens", changes)
    s = sub(s, r'check\("proposals: \d+ lines fully read with them",\n\s+len\(g\) == 2 and g\[0\] == \d+ and close\(g\[1\], [\d.]+, \.02\)',
            f'check("proposals: {L["flines"]} lines fully read with them",\n          len(g) == 2 and g[0] == {L["flines"]} and close(g[1], {L["fpct"]:.1f}, .02)', "check lines", changes)
    s = sub(s, r'"\d+ signs are read" in flat\n\s+and "23\.8% to \*\*[\d.]+%\*\*" in flat',
            f'"{L["signs"]} signs are read" in flat\n          and "23.8% to **{L["fpct"]:.1f}%**" in flat', "check signs", changes)
    s = sub(s, r'"\d+\\nfolios are translated" in doc', f'"{L["folios"]}\\nfolios are translated" in doc', "check folios doc", changes)
    s = sub(s, r'check\("translation: the file exists and covers \d+ folios",\n\s+md\.count\("\\n## 0"\) \+ md\.count\("\\n## 1"\) == \d+',
            f'check("translation: the file exists and covers {L["folios"]} folios",\n          md.count("\\n## 0") + md.count("\\n## 1") == {L["folios"]}', "check folios file", changes)
    if not dry:
        open(p, "w", encoding="utf-8").write(s)
    print("changed:", changes if changes else "nothing")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
