"""Woody's movement ("physics") and the scrolling camera - pygame-free.

Movement follows the game data:
  * rooms have a walking line (``path1``..``path2``) and floor areas that give the depth range,
  * ``woody``'s ``<speed name="mg1" speed="17" start="12">``: a gait starts at `start` px per tick and
    accelerates up to `speed`; it brakes before the target so he stops smoothly,
  * four facings: 0 up, 1 left, 2 down, 3 right  ->  animations ms<N> (stand), mg<N> (walk), sn<N> (sneak).
    (The data does not say which of 1 / 3 is left; ``swap_lr`` flips them if your sprites look mirrored.)
One tick = one animation frame.
"""
from __future__ import annotations
import math
from typing import Callable, Optional, Tuple

ACC, DEC, MIN_V = 1.0, 2.5, 2.0               # px / tick^2 up, px / tick^2 braking, creep speed
FACE_INDEX = {"up": 0, "left": 1, "down": 2, "right": 3}


class Walker:
    def __init__(self, scene, entity):
        self.scene, self.e = scene, entity
        self.room = entity.room
        self.x, self.y = (entity.p.position or (0, 0))[:2]
        self.x, self.y = float(self.x), float(self.y)
        self.v = 0.0
        self.face = "down"
        self.axis = "h"
        self.gait = "walk"                      # walk -> mgN, sneak -> snN
        self.swap_lr = False
        self.target: Optional[Tuple[float, float]] = None
        self.on_arrive: Optional[Callable[[], None]] = None
        self.params = {k: (float(v.get("speed", 0)), float(v.get("start", 0)))
                       for k, v in (entity.defn.speeds.items() if entity.defn else [])}
        entity.audible = True
        self._sync()

    # ---- helpers
    def _idx(self, face: str) -> int:
        i = FACE_INDEX[face]
        if self.swap_lr and i in (1, 3):
            i = 4 - i
        return i

    def _anim(self, prefix: str):
        name = f"{prefix}{self._idx(self.face)}"
        if name not in self.e.animations and prefix != "ms":
            name = f"mg{self._idx(self.face)}"
        self.e.set_loop(name)
        return name

    def _sync(self):
        self.e.move_to(self.room, self.x, self.y)
        self._anim("ms")

    def limits(self, room=None) -> Tuple[float, float, float, float]:
        """(xmin, xmax, ymin, ymax) Woody may be clicked to inside `room`."""
        r = room or self.room
        xs = sorted((r.path1[0], r.path2[0]))
        py = r.path1[1]
        flo = [f for f in r.floors if not f.wall]
        y0 = min([f.offset[1] for f in flo] + [py])
        y1 = max([f.offset[1] + f.size[1] for f in flo] + [py])
        if not flo:
            y0 = y1 = py
        return xs[0], xs[1], y0, y1

    @property
    def moving(self) -> bool:
        return self.target is not None

    @property
    def world(self) -> Tuple[float, float]:
        return self.room.offset[0] + self.x, self.room.offset[1] + self.y

    # ---- commands
    def place(self, room_name: str, x: float, y: float, face: str = "down"):
        self.room = self.scene.layout.rooms[room_name]
        self.x, self.y, self.v, self.target, self.on_arrive = float(x), float(y), 0.0, None, None
        self.face = face
        self._sync()

    def goto(self, x: float, y: float, on_arrive: Optional[Callable[[], None]] = None, clamp: bool = True):
        if clamp:
            x0, x1, y0, y1 = self.limits()
            x, y = min(max(x, x0), x1), min(max(y, y0), y1)
        self.target, self.on_arrive = (float(x), float(y)), on_arrive
        dx, dy = x - self.x, y - self.y
        self.axis = "h" if abs(dx) >= abs(dy) else "v"
        if math.hypot(dx, dy) < 0.5:               # already there
            self._arrive()

    def turn(self, face: str):
        self.face = face
        self._anim("ms")

    def stop(self):
        self.target, self.on_arrive, self.v = None, None, 0.0
        self._anim("ms")

    def _arrive(self):
        if self.target:
            self.x, self.y = self.target
        cb = self.on_arrive
        self.target, self.on_arrive, self.v = None, None, 0.0
        self.e.move_to(self.room, self.x, self.y)
        self._anim("ms")
        if cb:
            cb()

    # ---- one physics tick
    def tick(self):
        if self.e.playing:                          # a one-shot (door, 'smile' ...) owns the sprite
            return
        if self.target is None:
            self._anim("ms")
            return
        tx, ty = self.target
        dx, dy = tx - self.x, ty - self.y
        dist = math.hypot(dx, dy)
        if dist < 0.5:
            self._arrive()
            return
        ax, ay = abs(dx), abs(dy)
        if self.axis == "h" and ay > ax * 1.5:
            self.axis = "v"
        elif self.axis == "v" and ax > ay * 1.5:
            self.axis = "h"
        self.face = (("left" if dx < 0 else "right") if self.axis == "h"
                     else ("up" if dy < 0 else "down"))
        name = self._anim("sn" if self.gait == "sneak" else "mg")
        speed, start = self.params.get(name, (6.0, 0.0))
        if self.v <= 0:
            self.v = max(start, 1.0)
        if dist <= self.v * self.v / (2 * DEC) + self.v:
            self.v = max(MIN_V, self.v - DEC)       # brake
        else:
            self.v = min(speed or 6.0, self.v + ACC)
        self.v = min(self.v, speed or 6.0)
        step = min(self.v, dist)
        self.x += dx / dist * step
        self.y += dy / dist * step
        self.e.move_to(self.room, self.x, self.y)
        if step >= dist - 1e-6:
            self._arrive()


class Camera:
    """Top-left corner (x, y) of the view in world coordinates, plus zoom; edge scrolling like the original."""
    EDGE = 40            # px band at the view border that scrolls
    SPEED = 900.0        # screen px per second at the very edge

    def __init__(self):
        self.x = self.y = 0.0
        self.zoom = 1.0
        self.goal: Optional[Tuple[float, float]] = None

    def center_on(self, wx: float, wy: float, vw: int, vh: int, smooth: bool = True):
        gx, gy = wx - vw / self.zoom / 2, wy - vh / self.zoom / 2
        if smooth:
            self.goal = (gx, gy)
        else:
            self.x, self.y, self.goal = gx, gy, None

    def set_zoom(self, z: float, anchor_wx: float, anchor_wy: float, fx: float, fy: float):
        """Zoom keeping world point (anchor) under the same screen fraction (fx, fy) of the view."""
        z = min(2.5, max(0.3, z))
        self.x, self.y = anchor_wx - fx / z, anchor_wy - fy / z
        self.zoom = z
        self.goal = None

    def edge_velocity(self, mx: int, my: int, view) -> Tuple[float, float]:
        """-1..1 per axis from the mouse position inside view=(x, y, w, h)."""
        x, y, w, h = view
        if not (x <= mx < x + w and y <= my < y + h):
            return 0.0, 0.0

        def axis(p, lo, size):
            if p < lo + self.EDGE:
                return -(1 - (p - lo) / self.EDGE)
            if p >= lo + size - self.EDGE:
                return 1 - (lo + size - 1 - p) / self.EDGE
            return 0.0
        return axis(mx, x, w), axis(my, y, h)

    def update(self, dt: float, bounds, vw: int, vh: int, vel: Tuple[float, float] = (0, 0)):
        if vel != (0, 0):
            self.goal = None
            self.x += vel[0] * self.SPEED * dt / self.zoom
            self.y += vel[1] * self.SPEED * dt / self.zoom
        elif self.goal:
            k = min(1.0, dt * 6)
            self.x += (self.goal[0] - self.x) * k
            self.y += (self.goal[1] - self.y) * k
            if abs(self.goal[0] - self.x) < 0.5 and abs(self.goal[1] - self.y) < 0.5:
                self.goal = None
        self.clamp(bounds, vw, vh)

    def clamp(self, bounds, vw: int, vh: int, margin: int = 60):
        x0, y0, x1, y1 = bounds
        w, h = vw / self.zoom, vh / self.zoom
        lo_x, hi_x = x0 - margin, x1 + margin - w
        lo_y, hi_y = y0 - margin, y1 + margin - h
        self.x = (lo_x + hi_x) / 2 if lo_x > hi_x else min(max(self.x, lo_x), hi_x)
        self.y = (lo_y + hi_y) / 2 if lo_y > hi_y else min(max(self.y, lo_y), hi_y)
