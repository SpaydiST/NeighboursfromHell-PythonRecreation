# -*- coding: utf-8 -*-
# Generated from options.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('dialog', {'gfx': 'gui/main/optionsback.tga', 'offset': '0/0'}, [
        n('frame', {'name': 'logo', 'offset': '235/15'}, [
            n('image', {'gfx': 'gui/logo/logo_main.tga'}),
        ]),
        n('frame', {'name': 'speakers_left', 'offset': '0/281'}),
        n('frame', {'name': 'speakers_right', 'offset': '543/281'}),
        n('text', {'name': 'soundquality1text', 'offset': '320/367', 'size': '221/17', 'valign': 'center', 'halign': 'left', 'color': '75/255/0'}, [
            n('font', {'name': 'options_small'}),
            n('caption', {'text': 'sound_quality1'}),
        ]),
        n('button', {'name': 'soundquality1', 'offset': '296/367', 'size': '250/17'}, [
            n('image', {'name': 'std', 'gfx': 'gui/main/checkbox_off.tga'}),
            n('image', {'name': 'hover', 'gfx': 'gui/main/checkbox_off_hov.tga'}),
            n('image', {'name': 'down', 'gfx': 'gui/main/checkbox_on.tga'}),
            n('image', {'name': 'hover_down', 'gfx': 'gui/main/checkbox_on_hov.tga'}),
            n('image', {'name': 'disabled', 'gfx': 'gui/main/checkbox_dis.tga'}),
            n('sfx', {'name': 'hover', 'file': 'sfx/but_hover1.wav'}),
            n('sfx', {'name': 'down', 'file': 'sfx/but1.wav'}),
        ]),
        n('text', {'name': 'timelimit_text', 'offset': '320/388', 'size': '221/17', 'valign': 'center', 'halign': 'left', 'color': '75/255/0'}, [
            n('font', {'name': 'options_small'}),
            n('caption', {'text': 'timelimit'}),
        ]),
        n('button', {'name': 'timelimit', 'offset': '296/388', 'size': '250/17'}, [
            n('image', {'name': 'std', 'gfx': 'gui/main/checkbox_off.tga'}),
            n('image', {'name': 'hover', 'gfx': 'gui/main/checkbox_off_hov.tga'}),
            n('image', {'name': 'down', 'gfx': 'gui/main/checkbox_on.tga'}),
            n('image', {'name': 'hover_down', 'gfx': 'gui/main/checkbox_on_hov.tga'}),
            n('image', {'name': 'disabled', 'gfx': 'gui/main/checkbox_dis.tga'}),
            n('sfx', {'name': 'hover', 'file': 'sfx/but_hover1.wav'}),
            n('sfx', {'name': 'down', 'file': 'sfx/but1.wav'}),
        ]),
        n('text', {'name': 'autoscroll_text', 'offset': '320/409', 'size': '221/17', 'valign': 'center', 'halign': 'left', 'color': '75/255/0'}, [
            n('font', {'name': 'options_small'}),
            n('caption', {'text': 'autoscroll'}),
        ]),
        n('button', {'name': 'autoscroll', 'offset': '296/409', 'size': '250/17'}, [
            n('image', {'name': 'std', 'gfx': 'gui/main/checkbox_off.tga'}),
            n('image', {'name': 'hover', 'gfx': 'gui/main/checkbox_off_hov.tga'}),
            n('image', {'name': 'down', 'gfx': 'gui/main/checkbox_on.tga'}),
            n('image', {'name': 'hover_down', 'gfx': 'gui/main/checkbox_on_hov.tga'}),
            n('sfx', {'name': 'hover', 'file': 'sfx/but_hover1.wav'}),
            n('sfx', {'name': 'down', 'file': 'sfx/but1.wav'}),
        ]),
        n('text', {'name': 'coloredcursors_text', 'offset': '321/430', 'size': '221/17', 'valign': 'center', 'halign': 'left', 'color': '75/255/0'}, [
            n('font', {'name': 'options_small'}),
            n('caption', {'text': 'colored cursors'}),
        ]),
        n('button', {'name': 'coloredcursors', 'offset': '296/430', 'size': '250/17'}, [
            n('image', {'name': 'std', 'gfx': 'gui/main/checkbox_off.tga'}),
            n('image', {'name': 'hover', 'gfx': 'gui/main/checkbox_off_hov.tga'}),
            n('image', {'name': 'down', 'gfx': 'gui/main/checkbox_on.tga'}),
            n('image', {'name': 'hover_down', 'gfx': 'gui/main/checkbox_on_hov.tga'}),
            n('sfx', {'name': 'hover', 'file': 'sfx/but_hover1.wav'}),
            n('sfx', {'name': 'down', 'file': 'sfx/but1.wav'}),
        ]),
        n('text', {'name': 'musicvolume_text', 'offset': '410/287', 'size': '237/44', 'valign': 'center', 'halign': 'left', 'color': '75/255/0'}, [
            n('font', {'name': 'options_small'}),
            n('caption', {'text': 'music volume'}),
        ]),
        n('progressbar', {'name': 'musicvolume', 'offset': '295/290', 'mouse': 'true'}, [
            n('image', {'name': 'back', 'gfx': 'gui/volume_dark.tga'}),
            n('image', {'name': 'front', 'gfx': 'gui/volume_norm.tga'}),
            n('image', {'name': 'hover', 'gfx': 'gui/volume_hov.tga'}),
            n('range', {'min': '0', 'max': '100', 'steps': '15'}),
        ]),
        n('button', {'name': 'mute_music', 'offset': '251/292'}, [
            n('image', {'name': 'std', 'gfx': 'gui/main/sound_on.tga'}),
            n('image', {'name': 'hover', 'gfx': 'gui/main/sound_on_hov.tga'}),
            n('image', {'name': 'down', 'gfx': 'gui/main/sound_off.tga'}),
            n('image', {'name': 'hover_down', 'gfx': 'gui/main/sound_off_hov.tga'}),
            n('sfx', {'name': 'hover', 'file': 'sfx/but_hover1.wav'}),
            n('sfx', {'name': 'down', 'file': 'sfx/but1.wav'}),
        ]),
        n('text', {'name': 'mastervolume_text', 'offset': '410/249', 'size': '237/44', 'valign': 'center', 'halign': 'left', 'color': '75/255/0'}, [
            n('font', {'name': 'options_small'}),
            n('caption', {'text': 'master volume'}),
        ]),
        n('button', {'name': 'mute_master', 'offset': '251/248'}, [
            n('image', {'name': 'std', 'gfx': 'gui/main/sound_on.tga'}),
            n('image', {'name': 'hover', 'gfx': 'gui/main/sound_on_hov.tga'}),
            n('image', {'name': 'down', 'gfx': 'gui/main/sound_off.tga'}),
            n('image', {'name': 'hover_down', 'gfx': 'gui/main/sound_off_hov.tga'}),
            n('sfx', {'name': 'hover', 'file': 'sfx/but_hover1.wav'}),
            n('sfx', {'name': 'down', 'file': 'sfx/but1.wav'}),
        ]),
        n('progressbar', {'name': 'mastervolume', 'offset': '295/252', 'mouse': 'true'}, [
            n('image', {'name': 'back', 'gfx': 'gui/volume_dark.tga'}),
            n('image', {'name': 'front', 'gfx': 'gui/volume_norm.tga'}),
            n('image', {'name': 'hover', 'gfx': 'gui/volume_hov.tga'}),
            n('range', {'min': '0', 'max': '100', 'steps': '15'}),
        ]),
        n('button', {'name': 'reset_userdata', 'offset': '262/335'}, [
            n('font', {'name': 'options_small'}),
            n('image', {'name': 'std', 'gfx': 'gui/main/spielstand_norm.tga', 'text': 'reset_userdata', 'color': '75/255/0'}),
            n('image', {'name': 'hover', 'gfx': 'gui/main/spielstand_hov.tga', 'text': 'reset_userdata', 'color': '255/255/0'}),
            n('image', {'name': 'down', 'gfx': 'gui/main/spielstand_hov.tga', 'text': 'reset_userdata', 'color': '255/255/0'}),
            n('image', {'name': 'disabled', 'gfx': 'gui/main/spielstand_dis.tga', 'text': 'reset_userdata', 'color': '11/74/0'}),
            n('sfx', {'name': 'hover', 'file': 'sfx/but_hover1.wav'}),
            n('sfx', {'name': 'down', 'file': 'sfx/but1.wav'}),
        ]),
        n('text', {'name': 'statusbar', 'offset': '0/540', 'size': '800/46', 'valign': 'center', 'halign': 'center', 'color': '0/0/0'}, [
            n('font', {'name': 'menu_medium'}),
        ]),
        n('button', {'name': 'cancel', 'offset': '262/455'}, [
            n('font', {'name': 'options_small'}),
            n('image', {'name': 'std', 'gfx': 'gui/main/choice_norm.tga', 'text': 'option_cancel', 'color': '75/255/0'}),
            n('image', {'name': 'hover', 'gfx': 'gui/main/choice_hov.tga', 'text': 'option_cancel', 'color': '255/255/0'}),
            n('image', {'name': 'down', 'gfx': 'gui/main/choice_hov.tga', 'text': 'option_cancel', 'color': '255/255/0'}),
            n('sfx', {'name': 'hover', 'file': 'sfx/but_hover1.wav'}),
            n('sfx', {'name': 'down', 'file': 'sfx/but1.wav'}),
        ]),
        n('button', {'name': 'ok', 'offset': '402/455'}, [
            n('font', {'name': 'options_small'}),
            n('image', {'name': 'std', 'gfx': 'gui/main/choice_norm.tga', 'text': 'option_ok', 'color': '75/255/0'}),
            n('image', {'name': 'hover', 'gfx': 'gui/main/choice_hov.tga', 'text': 'option_ok', 'color': '255/255/0'}),
            n('image', {'name': 'down', 'gfx': 'gui/main/choice_hov.tga', 'text': 'option_ok', 'color': '255/255/0'}),
            n('sfx', {'name': 'hover', 'file': 'sfx/but_hover1.wav'}),
            n('sfx', {'name': 'down', 'file': 'sfx/but1.wav'}),
        ]),
    ]),
]
