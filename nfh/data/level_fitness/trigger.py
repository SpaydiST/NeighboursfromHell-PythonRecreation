# -*- coding: utf-8 -*-
# Generated from trigger.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('triggers', {}, [
        n('actor', {'name': 'neighbor'}, [
            n('behavior', {'name': 'electrotrap'}, [
                n('trigger', {'object': 'bas/electrotrap', 'position': 'nearobj', 'type': 'once'}),
            ]),
            n('behavior', {'name': 'marbles'}, [
                n('trigger', {'object': 'anc/marbles', 'position': 'nearobj', 'type': 'once'}),
            ]),
            n('behavior', {'name': 'marbles'}, [
                n('trigger', {'object': 'bas/marbles', 'position': 'nearobj', 'type': 'once'}),
            ]),
            n('behavior', {'name': 'marbles'}, [
                n('trigger', {'object': 'lir/marbles', 'position': 'nearobj', 'type': 'once'}),
            ]),
            n('behavior', {'name': 'marbles'}, [
                n('trigger', {'object': 'bed/marbles', 'position': 'nearobj', 'type': 'once'}),
            ]),
            n('behavior', {'name': 'marbles'}, [
                n('trigger', {'object': 'wor/marbles', 'position': 'nearobj', 'type': 'once'}),
            ]),
            n('behavior', {'name': 'skate'}, [
                n('trigger', {'object': 'kit/skate', 'position': 'nearobj', 'type': 'once'}),
            ]),
        ]),
    ]),
]
