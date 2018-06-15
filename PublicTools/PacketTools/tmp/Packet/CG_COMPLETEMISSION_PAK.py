#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.NetWork.Packet.PacketDefine import *
from Common.NetWork.Packet.PBMessage_pb2 import *

class CG_COMPLETEMISSION_PAK:
    def __init__(self):
        self.PacketData = CG_COMPLETEMISSION()

    def GetPacketId(self):
        return PACKET_CG_COMPLETEMISSION

    def GetPacketSize(self):
        return self.PacketData.ByteSize()


class CG_COMPLETEMISSION_PAKFactory:
    def __init__(self):
        pass

    def GetPacketId(self):
        return PACKET_CG_COMPLETEMISSION

    def CreatePacket(self):
        return CG_COMPLETEMISSION_PAK()