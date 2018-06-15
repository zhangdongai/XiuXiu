#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.Common.Assert import *
from DB.DBConnector.DBConnectorBase import *
from DB.DBSql import *
from DB.GameDefine_DB import *

class DBConnectorGeneralSet(DBConnectorBase):
    def __init__(self, dbConnectorInterface):
        super(DBConnectorGeneralSet, self).__init__(dbConnectorInterface)
        self.key = ''

    def init(self):
        pass

    def __del__(self):
        pass

    def load(self):
        try:
            ASSERT(self.key != '', 'key is NULL')
            self.dbConnectorInterface.setQueryComm(LoadGeneralSet % (self.key))
            self.dbConnectorInterface.execute()
        except BaseException as err:
            ASSERT(False, 'DBConnectorGeneralSet:save, ' + str(err))

    def parseResult(self):
        DB_GENERALSET_VALUE = 0
        try:
            self.dbConnectorInterface.fetch()
            return self.dbConnectorInterface.getInt(DB_GENERALSET_VALUE)
        except BaseException as err:
            ASSERT(False, 'DBConnectorGeneralSet:parseResult, ' + str(err))
        return None

    def setKey(self, key):
        self.key = key