# -*- coding: utf-8 -*-
# Generated from gameover.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('dialog', {'gfx': 'gui/ingame/abrechnungsscreen.tga', 'offset': '125/70'}, [
        n('text', {'name': 'rating', 'offset': '168/118', 'size': '349/42', 'halign': 'center', 'valign': 'center', 'color': '75/255/0'}, [
            n('font', {'name': 'gameover_big'}),
        ]),
        n('text', {'name': 'trickstext', 'offset': '168/185', 'size': '349/20', 'halign': 'center', 'valign': 'bottom', 'color': '75/255/0'}, [
            n('font', {'name': 'gameover_small'}),
        ]),
        n('text', {'name': 'tricks', 'offset': '168/200', 'size': '349/42', 'halign': 'center', 'valign': 'center', 'color': '75/255/0'}, [
            n('font', {'name': 'gameover_verybig'}),
        ]),
        n('text', {'name': 'quotatext', 'offset': '168/245', 'size': '349/20', 'halign': 'center', 'valign': 'bottom', 'color': '75/255/0'}, [
            n('font', {'name': 'gameover_small'}),
        ]),
        n('text', {'name': 'quota', 'offset': '168/260', 'size': '184/42', 'halign': 'right', 'valign': 'bottom', 'color': '75/255/0'}, [
            n('font', {'name': 'gameover_verybig'}),
        ]),
        n('text', {'name': 'percent', 'offset': '352/260', 'size': '23/40', 'halign': 'left', 'valign': 'bottom', 'color': '75/255/0'}, [
            n('font', {'name': 'gameover_percent'}),
            n('caption', {'text': 'percent'}),
        ]),
        n('button', {'name': 'restart', 'offset': '190/312'}, [
            n('font', {'name': 'options_small'}),
            n('image', {'name': 'std', 'gfx': 'gui/main/choice_norm.tga', 'text': 'gameover_restart', 'color': '75/255/0'}),
            n('image', {'name': 'hover', 'gfx': 'gui/main/choice_hov.tga', 'text': 'gameover_restart', 'color': '255/255/0'}),
            n('image', {'name': 'down', 'gfx': 'gui/main/choice_hov.tga', 'text': 'gameover_restart', 'color': '255/255/0'}),
            n('sfx', {'name': 'hover', 'file': 'sfx/but_hover1.wav'}),
            n('sfx', {'name': 'down', 'file': 'sfx/but1.wav'}),
        ]),
        n('button', {'name': 'ok', 'offset': '342/312'}, [
            n('font', {'name': 'options_small'}),
            n('image', {'name': 'std', 'gfx': 'gui/main/choice_norm.tga', 'text': 'gameover_continue', 'color': '75/255/0'}),
            n('image', {'name': 'hover', 'gfx': 'gui/main/choice_hov.tga', 'text': 'gameover_continue', 'color': '255/255/0'}),
            n('image', {'name': 'down', 'gfx': 'gui/main/choice_hov.tga', 'text': 'gameover_continue', 'color': '255/255/0'}),
            n('sfx', {'name': 'hover', 'file': 'sfx/but_hover1.wav'}),
            n('sfx', {'name': 'down', 'file': 'sfx/but1.wav'}),
        ]),
    ]),
]
