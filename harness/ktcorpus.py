"""The books the codex was read against, read out of DATA_PROVENANCE.md.

Every folio of Book One was read against the passage it retells, and most of
what the compiler wrote fits inside a small shelf of books: the Douay Bible,
the Life of Adam and Eve, the Golden Legend, the apocryphal gospels, Barlaam,
the Missal and the Office, Josephus, the play cycles. The provenance file is
where each was fetched, under what terms, and what it turned out to supply.
This reads that file so the site's corpus page and the book's appendix can
never drift from it.

    python3 ktcorpus.py          print the entries
"""
import os
import re

import corpus

PROV = os.path.join(corpus.ROOT, "DATA_PROVENANCE.md")


def _links(text):
    out = []
    for m in re.finditer(r"(?:Project )?Gutenberg ebooks? (\d+)(?:[–-](\d+))?", text):
        a, b = int(m.group(1)), int(m.group(2) or m.group(1))
        for n in range(a, min(b, a + 12) + 1):
            out.append((f"Gutenberg {n}", f"https://www.gutenberg.org/ebooks/{n}"))
    for m in re.finditer(r"(?:Internet Archive|archive\.org) scan `([^`]+)`", text):
        out.append(("archive.org", f"https://archive.org/details/{m.group(1)}"))
    if "archive.org" in text and not any(l == "archive.org" for l, _ in out):
        out.append(("archive.org", "https://archive.org/"))
    return out


def entries():
    txt = open(PROV, encoding="utf-8").read()
    out = []
    sec = re.search(r"^## 4\. `data/ref/rohonc/`.*?(?=^## )", txt, re.M | re.S)
    if sec:
        for b in re.findall(r"^- (\*\*.*?)(?=^- |\n\n(?!  )|\Z)", sec.group(0), re.M | re.S):
            one = " ".join(b.split())
            m = re.match(r"\*\*(.+?)\*\*\s*(?:[—-]+|,)\s*(.*)", one)
            if not m:
                continue
            name = re.sub(r"\*", "", m.group(1)).strip()
            body = m.group(2).strip()
            out.append({"name": name, "text": body, "links": _links(one),
                        "anchor": re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")})
    sec = re.search(r"^## 5\. Two sources added.*?(?=^## )", txt, re.M | re.S)
    if sec:
        for para in sec.group(0).split("\n\n"):
            one = " ".join(para.split())
            m = re.match(r"\*\*`[^`]+`(?: and `[^`]+`)?\.\*\*\s*(.+)", one)
            if not m:
                continue
            body = m.group(1)
            # Section 5 heads each paragraph with the FILE that was added, which is
            # what that section of the record is about and is no use to a reader of
            # the book, so the entry is named from the citation that opens the body.
            # The body then has to START AFTER that citation, or the printed appendix
            # says it twice -- which is what it did: "R. H. Charles, The Apocrypha and
            # Pseudepigrapha ... vol. 2. R. H. Charles, The Apocrypha and Pseudepigrapha
            # ... vol. 2 (Oxford, 1913), from ...". Every entry from section 4 splits
            # head from body at the em dash and reads correctly; these two were the only
            # ones that did not. The cut keeps its own separator, so "tr. William
            # Whiston" does not come out as "William Whiston". (2026-09-22)
            cut = re.search(r",\s*(?:from|tr\.)|\s*\(", body)
            head = body[:cut.start()] if cut else body
            name = re.sub(r"\*", "", head).strip().rstrip(",")
            rest = re.sub(r"^,\s*", "", body[cut.start():].strip()) if cut else ""
            out.append({"name": name, "text": rest, "links": _links(one),
                        "anchor": re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")[:60]})
    return out


if __name__ == "__main__":
    for e in entries():
        print(f"{e['name']}\n    {e['text'][:110]}...\n    {e['links']}")
