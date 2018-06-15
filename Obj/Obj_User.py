#!/usr/bin/python
# -*-coding: utf-8 -*-

from Common.Message.DBMsg import *
from Service.ServiceManager import *
from Common.Player.PlayerDefine import *
from Log.Log import *
from Common.Common.Assert import *
from DB.DBStruct.DBStruct_UserData import *
from Common.Scene.GameDefine_Scene import *
from Common.Money.GameStruct_Money import *
from Obj.Obj_Character import *
from Common.NetWork.Packet.GC_ENTER_SCENE_PAK import *
from Common.Table.Table_SceneClass import *
from Common.NetWork.Packet.GC_CREATE_PLAYER_PAK import *

class Obj_User(Obj_Character):
    def __init__(self, player):
        super(Obj_User, self).__init__()
        self.player = player
        '''
        commonData的存储方法，我们解释一下，可以先参见Gamedefine_Scene文件的注释
        commonData使用bytearray存储，即按照字节存储，目前定义大小为256 * 4个字节。
        python的int类型在64位环境下为8字节，32位环境下为4个字节。
        但是commonData我们统一使用4个字节存储一个int，最大值为4294967295，无符号类型！
        存储原理是：
        commonData的使用索引仍然为0-255
        例如，索引10存入数字68596
        则从commonData的第10，11，12，13字节，依次存储68596，最终存储表示为（16进制）00010BF4
        '''
        self.commonData = bytearray([0] * MAX_CHAR_COMMONDATA_NUM)
        '''
        commonFlag按照位进行存储，必须存储为0或者1，大小设置为7*4个字节，一共7*4*8位
        '''
        self.commonFlag = bytearray([0] * MAX_CHAR_COMMONFLAG_NUM)

        self.guid = None
        self.gender = -1
        self.profession = -1
        self.lastLogoutTime = 0
        self.curLoginTime = 0
        self.createTime = 0
        self.totalOnlineTime = 0
        self.vipCost = 0
        self.saveTimeInterval = 0   #存储时间间隔
        self.exp = 0
        self.money = MoneyData()
        self.lastSceneID = SceneID()
        self.lastScenePos = ScenePos()

        self.changingScenePos = ScenePos() #进入新场景时的位置

        self.objView = []

    def getObjType(self):
        return OBJTYPE_USER

    def tick(self, timeinfo):
        super(Obj_User, self).tick(timeinfo)

    def setCommonData(self, index, value):
        try:
            ASSERT(value <= 0XFFFFFFFF, 'value is larger than 4294967295(4 bytes!)')
            ASSERT(index < CD_MAX, 'index is out of range')
            # 每个数据按照4个字节进行存储
            for i in range(4):
                self.commonData[i + (index * 4)] = (value >> ((4 - 1 - i % 4) * 8)) & 0XFF
        except BaseException as err:
            ASSERT(False, 'Obj_User:setCommonData, ' + str(err))

    def getCommonData(self, index):
        try:
            ASSERT(index < CD_MAX, 'index is out of range')
            value = 0
            for i in range(4):
                value += (self.commonData[i + (index * 4)] << ((4 - 1 - i % 4) * 8))
            return value
        except BaseException as err:
            ASSERT(False, 'Obj_User:getCommonData, ' + str(err))
        return 0

    def setCommonFlag(self, index, value):
        try:
            ASSERT(index < CF_MAX, 'index is out of range')
            ASSERT(value == 1 or value == 1, 'invalid value')
            byteIndex = int(index / 8)
            bitIndex = index % 8
            value = value << (8 - 1 - bitIndex)
            self.commonFlag[byteIndex] |= value
            print(index, byteIndex, bitIndex, value)
        except BaseException as err:
            ASSERT(False, 'Obj_User:setCommonFlag, ' + str(err))

    def getCommonFlag(self, index):
        try:
            ASSERT(index < CF_MAX, 'index is out of range')
            byteIndex = int(index / 8)
            bitIndex = index % 8
            value = self.commonFlag[byteIndex] >> (8 - 1 - bitIndex)
            value = value & 1
            return value
        except BaseException as err:
            ASSERT(False, 'Obj_User:getCommonFlag, ' + str(err))

    def serializeFromDB(self, fullUserData):
        print('Obj_User:serializeFromDB, ')
        self.guid = fullUserData.userData.guid
        self.name = fullUserData.userData.charName
        self.gender = fullUserData.userData.gender
        self.level = fullUserData.userData.level
        self.hp = fullUserData.userData.hp
        self.mp = fullUserData.userData.mp
        self.xp = fullUserData.userData.xp
        self.exp = fullUserData.userData.exp
        self.profession = fullUserData.userData.profession
        self.vipCost = fullUserData.userData.vipCost
        for i in range(MONEYTYPE_COUNT):
            self.money.setMoney(i, fullUserData.userData.money[i])
        self.lastLogoutTime = fullUserData.userData.lastLogoutTime
        self.createTime = fullUserData.userData.createTime
        self.totalOnlineTime = fullUserData.userData.totalOnlineTime
        for i in range(MAX_CHAR_COMMONDATA_NUM):
            self.commonData[i] = fullUserData.userData.commonData[i]
        for i in range(MAX_CHAR_COMMONFLAG_NUM):
            self.commonFlag[i] = fullUserData.userData.commonFlag[i]
        self.lastSceneID.classId = fullUserData.userData.lastSceneId
        self.lastSceneID.instanceId = fullUserData.userData.lastSceneInstId
        self.lastScenePos.posX = fullUserData.userData.lastScenePosX
        self.lastScenePos.posZ = fullUserData.userData.lastScenePosZ
        print(self.guid, self.name, self.gender, self.level, self.hp, self.mp)

    def serializeToDB(self, fullUserData):
        fullUserData.userData.guid = self.guid
        fullUserData.userData.charName = self.name
        fullUserData.userData.gender = self.gender
        fullUserData.userData.level = self.level
        fullUserData.userData.hp = self.hp
        fullUserData.userData.mp = self.mp
        fullUserData.userData.xp = self.xp
        fullUserData.userData.exp = self.exp
        fullUserData.userData.profession = self.profession
        fullUserData.userData.vipCost = self.vipCost
        for i in range(MONEYTYPE_COUNT):
            fullUserData.userData.money[i] = self.money.getMoney(i)
            fullUserData.userData.lastLogoutTime = self.lastLogoutTime
            fullUserData.userData.createTime = self.createTime
            fullUserData.userData.totalOnlineTime = self.totalOnlineTime
        for i in range(MAX_CHAR_COMMONDATA_NUM):
            fullUserData.userData.commonData[i] = self.commonData[i]
        for i in range(MAX_CHAR_COMMONFLAG_NUM):
            fullUserData.userData.commonFlag[i] = self.commonFlag[i]

    def getIsFirstLogin(self):
        try:
            return not self.getCommonFlag(CF_FIRSTLOGIN)
        except BaseException as err:
            ASSERT(False, 'Obj_User:getIsFirstLogin, ' + str(err))
    def setIsFirstLogin(self):
        try:
            self.setCommonFlag(CF_FIRSTLOGIN, 1)
        except BaseException as err:
            ASSERT(False, 'Obj_User:setIsFirstLogin, ' + str(err))

    def onLogin(self):
        try:
            self.updateChangingScenePos()
        except BaseException as err:
            ASSERT(False, 'Obj_User:onLogin, ' + str(err))

    def onEnterScene(self):
        try:
            self.setScenePos(self.changingScenePos.posX, self.changingScenePos.posZ)
            pak = GC_ENTER_SCENE_PAK()
            pak.PacketData.sceneclass = self.getSceneClassId()
            pak.PacketData.sceneinst = self.getSceneInstanceId()
            pak.PacketData.mainplayerserverid = self.getId()
            scenePos = self.getScenePos()
            pak.PacketData.posX = int(scenePos.posX)
            pak.PacketData.posZ = int(scenePos.posZ)
            self.sendPacket(pak)

            self.forceInSight(self)
        except BaseException as err:
            ASSERT(False, 'Obj_User:onEnterScene, ' + str(err))

    def sendPacket(self, pak):
        try:
            self.player.SendPacket(pak)
        except BaseException as err:
            ASSERT(False, 'Obj_User:sendPacket, ' + str(err))

    def updateChangingScenePos(self):
        try:
            sceneClassId = self.getSceneClassId()
            if sceneClassId == self.lastSceneID.classId:
                self.setChangeScenePos(self.lastScenePos.posX, self.lastScenePos.posZ)
                return
            sceneClassTable = gTableManager.getSceneClassById(sceneClassId)
            ASSERT(sceneClassTable != None, 'sceneClassTable is None')
            self.setChangeScenePos(sceneClassTable.Entry_x, sceneClassTable.Entry_z)
        except BaseException as err:
            ASSERT(False, 'Obj_User:updateChangingScenePos, ' + str(err))

    def setChangeScenePos(self, x, z):
        self.changingScenePos.posX = x
        self.changingScenePos.posZ = z
    def getChangeScenePos(self):
        return self.changingScenePos

    def inSight(self, obj):
        try:
            self.objView.append(obj.getId())
        except BaseException as err:
            ASSERT(False, 'Obj_User:inSight, ' + str(err))
    def onInSight(self, obj):
        self.sendBaseAttr(obj)
    def forceInSight(self, obj):
        try:
            self.inSight(obj)
        except BaseException as err:
            ASSERT(False, 'Obj_User:forceInSight, ' + str(err))
    def isInSight(self, objId):
        return objId in self.objView

    def sendBaseAttr(self, obj):
        try:
            pak = GC_CREATE_PLAYER_PAK()
            pak.PacketData.serverId = obj.getId()
            pak.PacketData.guid = obj.guid.get64()
            pak.PacketData.dataId = -1
            pak.PacketData.posX = self.getScenePos().posX
            pak.PacketData.posZ = self.getScenePos().posZ
            pak.PacketData.sceneClass = self.getSceneClassId()
            pak.PacketData.sceneInst = self.getSceneInstanceId()
            pak.PacketData.curforce = 0
            pak.PacketData.name = self.name
            pak.PacketData.isDie = 0
            pak.PacketData.PKModle = 0
            pak.PacketData.curProfession = self.profession
            pak.PacketData.facedir = 0
            pak.PacketData.MoveSpeed = 0
            pak.PacketData.titlename = ''
            pak.PacketData.CurTitleID = -1
            pak.PacketData.MountID = -1
            pak.PacketData.ModelVisualID = -1
            pak.PacketData.WeaponDataID = -1
            pak.PacketData.WeaponEffectGem = -1
            pak.PacketData.StealthLev = 0
            pak.PacketData.VipCost = 0
            pak.PacketData.CombatValue = 0
            pak.PacketData.GuildGuid = INVALID_GUID
            pak.PacketData.bindparent = -1
            pak.PacketData.bindchildren = -1
            pak.PacketData.isEnemy2Self = 0
            pak.PacketData.isInPkList = 0
            self.sendPacket(pak)
        except BaseException as err:
            ASSERT(False, 'Obj_User:sendBaseAttr, ' + str(err))