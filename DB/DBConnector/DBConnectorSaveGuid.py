#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.Common.Assert import *
from DB.DBConnector.DBConnectorBase import *
from DB.DBSql import *
from DB.GameDefine_DB import *

class DBConnectorSaveGuid(DBConnectorBase):
    def __init__(self, dbConnectorInterface):
        super(DBConnectorSaveGuid, self).__init__(dbConnectorInterface)
        self.type = -1
        self.carry = 0
        self.serial = 0

    def init(self):
        pass

    def __del__(self):
        pass

    def save(self):
        try:
            self.dbConnectorInterface.setQueryComm(SaveGuid % (self.type, self.carry, self.serial))
            self.dbConnectorInterface.execute()
        except BaseException as err:
            ASSERT(False, 'DBConnectorSaveGuid:save, ' + str(err))

    def parseResult(self, charList):
        try:
            pass
        except BaseException as err:
            ASSERT(False, 'DBConnectorSaveGuid:parseResult, ' + str(err))

    def setType(self, type):
        self.type = type
    def setCarry(self, carry):
        self.carry = carry
    def setSerial(self, serial):
        self.serial = serial