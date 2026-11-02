"""Use `load("level_pig/anims")` to get the list of root `Node`s of that file."""

import importlib
from typing import List
from ..node import Node


def load(path: str) -> List[Node]:
    mod = importlib.import_module("nfh.data." + path.replace("\\", "/").replace("/", "."))
    return mod.ROOTS
