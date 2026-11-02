# -*- coding: utf-8 -*-
# Generated from victorydlg.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('dialog', {'gfx': 'gui/main/endscreen_default.tga', 'offset': '0/0'}, [
        n('text', {'name': 'victory1shadow', 'offset': '3/67', 'size': '720/60', 'valign': 'center', 'halign': 'right', 'color': '0/0/0'}, [
            n('font', {'name': 'victory_big'}),
            n('caption', {'text': 'victory_default_title'}),
        ]),
        n('text', {'name': 'victory1', 'offset': '0/65', 'size': '720/60', 'valign': 'center', 'halign': 'right', 'color': '255/255/255'}, [
            n('font', {'name': 'victory_big'}),
            n('caption', {'text': 'victory_default_title'}),
        ]),
        n('text', {'name': 'victory2shadow', 'offset': '513/172', 'size': '250/550', 'valign': 'top', 'halign': 'center', 'color': '0/0/0', 'multiline': 'true'}, [
            n('font', {'name': 'victory_small'}),
            n('caption', {'text': 'victory_default'}),
        ]),
        n('text', {'name': 'victory2', 'offset': '510/170', 'size': '250/550', 'valign': 'top', 'halign': 'center', 'color': '255/255/255', 'multiline': 'true'}, [
            n('font', {'name': 'victory_small'}),
            n('caption', {'text': 'victory_default'}),
        ]),
    ]),
]
