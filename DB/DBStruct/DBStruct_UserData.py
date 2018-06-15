#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.Common.Assert import *
from DB.GameDefine_DB import *
from Common.Common.Guid64 import *
from Common.Money.GameDefine_Money import *
from Common.Scene.GameDefine_Scene import *
from Common.Attr.GameDefine_Attr import *
import time

class DBUserData:
    def __init__(self):
        self.guid = Guid64(0XFFFF, 0XFF, 0XFF, 0XFFFF0000)
        self.hp                 = 100
        self.mp                 = 100
        self.xp                 = 0
        self.level              = 1
        self.exp                = 0
        self.profession         = -1
        self.gender             = -1
        self.money              = [0] * MONEYTYPE_COUNT
        self.lastSceneId        = -1
        self.lastSceneInstId    = -1
        self.lastScenePosX      = 20.0
        self.lastScenePosZ      = 18.0
        self.vipCost            = 0
        self.totalOnlineTime    = 0
        self.charName           = ''
        self.account            = ''
        self.lastLogoutTime     = 0
        self.createTime         = 0
        self.commonFlag         = bytearray([0] * MAX_CHAR_COMMONFLAG_NUM)
        self.commonData         = bytearray([0] * MAX_CHAR_COMMONDATA_NUM)
        self.isValid            = 1

    def initAsNewChar(self, charName, account, profession):
        self.guid = GENERATE_GUID(GUID_CHAR)
        self.profession = profession
        self.gender = GENDER_MALE if profession == PROFESSION_SHAOLIN or \
                                        profession == PROFESSION_DALI \
                                    else GENDER_FEMALE
        self.charName = charName
        self.account = account
        self.createTime = time.time()

    def copyFrom(self, userData):
        self.guid = userData.guid
        self.hp = userData.hp
        self.mp = userData.mp
        self.xp = userData.xp
        self.level = userData.level
        self.exp = userData.exp
        self.profession = userData.profession
        self.gender = userData.gender
        for i in range(MONEYTYPE_COUNT):
            self.money[i] = userData.money[i]
        self.lastSceneId = userData.lastSceneId
        self.lastSceneInstId = userData.lastSceneInstId
        self.lastScenePosX = userData.lastScenePosX
        self.lastScenePosZ = userData.lastScenePosZ
        self.vipCost = userData.vipCost
        self.totalOnlineTime = userData.totalOnlineTime
        self.charName = userData.charName
        self.account = userData.account
        self.lastLogoutTime = userData.lastLogoutTime
        self.createTime = userData.createTime
        for i in range(MAX_CHAR_COMMONFLAG_NUM):
            self.commonFlag[i] = userData.commonFlag[i]
        for i in range(MAX_CHAR_COMMONDATA_NUM):
            self.commonData[i] = userData.commonData[i]
        self.isValid = userData.isValid

class DBFullUserData:
    def __init__(self):
        self.userData = DBUserData()

    def initAsNewChar(self, charName, account, profession):
        self.userData.initAsNewChar(charName, account, profession)

    def copyFrom(self, fullUserData):
        self.userData.copyFrom(fullUserData.userData)

