# -*- coding: utf-8 -*-
# Generated from combine.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('combine', {}, [
        n('combination', {'name': 'kit/groundbanana', 'trick': 'true'}, [
            n('ingredient', {'name': 'kit', 'remove': 'false'}),
            n('ingredient', {'name': 'banana', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'anc/groundbanana', 'trick': 'true'}, [
            n('ingredient', {'name': 'anc', 'remove': 'false'}),
            n('ingredient', {'name': 'banana', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'lir/groundbanana', 'trick': 'true'}, [
            n('ingredient', {'name': 'lir', 'remove': 'false'}),
            n('ingredient', {'name': 'banana', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bed/groundbanana', 'trick': 'true'}, [
            n('ingredient', {'name': 'bed', 'remove': 'false'}),
            n('ingredient', {'name': 'banana', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'kit/cookiebox_hot', 'trick': 'true'}, [
            n('ingredient', {'name': 'kit/cookiebox', 'remove': 'true'}),
            n('ingredient', {'name': 'chips', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'kit/babybottle_nitro', 'trick': 'true'}, [
            n('ingredient', {'name': 'kit/babybottle', 'remove': 'true'}),
            n('ingredient', {'name': 'nitro', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bed/teeth_tabasco', 'trick': 'true'}, [
            n('ingredient', {'name': 'bed/teeth', 'remove': 'true'}),
            n('ingredient', {'name': 'tabasco', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bed/cactusclock', 'trick': 'true'}, [
            n('ingredient', {'name': 'bed/alarmclock', 'remove': 'true'}),
            n('ingredient', {'name': 'cactus', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bed/bed_pins', 'layer': '2', 'trick': 'true'}, [
            n('ingredient', {'name': 'bed/bed', 'remove': 'true'}),
            n('ingredient', {'name': 'pins', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'anc/pigout', 'trick': 'true'}, [
            n('ingredient', {'name': 'anc/pig', 'remove': 'true'}),
            n('ingredient', {'name': 'pigkey', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'wrongnitropig', 'wrong': 'true'}, [
            n('ingredient', {'name': 'anc/pig', 'remove': 'false'}),
            n('ingredient', {'name': 'nitro', 'remove': 'false'}),
        ]),
        n('combination', {'name': 'wrong_no_neighbor', 'wrong': 'true'}, [
            n('ingredient', {'name': 'toi', 'remove': 'false'}),
            n('ingredient', {'name': 'banana', 'remove': 'false'}),
        ]),
        n('combination', {'name': 'wrong_no_neighbor', 'wrong': 'true'}, [
            n('ingredient', {'name': 'bal', 'remove': 'false'}),
            n('ingredient', {'name': 'banana', 'remove': 'false'}),
        ]),
        n('combination', {'name': 'wrongtabasco', 'wrong': 'true'}, [
            n('ingredient', {'name': 'bed/teeth_empty', 'remove': 'false'}),
            n('ingredient', {'name': 'tabasco', 'remove': 'false'}),
        ]),
        n('combination', {'name': 'wrongbed', 'wrong': 'true'}, [
            n('ingredient', {'name': 'bed/bed_sleep', 'remove': 'false'}),
            n('ingredient', {'name': 'pins', 'remove': 'false'}),
        ]),
    ]),
]
