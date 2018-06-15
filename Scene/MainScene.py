#!/usr/bin/python
# -*- coding: utf-8 -*-

from Log.Log import *
from Scene.Scene import *

class MainScene(Scene):
    def __init__(self):
        super(MainScene, self).__init__()

    def init(self):
        pass

    def __del__(self):
        pass

    def tick(self, timeInfo):
        try:
            super(MainScene, self).tick(timeInfo)
        except BaseException as err:
            VERIFY(False, 'Error!MainScene:tick,' + str(err))