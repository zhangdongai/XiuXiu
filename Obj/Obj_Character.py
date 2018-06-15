#!/usr/bin/python
# -*-coding: utf-8 -*-

from Obj.Obj import *

class Obj_Character(Obj):
    def __init__(self):
        super(Obj_Character, self).__init__()

        self.name = ''
        self.level = 0
        self.hp = 0
        self.mp = 0
        self.xp = 0
        self.isDie = False

    def tick(self, timeinfo):
        super(Obj_Character, self).tick(timeinfo)