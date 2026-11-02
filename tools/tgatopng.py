#!/usr/bin/env python3
"""Convert the game's .tga files (ARGB4444 / RGB565 / 24 bit) to correct PNGs.

    python tools/tga2png.py path/to/gfxdata  out_dir
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from nfh.tga import load_tga

src, dst = sys.argv[1], sys.argv[2]
n = 0
for root, _d, files in os.walk(src):
    for f in files:
        if f.lower().endswith(".tga"):
            out = os.path.join(dst, os.path.relpath(os.path.join(root, f), src))[:-4] + ".png"
            os.makedirs(os.path.dirname(out), exist_ok=True)
            load_tga(os.path.join(root, f)).save(out)
            n += 1
print(f"{n} files converted")
