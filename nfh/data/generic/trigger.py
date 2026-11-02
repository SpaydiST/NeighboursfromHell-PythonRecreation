# -*- coding: utf-8 -*-
# Generated from trigger.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('triggers', {}, [
        n('actor', {'name': 'neighbor'}, [
            n('behavior', {'name': 'alarm'}, [
                n('trigger', {'noise': '2', 'position': 'house', 'type': 'always'}),
            ]),
        ]),
        n('actor', {'name': 'dog'}, [
            n('behavior', {'name': 'wakeup'}, [
                n('trigger', {'noise': '1', 'position': 'room', 'type': 'always'}),
            ]),
        ]),
        n('actor', {'name': 'chili'}, [
            n('behavior', {'name': 'wakeup'}, [
                n('trigger', {'noise': '1', 'position': 'room', 'type': 'always'}),
            ]),
        ]),
    ]),
]
