#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.NetWork.Packet.PacketDefine import *
from Common.NetWork.Packet.PBMessage_pb2 import *

class GC_CREATE_PLAYER_PAK:
    def __init__(self):
        self.PacketData = GC_CREATE_PLAYER()

    def GetPacketId(self):
        return PACKET_GC_CREATE_PLAYER

    def GetPacketSize(self):
        return self.PacketData.ByteSize()


class GC_CREATE_PLAYER_PAKFactory:
    def __init__(self):
        pass

    def GetPacketId(self):
        return PACKET_GC_CREATE_PLAYER

    def CreatePacket(self):
        return GC_CREATE_PLAYER_PAK()