#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.Message.MessageDefine import *

class AccountStateCheckMsg:
    def __init__(self):
        self.type = MESSAGE_TYPE_ACCOUNTSTATE_CHECK
        self.playerId = -1
        self.account = ''

class QueueFinishMsg:
    def __init__(self):
        self.type = MESSAGE_TYPE_QUEUE_FINISH
        self.playerId = -1
        self.account = ''

class AccountOfflineMsg:
    def __init__(self):
        self.type = MESSAGE_TYPE_ACCOUNT_OFFLINE
        self.account = ''