# -*- coding: utf-8 -*-
# Generated from combine.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('combine', {}, [
        n('combination', {'name': 'lir/flower'}, [
            n('ingredient', {'name': 'lir/lockedflower', 'remove': 'true'}),
            n('ingredient', {'name': 'shovel', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'lir/vacuum_hole', 'layer': '2', 'trick': 'true'}, [
            n('ingredient', {'name': 'lir/vacuum', 'remove': 'true'}),
            n('ingredient', {'name': 'paperknife', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'lir/dirtycarpet', 'trick': 'true'}, [
            n('ingredient', {'name': 'lir/carpet', 'remove': 'true'}),
            n('ingredient', {'name': 'soil', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'wor/fishfood_soap', 'trick': 'true'}, [
            n('ingredient', {'name': 'wor/fishfood', 'remove': 'true'}),
            n('ingredient', {'name': 'detergent', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bed/ironingboard_burn', 'trick': 'true'}, [
            n('ingredient', {'name': 'bed/ironingboard_clothes', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bal/clothes_food', 'trick': 'true'}, [
            n('ingredient', {'name': 'bal/clothes', 'remove': 'true'}),
            n('ingredient', {'name': 'birdfood', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bas/washingmachine_wine', 'trick': 'true'}, [
            n('ingredient', {'name': 'bas/washingmachine', 'remove': 'true'}),
            n('ingredient', {'name': 'winebottle', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bas/tumbledrier_smashed', 'trick': 'true'}, [
            n('ingredient', {'name': 'bas/tumbledrier', 'remove': 'true'}),
            n('ingredient', {'name': 'tongs', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bas/electrotrap', 'trick': 'true'}, [
            n('ingredient', {'name': 'bas/outlet', 'remove': 'true'}),
            n('ingredient', {'name': 'cable', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'anc/marbles', 'trick': 'true'}, [
            n('ingredient', {'name': 'anc', 'remove': 'false'}),
            n('ingredient', {'name': 'marbles', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'kit/marbles', 'trick': 'true'}, [
            n('ingredient', {'name': 'kit', 'remove': 'false'}),
            n('ingredient', {'name': 'marbles', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'lir/marbles', 'trick': 'true'}, [
            n('ingredient', {'name': 'lir', 'remove': 'false'}),
            n('ingredient', {'name': 'marbles', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'wrong_no_neighbor', 'wrong': 'true'}, [
            n('ingredient', {'name': 'toi', 'remove': 'false'}),
            n('ingredient', {'name': 'marbles', 'remove': 'false'}),
        ]),
        n('combination', {'name': 'bas/marbles', 'trick': 'true'}, [
            n('ingredient', {'name': 'bas', 'remove': 'false'}),
            n('ingredient', {'name': 'marbles', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bed/marbles', 'trick': 'true'}, [
            n('ingredient', {'name': 'bed', 'remove': 'false'}),
            n('ingredient', {'name': 'marbles', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'wor/marbles', 'trick': 'true'}, [
            n('ingredient', {'name': 'wor', 'remove': 'false'}),
            n('ingredient', {'name': 'marbles', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bal/marbles', 'trick': 'true'}, [
            n('ingredient', {'name': 'bal', 'remove': 'false'}),
            n('ingredient', {'name': 'marbles', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'wrongclothes_food', 'wrong': 'true'}, [
            n('ingredient', {'name': 'bal/noclothes', 'remove': 'false'}),
            n('ingredient', {'name': 'birdfood', 'remove': 'false'}),
        ]),
    ]),
]
