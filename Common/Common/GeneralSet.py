#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.Common.BaseDefine import *
import platform

gServerId = INVALID_ID
def ServerId():
    return gServerId
print('gServerId = %d' % gServerId)

X_PLATFROM = ''
X_PLATFROM = platform.architecture()[0]
