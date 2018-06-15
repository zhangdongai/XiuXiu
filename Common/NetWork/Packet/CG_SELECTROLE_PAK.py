#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.NetWork.Packet.PacketDefine import *
from Common.NetWork.Packet.PBMessage_pb2 import *

class CG_SELECTROLE_PAK:
    def __init__(self):
        self.PacketData = CG_SELECTROLE()

    def GetPacketId(self):
        return PACKET_CG_SELECTROLE

    def GetPacketSize(self):
        return self.PacketData.ByteSize()


class CG_SELECTROLE_PAKFactory:
    def __init__(self):
        pass

    def GetPacketId(self):
        return PACKET_CG_SELECTROLE

    def CreatePacket(self):
        return CG_SELECTROLE_PAK()