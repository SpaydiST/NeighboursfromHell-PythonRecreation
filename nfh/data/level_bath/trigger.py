# -*- coding: utf-8 -*-
# Generated from trigger.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('triggers', {}, [
        n('actor', {'name': 'neighbor'}, [
            n('behavior', {'name': 'mum_smeared'}, [
                n('trigger', {'object': 'anc/mum_smeared', 'position': 'nearobj', 'type': 'once'}),
            ]),
            n('behavior', {'name': 'dirty_microwave'}, [
                n('trigger', {'object': 'kit/microwavedirty', 'position': 'nearobj', 'type': 'once'}),
            ]),
            n('behavior', {'name': 'soap_on_floor'}, [
                n('trigger', {'object': 'toi/groundsoap', 'position': 'nearobj', 'type': 'once'}),
            ]),
            n('behavior', {'name': 'soap_on_floor'}, [
                n('trigger', {'object': 'kit/groundsoap', 'position': 'nearobj', 'type': 'once'}),
            ]),
            n('behavior', {'name': 'stuffed_toilet'}, [
                n('trigger', {'object': 'toi/toiletstuffed', 'position': 'nearobj', 'type': 'once'}),
            ]),
        ]),
    ]),
]
