#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.Common.Assert import *
from Common.Common.ServiceDefine import *

DBTASK_TYPEID_INVALID = -1
DBTASK_TYPEID_CHARLIST = 0
DBTASK_TYPEID_CREATECHAR = 1
DBTASK_TYPEID_SAVEGUID = 2

class DBBaseTask:
    def __init__(self):
        self.key = None
        self.opType = ''
        self.retServiceId = SERVICE_ID_INVALID
        self.opTime = time.time()

    def init(self):
        pass

    def __del__(self):
        pass

    def getTypeId(self):
        return DBTASK_TYPEID_INVALID

    def setRetServiceId(self, serviceId):
        self.retServiceId = serviceId

    def setLoad(self):
        self.opType = 'load'

    def setSave(self):
        self.opType = 'save'

    def setKey(self, key):
        self.key = key

    def isLoad(self):
        return True if self.opType == 'load' else False

    def isSave(self):
        return True if self.opType == 'save' else False

    def execute(self, dbConnectorInterface):
        if self.isLoad():
            print('DBBaseTask:execute for load')
            self.load(dbConnectorInterface)
        elif self.isSave():
            print('DBBaseTask:execute for save')
            self.save(dbConnectorInterface)

    def load(self, dbConnectorInterface):
        pass

    def save(self, dbConnectorInterface):
        pass