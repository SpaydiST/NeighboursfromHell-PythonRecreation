"""python -m nfh  -> overview of all levels, optional asset check and level renders.

    python -m nfh [--png NFH1_folder] [--tga gfxdata_folder] [--sfx sfxdata_folder] [--render out_dir]
"""
import argparse
import os
import sys

if __package__ in (None, ""):          # started as "python nfh/__main__.py" -> make `nfh` importable
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nfh import level_sets, load_level
from nfh.assets import SpriteBank, SoundBank


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--png", help="folder with PNG sprites")
    ap.add_argument("--tga", help="folder with the original .tga sprites")
    ap.add_argument("--sfx", help="folder with the sounds")
    ap.add_argument("--render", help="write one picture per level into this folder")
    a = ap.parse_args()
    sprites = SpriteBank(a.png, a.tga) if (a.png or a.tga) else None
    sounds = SoundBank(a.sfx) if a.sfx else None
    from nfh import load_game
    g = load_game()
    print(f"{g.title}  | saves: {g.save_dir()}")
    if a.render:
        os.makedirs(a.render, exist_ok=True)
    for s in level_sets():
        print(f"== {s.name} ({s.state})")
        for li in s.levels:
            L = load_level(li.name)
            rooms = len(L.layout.rooms) if L.layout else 0
            line = (f"  {li.name:16} rooms={rooms:2} objects={len(L.objects):3} anims={len(L.anims):3} "
                    f"tricks={len(L.tricks):2} combos={len(L.combinations):2} strings={len(L.strings):3}")
            if sprites:
                line += f" missing_sprites={len(sprites.missing(L))}"
            if sounds:
                line += f" missing_sounds={len(sounds.missing(f for f, _ in L.sfx))}"
            print(line)
            if sprites and a.render and L.layout:
                from nfh.render import render_level
                render_level(L, sprites).convert("RGB").save(os.path.join(a.render, li.name + ".jpg"), quality=88)


main()
