#!/usr/bin/python
# -*- coding: utf-8 -*-

from Login.LoginService import *
from Billing.BillingService import *
from Log.LogService import *
from DB.DBService import *
from Scene.SceneService import *
from Common.Table.TableManager import *
import Common.Common.GeneralSet as GeneralSet
from Common.Common.Config import *
from Common.Common.Assert import *
from Common.Common.Guid64 import *

#这是python程序的入口函数，c++程序首先调用这个函数初始化python内部的对象
def Py_Run(worldId):
    try:
        GeneralSet.gServerId = worldId
        gTableManager.initTable()
        print('table load end!')
        gGameConfig.load()
        print('config load end!')
        gPacketFactoryManager.Init()
        print('packetfactory init end!')
        InitLog()
        print('log init end!')
        Py_register()
        Py_init()
        print('services init end!')
        LoadGuidFromDB()
    except BaseException as err:
        print('Error!!!!Py_Run, ' + str(err))

def Py_register():
    gServiceManager.register(Py_LoginService)
    gServiceManager.register(Py_BillingService)
    gServiceManager.register(Py_LogService)
    gServiceManager.register(Py_DBService)
    gServiceManager.register(Py_SceneService)

def Py_init():
    Py_LoginService.init()
    Py_BillingService.init()
    Py_LogService.init()
    Py_DBService.init()
    Py_SceneService.init()

