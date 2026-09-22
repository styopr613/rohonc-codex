#!/opt/publish-app/venv/bin/python
"""Build and deploy every public Rohonc book artifact.

The public reader and the two download buttons use three separate paths. This
command rebuilds from the saved shelf design, validates the EPUB, and replaces
all three only after their candidates have been built successfully.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

sys.path.insert(0, "/opt/publish-app")
import gen  # noqa: E402

EPUBCHECK = "/opt/publish-app/tools/epubcheck/epubcheck.jar"
READER_EPUB = Path("/var/www/oona13/read/books/rohonc-codex.epub")
DOWNLOAD_EPUB = Path("/var/www/oona13/rohonc/book/the-rohonc-codex.epub")
DOWNLOAD_PDF = Path("/var/www/oona13/rohonc/book/the-rohonc-codex-print.pdf")


def digest(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def deploy(source, destination):
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.is_file():
        subprocess.run(
            ["sudo", "cp", str(destination), str(destination) + ".pre-update"],
            check=True,
        )
    staged = Path(str(destination) + ".new")
    subprocess.run(
        ["sudo", "install", "-o", "www-data", "-g", "www-data", "-m", "644",
         str(source), str(staged)],
        check=True,
    )
    subprocess.run(["sudo", "mv", str(staged), str(destination)], check=True)
    source_hash, deployed_hash = digest(source), digest(destination)
    if source_hash != deployed_hash:
        raise SystemExit(f"deployed file does not match validated build: {destination}")
    print(f"published {destination}  sha256 {deployed_hash}")


def publish(shelf):
    shelf = Path(shelf).resolve()
    book_path = shelf / "book.json"
    if not book_path.is_file():
        raise SystemExit(f"no book.json on shelf: {shelf}")
    book = json.loads(book_path.read_text(encoding="utf-8"))
    if book.get("title") != "The Rohonc Codex":
        raise SystemExit(f"refusing to publish a different book: {book.get('title')!r}")

    final_epub = shelf / "the-rohonc-codex.epub"
    candidate_epub = shelf / "the-rohonc-codex.candidate.epub"
    gen.build_epub(book, candidate_epub, shelf)
    subprocess.run(
        ["java", "-jar", EPUBCHECK, str(candidate_epub)],
        check=True,
    )
    os.replace(candidate_epub, final_epub)

    trim_file = shelf / "print.meta"
    trim = trim_file.read_text(encoding="utf-8").strip() if trim_file.is_file() else "6x9"
    if trim not in gen.PRINT_TRIMS:
        trim = "6x9"
    final_pdf = shelf / "print.pdf"
    candidate_pdf = shelf / "print.candidate.pdf"
    pages = gen.build_pdf(
        book, shelf, candidate_pdf, trim, recto=True,
        folio_pos="bottom-center", folio_style="plain", front_folios=True,
    )
    if not pages or not candidate_pdf.is_file():
        raise SystemExit("print PDF build produced no pages")
    os.replace(candidate_pdf, final_pdf)
    trim_file.write_text(trim, encoding="utf-8")

    deploy(final_epub, READER_EPUB)
    deploy(final_epub, DOWNLOAD_EPUB)
    deploy(final_pdf, DOWNLOAD_PDF)
    print(f"print PDF {pages} pages at {trim}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shelf", required=True)
    args = ap.parse_args()
    publish(args.shelf)


if __name__ == "__main__":
    main()
