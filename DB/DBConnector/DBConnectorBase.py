#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.Common.Assert import *

class DBConnectorBase:
    def __init__(self, dbConnectorInterface):
        self.dbConnectorInterface = dbConnectorInterface
        self.resultCount = 0

    def init(self):
        pass

    def __del__(self):
        pass

    def getResultCount(self):
        return self.resultCount

    def execute(self):
        try:
            self.dbConnectorInterface.execute()
            self.resultCount = self.dbConnectorInterface.getResultCount()
        except BaseException as err:
            ASSERT(False, 'DBConnectorBase:execute, ' + str(err))