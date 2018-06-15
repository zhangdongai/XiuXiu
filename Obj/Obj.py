#!/usr/bin/python
# -*-coding: utf-8 -*-

from Common.Scene.GameDefine_Scene import *
from Common.Scene.GameStruct_Scene import *

class Obj:
    def __init__(self):
        self.id = -1
        self.scene = None

        self.scenePos = ScenePos()

    def getObjType(self):
        return OBJTYPE_EMPTY

    def tick(self, timeinfo):
        pass

    def setId(self, id):
        self.id = id
    def getId(self):
        return self.id

    def setScene(self, scene):
        self.scene = scene
    def getScene(self):
        return self.scene

    def getSceneClassId(self):
        if self.scene == None:
            return -1
        return self.scene.getClassId()
    def getSceneInstanceId(self):
        if self.scene == None:
            return -1
        return self.scene.getInstanceId()

    def setScenePos(self, x, z):
        self.scenePos.posX = x
        self.scenePos.posZ = z
    def getScenePos(self):
        return self.scenePos