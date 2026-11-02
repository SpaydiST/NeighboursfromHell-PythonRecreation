# -*- coding: utf-8 -*-
# Generated from combine.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('combination', {'name': 'anc/mum_smeared', 'trick': 'true'}, [
        n('ingredient', {'name': 'anc/mum', 'remove': 'true'}),
        n('ingredient', {'name': 'marker', 'remove': 'false'}),
    ]),
    n('combination', {'name': 'toi/toiletstuffed', 'trick': 'true'}, [
        n('ingredient', {'name': 'toi/toilet', 'remove': 'true'}),
        n('ingredient', {'name': 'toiletpaper', 'remove': 'true'}),
    ]),
    n('combination', {'name': 'kit/microwavedirty', 'trick': 'true'}, [
        n('ingredient', {'name': 'kit/microwave', 'remove': 'true'}),
        n('ingredient', {'name': 'egg', 'remove': 'true'}),
    ]),
    n('combination', {'name': 'toi/groundsoap', 'trick': 'true'}, [
        n('ingredient', {'name': 'toi', 'remove': 'false'}),
        n('ingredient', {'name': 'soap', 'remove': 'true'}),
    ]),
    n('combination', {'name': 'anc/stinkflower', 'trick': 'true'}, [
        n('ingredient', {'name': 'anc/flower', 'remove': 'true'}),
        n('ingredient', {'name': 'cheese', 'remove': 'true'}),
    ]),
    n('combination', {'name': 'lir/scoresmeared', 'trick': 'true'}, [
        n('ingredient', {'name': 'lir/score', 'remove': 'true'}),
        n('ingredient', {'name': 'marker', 'remove': 'false'}),
    ]),
    n('combination', {'name': 'kit/bowlingball', 'trick': 'true'}, [
        n('ingredient', {'name': 'bowling', 'remove': 'true'}),
        n('ingredient', {'name': 'kit/football', 'remove': 'true'}),
    ]),
    n('combination', {'name': 'anc/phoneringing', 'animation': 'ring'}, [
        n('ingredient', {'name': 'handy', 'remove': 'false'}),
        n('ingredient', {'name': 'anc/phone', 'remove': 'true'}),
    ]),
    n('combination', {'name': 'kit/groundsoap', 'trick': 'true'}, [
        n('ingredient', {'name': 'kit', 'remove': 'false'}),
        n('ingredient', {'name': 'soap', 'remove': 'true'}),
    ]),
    n('combination', {'name': 'wrong_soap', 'wrong': 'true'}, [
        n('ingredient', {'name': 'anc', 'remove': 'false'}),
        n('ingredient', {'name': 'soap', 'remove': 'false'}),
    ]),
    n('combination', {'name': 'wrong_soap', 'wrong': 'true'}, [
        n('ingredient', {'name': 'lir', 'remove': 'false'}),
        n('ingredient', {'name': 'soap', 'remove': 'false'}),
    ]),
    n('combination', {'name': 'kit/wrongbowling', 'wrong': 'true'}, [
        n('ingredient', {'name': 'bowling', 'remove': 'false'}),
        n('ingredient', {'name': 'kit', 'remove': 'false'}),
    ]),
]
