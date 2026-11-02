# -*- coding: utf-8 -*-
# Generated from leveldata.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('leveldata', {}, [
        n('set', {'name': 'tutorial', 'state': 'playable'}, [
            n('level', {'name': 'tutorial_1', 'state': 'playable', 'reachable': '1', 'minquota': '100', 'time': '0'}),
            n('level', {'name': 'tutorial_2', 'state': 'playable', 'reachable': '2', 'minquota': '97', 'time': '0'}),
            n('level', {'name': 'tutorial_3', 'state': 'playable', 'reachable': '1', 'minquota': '100', 'time': '0'}),
        ]),
        n('set', {'name': 'set01', 'nextset': 'set02', 'state': 'playable'}, [
            n('level', {'name': 'level_peep', 'state': 'playable', 'reachable': '4', 'minquota': '50', 'time': '3600'}),
            n('level', {'name': 'level_sofa', 'state': 'playable', 'reachable': '6', 'minquota': '55', 'time': '3600'}),
            n('level', {'name': 'level_mail', 'state': 'playable', 'reachable': '6', 'minquota': '60', 'time': '3600'}),
            n('level', {'name': 'level_pie', 'state': 'playable', 'reachable': '7', 'minquota': '65', 'time': '4320'}),
            n('level', {'name': 'level_piano', 'state': 'playable', 'reachable': '8', 'minquota': '70', 'time': '4320'}),
            n('level', {'name': 'level_bath', 'state': 'playable', 'reachable': '9', 'minquota': '75', 'time': '4320'}),
        ]),
        n('set', {'name': 'set02', 'nextset': 'set03', 'state': 'locked'}, [
            n('level', {'name': 'level_art', 'state': 'locked', 'reachable': '7', 'minquota': '60', 'time': '5040'}),
            n('level', {'name': 'level_suntan', 'state': 'locked', 'reachable': '6', 'minquota': '65', 'time': '5040'}),
            n('level', {'name': 'level_pig', 'state': 'locked', 'reachable': '7', 'minquota': '70', 'time': '5040'}),
            n('level', {'name': 'level_barbecue', 'state': 'locked', 'reachable': '6', 'minquota': '75', 'time': '5040'}),
        ]),
        n('set', {'name': 'set03', 'state': 'locked'}, [
            n('level', {'name': 'level_laundry', 'state': 'locked', 'reachable': '8', 'minquota': '60', 'time': '7200'}),
            n('level', {'name': 'level_fitness', 'state': 'locked', 'reachable': '10', 'minquota': '65', 'time': '7200'}),
            n('level', {'name': 'level_DIY', 'state': 'locked', 'reachable': '8', 'minquota': '70', 'time': '7200'}),
            n('level', {'name': 'level_hunter', 'state': 'locked', 'reachable': '9', 'minquota': '75', 'time': '7200'}),
        ]),
    ]),
]
