# -*- coding: utf-8 -*-
# Generated from combine.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('combine', {}, [
        n('combination', {'name': 'bal/picture_smeared', 'trick': 'true'}, [
            n('ingredient', {'name': 'bal/picture', 'remove': 'true'}),
            n('ingredient', {'name': 'antispot', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'kit/stool_pins', 'trick': 'true'}, [
            n('ingredient', {'name': 'kit/stool', 'remove': 'true'}),
            n('ingredient', {'name': 'pins', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'kit/groundbanana', 'trick': 'true'}, [
            n('ingredient', {'name': 'kit', 'remove': 'false'}),
            n('ingredient', {'name': 'banana', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'wrong_no_neighbor', 'wrong': 'true'}, [
            n('ingredient', {'name': 'toi', 'remove': 'false'}),
            n('ingredient', {'name': 'banana', 'remove': 'false'}),
        ]),
        n('combination', {'name': 'wrong_no_neighbor', 'wrong': 'true'}, [
            n('ingredient', {'name': 'anc', 'remove': 'false'}),
            n('ingredient', {'name': 'banana', 'remove': 'false'}),
        ]),
        n('combination', {'name': 'bed/groundbanana', 'trick': 'true'}, [
            n('ingredient', {'name': 'bed', 'remove': 'false'}),
            n('ingredient', {'name': 'banana', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bal/groundbanana', 'trick': 'true'}, [
            n('ingredient', {'name': 'bal', 'remove': 'false'}),
            n('ingredient', {'name': 'banana', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'lir/groundbanana', 'trick': 'true'}, [
            n('ingredient', {'name': 'lir', 'remove': 'false'}),
            n('ingredient', {'name': 'banana', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'kit/potterswheel_fast', 'trick': 'true'}, [
            n('ingredient', {'name': 'kit/potterswheel', 'remove': 'true'}),
            n('ingredient', {'name': 'wrench', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bed/camera_flashy', 'trick': 'true'}, [
            n('ingredient', {'name': 'bed/camera', 'remove': 'true'}),
            n('ingredient', {'name': 'magnesium', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'lir/footstool_unlocked', 'trick': 'true'}, [
            n('ingredient', {'name': 'lir/footstool', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'bal/dove_free', 'trick': 'true'}, [
            n('ingredient', {'name': 'aux', 'remove': 'true'}),
            n('ingredient', {'name': 'scissors', 'remove': 'true'}),
        ]),
        n('combination', {'name': 'antispotempty', 'wrong': 'true'}, [
            n('ingredient', {'name': 'bal/picture_empty', 'remove': 'false'}),
            n('ingredient', {'name': 'antispot', 'remove': 'false'}),
        ]),
    ]),
]
