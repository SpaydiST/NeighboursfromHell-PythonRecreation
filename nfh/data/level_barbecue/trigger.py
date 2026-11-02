# -*- coding: utf-8 -*-
# Generated from trigger.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('triggers', {}, [
        n('actor', {'name': 'neighbor'}, [
            n('behavior', {'name': 'banana_on_floor'}, [
                n('trigger', {'object': 'kit/groundbanana', 'position': 'nearobj', 'type': 'once'}),
            ]),
            n('behavior', {'name': 'banana_on_floor'}, [
                n('trigger', {'object': 'bed/groundbanana', 'position': 'nearobj', 'type': 'once'}),
            ]),
            n('behavior', {'name': 'banana_on_floor'}, [
                n('trigger', {'object': 'lir/groundbanana', 'position': 'nearobj', 'type': 'once'}),
            ]),
            n('behavior', {'name': 'banana_on_floor'}, [
                n('trigger', {'object': 'bal/groundbanana', 'position': 'nearobj', 'type': 'once'}),
            ]),
        ]),
    ]),
]
