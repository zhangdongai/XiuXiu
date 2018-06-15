#!/usr/bin/python
# -*- coding: utf-8 -*-

from Log.Log import *
from Scene.Scene import *

class WildScene(Scene):
    def __init__(self):
        super(WildScene, self).__init__()

    def init(self):
        pass

    def __del__(self):
        pass

    def tick(self, timeInfo):
        try:
            super(WildScene, self).tick(timeInfo)
        except BaseException as err:
            VERIFY(False, 'Error!WildScene:tick,' + str(err))