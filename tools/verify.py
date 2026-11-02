#!/usr/bin/env python3
"""Round-trip check: generated Python data == freshly parsed XML (all files)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from nfh.xmlio import parse_file
from nfh import data

src = sys.argv[1]
ok = bad = 0
for root, _d, files in os.walk(src):
    for fn in files:
        if fn.endswith(".xml"):
            p = os.path.join(root, fn)
            rel = os.path.relpath(p, src)[:-4]
            a = [n.as_tuple() for n in parse_file(p)]
            b = [n.as_tuple() for n in data.load(rel)]
            if a == b: ok += 1
            else: bad += 1; print("MISMATCH", rel)
print(f"{ok} identical, {bad} mismatching")
sys.exit(1 if bad else 0)
