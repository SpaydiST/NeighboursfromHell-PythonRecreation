# -*- coding: utf-8 -*-
# Generated from trigger.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('triggers', {}, [
        n('actor', {'name': 'neighbor'}, [
            n('behavior', {'name': 'dirty_microwave'}, [
                n('trigger', {'object': 'kit/microwavedirty', 'position': 'nearobj', 'type': 'once'}),
            ]),
        ]),
    ]),
]
