# -*- coding: utf-8 -*-
# Generated from newgameright.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('dialog', {'gfx': 'gui/main/newgameright.tga', 'offset': '400/0'}, [
        n('frame', {'name': 'levelimage', 'offset': '28/121'}),
        n('text', {'name': 'newgamerightcaption', 'offset': '0/0', 'size': '375/50', 'valign': 'center', 'halign': 'right', 'color': '255/255/255'}, [
            n('font', {'name': 'menu_medium'}),
            n('caption', {'text': 'newgamerightcaption'}),
        ]),
        n('text', {'name': 'title', 'offset': '32/61', 'size': '335/53', 'valign': 'center', 'halign': 'left', 'color': '0/0/0'}, [
            n('font', {'name': 'briefing_big'}),
        ]),
        n('text', {'name': 'minquotaperc', 'offset': '258/151', 'size': '18/21', 'valign': 'bottom', 'halign': 'left', 'color': '255/255/255'}, [
            n('font', {'name': 'briefing_small'}),
            n('caption', {'text': 'minquotaperc'}),
        ]),
        n('text', {'name': 'minquotanum', 'offset': '212/149', 'size': '46/24', 'valign': 'bottom', 'halign': 'right', 'color': '255/255/255'}, [
            n('font', {'name': 'briefing_verybig'}),
        ]),
        n('text', {'name': 'minquotacap', 'offset': '187/178', 'size': '88/20', 'valign': 'top', 'halign': 'center', 'color': '255/255/255'}, [
            n('font', {'name': 'briefing_verysmall'}),
            n('caption', {'text': 'minquotacap'}),
        ]),
        n('text', {'name': 'timeunit', 'offset': '342/151', 'size': '27/21', 'valign': 'bottom', 'halign': 'left', 'color': '255/255/255'}, [
            n('font', {'name': 'briefing_small'}),
            n('caption', {'text': 'timeunit'}),
        ]),
        n('text', {'name': 'timenum', 'offset': '290/149', 'size': '52/24', 'valign': 'bottom', 'halign': 'right', 'color': '255/255/255'}, [
            n('font', {'name': 'briefing_verybig'}),
        ]),
        n('text', {'name': 'timecap', 'offset': '282/178', 'size': '88/20', 'valign': 'top', 'halign': 'center', 'color': '255/255/255'}, [
            n('font', {'name': 'briefing_verysmall'}),
            n('caption', {'text': 'timecap'}),
        ]),
        n('text', {'name': 'hinttitle', 'offset': '190/202', 'size': '177/22', 'valign': 'center', 'halign': 'center', 'color': '0/96/255'}, [
            n('font', {'name': 'briefing_verybig'}),
            n('caption', {'text': 'hinttitle'}),
        ]),
        n('text', {'name': 'hinttext', 'offset': '190/220', 'size': '177/58', 'valign': 'center', 'halign': 'center', 'color': '0/0/0'}, [
            n('font', {'name': 'briefing_quitesmall'}),
        ]),
        n('text', {'name': 'pictext', 'offset': '28/264', 'size': '149/24', 'valign': 'top', 'halign': 'left', 'color': '0/0/0'}, [
            n('font', {'name': 'briefing_verysmall'}),
        ]),
        n('text', {'name': 'briefing', 'offset': '28/287', 'size': '343/178', 'valign': 'top', 'halign': 'left', 'color': '0/0/0'}, [
            n('font', {'name': 'briefing_small'}),
        ]),
        n('text', {'name': 'lastscoretitle', 'offset': '67/475', 'size': '189/23', 'valign': 'center', 'halign': 'left', 'color': '0/0/0'}, [
            n('font', {'name': 'briefing_medium_bold'}),
            n('caption', {'text': 'lastscoretitle'}),
        ]),
        n('text', {'name': 'lasttrickscap', 'offset': '30/499', 'size': '155/23', 'valign': 'center', 'halign': 'center', 'color': '0/0/0'}, [
            n('font', {'name': 'briefing_medium'}),
            n('caption', {'text': 'lasttrickscap'}),
        ]),
        n('text', {'name': 'lasttricknum', 'offset': '132/523', 'size': '50/21', 'valign': 'bottom', 'halign': 'right', 'color': '0/0/0'}, [
            n('font', {'name': 'briefing_verybig'}),
        ]),
        n('text', {'name': 'lastquotacap', 'offset': '191/499', 'size': '63/23', 'valign': 'center', 'halign': 'center', 'color': '0/0/0'}, [
            n('font', {'name': 'briefing_medium'}),
            n('caption', {'text': 'lastquotacap'}),
        ]),
        n('text', {'name': 'lastquotaperc', 'offset': '235/522', 'size': '18/21', 'valign': 'bottom', 'halign': 'left', 'color': '0/0/0'}, [
            n('font', {'name': 'briefing_small'}),
            n('caption', {'text': 'lastquotaperc'}),
        ]),
        n('text', {'name': 'lastquotanum', 'offset': '191/523', 'size': '44/21', 'valign': 'bottom', 'halign': 'right', 'color': '0/0/0'}, [
            n('font', {'name': 'briefing_verybig'}),
        ]),
        n('text', {'name': 'play', 'offset': '269/475', 'size': '103/67', 'valign': 'center', 'halign': 'center', 'color': '0/0/0'}, [
            n('font', {'name': 'briefing_medium'}),
            n('caption', {'text': 'play'}),
        ]),
        n('button', {'name': 'start', 'offset': '320/530'}, [
            n('image', {'name': 'std', 'gfx': 'gui/main/start_right_std.tga'}),
            n('image', {'name': 'hover', 'gfx': 'gui/main/start_right_hover.tga'}),
            n('image', {'name': 'down', 'gfx': 'gui/main/start_right_pressed.tga'}),
            n('sfx', {'name': 'hover', 'file': 'sfx/but_hover1.wav'}),
            n('sfx', {'name': 'down', 'file': 'sfx/but1.wav'}),
        ]),
    ]),
]
