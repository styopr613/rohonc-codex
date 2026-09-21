"""TEST 12: Test 5 rescored under a strict rule.

Grok's objection to Test 5: our readings echoed in K&T's sentence
translations at 81.6% against 53.2% for K&T's own headwords in the same
sentences. Beating the dictionary's authors on their own sentences is a
warning, not a comfort: either the echo rule is loose or the glosses were
fitted to sentences the analyst had read. Test 5's rule WAS loose: any
content stem of any sense, matched by the crude stemmer, which lets a
two-sense gloss score twice and lets "priest" and "prince" meet at "pri".

THE STRICT RULE, declared before the run:
  * the FIRST sense only -- ours as entered, K&T's as they list it;
  * every content word of that sense must be present in their English;
  * present means the lemma itself: lower case, accents off, the irregular
    form mapped to its base (took -> take), and at most one regular
    inflection stripped (-s -es -ed -d -ing -eth -est, -ied -> y). No
    synonym table, no stemmer.
The looser "any content word of any sense" figure is printed beside it,
under the same lemma rule, for comparison only.
Everything else as Test 5: readings whose evidence mentions K&T excluded
as circular; glosses shuffled among the tested signs 20 times; the ceiling
is K&T's own headwords in the same sentences under the same rule.

THE INDEPENDENT RE-GLOSSER (Grok's second half): a reader who has K&T's
dictionary and their sentence translations, and does NOT have our glosses,
proposes a word for each unread sign. --prompt writes that file, with the
sentence rendered in K&T's words only, the target sign blanked, and their
English. --score FILE reads the reader's JSON answers and counts agreement
with our gloss under the strict lemma rule.

BARS, declared before the run, not moved (Grok's, verbatim):
  FAIL if strict A+B is under 40%, or under 3 sigma over the shuffle, or if
  ours beats K&T's own headwords by more than 10 points under the strict
  rule -- that pattern means leakage, not superiority.
  Re-glosser agreement under 30% means the sentences do not determine our
  reading.

    python3 ktstrict.py
    python3 ktstrict.py --prompt FILE
    python3 ktstrict.py --score REPLY.json
"""
import json
import random
import re
import sys
from collections import Counter, defaultdict

import ktcross as K
import kttranslate as T
import ktsentence as S
import kttestlib as TL

NSHUF = 20
SEED = 20260921
INFL = ("ing", "eth", "est", "es", "ed", "d", "s")


def lemma(w):
    w = w.lower().translate(K.ACCENT)
    w = K.IRREG.get(w, w)
    if len(w) > 4 and w.endswith("ied"):
        w = w[:-3] + "y"
    if len(w) > 4 and w.endswith("ies"):
        w = w[:-3] + "y"
    return w


def norm(w):
    for suf in INFL:
        if w.endswith(suf) and len(w) - len(suf) >= 3:
            w = w[:-len(suf)]
            break
    return w[:-1] if w.endswith("e") and len(w) > 3 else w


def same(a, b):
    return a == b or norm(a) == norm(b)


def words(text):
    g = re.sub(r"[<\[(][^>\])]*[>\])]", " ", text.replace("_", " "))
    return [lemma(w) for w in re.findall(r"[a-zA-Z]+", g)
            if w.lower() not in K.STOP and len(w) >= 3]


def first_sense(gloss):
    g = re.sub(r"[<\[(][^>\])]*[>\])]", " ", gloss)
    return re.split(r"[;,]", g)[0]


def strict_hit(gloss, eng_words):
    ws = words(first_sense(gloss))
    return bool(ws) and all(any(same(w, e) for e in eng_words) for w in ws)


def loose_hit(gloss, eng_words):
    ws = words(gloss)
    return any(any(same(w, e) for e in eng_words) for w in ws)


def hx(s):
    return S.hx(s)


def setup():
    gl, doc, seg, var, prop, inv = K.build()
    p = json.load(open('proposals.json', encoding='utf-8'))
    order = T.ordered()
    okey = {}
    for k, v in order.items():
        okey[hx(k) if not re.fullmatch(r"[0-9a-f]+", k) else k] = v
    ktfirst = {}
    for s, g in gl.items():
        h = hx(s)
        lst = okey.get(h) or sorted(g)
        ktfirst[h] = "; ".join(lst)
    ours = {}
    for h, v in p.items():
        if h.startswith('_') or not isinstance(v, dict) or v.get('tier') not in 'ABCDG':
            continue
        if S.CIRC.search(v.get('evidence', '')):
            continue
        if words(v.get('gloss', '')):
            ours[h] = (v['tier'], v['gloss'])
    sents = S.sentences()
    kpairs, opairs = [], defaultdict(list)
    for head, codes, eng, ref in sents:
        ew = words(eng)
        if not ew:
            continue
        for c in set(codes):
            # the same requirement as ours: a first sense with a content word.
            # 109 of K&T's pairs are particles ('from; away; the') and were
            # counted as misses in the first run, which deflated their rate.
            if c in ktfirst and c != head and words(first_sense(ktfirst[c])):
                kpairs.append((c, ktfirst[c], ew))
            if c in ours:
                opairs[ours[c][0]].append((c, ours[c][1], ew, codes, eng, ref))
    return gl, var, ktfirst, ours, sents, kpairs, opairs


def main(argv):
    gl, var, ktfirst, ours, sents, kpairs, opairs = setup()
    if '--prompt' in argv:
        return write_prompt(argv[argv.index('--prompt') + 1], gl, var, ktfirst, opairs)
    if '--score' in argv:
        return score(argv[argv.index('--score') + 1], opairs)
    print("TEST 12: TEST 5 RESCORED, STRICT LEMMA RULE, FIRST SENSE ONLY")
    print(f"  sentences {len(sents)}; K&T pairs {len(kpairs)}")
    ks = sum(strict_hit(g, ew) for _, g, ew in kpairs) / len(kpairs)
    kl = sum(loose_hit(g, ew) for _, g, ew in kpairs) / len(kpairs)
    print(f"  K&T's own headwords   strict {ks*100:5.1f}%   loose {kl*100:5.1f}%\n")
    print(f"  {'tier':6s}{'signs':>6s}{'pairs':>7s}{'strict':>8s}{'shuffle':>9s}{'sd':>6s}"
          f"{'sigma':>7s}{'loose':>8s}")
    rng = random.Random(SEED)
    res = {}
    for group, tiers in (('A+B', 'AB'), ('C+D', 'CD'), ('G', 'G')):
        rows = [r for t in tiers for r in opairs[t]]
        if not rows:
            print(f"  {group:6s}     0")
            continue
        n = len(rows)
        obs = sum(strict_hit(g, ew) for _, g, ew, *_ in rows) / n
        loose = sum(loose_hit(g, ew) for _, g, ew, *_ in rows) / n
        signs = sorted({c for c, *_ in rows})
        gl_of = {c: g for c, g, *_ in rows}
        nulls = []
        for _ in range(NSHUF):
            perm = signs[:]
            rng.shuffle(perm)
            m = dict(zip(signs, perm))
            nulls.append(sum(strict_hit(gl_of[m[c]], ew) for c, _, ew, *_ in rows) / n)
        mu, sd, sig = TL.sigma(obs, nulls)
        res[group] = (obs, sig, n)
        print(f"  {group:6s}{len(signs):6d}{n:7d}{obs*100:7.1f}%{mu*100:8.1f}%{sd*100:6.2f}"
              f"{sig:7.1f}{loose*100:7.1f}%")
        if group != 'G':
            miss = [(c, first_sense(g).strip()) for c, g, ew, *_ in rows if not strict_hit(g, ew)]
            print("         strict misses: " + ", ".join(f"{c}({g})" for c, g in miss)[:400])
    print()
    obs, sig, n = res.get('A+B', (0, 0, 0))
    a, b, c = obs >= 0.40, sig >= 3, obs - ks <= 0.10
    print(f"  A+B strict {obs*100:.1f}%  (bar >= 40%)                      {'ok' if a else 'FAIL'}")
    print(f"  A+B {sig:.1f} sigma over the shuffle  (bar >= 3)          {'ok' if b else 'FAIL'}")
    print(f"  A+B minus K&T's own headwords {(obs-ks)*100:+.1f} points  (bar <= +10)   {'ok' if c else 'FAIL'}")
    ok = a and b and c
    print(f"  BAR  ->  {'PASS' if ok else 'FAIL'}")
    part3(gl, ours, kpairs, opairs)
    return 0 if ok else 1


def part3(gl, ours, kpairs, opairs):
    """Two declared follow-ups, reported beside the bar, which stands as it fell.

    MATCHED COMPARISON. K&T's headwords in these sentences include particles,
    prefixes and the commonest words of the book, which a free translation
    swallows; the 26 signs of ours that reach this test are content words.
    Cells: (content words in the first sense: 1 or 2+) x (the sign's token
    count in the book: <= 10, 11-50, > 50). K&T's strict rate per cell,
    reweighted to our pairs' cell distribution, is the matched rate.

    LEAKAGE CHECK. If our glosses were echoes of these sentences, they carry
    nothing elsewhere. For the same signs, on cited folios that are neither
    in their evidence nor the folio of a K&T sentence: is a content stem of
    the gloss in the cited passage (Test 1's measure), against 20 shuffles.
    """
    import ktcross as K2
    import ktleft as L2
    import ktaffix as A2
    gl2, doc, seg, var, prop, inv = K2.build()
    cnt = Counter(A2.strip(t)[0] for pg in doc for t in pg.tokens)
    un = lambda h: "".join(chr(0xE000 + int(h[i:i + 3], 16)) for i in range(0, len(h), 3))

    def cell(gloss, h):
        nw = len(words(first_sense(gloss)))
        n = cnt.get(un(h), 0)
        return (1 if nw == 1 else 2, 0 if n <= 10 else 1 if n <= 50 else 2)

    rows = opairs['A'] + opairs['B']
    ours_cells = Counter(cell(g, c) for c, g, *_ in rows)
    kt_cells = defaultdict(list)
    for c, g, ew in kpairs:
        kt_cells[cell(g, c)].append(strict_hit(g, ew))
    print()
    print("  part 3a, K&T's headwords matched to ours by gloss length and sign frequency")
    print(f"    {'cell (words, freq band)':28s}{'ours pairs':>11s}{'K&T pairs':>10s}{'K&T strict':>12s}")
    matched = wsum = 0
    for k in sorted(set(ours_cells) | set(kt_cells)):
        kl = kt_cells.get(k, [])
        r = sum(kl) / len(kl) if kl else None
        print(f"    {str(k):28s}{ours_cells.get(k, 0):11d}{len(kl):10d}"
              f"{(r * 100 if r is not None else float('nan')):11.1f}%")
        if r is not None and ours_cells.get(k):
            matched += r * ours_cells[k]
            wsum += ours_cells[k]
    mr = matched / wsum if wsum else 0
    obs = sum(strict_hit(g, ew) for _, g, ew, *_ in rows) / len(rows)
    print(f"    matched K&T strict rate {mr*100:.1f}%   ours {obs*100:.1f}%   "
          f"difference {(obs-mr)*100:+.1f} points   (reported; the bar above stands)")

    # leakage check
    refs = TL.cited(doc)
    vv, vd = L2.verses(), L2.verses_dr()
    pool = {f: TL.passage_stems(vv, vd, r) for f, r in refs.items()}
    where = defaultdict(set)
    for pg in doc:
        for t in pg.tokens:
            where[A2.strip(t)[0]].add(pg.page)
    p = json.load(open('proposals.json', encoding='utf-8'))
    sent_folios = defaultdict(set)
    for c, g, ew, codes, eng, ref in rows:
        sent_folios[c].add(ref[:4])
    tests = []
    for c in sorted({r[0] for r in rows}):
        ev = set(re.findall(r"\b(\d{3}[rv])\b", p[c].get('evidence', '')))
        st = TL.content(p[c]['gloss'].replace('_', ' '))
        held = sorted(f for f in where.get(un(c), ()) if f in pool
                      and f not in ev and f not in sent_folios[c])
        if st and held:
            tests.append((c, st, held))
    def rate(ts):
        hit = tot = 0
        for c, st, held in ts:
            for f in held:
                tot += 1
                hit += bool(st & pool[f])
        return hit, tot
    hit, tot = rate(tests)
    rng = random.Random(SEED + 3)
    nulls = []
    for _ in range(NSHUF):
        sts = [st for _, st, _ in tests]
        rng.shuffle(sts)
        h2, t2 = rate([(c, s, held) for (c, _, held), s in zip(tests, sts)])
        nulls.append(h2 / t2 if t2 else 0)
    o = hit / tot if tot else 0
    mu, sd, sig = TL.sigma(o, nulls)
    print()
    print("  part 3b, leakage check: the same signs on folios that are neither in their evidence")
    print("    nor the folio of a K&T sentence; gloss stem in the cited passage (Test 1's measure)")
    print(f"    signs {len(tests)}   occurrences {tot}   hit {hit}   {o*100:.1f}%   "
          f"shuffle {mu*100:.1f}% (sd {sd*100:.2f})   {sig:.1f} sigma   (reported)")


def render_kt(codes, target, gl, var, ktfirst):
    out = []
    for c in codes:
        if c == target:
            out.append("___")
        elif c in ktfirst:
            out.append(first_sense(ktfirst[c]).strip().replace(" ", "_"))
        else:
            out.append("[?]")
    return " ".join(out)


def write_prompt(path, gl, var, ktfirst, opairs):
    rows = opairs['A'] + opairs['B']
    items = []
    for i, (c, g, ew, codes, eng, ref) in enumerate(sorted(rows, key=lambda r: (r[0], r[5])), 1):
        items.append({"id": i, "sign": c, "sentence_in_dictionary_words": render_kt(codes, c, gl, var, ktfirst),
                      "authors_english": eng, "cite": ref})
    text = (
        "You are helping test a decipherment of the Rohonc Codex. Király and Tokai "
        "published a dictionary of the codex and translated whole sentences. Below, each "
        "sentence is shown word by word using ONLY their dictionary glosses (first sense), "
        "in the codex's word order; a sign they did not gloss is shown as [?]; the sign we "
        "are asking about is shown as ___. Their own English translation of the sentence "
        "follows. From that translation alone, say what ENGLISH WORD the ___ sign most "
        "likely stands for. One or two words, a lemma (base form). If the translation does "
        "not determine it, answer \"undetermined\".\n\n"
        "Answer ONLY with a JSON list of objects {\"id\": n, \"word\": \"...\"}.\n\n"
        + json.dumps(items, ensure_ascii=False, indent=1))
    open(path, "w", encoding="utf-8").write(text)
    print(f"wrote {path}: {len(items)} items, {len({r[0] for r in rows})} signs; our glosses are not in it")
    return 0


def score(path, opairs):
    rows = sorted(opairs['A'] + opairs['B'], key=lambda r: (r[0], r[5]))
    raw = open(path, encoding="utf-8").read()
    m = re.search(r"\[.*\]", raw, re.S)
    ans = {a["id"]: a["word"] for a in json.loads(m.group(0))}
    agree = und = n = 0
    per_sign = defaultdict(list)
    for i, (c, g, ew, codes, eng, ref) in enumerate(rows, 1):
        w = ans.get(i, "").strip()
        n += 1
        if not w or w.lower().startswith("undetermined"):
            und += 1
            per_sign[c].append((w, first_sense(g).strip(), False))
            continue
        hit = bool(words(w)) and any(any(same(a, b) for b in words(first_sense(g))) for a in words(w))
        agree += hit
        per_sign[c].append((w, first_sense(g).strip(), hit))
    print("TEST 12, part 2: INDEPENDENT RE-GLOSSER, no access to our glosses")
    for c, lst in sorted(per_sign.items()):
        for w, g, hit in lst:
            print(f"  {c:22s} reader '{w[:24]:24s}' ours '{g[:24]:24s}' {'AGREE' if hit else ('undetermined' if not w or w.lower().startswith('undetermined') else 'differ')}")
    print(f"\n  pairs {n}; agree {agree} ({agree/n*100:.1f}%); undetermined {und}; "
          f"agree among determined {agree/max(1,n-und)*100:.1f}%")
    print(f"  BAR: agreement >= 30%  ->  {'PASS' if agree/n >= 0.30 else 'FAIL'}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
