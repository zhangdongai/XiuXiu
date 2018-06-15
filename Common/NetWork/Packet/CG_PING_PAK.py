#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.NetWork.Packet.PacketDefine import *
from Common.NetWork.Packet.PBMessage_pb2 import *

class CG_PING_PAK:
    def __init__(self):
        self.PacketData = CG_PING()

    def GetPacketId(self):
        return PACKET_CG_PING

    def GetPacketSize(self):
        return self.PacketData.ByteSize()


class CG_PING_PAKFactory:
    def __init__(self):
        pass

    def GetPacketId(self):
        return PACKET_CG_PING

    def CreatePacket(self):
        return CG_PING_PAK()