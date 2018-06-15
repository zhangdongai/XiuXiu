#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.NetWork.Packet.PacketDefine import *
from Common.NetWork.Packet.PBMessage_pb2 import *

class CG_ENTER_SCENE_OK_PAK:
    def __init__(self):
        self.PacketData = CG_ENTER_SCENE_OK()

    def GetPacketId(self):
        return PACKET_CG_ENTER_SCENE_OK

    def GetPacketSize(self):
        return self.PacketData.ByteSize()


class CG_ENTER_SCENE_OK_PAKFactory:
    def __init__(self):
        pass

    def GetPacketId(self):
        return PACKET_CG_ENTER_SCENE_OK

    def CreatePacket(self):
        return CG_ENTER_SCENE_OK_PAK()