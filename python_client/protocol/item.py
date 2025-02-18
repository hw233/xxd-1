#!/usr/bin/evn python
#  -*- coding: utf8 -*-

import struct

import interface

EQUIPMENT_POS_WEAPON = 0
EQUIPMENT_POS_CLOTHES = 1
EQUIPMENT_POS_ACCESSORIES = 2
EQUIPMENT_POS_SHOE = 3


ATTRIBUTE_NULL = 0
ATTRIBUTE_ATTACK = 1
ATTRIBUTE_DEFENCE = 2
ATTRIBUTE_HEALTH = 3
ATTRIBUTE_SPEED = 4
ATTRIBUTE_CULTIVATION = 5
ATTRIBUTE_HIT_LEVEL = 6
ATTRIBUTE_CRITICAL_LEVEL = 7
ATTRIBUTE_BLOCK_LEVEL = 8
ATTRIBUTE_DESTROY_LEVEL = 9
ATTRIBUTE_TENACITY_LEVEL = 10
ATTRIBUTE_DODGE_LEVEL = 11
ATTRIBUTE_NUM = 11


class GetAllItemsUp(object):
    _module = 7
    _action = 0

    def __init__(self):
        pass

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        return buff

    def decode(self, raw_msg):
        pass

    @staticmethod
    def size():
        return 2
        

class GetAllItemsDown(object):
    _module = 7
    _action = 0

    def __init__(self):
        pass
        self.items = []
        self.equipments = []
        self.buybacks = []
        self.buy_records = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack('<B', len(self.items)))
        for item in self.items:
            buff.extend(item.encode())
        buff.extend(struct.pack('<B', len(self.equipments)))
        for item in self.equipments:
            buff.extend(item.encode())
        buff.extend(struct.pack('<B', len(self.buybacks)))
        for item in self.buybacks:
            buff.extend(item.encode())
        buff.extend(struct.pack('<B', len(self.buy_records)))
        for item in self.buy_records:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        _items_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_items_size):
            obj = GetAllItemsDownItems()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.items.append(obj)

        _equipments_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_equipments_size):
            obj = GetAllItemsDownEquipments()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.equipments.append(obj)

        _buybacks_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_buybacks_size):
            obj = GetAllItemsDownBuybacks()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.buybacks.append(obj)

        _buy_records_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_buy_records_size):
            obj = GetAllItemsDownBuyRecords()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.buy_records.append(obj)

    def size(self):
        size = 4
        for item in self.items:
            size += item.size()
        for item in self.equipments:
            size += item.size()
        for item in self.buybacks:
            size += item.size()
        for item in self.buy_records:
            size += item.size()
        return size


class GetAllItemsDownItems(object):
    def __init__(self):
        pass
        self.id = 0
        self.item_id = 0
        self.num = 0
        self.attack = 0
        self.defence = 0
        self.health = 0
        self.speed = 0
        self.cultivation = 0
        self.hit_level = 0
        self.critical_level = 0
        self.block_level = 0
        self.destroy_level = 0
        self.tenacity_level = 0
        self.dodge_level = 0
        self.refine_level = 0
        self.refine_fail_times = 0
        self.recast_attr = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.id))
        buff.extend(struct.pack("<h", self.item_id))
        buff.extend(struct.pack("<h", self.num))
        buff.extend(struct.pack("<l", self.attack))
        buff.extend(struct.pack("<l", self.defence))
        buff.extend(struct.pack("<l", self.health))
        buff.extend(struct.pack("<l", self.speed))
        buff.extend(struct.pack("<l", self.cultivation))
        buff.extend(struct.pack("<l", self.hit_level))
        buff.extend(struct.pack("<l", self.critical_level))
        buff.extend(struct.pack("<l", self.block_level))
        buff.extend(struct.pack("<l", self.destroy_level))
        buff.extend(struct.pack("<l", self.tenacity_level))
        buff.extend(struct.pack("<l", self.dodge_level))
        buff.extend(struct.pack("<h", self.refine_level))
        buff.extend(struct.pack("<h", self.refine_fail_times))
        buff.extend(struct.pack("<B", self.recast_attr))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8

        self.item_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.num = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.attack = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.defence = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.health = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.speed = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.cultivation = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.hit_level = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.critical_level = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.block_level = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.destroy_level = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.tenacity_level = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.dodge_level = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.refine_level = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.refine_fail_times = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.recast_attr = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 61
        

class GetAllItemsDownEquipments(object):
    def __init__(self):
        pass
        self.role_id = 0
        self.equips = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<b", self.role_id))
        buff.extend(struct.pack('<B', len(self.equips)))
        for item in self.equips:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.role_id = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        _equips_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_equips_size):
            obj = GetAllItemsDownEquipmentsEquips()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.equips.append(obj)

    def size(self):
        size = 2
        for item in self.equips:
            size += item.size()
        return size


class GetAllItemsDownEquipmentsEquips(object):
    def __init__(self):
        pass
        self.id = 0
        self.item_id = 0
        self.attack = 0
        self.defence = 0
        self.health = 0
        self.speed = 0
        self.cultivation = 0
        self.hit_level = 0
        self.critical_level = 0
        self.block_level = 0
        self.destroy_level = 0
        self.tenacity_level = 0
        self.dodge_level = 0
        self.refine_level = 0
        self.refine_fail_times = 0
        self.recast_attr = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.id))
        buff.extend(struct.pack("<h", self.item_id))
        buff.extend(struct.pack("<l", self.attack))
        buff.extend(struct.pack("<l", self.defence))
        buff.extend(struct.pack("<l", self.health))
        buff.extend(struct.pack("<l", self.speed))
        buff.extend(struct.pack("<l", self.cultivation))
        buff.extend(struct.pack("<l", self.hit_level))
        buff.extend(struct.pack("<l", self.critical_level))
        buff.extend(struct.pack("<l", self.block_level))
        buff.extend(struct.pack("<l", self.destroy_level))
        buff.extend(struct.pack("<l", self.tenacity_level))
        buff.extend(struct.pack("<l", self.dodge_level))
        buff.extend(struct.pack("<h", self.refine_level))
        buff.extend(struct.pack("<h", self.refine_fail_times))
        buff.extend(struct.pack("<B", self.recast_attr))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8

        self.item_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.attack = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.defence = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.health = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.speed = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.cultivation = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.hit_level = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.critical_level = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.block_level = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.destroy_level = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.tenacity_level = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.dodge_level = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.refine_level = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.refine_fail_times = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.recast_attr = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 59
        

class GetAllItemsDownBuybacks(object):
    def __init__(self):
        pass
        self.id = 0
        self.item_id = 0
        self.num = 0
        self.refine_level = 0
        self.recast_attr = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.id))
        buff.extend(struct.pack("<h", self.item_id))
        buff.extend(struct.pack("<h", self.num))
        buff.extend(struct.pack("<h", self.refine_level))
        buff.extend(struct.pack("<B", self.recast_attr))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8

        self.item_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.num = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.refine_level = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.recast_attr = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 15
        

class GetAllItemsDownBuyRecords(object):
    def __init__(self):
        pass
        self.item_id = 0
        self.num = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.item_id))
        buff.extend(struct.pack("<h", self.num))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.item_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.num = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 4
        

class DropItemUp(object):
    _module = 7
    _action = 1

    def __init__(self):
        pass
        self.id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 10
        

class DropItemDown(object):
    _module = 7
    _action = 1

    def __init__(self):
        pass

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        return buff

    def decode(self, raw_msg):
        pass

    @staticmethod
    def size():
        return 0
        

class BuyItemUp(object):
    _module = 7
    _action = 2

    def __init__(self):
        pass
        self.item_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.item_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.item_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 4
        

class BuyItemDown(object):
    _module = 7
    _action = 2

    def __init__(self):
        pass
        self.id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 8
        

class SellItemUp(object):
    _module = 7
    _action = 3

    def __init__(self):
        pass
        self.id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 10
        

class SellItemDown(object):
    _module = 7
    _action = 3

    def __init__(self):
        pass

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        return buff

    def decode(self, raw_msg):
        pass

    @staticmethod
    def size():
        return 0
        

class DressUp(object):
    _module = 7
    _action = 4

    def __init__(self):
        pass
        self.role_id = 0
        self.id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<b", self.role_id))
        buff.extend(struct.pack("<q", self.id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.role_id = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 11
        

class DressDown(object):
    _module = 7
    _action = 4

    def __init__(self):
        pass

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        return buff

    def decode(self, raw_msg):
        pass

    @staticmethod
    def size():
        return 0
        

class UndressUp(object):
    _module = 7
    _action = 5

    def __init__(self):
        pass
        self.role_id = 0
        self.pos = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<b", self.role_id))
        buff.extend(struct.pack("<B", self.pos))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.role_id = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.pos = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 4
        

class UndressDown(object):
    _module = 7
    _action = 5

    def __init__(self):
        pass

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        return buff

    def decode(self, raw_msg):
        pass

    @staticmethod
    def size():
        return 0
        

class BuyItemBackUp(object):
    _module = 7
    _action = 6

    def __init__(self):
        pass
        self.id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 10
        

class BuyItemBackDown(object):
    _module = 7
    _action = 6

    def __init__(self):
        pass
        self.items = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack('<B', len(self.items)))
        for item in self.items:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        _items_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_items_size):
            obj = BuyItemBackDownItems()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.items.append(obj)

    def size(self):
        size = 1
        for item in self.items:
            size += item.size()
        return size


class BuyItemBackDownItems(object):
    def __init__(self):
        pass
        self.id = 0
        self.item_id = 0
        self.num = 0
        self.attack = 0
        self.defence = 0
        self.health = 0
        self.speed = 0
        self.cultivation = 0
        self.hit_level = 0
        self.critical_level = 0
        self.block_level = 0
        self.destroy_level = 0
        self.tenacity_level = 0
        self.dodge_level = 0
        self.refine_level = 0
        self.recast_attr = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.id))
        buff.extend(struct.pack("<h", self.item_id))
        buff.extend(struct.pack("<h", self.num))
        buff.extend(struct.pack("<l", self.attack))
        buff.extend(struct.pack("<l", self.defence))
        buff.extend(struct.pack("<l", self.health))
        buff.extend(struct.pack("<l", self.speed))
        buff.extend(struct.pack("<l", self.cultivation))
        buff.extend(struct.pack("<l", self.hit_level))
        buff.extend(struct.pack("<l", self.critical_level))
        buff.extend(struct.pack("<l", self.block_level))
        buff.extend(struct.pack("<l", self.destroy_level))
        buff.extend(struct.pack("<l", self.tenacity_level))
        buff.extend(struct.pack("<l", self.dodge_level))
        buff.extend(struct.pack("<h", self.refine_level))
        buff.extend(struct.pack("<B", self.recast_attr))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8

        self.item_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.num = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.attack = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.defence = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.health = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.speed = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.cultivation = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.hit_level = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.critical_level = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.block_level = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.destroy_level = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.tenacity_level = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.dodge_level = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.refine_level = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.recast_attr = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 59
        

class IsBagFullUp(object):
    _module = 7
    _action = 7

    def __init__(self):
        pass

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        return buff

    def decode(self, raw_msg):
        pass

    @staticmethod
    def size():
        return 2
        

class IsBagFullDown(object):
    _module = 7
    _action = 7

    def __init__(self):
        pass
        self.is_full = False

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<?", self.is_full))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.is_full = struct.unpack_from("<?", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 1
        

class DecomposeUp(object):
    _module = 7
    _action = 8

    def __init__(self):
        pass
        self.id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 10
        

class DecomposeDown(object):
    _module = 7
    _action = 8

    def __init__(self):
        pass

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        return buff

    def decode(self, raw_msg):
        pass

    @staticmethod
    def size():
        return 0
        

class RefineUp(object):
    _module = 7
    _action = 9

    def __init__(self):
        pass
        self.id = 0
        self.is_batch = False

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.id))
        buff.extend(struct.pack("<?", self.is_batch))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8

        self.is_batch = struct.unpack_from("<?", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 11
        

class RefineDown(object):
    _module = 7
    _action = 9

    def __init__(self):
        pass
        self.code = 0
        self.id = 0
        self.level = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<b", self.code))
        buff.extend(struct.pack("<q", self.id))
        buff.extend(struct.pack("<h", self.level))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.code = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8

        self.level = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 11
        

class GetRecastInfoUp(object):
    _module = 7
    _action = 10

    def __init__(self):
        pass
        self.id = 0
        self.attr = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.id))
        buff.extend(struct.pack("<B", self.attr))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8

        self.attr = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 11
        

class GetRecastInfoDown(object):
    _module = 7
    _action = 10

    def __init__(self):
        pass
        self.attrs = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack('<B', len(self.attrs)))
        for item in self.attrs:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        _attrs_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_attrs_size):
            obj = GetRecastInfoDownAttrs()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.attrs.append(obj)

    def size(self):
        size = 1
        for item in self.attrs:
            size += item.size()
        return size


class GetRecastInfoDownAttrs(object):
    def __init__(self):
        pass
        self.attr = 0
        self.value = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<B", self.attr))
        buff.extend(struct.pack("<l", self.value))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.attr = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1

        self.value = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 5
        

class RecastUp(object):
    _module = 7
    _action = 11

    def __init__(self):
        pass
        self.attr = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<B", self.attr))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.attr = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 3
        

class RecastDown(object):
    _module = 7
    _action = 11

    def __init__(self):
        pass

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        return buff

    def decode(self, raw_msg):
        pass

    @staticmethod
    def size():
        return 0
        

class UseItemUp(object):
    _module = 7
    _action = 12

    def __init__(self):
        pass
        self.id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 10
        

class UseItemDown(object):
    _module = 7
    _action = 12

    def __init__(self):
        pass
        self.origin = 0
        self.changed = False

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.origin))
        buff.extend(struct.pack("<?", self.changed))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.origin = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8

        self.changed = struct.unpack_from("<?", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 9
        

class RoleUseCostItemUp(object):
    _module = 7
    _action = 13

    def __init__(self):
        pass
        self.role_id = 0
        self.item_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<b", self.role_id))
        buff.extend(struct.pack("<q", self.item_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.role_id = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.item_id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 11
        

class RoleUseCostItemDown(object):
    _module = 7
    _action = 13

    def __init__(self):
        pass

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        return buff

    def decode(self, raw_msg):
        pass

    @staticmethod
    def size():
        return 0
        

class BatchUseItemUp(object):
    _module = 7
    _action = 14

    def __init__(self):
        pass
        self.role_id = 0
        self.id = 0
        self.num = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<b", self.role_id))
        buff.extend(struct.pack("<q", self.id))
        buff.extend(struct.pack("<l", self.num))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.role_id = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8

        self.num = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 15
        

class BatchUseItemDown(object):
    _module = 7
    _action = 14

    def __init__(self):
        pass
        self.id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 8
        

class DragonBallExchangeNotifyDown(object):
    _module = 7
    _action = 15

    def __init__(self):
        pass
        self.item_id = 0
        self.item_num = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.item_id))
        buff.extend(struct.pack("<h", self.item_num))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.item_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.item_num = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 4
        

class OpenCornucopiaUp(object):
    _module = 7
    _action = 16

    def __init__(self):
        pass
        self.id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 10
        

class OpenCornucopiaDown(object):
    _module = 7
    _action = 16

    def __init__(self):
        pass
        self.coins = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.coins))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.coins = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 8
        

class GetSealedbooksUp(object):
    _module = 7
    _action = 17

    def __init__(self):
        pass
        self.item_type = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<b", self.item_type))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.item_type = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 3
        

class GetSealedbooksDown(object):
    _module = 7
    _action = 17

    def __init__(self):
        pass
        self.items = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack('<B', len(self.items)))
        for item in self.items:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        _items_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_items_size):
            obj = GetSealedbooksDownItems()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.items.append(obj)

    def size(self):
        size = 1
        for item in self.items:
            size += item.size()
        return size


class GetSealedbooksDownItems(object):
    def __init__(self):
        pass
        self.item_type = 0
        self.item_id = 0
        self.status = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<b", self.item_type))
        buff.extend(struct.pack("<q", self.item_id))
        buff.extend(struct.pack("<b", self.status))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.item_type = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.item_id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8

        self.status = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 10
        

class ActivationSealedbookUp(object):
    _module = 7
    _action = 18

    def __init__(self):
        pass
        self.item_type = 0
        self.item_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<b", self.item_type))
        buff.extend(struct.pack("<q", self.item_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.item_type = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.item_id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 11
        

class ActivationSealedbookDown(object):
    _module = 7
    _action = 18

    def __init__(self):
        pass
        self.result = False

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<?", self.result))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.result = struct.unpack_from("<?", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 1
        

class ExchangeGhostCrystalUp(object):
    _module = 7
    _action = 19

    def __init__(self):
        pass
        self.item_id = 0
        self.exchange_type = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.item_id))
        buff.extend(struct.pack("<b", self.exchange_type))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.item_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.exchange_type = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 5
        

class ExchangeGhostCrystalDown(object):
    _module = 7
    _action = 19

    def __init__(self):
        pass

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        return buff

    def decode(self, raw_msg):
        pass

    @staticmethod
    def size():
        return 0
        

class ItemModule(interface.BaseModule):
    decoder_map = {
        0: GetAllItemsDown, 
        1: DropItemDown, 
        2: BuyItemDown, 
        3: SellItemDown, 
        4: DressDown, 
        5: UndressDown, 
        6: BuyItemBackDown, 
        7: IsBagFullDown, 
        8: DecomposeDown, 
        9: RefineDown, 
        10: GetRecastInfoDown, 
        11: RecastDown, 
        12: UseItemDown, 
        13: RoleUseCostItemDown, 
        14: BatchUseItemDown, 
        15: DragonBallExchangeNotifyDown, 
        16: OpenCornucopiaDown, 
        17: GetSealedbooksDown, 
        18: ActivationSealedbookDown, 
        19: ExchangeGhostCrystalDown, 
    }
    receive_callback = {}

    def decode(self, message):
        action = ord(message[0])
        decoder_maker = self.decoder_map[action]
        msg = decoder_maker()
        msg.decode(message[1:])
        return msg

    def add_callback(self, action, callback):
        if self.receive_callback.has_key(action):
            self.receive_callback[action].append(callback)
        else:
            self.receive_callback[action] = [callback,]

    def clear_callback(self):
        self.receive_callback = {}

    def add_get_all_items(self, callback):
        self.add_callback(0, callback)

    def add_drop_item(self, callback):
        self.add_callback(1, callback)

    def add_buy_item(self, callback):
        self.add_callback(2, callback)

    def add_sell_item(self, callback):
        self.add_callback(3, callback)

    def add_dress(self, callback):
        self.add_callback(4, callback)

    def add_undress(self, callback):
        self.add_callback(5, callback)

    def add_buy_item_back(self, callback):
        self.add_callback(6, callback)

    def add_is_bag_full(self, callback):
        self.add_callback(7, callback)

    def add_decompose(self, callback):
        self.add_callback(8, callback)

    def add_refine(self, callback):
        self.add_callback(9, callback)

    def add_get_recast_info(self, callback):
        self.add_callback(10, callback)

    def add_recast(self, callback):
        self.add_callback(11, callback)

    def add_use_item(self, callback):
        self.add_callback(12, callback)

    def add_role_use_cost_item(self, callback):
        self.add_callback(13, callback)

    def add_batch_use_item(self, callback):
        self.add_callback(14, callback)

    def add_dragon_ball_exchange_notify(self, callback):
        self.add_callback(15, callback)

    def add_open_cornucopia(self, callback):
        self.add_callback(16, callback)

    def add_get_sealedbooks(self, callback):
        self.add_callback(17, callback)

    def add_activation_sealedbook(self, callback):
        self.add_callback(18, callback)

    def add_exchange_ghost_crystal(self, callback):
        self.add_callback(19, callback)
