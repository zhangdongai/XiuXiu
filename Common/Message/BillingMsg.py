#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.Message.MessageDefine import *
from Common.Billing.GameStruct_Billing import *

class RequestHttpMessage:
    def __init__(self):
        self.type = MESSAGE_TYPE_REQUESTHTTP
        self.senddata = 10

class ReqAccountVerify:
    def __init__(self):
        self.type = MESSAGE_TYPE_ACCOUNTVERIFY_REQ
        self.playerId = -1
        self.account = ''

class RetAccountVerify:
    def __init__(self):
        self.type = MESSAGE_TYPE_ACCOUNTVERIFY_RET
        self.playerId = -1
        self.result = False

class ValidateAccountReqMsg:
    def __init__(self):
        self.type = MESSAGE_TYPE_ACCOUNTVALIDATE_REQ
        self.validateData = CommonValidateData()

class ValidateAccountRetMsg:
    def __init__(self):
        self.type = MESSAGE_TYPE_ACCOUNTVALIDATE_RET
        self.validateType = 0
        self.playerId = -1
        self.account = ''
        self.deviceId = ''
        self.deviceType = ''
        self.deviceVersion = ''
        self.channelId = ''
        self.mediaId = ''
        self.result = 0
        self.oid = ''
        self.accessToken = ''
        self.validateInfo = ''
        self.shouldCache = False
        self.rapidValidateCode = 0
        self.hostIp = ''