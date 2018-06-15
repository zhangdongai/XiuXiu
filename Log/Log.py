#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import Common.Common.GeneralSet as GeneralSet
from Common.Common.Assert import *
from Common.Message.DBMsg import *

class Loger:
    def __init__(self, name):
        self.name = name
        self.logFile = ''
        self.buf = ''

    def init(self):
        self.rebuildFile()

    def log(self, format, args):
        try:
            lt = time.localtime(time.time())
            tbuf = format % args
            ttime = '  %4d-%02d-%02d_%02d:%02d:%02d' % \
                    (lt.tm_year, lt.tm_mon, lt.tm_mday, lt.tm_hour, lt.tm_min, lt.tm_sec)
            tbuf += ttime
            self.buf += tbuf
            self.buf += '\n'
        except BaseException as err:
            ASSERT(False, 'Log:log, ' + str(err))

    def flushLog(self):
        try:
            if self.buf != '':
                file = open(self.logFile, 'a+')
                file.write(self.buf)
                file.close()
                self.buf = ''
        except BaseException as err:
            ASSERT(False, 'Log:flushLog, ' + str(err))

    def rebuildFile(self):
        lt = time.localtime(time.time())
        self.logFile = './RuntimeData/%d/Log/%s.%04d-%02d-%02d-%02d.log' % \
                       (GeneralSet.gServerId, self.name, lt.tm_year, lt.tm_mon, lt.tm_mday, lt.tm_hour)


LogerHome = {
    'Login' : Loger('Login'),
    'Billing' : Loger('Billing'),
    'Player' : Loger('Player'),
    'DB' : Loger('DB'),
    'Guid' : Loger('Guid'),
    'Scene' : Loger('Scene')
}

def Log(er, format, *args):
    loger = LogerHome.get(er)
    if loger != None:
        loger.log(format, args)

def InitLog():
    for value in LogerHome.values():
        value.init()

def FlushAll():
    try:
        for value in LogerHome.values():
            value.flushLog()
    except BaseException as err:
        ASSERT(False, 'FlushAll, ' + str(err))

def RebuildAll():
    try:
        for value in LogerHome.values():
            value.rebuildFile()
    except BaseException as err:
        ASSERT(False, 'RebuildAll, ' + str(err))
