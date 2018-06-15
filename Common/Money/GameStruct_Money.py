#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.Common.Assert import *
from Common.Money.GameDefine_Money import *

class MoneyData:
    def __init__(self):
        self.money = [0] * MONEYTYPE_COUNT

    def getMoney(self, type):
        try:
            ASSERT(type > MONEYTYPE_INVALID and type < MONEYTYPE_COUNT, 'moneytype is out of range')
            return self.money[type]
        except BaseException as err:
            ASSERT(False, 'MoneyData:getMoney, ' + str(err))

    def setMoney(self, type, value):
        try:
            ASSERT(type > MONEYTYPE_INVALID and type < MONEYTYPE_COUNT, 'moneytype is out of range')
            ASSERT(value >= 0, 'money value is lt 0!')
            self.money[type] = value
        except BaseException as err:
            ASSERT(False, 'MoneyData:setMoney, ' + str(err))