#!/usr/bin/python
# -*- coding: utf-8 -*-

from Billing.BillingServiceExec import *
from Service.Service import *
from Common.Common.Assert import *

class BillingService(Service):
    def __init__(self):
        super(BillingService, self).__init__()
        self.execList = []
        self.curExecIndex = 0
        self.execCount = 8

        self.dealFunction = {}

    def init(self):
        try:
            for i in range(self.execCount):
                billingExec = BillingServiceExec(i)
                self.execList.append(billingExec)
                timebegin =  time.time()
                billingExec.init()
                print('BillingService::init create billingexec%d, time elapsed%f' % (i, time.time() - timebegin))
        except BaseException as err:
            ASSERT(False, 'BillingService:init, ' + str(err))

    def tick(self):
        try:
            super(BillingService, self).tick()
        except BaseException as err:
            VERIFY(False, 'BillingService:tick, ', str(err))

    def tick_exec(self, execIndex):
        try:
            if len(self.execList) <= execIndex:
                return
            #调用执行单元的tick
            self.execList[execIndex].tick()
        except BaseException as err:
            VERIFY(False, 'BillingService:tick_exec, ', str(err))

    def getId(self):
        return SERVICE_ID_BILLING

    def stopService(self):
        try:
            for i in range(self.execCount):
                self.execList[i].stopService()
            self.execList = []
        except BaseException as err:
            ASSERT(False, 'BillingService:stopService, ' + str(err))

    def handleMessage(self, msg):
        try:
            execIndex = self.allocExecIndex()
            ASSERT(execIndex >= 0 and execIndex < len(self.execList), 'BillingService:handleMessage, serviceIndex Error!')
            self.execList[execIndex].receiveMessage(msg)
        except BaseException as err:
            ASSERT(False, 'BillingService:handleMessage, ' + str(err))

    def allocExecIndex(self):
        try:
            retIndex = self.curExecIndex
            self.curExecIndex = (self.curExecIndex + 1) % len(self.execList)
            return retIndex
        except BaseException as err:
            ASSERT(False, 'BillingService:allocExecIndex, ' + str(err))
        return -1

Py_BillingService = BillingService()

'''
timebegin = time.time()
billingService = BillingService()
billingService.init()
print('time elapsed total', time.time() - timebegin)

print('timebegin=', time.time())
for i in range(10):
    requesthttp = RequestHttpMessage()
    requesthttp.senddata = i
    billingService.receiveMessage(requesthttp)

time.sleep(15)
billingService.stopService()
'''
