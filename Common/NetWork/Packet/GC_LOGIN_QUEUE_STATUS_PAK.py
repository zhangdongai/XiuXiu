#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.NetWork.Packet.PacketDefine import *
from Common.NetWork.Packet.PBMessage_pb2 import *

class GC_LOGIN_QUEUE_STATUS_PAK:
    def __init__(self):
        self.PacketData = GC_LOGIN_QUEUE_STATUS()

    def GetPacketId(self):
        return PACKET_GC_LOGIN_QUEUE_STATUS

    def GetPacketSize(self):
        return self.PacketData.ByteSize()


class GC_LOGIN_QUEUE_STATUS_PAKFactory:
    def __init__(self):
        pass

    def GetPacketId(self):
        return PACKET_GC_LOGIN_QUEUE_STATUS

    def CreatePacket(self):
        return GC_LOGIN_QUEUE_STATUS_PAK()