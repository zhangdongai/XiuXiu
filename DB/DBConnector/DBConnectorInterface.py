#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from Service.ServiceManager import *
from Common.Common.Assert import *
import mysql.connector
from Log.Log import *

class DBConnectorInterface:
    def __init__(self):
        self.connected = False
        self.connector = None
        self.cursor = None
        self.connConfig = {}

        self.queryComm = ''

        self.resultCount = 0
        self.resultItertor = None
        self.resultCursor = None

        self.fetchTuple = ()
        self.fetchList = []
        self.fetchIndex = 0

    def init(self):
        '''
        connargs = {'user':'ServiceTech', 'password':'U743g3asgvASAa',
                    'database':'servicetechdb_1', 'host':'123.57.58.164',
                    'charset':'utf8'}
        #conn = mysql.connector.connect(**connargs)
        conn = mysql.connector.connect(user='ServiceTech', password='U743g3asgvASAa',
                                       database='servicetechdb_1', host='123.57.58.164')
        cur = conn.cursor()
        cur.execute('use servicetechdb_1')
        cur.execute('select count(1) from t_char')
        print(cur.rowcount)
        print(cur.fetchall())
        retlist = cur.execute('call load_char_info(%s)', (28428972647776256,), multi=True)
        for ret in retlist:
            if ret.with_rows:
                print(ret.fetchall())
        '''
        pass

    def __del__(self):
        pass

    def setQueryComm(self, comm):
        self.queryComm = comm

    def cleanQueryComm(self):
        self.queryComm = ''

    def getResultCount(self):
        return self.resultCount

    def connect(self, user, pwd, database, hostIp, port):
        try:
            ASSERT(self.connected == False, 'DBConnector is connected!')
            self.connConfig['user'] = user
            self.connConfig['password'] = pwd
            self.connConfig['database'] = database
            self.connConfig['host'] = hostIp
            self.connConfig['port'] = port
            #默认的链接编码为utf8，但是我们依然要明文指定为utf8
            self.connConfig['charset'] = 'utf8'
            #需要保证一点：数据库存储数据必须为utf8格式。客户端、服务器、数据库包括其中的链接必须是utf8
            self.connector = mysql.connector.connect(**self.connConfig)
            self.cursor = self.connector.cursor(buffered=True)
            self.connected = True
        except BaseException as err:
            self.close()
            ASSERT(False, 'DBConnectorInterface:connect, ' + str(err))

    def reconnect(self):
        try:
            ASSERT(self.connected == False, 'DBConnector is connected!')
            self.connector = mysql.connector.connect(**self.connConfig)
            self.cursor = self.connector.cursor(buffered=True)
            self.connected = True
        except BaseException as err:
            self.close()
            #重新链接失败，不再继续抛出异常
            VERIFY(False, 'DBConnectorInterface:reconnect, ' + str(err))

    def isConnected(self):
        return self.connected

    def close(self):
        try:
            if self.cursor != None:
                self.cursor.close()
                self.cursor = None
            if self.connector != None:
                self.connector.close()
                self.connector = None
            self.connected = False
            self.free()
        except BaseException as err:
            ASSERT(False, 'DBConnectorInterface:close, ' + str(err))

    def execute(self, multi=True):
        try:
            #执行之前先free掉一些变量
            self.free()
            print('DBConnectorInterface:execute, query=', self.queryComm)
            Log('DB', 'query=%s', self.queryComm)
            ASSERT(self.queryComm != '', 'Query Command is null!')
            ASSERT(self.connector != None and self.cursor != None, 'connector or cursor is None!')
            ASSERT(self.connected == True, 'can not connected to db!')
            #multi设置为true，表示默认执行多端sql语句，适用于存储过程
            self.resultItertor = self.cursor.execute(self.queryComm, multi=multi)
            if multi == False:
                self.resultCount = self.cursor.rowcount()
            fetchCount = self.fixCursor(multi)
            #并不是所有的执行结果的resultCursor都不是None
            #ASSERT(self.resultCursor != None, 'DBConnectorInterface:execute, result Cursor is None!')
            #self.resultCount = fetchCount if self.resultCursor == None else self.resultCursor.rowcount
            self.resultCount = fetchCount
            #sql执行结束，commit一次，我觉得最好加！
            self.commit()
        except BaseException as err:
            self.close()
            ASSERT(False, 'DBConnectorInterface:execute, ' + str(err))

    #
    def fetch(self):
        try:
            ASSERT(self.resultCursor != None, 'result Cursor is None!')
            ASSERT(self.fetchIndex < self.resultCount, 'fetch Index is out of range')
            #self.fetchTuple = self.resultCursor.fetchone()
            self.fetchTuple = self.fetchList[self.fetchIndex]
            self.fetchIndex += 1
        except BaseException as err:
            self.close()
            ASSERT(False, 'DBConnectorInterface:fetch, ' + str(err))

    #该函数内部调用，禁止外部调用！
    def fetchall(self, multi=True):
        try:
            ASSERT(self.resultCursor != None, 'result Cursor is None!')
            self.fetchList = self.resultCursor.fetchall()
        except BaseException as err:
            self.close()
            ASSERT(False, 'DBConnectorInterface:fetchall, ' + str(err))

    '''
    20170302注释
    创建角色后继续查询角色数据，发现无法正确查询到数据。反复测试定位到该函数的break语句：
    如果按照之前的实现方法（增加break），连续进行两次数据库操作，只有第一次可以fetch到数据，第二次无法fetch到数据。
    如果去掉break，则可能两次都fetch不到数据，很奇怪的问题。
    暂时还未完全get到问题的原因，猜测可能和cur in self.resultItertor有关，即保存的cur对象再次循环可能会失效
    所以修改方法为：
    1，查询到有效的cur后，直接fetchall出所有数据，不再使用fetchone函数。
    2，查询到有效的cur后，立即记录影响行数
    '''
    def fixCursor(self, multi=True):
        try:
            ret = 0
            if multi == False:
                self.resultCursor = self.cursor
            else:
                for cur in self.resultItertor:
                    #有返回结果时，保存返回结果
                    if cur.with_rows:
                        if self.resultCursor == None:
                            self.resultCursor = cur
                            ret = self.resultCursor.rowcount
                            #直接fetch出所有结果
                            self.fetchall()
                            ######注意事项######
                            #break
                            ######注意事项######
                    else:
                        #没有返回结果时，这样取得影响行数
                        if self.resultCursor == None:
                            ret = cur.rowcount
            print('DBConnectorInterface:fixCursor cur=', self.resultCursor, multi)
            return ret
        except BaseException as err:
            ASSERT(False, 'DBConnectorInterface:fixCursor, ' + str(err))
        return 0

    def commit(self):
        try:
            ASSERT(self.connector != None and self.cursor != None, 'connector or cursor is None!')
            ASSERT(self.connected == True, 'can not connected to db!')
            self.connector.commit()
        except BaseException as err:
            ASSERT(False, 'DBConnectorInterface:commit, ' + str(err))

    def free(self):
        self.resultCursor = None
        self.resultItertor = None
        self.fetchIndex = 0
        self.resultCount = 0
        self.fetchTuple = ()
        self.fetchList = []

    def getInt(self, index):
        try:
            ASSERT(index < len(self.fetchTuple), 'index%d out of range!' % index)
            return int(self.fetchTuple[index])
        except BaseException as err:
            ASSERT(False, 'DBConnectorInterface:getInt, ' + str(err))
        return 0

    def getFloat(self, index):
        try:
            ASSERT(index < len(self.fetchTuple), 'index%d out of range!' % index)
            return float(self.fetchTuple[index])
        except BaseException as err:
            ASSERT(False, 'DBConnectorInterface:getFloat, ' + str(err))
        return 0

    def getString(self, index):
        try:
            ASSERT(index < len(self.fetchTuple), 'index%d out of range!' % index)
            return self.fetchTuple[index]
        except BaseException as err:
            ASSERT(False, 'DBConnectorInterface:getString, ' + str(err))
        return 0