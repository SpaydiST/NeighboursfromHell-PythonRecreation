# -*- coding: utf-8 -*-
# Generated from container.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('dialog', {'gfx': 'gui/ingame/inventar.tga', 'offset': '316/150'}, [
        n('text', {'name': 'caption', 'offset': '20/10', 'size': '186/26', 'halign': 'center', 'valign': 'center'}, [
            n('font', {'name': 'std14'}),
        ]),
        n('button', {'name': 'ok', 'offset': '96/166'}, [
            n('image', {'name': 'std', 'gfx': 'gui/ingame/inventar_close_std.tga'}),
            n('image', {'name': 'hover', 'gfx': 'gui/ingame/inventar_close_hover.tga'}),
            n('image', {'name': 'down', 'gfx': 'gui/ingame/inventar_close_pressed.tga'}),
        ]),
        n('button', {'name': 'con01', 'offset': '39/45'}),
        n('button', {'name': 'con02', 'offset': '104/45'}),
        n('button', {'name': 'con03', 'offset': '39/102'}),
        n('button', {'name': 'con04', 'offset': '104/102'}),
    ]),
]
