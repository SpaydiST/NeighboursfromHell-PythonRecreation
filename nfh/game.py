"""Game core settings from game.xml (window title, save-game location)."""
from __future__ import annotations
import os
import sys
from dataclasses import dataclass
from typing import List

from . import data


@dataclass
class GameConfig:
    title: str              # window title ("Neighbours From Hell")
    appdata_path: str       # folder created inside the user's Documents folder ("JoWooD")
    appdata_folder: str     # sub-folder holding this game's saves ("NFH1")

    def documents_dir(self) -> str:
        home = os.path.expanduser("~")
        if sys.platform.startswith("win"):
            try:                                   # real "Documents" location, even if redirected
                import ctypes
                from ctypes import wintypes
                buf = ctypes.create_unicode_buffer(wintypes.MAX_PATH)
                if ctypes.windll.shell32.SHGetFolderPathW(None, 5, None, 0, buf) == 0:
                    return buf.value
            except Exception:
                pass
        return os.path.join(home, "Documents")

    def save_dir(self, create: bool = False) -> str:
        """<Documents>/<appdata_path>/<appdata_folder>"""
        p = os.path.join(self.documents_dir(), self.appdata_path, self.appdata_folder)
        if create:
            os.makedirs(p, exist_ok=True)
        return p

    def save_files(self) -> List[str]:
        d = self.save_dir()
        return sorted(os.listdir(d)) if os.path.isdir(d) else []


def load_game() -> GameConfig:
    root = data.load("game")[0]
    return GameConfig(root.find("title")["value"],
                      root.find("appdata")["path"], root.find("appdata")["folder"])
