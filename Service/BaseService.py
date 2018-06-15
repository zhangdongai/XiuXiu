#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from Common.Common.ServiceDefine import *
from Common.Common.TimeInfo import *

class BaseService(object):
    def __init__(self):
        self.tickTime = time.time()
        self.messageList = []
        self.timeInfo = TimeInfo()

    def tick(self):
        curTime = time.time()
        #print('BaseService::tick service%d, tickelapsed%f' % (self.getId(), curTime - self.tickTime))
        self.tickTime = curTime
        self.handleAllMessage()

    def stopService(self):
        pass

    def receiveMessage(self, msg):
        self.messageList.append(msg)
        print('BaseService.receiveMessage, msg = ', msg)

    def handleAllMessage(self):
        while len(self.messageList) != 0:
            msg = self.messageList.pop(0)
            self.handleMessage(msg)

    def handleMessage(self, msg):
        pass

    def updateTimeInfo(self, te, dy, dm, dw, dd00, dd04, dd12, dd18, dd20, dh, dhh, deh, dmi, ds):
        self.timeInfo.updateTimeInfo(te, dy, dm, dw,
                                     dd00, dd04, dd12, dd18,
                                     dd20, dh, dhh, deh, dmi, ds)
