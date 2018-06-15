#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.Common.Assert import *
from DB.DBConnector.DBConnectorBase import *
from DB.DBSql import *
from DB.DBStruct.DBStruct_CharList import *
from DB.GameDefine_DB import *

class DBConnectorAskCharList(DBConnectorBase):
    def __init__(self, dbConnectorInterface):
        super(DBConnectorAskCharList, self).__init__(dbConnectorInterface)

        self.accName = ''

    def init(self):
        pass

    def __del__(self):
        pass

    def load(self):
        try:
            self.dbConnectorInterface.setQueryComm(AskCharList % self.accName)
            self.execute()
        except BaseException as err:
            ASSERT(False, 'DBConnectorAskCharList:load, ' + str(err))

    def save(self):
        pass

    def parseResult(self, charList):
        DB_CHARLIST_CHARGUID = 0
        DB_CHARLIST_CHARNAME = 1
        DB_CHARLIST_PROFESSION = 2
        DB_CHARLIST_LEVEL = 3
        DB_CHARLIST_GENDER = 4

        try:
            ASSERT(self.resultCount <= MAX_CHAR_NUMBER, 'resultCount larger than MAX_CHAR_NUMBER!')
            for i in range(self.resultCount):
                self.dbConnectorInterface.fetch()

                charList.charList[i].charGuid = self.dbConnectorInterface.getInt(DB_CHARLIST_CHARGUID)
                charList.charList[i].charName = self.dbConnectorInterface.getString(DB_CHARLIST_CHARNAME)
                charList.charList[i].profession = self.dbConnectorInterface.getInt(DB_CHARLIST_PROFESSION)
                charList.charList[i].charLevel = self.dbConnectorInterface.getInt(DB_CHARLIST_LEVEL)
                charList.charList[i].gender = self.dbConnectorInterface.getInt(DB_CHARLIST_GENDER)
        except BaseException as err:
            ASSERT(False, 'DBConnectorAskCharList:parseResult, ' + str(err))

    def setAccName(self, accname):
        self.accName = accname