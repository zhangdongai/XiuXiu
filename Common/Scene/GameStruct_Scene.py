#!/usr/bin/python
# -*- coding: utf-8 -*-

class SceneID:
    def __init__(self):
        self.classId = -1
        self.instanceId = -1

class UserBaseInfo:
    def __init__(self):
        self.guid = -1
        self.charname = ''

class UserSceneInfo:
    def __init__(self):
        self.sceneInfo = SceneID()
        self.baseInfo = UserBaseInfo()

class ScenePos:
    def __init__(self):
        self.posX = 0.0
        self.posZ = 0.0