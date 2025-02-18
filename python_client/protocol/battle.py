#!/usr/bin/evn python
#  -*- coding: utf8 -*-

import struct

import interface

FIGHTER_TYPE_ATK = 0
FIGHTER_TYPE_DEF = 1


FIGHTER_KIND_PLAYER = 0
FIGHTER_KIND_BUDDY = 1
FIGHTER_KIND_ENEMY = 2


ROUND_EVENT_NONE = 0
ROUND_EVENT_DODGE = 1
ROUND_EVENT_CRIT = 2
ROUND_EVENT_BLOCK = 3
ROUND_EVENT_SQUELCH = 4


ROUND_STATUS_NOT_END = 0
ROUND_STATUS_ATK_WIN = 1
ROUND_STATUS_DEF_WIN = 2
ROUND_STATUS_ATK_NEXT = 3
ROUND_STATUS_DEF_NEXT = 4
ROUND_STATUS_TRIGGER_CALL_ENEMYS = 5
ROUND_STATUS_WAITING = 6


BUFF_MODE_POWER = 0
BUFF_MODE_SPEED = 1
BUFF_MODE_ATTACK = 2
BUFF_MODE_DEFEND = 3
BUFF_MODE_HEALTH = 4
BUFF_MODE_DIZZINESS = 5
BUFF_MODE_POISONING = 6
BUFF_MODE_CLEAN_BAD = 7
BUFF_MODE_CLEAN_GOOD = 8
BUFF_MODE_REDUCE_HURT = 9
BUFF_MODE_RANDOM = 10
BUFF_MODE_BLOCK = 11
BUFF_MODE_BLOCK_LEVEL = 12
BUFF_MODE_DODGE_LEVEL = 13
BUFF_MODE_CRITIAL_LEVEL = 14
BUFF_MODE_HIT_LEVEL = 15
BUFF_MODE_HURT_ADD = 16
BUFF_MODE_MAX_HEALTH = 17
BUFF_MODE_KEEPER_REDUCE_HURT = 18
BUFF_MODE_ATTRACT_FIRE = 19
BUFF_MODE_DESTROY_LEVEL = 20
BUFF_MODE_TENACITY_LEVEL = 21
BUFF_MODE_SUNDER = 22
BUFF_MODE_SLEEP = 23
BUFF_MODE_DISABLE_SKILL = 24
BUFF_MODE_BUFF_DIRECT_REDUCE_HURT = 25
BUFF_MODE_BUFF_ABSORB_HURT = 26
BUFF_MODE_BUFF_GHOST_POWER = 27
BUFF_MODE_BUFF_PET_LIVE_ROUND = 28
BUFF_MODE_BUFF_BUDDY_SKILL = 29
BUFF_MODE_BUFF_CLEAR_ABSORB_HURT = 30
BUFF_MODE_BUFF_SLEEP_LEVEL = 31
BUFF_MODE_BUFF_DIZZINESS_LEVEL = 32
BUFF_MODE_BUFF_RANDOM_LEVEL = 33
BUFF_MODE_BUFF_DISABLE_SKILL_LEVEL = 34
BUFF_MODE_BUFF_POISONING_LEVEL = 35
BUFF_MODE_BUFF_RECOVER_BUDDY_SKILL = 36
BUFF_MODE_BUFF_MAKE_POWER_FULL = 37
BUFF_MODE_BUFF_DOGE = 38
BUFF_MODE_BUFF_HIT = 39
BUFF_MODE_BUFF_CRITIAL = 40
BUFF_MODE_BUFF_TENACITY = 41
BUFF_MODE_BUFF_TAKE_SUNSER = 42
BUFF_MODE_BUFF_DEFEND_PERSENT = 43
BUFF_MODE_BUFF_SUNDER_STATE = 44
BUFF_MODE_BUFF_HEALTH_PERCENT = 45
BUFF_MODE_BUFF_ALL_RESIST = 46
BUFF_MODE_BUFF_REBOTH_HEALTH = 47
BUFF_MODE_BUFF_REBOTH_HEALTH_PERCENT = 48


BATTLE_TYPE_MISSION = 0
BATTLE_TYPE_RESOURCE = 1
BATTLE_TYPE_TOWER = 2
BATTLE_TYPE_MULTILEVEL = 3
BATTLE_TYPE_ARENA = 4
BATTLE_TYPE_HARD = 8
BATTLE_TYPE_BUDDY = 9
BATTLE_TYPE_PET = 10
BATTLE_TYPE_GHOST = 11
BATTLE_TYPE_RAINBOW = 12
BATTLE_TYPE_PVE = 13
BATTLE_TYPE_FATE_BOX = 14
BATTLE_TYPE_DRIVING_EXPLORING = 15
BATTLE_TYPE_DRIVING_SWORD_BF_LEVEL = 16
BATTLE_TYPE_HIJACK_BOAT = 17
BATTLE_TYPE_RECOVER_BOAT = 18


JOB_TYPE_NONE = 0
JOB_TYPE_ATTACKER = 1
JOB_TYPE_DESTROYER = 2
JOB_TYPE_DEFENDER = 3
JOB_TYPE_TREATER = 4
JOB_TYPE_SUPPORTER = 5
JOB_TYPE_OBSTRUCTOR = 6


class BattleRole(object):
    def __init__(self):
        pass
        self.kind = 0
        self.player_id = 0
        self.role_id = 0
        self.role_level = 0
        self.position = 0
        self.fashion_id = 0
        self.friendship_level = 0
        self.health = 0
        self.max_health = 0
        self.power = 0
        self.max_power = 0
        self.sunder_value = 0
        self.sunder_max_value = 0
        self.sunder_min_hurt_rate = 0
        self.sunder_end_hurt_rate = 0
        self.sunder_end_defend_rate = 0
        self.speed = 0
        self.ghost_shield_value = 0
        self.ghost_power = 0
        self.can_use_ghost = False
        self.ghosts = []
        self.could_use_sword_soul = False

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<B", self.kind))
        buff.extend(struct.pack("<q", self.player_id))
        buff.extend(struct.pack("<l", self.role_id))
        buff.extend(struct.pack("<h", self.role_level))
        buff.extend(struct.pack("<l", self.position))
        buff.extend(struct.pack("<h", self.fashion_id))
        buff.extend(struct.pack("<h", self.friendship_level))
        buff.extend(struct.pack("<l", self.health))
        buff.extend(struct.pack("<l", self.max_health))
        buff.extend(struct.pack("<h", self.power))
        buff.extend(struct.pack("<h", self.max_power))
        buff.extend(struct.pack("<h", self.sunder_value))
        buff.extend(struct.pack("<h", self.sunder_max_value))
        buff.extend(struct.pack("<h", self.sunder_min_hurt_rate))
        buff.extend(struct.pack("<h", self.sunder_end_hurt_rate))
        buff.extend(struct.pack("<h", self.sunder_end_defend_rate))
        buff.extend(struct.pack("<l", self.speed))
        buff.extend(struct.pack("<l", self.ghost_shield_value))
        buff.extend(struct.pack("<l", self.ghost_power))
        buff.extend(struct.pack("<?", self.can_use_ghost))
        buff.extend(struct.pack('<B', len(self.ghosts)))
        for item in self.ghosts:
            buff.extend(item.encode())
        buff.extend(struct.pack("<?", self.could_use_sword_soul))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.kind = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1

        self.player_id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8

        self.role_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.role_level = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.position = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.fashion_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.friendship_level = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.health = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.max_health = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.power = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.max_power = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.sunder_value = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.sunder_max_value = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.sunder_min_hurt_rate = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.sunder_end_hurt_rate = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.sunder_end_defend_rate = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.speed = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.ghost_shield_value = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.ghost_power = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.can_use_ghost = struct.unpack_from("<?", raw_msg, idx)[0]
        idx += 1

        _ghosts_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_ghosts_size):
            obj = BattleRoleGhosts()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.ghosts.append(obj)

        self.could_use_sword_soul = struct.unpack_from("<?", raw_msg, idx)[0]
        idx += 1

    def size(self):
        size = 60
        for item in self.ghosts:
            size += item.size()
        return size


class BattleRoleGhosts(object):
    def __init__(self):
        pass
        self.ghost_id = 0
        self.ghost_star = 0
        self.ghost_level = 0
        self.ghost_skill_id = 0
        self.related_ghost = 0
        self.used = False

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.ghost_id))
        buff.extend(struct.pack("<b", self.ghost_star))
        buff.extend(struct.pack("<h", self.ghost_level))
        buff.extend(struct.pack("<l", self.ghost_skill_id))
        buff.extend(struct.pack("<h", self.related_ghost))
        buff.extend(struct.pack("<?", self.used))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.ghost_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.ghost_star = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.ghost_level = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.ghost_skill_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.related_ghost = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.used = struct.unpack_from("<?", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 12
        

class BufferInfo(object):
    def __init__(self):
        pass
        self.mode = 0
        self.keep = 0
        self.value = 0
        self.skill_id = 0
        self.max_override = 0
        self.override_num = 0
        self.uncleanable = False

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<B", self.mode))
        buff.extend(struct.pack("<b", self.keep))
        buff.extend(struct.pack("<l", self.value))
        buff.extend(struct.pack("<h", self.skill_id))
        buff.extend(struct.pack("<b", self.max_override))
        buff.extend(struct.pack("<b", self.override_num))
        buff.extend(struct.pack("<?", self.uncleanable))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.mode = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1

        self.keep = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.value = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.skill_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.max_override = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.override_num = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.uncleanable = struct.unpack_from("<?", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 11
        

class SkillInfo(object):
    def __init__(self):
        pass
        self.skill_id = 0
        self.inc_power = 0
        self.dec_power = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.skill_id))
        buff.extend(struct.pack("<b", self.inc_power))
        buff.extend(struct.pack("<b", self.dec_power))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.skill_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.inc_power = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.dec_power = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 4
        

class StartBattleUp(object):
    _module = 6
    _action = 0

    def __init__(self):
        pass
        self.battle_type = 0
        self.battle_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<B", self.battle_type))
        buff.extend(struct.pack("<q", self.battle_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.battle_type = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1

        self.battle_id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 11
        

class StartBattleDown(object):
    _module = 6
    _action = 0

    def __init__(self):
        pass
        self.total_group = 0
        self.attacker_player_ids = []
        self.is_main_role_first = False
        self.is_attacker_first = False
        self.all_attackers = []
        self.all_defenders = []
        self.attacker_totems = []
        self.defender_totems = []
        self.attacker_groups = []
        self.defender_groups = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<b", self.total_group))
        buff.extend(struct.pack('<B', len(self.attacker_player_ids)))
        for item in self.attacker_player_ids:
            buff.extend(item.encode())
        buff.extend(struct.pack("<?", self.is_main_role_first))
        buff.extend(struct.pack("<?", self.is_attacker_first))
        buff.extend(struct.pack('<B', len(self.all_attackers)))
        for item in self.all_attackers:
            buff.extend(item.encode())
        buff.extend(struct.pack('<B', len(self.all_defenders)))
        for item in self.all_defenders:
            buff.extend(item.encode())
        buff.extend(struct.pack('<B', len(self.attacker_totems)))
        for item in self.attacker_totems:
            buff.extend(item.encode())
        buff.extend(struct.pack('<B', len(self.defender_totems)))
        for item in self.defender_totems:
            buff.extend(item.encode())
        buff.extend(struct.pack('<B', len(self.attacker_groups)))
        for item in self.attacker_groups:
            buff.extend(item.encode())
        buff.extend(struct.pack('<B', len(self.defender_groups)))
        for item in self.defender_groups:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.total_group = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        _attacker_player_ids_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_attacker_player_ids_size):
            obj = StartBattleDownAttackerPlayerIds()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.attacker_player_ids.append(obj)

        self.is_main_role_first = struct.unpack_from("<?", raw_msg, idx)[0]
        idx += 1

        self.is_attacker_first = struct.unpack_from("<?", raw_msg, idx)[0]
        idx += 1

        _all_attackers_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_all_attackers_size):
            obj = StartBattleDownAllAttackers()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.all_attackers.append(obj)

        _all_defenders_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_all_defenders_size):
            obj = StartBattleDownAllDefenders()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.all_defenders.append(obj)

        _attacker_totems_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_attacker_totems_size):
            obj = StartBattleDownAttackerTotems()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.attacker_totems.append(obj)

        _defender_totems_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_defender_totems_size):
            obj = StartBattleDownDefenderTotems()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.defender_totems.append(obj)

        _attacker_groups_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_attacker_groups_size):
            obj = StartBattleDownAttackerGroups()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.attacker_groups.append(obj)

        _defender_groups_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_defender_groups_size):
            obj = StartBattleDownDefenderGroups()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.defender_groups.append(obj)

    def size(self):
        size = 10
        for item in self.attacker_player_ids:
            size += item.size()
        for item in self.all_attackers:
            size += item.size()
        for item in self.all_defenders:
            size += item.size()
        for item in self.attacker_totems:
            size += item.size()
        for item in self.defender_totems:
            size += item.size()
        for item in self.attacker_groups:
            size += item.size()
        for item in self.defender_groups:
            size += item.size()
        return size


class StartBattleDownAttackerPlayerIds(object):
    def __init__(self):
        pass
        self.player_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.player_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.player_id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 8
        

class StartBattleDownAllAttackers(object):
    def __init__(self):
        pass
        self.player_id = 0
        self.ghost_skill_index = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.player_id))
        buff.extend(struct.pack("<b", self.ghost_skill_index))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.player_id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8

        self.ghost_skill_index = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 9
        

class StartBattleDownAllDefenders(object):
    def __init__(self):
        pass
        self.player_id = 0
        self.ghost_skill_index = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.player_id))
        buff.extend(struct.pack("<b", self.ghost_skill_index))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.player_id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8

        self.ghost_skill_index = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 9
        

class StartBattleDownAttackerTotems(object):
    def __init__(self):
        pass
        self.round = 0
        self.totem_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.round))
        buff.extend(struct.pack("<h", self.totem_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.round = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.totem_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 4
        

class StartBattleDownDefenderTotems(object):
    def __init__(self):
        pass
        self.round = 0
        self.totem_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.round))
        buff.extend(struct.pack("<h", self.totem_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.round = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.totem_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 4
        

class StartBattleDownAttackerGroups(object):
    def __init__(self):
        pass
        self.attackers = []
        self.self_buffs = []
        self.buddy_buffs = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack('<B', len(self.attackers)))
        for item in self.attackers:
            buff.extend(item.encode())
        buff.extend(struct.pack('<B', len(self.self_buffs)))
        for item in self.self_buffs:
            buff.extend(item.encode())
        buff.extend(struct.pack('<B', len(self.buddy_buffs)))
        for item in self.buddy_buffs:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        _attackers_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_attackers_size):
            obj = StartBattleDownAttackerGroupsAttackers()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.attackers.append(obj)

        _self_buffs_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_self_buffs_size):
            obj = StartBattleDownAttackerGroupsSelfBuffs()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.self_buffs.append(obj)

        _buddy_buffs_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_buddy_buffs_size):
            obj = StartBattleDownAttackerGroupsBuddyBuffs()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.buddy_buffs.append(obj)

    def size(self):
        size = 3
        for item in self.attackers:
            size += item.size()
        for item in self.self_buffs:
            size += item.size()
        for item in self.buddy_buffs:
            size += item.size()
        return size


class StartBattleDownAttackerGroupsAttackers(object):
    def __init__(self):
        pass
        self.role = BattleRole()
        self.skills = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(self.role.encode())
        buff.extend(struct.pack('<B', len(self.skills)))
        for item in self.skills:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.role.decode(raw_msg[idx:])
        idx += self.role.size()

        _skills_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_skills_size):
            obj = StartBattleDownAttackerGroupsAttackersSkills()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.skills.append(obj)

    def size(self):
        size = 1
        size += self.role.size()
        for item in self.skills:
            size += item.size()
        return size


class StartBattleDownAttackerGroupsAttackersSkills(object):
    def __init__(self):
        pass
        self.skill = SkillInfo()
        self.rest_release_num = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(self.skill.encode())
        buff.extend(struct.pack("<h", self.rest_release_num))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.skill.decode(raw_msg[idx:])
        idx += self.skill.size()

        self.rest_release_num = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

    def size(self):
        size = 2
        size += self.skill.size()
        return size


class StartBattleDownAttackerGroupsSelfBuffs(object):
    def __init__(self):
        pass
        self.buffer = BufferInfo()

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(self.buffer.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.buffer.decode(raw_msg[idx:])
        idx += self.buffer.size()

    def size(self):
        size = 0
        size += self.buffer.size()
        return size


class StartBattleDownAttackerGroupsBuddyBuffs(object):
    def __init__(self):
        pass
        self.pos = 0
        self.buffer = BufferInfo()

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<b", self.pos))
        buff.extend(self.buffer.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.pos = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.buffer.decode(raw_msg[idx:])
        idx += self.buffer.size()

    def size(self):
        size = 1
        size += self.buffer.size()
        return size


class StartBattleDownDefenderGroups(object):
    def __init__(self):
        pass
        self.defenders = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack('<B', len(self.defenders)))
        for item in self.defenders:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        _defenders_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_defenders_size):
            obj = StartBattleDownDefenderGroupsDefenders()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.defenders.append(obj)

    def size(self):
        size = 1
        for item in self.defenders:
            size += item.size()
        return size


class StartBattleDownDefenderGroupsDefenders(object):
    def __init__(self):
        pass
        self.role = BattleRole()
        self.skills = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(self.role.encode())
        buff.extend(struct.pack('<B', len(self.skills)))
        for item in self.skills:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.role.decode(raw_msg[idx:])
        idx += self.role.size()

        _skills_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_skills_size):
            obj = StartBattleDownDefenderGroupsDefendersSkills()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.skills.append(obj)

    def size(self):
        size = 1
        size += self.role.size()
        for item in self.skills:
            size += item.size()
        return size


class StartBattleDownDefenderGroupsDefendersSkills(object):
    def __init__(self):
        pass
        self.skill = SkillInfo()
        self.skill_id2 = 0
        self.rest_release_num = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(self.skill.encode())
        buff.extend(struct.pack("<h", self.skill_id2))
        buff.extend(struct.pack("<h", self.rest_release_num))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.skill.decode(raw_msg[idx:])
        idx += self.skill.size()

        self.skill_id2 = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.rest_release_num = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

    def size(self):
        size = 4
        size += self.skill.size()
        return size


class NextRoundUp(object):
    _module = 6
    _action = 1

    def __init__(self):
        pass
        self.use_skill = 0
        self.use_item = 0
        self.auto_fight = False
        self.is_attacker = False
        self.position = 0
        self.job_index = 0
        self.send_num = 0
        self.use_sword_soul = False
        self.use_ghost_skill_position = 0
        self.use_ghost_skill_id = 0
        self.use_totem = False

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<b", self.use_skill))
        buff.extend(struct.pack("<h", self.use_item))
        buff.extend(struct.pack("<?", self.auto_fight))
        buff.extend(struct.pack("<?", self.is_attacker))
        buff.extend(struct.pack("<b", self.position))
        buff.extend(struct.pack("<b", self.job_index))
        buff.extend(struct.pack("<h", self.send_num))
        buff.extend(struct.pack("<?", self.use_sword_soul))
        buff.extend(struct.pack("<b", self.use_ghost_skill_position))
        buff.extend(struct.pack("<l", self.use_ghost_skill_id))
        buff.extend(struct.pack("<?", self.use_totem))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.use_skill = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.use_item = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.auto_fight = struct.unpack_from("<?", raw_msg, idx)[0]
        idx += 1

        self.is_attacker = struct.unpack_from("<?", raw_msg, idx)[0]
        idx += 1

        self.position = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.job_index = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.send_num = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.use_sword_soul = struct.unpack_from("<?", raw_msg, idx)[0]
        idx += 1

        self.use_ghost_skill_position = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.use_ghost_skill_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.use_totem = struct.unpack_from("<?", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 18
        

class NextRoundDown(object):
    _module = 6
    _action = 1

    def __init__(self):
        pass
        self.status = 0
        self.now_round = 0
        self.all_attackers = []
        self.all_defenders = []
        self.results = []
        self.autos = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<B", self.status))
        buff.extend(struct.pack("<h", self.now_round))
        buff.extend(struct.pack('<B', len(self.all_attackers)))
        for item in self.all_attackers:
            buff.extend(item.encode())
        buff.extend(struct.pack('<B', len(self.all_defenders)))
        for item in self.all_defenders:
            buff.extend(item.encode())
        buff.extend(struct.pack('<B', len(self.results)))
        for item in self.results:
            buff.extend(item.encode())
        buff.extend(struct.pack('<B', len(self.autos)))
        for item in self.autos:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.status = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1

        self.now_round = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        _all_attackers_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_all_attackers_size):
            obj = NextRoundDownAllAttackers()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.all_attackers.append(obj)

        _all_defenders_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_all_defenders_size):
            obj = NextRoundDownAllDefenders()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.all_defenders.append(obj)

        _results_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_results_size):
            obj = NextRoundDownResults()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.results.append(obj)

        _autos_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_autos_size):
            obj = NextRoundDownAutos()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.autos.append(obj)

    def size(self):
        size = 7
        for item in self.all_attackers:
            size += item.size()
        for item in self.all_defenders:
            size += item.size()
        for item in self.results:
            size += item.size()
        for item in self.autos:
            size += item.size()
        return size


class NextRoundDownAllAttackers(object):
    def __init__(self):
        pass
        self.player_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.player_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.player_id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 8
        

class NextRoundDownAllDefenders(object):
    def __init__(self):
        pass
        self.player_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.player_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.player_id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 8
        

class NextRoundDownResults(object):
    def __init__(self):
        pass
        self.ftype = 0
        self.event = 0
        self.position = 0
        self.power = 0
        self.health = 0
        self.sunder_value = 0
        self.use_ghost_skill = False
        self.totem_id = 0
        self.ghost_id = 0
        self.ghost_shield_on = False
        self.shield_ghost_id = 0
        self.ghost_power = 0
        self.add_power = 0
        self.attacks = []
        self.item = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<B", self.ftype))
        buff.extend(struct.pack("<B", self.event))
        buff.extend(struct.pack("<b", self.position))
        buff.extend(struct.pack("<h", self.power))
        buff.extend(struct.pack("<l", self.health))
        buff.extend(struct.pack("<h", self.sunder_value))
        buff.extend(struct.pack("<?", self.use_ghost_skill))
        buff.extend(struct.pack("<h", self.totem_id))
        buff.extend(struct.pack("<h", self.ghost_id))
        buff.extend(struct.pack("<?", self.ghost_shield_on))
        buff.extend(struct.pack("<h", self.shield_ghost_id))
        buff.extend(struct.pack("<l", self.ghost_power))
        buff.extend(struct.pack("<l", self.add_power))
        buff.extend(struct.pack('<B', len(self.attacks)))
        for item in self.attacks:
            buff.extend(item.encode())
        buff.extend(struct.pack('<B', len(self.item)))
        for item in self.item:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.ftype = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1

        self.event = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1

        self.position = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.power = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.health = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.sunder_value = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.use_ghost_skill = struct.unpack_from("<?", raw_msg, idx)[0]
        idx += 1

        self.totem_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.ghost_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.ghost_shield_on = struct.unpack_from("<?", raw_msg, idx)[0]
        idx += 1

        self.shield_ghost_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.ghost_power = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.add_power = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        _attacks_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_attacks_size):
            obj = NextRoundDownResultsAttacks()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.attacks.append(obj)

        _item_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_item_size):
            obj = NextRoundDownResultsItem()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.item.append(obj)

    def size(self):
        size = 29
        for item in self.attacks:
            size += item.size()
        for item in self.item:
            size += item.size()
        return size


class NextRoundDownResultsAttacks(object):
    def __init__(self):
        pass
        self.skill_id = 0
        self.rest_release_num = 0
        self.targets = []
        self.self_buffs = []
        self.buddy_buffs = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.skill_id))
        buff.extend(struct.pack("<h", self.rest_release_num))
        buff.extend(struct.pack('<B', len(self.targets)))
        for item in self.targets:
            buff.extend(item.encode())
        buff.extend(struct.pack('<B', len(self.self_buffs)))
        for item in self.self_buffs:
            buff.extend(item.encode())
        buff.extend(struct.pack('<B', len(self.buddy_buffs)))
        for item in self.buddy_buffs:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.skill_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.rest_release_num = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        _targets_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_targets_size):
            obj = NextRoundDownResultsAttacksTargets()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.targets.append(obj)

        _self_buffs_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_self_buffs_size):
            obj = NextRoundDownResultsAttacksSelfBuffs()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.self_buffs.append(obj)

        _buddy_buffs_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_buddy_buffs_size):
            obj = NextRoundDownResultsAttacksBuddyBuffs()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.buddy_buffs.append(obj)

    def size(self):
        size = 9
        for item in self.targets:
            size += item.size()
        for item in self.self_buffs:
            size += item.size()
        for item in self.buddy_buffs:
            size += item.size()
        return size


class NextRoundDownResultsAttacksTargets(object):
    def __init__(self):
        pass
        self.ftype = 0
        self.hurt = 0
        self.event = 0
        self.position = 0
        self.take_sunder = 0
        self.take_ghost_shield = 0
        self.direct_reduct_hurt = 0
        self.ghost_shield_on = False
        self.shield_ghost_id = 0
        self.ghost_power = 0
        self.buffs = []
        self.passive_attack = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<B", self.ftype))
        buff.extend(struct.pack("<l", self.hurt))
        buff.extend(struct.pack("<B", self.event))
        buff.extend(struct.pack("<b", self.position))
        buff.extend(struct.pack("<h", self.take_sunder))
        buff.extend(struct.pack("<l", self.take_ghost_shield))
        buff.extend(struct.pack("<l", self.direct_reduct_hurt))
        buff.extend(struct.pack("<?", self.ghost_shield_on))
        buff.extend(struct.pack("<h", self.shield_ghost_id))
        buff.extend(struct.pack("<l", self.ghost_power))
        buff.extend(struct.pack('<B', len(self.buffs)))
        for item in self.buffs:
            buff.extend(item.encode())
        buff.extend(struct.pack('<B', len(self.passive_attack)))
        for item in self.passive_attack:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.ftype = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1

        self.hurt = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.event = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1

        self.position = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.take_sunder = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.take_ghost_shield = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.direct_reduct_hurt = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.ghost_shield_on = struct.unpack_from("<?", raw_msg, idx)[0]
        idx += 1

        self.shield_ghost_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.ghost_power = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        _buffs_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_buffs_size):
            obj = NextRoundDownResultsAttacksTargetsBuffs()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.buffs.append(obj)

        _passive_attack_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_passive_attack_size):
            obj = NextRoundDownResultsAttacksTargetsPassiveAttack()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.passive_attack.append(obj)

    def size(self):
        size = 26
        for item in self.buffs:
            size += item.size()
        for item in self.passive_attack:
            size += item.size()
        return size


class NextRoundDownResultsAttacksTargetsBuffs(object):
    def __init__(self):
        pass
        self.buffer = BufferInfo()

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(self.buffer.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.buffer.decode(raw_msg[idx:])
        idx += self.buffer.size()

    def size(self):
        size = 0
        size += self.buffer.size()
        return size


class NextRoundDownResultsAttacksTargetsPassiveAttack(object):
    def __init__(self):
        pass
        self.skill_id = 0
        self.targets = []
        self.buddy_buffs = []
        self.self_buffs = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.skill_id))
        buff.extend(struct.pack('<B', len(self.targets)))
        for item in self.targets:
            buff.extend(item.encode())
        buff.extend(struct.pack('<B', len(self.buddy_buffs)))
        for item in self.buddy_buffs:
            buff.extend(item.encode())
        buff.extend(struct.pack('<B', len(self.self_buffs)))
        for item in self.self_buffs:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.skill_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        _targets_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_targets_size):
            obj = NextRoundDownResultsAttacksTargetsPassiveAttackTargets()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.targets.append(obj)

        _buddy_buffs_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_buddy_buffs_size):
            obj = NextRoundDownResultsAttacksTargetsPassiveAttackBuddyBuffs()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.buddy_buffs.append(obj)

        _self_buffs_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_self_buffs_size):
            obj = NextRoundDownResultsAttacksTargetsPassiveAttackSelfBuffs()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.self_buffs.append(obj)

    def size(self):
        size = 7
        for item in self.targets:
            size += item.size()
        for item in self.buddy_buffs:
            size += item.size()
        for item in self.self_buffs:
            size += item.size()
        return size


class NextRoundDownResultsAttacksTargetsPassiveAttackTargets(object):
    def __init__(self):
        pass
        self.position = 0
        self.buffs = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<b", self.position))
        buff.extend(struct.pack('<B', len(self.buffs)))
        for item in self.buffs:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.position = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        _buffs_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_buffs_size):
            obj = NextRoundDownResultsAttacksTargetsPassiveAttackTargetsBuffs()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.buffs.append(obj)

    def size(self):
        size = 2
        for item in self.buffs:
            size += item.size()
        return size


class NextRoundDownResultsAttacksTargetsPassiveAttackTargetsBuffs(object):
    def __init__(self):
        pass
        self.buffer = BufferInfo()

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(self.buffer.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.buffer.decode(raw_msg[idx:])
        idx += self.buffer.size()

    def size(self):
        size = 0
        size += self.buffer.size()
        return size


class NextRoundDownResultsAttacksTargetsPassiveAttackBuddyBuffs(object):
    def __init__(self):
        pass
        self.pos = 0
        self.buffer = BufferInfo()

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<b", self.pos))
        buff.extend(self.buffer.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.pos = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.buffer.decode(raw_msg[idx:])
        idx += self.buffer.size()

    def size(self):
        size = 1
        size += self.buffer.size()
        return size


class NextRoundDownResultsAttacksTargetsPassiveAttackSelfBuffs(object):
    def __init__(self):
        pass
        self.buffer = BufferInfo()

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(self.buffer.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.buffer.decode(raw_msg[idx:])
        idx += self.buffer.size()

    def size(self):
        size = 0
        size += self.buffer.size()
        return size


class NextRoundDownResultsAttacksSelfBuffs(object):
    def __init__(self):
        pass
        self.buffer = BufferInfo()

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(self.buffer.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.buffer.decode(raw_msg[idx:])
        idx += self.buffer.size()

    def size(self):
        size = 0
        size += self.buffer.size()
        return size


class NextRoundDownResultsAttacksBuddyBuffs(object):
    def __init__(self):
        pass
        self.pos = 0
        self.buffer = BufferInfo()

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<b", self.pos))
        buff.extend(self.buffer.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.pos = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.buffer.decode(raw_msg[idx:])
        idx += self.buffer.size()

    def size(self):
        size = 1
        size += self.buffer.size()
        return size


class NextRoundDownResultsItem(object):
    def __init__(self):
        pass
        self.item_id = 0
        self.targets = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.item_id))
        buff.extend(struct.pack('<B', len(self.targets)))
        for item in self.targets:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.item_id = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        _targets_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_targets_size):
            obj = NextRoundDownResultsItemTargets()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.targets.append(obj)

    def size(self):
        size = 5
        for item in self.targets:
            size += item.size()
        return size


class NextRoundDownResultsItemTargets(object):
    def __init__(self):
        pass
        self.ftype = 0
        self.health = 0
        self.power = 0
        self.hurt = 0
        self.position = 0
        self.buffs = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<B", self.ftype))
        buff.extend(struct.pack("<l", self.health))
        buff.extend(struct.pack("<h", self.power))
        buff.extend(struct.pack("<l", self.hurt))
        buff.extend(struct.pack("<b", self.position))
        buff.extend(struct.pack('<B', len(self.buffs)))
        for item in self.buffs:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.ftype = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1

        self.health = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.power = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.hurt = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.position = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        _buffs_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_buffs_size):
            obj = NextRoundDownResultsItemTargetsBuffs()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.buffs.append(obj)

    def size(self):
        size = 13
        for item in self.buffs:
            size += item.size()
        return size


class NextRoundDownResultsItemTargetsBuffs(object):
    def __init__(self):
        pass
        self.buffer = BufferInfo()

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(self.buffer.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.buffer.decode(raw_msg[idx:])
        idx += self.buffer.size()

    def size(self):
        size = 0
        size += self.buffer.size()
        return size


class NextRoundDownAutos(object):
    def __init__(self):
        pass
        self.player_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.player_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.player_id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 8
        

class EndDown(object):
    _module = 6
    _action = 2

    def __init__(self):
        pass
        self.status = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<B", self.status))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.status = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 1
        

class EscapeUp(object):
    _module = 6
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
        return 2
        

class EscapeDown(object):
    _module = 6
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
        

class FightnumDown(object):
    _module = 6
    _action = 4

    def __init__(self):
        pass
        self.attacker = 0
        self.defender = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.attacker))
        buff.extend(struct.pack("<l", self.defender))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.attacker = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.defender = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 8
        

class StartReadyTimeoutDown(object):
    _module = 6
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
        

class StartReadyUp(object):
    _module = 6
    _action = 6

    def __init__(self):
        pass
        self.ok = False

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<?", self.ok))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.ok = struct.unpack_from("<?", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 3
        

class StartReadyDown(object):
    _module = 6
    _action = 6

    def __init__(self):
        pass
        self.ready_pid = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.ready_pid))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.ready_pid = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 8
        

class StateChangeDown(object):
    _module = 6
    _action = 7

    def __init__(self):
        pass
        self.player_id = 0
        self.auto = False
        self.desc = ''

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.player_id))
        buff.extend(struct.pack("<?", self.auto))
        buff.extend(struct.pack('<H', len(self.desc)))
        buff.extend(self.desc)
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.player_id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8

        self.auto = struct.unpack_from("<?", raw_msg, idx)[0]
        idx += 1

        _desc_size = struct.unpack_from("<H", raw_msg, idx)[0]
        idx += 2
        self.desc = str(raw_msg[idx:idx+_desc_size])
        idx += _desc_size

    def size(self):
        size = 11
        size += len(self.desc)
        return size


class CallBattlePetUp(object):
    _module = 6
    _action = 8

    def __init__(self):
        pass
        self.grid_num = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<b", self.grid_num))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.grid_num = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 3
        

class CallBattlePetDown(object):
    _module = 6
    _action = 8

    def __init__(self):
        pass
        self.success = False
        self.player_power = 0
        self.role = BattleRole()
        self.skills = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<?", self.success))
        buff.extend(struct.pack("<h", self.player_power))
        buff.extend(self.role.encode())
        buff.extend(struct.pack('<B', len(self.skills)))
        for item in self.skills:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.success = struct.unpack_from("<?", raw_msg, idx)[0]
        idx += 1

        self.player_power = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.role.decode(raw_msg[idx:])
        idx += self.role.size()

        _skills_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_skills_size):
            obj = CallBattlePetDownSkills()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.skills.append(obj)

    def size(self):
        size = 4
        size += self.role.size()
        for item in self.skills:
            size += item.size()
        return size


class CallBattlePetDownSkills(object):
    def __init__(self):
        pass
        self.skill = SkillInfo()

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(self.skill.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.skill.decode(raw_msg[idx:])
        idx += self.skill.size()

    def size(self):
        size = 0
        size += self.skill.size()
        return size


class UseBuddySkillUp(object):
    _module = 6
    _action = 9

    def __init__(self):
        pass
        self.pos = 0
        self.use_skill = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<b", self.pos))
        buff.extend(struct.pack("<b", self.use_skill))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.pos = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.use_skill = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 4
        

class UseBuddySkillDown(object):
    _module = 6
    _action = 9

    def __init__(self):
        pass
        self.pos = 0
        self.use_skill = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<b", self.pos))
        buff.extend(struct.pack("<b", self.use_skill))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.pos = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.use_skill = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 2
        

class CallNewEnemysDown(object):
    _module = 6
    _action = 10

    def __init__(self):
        pass
        self.call_info = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack('<B', len(self.call_info)))
        for item in self.call_info:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        _call_info_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_call_info_size):
            obj = CallNewEnemysDownCallInfo()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.call_info.append(obj)

    def size(self):
        size = 1
        for item in self.call_info:
            size += item.size()
        return size


class CallNewEnemysDownCallInfo(object):
    def __init__(self):
        pass
        self.ftype = 0
        self.position = 0
        self.attack_index = 0
        self.enemys = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<b", self.ftype))
        buff.extend(struct.pack("<b", self.position))
        buff.extend(struct.pack("<b", self.attack_index))
        buff.extend(struct.pack('<B', len(self.enemys)))
        for item in self.enemys:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.ftype = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.position = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.attack_index = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        _enemys_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_enemys_size):
            obj = CallNewEnemysDownCallInfoEnemys()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.enemys.append(obj)

    def size(self):
        size = 4
        for item in self.enemys:
            size += item.size()
        return size


class CallNewEnemysDownCallInfoEnemys(object):
    def __init__(self):
        pass
        self.role = BattleRole()
        self.skills = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(self.role.encode())
        buff.extend(struct.pack('<B', len(self.skills)))
        for item in self.skills:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.role.decode(raw_msg[idx:])
        idx += self.role.size()

        _skills_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_skills_size):
            obj = CallNewEnemysDownCallInfoEnemysSkills()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.skills.append(obj)

    def size(self):
        size = 1
        size += self.role.size()
        for item in self.skills:
            size += item.size()
        return size


class CallNewEnemysDownCallInfoEnemysSkills(object):
    def __init__(self):
        pass
        self.skill = SkillInfo()
        self.skill_id2 = 0
        self.rest_release_num = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(self.skill.encode())
        buff.extend(struct.pack("<h", self.skill_id2))
        buff.extend(struct.pack("<h", self.rest_release_num))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.skill.decode(raw_msg[idx:])
        idx += self.skill.size()

        self.skill_id2 = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.rest_release_num = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

    def size(self):
        size = 4
        size += self.skill.size()
        return size


class NewFighterGroupDown(object):
    _module = 6
    _action = 11

    def __init__(self):
        pass
        self.ftype = 0
        self.player_id = 0
        self.ghost_skill_index = 0
        self.fighters = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<b", self.ftype))
        buff.extend(struct.pack("<q", self.player_id))
        buff.extend(struct.pack("<b", self.ghost_skill_index))
        buff.extend(struct.pack('<B', len(self.fighters)))
        for item in self.fighters:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.ftype = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.player_id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8

        self.ghost_skill_index = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        _fighters_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_fighters_size):
            obj = NewFighterGroupDownFighters()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.fighters.append(obj)

    def size(self):
        size = 11
        for item in self.fighters:
            size += item.size()
        return size


class NewFighterGroupDownFighters(object):
    def __init__(self):
        pass
        self.role = BattleRole()
        self.skills = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(self.role.encode())
        buff.extend(struct.pack('<B', len(self.skills)))
        for item in self.skills:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.role.decode(raw_msg[idx:])
        idx += self.role.size()

        _skills_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_skills_size):
            obj = NewFighterGroupDownFightersSkills()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.skills.append(obj)

    def size(self):
        size = 1
        size += self.role.size()
        for item in self.skills:
            size += item.size()
        return size


class NewFighterGroupDownFightersSkills(object):
    def __init__(self):
        pass
        self.skill = SkillInfo()
        self.rest_release_num = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(self.skill.encode())
        buff.extend(struct.pack("<h", self.rest_release_num))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.skill.decode(raw_msg[idx:])
        idx += self.skill.size()

        self.rest_release_num = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

    def size(self):
        size = 2
        size += self.skill.size()
        return size


class StartBattleForHijackBoatUp(object):
    _module = 6
    _action = 12

    def __init__(self):
        pass
        self.pid = 0
        self.boat_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.pid))
        buff.extend(struct.pack("<q", self.boat_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.pid = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8

        self.boat_id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 18
        

class StartBattleForHijackBoatDown(object):
    _module = 6
    _action = 12

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
        

class StartBattleForRecoverBoatUp(object):
    _module = 6
    _action = 13

    def __init__(self):
        pass
        self.pid = 0
        self.boat_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.pid))
        buff.extend(struct.pack("<q", self.boat_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.pid = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8

        self.boat_id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 18
        

class StartBattleForRecoverBoatDown(object):
    _module = 6
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
        

class RoundReadyUp(object):
    _module = 6
    _action = 14

    def __init__(self):
        pass
        self.is_auto = False

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<?", self.is_auto))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.is_auto = struct.unpack_from("<?", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 3
        

class RoundReadyDown(object):
    _module = 6
    _action = 14

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
        

class InitRoundUp(object):
    _module = 6
    _action = 15

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
        

class InitRoundDown(object):
    _module = 6
    _action = 15

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
        

class SetAutoUp(object):
    _module = 6
    _action = 17

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
        

class SetAutoDown(object):
    _module = 6
    _action = 17

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
        

class CancelAutoUp(object):
    _module = 6
    _action = 18

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
        

class CancelAutoDown(object):
    _module = 6
    _action = 18

    def __init__(self):
        pass
        self.round = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<h", self.round))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.round = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 2
        

class SetSkillUp(object):
    _module = 6
    _action = 19

    def __init__(self):
        pass
        self.is_attacker = False
        self.pos_idx = 0
        self.skill_idx = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<?", self.is_attacker))
        buff.extend(struct.pack("<b", self.pos_idx))
        buff.extend(struct.pack("<b", self.skill_idx))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.is_attacker = struct.unpack_from("<?", raw_msg, idx)[0]
        idx += 1

        self.pos_idx = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.skill_idx = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 5
        

class SetSkillDown(object):
    _module = 6
    _action = 19

    def __init__(self):
        pass
        self.pos_idx = 0
        self.skill_idx = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<b", self.pos_idx))
        buff.extend(struct.pack("<b", self.skill_idx))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.pos_idx = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.skill_idx = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 2
        

class UseItemUp(object):
    _module = 6
    _action = 20

    def __init__(self):
        pass
        self.is_attacker = False
        self.position = 0
        self.item_id = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<?", self.is_attacker))
        buff.extend(struct.pack("<b", self.position))
        buff.extend(struct.pack("<h", self.item_id))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.is_attacker = struct.unpack_from("<?", raw_msg, idx)[0]
        idx += 1

        self.position = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.item_id = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2


    @staticmethod
    def size():
        return 6
        

class UseItemDown(object):
    _module = 6
    _action = 20

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
        

class UseGhostUp(object):
    _module = 6
    _action = 21

    def __init__(self):
        pass
        self.is_attacker = False
        self.position = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<?", self.is_attacker))
        buff.extend(struct.pack("<b", self.position))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.is_attacker = struct.unpack_from("<?", raw_msg, idx)[0]
        idx += 1

        self.position = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 4
        

class UseGhostDown(object):
    _module = 6
    _action = 21

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
        

class NotifyReadyDown(object):
    _module = 6
    _action = 22

    def __init__(self):
        pass
        self.Pid = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.Pid))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.Pid = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 8
        

class BattleReconnectUp(object):
    _module = 6
    _action = 23

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
        

class BattleReconnectDown(object):
    _module = 6
    _action = 23

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
        

class BattleModule(interface.BaseModule):
    decoder_map = {
        0: StartBattleDown, 
        1: NextRoundDown, 
        2: EndDown, 
        3: EscapeDown, 
        4: FightnumDown, 
        5: StartReadyTimeoutDown, 
        6: StartReadyDown, 
        7: StateChangeDown, 
        8: CallBattlePetDown, 
        9: UseBuddySkillDown, 
        10: CallNewEnemysDown, 
        11: NewFighterGroupDown, 
        12: StartBattleForHijackBoatDown, 
        13: StartBattleForRecoverBoatDown, 
        14: RoundReadyDown, 
        15: InitRoundDown, 
        17: SetAutoDown, 
        18: CancelAutoDown, 
        19: SetSkillDown, 
        20: UseItemDown, 
        21: UseGhostDown, 
        22: NotifyReadyDown, 
        23: BattleReconnectDown, 
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

    def add_start_battle(self, callback):
        self.add_callback(0, callback)

    def add_next_round(self, callback):
        self.add_callback(1, callback)

    def add_end(self, callback):
        self.add_callback(2, callback)

    def add_escape(self, callback):
        self.add_callback(3, callback)

    def add_fightnum(self, callback):
        self.add_callback(4, callback)

    def add_start_ready_timeout(self, callback):
        self.add_callback(5, callback)

    def add_start_ready(self, callback):
        self.add_callback(6, callback)

    def add_state_change(self, callback):
        self.add_callback(7, callback)

    def add_call_battle_pet(self, callback):
        self.add_callback(8, callback)

    def add_use_buddy_skill(self, callback):
        self.add_callback(9, callback)

    def add_call_new_enemys(self, callback):
        self.add_callback(10, callback)

    def add_new_fighter_group(self, callback):
        self.add_callback(11, callback)

    def add_start_battle_for_hijack_boat(self, callback):
        self.add_callback(12, callback)

    def add_start_battle_for_recover_boat(self, callback):
        self.add_callback(13, callback)

    def add_round_ready(self, callback):
        self.add_callback(14, callback)

    def add_init_round(self, callback):
        self.add_callback(15, callback)

    def add_set_auto(self, callback):
        self.add_callback(17, callback)

    def add_cancel_auto(self, callback):
        self.add_callback(18, callback)

    def add_set_skill(self, callback):
        self.add_callback(19, callback)

    def add_use_item(self, callback):
        self.add_callback(20, callback)

    def add_use_ghost(self, callback):
        self.add_callback(21, callback)

    def add_notify_ready(self, callback):
        self.add_callback(22, callback)

    def add_battle_reconnect(self, callback):
        self.add_callback(23, callback)
