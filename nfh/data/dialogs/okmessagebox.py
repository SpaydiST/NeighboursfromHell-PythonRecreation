# -*- coding: utf-8 -*-
# Generated from okmessagebox.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('resizedialog', {}, [
        n('top', {'gfx': 'gui/ingame/messagebox_top.tga'}, [
            n('animation', {'name': 'head', 'offset': '175/0'}, [
                n('image', {'gfx': 'gui/ingame/mb_head_02.tga'}),
                n('image', {'gfx': 'gui/ingame/mb_head_03.tga'}),
                n('image', {'gfx': 'gui/ingame/mb_head_04.tga'}),
                n('image', {'gfx': 'gui/ingame/mb_head_05.tga'}),
                n('image', {'gfx': 'gui/ingame/mb_head_06.tga'}),
                n('image', {'gfx': 'gui/ingame/mb_head_07.tga'}),
                n('image', {'gfx': 'gui/ingame/mb_head_08.tga'}),
                n('image', {'gfx': 'gui/ingame/mb_head_09.tga'}),
                n('image', {'gfx': 'gui/ingame/mb_head_10.tga'}),
                n('image', {'gfx': 'gui/ingame/mb_head_09.tga'}),
                n('image', {'gfx': 'gui/ingame/mb_head_08.tga'}),
                n('image', {'gfx': 'gui/ingame/mb_head_07.tga'}),
                n('image', {'gfx': 'gui/ingame/mb_head_06.tga'}),
                n('image', {'gfx': 'gui/ingame/mb_head_05.tga'}),
                n('image', {'gfx': 'gui/ingame/mb_head_04.tga'}),
                n('image', {'gfx': 'gui/ingame/mb_head_03.tga'}),
                n('image', {'gfx': 'gui/ingame/mb_head_02.tga'}),
                n('image', {'gfx': 'gui/ingame/mb_head_01.tga'}),
                n('image', {'gfx': 'gui/ingame/mb_head_01.tga'}),
                n('image', {'gfx': 'gui/ingame/mb_head_01.tga'}),
                n('image', {'gfx': 'gui/ingame/mb_head_01.tga'}),
                n('image', {'gfx': 'gui/ingame/mb_head_01.tga'}),
                n('image', {'gfx': 'gui/ingame/mb_head_01.tga'}),
                n('image', {'gfx': 'gui/ingame/mb_head_00.tga'}),
                n('image', {'gfx': 'gui/ingame/mb_head_01.tga'}),
                n('image', {'gfx': 'gui/ingame/mb_head_01.tga'}),
                n('image', {'gfx': 'gui/ingame/mb_head_00.tga'}),
                n('image', {'gfx': 'gui/ingame/mb_head_01.tga'}),
                n('image', {'gfx': 'gui/ingame/mb_head_01.tga'}),
                n('image', {'gfx': 'gui/ingame/mb_head_01.tga'}),
                n('image', {'gfx': 'gui/ingame/mb_head_01.tga'}),
                n('image', {'gfx': 'gui/ingame/mb_head_01.tga'}),
                n('image', {'gfx': 'gui/ingame/mb_head_01.tga'}),
            ]),
        ]),
        n('mid', {'gfx': 'gui/ingame/messagebox_mid.tga'}, [
            n('text', {'name': 'text', 'offset': '28/0', 'size': '385/500', 'halign': 'center', 'valign': 'top', 'resize': 'true'}, [
                n('font', {'name': 'mb_normal'}),
            ]),
        ]),
        n('bottom', {'gfx': 'gui/ingame/messagebox_low.tga'}, [
            n('button', {'name': 'ok', 'offset': '375/18'}, [
                n('image', {'name': 'std', 'gfx': 'gui/ingame/messagebox_ok_std.tga'}),
                n('image', {'name': 'hover', 'gfx': 'gui/ingame/messagebox_ok_hover.tga'}),
                n('image', {'name': 'down', 'gfx': 'gui/ingame/messagebox_ok_pressed.tga'}),
                n('sfx', {'name': 'hover', 'file': 'sfx/but_hover1.wav'}),
                n('sfx', {'name': 'down', 'file': 'sfx/but1.wav'}),
            ]),
        ]),
    ]),
]
