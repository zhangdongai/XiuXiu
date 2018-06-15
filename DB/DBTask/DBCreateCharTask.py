#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.Common.Assert import *
from Common.Common.ServiceDefine import *
from DB.DBConnector.DBConnectorInterface import *
from DB.DBTask.DBBaseTask import *
from DB.DBConnector.DBConnectorCreateChar import *
from Common.Message.DBMsg import *
from Log.Log import *
from DB.DBConnector.DBConnectorUserData import *

class DBCreateCharTask(DBBaseTask):
    def __init__(self):
        super(DBCreateCharTask, self).__init__()

        self.accName = ''
        self.playerId = 0
        self.userData = None

    def init(self):
        pass

    def __del__(self):
        pass

    def getTypeId(self):
        return DBTASK_TYPEID_CREATECHAR

    def setAccName(self, acc):
        self.accName = acc
    def setPlayerId(self, id):
        self.playerId = id
    def setData(self, userData):
        self.userData = userData

    def save(self, dbConnectorInterface):
        try:
            connector = DBConnectorCreateChar(dbConnectorInterface)
            connector.setData(self.userData)
            connector.save()

            retMsg = DBRetCreateCharMsg()
            retMsg.playerId = self.playerId
            retMsg.account = self.accName
            dbResult = connector.parseResult()
            retMsg.result = dbResult
            if dbResult != DB_RESULT_SUCCESS:
                gServiceManager.SendMessage2Srv(self.retServiceId, retMsg)
                return

            userdataConnector = DBConnectorUserData(dbConnectorInterface)
            userdataConnector.setGuid(self.userData.guid)
            userdataConnector.load()
            retMsg.fullUserData = DBFullUserData()
            userdataConnector.parseResult(retMsg.fullUserData.userData)
            gServiceManager.SendMessage2Srv(self.retServiceId, retMsg)
        except BaseException as err:
            ASSERT(False, 'DBCreateCharTask:save, ' + str(err))