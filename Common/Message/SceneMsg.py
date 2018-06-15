#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.Message.MessageDefine import *

class PlayerEnterWorldMsg:
    def __init__(self):
        self.type = MESSAGE_TYPE_PLAYERENTERWORLD
        self.player = None

class PlayerEnterSceneMsg:
    def __init__(self):
        self.type = MESSAGE_TYPE_PLAYERENTERSCENE
        self.player = None
        self.firstEnter = False