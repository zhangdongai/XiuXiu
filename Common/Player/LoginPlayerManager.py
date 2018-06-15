#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.Player.PlayerManager import *
from Common.Common.Assert import *
from Common.Common.BaseDefine import *
from Common.Player.PlayerDefine import *
from Log.Log import *

class LoginPlayerManager(PlayerManager):
    def __init__(self, loginService):
        super(LoginPlayerManager, self).__init__()
        self.loginService = loginService

    def tick(self, timeInfo):
        try:
            super(LoginPlayerManager, self).tick(timeInfo)
        except BaseException as err:
            VERIFY(False, 'LoginPlayerManager:tick, ' + str(err))

    def onDelPlayer(self, player):
        delPlayer = False
        status = player.getStatus()
        if status == PLAYERSTATUS_CONNECTED or \
           status == PLAYERSTATUS_VALIDATING or \
           status == PLAYERSTATUS_VALIDATE_OK or \
           status == PLAYERSTATUS_VALIDATE_FAILED or \
           status == PLAYERSTATUS_ACCOUNTSTATE_CHECKING or \
           status == PLAYERSTATUS_ACCOUNTSTATE_CHECKOK or \
           status == PLAYERSTATUS_ACCOUNTSTATE_CHECKFAILED or \
           status == PLAYERSTATUS_CREATECHAR_FAILED or \
           status == PLAYERSTATUS_LOADCHAR_FAILED:
            delPlayer = False
        elif status == PLAYERSTATUS_QUEUEING or \
             status == PLAYERSTATUS_QUEUE_FINISH or \
             status == PLAYERSTATUS_CHARLIST_QUERYING or \
             status == PLAYERSTATUS_CHARLIST_QUERY_OK or \
             status == PLAYERSTATUS_CREATEINGCHAR or \
             status == PLAYERSTATUS_CREATECHAR_SUCCESS or \
             status == PLAYERSTATUS_LOADINGCHAR or \
             status == PLAYERSTATYS_LOADCHAR_SUCCESS or \
             status == PLAYERSTATUS_READYENTERWORLD or \
             status == PLAYERSTATUS_ENTERINGWORLD:
            delPlayer = True

        if delPlayer:
            self.loginService.olDelPlayer(player.ObjLogin.account)

    def popReadyEnterWorldPlayer(self):
        retPlayer = None
        try:
            for player in self.playerList.values():
                if player.getStatus() == PLAYERSTATUS_READYENTERWORLD:
                    retPlayer = player
                    self.delPlayer(player)
                    return  retPlayer
        except BaseException as err:
            ASSERT(False, 'LoginPlayerManager:popReadyEnterWorldPlayer, ' + str(err))
        return None

            
