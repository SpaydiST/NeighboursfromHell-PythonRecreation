# -*- coding: utf-8 -*-
# Generated from combine.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('combination', {'name': 'anc/mum_smeared', 'trick': 'true'}, [
        n('ingredient', {'name': 'anc/mum', 'remove': 'true'}),
        n('ingredient', {'name': 'marker', 'remove': 'true'}),
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
    n('combination', {'name': 'toi/tub_hair', 'trick': 'true'}, [
        n('ingredient', {'name': 'toi/tub', 'remove': 'true'}),
        n('ingredient', {'name': 'hairrestorer', 'remove': 'true'}),
    ]),
    n('combination', {'name': 'toi/dirtytowel', 'trick': 'true'}, [
        n('ingredient', {'name': 'toi/towel', 'remove': 'true'}),
        n('ingredient', {'name': 'shoepolish', 'remove': 'true'}),
    ]),
    n('combination', {'name': 'lir/bathcandy', 'trick': 'true'}, [
        n('ingredient', {'name': 'lir/candy', 'remove': 'true'}),
        n('ingredient', {'name': 'foamballs', 'remove': 'true'}),
    ]),
    n('combination', {'name': 'kit/foambottle', 'trick': 'true'}, [
        n('ingredient', {'name': 'kit/milkbottle', 'remove': 'true'}),
        n('ingredient', {'name': 'fullbottle', 'remove': 'true'}),
    ]),
    n('combination', {'name': 'fullbottle'}, [
        n('ingredient', {'name': 'emptybottle', 'remove': 'true'}),
        n('ingredient', {'name': 'toi/tub_hair', 'remove': 'false'}),
    ]),
    n('combination', {'name': 'fullbottle'}, [
        n('ingredient', {'name': 'emptybottle', 'remove': 'true'}),
        n('ingredient', {'name': 'toi/tub', 'remove': 'false'}),
    ]),
    n('combination', {'name': 'lir/stickybook', 'trick': 'true'}, [
        n('ingredient', {'name': 'glue', 'remove': 'true'}),
        n('ingredient', {'name': 'lir/book', 'remove': 'true'}),
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
    n('combination', {'name': 'wrongtub_hair', 'wrong': 'true'}, [
        n('ingredient', {'name': 'toi/tub_empty', 'remove': 'false'}),
        n('ingredient', {'name': 'hairrestorer', 'remove': 'false'}),
    ]),
]
