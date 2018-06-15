#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.NetWork.Packet.PacketDefine import *
from Common.NetWork.Packet.PBMessage_pb2 import *

class GC_MISSION_STATE_PAK:
    def __init__(self):
        self.PacketData = GC_MISSION_STATE()

    def GetPacketId(self):
        return PACKET_GC_MISSION_STATE

    def GetPacketSize(self):
        return self.PacketData.ByteSize()


class GC_MISSION_STATE_PAKFactory:
    def __init__(self):
        pass

    def GetPacketId(self):
        return PACKET_GC_MISSION_STATE

    def CreatePacket(self):
        return GC_MISSION_STATE_PAK()