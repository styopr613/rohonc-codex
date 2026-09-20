"""What is left: the words of a folio's own source passage that no sign carries.

The crosser-off (ktcross.py) says what a hole CANNOT be: any of the ~1,050
English stems already attached to a sign. This is the other half. Where the
translation names the passage a folio retells -- "Luke 24:36-41", "Genesis
3:24" -- the words of that passage are known, and the ones with no sign yet
are the short list of what the folio's holes can still be.

It is a candidate list, not a reading. A folio retells; it does not copy
(ktpair.py measured that at 0.4% agreement on doubled passages), so the
passage's free words are the pool, and each hole still has to be read on its
line and carried to every other occurrence of its sign. But a pool of ten
beats a pool of ten thousand, and the pool shrinks as signs land.

The verse text is the King James (Gutenberg #10, data/ref/rohonc/
bible_kjv_verses.txt), which keeps verse numbers; the flat bible_kjv.txt the
crosser-off ranks on does not. Passages the notes cite without chapter and
verse -- the Vita Adae, the Golden Legend, the Protevangelium -- are not
looked up; those folios show no pool.

    python ktleft.py                # every cited passage: the free words, ranked
                                    # by how many folios' passages use them
    python ktleft.py 128v 129r      # one folio: its pool beside its holes
    python ktleft.py --pages        # every folio with a cited passage
    python ktleft.py --wide 2 128v  # widen each citation by N verses each way
"""
import os
import re
import sys
from collections import Counter, defaultdict

import ktaffix as A
import ktcross as K
import kttranslate as T

HERE = os.path.dirname(os.path.abspath(__file__))
KJV = os.path.join(os.path.dirname(HERE), "data", "ref", "rohonc", "bible_kjv_verses.txt")

# The 66 books in canonical order, which is the order the Gutenberg King James
# prints them. Books are assigned by POSITION, not by parsing the heading:
# the headings are inconsistent prose ("The Second Book of the Kings", "The
# Revelation of Saint John the Devine") and guessing a short name from them
# silently merged 1 and 2 Kings, merged the gospel of John with the three
# epistles of John, and lost Samuel altogether. "Kings 19:6" then fetched
# 2 Kings 19 (Rabshakeh and Assyria) for a note that meant 1 Kings 19 (the
# cake and the cruse of water), and the shared-word intersection reported
# "rabshakeh" as a candidate for two folios about Elijah.
CANON = """Genesis Exodus Leviticus Numbers Deuteronomy Joshua Judges Ruth
1Samuel 2Samuel 1Kings 2Kings 1Chronicles 2Chronicles Ezra Nehemiah Esther Job
Psalms Proverbs Ecclesiastes Song Isaiah Jeremiah Lamentations Ezekiel Daniel
Hosea Joel Amos Obadiah Jonah Micah Nahum Habakkuk Zephaniah Haggai Zechariah
Malachi Matthew Mark Luke John Acts Romans 1Corinthians 2Corinthians Galatians
Ephesians Philippians Colossians 1Thessalonians 2Thessalonians 1Timothy
2Timothy Titus Philemon Hebrews James 1Peter 2Peter 1John 2John 3John Jude
Revelation""".split() + ["Tobias", "Judith", "Wisdom", "Ecclesiasticus",
                          "Baruch", "1Machabees", "2Machabees"]

# What a citation may call each book. A bare name with no ordinal means the
# FIRST book of that name, which is what "Kings 19:6" meant in every note
# this project wrote.
NAMES = ("Genesis Exodus Leviticus Numbers Deuteronomy Joshua Judges Ruth Samuel "
         "Kings Chronicles Ezra Nehemiah Esther Job Psalms Psalm Proverbs "
         "Ecclesiastes Song Isaiah Jeremiah Lamentations Ezekiel Daniel Hosea Joel "
         "Amos Obadiah Jonah Micah Nahum Habakkuk Zephaniah Haggai Zechariah "
         "Malachi Matthew Mark Luke John Acts Romans Corinthians Galatians "
         "Ephesians Philippians Colossians Thessalonians Timothy Titus Philemon "
         "Hebrews James Peter Jude Revelation Apocalypse Tobias Tobit Judith Wisdom "
         "Ecclesiasticus Sirach Baruch Machabees Maccabees Josue Isaias Jeremias "
         "Ezechiel Osee Abdias Jonas Micheas Habacuc Sophonias Aggeus Zacharias "
         "Malachias Paralipomenon Esdras").split()
ALIAS = {"Psalm": "Psalms", "Apocalypse": "Revelation", "Canticles": "Song",
         "Tobit": "Tobias", "Sirach": "Ecclesiasticus", "Maccabees": "Machabees",
         "Josue": "Joshua", "Isaias": "Isaiah", "Jeremias": "Jeremiah",
         "Ezechiel": "Ezekiel", "Osee": "Hosea", "Abdias": "Obadiah",
         "Jonas": "Jonah", "Micheas": "Micah", "Habacuc": "Habakkuk",
         "Sophonias": "Zephaniah", "Aggeus": "Haggai", "Zacharias": "Zechariah",
         "Malachias": "Malachi"}

ORD = {"1": "1", "2": "2", "3": "3", "i": "1", "ii": "2", "iii": "3",
       "first": "1", "second": "2", "third": "3"}

# ---- Douay-Rheims, the text tradition the book's author actually had.
#
# The codex is a Catholic devotional compilation and its sources are the
# Vulgate and the legends round it, not a Protestant English Bible. Pooling
# candidate words off the King James therefore manufactures near-misses: it
# offers "meat" where the Douay says "table" and the codex already reads
# *at table*, and it offers "dust" at Genesis 2:7 where the Vulgate has
# *de limo terrae*, slime. A word that is free in the King James and absent
# from the Douay is usually a translator's word, not the book's.
#
# Douay also carries the deuterocanon -- Tobias, Judith, Wisdom,
# Ecclesiasticus, Baruch, Machabees -- which a Catholic compilation may well
# draw on and which the King James file here does not contain at all.
#
# CAVEAT, not handled: Douay follows the Septuagint psalm numbering, so from
# Psalm 10 to 146 its numbers run one behind the King James. Any psalm
# citation is looked up in whichever text the note's numbering belongs to;
# this tool does not try to reconcile them, so treat a psalm pool as KJV-only.
DR = os.path.join(os.path.dirname(HERE), "data", "ref", "rohonc",
                  "bible_dr_verses.txt")

# canonical key -> the name Douay prints in its chapter headings
DRNAME = {
    "Joshua": "Josue", "1Samuel": "1 Kings", "2Samuel": "2 Kings",
    "1Kings": "3 Kings", "2Kings": "4 Kings",
    "1Chronicles": "1 Paralipomenon", "2Chronicles": "2 Paralipomenon",
    "Ezra": "1 Esdras", "Nehemiah": "2 Esdras",
    "Song": "Canticle of Canticles", "Isaiah": "Isaias", "Jeremiah": "Jeremias",
    "Ezekiel": "Ezechiel", "Hosea": "Osee", "Obadiah": "Abdias",
    "Jonah": "Jonas", "Micah": "Micheas", "Habakkuk": "Habacuc",
    "Zephaniah": "Sophonias", "Haggai": "Aggeus", "Zechariah": "Zacharias",
    "Malachi": "Malachias", "Revelation": "Apocalypse",
}
DEUTERO = ["Tobias", "Judith", "Wisdom", "Ecclesiasticus", "Baruch",
           "1Machabees", "2Machabees"]
DRNAME.update({"1Machabees": "1 Machabees", "2Machabees": "2 Machabees"})
DR2CANON = {v: k for k, v in DRNAME.items()}


def verses_dr():
    """{(canonical book, chapter, verse): text} from the Douay-Rheims.

    Douay prints "<Book> Chapter <n>" headings and "<c>:<v>." verse marks,
    so unlike the King James file it can be parsed by what it says rather
    than by position.
    """
    out = {}
    if not os.path.exists(DR):
        return out
    text = open(DR, encoding="utf-8", errors="ignore").read()
    marks = list(re.finditer(r"^(?:([A-Za-z0-9 ]+) Chapter (\d+)\s*$)|"
                             r"^(\d+):(\d+)\.\s", text, re.M))
    book = None
    for k, m in enumerate(marks):
        if m.group(1):
            name = m.group(1).strip()
            book = DR2CANON.get(name, name.replace(" ", ""))
            continue
        if not book:
            continue
        end = marks[k + 1].start() if k + 1 < len(marks) else len(text)
        # Douay carries Challoner's explanatory notes between the verses, set
        # as their own paragraphs ("To fulfil... By accomplishing all the
        # figures and prophecies"). Appending those to the verse put
        # commentary words -- accomplishing, assumption, perfecting -- into
        # the candidate pool as though the book could contain them. A verse
        # is one paragraph; keep the first and drop whatever follows it.
        block = text[m.end():end]
        body = " ".join(re.split(r"\n\s*\n", block.strip(), 1)[0].split())
        out[(book, int(m.group(3)), int(m.group(4)))] = body
    return out

REF = re.compile(
    r"\b(?:(1|2|3|I{1,3}|First|Second|Third)\s+)?(%s)\b\.?\s*"
    r"(\d+)(?::(\d+)(?:\s*[-\u2013]\s*(\d+))?)?"
    r"|(?<![\d:])(\d+):(\d+)(?:\s*[-\u2013]\s*(\d+))?" % "|".join(NAMES),
    re.I)

def verses():
    """{(book, chapter, verse): text} from the Gutenberg King James.

    Two things the first version of this got wrong. Books were named by
    regex off the heading, which merged 1 and 2 Kings; they are assigned by
    canonical position here, advancing at each "1:1". And a verse was only
    recognised at the start of a line, but the King James wraps and a new
    verse often begins mid-line, so each verse swallowed the start of the
    next one and every pool was inflated with a neighbouring verse's words.
    """
    out = {}
    if not os.path.exists(KJV):
        return out
    text = open(KJV, encoding="utf-8", errors="ignore").read()
    marks = list(re.finditer(r"(?<![\d:])(\d+):(\d+)\s", text))
    bi = -1
    for k, m in enumerate(marks):
        ch, v = int(m.group(1)), int(m.group(2))
        if ch == 1 and v == 1:
            bi += 1
        if bi < 0 or bi >= len(CANON):
            continue
        end = marks[k + 1].start() if k + 1 < len(marks) else len(text)
        body = " ".join(text[m.end():end].split())
        out[(CANON[bi], ch, v)] = body
    return out


def canon(name, ordinal):
    """A cited name plus an optional ordinal -> the canonical book key."""
    name = ALIAS.get(name.title(), name.title())
    n = ORD.get((ordinal or "").lower(), "")
    if n and n + name in CANON:
        return n + name
    if name in CANON:
        return name
    for b in CANON:                      # bare "Kings" means 1 Kings
        if b.endswith(name):
            return b
    return name


def refs_in(note):
    """[(book, chapter, v_from, v_to)] -- a bare C:V takes the last-named book."""
    out, book = [], None
    for m in REF.finditer(note):
        if m.group(2):
            book = canon(m.group(2), m.group(1))
            ch = int(m.group(3))
            if m.group(4):
                a = int(m.group(4))
                b = int(m.group(5)) if m.group(5) else a
                out.append((book, ch, a, b))
            else:
                out.append((book, ch, 1, 999))
        elif book:
            a = int(m.group(7))
            b = int(m.group(8)) if m.group(8) else a
            out.append((book, int(m.group(6)), a, b))
    return out


def passage(vv, refs, wide=0):
    """The verse texts a set of references names, widened by `wide` each way."""
    seen, out = set(), []
    for book, ch, a, b in refs:
        for v in range(max(1, a - wide), b + wide + 1):
            k = (book, ch, v)
            if k in vv and k not in seen:
                seen.add(k)
                out.append((k, vv[k]))
    return out


def pool(text, idx):
    """{stem: Counter(surface forms)} of the content words no sign carries."""
    stopstem = {K.stem(w) for w in K.STOP}
    free = defaultdict(Counter)
    for w in re.findall(r"[A-Za-z]+", text):
        lw = w.lower()
        if len(lw) < 3 or lw in K.STOP:
            continue
        s = K.stem(lw)
        if s in stopstem or s in idx:
            continue
        free[s][lw] += 1
    return free


def pools_for(vvk, vvd, refs, idx, wide=0):
    """(both, douay_only, kjv_only) -- the free words of a passage, split by
    which translation they come from.

    A candidate that both translations use is the safest: it survives the
    choice of English. One only Douay has is next, because Douay renders the
    Vulgate the book's author was working from. One only the King James has
    is the weakest and is usually an artifact of the translation rather than
    a word the book could contain -- "meat" for Douay's "table", "exceed"
    for its "abound", "dust" at Genesis 2:7 for its "slime".
    """
    k = pool(" ".join(t for _, t in passage(vvk, refs, wide)), idx)
    d = pool(" ".join(t for _, t in passage(vvd, refs, wide)), idx)
    both = {s: k[s] + d[s] for s in set(k) & set(d)}
    dro = {s: d[s] for s in set(d) - set(k)}
    kjo = {s: k[s] for s in set(k) - set(d)}
    # Pull out the cross-language synonyms and hand them back separately, so
    # a judgment shows as a judgment instead of sitting in the pool looking
    # like a measured candidate. See ktcross.SYNONYM.
    syn = {}
    for grp in (both, dro, kjo):
        for st in [x for x in grp if any(K.stem(w) == x for w in K.SYNONYM)]:
            syn[st] = grp.pop(st)
    return both, dro, kjo, syn


def show(p):
    return ", ".join("/".join(sorted(c)) for _, c in
                     sorted(p.items(), key=lambda x: -sum(x[1].values())))


def synnote(syn):
    """'heathen (pagan is read)' for each synonym pulled out of a pool."""
    out = []
    for st, c in syn.items():
        w = sorted(c)[0]
        base = K.SYNONYM.get(w.lower()) or next(
            (K.SYNONYM[x] for x in K.SYNONYM if K.stem(x) == st), "?")
        out.append(f"{'/'.join(sorted(c))} ({base} is read)")
    return ", ".join(out)


def page_holes(page, doc, gl, seg, var, prop, inv, cnt):
    out = []
    for p in doc:
        if p.page != page:
            continue
        for i, ln in enumerate(p.lines, 1):
            tk = [t for run in ln for t in run]
            miss = [A.strip(t)[0] for t in tk if A.strip(t)[0] not in inv]
            if not miss:
                continue
            s = " ".join(("<<%s>>" % K.hx(A.strip(t)[0])) if A.strip(t)[0] in miss
                         else T.render_token(t, gl, seg, False, var, prop) for t in tk)
            out.append((i, [(K.hx(m), cnt[m]) for m in miss], s))
    return out


def render(tk, sign, gl, seg, var, prop, inv):
    return " ".join("<<___>>" if A.strip(t)[0] == sign
                    else ("[?]" if A.strip(t)[0] not in inv
                          else T.render_token(t, gl, seg, False, var, prop)) for t in tk)


def cross(gl, doc, seg, var, prop, inv, idx, vv, vd, cited, cnt, wide):
    """Signs that recur on cited folios, with the words their passages SHARE.

    A sign standing on two folios whose passages are known can only mean a
    word both passages contain (if it is a content word from the passage at
    all). Intersecting the free pools does K&T's carry-the-guess-to-every-
    occurrence test mechanically, before any guess is made. An empty
    intersection is informative too: the sign is not a word of the passage.
    """
    where = defaultdict(list)
    for p in doc:
        for i, ln in enumerate(p.lines, 1):
            tk = [t for run in ln for t in run]
            for t in tk:
                b = A.strip(t)[0]
                if b not in inv:
                    where[b].append((p.page, i, tk))
    # Intersect on the words BOTH translations use plus the Douay-only ones.
    # A King-James-only word is dropped here: it is the class that produced
    # "meat" for a codex that says "at table".
    pools = {}
    for pg, r in cited.items():
        both, dro, _, _ = pools_for(vv, vd, r, idx, wide)
        pools[pg] = {**both, **dro}
    rows = []
    for b, occ in where.items():
        pgs = sorted({pg for pg, _, _ in occ})
        cpg = [pg for pg in pgs if pg in pools]
        if len(cpg) < 2:
            continue
        common = set.intersection(*[set(pools[pg]) for pg in cpg])
        if not common:
            continue
        rows.append((len(cpg), len(common), b, cpg, common, occ))
    rows.sort(key=lambda r: (-r[0], r[1]))
    print(f"{len(rows)} unread signs stand on 2+ cited folios whose passages share a free word")
    for ncp, nc, b, cpg, common, occ in rows:
        forms = ["/".join(sorted(set().union(*[set(pools[pg][s]) for pg in cpg]))) for s in sorted(common)]
        print(f"\n=== {K.hx(b)}  x{cnt[b]}  on {len(cpg)} cited folio(s) of {len({pg for pg,_,_ in occ})}")
        print(f"    shared: {', '.join(forms)}")
        for pg, i, tk in occ:
            print(f"    {pg}:{i:<3d} {render(tk, b, gl, seg, var, prop, inv)[:150]}")
    return 0


def onehole(gl, doc, seg, var, prop, inv, idx, vv, vd, cited, cnt, wide):
    """Lines with one hole on a cited folio, smallest pool first."""
    rows = []
    for p in doc:
        if p.page not in cited:
            continue
        b_, d_, k_, _ = pools_for(vv, vd, cited[p.page], idx, wide)
        pl = {**b_, **d_}
        kjonly = k_
        for i, ln in enumerate(p.lines, 1):
            tk = [t for run in ln for t in run]
            miss = [A.strip(t)[0] for t in tk if A.strip(t)[0] not in inv]
            if len(miss) != 1:
                continue
            forms = ["/".join(sorted(c)) for _, c in sorted(pl.items(), key=lambda x: -sum(x[1].values()))]
            rows.append((len(forms), p.page, i, miss[0], forms,
                         render(tk, miss[0], gl, seg, var, prop, inv), show(kjonly)))
    rows.sort(key=lambda r: (r[0], r[1], r[2]))
    print(f"{len(rows)} one-hole lines on cited folios")
    for n, pg, i, b, forms, s, kjo in rows:
        print(f"\n{pg}:{i:<3d} {K.hx(b)} x{cnt[b]}   pool {n}: {', '.join(forms)[:200]}")
        if kjo:
            print(f"    KJV only (weak): {kjo[:150]}")
        print(f"    {s[:160]}")
    return 0


def main(argv):
    wide = 0
    if "--wide" in argv:
        k = argv.index("--wide")
        wide = int(argv[k + 1])
        del argv[k:k + 2]
    gl, doc, seg, var, prop, inv = K.build()
    idx = K.taken_index(gl, prop)
    vv = verses()
    vd = verses_dr()
    cnt = Counter(A.strip(t)[0] for p in doc for t in p.tokens)
    pages = sorted({p.page for p in doc})
    cited = {}
    for pg in pages:
        r = refs_in(K.note_for(pg))
        if r:
            cited[pg] = r

    if not vv:
        print(f"no verse text at {KJV}")
        return 1

    want = [a for a in argv if re.fullmatch(r"\d{3}[rv]", a)]
    if "--pages" in argv:
        want = sorted(cited)

    if want:
        for pg in want:
            r = cited.get(pg, [])
            print(f"\n=== {pg}   {', '.join(f'{b} {c}:{a}' + (f'-{z}' if z != a and z != 999 else '') for b, c, a, z in r) or 'no chapter and verse cited'}")
            vs = passage(vv, r, wide)
            vsd = passage(vd, r, wide)
            if vs or vsd:
                both, dro, kjo, syn = pools_for(vv, vd, r, idx, wide)
                print(f"    {len(vs)} KJV verse(s), {len(vsd)} Douay; "
                      f"{len(both)} words free in both, {len(dro)} Douay only, {len(kjo)} KJV only")
                if both:
                    print("    both  : " + show(both))
                if dro:
                    print("    douay : " + show(dro))
                if kjo:
                    print("    KJV   : " + show(kjo) + "   <- weakest, likely translator's wording")
                if syn:
                    print("    JUDGE : " + synnote(syn)
                          + "   <- another English word for a sign already read")
            hs = page_holes(pg, doc, gl, seg, var, prop, inv, cnt)
            for i, miss, s in hs:
                tag = " ".join(f"{h}(x{n})" for h, n in miss)
                print(f"  {pg}:{i:<3d} {tag:24s} {s[:150]}")
        return 0

    if "--cross" in argv:
        return cross(gl, doc, seg, var, prop, inv, idx, vv, vd, cited, cnt, wide)
    if "--holes" in argv:
        return onehole(gl, doc, seg, var, prop, inv, idx, vv, vd, cited, cnt, wide)

    # ---- the whole pool, ranked by how many folios' passages use the word
    print(f"{len(cited)} folios cite a chapter and verse")
    byword = defaultdict(set)
    forms = defaultdict(Counter)
    nverse = 0
    for pg, r in cited.items():
        vs = passage(vv, r, wide)
        nverse += len(vs)
        b_, d_, _, _ = pools_for(vv, vd, r, idx, wide)
        for s, c in {**b_, **d_}.items():
            byword[s].add(pg)
            forms[s].update(c)
    print(f"{nverse} verses looked up; {len(byword)} content words in them carry no sign")
    print(f"{'folios':>6s}  word")
    for s, pgs in sorted(byword.items(), key=lambda x: (-len(x[1]), x[0]))[:120]:
        print(f"{len(pgs):6d}  {'/'.join(sorted(forms[s])):28s} {' '.join(sorted(pgs))[:60]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
