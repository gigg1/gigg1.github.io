#!/usr/bin/env python
"""Regenerate the favicon set from the 512x512 master at assets/img/icon.png.

Run from the repo root:
    .venv/bin/python tools/make_favicons.py

To change the artwork, replace assets/img/icon.png with a square image
(512x512 or larger) first, then run this script.

Outputs (all in assets/img/):
  icon.png         - 512x512 master; regenerated in place and idempotent
  favicon-32.png   - classic browser tab icon
  favicon-180.png  - apple-touch-icon for iOS home screen
  favicon-ico.ico  - multi-size legacy icon (16/32/48)
"""
import os
from PIL import Image, ImageFilter

SRC = "assets/img/icon.png"
OUT_DIR = "assets/img"

im = Image.open(SRC).convert("RGB")
print("source: %s %s" % (im.size, os.path.getsize(SRC)))

# Centre-crop to a square first, in case the source is not square.
w, h = im.size
side = min(w, h)
im = im.crop(((w - side) // 2, (h - side) // 2, (w + side) // 2, (h + side) // 2))

# Normalise to a fixed 512x512 base so every run derives the small icons from
# the exact same pixels. Without this, a re-run would downscale an already
# downscaled icon.png and the output would drift each time.
BASE = 512
master = im.resize((BASE, BASE), Image.LANCZOS)


def downscale(size, sharpen=True):
    out = master.resize((size, size), Image.LANCZOS)
    if sharpen and size <= 64:
        # LANCZOS softening hurts tiny icons; a light unsharp mask restores edges.
        out = out.filter(ImageFilter.UnsharpMask(radius=0.6, percent=90, threshold=2))
    return out


def save_png(img, name):
    path = os.path.join(OUT_DIR, name)
    img.save(path, "PNG", optimize=True)
    print("  %-18s %-10s %s" % (name, "%dx%d" % img.size, human(os.path.getsize(path))))


def human(n):
    return "%.1fK" % (n / 1024.0) if n < 1024 * 1024 else "%.1fM" % (n / 1048576.0)


# 512x512 master -> apple-touch-icon source
save_png(master, "icon.png")

# 32x32 -> browser tab
save_png(downscale(32), "favicon-32.png")

# 180x180 -> apple-touch-icon (iOS home screen)
save_png(downscale(180), "favicon-180.png")

# multi-size .ico for legacy browsers
ico_path = os.path.join(OUT_DIR, "favicon-ico.ico")
sizes = [(16, 16), (32, 32), (48, 48)]
downscale(48).save(ico_path, "ICO", sizes=sizes)
print("  %-18s %-10s %s" % ("favicon-ico.ico", "/".join(str(s[0]) for s in sizes), human(os.path.getsize(ico_path))))
