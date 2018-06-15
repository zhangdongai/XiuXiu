#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.Message.BillingMsg import *
from Service.ServiceManager import *
from Common.Billing.GameDefine_Billing import *
from Common.Common.ServiceDefine import *
import platform

class BillingInterface:
    @staticmethod
    def getBillingWorkMode():
        plat = platform.system()
        if plat == 'Windows':
            return BILLINGWORKMODE_PROJECT
        elif plat == 'Linux':
            return BILLINGWORKMODE_PROJECT
        return BILLINGWORKMODE_PROJECT

    @staticmethod
    def ValidateAccount(vtype, playerId, account, deviceId, deviceType,
                        deviceVersion, validateInfo, channelId, mediaChannelId,
                        rapidValidCode, hostIp):
        validateMsg = ValidateAccountReqMsg()
        validateMsg.validateData.validateType = vtype
        validateMsg.validateData.playerId = playerId
        validateMsg.validateData.account = account
        validateMsg.validateData.deviceId = deviceId
        validateMsg.validateData.deviceType = deviceType
        validateMsg.validateData.deviceVersion = deviceVersion
        validateMsg.validateData.validateInfo = validateInfo
        validateMsg.validateData.channelId = channelId
        validateMsg.validateData.mediaId = mediaChannelId
        validateMsg.validateData.rapidValidateCode = rapidValidCode
        validateMsg.validateData.hostIp = hostIp
        gServiceManager.SendMessage2Srv(SERVICE_ID_BILLING, validateMsg)
        print('ValidateAccount')

    @staticmethod
    def validateAccountOk(validateType, playerId, account,
                          deviceId, deviceType, deviceVersion,
                          channelId, mediaId, oId,
                          accessToken, validateInfo,
                          shouldCache, rapidValidateCode, hostIp):
        validateRetMsg = ValidateAccountRetMsg()
        validateRetMsg.validateType = validateType
        validateRetMsg.playerId = playerId
        validateRetMsg.account = account
        validateRetMsg.deviceId = deviceId
        validateRetMsg.deviceType = deviceType
        validateRetMsg.deviceVersion = deviceVersion
        validateRetMsg.channelId = channelId
        validateRetMsg.mediaId = mediaId
        validateRetMsg.result = VALIDATERESULT_SUCCESS
        validateRetMsg.oid = oId
        validateRetMsg.accessToken = accessToken
        validateRetMsg.validateInfo = validateInfo
        validateRetMsg.shouldCache = shouldCache
        validateRetMsg.rapidValidateCode = rapidValidateCode
        validateRetMsg.hostIp = hostIp
        gServiceManager.SendMessage2Srv(SERVICE_ID_LOGIN, validateRetMsg)

    @staticmethod
    def validateAccountFailed(validateType, playerId, result, hostIp):
        validateRetMsg = ValidateAccountRetMsg()
        validateRetMsg.validateType = validateType
        validateRetMsg.playerId = playerId
        validateRetMsg.account = ''
        validateRetMsg.deviceId = ''
        validateRetMsg.deviceType = ''
        validateRetMsg.deviceVersion = ''
        validateRetMsg.channelId = ''
        validateRetMsg.mediaId = ''
        validateRetMsg.result = VALIDATERESULT_FAILED
        validateRetMsg.oid = ''
        validateRetMsg.accessToken = ''
        validateRetMsg.validateInfo = ''
        validateRetMsg.shouldCache = ''
        validateRetMsg.rapidValidateCode = ''
        validateRetMsg.hostIp = hostIp
        gServiceManager.SendMessage2Srv(SERVICE_ID_LOGIN, validateRetMsg)