#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.NetWork.Packet.PacketDefine import *
from Common.NetWork.Packet.PBMessage_pb2 import *

class GC_ENTER_SCENE_PAK:
    def __init__(self):
        self.PacketData = GC_ENTER_SCENE()

    def GetPacketId(self):
        return PACKET_GC_ENTER_SCENE

    def GetPacketSize(self):
        return self.PacketData.ByteSize()


class GC_ENTER_SCENE_PAKFactory:
    def __init__(self):
        pass

    def GetPacketId(self):
        return PACKET_GC_ENTER_SCENE

    def CreatePacket(self):
        return GC_ENTER_SCENE_PAK()