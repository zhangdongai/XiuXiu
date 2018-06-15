#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.NetWork.Packet.PacketDefine import *
from Common.NetWork.Packet.PBMessage_pb2 import *

class CG_CREATEROLE_PAK:
    def __init__(self):
        self.PacketData = CG_CREATEROLE()

    def GetPacketId(self):
        return PACKET_CG_CREATEROLE

    def GetPacketSize(self):
        return self.PacketData.ByteSize()


class CG_CREATEROLE_PAKFactory:
    def __init__(self):
        pass

    def GetPacketId(self):
        return PACKET_CG_CREATEROLE

    def CreatePacket(self):
        return CG_CREATEROLE_PAK()