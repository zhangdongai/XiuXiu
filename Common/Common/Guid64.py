#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
看到这个模块的人，应该写过C/C++，或者Java，起码他要懂得字节、位、有符号无符号的区别、各个数据类型占几个字节、各个数据类型的最大值等知识

Guid64是一个64位bit的唯一码类。将64为分成4个数据块，分别为head、type、carry和serial。分别表示唯一码头信息、唯一码类型、唯一码进位和唯一码序号
4个数据块全部默认为无符号类型，占用的字节数分别为2个、1个、1个、4个。bit位数分别为16位、8位、8位、32位。
最大值分别设置为0XFFFF、0XFF、0XFF和0XFFFF0000。serial是为了做容错处理才设置为0XFFFF0000，理论上的最大值为0XFFFFFFFF
'''

import Common.Common.GeneralSet as GeneralSet
from Common.Message.DBMsg import *
from Common.Common.BaseDefine import *
from Service.ServiceManager import *
from Common.Table.TableManager import *
from Common.Common.GeneralSet import *
import mysql.connector
from Log.Log import *

GUID_MAXHEAD   = 0XFFFF
GUID_MAXTYPE   = 0XFF
GUID_MAXCARRY  = 0XFF
GUID_MAXSERIAL = 0XFFFF0000
INVALID_GUID   = 0XFFFFFFFFFFFFFFFF

class Guid64:
    def __init__(self, head, type, carry, serial):
        self.head = head
        self.type = type
        self.carry = carry
        self.serial = serial
        self.value64 = 0
        self.general64()
        
    def general64(self):
        self.value64 = (self.head << 48) + (self.type << 40) + (self.carry << 32) + self.serial

    #print函数返回格式化结果
    def __str__(self):
        return str('%016X' % self.value64)

    #运算符重载Begin
    #self<otherGuid
    def __lt__(self, otherGuid):
        if not isinstance(otherGuid, Guid64):
            print('error type')
            return False
        return self.value64 < otherGuid.value64
    #self>otherGuid
    def __gt__(self, otherGuid):
        if not isinstance(otherGuid, Guid64):
            print('error type')
            return False
        return self.value64 > otherGuid.value64
    #self<=otherGuid
    def __le__(self, otherGuid):
        if not isinstance(otherGuid, Guid64):
            print('error type')
            return False
        return self.value64 <= otherGuid.value64
    #self>=otherGuid
    def __ge__(self, otherGuid):
        if not isinstance(otherGuid, Guid64):
            print('error type')
            return False
        return self.value64 >= otherGuid.value64
    #self==otherGuid
    def __eq__(self, otherGuid):
        if not isinstance(otherGuid, Guid64):
            print('error type')
            return False
        return self.value64 == otherGuid.value64
    #self!=otherGuid
    def __ne__(self, otherGuid):
        if not isinstance(otherGuid, Guid64):
            print('error type')
            return False
        return self.value64 != otherGuid.value64
    #运算符重载End

    def low32(self):
        return self.serial
    def high32(self):
        return (self.head << 16) + (self.type << 8) + self.carry

    def get64(self):
        return self.value64
    def gethead(self):
        return self.head
    def gettype(self):
        return self.type
    def getcarry(self):
        return self.carry
    def getserial(self):
        return self.serial

    def isvalid(self):
        return self.value64 != INVALID_GUID

    def construct(self, value64):
        self.value64 = value64

    

class GuidGenerator:
    def __init__(self, type, carry, serial):
        self.head = GeneralSet.gServerId
        self.type = type
        self.incSerial = {'carry' : carry, 'serial' : serial}#逐1生成Guid并记录
        self.signalSerial = {'carry' : carry, 'serial' : serial}#Guid生成达到标记最大值数值

    def Gen(self):
        nextSerial = self.incSerial['carry'] + 1
        if self.incSerial['carry'] >= self.signalSerial['carry'] and self.incSerial['serial'] >= self.signalSerial['serial']:
            #每次增加512个，512期间内生成新Guid不再存储
            self.IncSignalSerial(512)
            self.Save()

        guid64 = Guid64(self.head, self.type, self.incSerial['carry'], self.incSerial['serial'])
        Log('Guid', 'generate new guid(%d, %d, %d, %d)', self.head, self.type, self.incSerial['carry'], self.incSerial['serial'])
        self.IncIncSerial(1)
        return guid64

    def IncSignalSerial(self, incValue):
        self.signalSerial['serial'] += incValue
        if self.signalSerial['serial'] >= GUID_MAXSERIAL:
            #serial不得设置为0，必须设置为余数
            self.signalSerial['serial'] = self.signalSerial['serial'] % GUID_MAXSERIAL
            self.signalSerial['carry'] += 1

    def IncIncSerial(self, incValue):
        self.incSerial['serial'] += incValue
        if self.incSerial['serial'] >= GUID_MAXSERIAL:
            #serial不得设置为0，必须设置为余数
            self.incSerial['serial'] = self.incSerial['serial'] % GUID_MAXSERIAL
            self.incSerial['carry'] += 1
    
    def Save(self):
        #为了做容错处理，在存储时额外多增加1024然后再存储
        tempSerial = self.signalSerial['serial'] + 1024
        tempCarry = self.signalSerial['carry']
        if tempSerial >= GUID_MAXSERIAL:
            #serial不得设置为0，必须设置为余数
            tempSerial = tempSerial % GUID_MAXSERIAL
            tempCarry += 1

        saveMsg = DBSaveGuidMsg()
        saveMsg.gtype = self.type
        saveMsg.carry = tempCarry
        saveMsg.serial = tempSerial
        gServiceManager.SendMessage2Srv(SERVICE_ID_DB, saveMsg)



#定义各个用途的Guid生成器
#默认设置为NULL，不要在外部初始化Generator，因为引用ServerId有可能没有初始化
GUID_CHAR = 0
GUID_FELLOW = 1
GUID_TEIM = 2
GUID_MAIL = 3
GUID_COUNT= 4
gGuidGenerator = []

def GENERATE_GUID(GUIDTYPE):
    try:
        ASSERT(GUIDTYPE >= GUID_CHAR and GUIDTYPE < GUID_COUNT, 'guidtype out of index')
        return gGuidGenerator[GUIDTYPE].Gen()
    except BaseException as err:
        ASSERT(False, 'Guid64:GENERATE_GUID, ' + str(err))


def LoadGuidFromDB():
    try:
        serverConfig = gTableManager.getServerConfigListById(ServerId())
        connConfig = {}
        connConfig['user'] = serverConfig.DBUser
        connConfig['password'] = serverConfig.DBPsw
        connConfig['database'] = serverConfig.DBName
        connConfig['host'] = serverConfig.DBIp
        connConfig['port'] = serverConfig.DBPort
        # 默认的链接编码为utf8，但是我们依然要明文指定为utf8
        connConfig['charset'] = 'utf8'
        # 需要保证一点：数据库存储数据必须为utf8格式。客户端、服务器、数据库包括其中的链接必须是utf8
        connector = mysql.connector.connect(**connConfig)
        cursor = connector.cursor(buffered=True)
        cursor.execute('select * from t_guid')
        resultCount = cursor.rowcount

        DB_TYPE = 0
        DB_CARRY = 1
        DB_SERIAL = 2

        for i in range(resultCount):
            resultTuple = cursor.fetchone()
            print(resultTuple)
            type = resultTuple[DB_TYPE]
            carry = resultTuple[DB_CARRY]
            serial = resultTuple[DB_SERIAL]
            gGuidGenerator.append(GuidGenerator(type, carry, serial))

        cursor.close()
        connector.close()

    except BaseException as err:
        ASSERT(False, 'loadGuidFromDB, ' + str(err))



    
