#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.Common.Assert import *
from Common.Common.ServiceDefine import *
from DB.DBConnector.DBConnectorInterface import *
from DB.DBTask.DBBaseTask import *
from DB.DBConnector.DBConnectorAskCharList import *
from Common.Message.DBMsg import *
from Log.Log import *

class DBAskCharListTask(DBBaseTask):
    def __init__(self):
        super(DBAskCharListTask, self).__init__()

        self.accName = ''
        self.playerId = 0

    def init(self):
        pass

    def __del__(self):
        pass

    def getTypeId(self):
        return DBTASK_TYPEID_CHARLIST

    def setAccName(self, acc):
        self.accName = acc
    def setPlayerId(self, id):
        self.playerId = id

    def load(self, dbConnectorInterface):
        try:
            print('DBAskCharListTask:execute for load')
            connector = DBConnectorAskCharList(dbConnectorInterface)
            connector.setAccName(self.accName)
            connector.load()
            print('DBAskCharListTask:execute load end, resultcount=', connector.resultCount)

            retMsg = RetCharListMsg()
            retMsg.charList = DBCharList()
            retMsg.charList.cleanUp()
            if connector.getResultCount() < 0:
                Log('DB', 'DBAskCharListTask:load, load charlist failed, account=%s', self.accName)
                retMsg.result = DB_RESULT_FAILED
                retMsg.playerId = self.playerId
                retMsg.account = self.accName
                gServiceManager.SendMessage2Srv(self.retServiceId, retMsg)
            if connector.getResultCount() != 0:
                connector.parseResult(retMsg.charList)
            retMsg.result = DB_RESULT_SUCCESS
            retMsg.playerId = self.playerId
            retMsg.account = self.accName
            retMsg.charList.validCharNum = connector.getResultCount()
            gServiceManager.SendMessage2Srv(self.retServiceId, retMsg)
        except BaseException as err:
            ASSERT(False, 'DBAskCharListTask:load, ' + str(err))

    def save(self, dbConnectorInterface):
        print('DBAskCharListTask:execute for save')