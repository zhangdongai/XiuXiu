#!/usr/bin/python
# -*- coding: utf-8 -*-

from Service.ServiceManager import *
from Service.Service import *
from Log.Log import *
from Common.Common.Assert import *

class LogService(Service):
    def __init__(self):
        super(LogService, self).__init__()

    def init(self):
        pass

    def tick(self):
        try:
            super(LogService, self).tick()
            if self.timeInfo.diffHour:
                RebuildAll()

            FlushAll()
        except BaseException as err:
            VERIFY(False, 'LogService:tick, ' + str(err))

Py_LogService = LogService()