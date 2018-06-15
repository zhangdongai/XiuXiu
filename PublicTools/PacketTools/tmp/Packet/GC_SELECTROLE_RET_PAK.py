#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.NetWork.Packet.PacketDefine import *
from Common.NetWork.Packet.PBMessage_pb2 import *

class GC_SELECTROLE_RET_PAK:
    def __init__(self):
        self.PacketData = GC_SELECTROLE_RET()

    def GetPacketId(self):
        return PACKET_GC_SELECTROLE_RET

    def GetPacketSize(self):
        return self.PacketData.ByteSize()


class GC_SELECTROLE_RET_PAKFactory:
    def __init__(self):
        pass

    def GetPacketId(self):
        return PACKET_GC_SELECTROLE_RET

    def CreatePacket(self):
        return GC_SELECTROLE_RET_PAK()