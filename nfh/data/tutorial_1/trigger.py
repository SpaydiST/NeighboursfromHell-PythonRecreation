# -*- coding: utf-8 -*-
# Generated from trigger.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('triggers', {}, [
        n('actor', {'name': 'HAL'}, [
            n('behavior', {'name': 'target'}, [
                n('trigger', {'object': 'kit/sign', 'position': 'nearobj', 'type': 'once', 'actor': 'woody'}),
            ]),
            n('behavior', {'name': 'target'}, [
                n('trigger', {'object': 'lir/kit', 'position': 'room', 'type': 'once', 'actor': 'woody'}),
            ]),
            n('behavior', {'name': 'target'}, [
                n('trigger', {'object': 'lir/sign', 'position': 'nearobj', 'type': 'once', 'actor': 'woody'}),
            ]),
            n('behavior', {'name': 'target'}, [
                n('trigger', {'object': 'anc/lir', 'position': 'room', 'type': 'once', 'actor': 'woody'}),
            ]),
            n('behavior', {'name': 'target'}, [
                n('trigger', {'object': 'anc/sign', 'position': 'nearobj', 'type': 'once', 'actor': 'woody'}),
            ]),
            n('behavior', {'name': 'target'}, [
                n('trigger', {'object': 'fro/anc', 'position': 'room', 'type': 'once', 'actor': 'woody'}),
            ]),
        ]),
    ]),
]
