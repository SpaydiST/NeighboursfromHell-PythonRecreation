# -*- coding: utf-8 -*-
# Generated from level.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('level', {'name': 'level01', 'size': '1428/736', 'angrytime': '240'}, [
        n('object', {'name': 'house', 'layer': '0'}),
        n('room', {'name': 'fro', 'offset': '1236/379', 'path1': '50/218', 'path2': '1840/218'}, [
            n('floor', {'offset': '19/-2', 'size': '905/260', 'wall': 'true'}),
            n('door', {'name': 'fro/anc', 'layer': '2', 'position': '-344/-202'}),
            n('neighbor', {'name': 'anc', 'costs': '1000', 'doorin': 'fro/anc', 'doorout': 'anc/fro'}),
            n('actor', {'name': 'woody', 'layer': '4', 'position': '380/218'}),
        ]),
        n('room', {'name': 'anc', 'offset': '325/177', 'path1': '100/420', 'path2': '840/420'}, [
            n('floor', {'offset': '19/200', 'size': '905/160', 'wall': 'true'}),
            n('floor', {'offset': '37/360', 'size': '283/100', 'hotspot': '230/420'}),
            n('floor', {'offset': '320/360', 'size': '283/100', 'hotspot': '400/420'}),
            n('floor', {'offset': '603/360', 'size': '283/100', 'hotspot': '620/420'}),
            n('object', {'name': 'anc/wardrobe', 'layer': '1'}),
            n('object', {'name': 'anc/ark', 'layer': '1'}),
            n('door', {'name': 'anc/kit', 'layer': '1', 'position': '298/0'}),
            n('door', {'name': 'anc/bas', 'layer': '1', 'position': '93/0'}),
            n('door', {'name': 'anc/lir', 'layer': '1', 'position': '-313/0'}),
            n('door', {'name': 'anc/toi', 'layer': '2', 'position': '-312/0'}),
            n('door', {'name': 'anc/fro', 'layer': '2', 'position': '288/0'}),
            n('neighbor', {'name': 'kit', 'costs': '1000', 'doorin': 'anc/kit', 'doorout': 'kit/anc'}),
            n('neighbor', {'name': 'lir', 'costs': '1000', 'doorin': 'anc/lir', 'doorout': 'lir/anc'}),
            n('neighbor', {'name': 'toi', 'costs': '1000', 'doorin': 'anc/toi', 'doorout': 'toi/anc'}),
            n('neighbor', {'name': 'fro', 'costs': '1000', 'doorin': 'anc/fro', 'doorout': 'fro/anc'}),
        ]),
        n('room', {'name': 'kit', 'offset': '617/-101', 'path1': '276/420', 'path2': '688/420'}, [
            n('floor', {'offset': '226/200', 'size': '518/185', 'wall': 'true'}),
            n('floor', {'offset': '266/385', 'size': '431/66', 'hotspot': '347/410'}),
            n('object', {'name': 'kit/fridge', 'layer': '1'}),
            n('object', {'name': 'kit/microwave', 'layer': '1'}),
            n('object', {'name': 'kit/beer', 'layer': '1'}),
            n('door', {'name': 'kit/anc', 'layer': '1', 'position': '-5/-3'}),
            n('door', {'name': 'kit/lir', 'layer': '2', 'position': '-121/0'}),
            n('neighbor', {'name': 'anc', 'costs': '1000', 'doorin': 'kit/anc', 'doorout': 'anc/kit'}),
            n('neighbor', {'name': 'lir', 'costs': '1000', 'doorin': 'kit/lir', 'doorout': 'lir/kit'}),
        ]),
        n('room', {'name': 'lir', 'offset': '4/-105', 'path1': '184/420', 'path2': '770/420'}, [
            n('floor', {'offset': '110/200', 'size': '720/169', 'wall': 'true'}),
            n('floor', {'offset': '140/369', 'size': '670/83'}),
            n('actor', {'name': 'neighbor', 'layer': '4', 'position': '500/420'}),
            n('object', {'name': 'lir/sofa', 'layer': '2'}),
            n('object', {'name': 'lir/tv', 'layer': '1'}),
            n('door', {'name': 'lir/kit', 'layer': '2', 'position': '211/0'}),
            n('door', {'name': 'lir/anc', 'layer': '1', 'position': '0/0'}),
            n('door', {'name': 'lir/bed', 'layer': '1', 'position': '109/0'}),
            n('neighbor', {'name': 'kit', 'costs': '1000', 'doorin': 'lir/kit', 'doorout': 'kit/lir'}),
            n('neighbor', {'name': 'anc', 'costs': '1000', 'doorin': 'lir/anc', 'doorout': 'anc/lir'}),
        ]),
        n('room', {'name': 'toi', 'offset': '-262/176', 'path1': '402/420', 'path2': '581/420'}, [
            n('floor', {'offset': '344/200', 'size': '275/181', 'wall': 'true'}),
            n('floor', {'offset': '385/381', 'size': '225/73', 'hotspot': '496/420'}),
            n('object', {'name': 'toi/toilet', 'layer': '2'}),
            n('object', {'name': 'toi/firstaid', 'layer': '2'}),
            n('object', {'name': 'toi/paperbracket', 'layer': '1'}),
            n('door', {'name': 'toi/anc', 'layer': '2', 'position': '-1/0'}),
            n('neighbor', {'name': 'anc', 'costs': '1000', 'doorin': 'toi/anc', 'doorout': 'anc/toi'}),
        ]),
    ]),
]
