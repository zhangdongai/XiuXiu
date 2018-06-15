#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.Player.Player import *
from Service.BaseService import *
from Log.Log import *
from Common.Table.TableManager import *
from Common.Table.Table_SceneClass import *
from Common.Scene.GameDefine_Scene import *
from Scene.MainSceneClass import *
from Scene.WildSceneClass import *
from Scene.CopySceneClass import *

class SceneService(BaseService):
    def __init__(self):
        super(SceneService, self).__init__()

        self.sceneClassList = {}

        #记录所有场景玩家的基本信息和场景信息
        self.sceneUserInfo = {} #Guid64:UserSceneInfo

        self.dealFunction = {MESSAGE_TYPE_PLAYERENTERWORLD: self.handleMessage_playerEnterWorld
                             }

    def __del__(self):
        pass

    def init(self):
        self.initSceneClass()

    def getId(self):
        return SERVICE_ID_SCENE

    def initSceneClass(self):
        try:
            classCount = gTableManager.getSceneClassCount()
            for i in range(classCount):
                sceneClassTable = gTableManager.getSceneClassByIndex(i)
                if sceneClassTable.Type == SCENETYPE_MAIN:
                    sceneClass = MainSceneClass()
                    sceneClass.setSceneClassId(sceneClassTable.SceneID)
                    self.sceneClassList[sceneClassTable.SceneID] = sceneClass
                elif sceneClassTable.Type == SCENETYPE_COPY:
                    sceneClass = CopySceneClass()
                    sceneClass.setSceneClassId(sceneClassTable.SceneID)
                    self.sceneClassList[sceneClassTable.SceneID] = sceneClass
                elif sceneClassTable.Type == SCENETYPE_WILD:
                    sceneClass = WildSceneClass()
                    sceneClass.setSceneClassId(sceneClassTable.SceneID)
                    self.sceneClassList[sceneClassTable.SceneID] = sceneClass
        except BaseException as err:
            ASSERT(False, 'SceneService:initSceneClass, ' + str(err))

    def stopService(self):
        pass
    
    def tick(self):
        '''
        python的GIL真的很棘手，服务器单线程几乎是无法理解的。即使这样，仍然有继续做下去的理由，
         因为单线程的服务器可以用在别的领域。
         Scene是可能存在很多个的，Scene在之前我们理解为单个的线程，但是在XiuXiu中，可能无法完全
         沿用以前的设计思路了。所以，我决定将Scene的更新在SceneService里统一做。
        '''
        try:
            #先进行所有场景的心跳，保证先处理完上一个心跳分配的任务
            self.tick_SceneClass()
            #然后进行自己的心跳
            super(SceneService, self).tick()
        except BaseException as err:
            VERIFY(False, 'Error!SceneService:tick,' + str(err))

    def tick_SceneClass(self):
        try:
            for sceneClass in self.sceneClassList.values():
                sceneClass.tick(self.timeInfo)
        except BaseException as err:
            ASSERT(False, 'SceneService:tick_SceneClass, ' + str(err))

    def handleMessage(self, msg):
        try:
            print('SceneService.handleMessage')
            if msg.type in self.dealFunction.keys():
                self.dealFunction[msg.type](msg)
        except BaseException as err:
            ASSERT(False, 'SceneService:handleMessage, ' + str(err))

    def handleMessage_playerEnterWorld(self, msg):
        try:
            print('SceneService:handleMessage_playerEnterWorld')
            objUser = msg.player.ObjUser
            ASSERT(objUser != None, 'objUser is None')
            if objUser.getIsFirstLogin():
                print('SceneService:handleMessage_playerEnterWorld, getIsFirstLogin')
                self.firstEnterTo(msg.player)
            else:
                pass
        except BaseException as err:
            ASSERT(False, 'SceneService:handleMessage_playerEnterWorld, ' + str(err))

    def firstEnterTo(self, player):
        try:
            if PLAYERGUIDNEWSCENE in self.sceneClassList.keys():
                userSceneInfo = self.sceneClassList[PLAYERGUIDNEWSCENE].firstEnterTo(player)
                ASSERT(userSceneInfo != None, 'can not enter scene')
                userSceneInfo.baseInfo.guid = player.ObjUser.guid
                userSceneInfo.baseInfo.charname = player.ObjUser.name
                self.addUserSceneInfo(userSceneInfo)
        except BaseException as err:
            ASSERT(False, 'SceneService:firstEnterTo, ' + str(err))

    def enterTo(self, player):
        try:
            pass
        except BaseException as err:
            ASSERT(False, 'SceneService:firstEnterTo, ' + str(err))

    def addUserSceneInfo(self, userSceneInfo):
        try:
            ASSERT(userSceneInfo.baseInfo.guid not in self.sceneUserInfo.keys(), 'user info is existed!')
            self.sceneUserInfo[userSceneInfo.baseInfo.guid] = userSceneInfo
        except BaseException as err:
            ASSERT(False, 'SceneService:addUserSceneInfo, ' + str(err))

    def delUserSceneInfo(self, guid):
        try:
            if guid in self.sceneUserInfo.keys():
                del self.sceneUserInfo[guid]
        except BaseException as err:
            ASSERT(False, 'SceneService:delUserSceneInfo, ' + str(err))

Py_SceneService = SceneService()
