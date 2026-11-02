# -*- coding: utf-8 -*-
# Generated from combine.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('combine', {}, [
        n('combination', {'name': 'anc/fuse', 'trick': 'true'}, [
            n('ingredient', {'name': 'anc/no_fuse', 'remove': 'true'}),
            n('ingredient', {'name': 'fuse', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'lir/stoolkit_pain', 'trick': 'true'}, [
            n('ingredient', {'name': 'lir/stoolkit', 'remove': 'true'}),
            n('ingredient', {'name': 'painbook', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'wor/ladder_cut', 'trick': 'true'}, [
            n('ingredient', {'name': 'wor/ladder', 'remove': 'true'}),
            n('ingredient', {'name': 'tongs', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bal/anglegrinder_manipulated', 'trick': 'true'}, [
            n('ingredient', {'name': 'bal/anglegrinder', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bas/water'}, [
            n('ingredient', {'name': 'bas/tatter', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bas/valve_off'}, [
            n('ingredient', {'name': 'bas/valve_on', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bas/valve_on'}, [
            n('ingredient', {'name': 'bas/valve_off', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bas/heatvalve_off'}, [
            n('ingredient', {'name': 'bas/heatvalve_on', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bas/heatvalve_on'}, [
            n('ingredient', {'name': 'bas/heatvalve_off', 'remove': 'true'}),
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
        n('combination', {'name': 'toi/marbles', 'trick': 'true'}, [
            n('ingredient', {'name': 'toi', 'remove': 'false'}),
            n('ingredient', {'name': 'marbles', 'remove': 'true'}),
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
        n('combination', {'name': 'wrongelectrotrap', 'wrong': 'true'}, [
            n('ingredient', {'name': 'bas/outlet_no_water', 'remove': 'false'}),
            n('ingredient', {'name': 'cable', 'remove': 'false'}),
        ]),
    ]),
]
