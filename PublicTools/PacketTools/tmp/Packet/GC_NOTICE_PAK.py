#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.NetWork.Packet.PacketDefine import *
from Common.NetWork.Packet.PBMessage_pb2 import *

class GC_NOTICE_PAK:
    def __init__(self):
        self.PacketData = GC_NOTICE()

    def GetPacketId(self):
        return PACKET_GC_NOTICE

    def GetPacketSize(self):
        return self.PacketData.ByteSize()


class GC_NOTICE_PAKFactory:
    def __init__(self):
        pass

    def GetPacketId(self):
        return PACKET_GC_NOTICE

    def CreatePacket(self):
        return GC_NOTICE_PAK()