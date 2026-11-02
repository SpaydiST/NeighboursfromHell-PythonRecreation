# -*- coding: utf-8 -*-
# Generated from victory_gold_dlg.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('dialog', {'gfx': 'gui/main/endscreen_gold.tga', 'offset': '0/0'}, [
        n('text', {'name': 'victory1shadow', 'offset': '3/67', 'size': '720/60', 'valign': 'center', 'halign': 'right', 'color': '0/0/0'}, [
            n('font', {'name': 'victory_big'}),
            n('caption', {'text': 'victory_gold_title'}),
        ]),
        n('text', {'name': 'victory1', 'offset': '0/65', 'size': '720/60', 'valign': 'center', 'halign': 'right', 'color': '255/255/255'}, [
            n('font', {'name': 'victory_big'}),
            n('caption', {'text': 'victory_gold_title'}),
        ]),
        n('text', {'name': 'victory2shadow', 'offset': '463/172', 'size': '300/550', 'valign': 'top', 'halign': 'center', 'color': '0/0/0', 'multiline': 'true'}, [
            n('font', {'name': 'victory_small'}),
            n('caption', {'text': 'victory_gold'}),
        ]),
        n('text', {'name': 'victory2', 'offset': '460/170', 'size': '300/550', 'valign': 'top', 'halign': 'center', 'color': '255/255/255', 'multiline': 'true'}, [
            n('font', {'name': 'victory_small'}),
            n('caption', {'text': 'victory_gold'}),
        ]),
    ]),
]
