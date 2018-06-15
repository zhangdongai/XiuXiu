#!/usr/bin/python
# -*- coding: utf-8 -*-

import pycurl
import time
from Common.Message.BillingMsg import *
#from threading import Thread
from Service.ServiceManager import *
from Common.Billing.GameInterface_Billing import *
from Common.Common.Assert import *

class BillingServiceExec:
    def __init__(self, index):
        self.index = index
        self.active = True
        self.msgList = []

        #创建和初始化curl
        self.curl = pycurl.Curl()
        self.curl.setopt(pycurl.WRITEFUNCTION, self.httpResponse)
        self.curl.setopt(pycurl.CONNECTTIMEOUT, 10)
        self.curl.setopt(pycurl.TIMEOUT, 30)

        #创建thread
        #self.thread = Thread(target = self.threadEntry)
        
        #消息处理函数结构
        self.dealFunction = {MESSAGE_TYPE_REQUESTHTTP : self.handleMessage_httpRequest,
                             MESSAGE_TYPE_ACCOUNTVERIFY_REQ : self.handleMessage_reqAccountVerify,
                             MESSAGE_TYPE_ACCOUNTVALIDATE_REQ : self.handleMessage_reqAccountValidate}

    def init(self):
        #self.thread.start()
        pass

    def __del__(self):
        self.curl.close()

    '''
    def threadEntry(self):
        while self.active:
            if len(self.msgList) == 0:
                continue
            msg = self.msgList.pop(0)
            if msg.type in self.dealFunction.keys():
                self.dealFunction.get(msg.type)(msg)
    '''

    def tick(self):
        try:
            while self.active:
                if len(self.msgList) == 0:
                    break
                msg = self.msgList.pop(0)
                if msg.type in self.dealFunction.keys():
                    self.dealFunction.get(msg.type)(msg)
        except BaseException as err:
            ASSERT(False, 'BillingServiceExec:tick, ' + str(err))

    def stopService(self):
        try:
            self.setActive(False)
            self.thread.join()
            print('BillingServiceExec::stopService thread%d join end' % self.index)
        except BaseException as err:
            ASSERT(False, 'BillingServiceExec:stopService, ' + str(err))

    def isActive(self):
        return self.active

    def setActive(self, active):
        self.active = active

    def httpResponse(self, bufRet):
        print('execindex%d time=' % self.index, time.time())
        pass

    def receiveMessage(self, msg):
        try:
            self.msgList.append(msg)
        except BaseException as err:
            ASSERT(False, 'BillingServiceExec:receiveMessage, ' + str(err))

    def handleMessage_httpRequest(self, msg):
        #print('httprequest data=', msg.senddata)
        self.curl.setopt(pycurl.URL, 'http://123.57.58.164:8008/php/1.txt')
        self.curl.perform()

    def handleMessage_reqAccountVerify(self, msg):
        print('BillingServiceExec.reqAccountVerify, msgtype = ', msg.type)
        print('BillingServiceExec.reqAccountVerify, msgdata = ', msg.account)
        retMsg = RetAccountVerify()
        retMsg.playerId = msg.playerId
        retMsg.result = True
        gServiceManager.SendMessage2Srv(SERVICE_ID_LOGIN, retMsg)

    def handleMessage_reqAccountValidate(self, msg):
        try:
            print('BillingServiceExec.reqAccountValidate', BillingInterface.getBillingWorkMode(), msg.validateData.validateType)
            if BillingInterface.getBillingWorkMode() == BILLINGWORKMODE_PROJECT:
                if msg.validateData.validateType == VALIDATETYPE_TEST:
                    BillingInterface.validateAccountOk(msg.validateData.validateType,
                                                       msg.validateData.playerId,
                                                       msg.validateData.account,
                                                       msg.validateData.deviceId,
                                                       msg.validateData.deviceType,
                                                       msg.validateData.deviceVersion,
                                                       '',
                                                       '',
                                                       '',
                                                       '',
                                                       '',
                                                       False,
                                                       0,
                                                       msg.validateData.hostIp)
        except BaseException as err:
            ASSERT(False, 'BillingServiceExec:handleMessage_reqAccountValidate, ' + str(err))
'''
msg = RequestHttpMessage()
msg.senddata = 50
billingExec = BillingServiceExec(0)
billingExec.init()
billingExec.receiveMessage(msg)
time.sleep(3)
billingExec.setActive(False)
billingExec.stopService()
'''
