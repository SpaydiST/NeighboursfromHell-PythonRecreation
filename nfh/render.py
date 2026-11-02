"""Draw a World (or a still picture of a level) with Pillow - no pygame needed."""
from __future__ import annotations
from typing import Optional, Tuple

from .assets import SpriteBank
from .engine import World


def render_world(world: World, rect: Optional[Tuple[int, int, int, int]] = None,
                 background=(30, 30, 30, 255)):
    """Return a PIL RGBA image of `rect` (x, y, w, h in level coordinates; default: whole level)."""
    from PIL import Image
    if rect is None:
        rect = (0, 0) + tuple(world.level.layout.size)
    rx, ry, rw, rh = (int(v) for v in rect)
    canvas = Image.new("RGBA", (rw, rh), background)
    for e in world.draw_order():
        s = e.sprite()
        if s is None:
            continue
        img = world.bank.get(s[0], s[1])
        if img is None:
            continue
        x, y = int(round(s[2][0])) - rx, int(round(s[2][1])) - ry
        if x >= rw or y >= rh or x + img.width <= 0 or y + img.height <= 0:
            continue
        # clip to the canvas
        sx0, sy0 = max(0, -x), max(0, -y)
        sx1, sy1 = min(img.width, rw - x), min(img.height, rh - y)
        part = img.crop((sx0, sy0, sx1, sy1))
        canvas.alpha_composite(part, (x + sx0, y + sy0))
    return canvas


def render_level(level, bank: SpriteBank, rect=None):
    """Still picture of a LevelData at its starting state."""
    return render_world(World(level, bank), rect)
