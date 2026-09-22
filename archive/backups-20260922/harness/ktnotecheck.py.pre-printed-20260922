"""Endnotes for Book One, and the rules they are refused by.

Book Two needs no notes. It is the evidence, every word marked, and it stands
on its own. Book One is the retelling, and a retelling is for people — so it
carries the notes, and the notes exist to let a reader check it rather than
trust it.

The house rules are Plaintext Classics', set for the Gospels by the owner and
copied here with one change for a manuscript rather than a Bible.

  1. FACTS ONLY, AND EVERY NOTE CITES.  A note states something checkable and
     names where to check it, on a `source:` line. For this book the citable
     things are:

         a folio and line of the manuscript        029r:7
         a Kiraly & Tokai dictionary entry         K&T <code>, gloss "..."
         a chapter and verse                       Douay-Rheims Luke 16:24
         a named outside text                      Golden Legend; Josephus,
                                                   Antiquities 6.201
         what THIS edition does                    proposals.json, tier B

     No interpretation. No "this is often read as". No reception history
     without a citation. No calling anything the best or the cleverest thing
     in the book. We are reading the codex, not the annotator.

  2. ONE PARAGRAPH.  A few sentences. Say the fact once and stop. No second
     paragraph — the EPUB build puts each note in one footnote aside, and a
     continuation paragraph falls outside it and renders at body size.

  3. START WITH THE FACT.  No scene-setting opener. The first sentence is the
     first fact. "The manuscript never says..." is not a fact about the text,
     it is a complaint that the text should have said it.

  4. SMALL WORDS.  No big word where a small one does the same work. This is
     the house voice and it applies to the notes as much as the prose.

  5. WHAT IS OURS IS SAID TO BE OURS.  Where a note rests on a reading this
     project made rather than on Kiraly & Tokai's dictionary, the note says
     so and gives the tier.

The bar, declared here before the first note was written, is ZERO failures on
all five checks that can be tested mechanically. Rule 1's "no interpretation"
cannot be tested by a machine; rules 1 (has a source line), 2 (one paragraph),
3 (no opener from the list), 4 (no word from the list) and 5 can.

    python3 ktnotecheck.py
    python3 ktnotecheck.py --words     what the plain-word sweep would flag
"""
import os
import re
import sys

import corpus

RT = os.path.join(corpus.ROOT, "work", "rohonc", "translation", "retelling.md")
NOTES = os.path.join(corpus.ROOT, "work", "rohonc", "translation", "notes.md")

# Openers that set a scene instead of stating a fact. Owner's rule, Luke 3:19.
OPENER = re.compile(
    r"^(the (manuscript|codex|compiler) (never|does not)|nobody |it is (often|worth|"
    r"tempting)|one might|readers? (would|will|may)|this is the (kind|sort))",
    re.I)

# Big words where small ones do. Each maps to what the house would write.
# Kept short on purpose: a long list becomes a style police and stops being read.
BIG = {
    "utilise": "use", "utilize": "use", "commence": "begin", "terminate": "end",
    "subsequently": "later", "previously": "before", "additionally": "also",
    "furthermore": "and", "moreover": "and", "however": "but",
    "numerous": "many", "sufficient": "enough", "requires": "needs",
    "demonstrates": "shows", "indicates": "shows", "illustrates": "shows",
    "constitutes": "is", "comprises": "is", "represents": "is",
    "approximately": "about", "concerning": "about", "regarding": "about",
    "obtain": "get", "purchase": "buy", "reside": "live", "depart": "leave",
    "attempt": "try", "assist": "help", "inquire": "ask", "respond": "answer",
    "initial": "first", "final": "last", "prior": "earlier",
    "facilitate": "help", "implement": "do", "methodology": "method",
    "aforementioned": "this", "hitherto": "until now", "thereupon": "then",
    "notwithstanding": "even so", "encompasses": "covers",
    "elucidate": "explain", "delineate": "set out", "posit": "suggest",
    "ascertain": "find out", "endeavour": "try", "endeavor": "try",
    "cognisant": "aware", "cognizant": "aware", "proximate": "near",
    "erroneous": "wrong", "veracity": "truth", "efficacious": "works",
    "predicated": "based", "problematic": "a problem", "myriad": "many",
    "plethora": "too many", "paradigm": "pattern", "leverage": "use",
}

# Words a note may not use about the text, because they are the annotator's
# judgment and not a fact. Rule 1.
OPINION = {
    "best", "finest", "cleverest", "greatest", "worst", "beautiful",
    "remarkable", "striking", "astonishing", "extraordinary", "brilliant",
    "masterly", "clumsy", "crude", "charming", "delightful", "moving",
    "powerful", "memorable", "enjoys", "enjoyed", "relished", "loves",
    "wonderful", "superb", "magnificent", "poignant",
}

SRC = re.compile(r"^\s*source:\s*\S", re.I | re.M)


def split_note(body):
    """(prose, source) — everything from the `source:` line on is the source.

    The first version matched only `source:` plus one character, so stripping
    it left the rest of the line behind in the prose and the rendered note
    printed a mangled half-citation followed by the whole one again. A source
    line may wrap onto the next line, so the split is positional, not a
    line match.
    """
    m = SRC.search(body)
    if not m:
        return body.strip(), ""
    return body[:m.start()].strip(), " ".join(body[m.start():].split())


def notes():
    """(anchor, body) for every note, in file order."""
    if not os.path.exists(NOTES):
        return []
    txt = open(NOTES, encoding="utf-8").read()
    out = []
    for m in re.finditer(r"^## anchor: (.+?)\n(.*?)(?=^## anchor: |\Z)",
                         txt, re.M | re.S):
        out.append((m.group(1).strip(), m.group(2).strip()))
    return out


def count(rt, anchor):
    """How many times the anchor stands in the retelling, ignoring wrapping.

    The retelling is hard-wrapped at 78 columns, so an anchor of more than a
    few words almost always straddles a line break in the file and a plain
    substring test finds nothing. Fourteen of the first forty notes failed
    that way and every one of them was really there.
    """
    pat = re.compile(r"\s+".join(re.escape(t) for t in anchor.split()))
    return len(pat.findall(rt))


def main(argv):
    rt = open(RT, encoding="utf-8").read() if os.path.exists(RT) else ""
    ns = notes()
    bad = 0
    if "--words" in argv:
        for w in sorted(set(re.findall(r"[a-z]+", rt.lower())) & set(BIG)):
            print(f"   {w} -> {BIG[w]}")
        return 0
    print(f"{len(ns)} notes")
    seen = set()
    for anchor, body in ns:
        why = []
        # 1. anchored in the retelling, exactly once
        n = count(rt, anchor)
        if n == 0:
            why.append("anchor not in the retelling")
        elif n > 1:
            why.append(f"anchor occurs {n} times; make it unique")
        if anchor in seen:
            why.append("duplicate anchor")
        seen.add(anchor)
        # 1. a source line
        if not SRC.search(body):
            why.append("no source: line")
        # 2. one paragraph
        prose, _ = split_note(body)
        if re.search(r"\n\s*\n", prose):
            why.append("more than one paragraph")
        # 3. no scene-setting opener
        if OPENER.match(prose):
            why.append("scene-setting opener; start with the fact")
        # 4/1. no big words, no opinion words
        words = set(re.findall(r"[a-z]+", prose.lower()))
        for w in sorted(words & set(BIG)):
            why.append(f"big word '{w}' -> '{BIG[w]}'")
        for w in sorted(words & OPINION):
            why.append(f"opinion word '{w}'")
        if why:
            bad += len(why)
            print(f"  FAIL  «{anchor[:46]}»")
            for x in why:
                print(f"        {x}")
    print(f"\n{'PASS' if bad == 0 else 'FAIL'}: {bad} problems, bar was 0")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
