#!/usr/bin/python
# -*- coding: utf-8 -*-


from Common.Message.SceneMsg import *
from Common.Player.LoginPlayerManager import *
from Common.Player.Player import *
from Log.Log import *
from Service.Service import *


class LoginService(Service):
    def __init__(self):
        super(LoginService, self).__init__()
        self.serverSocket = ServerSocket()
        self.playerManager = LoginPlayerManager(self)

        self.loginQueuePlayerList = []
        self.loginPlayingPlayerList = {}
        self.scenePlayingPlayerList = {}

        self.queueUpdateIndexTime = 0

        self.dealFunction = {MESSAGE_TYPE_ACCOUNTVERIFY_RET : self.handleMessage_retAccountVerify,
                             MESSAGE_TYPE_ACCOUNTVALIDATE_RET : self.handleMessage_retAccountValidate,
                             MESSAGE_TYPE_ACCOUNTSTATE_CHECK : self.handleMessage_checkAccountState,
                             MESSAGE_TYPE_QUEUE_FINISH : self.handleMessage_QueueFinish,
                             MESSAGE_TYPE_RETCHARLIST : self.handleMessage_RetCharList,
                             MESSAGE_TYPE_ACCOUNT_OFFLINE : self.handleMessag_accountOffline,
                             MESSAGE_TYPE_RETCREATECHAR : self.handleMessage_retCreateChar}


    def init(self):
        pass

    def __del__(self):
        #del self.serverSocket
        #del self.playerManager
        pass

    def getId(self):
        return SERVICE_ID_LOGIN

    def stopService(self):
        self.playerManager.delAllPlayer()
        self.serverSocket.Socket.close()
    
    def tick(self):
        try:
            super(LoginService, self).tick()
            self.tick_Accept(self.timeInfo)
            self.tick_Queueing(self.timeInfo)
            self.tick_UpdateQueueIndex(self.timeInfo)
            self.tick_Transport(self.timeInfo)
            self.playerManager.tick(self.timeInfo)
        except BaseException as err:
            VERIFY(False, 'Error!LoginService:tick,' + str(err))

    def tick_Accept(self, timeInfo):
        try:
            if self.serverSocket.isHaveNewAccept():
                self.acceptNewPlayer()
        except BaseException as err:
            ASSERT(False, 'LoginService:tick_Accept, ' + str(err))

    def acceptNewPlayer(self):
        try:
            player = Player()
            self.serverSocket.accept(player.Socket)
            player.Socket.setblocking(0)
            player.setStatus(PLAYERSTATUS_CONNECTED)
            self.playerManager.addPlayer(player)
            print('accept new player, id=%d, addrinfo = %s' %
                  (player.Id, str(player.Socket.addr)))
            Log('Login', 'accept new player, id=%d, addrinfo = %s', player.Id, str(player.Socket.addr))
        except BaseException as err:
            ASSERT(False, 'LoginService:acceptNewPlayer, ' + str(err))

    def tick_Queueing(self, timeInfo):
        try:
            curPlayingCount = len(self.loginPlayingPlayerList) + len(self.scenePlayingPlayerList)
            maxQueueFinishCount = 2000 - curPlayingCount
            for index in range(4):
                if index < maxQueueFinishCount:
                    self.olQueueFinishOne()
        except BaseException as err:
            ASSERT(False, 'LoginService:tick_Queueing, ' + str(err))

    def tick_UpdateQueueIndex(self, timeInfo):
        try:
            self.queueUpdateIndexTime += timeInfo.timeElapsed
            if self.queueUpdateIndexTime >= 4000:
                self.queueUpdateIndexTime = 0
                index = 0
                for queueData in self.loginQueuePlayerList:
                    index += 1
                    player = self.playerManager.getPlayer(queueData.playerId)
                    if player != None:
                        player.ObjLogin.updateQueue(index)
        except BaseException as err:
            ASSERT(False, 'LoginService:tick_UpdateQueueIndex, ' + str(err))

    def tick_Transport(self, timeInfo):
        try:
            for i in range(8):
                player = self.playerManager.popReadyEnterWorldPlayer()
                if player == None:
                    break
                player.setStatus(PLAYERSTATUS_ENTERINGWORLD)
                self.olScenePlayer(player.ObjLogin.account, player.ObjUser.guid)

                enterMsg = PlayerEnterWorldMsg()
                enterMsg.player = player
                gServiceManager.SendMessage2Srv(SERVICE_ID_SCENE, enterMsg)
        except BaseException as err:
            ASSERT(False, 'LoginService:tick_Transport, ' + str(err))

    def handleMessage(self, msg):
        try:
            if msg.type in self.dealFunction.keys():
                self.dealFunction[msg.type](msg)
        except BaseException as err:
            ASSERT(False, 'LoginService:handleMessage, ' + str(err))

    def handleMessage_retAccountVerify(self, msg):
        print('LoginService.retAccountVerify, msg = ', msg)
        print('LoginService.retAccountVerify, playerId = ', msg.playerId)
        print('LoginService.retAccountVerify, result = ', msg.result)
        player = self.playerManager.getPlayer(msg.playerId)
        if player != -1:
            player.ObjLogin.retAccountVerify()

    def handleMessage_retAccountValidate(self, msg):
        player = self.playerManager.getPlayer(msg.playerId)
        if player != None:
            player.ObjLogin.retAccountValidate(msg.result,
                                               msg.validateType,
                                               msg.account,
                                               msg.deviceId,
                                               msg.deviceType,
                                               msg.deviceVersion,
                                               msg.channelId,
                                               msg.mediaId,
                                               msg.oid,
                                               msg.accessToken,
                                               msg.shouldCache,
                                               msg.rapidValidateCode)

    def handleMessage_checkAccountState(self, msg):
        player = self.playerManager.getPlayer(msg.playerId)
        if player == None:
            return

        if not self.olHavePlayer(msg.account):
            if self.olQueuePlayer(msg.account, msg.playerId, 0):
                player.ObjLogin.onAccountStateCheckRet(True, True)
            else:
                player.ObjLogin.onAccountStateCheckRet(True, False)
        else:
            player.ObjLogin.onAccountStateCheckRet(False, False)

    def olHavePlayer(self, account):
        try:
            return self.olCheckPlayer(account) > 0
        except BaseException as err:
            ASSERT(False, 'LoginService:olHavePlayer, ' + str(err))
            return False
        return True

    def olCheckPlayer(self, account):
        try:
            checkRet = 0
            for playerData in self.loginQueuePlayerList:
                if playerData.account == account:
                    checkRet += 1
            if self.loginPlayingPlayerList.get(account) != None:
                checkRet += 1
            if self.scenePlayingPlayerList.get(account) != None:
                checkRet += 1
            return checkRet
        except BaseException as err:
            ASSERT(False, 'LoginService:olCheckPlayer, ' + str(err))
            return 0
        return 0

    def olQueuePlayer(self, account, playerId, queueLevel):
        try:
            if len(self.loginQueuePlayerList) >= 2000:
                return False
            if self.olCheckPlayer(account) != 0:
                return False
            queueData = PlayerQueueData(account, playerId, queueLevel)
            self.loginQueuePlayerList.append(queueData)
            return True
        except BaseException as err:
            ASSERT(False, 'LoginService:olQueuePlayer, ' + str(err))
            return False
        return False

    def olQueueFinishOne(self):
        try:
            if len(self.loginQueuePlayerList) == 0:
                return
            queueData = self.loginQueuePlayerList[0]
            print('ol queue finish, playerid=%d, account=%s' % (queueData.playerId, queueData.account))
            Log('Login', 'ol queue finish, playerid=%d, account=%s', queueData.playerId, queueData.account)
            self.olLoginPlayer(queueData)

            queueMsg = QueueFinishMsg()
            queueMsg.playerId = queueData.playerId
            queueMsg.account = queueData.account
            gServiceManager.SendMessage2Srv(SERVICE_ID_LOGIN, queueMsg)
        except BaseException as err:
            ASSERT(False, 'LoginService:olQueueFinishOne, ' + str(err))

    def olLoginPlayer(self, queueData):
        try:
            if self.olCheckPlayer(queueData.account) != 1:
                return
            print('ol login player, playerid=%d, account=%s' % (queueData.playerId, queueData.account))
            Log('Login', 'ol login player, playerid=%d, account=%s', queueData.playerId, queueData.account)
            self.loginPlayingPlayerList[queueData.account] = queueData.playerId
            self.loginQueuePlayerList.remove(queueData)
        except BaseException as err:
            ASSERT(False, 'LoginService:olLoginPlayer, ' + str(err))

    def olDelPlayer(self, account):
        try:
            ASSERT(self.olCheckPlayer(account) == 1, 'LoginService:olDelPlayer, olCheckPlayer != 1')
            for queueData in self.loginQueuePlayerList:
                if queueData.account == account:
                    self.loginQueuePlayerList.remove(queueData)
                    Log('Login', 'del player from loginQueuePlayerList, playerId = %d, account = %s',
                        queueData.playerId, queueData.account)
                    break
            for key in self.loginPlayingPlayerList.keys():
                if key == account:
                    Log('Login', 'del player from loginPlayingPlayerList, playerId = %d, account = %s',
                        self.loginPlayingPlayerList[key], key)
                    del self.loginPlayingPlayerList[key]
                    break
            for key in self.scenePlayingPlayerList.keys():
                if key == account:
                    Log('Login', 'del player from scenePlayingPlayerList, playerId = %d, account = %s',
                        self.scenePlayingPlayerList[key], key)
                    del self.scenePlayingPlayerList[key]
                    break
        except BaseException as err:
            ASSERT(False, 'LoginService:olDelPlayer, ' + str(err))

    def olScenePlayer(self, account, guid):
        try:
            for key in self.loginPlayingPlayerList.keys():
                if key == account:
                    del self.loginPlayingPlayerList[key]
                    break
            self.scenePlayingPlayerList[account] = guid
        except BaseException as err:
            ASSERT(False, 'LoginService:olScenePlayer, ' + str(err))

    def handleMessage_QueueFinish(self, msg):
        try:
            player = self.playerManager.getPlayer(msg.playerId)
            if player != None:
                player.ObjLogin.onQueueFinish()
        except BaseException as err:
            ASSERT(False, 'LoginService:handleMessage_QueueFinish, ' + str(err))

    def handleMessage_RetCharList(self, msg):
        try:
            player = self.playerManager.getPlayer(msg.playerId)
            if player != None:
                charList = msg.charList
                player.ObjLogin.onRetCharList(msg.result, charList)
        except BaseException as err:
            ASSERT(False, 'LoginService:handleMessage_RetCharList, ' + str(err))

    def handleMessag_accountOffline(self, msg):
        try:
            self.olDelPlayer(msg.account)
        except BaseException as err:
            ASSERT(False, 'LoginService:handleMessag_accountOffline, ' + str(err))

    def handleMessage_retCreateChar(self, msg):
        try:
            player = self.playerManager.getPlayer(msg.playerId)
            if player != None:
                player.ObjLogin.onRetCreateChar(msg.result, msg.fullUserData)
        except BaseException as err:
            ASSERT(False, 'LoginService:handleMessage_retCreateChar, ' + str(err))


'''
ls = LoginService()
try:
    while True:
        ls.tick('123')
except BaseException as err:
    del ls
'''
print('loginService module loaded')

Py_LoginService = LoginService()
