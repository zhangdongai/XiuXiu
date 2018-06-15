#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.Common.Assert import *
from DB.DBConnector.DBConnectorBase import *
from DB.DBSql import *
from DB.DBStruct.DBStruct_UserData import *
from DB.GameDefine_DB import *

class DBConnectorCreateChar(DBConnectorBase):
    def __init__(self, dbConnectorInterface):
        super(DBConnectorCreateChar, self).__init__(dbConnectorInterface)

        self.userData = DBUserData()

    def init(self):
        pass

    def __del__(self):
        pass

    def save(self):
        try:
            szCommonData = Bytes2DBString(self.userData.commonData)
            szCommonFlag = Bytes2DBString(self.userData.commonFlag)

            self.dbConnectorInterface.setQueryComm(CreateChar % \
                                                   (self.userData.guid.get64(), \
                                                    self.userData.charName, \
                                                    self.userData.account, \
                                                    1, \
                                                    self.userData.hp, \
                                                    self.userData.mp, \
                                                    self.userData.xp, \
                                                    self.userData.level, \
                                                    self.userData.profession, \
                                                    self.userData.gender, \
                                                    self.userData.exp, \
                                                    self.userData.lastSceneId, \
                                                    self.userData.lastSceneInstId, \
                                                    self.userData.lastScenePosX, \
                                                    self.userData.lastScenePosZ, \
                                                    self.userData.lastLogoutTime, \
                                                    self.userData.money[MONEYTYPE_COIN], \
                                                    self.userData.money[MONEYTYPE_YUANBAO], \
                                                    self.userData.money[MONEYTYPE_YUANBAOBIND], \
                                                    self.userData.vipCost, \
                                                    self.userData.createTime, \
                                                    self.userData.totalOnlineTime,
                                                    szCommonFlag, \
                                                    szCommonData, \
                                                    1111))

            self.execute()
        except BaseException as err:
            ASSERT(False, 'DBConnectorCreateChar:save, ' + str(err))

    def parseResult(self):
        DB_CREATECHAR_RESULT = 0

        try:
            ret = DB_RESULT_SUCCESS
            self.dbConnectorInterface.fetch()
            queryResult = self.dbConnectorInterface.getInt(DB_CREATECHAR_RESULT)
            if queryResult == -2:
                ret = DB_RESULT_SAMEGUID
            elif queryResult == -3:
                ret = DB_RESULT_SAMENAME
            elif queryResult == -4:
                ret = DB_RESULT_MAXNUM
            elif queryResult == 1:
                ret = DB_RESULT_SUCCESS
            return ret
        except BaseException as err:
            ASSERT(False, 'DBConnectorSaveGuid:parseResult, ' + str(err))
        return DB_RESULT_FAILED

    def setData(self, userData):
        self.userData = userData