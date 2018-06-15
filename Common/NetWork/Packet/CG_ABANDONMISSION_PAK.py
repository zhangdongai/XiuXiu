#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.NetWork.Packet.PacketDefine import *
from Common.NetWork.Packet.PBMessage_pb2 import *

class CG_ABANDONMISSION_PAK:
    def __init__(self):
        self.PacketData = CG_ABANDONMISSION()

    def GetPacketId(self):
        return PACKET_CG_ABANDONMISSION

    def GetPacketSize(self):
        return self.PacketData.ByteSize()


class CG_ABANDONMISSION_PAKFactory:
    def __init__(self):
        pass

    def GetPacketId(self):
        return PACKET_CG_ABANDONMISSION

    def CreatePacket(self):
        return CG_ABANDONMISSION_PAK()