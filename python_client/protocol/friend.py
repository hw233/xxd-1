#!/usr/bin/evn python
#  -*- coding: utf8 -*-

import struct

import interface

FRIEND_TYPE_GAME_FRIEND = 1
FRIEND_TYPE_PLATFORM_FRIEND = 2


FRIEND_MODE_STRANGE = 0
FRIEND_MODE_LISTEN_ONLY = 1
FRIEND_MODE_LISTENED_ONLY = 2
FRIEND_MODE_FRIEND = 3


ADD_RESULT_SUCCEED = 0
ADD_RESULT_FAILED_ADD_SELF = 1
ADD_RESULT_FAILED_ADD_NOT_EXIST = 2
ADD_RESULT_FAILED_ADD_FOLLOW = 3
ADD_RESULT_FAILED_ADD_FULL = 4
ADD_RESULT_FAILED_TARGET_FULL = 5


LISTEND_STATE_CANCEL = 1
LISTEND_STATE_LISTEND = 2


MSG_MODE_SEND = 1
MSG_MODE_RECEIVE = 2


class GetFriendListUp(object):
    _module = 14
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
        

class GetFriendListDown(object):
    _module = 14
    _action = 0

    def __init__(self):
        pass
        self.cancel_listen_count = 0
        self.platform_friend_num = 0
        self.friends = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.cancel_listen_count))
        buff.extend(struct.pack("<l", self.platform_friend_num))
        buff.extend(struct.pack('<B', len(self.friends)))
        for item in self.friends:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.cancel_listen_count = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.platform_friend_num = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        _friends_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_friends_size):
            obj = GetFriendListDownFriends()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.friends.append(obj)

    def size(self):
        size = 9
        for item in self.friends:
            size += item.size()
        return size


class GetFriendListDownFriends(object):
    def __init__(self):
        pass
        self.pid = 0
        self.role_id = 0
        self.nickname = ''
        self.level = 0
        self.fight_num = 0
        self.friend_mode = 0
        self.block_mode = 0
        self.last_chat_time = 0
        self.friend_time = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.pid))
        buff.extend(struct.pack("<b", self.role_id))
        buff.extend(struct.pack('<H', len(self.nickname)))
        buff.extend(self.nickname)
        buff.extend(struct.pack("<h", self.level))
        buff.extend(struct.pack("<l", self.fight_num))
        buff.extend(struct.pack("<B", self.friend_mode))
        buff.extend(struct.pack("<b", self.block_mode))
        buff.extend(struct.pack("<q", self.last_chat_time))
        buff.extend(struct.pack("<q", self.friend_time))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.pid = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8

        self.role_id = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        _nickname_size = struct.unpack_from("<H", raw_msg, idx)[0]
        idx += 2
        self.nickname = str(raw_msg[idx:idx+_nickname_size])
        idx += _nickname_size

        self.level = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.fight_num = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

        self.friend_mode = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1

        self.block_mode = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.last_chat_time = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8

        self.friend_time = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8

    def size(self):
        size = 35
        size += len(self.nickname)
        return size


class ListenByNickUp(object):
    _module = 14
    _action = 1

    def __init__(self):
        pass
        self.nick = ''

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack('<H', len(self.nick)))
        buff.extend(self.nick)
        return buff

    def decode(self, raw_msg):
        idx = 0

        _nick_size = struct.unpack_from("<H", raw_msg, idx)[0]
        idx += 2
        self.nick = str(raw_msg[idx:idx+_nick_size])
        idx += _nick_size

    def size(self):
        size = 4
        size += len(self.nick)
        return size


class ListenByNickDown(object):
    _module = 14
    _action = 1

    def __init__(self):
        pass
        self.result = 0
        self.role_id = 0
        self.nickname = ''
        self.level = 0
        self.fight_num = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<B", self.result))
        buff.extend(struct.pack("<b", self.role_id))
        buff.extend(struct.pack('<H', len(self.nickname)))
        buff.extend(self.nickname)
        buff.extend(struct.pack("<h", self.level))
        buff.extend(struct.pack("<l", self.fight_num))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.result = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1

        self.role_id = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        _nickname_size = struct.unpack_from("<H", raw_msg, idx)[0]
        idx += 2
        self.nickname = str(raw_msg[idx:idx+_nickname_size])
        idx += _nickname_size

        self.level = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

        self.fight_num = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4

    def size(self):
        size = 10
        size += len(self.nickname)
        return size


class CancelListenUp(object):
    _module = 14
    _action = 2

    def __init__(self):
        pass
        self.pid = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.pid))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.pid = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 10
        

class CancelListenDown(object):
    _module = 14
    _action = 2

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
        

class SendHeartUp(object):
    _module = 14
    _action = 3

    def __init__(self):
        pass
        self.nickname = ''
        self.friend_type = 0
        self.pid = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack('<H', len(self.nickname)))
        buff.extend(self.nickname)
        buff.extend(struct.pack("<B", self.friend_type))
        buff.extend(struct.pack("<q", self.pid))
        return buff

    def decode(self, raw_msg):
        idx = 0

        _nickname_size = struct.unpack_from("<H", raw_msg, idx)[0]
        idx += 2
        self.nickname = str(raw_msg[idx:idx+_nickname_size])
        idx += _nickname_size

        self.friend_type = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1

        self.pid = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8

    def size(self):
        size = 13
        size += len(self.nickname)
        return size


class SendHeartDown(object):
    _module = 14
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
        

class ChatUp(object):
    _module = 14
    _action = 4

    def __init__(self):
        pass
        self.pid = 0
        self.message = ''

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.pid))
        buff.extend(struct.pack('<H', len(self.message)))
        buff.extend(self.message)
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.pid = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8

        _message_size = struct.unpack_from("<H", raw_msg, idx)[0]
        idx += 2
        self.message = str(raw_msg[idx:idx+_message_size])
        idx += _message_size

    def size(self):
        size = 12
        size += len(self.message)
        return size


class ChatDown(object):
    _module = 14
    _action = 4

    def __init__(self):
        pass
        self.banned = False

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<?", self.banned))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.banned = struct.unpack_from("<?", raw_msg, idx)[0]
        idx += 1


    @staticmethod
    def size():
        return 1
        

class GetChatHistoryUp(object):
    _module = 14
    _action = 5

    def __init__(self):
        pass
        self.pid = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.pid))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.pid = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 10
        

class GetChatHistoryDown(object):
    _module = 14
    _action = 5

    def __init__(self):
        pass
        self.messages = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack('<B', len(self.messages)))
        for item in self.messages:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        _messages_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_messages_size):
            obj = GetChatHistoryDownMessages()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.messages.append(obj)

    def size(self):
        size = 1
        for item in self.messages:
            size += item.size()
        return size


class GetChatHistoryDownMessages(object):
    def __init__(self):
        pass
        self.mode = 0
        self.id = 0
        self.send_time = 0
        self.message = ''

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<B", self.mode))
        buff.extend(struct.pack("<q", self.id))
        buff.extend(struct.pack("<q", self.send_time))
        buff.extend(struct.pack('<H', len(self.message)))
        buff.extend(self.message)
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.mode = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1

        self.id = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8

        self.send_time = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8

        _message_size = struct.unpack_from("<H", raw_msg, idx)[0]
        idx += 2
        self.message = str(raw_msg[idx:idx+_message_size])
        idx += _message_size

    def size(self):
        size = 19
        size += len(self.message)
        return size


class GetOfflineMessagesDown(object):
    _module = 14
    _action = 6

    def __init__(self):
        pass
        self.chats = []
        self.listener = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack('<B', len(self.chats)))
        for item in self.chats:
            buff.extend(item.encode())
        buff.extend(struct.pack('<B', len(self.listener)))
        for item in self.listener:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        _chats_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_chats_size):
            obj = GetOfflineMessagesDownChats()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.chats.append(obj)

        _listener_size = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1
        for i in range(_listener_size):
            obj = GetOfflineMessagesDownListener()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.listener.append(obj)

    def size(self):
        size = 2
        for item in self.chats:
            size += item.size()
        for item in self.listener:
            size += item.size()
        return size


class GetOfflineMessagesDownChats(object):
    def __init__(self):
        pass
        self.pid = 0
        self.nickname = ''
        self.role_id = 0
        self.level = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.pid))
        buff.extend(struct.pack('<H', len(self.nickname)))
        buff.extend(self.nickname)
        buff.extend(struct.pack("<b", self.role_id))
        buff.extend(struct.pack("<h", self.level))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.pid = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8

        _nickname_size = struct.unpack_from("<H", raw_msg, idx)[0]
        idx += 2
        self.nickname = str(raw_msg[idx:idx+_nickname_size])
        idx += _nickname_size

        self.role_id = struct.unpack_from("<b", raw_msg, idx)[0]
        idx += 1

        self.level = struct.unpack_from("<h", raw_msg, idx)[0]
        idx += 2

    def size(self):
        size = 13
        size += len(self.nickname)
        return size


class GetOfflineMessagesDownListener(object):
    def __init__(self):
        pass
        self.pid = 0
        self.nick = ''

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.pid))
        buff.extend(struct.pack('<H', len(self.nick)))
        buff.extend(self.nick)
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.pid = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8

        _nick_size = struct.unpack_from("<H", raw_msg, idx)[0]
        idx += 2
        self.nick = str(raw_msg[idx:idx+_nick_size])
        idx += _nick_size

    def size(self):
        size = 10
        size += len(self.nick)
        return size


class BlockUp(object):
    _module = 14
    _action = 7

    def __init__(self):
        pass
        self.pid = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.pid))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.pid = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 10
        

class BlockDown(object):
    _module = 14
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
        return 0
        

class CancelBlockUp(object):
    _module = 14
    _action = 8

    def __init__(self):
        pass
        self.pid = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.pid))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.pid = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 10
        

class CancelBlockDown(object):
    _module = 14
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
        

class CleanChatHistoryUp(object):
    _module = 14
    _action = 9

    def __init__(self):
        pass
        self.pid = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.pid))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.pid = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 10
        

class CleanChatHistoryDown(object):
    _module = 14
    _action = 9

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
        

class NotifyListenedStateDown(object):
    _module = 14
    _action = 10

    def __init__(self):
        pass
        self.pid = 0
        self.nick = ''
        self.state = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.pid))
        buff.extend(struct.pack('<H', len(self.nick)))
        buff.extend(self.nick)
        buff.extend(struct.pack("<B", self.state))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.pid = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8

        _nick_size = struct.unpack_from("<H", raw_msg, idx)[0]
        idx += 2
        self.nick = str(raw_msg[idx:idx+_nick_size])
        idx += _nick_size

        self.state = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1

    def size(self):
        size = 11
        size += len(self.nick)
        return size


class CurrentPlatformFriendNumUp(object):
    _module = 14
    _action = 11

    def __init__(self):
        pass
        self.num = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<l", self.num))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.num = struct.unpack_from("<l", raw_msg, idx)[0]
        idx += 4


    @staticmethod
    def size():
        return 6
        

class CurrentPlatformFriendNumDown(object):
    _module = 14
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
        

class GetSendHeartListUp(object):
    _module = 14
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
        return 2
        

class GetSendHeartListDown(object):
    _module = 14
    _action = 12

    def __init__(self):
        pass
        self.friends = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack('<H', len(self.friends)))
        for item in self.friends:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        _friends_size = struct.unpack_from("<H", raw_msg, idx)[0]
        idx += 2
        for i in range(_friends_size):
            obj = GetSendHeartListDownFriends()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.friends.append(obj)

    def size(self):
        size = 2
        for item in self.friends:
            size += item.size()
        return size


class GetSendHeartListDownFriends(object):
    def __init__(self):
        pass
        self.pid = 0
        self.send_heart_time = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<q", self.pid))
        buff.extend(struct.pack("<q", self.send_heart_time))
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.pid = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8

        self.send_heart_time = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8


    @staticmethod
    def size():
        return 16
        

class SendHeartToAllFriendsUp(object):
    _module = 14
    _action = 13

    def __init__(self):
        pass
        self.friend_type = 0
        self.friends = []

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack("<B", self.friend_type))
        buff.extend(struct.pack('<H', len(self.friends)))
        for item in self.friends:
            buff.extend(item.encode())
        return buff

    def decode(self, raw_msg):
        idx = 0

        self.friend_type = struct.unpack_from("<B", raw_msg, idx)[0]
        idx += 1

        _friends_size = struct.unpack_from("<H", raw_msg, idx)[0]
        idx += 2
        for i in range(_friends_size):
            obj = SendHeartToAllFriendsUpFriends()
            obj.decode(raw_msg[idx:])
            idx += obj.size()
            self.friends.append(obj)

    def size(self):
        size = 5
        for item in self.friends:
            size += item.size()
        return size


class SendHeartToAllFriendsUpFriends(object):
    def __init__(self):
        pass
        self.nickname = ''
        self.pid = 0

    def encode(self):
        buff = bytearray()
        buff.extend(struct.pack('<B', self._module))
        buff.extend(struct.pack('<B', self._action))
        buff.extend(struct.pack('<H', len(self.nickname)))
        buff.extend(self.nickname)
        buff.extend(struct.pack("<q", self.pid))
        return buff

    def decode(self, raw_msg):
        idx = 0

        _nickname_size = struct.unpack_from("<H", raw_msg, idx)[0]
        idx += 2
        self.nickname = str(raw_msg[idx:idx+_nickname_size])
        idx += _nickname_size

        self.pid = struct.unpack_from("<q", raw_msg, idx)[0]
        idx += 8

    def size(self):
        size = 10
        size += len(self.nickname)
        return size


class SendHeartToAllFriendsDown(object):
    _module = 14
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
        

class FriendModule(interface.BaseModule):
    decoder_map = {
        0: GetFriendListDown, 
        1: ListenByNickDown, 
        2: CancelListenDown, 
        3: SendHeartDown, 
        4: ChatDown, 
        5: GetChatHistoryDown, 
        6: GetOfflineMessagesDown, 
        7: BlockDown, 
        8: CancelBlockDown, 
        9: CleanChatHistoryDown, 
        10: NotifyListenedStateDown, 
        11: CurrentPlatformFriendNumDown, 
        12: GetSendHeartListDown, 
        13: SendHeartToAllFriendsDown, 
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

    def add_get_friend_list(self, callback):
        self.add_callback(0, callback)

    def add_listen_by_nick(self, callback):
        self.add_callback(1, callback)

    def add_cancel_listen(self, callback):
        self.add_callback(2, callback)

    def add_send_heart(self, callback):
        self.add_callback(3, callback)

    def add_chat(self, callback):
        self.add_callback(4, callback)

    def add_get_chat_history(self, callback):
        self.add_callback(5, callback)

    def add_get_offline_messages(self, callback):
        self.add_callback(6, callback)

    def add_block(self, callback):
        self.add_callback(7, callback)

    def add_cancel_block(self, callback):
        self.add_callback(8, callback)

    def add_clean_chat_history(self, callback):
        self.add_callback(9, callback)

    def add_notify_listened_state(self, callback):
        self.add_callback(10, callback)

    def add_current_platform_friend_num(self, callback):
        self.add_callback(11, callback)

    def add_get_send_heart_list(self, callback):
        self.add_callback(12, callback)

    def add_send_heart_to_all_friends(self, callback):
        self.add_callback(13, callback)
