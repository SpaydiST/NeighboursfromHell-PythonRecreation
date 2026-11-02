# -*- coding: utf-8 -*-
# Generated from mainmenuwhilegame.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('dialog', {'gfx': 'gui/main/ingamemenu_left.tga', 'offset': '0/0'}, [
        n('text', {'name': 'title', 'offset': '32/61', 'size': '335/53', 'valign': 'center', 'halign': 'left', 'color': '0/0/0'}, [
            n('font', {'name': 'briefing_big'}),
            n('caption', {'text': 'mainmenuwhilegame_title'}),
        ]),
        n('button', {'name': 'backtogame', 'offset': '33/170', 'size': '333/54'}, [
            n('font', {'name': 'menu_medium'}),
            n('image', {'name': 'std', 'gfx': 'gui/main/mainmenu_btn3_hover.tga', 'text': 'mainmenu_back2game', 'color': '200/200/200'}),
            n('image', {'name': 'hover', 'gfx': 'gui/main/mainmenu_btn3_hover.tga', 'text': 'mainmenu_back2game', 'color': '255/255/255'}),
            n('image', {'name': 'down', 'gfx': 'gui/main/mainmenu_btn3_pressed.tga', 'text': 'mainmenu_back2game', 'color': '255/255/255'}),
            n('sfx', {'name': 'hover', 'file': 'sfx/but_hover1.wav'}),
            n('sfx', {'name': 'down', 'file': 'sfx/but1.wav'}),
        ]),
        n('button', {'name': 'restart', 'offset': '33/225', 'size': '333/54'}, [
            n('font', {'name': 'menu_medium'}),
            n('image', {'name': 'std', 'gfx': 'gui/main/mainmenu_btn2_hover.tga', 'text': 'mainmenu_restart', 'color': '200/200/200'}),
            n('image', {'name': 'hover', 'gfx': 'gui/main/mainmenu_btn2_hover.tga', 'text': 'mainmenu_restart', 'color': '255/255/255'}),
            n('image', {'name': 'down', 'gfx': 'gui/main/mainmenu_btn2_pressed.tga', 'text': 'mainmenu_restart', 'color': '255/255/255'}),
            n('sfx', {'name': 'hover', 'file': 'sfx/but_hover1.wav'}),
            n('sfx', {'name': 'down', 'file': 'sfx/but1.wav'}),
        ]),
        n('button', {'name': 'startother', 'offset': '33/280', 'size': '333/54'}, [
            n('font', {'name': 'menu_medium'}),
            n('image', {'name': 'std', 'gfx': 'gui/main/mainmenu_btn2_hover.tga', 'text': 'mainmenu_startnew', 'color': '200/200/200'}),
            n('image', {'name': 'hover', 'gfx': 'gui/main/mainmenu_btn2_hover.tga', 'text': 'mainmenu_startnew', 'color': '255/255/255'}),
            n('image', {'name': 'down', 'gfx': 'gui/main/mainmenu_btn2_pressed.tga', 'text': 'mainmenu_startnew', 'color': '255/255/255'}),
            n('sfx', {'name': 'hover', 'file': 'sfx/but_hover1.wav'}),
            n('sfx', {'name': 'down', 'file': 'sfx/but1.wav'}),
        ]),
        n('button', {'name': 'optionswhilegame', 'offset': '33/335', 'size': '333/54'}, [
            n('font', {'name': 'menu_medium'}),
            n('image', {'name': 'std', 'gfx': 'gui/main/mainmenu_btn2_hover.tga', 'text': 'mainmenu_options', 'color': '200/200/200'}),
            n('image', {'name': 'hover', 'gfx': 'gui/main/mainmenu_btn2_hover.tga', 'text': 'mainmenu_options', 'color': '255/255/255'}),
            n('image', {'name': 'down', 'gfx': 'gui/main/mainmenu_btn2_pressed.tga', 'text': 'mainmenu_options', 'color': '255/255/255'}),
            n('sfx', {'name': 'hover', 'file': 'sfx/but_hover1.wav'}),
            n('sfx', {'name': 'down', 'file': 'sfx/but1.wav'}),
        ]),
        n('button', {'name': 'backtomain', 'offset': '33/390', 'size': '333/54'}, [
            n('font', {'name': 'menu_medium'}),
            n('image', {'name': 'std', 'gfx': 'gui/main/mainmenu_btn1_hover.tga', 'text': 'mainmenu_backtomain', 'color': '200/200/200'}),
            n('image', {'name': 'hover', 'gfx': 'gui/main/mainmenu_btn1_hover.tga', 'text': 'mainmenu_backtomain', 'color': '255/255/255'}),
            n('image', {'name': 'down', 'gfx': 'gui/main/mainmenu_btn1_pressed.tga', 'text': 'mainmenu_backtomain', 'color': '255/255/255'}),
            n('sfx', {'name': 'hover', 'file': 'sfx/but_hover1.wav'}),
            n('sfx', {'name': 'down', 'file': 'sfx/but1.wav'}),
        ]),
    ]),
]
