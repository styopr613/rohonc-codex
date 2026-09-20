"""Render the Rohonc Codex, page by page, as far as it can honestly be read.

Everything the gated work established is put on the page here and nothing
more. Each word is rendered one of four ways, and the marks say which:

    word            in Kiraly & Tokai's dictionary with one sense
    word/word       in their dictionary with several senses; the first is
                    the sense they list first, the rest follow after slashes
    word-word       not in their dictionary, but cut cleanly into dictionary
                    codes by the construction ktname.py and ktsegment.py
                    gated (12.4 and 9.8 sigma). The hyphen marks the cut.
    ~word           a variant spelling Kiraly & Tokai's own entry marks with
                    "var." (ktvariant.py); read as the headword
    [?]             no reading. The code is neither defined nor cuttable.

Two files are written.  The short one shows the first sense only, so a line
reads as a line; the full one shows every sense, so nothing is hidden.  A
vertical bar inside a line marks an unreadable glyph or an editorial gap in
the transcription.

This is a rendering of their dictionary over their transcription plus one
construction of ours.  It is not their translation, which is unpublished,
and it does not choose between senses, which needs their grammar.  Every
gloss belongs to Kiraly & Tokai and is credited to them.

    python kttranslate.py            # writes work/rohonc/translation/*.txt
"""
import json
import os
import sys
from collections import Counter

import corpus
import ktcoverage as C
import ktdict
import ktaffix as A
import ktvariant as V

PROPOSALS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "proposals.json")
import ktsegment as S

OUT = os.path.join(os.path.dirname(corpus.DATA), "work", "rohonc", "translation")


def hx(s):
    return "".join(f"{ord(c) - 0xE000:03x}" for c in s)


def ordered():
    """{code: [glosses in the order Kiraly & Tokai list them]}.

    ktdict.load() returns each code's glosses as a set, which is right for
    every test in the harness and wrong for a rendering: the first sense
    they list is their headline sense, and the shortest plain sense (which
    ktsegment.best_sense picks) is not.  For E569 that is the difference
    between 'this' and 'so'; for the copula between 'is' and 'exist'.
    Homograph entries sharing a code are merged in file order, as in ktdict.
    """
    raw = json.load(open(ktdict.DICT, encoding="utf-8"))
    out = {}
    for e in raw:
        for frag in e["entry"]:
            if frag.get("style") == "lemma" and frag.get("text", "").strip():
                g = frag["text"].strip()
                lst = out.setdefault(e["code"], [])
                if g not in lst:
                    lst.append(g)
    return out


ORDER = {}


def senses(glosses):
    """Their first plain sense first, then the rest in their order."""
    code = senses.code
    lst = [g for g in ORDER.get(code, []) if g in glosses]
    lst += sorted(g for g in glosses if g not in lst)
    plain = [g for g in lst if not g.startswith("<")]
    meta = [g for g in lst if g.startswith("<")]
    return plain + meta


def clean(s):
    """Tidy a gloss for the page: no spaces inside a word slot."""
    return s.strip().replace(" ", "_")


def seg_word(c, gl, var, prop, full):
    """Render one piece of an extended segmentation."""
    if c in gl:
        return word(c, gl, full)
    if c in var:
        return "~" + word(var[c], gl, full)
    if c in prop_ref:
        g, tier = prop_ref[c]
        return ("+" if tier in ("A", "B") else "?") + g.replace(" ", "_")
    return "[?]"


prop_ref = {}


def word(c, gl, full):
    senses.code = c
    ss = senses(gl[c])
    return clean(ss[0]) if not full else "/".join(clean(x) for x in ss)


def render_token(t, gl, seg, full, var, prop=None):
    t, mark = A.strip(t)
    if t in gl:
        return word(t, gl, full) + mark
    if t in seg:
        return "-".join(seg_word(p, gl, var, prop or {}, full) for p in seg[t]) + mark
    if t in var:
        return "~" + word(var[t], gl, full) + mark
    if prop and t in prop:
        g, tier = prop[t]
        return ("+" if tier in ("A", "B") else "?") + g.replace(" ", "_") + mark
    return ("[?]" if not full else f"[?{hx(t)}]") + mark


def kind(t, gl, seg, var, prop=None):
    t = A.strip(t)[0]
    if t in gl:
        return "one" if len(gl[t]) == 1 else "many"
    if t in seg:
        return "cut1" if all(p in gl and len(gl[p]) == 1 for p in seg[t]) else "cut"
    if t in var:
        return "var"
    if prop and t in prop:
        return "prop"
    return "none"


def load_proposals(tiers=("A", "B", "C")):
    """{code: gloss} for the readings in proposals.json.

    Tier C is included and marked differently on the page. A tier C reading
    is a reading made from one passage that nothing in the book can check,
    usually because the sign occurs only once or twice. Leaving it off the
    page does not make the page more honest, it makes it less readable; the
    mark is what carries the honesty.
    """
    if not os.path.exists(PROPOSALS):
        return {}
    raw = json.load(open(PROPOSALS, encoding="utf-8"))
    out = {}
    for h, v in raw.items():
        if h.startswith("_") or v.get("tier") not in tiers:
            continue
        code = "".join(chr(0xE000 + int(h[i:i + 3], 16)) for i in range(0, len(h), 3))
        out[code] = (v["gloss"], v["tier"])
    return out


HEADER = """\
THE ROHONC CODEX, RENDERED AS FAR AS IT READS
{mode}

Glosses: Kiraly & Tokai's dictionary (rechnitzer-kodex.hu), used by permission
of its being public and credited to them in full.  Transcription and page
order: theirs.  Composition of undefined codes into defined ones: this project
(ktname.py, ktsegment.py).  Nothing here is their translation; that is
unpublished.  Nothing here chooses between senses; that needs their grammar.

  word          dictionary word, one sense
  word/word     dictionary word, several senses, their first sense first
  word-word     undefined code read as the dictionary codes it cuts into
  ~word         variant spelling their own entry marks "var.", read as the headword
  +word         read by this project and checked at every occurrence
  ?word         read by this project from one passage, with nothing to check it against
  [?]           no reading
  word.         a full stop: the glyph E034, which ends 99.7% of the words
                carrying it at the end of a run, so it punctuates
  |             unreadable glyph or gap in the transcription

Of {tot} words: {one} read with one sense ({pone:.1f}%), {many} carry several
({pmany:.1f}%), {cut} are read by composition ({pcut:.1f}%), {var} are their
declared variant spellings ({pvar:.1f}%), {none} have no reading ({pnone:.1f}%).  Lines with every word read: {full_lines} of {lines}
({pfull:.1f}%).
"""


def main():
    gl, doc, seg = C.build()
    types_all = {t for p in doc for t in p.tokens}
    ORDER.update(ordered())
    var = {v: h for v, (h, _) in V.readings()[6].items()}
    os.makedirs(OUT, exist_ok=True)
    kinds = Counter()
    lines = full_lines = 0
    for p in doc:
        for ln in p.lines:
            toks = [t for run in ln for t in run]
            if not toks:
                continue
            lines += 1
            ks = [kind(t, gl, seg, var) for t in toks]
            kinds.update(ks)
            full_lines += all(k != "none" for k in ks)
    tot = sum(kinds.values())
    cut = kinds["cut"] + kinds["cut1"]
    stats = dict(tot=tot, one=kinds["one"], pone=kinds["one"] / tot * 100,
                 many=kinds["many"], pmany=kinds["many"] / tot * 100,
                 cut=cut, pcut=cut / tot * 100,
                 var=kinds["var"], pvar=kinds["var"] / tot * 100,
                 none=kinds["none"], pnone=kinds["none"] / tot * 100,
                 lines=lines, full_lines=full_lines,
                 pfull=full_lines / lines * 100)

    for full, name, mode in ((False, "rohonc_reading.txt", "First sense only."),
                             (True, "rohonc_reading_full.txt",
                              "Every sense, and the glyph codes of unread words.")):
        path = os.path.join(OUT, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(HEADER.format(mode=mode, **stats))
            for p in doc:
                f.write(f"\n\n=== {p.page} ===\n")
                for i, ln in enumerate(p.lines, 1):
                    runs = [" ".join(render_token(t, gl, seg, full, var) for t in run)
                            for run in ln if run]
                    f.write(f"{i:2d}  " + " | ".join(runs) + "\n")
        print(f"wrote {path}")

    print()
    print("=" * 70)
    print("THE RENDERING")
    print("=" * 70)
    print(f"words                          {tot:6d}")
    print(f"  one sense                    {kinds['one']:6d}  {stats['pone']:5.1f}%")
    print(f"  several senses               {kinds['many']:6d}  {stats['pmany']:5.1f}%")
    print(f"  by composition               {cut:6d}  {stats['pcut']:5.1f}%")
    print(f"    every part one sense       {kinds['cut1']:6d}")
    print(f"  their variant spelling       {kinds['var']:6d}  {stats['pvar']:5.1f}%")
    print(f"  no reading                   {kinds['none']:6d}  {stats['pnone']:5.1f}%")
    print(f"lines                          {lines:6d}")
    print(f"  every word read              {full_lines:6d}  {stats['pfull']:5.1f}%")

    # ---- extend the segmentation with everything now readable.
    #
    # ktsegment cuts a word into pieces Kiraly & Tokai define. Their own
    # variant spellings, this project's readings and the clause terminator
    # are all readable too, and a compound made of those pieces is just as
    # readable as one made of theirs. Cutting with the full inventory, and
    # repeating until nothing new appears, costs no guess at all: every part
    # was already read on its own evidence.
    prop = load_proposals()
    prop_ref.update(prop)
    inv = set(gl) | set(seg) | set(var) | set(prop)
    xseg = dict(seg)
    while True:
        added = 0
        for t in types_all:
            b = A.strip(t)[0]
            if b in inv:
                continue
            cut = S.segment(b, inv)
            if cut and len(cut) >= 2:
                xseg[b] = cut
                inv.add(b)
                added += 1
        if not added:
            break
    seg = xseg

    # ---- a third rendering with this project's own proposed readings applied,
    # marked with a plus so they can never be mistaken for K&T's. Tiers A and B.
    kp = Counter()
    fl = 0
    for p in doc:
        for ln in p.lines:
            toks = [t for run in ln for t in run]
            if not toks:
                continue
            ks = [kind(t, gl, seg, var, prop) for t in toks]
            kp.update(ks)
            fl += all(k != "none" for k in ks)
    path = os.path.join(OUT, "rohonc_reading_plus.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(HEADER.format(mode="First sense only, PLUS this project's proposed readings "
                              "marked +word (harness/proposals.json, tiers A and B).", **stats))
        for p in doc:
            f.write(f"\n\n=== {p.page} ===\n")
            for i, ln in enumerate(p.lines, 1):
                runs = [" ".join(render_token(t, gl, seg, False, var, prop) for t in run)
                        for run in ln if run]
                f.write(f"{i:2d}  " + " | ".join(runs) + "\n")
    print()
    print("WITH THIS PROJECT'S PROPOSED READINGS (tiers A and B), marked +word")
    print(f"  proposed here                {kp['prop']:6d}  {kp['prop']/tot*100:5.1f}%")
    print(f"  no reading                   {kp['none']:6d}  {kp['none']/tot*100:5.1f}%")
    print(f"  lines with every word read   {fl:6d}  {fl/lines*100:5.1f}%")
    print(f"wrote {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
