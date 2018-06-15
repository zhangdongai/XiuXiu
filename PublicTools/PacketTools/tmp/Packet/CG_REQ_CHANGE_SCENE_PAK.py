#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.NetWork.Packet.PacketDefine import *
from Common.NetWork.Packet.PBMessage_pb2 import *

class CG_REQ_CHANGE_SCENE_PAK:
    def __init__(self):
        self.PacketData = CG_REQ_CHANGE_SCENE()

    def GetPacketId(self):
        return PACKET_CG_REQ_CHANGE_SCENE

    def GetPacketSize(self):
        return self.PacketData.ByteSize()


class CG_REQ_CHANGE_SCENE_PAKFactory:
    def __init__(self):
        pass

    def GetPacketId(self):
        return PACKET_CG_REQ_CHANGE_SCENE

    def CreatePacket(self):
        return CG_REQ_CHANGE_SCENE_PAK()