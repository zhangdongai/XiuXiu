#!/usr/bin/python
# -*- coding: utf-8 -*-

from Log.Log import *
from Service.ServiceCell import *
from Common.Message.SceneMsg import *
from Common.Player.ScenePlayerManager import *

class Scene(ServiceCell):
    def __init__(self):
        super(Scene, self).__init__()

        self.classId = -1
        self.instanceId = -1

        self.playerManager = ScenePlayerManager(self)

        self.curPlayerCount = 0
        self.enteringPlayerCount = 0

        self.allocedObjId = -1
        self.objList = {}

        self.dealFunction = {MESSAGE_TYPE_PLAYERENTERSCENE: self.handleMessage_PlayerEnterScene
                            }

    def init(self):
        pass

    def __del__(self):
        pass

    def tick(self, timeInfo):
        try:
            super(Scene, self).tick()
            self.playerManager.tick(timeInfo)
        except BaseException as err:
            VERIFY(False, 'Error!Scene:tick,' + str(err))

    def handleMessage(self, msg):
        try:
            if msg.type in self.dealFunction.keys():
                self.dealFunction[msg.type](msg)
        except BaseException as err:
            ASSERT(False, 'Scene:handleMessage, ' + str(err))

    def isActive(self):
        return True

    def setClassId(self, classId):
        self.classId = classId
    def setInstanceId(self, instId):
        self.instanceId = instId
    def getClassId(self):
        return self.classId
    def getInstanceId(self):
        return self.instanceId

    def handleMessage_PlayerEnterScene(self, msg):
        try:
            print('Scene:handleMessage_PlayerEnterScene')
            self.decEnteringPlayerCount()
            msg.player.setStatus(PLAYERSTATUS_SCENEPLAYING)
            self.playerManager.addPlayer(msg.player, msg.firstEnter)
        except BaseException as err:
            ASSERT(False, 'Scene:handleMessage_PlayerEnterScene, ' + str(err))

    def addUser(self, objUser, firstLogin, playerCount):
        try:
            self.curPlayerCount = playerCount

            objId = self.allocObjId()
            objUser.setId(objId)
            objUser.setScene(self)
            self.objList[objId] = objUser
            if firstLogin:
                objUser.onLogin()
            objUser.onEnterScene()
        except BaseException as err:
            ASSERT(False, 'Scene:addUser, ' + str(err))

    def allocObjId(self):
        self.allocedObjId += 1
        return self.allocedObjId

    def incEnteringPlayerCount(self):
        self.enteringPlayerCount += 1
    def decEnteringPlayerCount(self):
        self.enteringPlayerCount -= 1

    def setCurPlayerCount(self, count):
        self.curPlayerCount = count
    def getCurPlayerCount(self):
        return self.curPlayerCount