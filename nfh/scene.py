"""Playable scene built from a level: entities with animation playback, room rectangles, doors.

No pygame in here, so it can be tested headless.

Position rules (derived from the data):
  * objects / doors : room.offset + placement.position + sprite offset from gfxdata
  * actors          : the same, minus the actor's foot hotspot (the position is where the feet stand)
  * level-wide objects (the house picture) use (0, 0) as room offset
Sprites and animations are keyed by the *gfx key* of the object definition (``objects.xml`` ``gfx=``),
e.g. placement ``anc/fro`` -> key ``doorright``; if there is no definition the placement name is the key.
"""
from __future__ import annotations
from typing import Callable, Dict, List, Optional, Tuple

from . import load_level
from .model import Animation, LevelData, Placement, Room

IDLE_NAMES = ("ms", "ms1", "ms2", "ms3", "std", "stand")
Pt = Tuple[int, int]


class Entity:
    def __init__(self, scene: "Scene", p: Placement, room: Optional[Room], order: int):
        lv = scene.level
        self.scene, self.p, self.room, self.order = scene, p, room, order
        self.name, self.kind, self.layer = p.name, p.kind, p.layer
        self.defn = lv.objects.get(p.name)
        self.key = (self.defn.gfx if self.defn and self.defn.gfx else p.name)
        self.ao = lv.anims.get(self.key)
        self.files = {g.image.lower(): g.offset for g in lv.gfx.get(self.key, [])}
        ox, oy = room.offset[:2] if room else (0, 0)
        px, py = (p.position or (0, 0))[:2]
        self.origin: Pt = (ox + px, oy + py)
        hot = self.defn.hotspot if (self.defn and self.kind == "actor" and self.defn.hotspot) else (0, 0)
        self.origin = (self.origin[0] - hot[0], self.origin[1] - hot[1])
        self.visible = p.visible
        self.twin: Optional["Entity"] = None       # door <-> its "_dummy" (closed door picture)
        self.dummy: Optional["Entity"] = None
        self.cur: Optional[Animation] = None
        self.i = 0
        self.playing = False                       # a user-triggered (non-idle) animation is running
        self.audible = False                       # idle-loop sounds are played too (Woody's footsteps)
        self.on_done: Optional[Callable[[], None]] = None
        self.last_gfx: Optional[str] = None
        self.idle = self._pick_idle()
        self._set_idle()
        if self.last_gfx is None:                  # no idle animation: show first sprite of anything
            self.last_gfx = self._fallback_gfx()

    # ---- animation bookkeeping
    @property
    def animations(self) -> Dict[str, Animation]:
        return self.ao.animations if self.ao else {}

    def _pick_idle(self) -> Optional[str]:
        a = self.animations
        if self.p.animation in a:
            return self.p.animation
        for n in IDLE_NAMES:
            if n in a:
                return n
        return None

    def _fallback_gfx(self) -> Optional[str]:
        for an in self.animations.values():
            for f in an.frames:
                if f.gfx:
                    return f.gfx
        files = self.scene.level.gfx.get(self.key)
        return files[0].image if files else None

    def _set_idle(self):
        self.playing = False
        self.on_done = None
        if self.idle:
            self.cur, self.i = self.animations[self.idle], 0
            self._enter_frame()
        else:
            self.cur = None

    def _enter_frame(self):
        f = self.cur.frames[self.i] if self.cur and self.cur.frames else None
        if f is None:
            return
        if f.gfx:
            self.last_gfx = f.gfx
        if f.sfx:
            self.scene.events.append((self, f.sfx, self.playing or self.audible))

    def play(self, name: str, on_done: Optional[Callable[[], None]] = None) -> bool:
        a = self.animations.get(name)
        if a is None or not a.frames:
            return False
        self.cur, self.i, self.on_done = a, 0, on_done
        self.playing = name != self.idle
        self._enter_frame()
        return True

    def stop(self):
        self._set_idle()

    def set_loop(self, name: str):
        """Change the looping 'idle' animation (stand / walk) without interrupting a one-shot."""
        if name not in self.animations or (self.idle == name and self.cur is self.animations[name]):
            return
        self.idle = name
        if not self.playing:
            self._set_idle()

    def move_to(self, room: Optional[Room], x: float, y: float):
        """Put an actor with its feet at room-local (x, y)."""
        self.room = room
        hot = self.defn.hotspot if (self.defn and self.defn.hotspot) else (0, 0)
        ox, oy = room.offset[:2] if room else (0, 0)
        self.origin = (ox + x - hot[0], oy + y - hot[1])

    def tick(self):
        if not self.cur or not self.cur.frames:
            return
        self.i += 1
        if self.i >= len(self.cur.frames):
            if self.cur.type == "oneshot" and self.playing:
                cb = self.on_done
                self._set_idle()
                if cb:
                    cb()
                return
            self.i = 0
        self._enter_frame()

    # ---- drawing info
    def drawn(self) -> bool:
        if self.dummy and self.dummy.playing:      # the real door animates -> hide closed-door picture
            return False
        return self.visible or self.playing

    def sprite(self) -> Optional[Tuple[str, Pt]]:
        """(image name, top-left in house coordinates) of the current frame."""
        if not self.last_gfx:
            return None
        ox, oy = self.files.get(self.last_gfx.lower(), (0, 0))[:2]
        return self.last_gfx, (self.origin[0] + ox, self.origin[1] + oy)


class Scene:
    def __init__(self, level_name: str):
        self.level: LevelData = load_level(level_name)
        self.name = level_name
        self.layout = self.level.layout
        if self.layout is None:
            raise ValueError(f"{level_name} has no layout")
        self.size: Pt = tuple(self.layout.size[:2])
        self.events: List[Tuple[Entity, str, bool]] = []
        self.volumes: Dict[str, int] = {}
        for f, v in self.level.sfx:
            if v:
                self.volumes[f.lower()] = int(v)
        self.entities: List[Entity] = []
        order = 0
        for p in self.layout.placements:
            self.entities.append(Entity(self, p, None, order)); order += 1
        for room in self.layout.rooms.values():
            for p in room.placements:
                self.entities.append(Entity(self, p, room, order)); order += 1
        self.by_name: Dict[str, Entity] = {}
        for e in self.entities:
            self.by_name.setdefault(e.name, e)
        for e in self.entities:                    # pair "x/y" with "x/y_dummy"
            if e.name.endswith("_dummy") and e.name[:-6] in self.by_name:
                twin = self.by_name[e.name[:-6]]
                e.twin, twin.dummy = twin, e
        self.draw_order = sorted(self.entities, key=lambda e: (e.layer, e.order))
        self.room_names = list(self.layout.rooms)

    # ---- rooms
    def room_entities(self, room: str) -> List[Entity]:
        return [e for e in self.entities if e.room is not None and e.room.name == room]

    def room_rect(self, room: str, margin: int = 0) -> Tuple[int, int, int, int]:
        """The room's cut-away in house coordinates (x, y, w, h), from its floor areas."""
        r = self.layout.rooms[room]
        if r.floors:
            x0 = min(f.offset[0] for f in r.floors)
            y0 = min(f.offset[1] for f in r.floors)
            x1 = max(f.offset[0] + f.size[0] for f in r.floors)
            y1 = max(f.offset[1] + f.size[1] for f in r.floors)
        else:
            x0, y0, x1, y1 = 0, 0, 950, 460
        return (r.offset[0] + x0 - margin, r.offset[1] + y0 - margin,
                x1 - x0 + 2 * margin, y1 - y0 + 2 * margin)

    def room_extent(self, room: str) -> Tuple[int, int, int, int]:
        """room_rect widened to the whole walkable path (the front yard is much wider than its cut-away)."""
        x, y, w, h = self.room_rect(room)
        r = self.layout.rooms[room]
        px0 = r.offset[0] + min(r.path1[0], r.path2[0]) - 60
        px1 = r.offset[0] + max(r.path1[0], r.path2[0]) + 60
        x0, x1 = min(x, px0), max(x + w, px1)
        return (x0, y, x1 - x0, h)

    @property
    def woody(self) -> Optional[Entity]:
        return next((e for e in self.entities if e.kind == "actor" and e.name == "woody"), None)

    def stand_point(self, e: Entity, out: bool = False) -> Optional[Tuple[int, int]]:
        """Room-local spot where Woody stands to use an object / door (None if the data has none)."""
        hs = e.defn.hotspots if e.defn else {}
        h = hs.get("woody_out") if out and "woody_out" in hs else hs.get("woody")
        if not h or tuple(h[:2]) == (0, 0):
            return None
        px, py = (e.p.position or (0, 0))[:2]
        return (px + h[0], py + h[1])

    def doors(self, room: str) -> List[Tuple[object, Entity]]:
        """[(Neighbor, door entity)] of a room."""
        out = []
        for nb in self.layout.rooms[room].neighbors:
            d = self.by_name.get(nb.doorin)
            if d is not None:
                out.append((nb, d))
        return out

    def default_room(self) -> str:
        for cand in ("anc",):
            if cand in self.layout.rooms:
                return cand
        return self.room_names[0]

    def selectable(self, room: str) -> List[Entity]:
        """Things in a room that have animations to play (house picture and dummies excluded)."""
        return [e for e in self.room_entities(room)
                if e.animations and e.twin is None and e.name != "house"]

    # ---- time
    def step(self, n: int = 1):
        for _ in range(n):
            for e in list(self.entities):
                e.tick()

    def pop_events(self) -> List[Tuple[Entity, str, bool]]:
        ev, self.events = self.events, []
        return ev

    def volume(self, sfx: str) -> float:
        return self.volumes.get(sfx.lower(), 100) / 100.0
