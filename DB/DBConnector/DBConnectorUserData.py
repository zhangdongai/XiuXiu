#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.Common.Assert import *
from DB.DBConnector.DBConnectorBase import *
from DB.DBSql import *
from DB.DBStruct.DBStruct_UserData import *
from DB.GameDefine_DB import *

class DBConnectorUserData(DBConnectorBase):
    def __init__(self, dbConnectorInterface):
        super(DBConnectorUserData, self).__init__(dbConnectorInterface)

        self.charguid = -1

    def init(self):
        pass

    def __del__(self):
        pass

    def load(self):
        try:
            self.dbConnectorInterface.setQueryComm(LoadCharInfo % self.charguid.get64())
            self.execute()
        except BaseException as err:
            ASSERT(False, 'DBConnectorUserData:load, ' + str(err))

    def parseResult(self, userdata):
        DB_USERDATA_ACCNAME = 0
        DB_USERDATA_CHARGUID = 1
        DB_USERDATA_CHARNAME = 2
        DB_USERDATA_ISVALID = 3
        DB_USERDATA_HP = 4
        DB_USERDATA_MP = 5
        DB_USERDATA_XP = 6
        DB_USERDATA_LEVEL = 7
        DB_USERDATA_PROFESSION = 8
        DB_USERDATA_GENDER = 9
        DB_USERDATA_EXP = 10
        DB_USERDATA_SCENEID = 11
        DB_USERDATA_SCENEINSTID = 12
        DB_USERDATA_SCENEPOSX = 13
        DB_USERDATA_SCENEPOSZ = 14
        DB_USERDATA_LOGOUTTIME = 15
        DB_USERDATA_MONEYCOIN = 16
        DB_USERDATA_MONEYYB = 17
        DB_USERDATA_MONEYYBBIND = 18
        DB_USERDATA_VIPCOST = 19
        DB_USERDATA_CREATETIME = 20
        DB_USERDATA_ONLINETIME = 21
        DB_USERDATA_COMMONFLAG = 22
        DB_USERDATA_COMMONDATA = 23
        DB_USERDATA_CRC = 24

        try:
            self.dbConnectorInterface.fetch()
            print(self.dbConnectorInterface.fetchTuple)
            userdata.account = self.dbConnectorInterface.getString(DB_USERDATA_ACCNAME)
            userdata.guid = self.dbConnectorInterface.getInt(DB_USERDATA_CHARGUID)
            userdata.charName = self.dbConnectorInterface.getString(DB_USERDATA_CHARNAME)
            userdata.hp = self.dbConnectorInterface.getInt(DB_USERDATA_HP)
            userdata.mp = self.dbConnectorInterface.getInt(DB_USERDATA_MP)
            userdata.xp = self.dbConnectorInterface.getInt(DB_USERDATA_XP)
            userdata.level = self.dbConnectorInterface.getInt(DB_USERDATA_LEVEL)
            userdata.profession = self.dbConnectorInterface.getInt(DB_USERDATA_PROFESSION)
            userdata.gender = self.dbConnectorInterface.getInt(DB_USERDATA_GENDER)
            userdata.exp = self.dbConnectorInterface.getInt(DB_USERDATA_EXP)
            userdata.lastSceneId = self.dbConnectorInterface.getInt(DB_USERDATA_SCENEID)
            userdata.lastSceneInstId = self.dbConnectorInterface.getInt(DB_USERDATA_SCENEINSTID)
            userdata.lastScenePosX = self.dbConnectorInterface.getInt(DB_USERDATA_SCENEPOSX)
            userdata.lastScenePosZ = self.dbConnectorInterface.getInt(DB_USERDATA_SCENEPOSZ)
            userdata.lastLogoutTime = self.dbConnectorInterface.getInt(DB_USERDATA_LOGOUTTIME)
            userdata.money[MONEYTYPE_COIN] = self.dbConnectorInterface.getInt(DB_USERDATA_MONEYCOIN)
            userdata.money[MONEYTYPE_YUANBAO] = self.dbConnectorInterface.getInt(DB_USERDATA_MONEYYB)
            userdata.money[MONEYTYPE_YUANBAOBIND] = self.dbConnectorInterface.getInt(DB_USERDATA_MONEYYBBIND)
            userdata.vipCost = self.dbConnectorInterface.getInt(DB_USERDATA_VIPCOST)
            userdata.createTime = self.dbConnectorInterface.getInt(DB_USERDATA_CREATETIME)
            userdata.totalOnlineTime = self.dbConnectorInterface.getInt(DB_USERDATA_ONLINETIME)
            commonFlag = self.dbConnectorInterface.getString(DB_USERDATA_COMMONFLAG)
            userdata.commonFlag = DBString2Bytes(commonFlag)
            commonData = self.dbConnectorInterface.getString(DB_USERDATA_COMMONDATA)
            userdata.commonData = DBString2Bytes(commonData)
        except BaseException as err:
            ASSERT(False, 'DBConnectorrUserData:parseResult, ' + str(err))

    def setGuid(self, guid):
        self.charguid = guid