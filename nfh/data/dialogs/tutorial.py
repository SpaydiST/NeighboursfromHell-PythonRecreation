# -*- coding: utf-8 -*-
# Generated from tutorial.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('resizedialog', {'offset': '101/0'}, [
        n('top', {'gfx': 'gui/ingame/tutorial_top.tga'}),
        n('mid', {'gfx': 'gui/ingame/tutorial_center.tga'}, [
            n('text', {'name': 'text', 'offset': '28/-56', 'size': '648/200', 'halign': 'left', 'valign': 'top', 'color': '255/255/255', 'resize': 'true'}, [
                n('font', {'name': 'mb_tutorial'}),
            ]),
        ]),
        n('bottom', {'gfx': 'gui/ingame/tutorial_bottom.tga'}),
    ]),
]
