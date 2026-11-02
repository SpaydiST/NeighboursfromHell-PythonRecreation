# -*- coding: utf-8 -*-
# Generated from combine.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('combination', {'name': 'anc/mum_smeared', 'trick': 'true'}, [
        n('ingredient', {'name': 'anc/mum', 'remove': 'true'}),
        n('ingredient', {'name': 'marker', 'remove': 'true'}),
    ]),
    n('combination', {'name': 'kit/candlebox_boom', 'trick': 'true'}, [
        n('ingredient', {'name': 'kit/candlebox', 'remove': 'true'}),
        n('ingredient', {'name': 'boom', 'remove': 'true'}),
    ]),
    n('combination', {'name': 'toi/toiletstuffed', 'trick': 'true'}, [
        n('ingredient', {'name': 'toi/toilet', 'remove': 'true'}),
        n('ingredient', {'name': 'toiletpaper', 'remove': 'true'}),
    ]),
    n('combination', {'name': 'kit/microwavedirty', 'trick': 'true', 'layer': '2'}, [
        n('ingredient', {'name': 'kit/microwave', 'remove': 'true'}),
        n('ingredient', {'name': 'egg', 'remove': 'true'}),
    ]),
    n('combination', {'name': 'toi/groundsoap', 'trick': 'true'}, [
        n('ingredient', {'name': 'toi', 'remove': 'false'}),
        n('ingredient', {'name': 'soap', 'remove': 'true'}),
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
    n('combination', {'name': 'anc/mailbox_trap', 'trick': 'true'}, [
        n('ingredient', {'name': 'anc/mailbox', 'remove': 'true'}),
        n('ingredient', {'name': 'mousetrap', 'remove': 'true'}),
    ]),
]
