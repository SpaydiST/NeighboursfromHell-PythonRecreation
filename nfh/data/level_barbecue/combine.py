# -*- coding: utf-8 -*-
# Generated from combine.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('combine', {}, [
        n('combination', {'name': 'bal/fuelbeer', 'trick': 'true'}, [
            n('ingredient', {'name': 'bal/beer', 'remove': 'true'}),
            n('ingredient', {'name': 'fuel', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'lir/chair_pins', 'trick': 'true'}, [
            n('ingredient', {'name': 'lir/chair', 'remove': 'true'}),
            n('ingredient', {'name': 'pins', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'kit/groundbanana', 'trick': 'true'}, [
            n('ingredient', {'name': 'kit', 'remove': 'false'}),
            n('ingredient', {'name': 'banana', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'wrong_no_neighbor', 'wrong': 'true'}, [
            n('ingredient', {'name': 'toi', 'remove': 'false'}),
            n('ingredient', {'name': 'banana', 'remove': 'false'}),
        ]),
        n('combination', {'name': 'wrong_no_neighbor', 'wrong': 'true'}, [
            n('ingredient', {'name': 'anc', 'remove': 'false'}),
            n('ingredient', {'name': 'banana', 'remove': 'false'}),
        ]),
        n('combination', {'name': 'bed/groundbanana', 'trick': 'true'}, [
            n('ingredient', {'name': 'bed', 'remove': 'false'}),
            n('ingredient', {'name': 'banana', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bal/groundbanana', 'trick': 'true'}, [
            n('ingredient', {'name': 'bal', 'remove': 'false'}),
            n('ingredient', {'name': 'banana', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'lir/groundbanana', 'trick': 'true'}, [
            n('ingredient', {'name': 'lir', 'remove': 'false'}),
            n('ingredient', {'name': 'banana', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'lir/vinegar', 'trick': 'true'}, [
            n('ingredient', {'name': 'lir/wine', 'remove': 'true'}),
            n('ingredient', {'name': 'vinegar', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bed/extinguisher_knotted', 'trick': 'true'}, [
            n('ingredient', {'name': 'bed/extinguisher', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bal/growspray', 'trick': 'true'}, [
            n('ingredient', {'name': 'bal/spray', 'remove': 'true'}),
            n('ingredient', {'name': 'growthliquid', 'remove': 'true'}),
        ]),
    ]),
]
