#!/usr/bin/python
# -*- coding: utf-8 -*-

#按位做异或，必须定义为bytes类型
XorKey = b'1E95A51FD4C38CD68428186BC5C3E26F'
keyLen = len(XorKey)

#参数必须为bytes类型，返回值为bytes类型
def Xor(buffer):
    #按照bytes的长度循环
    byteLen = len(buffer)
    #结果先存储到bytearray内部
    bytea = bytearray()
    for i in range(byteLen):
        bytea.append(buffer[i] ^ XorKey[i % keyLen])
    return bytes(bytea)

def XorEncrypt(buffer):
    return Xor(buffer)

def XorDecrypt(buffer):
    return Xor(buffer)

