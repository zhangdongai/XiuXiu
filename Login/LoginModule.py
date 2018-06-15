#!/usr/bin/python
# -*- coding: utf-8 -*-

from Login.LoginService import *
from Billing.BillingService import *
from Service.ServiceManager import *
from Common.NetWork.Packet.PacketFactory import *

if __name__ == '__main__':
    print('main serviceMsg = ', gServiceManager)
    gPacketFactoryManager.Init()
    gServiceManager.register(LoginService())
    gServiceManager.register(BillingService())

    gServiceManager.initAllService()
    gServiceManager.run()
