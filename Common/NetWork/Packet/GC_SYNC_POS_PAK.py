#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.NetWork.Packet.PacketDefine import *
from Common.NetWork.Packet.PBMessage_pb2 import *

class GC_SYNC_POS_PAK:
    def __init__(self):
        self.PacketData = GC_SYNC_POS()

    def GetPacketId(self):
        return PACKET_GC_SYNC_POS

    def GetPacketSize(self):
        return self.PacketData.ByteSize()


class GC_SYNC_POS_PAKFactory:
    def __init__(self):
        pass

    def GetPacketId(self):
        return PACKET_GC_SYNC_POS

    def CreatePacket(self):
        return GC_SYNC_POS_PAK()