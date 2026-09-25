"""Fetch the pictures for 'Discovering the work' from Wikimedia Commons.

The list is harness/finds_pictures.json; the files land in work/rohonc/finds/,
which git ignores, so the repository carries only the list. A picture already
there is not fetched again. Each is taken at 1200 px wide (or its own width,
if smaller), which is more than the page's column needs.

    python3 ktfindpics.py
"""
import io
import json
import os
import sys
import time
import urllib.parse
import urllib.request

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LIST = os.path.join(HERE, "finds_pictures.json")
OUT = os.path.join(ROOT, "work", "rohonc", "finds")
UA = {"User-Agent": "rohonc-edition/1.0 (https://oona13.com/rohonc/)"}
API = "https://commons.wikimedia.org/w/api.php?"


def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()


def main():
    pics = json.load(open(LIST, encoding="utf-8"))["pictures"]
    os.makedirs(OUT, exist_ok=True)
    for p in pics:
        dst = os.path.join(OUT, p["file"])
        if os.path.exists(dst):
            continue
        q = API + urllib.parse.urlencode({"action": "query", "format": "json", "prop": "imageinfo",
                                          "iiprop": "url|size", "iiurlwidth": "1200", "titles": p["commons"]})
        page = next(iter(json.loads(get(q))["query"]["pages"].values()))
        if "imageinfo" not in page:
            raise SystemExit(f"ktfindpics: not on Commons: {p['commons']}")
        ii = page["imageinfo"][0]
        # re-saved at quality 82: Commons thumbnails of big scans run heavy
        im = Image.open(io.BytesIO(get(ii.get("thumburl") or ii["url"]))).convert("RGB")
        im.save(dst, "JPEG", quality=82, optimize=True, progressive=True)
        print(f"{p['file']}: {os.path.getsize(dst) // 1024} KB")
        time.sleep(2)
    print(f"ktfindpics: {len(pics)} pictures in {OUT}")


if __name__ == "__main__":
    sys.exit(main())
