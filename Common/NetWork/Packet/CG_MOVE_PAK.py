#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.NetWork.Packet.PacketDefine import *
from Common.NetWork.Packet.PBMessage_pb2 import *

class CG_MOVE_PAK:
    def __init__(self):
        self.PacketData = CG_MOVE()

    def GetPacketId(self):
        return PACKET_CG_MOVE

    def GetPacketSize(self):
        return self.PacketData.ByteSize()


class CG_MOVE_PAKFactory:
    def __init__(self):
        pass

    def GetPacketId(self):
        return PACKET_CG_MOVE

    def CreatePacket(self):
        return CG_MOVE_PAK()