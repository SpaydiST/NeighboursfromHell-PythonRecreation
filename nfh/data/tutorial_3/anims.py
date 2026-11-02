# -*- coding: utf-8 -*-
# Generated from anims.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('all_objects', {}, [
        n('object', {'name': 'house'}, [
            n('animation', {'name': 'ms', 'type': 'loop'}, [
                n('frame', {'gfx': 'house00_3.tga'}),
            ]),
        ]),
        n('object', {'name': 'arrow'}, [
            n('animation', {'name': 'ms2', 'type': 'loop'}, [
                n('frame', {'gfx': 'ms_0000.tga'}),
                n('frame', {'gfx': 'ms_0000.tga'}),
                n('frame', {'gfx': 'ms_0001.tga'}),
                n('frame', {'gfx': 'ms_0001.tga'}),
                n('frame', {'gfx': 'ms_0002.tga'}),
                n('frame', {'gfx': 'ms_0002.tga'}),
                n('frame', {'gfx': 'ms_0003.tga'}),
                n('frame', {'gfx': 'ms_0003.tga'}),
            ]),
        ]),
        n('object', {'name': 'kit/marbles'}, [
            n('region', {'position': '0/0', 'size': '110/48'}),
            n('animation', {'name': 'ms', 'type': 'oneshot'}, [
                n('frame', {'gfx': 'marbles_ms.tga'}),
            ]),
        ]),
        n('object', {'name': 'anc/ark'}, [
            n('region', {'position': '625/315', 'size': '70/70'}),
            n('animation', {'name': 'ms', 'type': 'oneshot'}),
            n('animation', {'name': 'empty', 'type': 'oneshot'}),
            n('animation', {'name': 'open', 'type': 'oneshot'}, [
                n('frame', {'gfx': 'ark_open.tga'}),
            ]),
        ]),
        n('object', {'name': 'anc/wardrobe'}, [
            n('region', {'position': '328/249', 'size': '92/141'}),
            n('region', {'position': '280/270', 'size': '0/0', 'type': 'text'}),
            n('animation', {'name': 'ms', 'type': 'oneshot'}),
            n('animation', {'name': 'woody_enter', 'type': 'oneshot'}, [
                n('frame', {'gfx': 'w_hide_wardrobe_0000.tga'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0001.tga', 'sfx': 'sfx/wod_step1a.wav'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0002.tga', 'sfx': 'sfx/obj_open1.wav'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0003.tga'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0004.tga'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0005.tga'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0006.tga'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0007.tga'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0008.tga'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0009.tga', 'sfx': 'sfx/wod_step1a.wav'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0010.tga'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0011.tga'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0012.tga', 'sfx': 'sfx/wod_step1a.wav'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0013.tga'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0014.tga', 'sfx': 'sfx/wod_step2a.wav'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0015.tga'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0016.tga'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0017.tga', 'sfx': 'sfx/obj_close1.wav'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0018.tga'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0019.tga'}),
            ]),
            n('animation', {'name': 'woody_leave', 'type': 'oneshot'}, [
                n('frame', {'gfx': 'w_hide_wardrobe_0019.tga'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0018.tga', 'sfx': 'sfx/obj_open1.wav'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0017.tga'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0016.tga'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0015.tga'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0014.tga'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0013.tga'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0012.tga', 'sfx': 'sfx/wod_step1a.wav'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0011.tga'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0010.tga'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0009.tga', 'sfx': 'sfx/wod_step1a.wav'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0008.tga'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0007.tga'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0006.tga', 'sfx': 'sfx/wod_step2a.wav'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0005.tga'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0004.tga'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0003.tga', 'sfx': 'sfx/obj_close1.wav'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0002.tga'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0001.tga', 'sfx': 'sfx/wod_step1a.wav'}),
                n('frame', {'gfx': 'w_hide_wardrobe_0000.tga'}),
            ]),
        ]),
        n('object', {'name': 'lir/tafel1'}),
        n('object', {'name': 'kit/tafel2'}),
    ]),
]
