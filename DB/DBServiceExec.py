#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from Service.ServiceManager import *
from Common.Common.Assert import *
from Common.Message.MessageDefine import *
from DB.DBConnector.DBConnectorInterface import *
from Common.Table.TableManager import *
from Common.Common.GeneralSet import *
from Common.Common.Version import *
from Log.Log import *
from DB.DBTask.DBBaseTask import *
from DB.DBConnector.DBConnectorGeneralSet import *

class DBServiceExec:
    def __init__(self, index):
        self.index = index
        self.msgList = []

        self.dbConnectorInterface = DBConnectorInterface()
        
        #消息处理函数结构
        self.dealFunction = {MESSAGE_TYPE_ASSIGN_DBTASK : self.handleMessage_assignDBTask}

    def __del__(self):
        pass

    def init(self):
        self.init_dbConnectorInterface()

        self.checkDBInfo()

    def init_dbConnectorInterface(self):
        try:
            self.connect()
        except BaseException as err:
            ASSERT(False, 'DBServiceExec:init_dbConnectorInterface, ' + str(err))

    def connect(self):
        try:
            serverConfig = gTableManager.getServerConfigListById(ServerId())
            ASSERT(serverConfig != None, 'can not get serverConfig, %d' % ServerId())
            self.dbConnectorInterface.connect(serverConfig.DBUser,
                                       serverConfig.DBPsw,
                                       serverConfig.DBName,
                                       serverConfig.DBIp,
                                       serverConfig.DBPort)
            print('db serviceexec index=%d, connect to db, result = %d' % \
                  (self.index, 1 if self.dbConnectorInterface.isConnected() else 0))
        except BaseException as err:
            ASSERT(False, 'DBServiceExec:connect, ' + str(err))

    def reconnect(self):
        try:
            Log('DB', 'db serviceexec index=%d, try to reconnect to db', self.index)
            self.dbConnectorInterface.reconnect()
        except BaseException as err:
            ASSERT(False, 'DBServiceExec:reconnect, ' + str(err))

    def tick(self):
        try:
            self.tick_connect()
            while True:
                if len(self.msgList) == 0:
                    break
                msg = self.msgList.pop(0)
                if msg.type in self.dealFunction.keys():
                    self.dealFunction.get(msg.type)(msg)
        except BaseException as err:
            ASSERT(False, 'DBServiceExec:tick, ' + str(err))

    def tick_connect(self):
        try:
            if self.dbConnectorInterface.isConnected() == False:
                self.reconnect()
        except BaseException as err:
            ASSERT(False, 'DBServiceExec:tick_connect, ' + str(err))

    def stopService(self):
        try:
            print('DBServiceExec::stopService thread%d join end' % self.index)
        except BaseException as err:
            ASSERT(False, 'DBServiceExec:stopService, ' + str(err))

    def checkDBInfo(self):
        try:
            generalset = DBConnectorGeneralSet(self.dbConnectorInterface)
            generalset.setKey('WORLDID')
            generalset.load()
            worldId = generalset.parseResult()
            ASSERT(worldId == ServerId(), 'worldid is different from DB %d, %d' % (worldId, ServerId()))
            generalset.setKey('DBVERSION')
            generalset.load()
            dbVersion = generalset.parseResult()
            ASSERT(dbVersion == DBVERSION, 'dbversion is different from DB %d, %d' % (dbVersion, DBVERSION))
        except BaseException as err:
            ASSERT(False, 'DBServiceExec:checkDBInfo, ' + str(err))

    def receiveMessage(self, msg):
        try:
            self.msgList.append(msg)
        except BaseException as err:
            ASSERT(False, 'DBServiceExec:receiveMessage, ' + str(err))

    def handleMessage_assignDBTask(self, msg):
        try:
            print('DBServiceExec:handleMessage_assignDBTask')
            task = msg.dbTask
            task.execute(self.dbConnectorInterface)
        except BaseException as err:
            ASSERT(False, 'DBServiceExec:handleMessage_assignDBTask, ' + str(err))