#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.Common.Assert import *
from DB.GameDefine_DB import *

class DBChar:
    def __init__(self):
        self.charGuid = 0
        self.charName = ''
        self.profession = 0
        self.charLevel = 0
        self.gender = 0

    def cleanUp(self):
        self.charGuid = 0
        self.charName = ''
        self.profession = 0
        self.charLevel = 0
        self.gender = 0

    def copy(self, dbChar):
        self.charGuid = dbChar.charGuid
        self.charName = dbChar.charName
        self.profession = dbChar.profession
        self.charLevel = dbChar.charLevel
        self.gender = dbChar.gender

class DBCharList:
    def __init__(self):
        #重要提醒！如果按照下面的定义方法，设置charList的任何一个对象，所有对象都会变化。
        #经过测试发现，这种定义方式是创建了3个对象，但是指向了同一块内存，这并不符合我们的预期！
        #请注意：只有对象数组才会这样，基本数据类型的数组是木有问题啦！
        #self.charList = [DBChar()] * MAX_CHAR_NUMBER
        #我们修改成如下的代码：
        self.charList = []
        for i in range(MAX_CHAR_NUMBER):
            self.charList.append(DBChar())
        self.validCharNum = 0

    def cleanUp(self):
        for i in range(MAX_CHAR_NUMBER):
            self.charList[i].cleanUp()

    def copy(self, charList):
        for i in range(MAX_CHAR_NUMBER):
            self.charList[i].copy(charList[i])