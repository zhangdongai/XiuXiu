#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.NetWork.Packet.PacketDefine import *
from Common.NetWork.Packet.PBMessage_pb2 import *

class GC_RET_RANDOMNAME_PAK:
    def __init__(self):
        self.PacketData = GC_RET_RANDOMNAME()

    def GetPacketId(self):
        return PACKET_GC_RET_RANDOMNAME

    def GetPacketSize(self):
        return self.PacketData.ByteSize()


class GC_RET_RANDOMNAME_PAKFactory:
    def __init__(self):
        pass

    def GetPacketId(self):
        return PACKET_GC_RET_RANDOMNAME

    def CreatePacket(self):
        return GC_RET_RANDOMNAME_PAK()