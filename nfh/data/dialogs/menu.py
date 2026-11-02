# -*- coding: utf-8 -*-
# Generated from menu.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('dialog', {'gfx': 'gui/ingame/interface_center.tga', 'offset': '123/511'}, [
        n('text', {'name': 'text', 'offset': '8/1', 'size': '520/24', 'valign': 'center', 'halign': 'left', 'color': '255/255/255'}, [
            n('font', {'name': 'ingame_info'}),
        ]),
        n('button', {'name': 'left', 'offset': '0/36'}, [
            n('image', {'name': 'std', 'gfx': 'gui/ingame/scroll_left_std.tga'}),
            n('image', {'name': 'hover', 'gfx': 'gui/ingame/scroll_left_hover.tga'}),
            n('image', {'name': 'down', 'gfx': 'gui/ingame/scroll_left_pressed.tga'}),
        ]),
        n('button', {'name': 'right', 'offset': '422/36'}, [
            n('image', {'name': 'std', 'gfx': 'gui/ingame/scroll_right_std.tga'}),
            n('image', {'name': 'hover', 'gfx': 'gui/ingame/scroll_right_hover.tga'}),
            n('image', {'name': 'down', 'gfx': 'gui/ingame/scroll_right_pressed.tga'}),
        ]),
        n('button', {'name': 'inv00', 'offset': '41/26'}),
        n('button', {'name': 'inv01', 'offset': '116/26'}),
        n('button', {'name': 'inv02', 'offset': '191/26'}),
        n('button', {'name': 'inv03', 'offset': '266/26'}),
        n('button', {'name': 'inv04', 'offset': '341/26'}),
    ]),
]
