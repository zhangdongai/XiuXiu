#!/usr/bin/python
# -*- coding: utf-8 -*-

from Log.Log import *
from Scene.SceneClass import *
from Common.Message.SceneMsg import *
from Scene.CopyScene import *
from Common.Scene.GameStruct_Scene import *

class CopySceneClass(SceneClass):
    def __init__(self):
        super(CopySceneClass, self).__init__()
        pass

    def init(self):
        pass

    def __del__(self):
        pass

    def firstEnterTo(self, player):
        try:
            print('CopySceneClass:firstEnterTo')
            instId = self.reuseScene()
            if instId == -1:
                instId = self.enlargeScene()
            self.sceneList[instId].setActive()
            enterMsg = PlayerEnterSceneMsg()
            enterMsg.player = player
            enterMsg.firstEnter = True
            self.sendPlayerEnterSceneMsg(instId, enterMsg)

            userSceneInfo = UserSceneInfo()
            userSceneInfo.sceneInfo.classId = self.getSceneClassId()
            userSceneInfo.sceneInfo.instanceId = instId
            return userSceneInfo
        except BaseException as err:
            ASSERT(False, 'CopySceneClass:firstEnterTo, ' + str(err))
        return None

    def enterTo(self, player):
        pass

    def reuseScene(self):
        try:
            for scene in self.sceneList:
                if scene.isActive():
                    return scene.getInstanceId()
            return -1
        except BaseException as err:
            ASSERT(False, 'CopySceneClass:reuseScene, ' + str(err))
        return -1

    def enlargeScene(self):
        try:
            instId = len(self.sceneList)
            scene = CopyScene()
            scene.setClassId(self.getSceneClassId())
            scene.setInstanceId(instId)
            self.sceneList.append(scene)
            return instId
        except BaseException as err:
            ASSERT(False, 'CopySceneClass:enlargeScene, ' + str(err))
        return -1