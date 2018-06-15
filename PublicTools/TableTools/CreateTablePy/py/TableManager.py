#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.Table.Table_SceneClass import *
from Common.Table.Table_ServerConfigList import *
class TableManager:
    def __init__(self):
        self.tableList = {}
    def initTable(self):
        self.init_SceneClass()
        self.init_ServerConfigList()
    def init_SceneClass(self):
        print('begin load table SceneClass.txt')
        file = open('./Config/SceneClass.txt', 'r', -1, 'utf-8')
        lines = file.readlines()
        rowList = []
        index = 0
        for line in lines:
            index += 1
            if index <= 4:
                continue
            if len(line) == 0:
                continue
            table = Table_SceneClass()
            table.load(line)
            rowList.append(table)
        self.tableList['SceneClass'] = rowList
        print('end load table SceneClass.txt')

    def getSceneClassByIndex(self, index):
        rowList = self.tableList.get('SceneClass')
        if rowList == None:
            return None
        if index < 0 or index >= len(rowList):
            return None
        return rowList[index]

    def getSceneClassById(self, id):
        rowList = self.tableList.get('SceneClass')
        if rowList == None:
            return None
        for row in rowList:
            if row.__ID__ == id:
                return row
        return None

    def getSceneClassCount(self):
        rowList = self.tableList.get('SceneClass')
        if rowList == None:
            return 0
        return len(rowList)

    def init_ServerConfigList(self):
        print('begin load table ServerConfigList.txt')
        file = open('./Config/ServerConfigList.txt', 'r', -1, 'utf-8')
        lines = file.readlines()
        rowList = []
        index = 0
        for line in lines:
            index += 1
            if index <= 4:
                continue
            if len(line) == 0:
                continue
            table = Table_ServerConfigList()
            table.load(line)
            rowList.append(table)
        self.tableList['ServerConfigList'] = rowList
        print('end load table ServerConfigList.txt')

    def getServerConfigListByIndex(self, index):
        rowList = self.tableList.get('ServerConfigList')
        if rowList == None:
            return None
        if index < 0 or index >= len(rowList):
            return None
        return rowList[index]

    def getServerConfigListById(self, id):
        rowList = self.tableList.get('ServerConfigList')
        if rowList == None:
            return None
        for row in rowList:
            if row.__ID__ == id:
                return row
        return None

    def getServerConfigListCount(self):
        rowList = self.tableList.get('ServerConfigList')
        if rowList == None:
            return 0
        return len(rowList)

gTableManager = TableManager()