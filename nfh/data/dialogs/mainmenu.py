# -*- coding: utf-8 -*-
# Generated from mainmenu.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('dialog', {'gfx': 'gui/main/mainmenu.tga', 'offset': '0/0'}, [
        n('frame', {'name': 'logo', 'offset': '235/15'}, [
            n('image', {'gfx': 'gui/logo/logo_main.tga'}),
        ]),
        n('button', {'name': 'start', 'offset': '248/286', 'size': '333/54'}, [
            n('font', {'name': 'main_medium'}),
            n('image', {'name': 'std', 'gfx': 'gui/main/mainmenu_btn3_hover.tga', 'text': 'mainmenu_start', 'color': '200/200/200'}),
            n('image', {'name': 'hover', 'gfx': 'gui/main/mainmenu_btn3_hover.tga', 'text': 'mainmenu_start', 'color': '255/255/255'}),
            n('image', {'name': 'down', 'gfx': 'gui/main/mainmenu_btn3_pressed.tga', 'text': 'mainmenu_start', 'color': '255/255/255'}),
            n('sfx', {'name': 'hover', 'file': 'sfx/but_hover1.wav'}),
            n('sfx', {'name': 'down', 'file': 'sfx/but1.wav'}),
        ]),
        n('button', {'name': 'credits', 'offset': '248/341', 'size': '333/54'}, [
            n('font', {'name': 'main_medium'}),
            n('image', {'name': 'std', 'gfx': 'gui/main/mainmenu_btn2_hover.tga', 'text': 'mainmenu_credits', 'color': '200/200/200'}),
            n('image', {'name': 'hover', 'gfx': 'gui/main/mainmenu_btn2_hover.tga', 'text': 'mainmenu_credits', 'color': '255/255/255'}),
            n('image', {'name': 'down', 'gfx': 'gui/main/mainmenu_btn2_pressed.tga', 'text': 'mainmenu_credits', 'color': '255/255/255'}),
            n('sfx', {'name': 'hover', 'file': 'sfx/but_hover1.wav'}),
            n('sfx', {'name': 'down', 'file': 'sfx/but1.wav'}),
        ]),
        n('button', {'name': 'options', 'offset': '248/396', 'size': '333/54'}, [
            n('font', {'name': 'main_medium'}),
            n('image', {'name': 'std', 'gfx': 'gui/main/mainmenu_btn2_hover.tga', 'text': 'mainmenu_options', 'color': '200/200/200'}),
            n('image', {'name': 'hover', 'gfx': 'gui/main/mainmenu_btn2_hover.tga', 'text': 'mainmenu_options', 'color': '255/255/255'}),
            n('image', {'name': 'down', 'gfx': 'gui/main/mainmenu_btn2_pressed.tga', 'text': 'mainmenu_options', 'color': '255/255/255'}),
            n('sfx', {'name': 'hover', 'file': 'sfx/but_hover1.wav'}),
            n('sfx', {'name': 'down', 'file': 'sfx/but1.wav'}),
        ]),
        n('button', {'name': 'quit', 'offset': '248/451', 'size': '333/54'}, [
            n('font', {'name': 'main_medium'}),
            n('image', {'name': 'std', 'gfx': 'gui/main/mainmenu_btn1_hover.tga', 'text': 'mainmenu_quit', 'color': '200/200/200'}),
            n('image', {'name': 'hover', 'gfx': 'gui/main/mainmenu_btn1_hover.tga', 'text': 'mainmenu_quit', 'color': '255/255/255'}),
            n('image', {'name': 'down', 'gfx': 'gui/main/mainmenu_btn1_pressed.tga', 'text': 'mainmenu_quit', 'color': '255/255/255'}),
            n('sfx', {'name': 'hover', 'file': 'sfx/but_hover1.wav'}),
            n('sfx', {'name': 'down', 'file': 'sfx/but1.wav'}),
        ]),
        n('text', {'name': 'version', 'offset': '10/570', 'size': '790/25', 'valign': 'bottom', 'halign': 'left', 'color': '255/255/255'}, [
            n('font', {'name': 'menu_verysmall'}),
        ]),
    ]),
]
