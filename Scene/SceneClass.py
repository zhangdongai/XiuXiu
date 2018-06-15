#!/usr/bin/python
# -*- coding: utf-8 -*-

from Log.Log import *

class SceneClass:
    def __init__(self):
        self.sceneClassId = -1

        self.sceneList = []

    def init(self):
        pass

    def __del__(self):
        pass
    
    def tick(self, timeInfo):
        try:
            for scene in self.sceneList:
                scene.tick(timeInfo)
        except BaseException as err:
            VERIFY(False, 'Error!SceneClass:tick,' + str(err))

    def sendMessage(self, instId, msg):
        try:
            ASSERT(instId > -1 and instId < len(self.sceneList), 'can not find instid')
            self.sceneList[instId].receiveMessage(msg)
        except BaseException as err:
            ASSERT(False, 'SceneClass:sendMessage, ' + str(err))

    def sendPlayerEnterSceneMsg(self, instId, msg):
        try:
            ASSERT(instId > -1 and instId < len(self.sceneList), 'can not find instid')
            self.sceneList[instId].incEnteringPlayerCount()
            self.sendMessage(instId, msg)
        except BaseException as err:
            ASSERT(False, 'SceneClass:sendPlayerEnterSceneMsg, ' + str(err))

    def setSceneClassId(self, id):
        self.sceneClassId = id
    def getSceneClassId(self):
        return self.sceneClassId

    def firstEnterTo(self, player):
        pass
    def enterTo(self, player):
        pass