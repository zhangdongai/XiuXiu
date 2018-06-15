#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.NetWork.Packet.PacketDefine import *
from Common.NetWork.Packet.PBMessage_pb2 import *

class GC_DELETE_OBJ_PAK:
    def __init__(self):
        self.PacketData = GC_DELETE_OBJ()

    def GetPacketId(self):
        return PACKET_GC_DELETE_OBJ

    def GetPacketSize(self):
        return self.PacketData.ByteSize()


class GC_DELETE_OBJ_PAKFactory:
    def __init__(self):
        pass

    def GetPacketId(self):
        return PACKET_GC_DELETE_OBJ

    def CreatePacket(self):
        return GC_DELETE_OBJ_PAK()