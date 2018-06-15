#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.Common.Assert import *
from Common.Common.ServiceDefine import *
from DB.DBConnector.DBConnectorInterface import *
from DB.DBTask.DBBaseTask import *
from DB.DBConnector.DBConnectorSaveGuid import *
from Common.Message.DBMsg import *
from Log.Log import *

class DBSaveGuidTask(DBBaseTask):
    def __init__(self):
        super(DBSaveGuidTask, self).__init__()
        self.type = -1
        self.carry = 0
        self.serial = 0

    def init(self):
        pass

    def __del__(self):
        pass

    def getTypeId(self):
        return DBTASK_TYPEID_SAVEGUID

    def setType(self, type):
        self.type = type
    def setCarry(self, carry):
        self.carry = carry
    def setSerial(self, serial):
        self.serial = serial

    def save(self, dbConnectorInterface):
        try:
            connector = DBConnectorSaveGuid(dbConnectorInterface)
            connector.setType(self.type)
            connector.setCarry(self.carry)
            connector.setSerial(self.serial)
            connector.save()
            print('DBSaveGuidTask:execute save end, resultcount=', connector.resultCount)
        except BaseException as err:
            ASSERT(False, 'DBSaveGuidTask:save, ' + str(err))