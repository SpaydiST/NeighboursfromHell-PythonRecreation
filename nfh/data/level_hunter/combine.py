# -*- coding: utf-8 -*-
# Generated from combine.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('combine', {}, [
        n('combination', {'name': 'kit/blackpolish', 'trick': 'true'}, [
            n('ingredient', {'name': 'kit/polish', 'remove': 'true'}),
            n('ingredient', {'name': 'shoepolish', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bed/stickyhat', 'trick': 'true'}, [
            n('ingredient', {'name': 'bed/hat', 'remove': 'true'}),
            n('ingredient', {'name': 'superglue', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bas/gun_loaded', 'trick': 'true'}, [
            n('ingredient', {'name': 'bas/gun', 'remove': 'true'}),
            n('ingredient', {'name': 'munition', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bas/gun_plugged'}, [
            n('ingredient', {'name': 'bas/gun', 'remove': 'true'}),
            n('ingredient', {'name': 'cork', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bas/gun_loaded_plugged', 'trick': 'true'}, [
            n('ingredient', {'name': 'bas/gun_loaded', 'remove': 'true'}),
            n('ingredient', {'name': 'cork', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bas/gun_loaded_plugged', 'trick': 'true'}, [
            n('ingredient', {'name': 'bas/gun_plugged', 'remove': 'true'}),
            n('ingredient', {'name': 'munition', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'lir/tabacbox_explosive', 'trick': 'true'}, [
            n('ingredient', {'name': 'lir/tabacbox', 'remove': 'true'}),
            n('ingredient', {'name': 'gunpowder', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'lir/phono_nail', 'trick': 'true'}, [
            n('ingredient', {'name': 'lir/phono_open', 'remove': 'true'}),
            n('ingredient', {'name': 'nail', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bal/clothes_food', 'trick': 'true'}, [
            n('ingredient', {'name': 'bal/clothes', 'remove': 'true'}),
            n('ingredient', {'name': 'birdfood', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bed/medalbox_rat', 'trick': 'true'}, [
            n('ingredient', {'name': 'bed/medalbox', 'remove': 'true'}),
            n('ingredient', {'name': 'rat', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bal/balloonhorn', 'trick': 'true'}, [
            n('ingredient', {'name': 'bal/woodhorn', 'remove': 'true'}),
            n('ingredient', {'name': 'balloon', 'remove': 'true'}),
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
        n('combination', {'name': 'dog'}, [
            n('ingredient', {'name': 'dogwhistle', 'remove': 'false'}),
        ]),
        n('combination', {'name': 'phono_nail_play', 'wrong': 'true'}, [
            n('ingredient', {'name': 'lir/phono_play', 'remove': 'false'}),
            n('ingredient', {'name': 'nail', 'remove': 'false'}),
        ]),
    ]),
]
