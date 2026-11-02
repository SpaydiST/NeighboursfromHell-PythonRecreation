#!/usr/bin/env python3
"""Convert every XML file of the game's `gamedata` folder into a Python module.

    python tools/xml2py.py path/to/gamedata  [path/to/nfh/data]

Each XML file `a/b.xml` becomes `nfh/data/a/b.py` containing `ROOTS = [n(...), ...]`.
The conversion is lossless (tags, attributes, text, order) except for XML comments.
"""
from __future__ import annotations
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from nfh.xmlio import parse_file          # noqa: E402
from nfh.node import Node                 # noqa: E402


def emit(node: Node, level: int, out: list):
    pad = "    " * level
    parts = [repr(node.tag)]
    parts.append(repr(node.attrs) if node.attrs or node.children or node.text else "")
    if node.attrs:
        pass
    args = [repr(node.tag), repr(node.attrs)]
    if node.children:
        out.append(f"{pad}n({args[0]}, {args[1]}, [")
        for c in node.children:
            emit(c, level + 1, out)
        tail = f", {node.text!r}" if node.text else ""
        out.append(f"{pad}]{tail}),")
    else:
        tail = f", None, {node.text!r}" if node.text else ""
        out.append(f"{pad}n({args[0]}, {args[1]}{tail}),")


def convert_file(src: str, dst: str):
    roots = parse_file(src)
    lines = ["# -*- coding: utf-8 -*-",
             f"# Generated from {os.path.basename(src)} by tools/xml2py.py - do not edit by hand.",
             "from nfh.node import n", "", "ROOTS = ["]
    for r in roots:
        emit(r, 1, lines)
    lines.append("]")
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")


def main():
    src_root = sys.argv[1] if len(sys.argv) > 1 else "gamedata"
    dst_root = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(HERE), "nfh", "data")
    count = 0
    for root, _dirs, files in os.walk(src_root):
        for fn in sorted(files):
            if not fn.lower().endswith(".xml"):
                continue
            src = os.path.join(root, fn)
            rel = os.path.relpath(src, src_root)[:-4]
            dst = os.path.join(dst_root, rel + ".py")
            convert_file(src, dst)
            count += 1
    # make every directory a package
    for root, dirs, _files in os.walk(dst_root):
        init = os.path.join(root, "__init__.py")
        if not os.path.exists(init):
            open(init, "w").close()
    print(f"converted {count} XML files -> {dst_root}")


if __name__ == "__main__":
    main()
