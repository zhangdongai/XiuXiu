#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from Service.BaseService import *

class ServiceManager:
    def __init__(self):
        self.serviceList = {}
    
    def register(self, service):
        self.serviceList[service.getId()] = service

    def initAllService(self):
        for service in self.serviceList.values():
            service.init()

    def run(self):
        self.runMaiLogic()
        self.runShutdown()

    def runMaiLogic(self):
        while True:
            try:
                for service in self.serviceList.values():
                    service.tick()
                if self.isShouldShutdown():
                    print('ServiceManager::runMaiLogic begin to shutdown')
                    break
            except BaseException as err:
                break

    def runShutdown(self):
        for service in self.serviceList.values():
            print('ServiceManager::runShutdown begin to stopService %d' % service.getId())
            service.stopService()

    def isShouldShutdown(self):
        fileName = os.getcwd() + '\shutdown.py'
        #print(os.getcwd())#获取当前目录
        #print(os.path.abspath('..'))#获取第一层父级目录
        #print(fileName)
        if os.path.exists(fileName):
            os.remove(fileName)
            return True
        return False

    def SendMessage2Srv(self, serviceId, msg):
        if serviceId in self.serviceList.keys():
            print('ServiceManager.SendMessage2Srv, serviceId = ', serviceId)
            self.serviceList[serviceId].receiveMessage(msg)

            
gServiceManager = ServiceManager()