#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.NetWork.Packet.PacketDefine import *
from Common.NetWork.Packet.PBMessage_pb2 import *

class CG_CONNECTED_HEARTBEAT_PAK:
    def __init__(self):
        self.PacketData = CG_CONNECTED_HEARTBEAT()

    def GetPacketId(self):
        return PACKET_CG_CONNECTED_HEARTBEAT

    def GetPacketSize(self):
        return self.PacketData.ByteSize()


class CG_CONNECTED_HEARTBEAT_PAKFactory:
    def __init__(self):
        pass

    def GetPacketId(self):
        return PACKET_CG_CONNECTED_HEARTBEAT

    def CreatePacket(self):
        return CG_CONNECTED_HEARTBEAT_PAK()