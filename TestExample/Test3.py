#!/usr/bin/python
# -*- coding: utf-8 -*-
from Common.Scene.GameDefine_Scene import *

cd = bytearray([0] * MAX_CHAR_COMMONDATA_NUM)
cf = bytearray([0] * MAX_CHAR_COMMONFLAG_NUM)

def setcd(index, value):
    #每个数据按照4个字节进行存储
    for i in range(4):
        cd[i + (index * 4)] = (value >> ((4 - 1 - i % 4) * 8)) & 0XFF
def getcd(index):
    value = 0
    for i in range(4):
        value += (cd[i + (index * 4)] << ((4 - 1 - i % 4) * 8))
    return value

def setcf(index, value):
    byteIndex = int(index / 8)
    bitIndex = index % 8
    value = value << (8 - 1 - bitIndex)
    cf[byteIndex] |= value
    print(index, byteIndex, bitIndex, value)

def getcf(index):
    byteIndex = int(index / 8)
    bitIndex = index % 8
    value = cf[byteIndex] >> (8 - 1 - bitIndex)
    value = value & 1
    return value

print(cd)
#print(cf)

setcd(0, 4294967295)
setcd(1, 328789654)
setcd(2, 65535)
setcd(3, 2)
print(cd)
print(getcd(0))
print(getcd(1))
print(getcd(2))
print(getcd(3))

dbs = Bytes2DBString(cd)
print(dbs)
bs = DBString2Bytes(dbs)
print(bs)
print(DBString2Bytes(Bytes2DBString(cd)) == cd)
'''
setcf(0, 1)
setcf(1, 1)
setcf(8, 1)
setcf(9, 1)
setcf(56, 1)
setcf(63, 1)
print(cf)
print(getcf(8))
print(getcf(56))
print(getcf(7))
print(getcf(6))
print(getcf(63))
print(getcf(62))
s = hex(cf[0])[2]
'''
class T:
    def __init__(self):
        self.data = 10

list = []
for i in range(3):
    list.append(T())
print(list[0])
print(list[1])
print(list[2])
list[1].data = 11
print(list[0])
print(list[1])
print(list[2])
print(list[0].data)