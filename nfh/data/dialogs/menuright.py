# -*- coding: utf-8 -*-
# Generated from menuright.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('dialog', {'gfx': 'gui/ingame/interface_right.tga', 'offset': '581/471'}, [
        n('text', {'name': 'time', 'offset': '84/20', 'size': '90/29', 'valign': 'center', 'halign': 'center', 'color': '122/182/182'}, [
            n('font', {'name': 'ingame_time'}),
            n('caption', {'text': 'notimelimit'}),
        ]),
        n('text', {'name': 'bonus', 'offset': '60/70', 'size': '56/20', 'valign': 'bottom', 'halign': 'right', 'color': '255/160/0'}, [
            n('font', {'name': 'ingame_quotachange'}),
        ]),
        n('text', {'name': 'bonuspercent', 'offset': '116/58', 'size': '16/30', 'valign': 'bottom', 'halign': 'right', 'color': '255/160/0'}, [
            n('font', {'name': 'ingame_change_percent'}),
        ]),
        n('text', {'name': 'changepercent', 'offset': '116/58', 'size': '16/30', 'valign': 'bottom', 'halign': 'right', 'color': '240/240/0'}, [
            n('font', {'name': 'ingame_change_percent'}),
        ]),
        n('text', {'name': 'quotachange', 'offset': '60/70', 'size': '56/20', 'valign': 'bottom', 'halign': 'right', 'color': '240/240/0'}, [
            n('font', {'name': 'ingame_quotachange'}),
        ]),
        n('text', {'name': 'quota', 'offset': '65/85', 'size': '52/34', 'valign': 'bottom', 'halign': 'right', 'color': '255/255/255'}, [
            n('font', {'name': 'ingame_quota'}),
        ]),
        n('text', {'name': 'percent', 'offset': '118/85', 'size': '16/32', 'valign': 'bottom', 'halign': 'right', 'color': '255/255/255'}, [
            n('font', {'name': 'ingame_percent'}),
            n('caption', {'text': 'percent'}),
        ]),
        n('text', {'name': 'bonuscount', 'offset': '163/96', 'size': '47/29', 'valign': 'center', 'halign': 'center', 'color': '255/160/0'}, [
            n('font', {'name': 'ingame_menu_medium'}),
        ]),
        n('text', {'name': 'trickcount', 'offset': '163/62', 'size': '49/29', 'valign': 'center', 'halign': 'center', 'color': '240/240/0'}, [
            n('font', {'name': 'ingame_menu_medium'}),
        ]),
        n('button', {'name': 'info', 'offset': '167/20'}, [
            n('image', {'name': 'std', 'gfx': 'gui/ingame/mission_normal.tga'}),
            n('image', {'name': 'hover', 'gfx': 'gui/ingame/mission_hover.tga'}),
            n('image', {'name': 'down', 'gfx': 'gui/ingame/mission_pressed.tga'}),
            n('sfx', {'name': 'hover', 'file': 'sfx/but_hover1.wav'}),
            n('sfx', {'name': 'down', 'file': 'sfx/but1.wav'}),
        ]),
    ]),
]
