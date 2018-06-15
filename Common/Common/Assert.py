#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time
import platform
from Common.Common.BaseDefine import *
import Common.Common.GeneralSet as GeneralSet

def do_assert(msg, throw):
    lt = time.localtime(time.time())
    ttime = '  %4d-%02d-%02d_%02d:%02d:%02d' % \
            (lt.tm_year, lt.tm_mon, lt.tm_mday, lt.tm_hour, lt.tm_min, lt.tm_sec)
    msg += ttime
    szAssert = "Assert!!!\n%s\n" % \
               (msg)
    logFile = './RuntimeData/%d/Log/assert.%04d-%02d-%02d-%02d.log' % \
              (GeneralSet.gServerId, lt.tm_year, lt.tm_mon, lt.tm_mday, lt.tm_hour)

    fs = open(logFile, 'a+')
    fs.write(szAssert)
    fs.close()

    print(szAssert)
    if throw:
        raise Exception(msg)

def Assert(expression, msg):
    if not expression:
        do_assert(msg, True)

def Verify(expression, msg):
    if not expression:
        do_assert(msg, False)

ASSERT = Assert
VERIFY = Verify

