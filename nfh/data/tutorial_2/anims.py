# -*- coding: utf-8 -*-
# Generated from anims.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('all_objects', {}, [
        n('object', {'name': 'house'}, [
            n('animation', {'name': 'ms', 'type': 'loop'}, [
                n('frame', {'gfx': 'house00_2.tga'}),
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
        n('object', {'name': 'neighbor'}, [
            n('animation', {'name': 'clean', 'type': 'oneshot'}, [
                n('frame', {'gfx': 'n_clean_0001.tga'}),
                n('frame', {'gfx': 'n_clean_0002.tga', 'sfx': 'sfx/na_towel1.wav'}),
                n('frame', {'gfx': 'n_clean_0003.tga'}),
                n('frame', {'gfx': 'n_clean_0004.tga'}),
                n('frame', {'gfx': 'n_clean_0004.tga'}),
                n('frame', {'gfx': 'n_clean_0003.tga', 'sfx': 'sfx/na_towel2.wav'}),
                n('frame', {'gfx': 'n_clean_0002.tga'}),
                n('frame', {'gfx': 'n_clean_0001.tga'}),
                n('frame', {'gfx': 'n_clean_0001.tga'}),
                n('frame', {'gfx': 'n_clean_0002.tga', 'sfx': 'sfx/na_towel1.wav'}),
                n('frame', {'gfx': 'n_clean_0003.tga'}),
                n('frame', {'gfx': 'n_clean_0004.tga'}),
                n('frame', {'gfx': 'n_clean_0004.tga'}),
                n('frame', {'gfx': 'n_clean_0003.tga', 'sfx': 'sfx/na_towel2.wav'}),
                n('frame', {'gfx': 'n_clean_0002.tga'}),
                n('frame', {'gfx': 'n_clean_0001.tga'}),
                n('frame', {'gfx': 'n_clean_0001.tga'}),
                n('frame', {'gfx': 'n_clean_0002.tga', 'sfx': 'sfx/na_towel1.wav'}),
                n('frame', {'gfx': 'n_clean_0003.tga'}),
                n('frame', {'gfx': 'n_clean_0004.tga'}),
                n('frame', {'gfx': 'n_clean_0004.tga'}),
                n('frame', {'gfx': 'n_clean_0003.tga', 'sfx': 'sfx/na_towel2.wav'}),
                n('frame', {'gfx': 'n_clean_0002.tga'}),
                n('frame', {'gfx': 'n_clean_0001.tga'}),
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
        n('object', {'name': 'anc/flower'}, [
            n('region', {'position': '270/290', 'size': '60/90'}),
            n('animation', {'name': 'ms', 'type': 'oneshot'}, [
                n('frame', {'gfx': 'flower_ms.tga'}),
            ]),
        ]),
        n('object', {'name': 'lir/mum_smeared'}, [
            n('region', {'position': '425/255', 'size': '50/52'}),
            n('animation', {'name': 'ms', 'type': 'oneshot'}, [
                n('frame', {'gfx': 'mum_smeared.tga'}),
            ]),
        ]),
        n('object', {'name': 'lir/mum'}, [
            n('region', {'position': '550/230', 'size': '120/100'}),
            n('animation', {'name': 'ms', 'type': 'oneshot'}),
        ]),
        n('object', {'name': 'lir/tafel1'}),
        n('object', {'name': 'kit/tafel2'}),
    ]),
]
