#!/usr/bin/python
# -*- coding: utf-8 -*-

class TimeInfo:
    def __init__(self):
        self.timeElapsed = 0
        self.diffYear = False
        self.diffMonth = False
        self.diffWeek = False
        self.diffDay00 = False
        self.diffDay04 = False
        self.diffDay12 = False
        self.diffDay18 = False
        self.diffDay20 = False
        self.diffHour = False
        self.diffHalfHour = False
        self.diffEvenHour = False
        self.diffMinute = False
        self.diffSecond = False

    def updateTimeInfo(self, te, dy, dm, dw, dd00, dd04, dd12, dd18, dd20, dh, dhh, deh, dmi, ds):
        self.timeElapsed = te
        self.diffYear = dy
        self.diffMonth = dm
        self.diffWeek = dw
        self.diffDay00 = dd00
        self.diffDay04 = dd04
        self.diffDay12 = dd12
        self.diffDay18 = dd18
        self.diffDay20 = dd20
        self.diffHour = dh
        self.diffHalfHour = dhh
        self.diffEvenHour = deh
        self.diffMinute = dmi
        self.diffSecond = ds
