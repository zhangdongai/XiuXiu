#!/usr/bin/python
# -*- coding: utf-8 -*-

from TestExample.Test2 import *
from Login.LoginService import *
import operator
from Common.Common.GeneralSet import *
print(X_PLATFROM)

def TestGo(a, b, c):
    print('i am function testGo, param is ', a, b, c)
print('abcd')

class TimeInfo:
    def __init__(self):
        self.week = 7

    def setweek(self,w):
        self.week = w

ti = TimeInfo()

def changeObj(t):
    msg = DBSaveGuidMsg()
    t.week = 10
print('week=', ti.week)
changeObj(ti)
print('week=', ti.week)

li = []
li.append(TimeInfo())
li[0].setweek(11)
print('week=', li[0].week)

class pm:
    def __init__(self):
        self.dict = {}

    def add(self, key, value):
        self.dict[key] = value

    def check(self):
        for key in self.dict.keys():
            print('pm:check', key)
        self.dict = {}
        print('pm:check', self.dict)

class TestClass:
    def __init__(self):
        self.data = 1
        self.p = pm()

    def setdata(self, d, t):
        self.data = d
        self.p.add(1, 2)
        self.p.add(3, 4)
        self.p.add(5, 6)
        print('call TestClass setdata success, data = ', d)
        print('call TestClass setdata success, t.week = ', type(t.week))
        self.p.check()

tc = TestClass()
print('TestClass data = ', tc.data)

def TestObj(d):
    tc.setdata(d, ti)
    print('TestClass data = ', tc.data)

TestObj(10)

dict = {1:2, 3:4, 5:6, 7:8, 9:0}
print(dict)
for value in dict.values():
    print(value)
print('key is', dict.keys())


list = ['a', 'b', 'c']
print(list)
list = []
print(list)

class L(object):
    def __init__(self):
        self.data = 0

    def __str__(self):
        return str(self.data)
    __repr__ = __str__

    def setdata(self, data):
        self.data = data

    def __cmp__(self, other):
        return self.data < other.data

    def __lt__(self, other):
        return self.data < other.data

l1 = L()
l1.setdata(1)
l2 = L()
l2.setdata(2)
l3 = L()
l3.setdata(3)
l4 = L()
l4.setdata(4)
list = []
list.append(l3)
list.append(l1)
list.append(l2)
list.append(l4)
print(list)
print(sorted(list, key=lambda l : l.data, reverse=True))
print(l3 < l1)

