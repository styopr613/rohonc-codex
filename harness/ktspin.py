"""Cut the three faces of the printed book out of its Cover Maker wrap.

The Read page shows the book as a turning object: a CSS box whose front,
back and spine are real slices of the printed wrap, exactly as the OONA 13
home page shows its own paperback. This cuts those slices. The wrap is the
studio's own file and never enters the repository (7 MB, and the studio owns
it); the three slices are small, live in work/rohonc/, and are what ktsite
copies to the site.

The geometry is read from the wrap's own KDP-SETUP.txt beside it, not typed
here, so a new wrap with a different page count or trim cuts correctly.

    python3 ktspin.py                      the current design's 6x9 wrap
    python3 ktspin.py path/to/wrap.png     another wrap (its KDP-SETUP.txt beside it)
"""
import os
import re
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = os.path.join(ROOT, "work", "rohonc")
WRAP = ("/opt/covers-app/data/users/u1/out/20260922-222229-xnfy/"
        "cover-wrap-6x9-553pp-cream.png")
FACE_W = 600           # the slices are cut at this face width, the height follows the trim


def geometry(setup_txt):
    """trim (w, h), spine, bleed, dpi, all in inches except dpi."""
    t = open(setup_txt, encoding="utf-8").read()
    trim = re.search(r"Trim ([\d.]+) x ([\d.]+) in", t)
    spine = re.search(r"Spine ([\d.]+) in", t)
    bleed = re.search(r"bleed ([\d.]+) in", t)
    dpi = re.search(r"@ (\d+) DPI", t)
    if not (trim and spine and bleed and dpi):
        raise SystemExit(f"cannot read the geometry from {setup_txt}")
    return ((float(trim.group(1)), float(trim.group(2))), float(spine.group(1)),
            float(bleed.group(1)), int(dpi.group(1)))


def main(argv):
    wrap = argv[0] if argv else WRAP
    (tw, th), sp, bl, dpi = geometry(os.path.join(os.path.dirname(wrap), "KDP-SETUP.txt"))
    Image.MAX_IMAGE_PIXELS = None
    im = Image.open(wrap).convert("RGB")
    b, w, h, s = round(bl * dpi), round(tw * dpi), round(th * dpi), round(sp * dpi)
    if abs(im.width - (2 * b + 2 * w + s)) > 2 or abs(im.height - (2 * b + h)) > 2:
        raise SystemExit(f"{wrap} is {im.size}; KDP-SETUP.txt says {2*b+2*w+s}x{2*b+h}")
    face_h = round(FACE_W * th / tw)
    spine_w = round(FACE_W * sp / tw)
    faces = {
        "back": im.crop((b, b, b + w, b + h)).resize((FACE_W, face_h), Image.LANCZOS),
        "spine": im.crop((b + w, b, b + w + s, b + h)).resize((spine_w, face_h), Image.LANCZOS),
        "front": im.crop((b + w + s, b, b + w + s + w, b + h)).resize((FACE_W, face_h), Image.LANCZOS),
    }
    for name, img in faces.items():
        out = os.path.join(WORK, f"spin-{name}.webp")
        img.save(out, quality=88)
        print(f"wrote {out}  {img.width}x{img.height}")
    print(f"trim {tw}x{th} in, spine {sp} in: height/width {th/tw:.4f}, spine/width {sp/tw:.4f}")


if __name__ == "__main__":
    main(sys.argv[1:])
