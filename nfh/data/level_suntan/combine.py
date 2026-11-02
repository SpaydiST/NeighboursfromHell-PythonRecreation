# -*- coding: utf-8 -*-
# Generated from combine.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('combine', {}, [
        n('combination', {'name': 'toi/firstaid'}, [
            n('ingredient', {'name': 'toi/firstaid_locked', 'remove': 'true'}),
            n('ingredient', {'name': 'key', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'toi/shoebrushset', 'trick': 'true'}, [
            n('ingredient', {'name': 'toi/toothbrushset', 'remove': 'true'}),
            n('ingredient', {'name': 'brush', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'kit/groundbanana', 'trick': 'true'}, [
            n('ingredient', {'name': 'kit', 'remove': 'false'}),
            n('ingredient', {'name': 'banana', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'toi/groundbanana', 'trick': 'true'}, [
            n('ingredient', {'name': 'toi', 'remove': 'false'}),
            n('ingredient', {'name': 'banana', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'anc/groundbanana', 'trick': 'true'}, [
            n('ingredient', {'name': 'anc', 'remove': 'false'}),
            n('ingredient', {'name': 'banana', 'remove': 'true'}),
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
        n('combination', {'name': 'kit/coffeebox_soil', 'trick': 'true'}, [
            n('ingredient', {'name': 'kit/coffeebox', 'remove': 'true'}),
            n('ingredient', {'name': 'soil', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bal/ewer_poisoned', 'trick': 'true'}, [
            n('ingredient', {'name': 'bal/ewer', 'remove': 'true'}),
            n('ingredient', {'name': 'poison', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bal/suncream_sweet', 'trick': 'true'}, [
            n('ingredient', {'name': 'bal/suncream', 'remove': 'true'}),
            n('ingredient', {'name': 'honey', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bal/sunshade_closed'}, [
            n('ingredient', {'name': 'bal/sunshade', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bal/foldingchair_pins', 'layer': '2', 'trick': 'true'}, [
            n('ingredient', {'name': 'bal/foldingchair', 'remove': 'true'}),
            n('ingredient', {'name': 'pins', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'wrongpoison', 'wrong': 'true'}, [
            n('ingredient', {'name': 'anc/flower', 'remove': 'false'}),
            n('ingredient', {'name': 'poison', 'remove': 'true'}),
        ]),
    ]),
]
