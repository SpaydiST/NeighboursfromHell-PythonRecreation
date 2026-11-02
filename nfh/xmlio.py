"""Reading the game's XML files (mixed encodings, several roots per file)."""
from __future__ import annotations
import re
import xml.etree.ElementTree as ET
from typing import List
from .node import Node


def decode_bytes(b: bytes) -> str:
    """The original files are UTF-16LE (with BOM), UTF-8 or Latin-1."""
    if b[:2] in (b"\xff\xfe", b"\xfe\xff"):
        return b.decode("utf-16")
    if b[:3] == b"\xef\xbb\xbf":
        return b[3:].decode("utf-8")
    try:
        return b.decode("utf-8")
    except UnicodeDecodeError:
        return b.decode("latin-1")


def _convert(el: ET.Element) -> Node:
    return Node(el.tag, dict(el.attrib), [_convert(c) for c in el],
                (el.text or "").strip() if len(el) == 0 else (el.text or "").strip())


def parse_text(text: str) -> List[Node]:
    """Parse a document that may contain several top-level elements."""
    text = re.sub(r"^\s*<\?xml[^>]*\?>", "", text.lstrip("\ufeff"))
    wrapper = ET.fromstring("<__wrapper__>" + text + "</__wrapper__>")
    return [_convert(c) for c in wrapper]


def parse_file(path: str) -> List[Node]:
    with open(path, "rb") as f:
        return parse_text(decode_bytes(f.read()))
