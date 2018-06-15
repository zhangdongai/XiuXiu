#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.NetWork.Packet.PacketDefine import *
from Common.NetWork.Packet.PBMessage_pb2 import *

class CG_ACCEPTMISSION_PAK:
    def __init__(self):
        self.PacketData = CG_ACCEPTMISSION()

    def GetPacketId(self):
        return PACKET_CG_ACCEPTMISSION

    def GetPacketSize(self):
        return self.PacketData.ByteSize()


class CG_ACCEPTMISSION_PAKFactory:
    def __init__(self):
        pass

    def GetPacketId(self):
        return PACKET_CG_ACCEPTMISSION

    def CreatePacket(self):
        return CG_ACCEPTMISSION_PAK()