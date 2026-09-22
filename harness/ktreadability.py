"""Measure the declared plain-English bar for the Rohonc reading edition.

    python3 ktreadability.py

The targets come from CODEX_REWRITE.md and are fixed before the rewrite:
semicolons <= 1.2 per 100 words, comma-and chains <= 1.3 per 100 words,
no runs of three verbless phrases, and no gloss apparatus or archaic leakage.
"""
import os
import re
import sys

import corpus

READ = os.path.join(corpus.ROOT, "work", "rohonc", "translation", "reading.md")

APPARATUS = re.compile(
    r"\b(?:in turn|somebody|then-exist|exist|why in turn|chapter-oh|O chapter)\b",
    re.I)
ARCHAIC = re.compile(
    r"\b(?:thee|thou|thy|thine|ye|unto|whither|behold|verily|lo|doth|hath|saith|"
    r"believeth|needeth|goest|healeth|seeth|taketh|hateth|divideth)\b", re.I)
FINITE = set("""am is are was were be been being has have had do does did can could
may might must shall should will would say says said speak speaks spoke tell tells told
answer answers answered ask asks asked go goes went come comes came leave leaves left
stand stands stood sit sits sat rise rises rose fall falls fell make makes made take
takes took give gives gave see sees saw hear hears heard know knows knew believe
believes believed die dies died live lives lived save saves saved damn damns damned
write writes wrote written read reads begin begins began end ends ended pray prays
prayed eat eats ate drink drinks drank call calls called cry cries cried bring brings
brought bear bears bore born keep keeps kept hold holds held put puts send sends sent
find finds found lead leads led love loves loved heal heals healed kill kills killed
judge judges judged worship worships worshipped bow bows bowed baptize baptizes baptized
appear appears appeared depart departs departed return returns returned receive receives
received open opens opened close closes closed hide hides hid suffer suffers suffered
carry carries carried walk walks walked run runs ran shine shines shone become becomes
became mean means meant signify signifies signified fulfill fulfills fulfilled create
creates created destroy destroys destroyed forgive forgives forgave forgiven betray
betrays betrayed remember remembers remembered remain remains remained show shows showed
cast casts crucify crucifies crucified pierce pierces pierced""".split())


def words(text):
    return re.findall(r"\b[^\W\d_]+(?:[’'-][^\W\d_]+)*\b", text, re.U)


def has_finite(clause):
    ws = [w.lower() for w in words(clause)]
    return any(w in FINITE or re.search(r"(?:ed|ing)$", w) for w in ws)


def verbless_runs(text):
    """Sentences containing three consecutive comma/semicolon phrases with no verb."""
    bad = []
    clean = re.sub(r"\(\d{3}[rv](?:[-–,]\d{3}[rv])*\)", "", text)
    for sentence in re.split(r"[.!?]+", clean):
        clauses = [x.strip() for x in re.split(r"[;,]", sentence) if x.strip()]
        run = []
        for clause in clauses:
            if len(words(clause)) >= 2 and not has_finite(clause):
                run.append(clause)
                if len(run) >= 3:
                    bad.append("; ".join(run[-3:]))
                    break
            else:
                run = []
    return bad


def measures(text):
    n = max(1, len(words(text)))
    return {
        "words": n,
        "semis": text.count(";"),
        "ands": len(re.findall(r",\s+and\b", text, re.I)),
        "verbless": verbless_runs(text),
        "apparatus": sorted(set(m.group(0) for m in APPARATUS.finditer(text))),
        "archaic": sorted(set(m.group(0) for m in ARCHAIC.finditer(text))),
    }


def main():
    text = open(READ, encoding="utf-8").read()
    chunks = re.split(r"(?=^## )", text, flags=re.M)
    rows = []
    for chunk in chunks:
        m = re.match(r"## ([^\n]+)", chunk)
        if m:
            rows.append((m.group(1), measures(chunk)))
    whole = measures(text)
    print(f"{'part':48} {'words':>7} {';/100':>7} {', and/100':>10} {'verbless':>9} {'apparatus':>9} {'archaic':>7}")
    for name, d in rows + [("WHOLE BOOK", whole)]:
        print(f"{name[:48]:48} {d['words']:7} {100*d['semis']/d['words']:7.2f} "
              f"{100*d['ands']/d['words']:10.2f} {len(d['verbless']):9} "
              f"{len(d['apparatus']):9} {len(d['archaic']):7}")
    if whole["apparatus"]:
        print("apparatus words:", ", ".join(whole["apparatus"]))
    if whole["archaic"]:
        print("archaic words:", ", ".join(whole["archaic"]))
    for run in whole["verbless"][:20]:
        print("verbless run:", run[:220])
    fail = (100*whole["semis"]/whole["words"] > 1.2 or
            100*whole["ands"]/whole["words"] > 1.3 or
            bool(whole["verbless"] or whole["apparatus"] or whole["archaic"]))
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
