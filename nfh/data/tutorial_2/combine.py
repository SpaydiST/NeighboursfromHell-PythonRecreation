# -*- coding: utf-8 -*-
# Generated from combine.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('combine', {}, [
        n('combination', {'name': 'wronglirmarbles', 'wrong': 'true'}, [
            n('ingredient', {'name': 'lir', 'remove': 'false'}),
            n('ingredient', {'name': 'marbles', 'remove': 'false'}),
        ]),
        n('combination', {'name': 'kit/marbles', 'trick': 'true'}, [
            n('ingredient', {'name': 'kit', 'remove': 'false'}),
            n('ingredient', {'name': 'marbles', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'wrongmarbles', 'wrong': 'true'}, [
            n('ingredient', {'name': 'anc', 'remove': 'false'}),
            n('ingredient', {'name': 'marbles', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'lir/mum_smeared', 'trick': 'true'}, [
            n('ingredient', {'name': 'lir/mum', 'remove': 'true'}),
            n('ingredient', {'name': 'marker', 'remove': 'true'}),
        ]),
    ]),
]
