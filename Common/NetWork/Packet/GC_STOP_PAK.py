#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.NetWork.Packet.PacketDefine import *
from Common.NetWork.Packet.PBMessage_pb2 import *

class GC_STOP_PAK:
    def __init__(self):
        self.PacketData = GC_STOP()

    def GetPacketId(self):
        return PACKET_GC_STOP

    def GetPacketSize(self):
        return self.PacketData.ByteSize()


class GC_STOP_PAKFactory:
    def __init__(self):
        pass

    def GetPacketId(self):
        return PACKET_GC_STOP

    def CreatePacket(self):
        return GC_STOP_PAK()