#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.Common.IniReader import *

class GameConfig:
    def __init__(self):
        self.connectHealthLimit = 0
        self.LuckDrawEndTime = 0

    def load(self):
        reader = IniReader()
        reader.load('./Config/GameConfig.ini')
        self.connectHealthLimit = reader.readInt('Login', 'ProcessConnectionHealthLimit')
        self.LuckDrawEndTime = reader.readInt('LuckDraw', 'LuckDrawEndTime')

gGameConfig = GameConfig()

