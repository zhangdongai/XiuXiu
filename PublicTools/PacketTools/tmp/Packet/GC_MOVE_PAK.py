#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.NetWork.Packet.PacketDefine import *
from Common.NetWork.Packet.PBMessage_pb2 import *

class GC_MOVE_PAK:
    def __init__(self):
        self.PacketData = GC_MOVE()

    def GetPacketId(self):
        return PACKET_GC_MOVE

    def GetPacketSize(self):
        return self.PacketData.ByteSize()


class GC_MOVE_PAKFactory:
    def __init__(self):
        pass

    def GetPacketId(self):
        return PACKET_GC_MOVE

    def CreatePacket(self):
        return GC_MOVE_PAK()