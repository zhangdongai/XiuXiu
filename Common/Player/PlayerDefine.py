#!/usr/bin/python
# -*- coding: utf-8 -* -

PLAYER_ID_GENERATE = 0

#客户端服务器链接player状态
PLAYERSTATUS_EMPTY = 0
PLAYERSTATUS_CONNECTED = 1
PLAYERSTATUS_VALIDATING = 2#账号验证中
PLAYERSTATUS_VALIDATE_OK = 3#账号验证正确
PLAYERSTATUS_VALIDATE_FAILED = 4#账号验证失败
PLAYERSTATUS_ACCOUNTSTATE_CHECKING = 5#检查账号状态
PLAYERSTATUS_ACCOUNTSTATE_CHECKOK = 6#检查账号成功
PLAYERSTATUS_ACCOUNTSTATE_CHECKFAILED = 7#检查账号失败
PLAYERSTATUS_QUEUEING = 8#正在排队
PLAYERSTATUS_QUEUE_FINISH = 9#排队结束
PLAYERSTATUS_CHARLIST_QUERYING = 10#查询角色列表
PLAYERSTATUS_CHARLIST_QUERY_OK = 11#角色列表查询成功
PLAYERSTATUS_CREATEINGCHAR = 12 #正在创建角色
PLAYERSTATUS_CREATECHAR_SUCCESS = 13    #创建角色成功
PLAYERSTATUS_CREATECHAR_FAILED = 14 #创建角色失败
PLAYERSTATUS_LOADINGCHAR = 15   #正在加载角色
PLAYERSTATYS_LOADCHAR_SUCCESS = 16  #角色加载成功
PLAYERSTATUS_LOADCHAR_FAILED = 17   #角色加载失败
PLAYERSTATUS_READYENTERWORLD = 18   #准备进入场景
PLAYERSTATUS_ENTERINGWORLD = 19 #正在进入场景
PLAYERSTATUS_SCENEPLAYING = 20 #正在场景中

class PlayerQueueData:
    def __init__(self, account, playerId, ql):
        self.account = account
        self.playerId = playerId
        self.queueLevel = ql

    def setQueueLevel(self, queueLevel):
        self.queueLevel = queueLevel

    def __lt__(self, other):
        return self.queueLevel < other.queueLevel

    def __gt__(self, other):
        return self.queueLevel > other.queueLevel

    def __eq__(self, other):
        return  self.queueLevel == other.queueLevel