#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.Common.Assert import *
from Common.Common.BaseDefine import *
import select
from Log.Log import *

CONNECTIONTIME_LIMIT = 6000
class PlayerManager:
    def __init__(self):
        self.playerList = {}
        self.readlist = []
        self.writelist = []
        self.errlist = []

        self.connectionTime = CONNECTIONTIME_LIMIT#连接心跳的时间间隔，6秒

    def tick(self, timeInfo):
        try:
            self.tick_Socket()
            self.tick_Input()
            self.tick_Output()
            self.tick_Command()
            self.tick_Connection(timeInfo)
        except BaseException as err:
            VERIFY(False, 'PlayerManager:tick, ' + str(err))

    def tick_Socket(self):
        try:
            if len(self.playerList) == 0:
                return
            self.readlist = []
            self.writelist = []
            for player in self.playerList.values():
                self.readlist.append(player.Socket.socket)
                self.writelist.append(player.Socket.socket)
            self.readlist, self.writelist, self.errlist = select.select(self.readlist, self.writelist, self.errlist, 0)
        except BaseException as err:
            VERIFY(False, 'PlayerManager:tick_Socket, ' + str(err))

    def tick_Input(self):
        try:
            if len(self.playerList) == 0:
                return
            #在列表的遍历内部不能对列表进行添加和删除操作，所以需要对列表复制一份
            playerValues = list(self.playerList.values())
            #这样是存了列表的一个引用，并不是复制
            #playerValues = self.playerList.values()
            for player in playerValues:
                try:
                    if player.Socket.socket in self.readlist:
                        #接受消息发生错误，直接断开连接
                        if player.ProcessInput() == False:
                            self.delPlayer(player)
                            continue
                except BaseException as err:
                    self.delPlayer(player)
                    VERIFY(False, 'PlayerManager:tick_Input, player.ProcessInput, ' + str(err))
                    continue
        except BaseException as err:
            VERIFY(False, 'PlayerManager:tick_Input, ' + str(err))

    def tick_Output(self):
        try:
            if len(self.playerList) == 0:
                return
            # 在列表的遍历内部不能对列表进行添加和删除操作，所以需要对列表复制一份
            playerValues = list(self.playerList.values())
            # 这样是存了列表的一个引用，并不是复制
            # playerValues = self.playerList.values()
            for player in playerValues:
                try:
                    if player.Socket.socket in self.writelist:
                        if player.ProcessOutput() == False:
                            self.delPlayer(player)
                            continue
                except BaseException as err:
                    VERIFY(False, 'PlayerManager:tick_Output, player.ProcessOutput, ' + str(err))
                    self.delPlayer(player)
                    continue
        except BaseException as err:
            VERIFY(False, 'PlayerManager:tick_Output, ' + str(err))

    def tick_Command(self):
        try:
            if len(self.playerList) == 0:
                return
            # 在列表的遍历内部不能对列表进行添加和删除操作，所以需要对列表复制一份
            playerValues = list(self.playerList.values())
            # 这样是存了列表的一个引用，并不是复制
            # playerValues = self.playerList.values()
            for player in playerValues:
                try:
                    if player.Socket.socket in self.readlist:
                        if player.ProcessCommand() == False:
                            self.delPlayer(player)
                            continue
                except BaseException as err:
                    VERIFY(False, 'PlayerManager:tick_Command, player.ProcessCommand, ' + str(err))
                    self.delPlayer(player)
                    continue
        except BaseException as err:
            VERIFY(False, 'PlayerManager:tick_Command, ' + str(err))

    def tick_Connection(self, timeInfo):
        try:
            if self.connectionTime > 0:
                self.connectionTime -= timeInfo.timeElapsed
                return
            self.connectionTime = CONNECTIONTIME_LIMIT
            if len(self.playerList) == 0:
                return
            # 在列表的遍历内部不能对列表进行添加和删除操作，所以需要对列表复制一份
            playerValues = list(self.playerList.values())
            # 这样是存了列表的一个引用，并不是复制
            # playerValues = self.playerList.values()
            for player in playerValues:
                try:
                    if player.Socket.socket in self.writelist:
                        if player.ProcessConnection() == False:
                            self.delPlayer(player)
                            continue
                except BaseException as err:
                    VERIFY(False, 'PlayerManager:tick_Connection, player.ProcessConnection, ' + str(err))
                    self.delPlayer(player)
                    continue
        except BaseException as err:
            VERIFY(False, 'PlayerManager:tick_Connection, ' + str(err))

    def addPlayer(self, player, firstLogin=False):
        try:
            self.playerList[player.getId()] = player
            print('PlayerManager::addPlayer, playerid = %d, playercount = %d' %
                  (player.Id, len(self.playerList)))
            Log('Player', 'PlayerManager::addPlayer, playerid = %d, playercount = %d', player.Id, len(self.playerList))
            self.onAddPlayer(player, firstLogin)
        except BaseException as err:
            ASSERT(False, 'PlayerManager:addPlayer, ' + str(err))

    def delPlayer(self, player):
        try:
            playerId = player.getId()
            ASSERT(playerId in self.playerList.keys(), 'player is not in playerList')
            del self.playerList[playerId]
            self.onDelPlayer(player)
            print('del player %d, current player count%d' % (playerId, len(self.playerList)))
            Log('Player', 'del player %d, current player count%d', playerId, len(self.playerList))
        except BaseException as err:
            ASSERT(False, 'PlayerManager:delPlayer, ' + str(err))

    def delAllPlayer(self):
        try:
            for player in self.playerList.values():
                player.die()
            self.playerList = []
        except BaseException as err:
            ASSERT(False, 'PlayerManager:delAllPlayer, ' + str(err))

    def onAddPlayer(self, player, firstLogin):
        pass

    def onDelPlayer(self, player):
        pass

    def getPlayer(self, playerId):
        try:
            if playerId in self.playerList.keys():
                return self.playerList[playerId]
        except BaseException as err:
            ASSERT(False, 'PlayerManager:getPlayer, ' + str(err))
        return None
            
