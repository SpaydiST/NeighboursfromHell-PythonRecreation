# -*- coding: utf-8 -*-
# Generated from menuleft_bar.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('dialog', {'gfx': 'gui/ingame/interface_bar_dialog.tga', 'offset': '85/482'}, [
        n('progressbar', {'name': 'rageometer', 'offset': '0/4', 'direction': 'vertical'}, [
            n('image', {'name': 'back', 'gfx': 'gui/ingame/interface_bar_back.tga'}),
            n('image', {'name': 'front', 'gfx': 'gui/ingame/interface_bar_front.tga'}),
            n('range', {'min': '0', 'max': '100', 'steps': '100'}),
        ]),
    ]),
]
