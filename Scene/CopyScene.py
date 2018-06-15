#!/usr/bin/python
# -*- coding: utf-8 -*-

from Log.Log import *
from Scene.Scene import *

STATUS_READY = 0
STATUS_OPEN = 1
STATUS_CLOSE = 2

class CopyScene(Scene):
    def __init__(self):
        super(CopyScene, self).__init__()

        self.status = STATUS_CLOSE

    def init(self):
        pass

    def __del__(self):
        pass

    def tick(self, timeInfo):
        try:
            super(CopyScene, self).tick(timeInfo)
        except BaseException as err:
            VERIFY(False, 'Error!CopyScene:tick,' + str(err))

    def isActive(self):
        return self.status != STATUS_CLOSE

    def setActive(self):
        self.status = STATUS_READY