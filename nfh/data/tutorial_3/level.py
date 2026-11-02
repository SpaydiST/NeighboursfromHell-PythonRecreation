# -*- coding: utf-8 -*-
# Generated from level.xml by tools/xml2py.py - do not edit by hand.
from nfh.node import n

ROOTS = [
    n('level', {'name': 'level00', 'size': '1428/796', 'angrytime': '280'}, [
        n('object', {'name': 'house', 'layer': '0'}),
        n('room', {'name': 'fro', 'offset': '1236/439', 'path1': '50/218', 'path2': '1840/218'}, [
            n('floor', {'offset': '19/-2', 'size': '905/260', 'wall': 'true'}),
            n('door', {'name': 'fro/anc', 'layer': '2', 'position': '-344/-202', 'visible': 'false'}),
            n('door', {'name': 'fro/anc_dummy', 'layer': '2', 'position': '-344/-202', 'visible': 'true'}),
            n('neighbor', {'name': 'anc', 'costs': '1000', 'doorin': 'fro/anc', 'doorout': 'anc/fro'}),
            n('actor', {'name': 'HAL', 'layer': '3', 'position': '0/0'}),
        ]),
        n('room', {'name': 'anc', 'offset': '324/237', 'path1': '100/420', 'path2': '840/420'}, [
            n('floor', {'offset': '19/200', 'size': '905/160', 'wall': 'true'}),
            n('floor', {'offset': '37/360', 'size': '283/100', 'hotspot': '230/420'}),
            n('floor', {'offset': '320/360', 'size': '283/100', 'hotspot': '400/420'}),
            n('floor', {'offset': '603/360', 'size': '283/100', 'hotspot': '620/420'}),
            n('actor', {'name': 'woody', 'layer': '4', 'position': '650/420'}),
            n('object', {'name': 'anc/ark_dummy', 'layer': '1'}),
            n('object', {'name': 'anc/wardrobe', 'layer': '1'}),
            n('door', {'name': 'anc/lir', 'layer': '1', 'position': '-313/0', 'visible': 'false'}),
            n('object', {'name': 'anc/lir_dummy', 'layer': '1', 'position': '-313/0', 'visible': 'true'}),
            n('door', {'name': 'anc/fro', 'layer': '2', 'position': '286/0', 'visible': 'false'}),
            n('object', {'name': 'anc/fro_dummy', 'layer': '2', 'position': '286/0', 'visible': 'true'}),
            n('door', {'name': 'anc/kit', 'layer': '1', 'position': '298/0', 'visible': 'false'}),
            n('object', {'name': 'anc/kit_dummy', 'layer': '1', 'position': '298/0', 'visible': 'true'}),
            n('neighbor', {'name': 'lir', 'costs': '1000', 'doorin': 'anc/lir', 'doorout': 'lir/anc'}),
            n('neighbor', {'name': 'fro', 'costs': '1000', 'doorin': 'anc/fro', 'doorout': 'fro/anc'}),
            n('neighbor', {'name': 'kit', 'costs': '1000', 'doorin': 'anc/kit', 'doorout': 'kit/anc'}),
        ]),
        n('room', {'name': 'kit', 'offset': '617/-41', 'path1': '276/420', 'path2': '688/420'}, [
            n('floor', {'offset': '226/200', 'size': '518/185', 'wall': 'true'}),
            n('floor', {'offset': '266/385', 'size': '431/66', 'hotspot': '547/395'}),
            n('actor', {'name': 'dog', 'layer': '2', 'position': '354/410', 'animation': 'sleep'}),
            n('object', {'name': 'kit/sign2', 'layer': '1'}),
            n('door', {'name': 'kit/lir', 'layer': '2', 'position': '-121/-4', 'visible': 'true'}),
            n('object', {'name': 'kit/lir_dummy', 'layer': '2', 'position': '-121/-4', 'visible': 'false'}),
            n('door', {'name': 'kit/anc', 'layer': '1', 'position': '-5/-3', 'visible': 'false'}),
            n('object', {'name': 'kit/anc_dummy', 'layer': '1', 'position': '-5/-3', 'visible': 'true'}),
            n('neighbor', {'name': 'lir', 'costs': '1000', 'doorin': 'kit/lir', 'doorout': 'lir/kit'}),
            n('neighbor', {'name': 'anc', 'costs': '1000', 'doorin': 'kit/anc', 'doorout': 'anc/kit'}),
        ]),
        n('room', {'name': 'lir', 'offset': '3/-48', 'path1': '184/420', 'path2': '770/420'}, [
            n('floor', {'offset': '110/200', 'size': '720/169', 'wall': 'true'}),
            n('floor', {'offset': '140/369', 'size': '670/83', 'hotspot': '347/410'}),
            n('actor', {'name': 'neighbor', 'layer': '4', 'position': '500/420'}),
            n('object', {'name': 'lir/sign1', 'layer': '1'}),
            n('door', {'name': 'lir/kit', 'layer': '2', 'position': '211/0', 'visible': 'true'}),
            n('object', {'name': 'lir/kit_dummy', 'layer': '2', 'position': '211/0', 'visible': 'false'}),
            n('door', {'name': 'lir/anc', 'layer': '1', 'position': '-2/-3', 'visible': 'false'}),
            n('object', {'name': 'lir/anc_dummy', 'layer': '1', 'position': '-2/-3', 'visible': 'true'}),
            n('neighbor', {'name': 'kit', 'costs': '1000', 'doorin': 'lir/kit', 'doorout': 'kit/lir'}),
            n('neighbor', {'name': 'anc', 'costs': '1000', 'doorin': 'lir/anc', 'doorout': 'anc/lir'}),
        ]),
    ]),
]
