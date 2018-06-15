#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.Player.PlayerManager import *
from Common.Common.Assert import *
from Common.Common.BaseDefine import *
from Common.Player.PlayerDefine import *
from Log.Log import *

class ScenePlayerManager(PlayerManager):
    def __init__(self, scene):
        super(ScenePlayerManager, self).__init__()

        self.scene = scene

    def tick(self, timeInfo):
        try:
            super(ScenePlayerManager, self).tick(timeInfo)
        except BaseException as err:
            VERIFY(False, 'ScenePlayerManager:tick, ' + str(err))

    def onAddPlayer(self, player, firstLogin):
        try:
            self.scene.addUser(player.ObjUser, firstLogin, len(self.playerList))
            Log('Player', 'ScenePlayerManager:onAddPlayer scene(%d, %d) add player(%d), firstLogin(%d)',
                self.scene.getClassId(),
                self.scene.getInstanceId(),
                player.getId(),
                firstLogin)
        except BaseException as err:
            ASSERT(False, 'ScenePlayerManager:onAddPlayer, ' + str(err))

            
