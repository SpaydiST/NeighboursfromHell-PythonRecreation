# -*- coding: utf-8 -*-
# Generated from trigger.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('triggers', {}, [
        n('actor', {'name': 'HAL'}, [
            n('behavior', {'name': 'anc'}, [
                n('trigger', {'object': 'anc/ark', 'position': 'room', 'type': 'always', 'actor': 'woody'}),
            ]),
            n('behavior', {'name': 'marbles'}, [
                n('trigger', {'object': 'kit/marbles', 'position': 'nearobj', 'type': 'once', 'actor': 'woody'}),
            ]),
        ]),
        n('actor', {'name': 'neighbor'}, [
            n('behavior', {'name': 'marbles'}, [
                n('trigger', {'object': 'kit/marbles', 'position': 'nearobj', 'type': 'once'}),
            ]),
        ]),
    ]),
]
