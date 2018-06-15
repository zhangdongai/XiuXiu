#!/usr/bin/python
# -*-coding: utf-8 -*-

from Common.NetWork.Packet.CG_LOGIN_PAK import *
from Common.NetWork.Packet.GC_LOGIN_RET_PAK import*
from Common.NetWork.Packet.GC_LOGIN_QUEUE_STATUS_PAK import *
from Common.NetWork.Packet.GC_CREATEROLE_RET_PAK import *
from Common.Message.BillingMsg import *
from Common.Message.LoginMsg import *
from Common.Message.DBMsg import *
from Service.ServiceManager import *
from Common.Common.Version import *
from Common.Billing.GameDefine_Billing import *
from Common.Player.PlayerDefine import *
from Common.Billing.GameInterface_Billing import *
from Log.Log import *
from Common.Common.Assert import *
from DB.DBStruct.DBStruct_UserData import *

class Obj_Login:
    def __init__(self, player):
        self.player = player
        self.validateType = 0
        self.account = ''
        self.deviceId = ''
        self.deviceType = ''
        self.deviceVersion = ''
        self.channelId = ''
        self.mediaId = ''
        self.oid = ''
        self.accessToken = ''
        self.shouleCache = False
        self.rapidValidateCode = 0
        self.isGm = False

    def checkVersion(self, gameVersion, progVersion):
        if gameVersion != GAMEVERSION and progVersion != PROGRAMEVERSION:
            return False
        return True

    def PacketHandler(self, packetId, packet):
        try:
            ASSERT(packetId in self.Handler.keys(), 'can not find packetId=%d in packet handler' % packetId)
            self.Handler[packetId](packet)
        except BaseException as err:
            ASSERT(False, 'Obj_Login:PacketHandler, ' + str(err))

    def HandleLogin(self, packet):
        try:
            print('Obj_Login.HandleLogin, receive data, id = ', packet.GetPacketId())
            print(packet.PacketData.vtype)
            print(packet.PacketData.gameversion)
            print(packet.PacketData.programversion)
            print(packet.PacketData.maxpacketid)
            print(packet.PacketData.account)
            print('CG_LOGIN size = ', packet.PacketData.ByteSize())
            '''
            login = GC_LOGIN_RET_PAK()
            login.PacketData.result = 2122
            login.PacketData.validateresult = 101
            login.PacketData.userid = 'zhangdongaihehe'
            self.player.SendPacket(login)
            '''
            #这个测试的消息去掉了
            '''
            msg = ReqAccountVerify()
            msg.playerId = self.player.getId()
            msg.account = packet.PacketData.account
            print('Obj_Login serviceMsg = ', gServiceManager)
            gServiceManager.SendMessage2Srv(SERVICE_ID_BILLING, msg)
            '''
            ##############################################
            #从这儿开始写正式的逻辑了
            vtype = packet.PacketData.vtype
            gameVersion = packet.PacketData.gameversion
            progVersion = packet.PacketData.programversion
            maxpacketId = packet.PacketData.maxpacketid

            forceEnter = True if packet.PacketData.forceenter == 1 else False

            deviceId = packet.PacketData.deviceid
            deviceType = packet.PacketData.devicetype
            deviceVersion = packet.PacketData.deviceversion

            account = packet.PacketData.account

            validateInfo = packet.PacketData.validateinfo
            channelId = packet.PacketData.channelid
            mediachannelId = packet.PacketData.mediachannel
            rapvalidCode = packet.PacketData.rapidvalidatecode

            reverseInt1 = packet.PacketData.reservedint1
            reverseInt2 = packet.PacketData.reservedint2
            reverseInt3 = packet.PacketData.reservedint3
            reverseInt4 = packet.PacketData.reservedint4

            reverseStr1 = packet.PacketData.reservedstring1
            reverseStr2 = packet.PacketData.reservedstring2
            reverseStr3 = packet.PacketData.reservedstring3
            reverseStr4 = packet.PacketData.reservedstring4
            print('gameVersion', gameVersion)
            print('progVersion', progVersion)
            #版本号不匹配
            if not self.checkVersion(gameVersion, progVersion):
                retLogin = GC_LOGIN_RET_PAK()
                retLogin.PacketData.result = GC_LOGIN_RET.VERSIONNOTMATCH
                retLogin.PacketData.validateresult = 0
                retLogin.PacketData.userid = ''
                retLogin.PacketData.oid = ''
                retLogin.PacketData.accesstoken = ''
                retLogin.PacketData.rapidvalidatecode = 0
                self.player.SendPacket(retLogin)
                return

            BillingInterface.ValidateAccount(vtype, self.player.getId(),
                                             account, deviceId,
                                             deviceType, deviceVersion,
                                             validateInfo, channelId,
                                             mediachannelId, rapvalidCode,
                                             self.player.Socket.addr)
        except BaseException as err:
            ASSERT(False, 'Obj_Login:HandleLogin, ' + str(err))

    def HandlePing(self, packet):
        pass

    def retAccountVerify(self):
        print('Obj_Login.retAccountVerify')

    def retAccountValidate(self, result, validateType, account,
                           deviceId, deviceType, deviceVersion,
                           channelId, mediaId, oid, accessToken,
                           shouldCache, rapidValidateCode):
        try:
            if result == VALIDATERESULT_SUCCESS:
                self.player.setStatus(PLAYERSTATUS_VALIDATE_OK)
                print('ObjLogin.retAccountValidate Success')
                Log('Login', 'ObjLogin.retAccountValidate Success, account=%s', account)
                self.validateType = validateType
                self.account = account
                self.deviceId = deviceId
                self.deviceType = deviceType
                self.deviceVersion = deviceVersion
                self.channelId = channelId
                self.mediaId = mediaId
                self.oid = oid
                self.accessToken = accessToken
                self.shouleCache = shouldCache
                self.rapidValidateCode = rapidValidateCode

                checkMsg = AccountStateCheckMsg()
                checkMsg.playerId = self.player.getId()
                checkMsg.account = self.account
                gServiceManager.SendMessage2Srv(SERVICE_ID_LOGIN, checkMsg)
                self.player.setStatus(PLAYERSTATUS_ACCOUNTSTATE_CHECKING)
            else:
                self.player.setStatus(PLAYERSTATUS_VALIDATE_FAILED)
                print('ObjLogin.retAccountValidate Failed')
                Log('Login', 'ObjLogin.retAccountValidate Failed, account=%s', account)
        except BaseException as err:
            ASSERT(False, 'Obj_Login:retAccountValidate, ' + str(err))

    def onAccountStateCheckRet(self, checkRet, queueRet):
        try:
            if checkRet:
                if queueRet:
                    self.player.setStatus(PLAYERSTATUS_ACCOUNTSTATE_CHECKOK)
                    self.beginQueue()
                    self.player.setStatus(PLAYERSTATUS_QUEUEING)
                else:
                    retLogin = GC_LOGIN_RET_PAK()
                    retLogin.PacketData.result = GC_LOGIN_RET.QUEUEFULL
                    retLogin.PacketData.validateresult = 0
                    retLogin.PacketData.userid = ''
                    retLogin.PacketData.oid = ''
                    retLogin.PacketData.accesstoken = ''
                    retLogin.PacketData.rapidvalidatecode = 0
                    self.player.SendPacket(retLogin)
                    print('ol player queue failed, playerId=%d, account=%s' % (self.player.getId(), self.account))
                    Log('Login', 'ol player queue failed, playerId=%d, account=%s', self.player.getId(), self.account)
            else:
                retLogin = GC_LOGIN_RET_PAK()
                retLogin.PacketData.result = GC_LOGIN_RET.ALREADYLOGIN
                retLogin.PacketData.validateresult = 0
                retLogin.PacketData.userid = ''
                retLogin.PacketData.oid = ''
                retLogin.PacketData.accesstoken = ''
                retLogin.PacketData.rapidvalidatecode = 0
                self.player.SendPacket(retLogin)
                print('ol player check state failed, playerId=%d, account=%s' % (self.player.getId(), self.account))
                Log('Login', 'ol player check state failed, playerId=%d, account=%s', self.player.getId(), self.account)
        except BaseException as err:
            ASSERT(False, 'Obj_Login:onAccountStateCheckRet, ' + str(err))

    def beginQueue(self):
        try:
            queueRet = GC_LOGIN_QUEUE_STATUS_PAK()
            queueRet.PacketData.status = GC_LOGIN_QUEUE_STATUS.BEGINQUEUE
            queueRet.PacketData.index = 9999
            self.player.SendPacket(queueRet)
            print('ol player begin queue, playerId=%d, account=%s' % (self.player.getId(), self.account))
            Log('Login', 'ol player begin queue, playerId=%d, account=%s', self.player.getId(), self.account)
        except BaseException as err:
            ASSERT(False, 'Obj_Login:beginQueue, ' + str(err))

    def updateQueue(self, index):
        try:
            queueRet = GC_LOGIN_QUEUE_STATUS_PAK()
            queueRet.PacketData.status = GC_LOGIN_QUEUE_STATUS.QUEUING
            queueRet.PacketData.index = index
            self.player.SendPacket(queueRet)
        except BaseException as err:
            ASSERT(False, 'Obj_Login:updateQueue, ' + str(err))

    def endQueue(self):
        try:
            queueRet = GC_LOGIN_QUEUE_STATUS_PAK()
            queueRet.PacketData.status = GC_LOGIN_QUEUE_STATUS.ENDQUEUE
            queueRet.PacketData.index = 0
            self.player.SendPacket(queueRet)
        except BaseException as err:
            ASSERT(False, 'Obj_Login:endQueue, ' + str(err))

    def onQueueFinish(self):
        try:
            self.player.setStatus(PLAYERSTATUS_QUEUE_FINISH)
            self.endQueue()
            print('ol queue finish playerId=%d, account=%s' % (self.player.getId(), self.account))
            Log('Login', 'ol queue finish playerId=%d, account=%s', self.player.getId(), self.account)

            charListMsg = AskCharListMsg()
            charListMsg.playerId = self.player.getId()
            charListMsg.account = self.account
            gServiceManager.SendMessage2Srv(SERVICE_ID_DB, charListMsg)

            self.player.setStatus(PLAYERSTATUS_CHARLIST_QUERYING)
        except BaseException as err:
            ASSERT(False, 'Obj_Login:onQueueFinish, ' + str(err))

    def onRetCharList(self, ret, charList):
        try:
            if ret == DB_RESULT_SUCCESS:
                self.player.setStatus(PLAYERSTATUS_CHARLIST_QUERY_OK)
                retLogin = GC_LOGIN_RET_PAK()
                retLogin.PacketData.result = GC_LOGIN_RET.SUCCESS
                retLogin.PacketData.validateresult = 0
                retLogin.PacketData.userid = self.account
                retLogin.PacketData.oid = self.oid
                retLogin.PacketData.accesstoken = self.accessToken
                retLogin.PacketData.rapidvalidatecode = self.rapidValidateCode
                for i in range(charList.validCharNum):
                    print('guid', charList.charList[i].charGuid)
                    name = charList.charList[i].charName
                    print('name', name)
                    print('name', name.decode())
                    print('profession', charList.charList[i].profession)
                    print('level', charList.charList[i].charLevel)
                    print('gender', charList.charList[i].gender)
                    retLogin.PacketData.roleGUIDList.append(charList.charList[i].charGuid)
                    retLogin.PacketData.roleTypeList.append(charList.charList[i].profession)
                    #字符串默认读出的为bytearray类型，需要转换为bytes或者str类型
                    #通过name.decode()转换成str类型
                    #通过bytes(name)转换成bytes类型
                    retLogin.PacketData.playerNameList.append(name.decode())
                    #print(retLogin.PacketData.playerNameList[i])
                    retLogin.PacketData.roleLevelList.append(charList.charList[i].charLevel)
                    retLogin.PacketData.ModelVisualID.append(-1)
                    retLogin.PacketData.WeaponID.append(-1)
                    retLogin.PacketData.WeaponEffectGem.append(-1)
                self.player.SendPacket(retLogin)
            else:
                retLogin = GC_LOGIN_RET_PAK()
                retLogin.PacketData.result = GC_LOGIN_RET.READROLELISTFAIL
                retLogin.PacketData.validateresult = 0
                retLogin.PacketData.userid = self.account
                retLogin.PacketData.oid = self.oid
                retLogin.PacketData.accesstoken = self.accessToken
                retLogin.PacketData.rapidvalidatecode = self.rapidValidateCode
                self.player.SendPacket(retLogin)

                msg = AccountOfflineMsg()
                msg.account = self.account
                gServiceManager.SendMessage2Srv(SERVICE_ID_LOGIN, msg)

                self.player.setStatus(PLAYERSTATUS_CONNECTED)

        except BaseException as err:
            ASSERT(False, 'Obj_Login:onRetCharList, ' + str(err))

    def HandleRandomName(self, packet):
        pass

    def HandleCreateRole(self, packet):
        try:
            self.player.setStatus(PLAYERSTATUS_CREATEINGCHAR)
            charName = packet.PacketData.name
            profession = packet.PacketData.type
            print('HandleCreateRole, name=', charName)

            createMsg = DBCreateCharMsg()
            createMsg.playerId = self.player.getId()
            createMsg.account = self.account
            createMsg.fullUserData = DBFullUserData()
            createMsg.fullUserData.initAsNewChar(charName, self.account, profession)
            gServiceManager.SendMessage2Srv(SERVICE_ID_DB, createMsg)
        except BaseException as err:
            ASSERT(False, 'Obj_Login:HandleCreateRole, ' + str(err))

    def onRetCreateChar(self, result, fullUserData):
        try:
            print('Obj_Login:onRetCreateChar')
            if result == DB_RESULT_SUCCESS:
                print('Obj_Login:onRetCreateChar', fullUserData.userData.commonFlag)
                print('Obj_Login:onRetCreateChar', fullUserData.userData.commonData)
                self.player.setStatus(PLAYERSTATUS_CREATECHAR_SUCCESS)
                self.player.ObjUser.serializeFromDB(fullUserData)
                pak = GC_CREATEROLE_RET_PAK()
                pak.PacketData.result = GC_CREATEROLE_RET.CREATEROLE_SUCCESS
                pak.PacketData.profession = fullUserData.userData.profession
                pak.PacketData.playerGuid = fullUserData.userData.guid
                pak.PacketData.playerName = fullUserData.userData.charName.decode()
                self.player.SendPacket(pak)

                self.player.setStatus(PLAYERSTATUS_READYENTERWORLD)
            elif result == DB_RESULT_SAMENAME:
                self.player.setStatus(PLAYERSTATUS_CREATECHAR_FAILED)

                pak = GC_CREATEROLE_RET_PAK()
                pak.PacketData.result = GC_CREATEROLE_RET.CREATEROLE_FAIL_NAMEEXIST
                pak.PacketData.profession = 0
                pak.PacketData.playerGuid = 0
                pak.PacketData.playerName = ''
                self.player.SendPacket(pak)
            else:
                self.player.setStatus(PLAYERSTATUS_CREATECHAR_FAILED)

                msg = AccountOfflineMsg()
                msg.account = self.account
                gServiceManager.SendMessage2Srv(SERVICE_ID_LOGIN, msg)

                self.player.setStatus(PLAYERSTATUS_CONNECTED)
        except BaseException as err:
            ASSERT(False, 'Obj_Login:onRetCreateChar, ' + str(err))