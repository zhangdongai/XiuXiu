#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.NetWork.Packet.CG_PING_PAK import *
from Common.NetWork.Packet.GC_RET_PING_PAK import *
from Common.NetWork.Packet.CG_LOGIN_PAK import *
from Common.NetWork.Packet.GC_LOGIN_RET_PAK import *
from Common.NetWork.Packet.GC_LOGIN_QUEUE_STATUS_PAK import *
from Common.NetWork.Packet.CG_CREATEROLE_PAK import *
from Common.NetWork.Packet.GC_CREATEROLE_RET_PAK import *
from Common.NetWork.Packet.CG_SELECTROLE_PAK import *
from Common.NetWork.Packet.GC_SELECTROLE_RET_PAK import *
from Common.NetWork.Packet.CG_REQ_RANDOMNAME_PAK import *
from Common.NetWork.Packet.GC_RET_RANDOMNAME_PAK import *
from Common.NetWork.Packet.CG_REQ_CHANGE_SCENE_PAK import *
from Common.NetWork.Packet.GC_ENTER_SCENE_PAK import *
from Common.NetWork.Packet.CG_ENTER_SCENE_OK_PAK import *
from Common.NetWork.Packet.CG_CONNECTED_HEARTBEAT_PAK import *
from Common.NetWork.Packet.GC_CONNECTED_HEARTBEAT_PAK import *
from Common.NetWork.Packet.GC_NOTICE_PAK import *
from Common.NetWork.Packet.GC_MISSION_SYNC_MISSIONLIST_PAK import *
from Common.NetWork.Packet.CG_ACCEPTMISSION_PAK import *
from Common.NetWork.Packet.GC_ACCEPTMISSION_RET_PAK import *
from Common.NetWork.Packet.CG_COMPLETEMISSION_PAK import *
from Common.NetWork.Packet.GC_COMPLETEMISSION_RET_PAK import *
from Common.NetWork.Packet.CG_ABANDONMISSION_PAK import *
from Common.NetWork.Packet.GC_ABANDONMISSION_RET_PAK import *
from Common.NetWork.Packet.GC_MISSION_STATE_PAK import *
from Common.NetWork.Packet.GC_MISSION_PARAM_PAK import *
from Common.NetWork.Packet.GC_CREATE_PLAYER_PAK import *
from Common.NetWork.Packet.GC_DELETE_OBJ_PAK import *
from Common.NetWork.Packet.CG_SYNC_POS_PAK import *
from Common.NetWork.Packet.GC_SYNC_POS_PAK import *
from Common.NetWork.Packet.CG_MOVE_PAK import *
from Common.NetWork.Packet.GC_MOVE_PAK import *
from Common.NetWork.Packet.GC_STOP_PAK import *

from Common.Common.Assert import *
class PacketFactoryManager:
    def __init__(self):
        self.FactoryList = [0] * PACKET_MAX

    def Init(self):
        self.AddFactory(CG_PING_PAKFactory())
        self.AddFactory(GC_RET_PING_PAKFactory())
        self.AddFactory(CG_LOGIN_PAKFactory())
        self.AddFactory(GC_LOGIN_RET_PAKFactory())
        self.AddFactory(GC_LOGIN_QUEUE_STATUS_PAKFactory())
        self.AddFactory(CG_CREATEROLE_PAKFactory())
        self.AddFactory(GC_CREATEROLE_RET_PAKFactory())
        self.AddFactory(CG_SELECTROLE_PAKFactory())
        self.AddFactory(GC_SELECTROLE_RET_PAKFactory())
        self.AddFactory(CG_REQ_RANDOMNAME_PAKFactory())
        self.AddFactory(GC_RET_RANDOMNAME_PAKFactory())
        self.AddFactory(CG_REQ_CHANGE_SCENE_PAKFactory())
        self.AddFactory(GC_ENTER_SCENE_PAKFactory())
        self.AddFactory(CG_ENTER_SCENE_OK_PAKFactory())
        self.AddFactory(CG_CONNECTED_HEARTBEAT_PAKFactory())
        self.AddFactory(GC_CONNECTED_HEARTBEAT_PAKFactory())
        self.AddFactory(GC_NOTICE_PAKFactory())
        self.AddFactory(GC_MISSION_SYNC_MISSIONLIST_PAKFactory())
        self.AddFactory(CG_ACCEPTMISSION_PAKFactory())
        self.AddFactory(GC_ACCEPTMISSION_RET_PAKFactory())
        self.AddFactory(CG_COMPLETEMISSION_PAKFactory())
        self.AddFactory(GC_COMPLETEMISSION_RET_PAKFactory())
        self.AddFactory(CG_ABANDONMISSION_PAKFactory())
        self.AddFactory(GC_ABANDONMISSION_RET_PAKFactory())
        self.AddFactory(GC_MISSION_STATE_PAKFactory())
        self.AddFactory(GC_MISSION_PARAM_PAKFactory())
        self.AddFactory(GC_CREATE_PLAYER_PAKFactory())
        self.AddFactory(GC_DELETE_OBJ_PAKFactory())
        self.AddFactory(CG_SYNC_POS_PAKFactory())
        self.AddFactory(GC_SYNC_POS_PAKFactory())
        self.AddFactory(CG_MOVE_PAKFactory())
        self.AddFactory(GC_MOVE_PAKFactory())
        self.AddFactory(GC_STOP_PAKFactory())

    def AddFactory(self, factory):
        self.FactoryList[factory.GetPacketId()] = factory

    def CreatePacket(self, packetId):
        try:
            ASSERT(packetId < PACKET_MAX, 'packetId is out of range')
            return self.FactoryList[packetId].CreatePacket()
        except BaseException as err:
            ASSERT(False, 'PacketFactory:CreatePacket, ' + str(err))
            return None
        return None

gPacketFactoryManager = PacketFactoryManager()