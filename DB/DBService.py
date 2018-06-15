#!/usr/bin/python
# -*- coding: utf-8 -*-

from DB.DBServiceExec import *
from Service.Service import *
from Common.Common.Assert import *
from Common.Message.MessageDefine import *
from Common.Message.DBMsg import *
from DB.DBTask.DBAskCharListTask import *
from DB.DBTask.DBCreateCharTask import *
from DB.DBTask.DBSaveGuidTask import *

class DBService(Service):
    def __init__(self):
        super(DBService, self).__init__()
        self.execList = []
        self.curExecIndex = 0
        self.execCount = 8

        self.taskList = []

        # 消息处理函数结构
        self.dealFunction = {MESSAGE_TYPE_ASKCHARLIST : self.handleMessage_askCharList,
                             MESSAGE_TYPE_CREATECHAR : self.handleMessage_createChar,
                             MESSAGE_TYPE_SAVEGUID : self.handleMessage_saveGuid}

    def init(self):
        try:
            for i in range(self.execCount):
                dbExec = DBServiceExec(i)
                self.execList.append(dbExec)
                timebegin =  time.time()
                dbExec.init()
                print('DBService::init create dbexec%d, time elapsed%f' % (i, time.time() - timebegin))
        except BaseException as err:
            ASSERT(False, 'DBService:init, ' + str(err))

    def tick(self):
        try:
            super(DBService, self).tick()
            self.tick_assignTask()
        except BaseException as err:
            VERIFY(False, 'DBService:tick, ', str(err))

    def tick_exec(self, execIndex):
        try:
            if len(self.execList) <= execIndex:
                return
            #调用执行单元的tick
            self.execList[execIndex].tick()
        except BaseException as err:
            VERIFY(False, 'DBService:tick_exec, ', str(err))

    def tick_assignTask(self):
        try:
            while len(self.taskList) != 0:
                task = self.taskList.pop(0)
                assignTaskMsg = DBAssignTaskMsg()
                assignTaskMsg.dbTask = task
                execIndex = self.allocExecIndex()
                print('DBService, alloc exec index', execIndex)
                ASSERT(execIndex < self.execCount, 'execIndex out of range')
                self.execList[execIndex].receiveMessage(assignTaskMsg)
        except BaseException as err:
            ASSERT(False, 'DBService:tick_assignTask, ' + str(err))

    def getId(self):
        return SERVICE_ID_DB

    def stopService(self):
        try:
            for i in range(self.execCount):
                self.execList[i].stopService()
            self.execList = []
        except BaseException as err:
            ASSERT(False, 'DBService:stopService, ' + str(err))

    def handleMessage(self, msg):
        try:
            if msg.type in self.dealFunction.keys():
                self.dealFunction[msg.type](msg)
        except BaseException as err:
            ASSERT(False, 'DBService:handleMessage, ' + str(err))

    def allocExecIndex(self):
        try:
            retIndex = self.curExecIndex
            self.curExecIndex = (self.curExecIndex + 1) % len(self.execList)
            return retIndex
        except BaseException as err:
            ASSERT(False, 'DBService:allocExecIndex, ' + str(err))
        return -1

    def addTask(self, task):
        added = False
        for i in range(len(self.taskList)):
            t = self.taskList[i]
            if self.isSameTask(task, t):
                if task.opTime > t.opTime:
                    self.taskList[i] = task
                    Log('DB', 'DBService:addTask, task replaced type=%d', task.getTypeId())
                    added = True
                    return
                elif task.opTime >= t.opTime:
                    #时间相同？不做处理
                    added = True
                    return
        if added == False:
            self.taskList.append(task)
        #需要增加task替换的逻辑

    def canAddTask(self, task):
        pass

    def isSameTask(self, task1, task2):
        return task1.key == task2.key and \
                task1.getTypeId() == task2.getTypeId() and \
                task1.opType == task2.opType


    def handleMessage_askCharList(self, msg):
        try:
            print('DBService:handleMessage_askCharList')
            dbTask = DBAskCharListTask()
            dbTask.setAccName(msg.account)
            dbTask.setPlayerId(msg.playerId)
            dbTask.setLoad()
            dbTask.setRetServiceId(SERVICE_ID_LOGIN)
            self.addTask(dbTask)

            dbTask2 = DBAskCharListTask()
            dbTask.setLoad()
            self.addTask(dbTask)
        except BaseException as err:
            ASSERT(False, 'DBService:handleMessage_askCharList, ' + str(err))

    def handleMessage_createChar(self, msg):
        try:
            dbTask = DBCreateCharTask()
            dbTask.setPlayerId(msg.playerId)
            dbTask.setAccName(msg.account)
            dbTask.setData(msg.fullUserData.userData)
            dbTask.setSave()
            dbTask.setRetServiceId(SERVICE_ID_LOGIN)
            self.addTask(dbTask)
        except BaseException as err:
            ASSERT(False, 'DBService:handleMessage_createChar, ' + str(err))

    def handleMessage_saveGuid(self, msg):
        try:
            dbTask = DBSaveGuidTask()
            dbTask.setType(msg.gtype)
            dbTask.setCarry(msg.carry)
            dbTask.setSerial(msg.serial)
            dbTask.setSave()
            self.addTask(dbTask)
        except BaseException as err:
            ASSERT(False, 'DBService:handleMessage_saveGuid, ' + str(err))

Py_DBService = DBService()