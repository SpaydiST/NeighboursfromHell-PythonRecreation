"""Tiny XML-like tree used by the generated data modules."""
from __future__ import annotations
from typing import Dict, Iterator, List, Optional
from xml.sax.saxutils import quoteattr, escape


class Node:
    __slots__ = ("tag", "attrs", "children", "text")

    def __init__(self, tag: str, attrs: Optional[Dict[str, str]] = None,
                 children: Optional[List["Node"]] = None, text: str = ""):
        self.tag = tag
        self.attrs = attrs if attrs is not None else {}
        self.children = children if children is not None else []
        self.text = text

    # -- access helpers -------------------------------------------------
    def get(self, key: str, default=None):
        return self.attrs.get(key, default)

    def __getitem__(self, key: str) -> str:
        return self.attrs[key]

    def __iter__(self) -> Iterator["Node"]:
        return iter(self.children)

    def find(self, tag: str) -> Optional["Node"]:
        for c in self.children:
            if c.tag == tag:
                return c
        return None

    def findall(self, tag: str) -> List["Node"]:
        return [c for c in self.children if c.tag == tag]

    def iter(self, tag: Optional[str] = None) -> Iterator["Node"]:
        if tag is None or self.tag == tag:
            yield self
        for c in self.children:
            yield from c.iter(tag)

    # -- serialisation --------------------------------------------------
    def to_xml(self, level: int = 0) -> str:
        pad = "\t" * level
        attrs = "".join(f" {k}={quoteattr(v)}" for k, v in self.attrs.items())
        if not self.children and not self.text:
            return f"{pad}<{self.tag}{attrs}/>"
        if not self.children:
            return f"{pad}<{self.tag}{attrs}>{escape(self.text)}</{self.tag}>"
        inner = "\n".join(c.to_xml(level + 1) for c in self.children)
        return f"{pad}<{self.tag}{attrs}>\n{inner}\n{pad}</{self.tag}>"

    def __repr__(self) -> str:
        return f"Node({self.tag!r}, {self.attrs!r}, <{len(self.children)} children>)"

    def as_tuple(self):
        """Canonical form used for comparisons / round-trip tests."""
        return (self.tag, tuple(self.attrs.items()),
                tuple(c.as_tuple() for c in self.children), self.text.strip())


def n(tag, attrs=None, children=None, text=""):
    """Short constructor used by generated modules."""
    return Node(tag, attrs, children, text)
