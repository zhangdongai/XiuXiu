#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.Message.MessageDefine import *
#from DB.DBStruct.DBStruct_CharList import *
#import DB.DBStruct.DBStruct_UserData as UserData

class DBAssignTaskMsg:
    def __init__(self):
        self.type = MESSAGE_TYPE_ASSIGN_DBTASK
        self.dbTask = None

class AskCharListMsg:
    def __init__(self):
        self.type = MESSAGE_TYPE_ASKCHARLIST
        self.playerId = -1
        self.account = ''

class RetCharListMsg:
    def __init__(self):
        self.type = MESSAGE_TYPE_RETCHARLIST
        self.result = 0
        self.charList = None
        self.playerId = -1
        self.account = ''

class DBCreateCharMsg:
    def __init__(self):
        self.type = MESSAGE_TYPE_CREATECHAR
        self.playerId = -1
        self.account = ''
        self.fullUserData = None


class DBRetCreateCharMsg:
    def __init__(self):
        self.type = MESSAGE_TYPE_RETCREATECHAR
        self.playerId = -1
        self.account = ''
        self.result = 0
        self.fullUserData = None

class DBSaveGuidMsg:
    def __init__(self):
        self.type = MESSAGE_TYPE_SAVEGUID
        self.gtype = -1
        self.carry = 0
        self.serial = 0