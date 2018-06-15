#!/usr/bin/python
# -*- coding: utf-8 -*-

class IniReader:
    def __init__(self):
        self.dataList = {}

    def load(self, filename):
        fs = open(filename, 'r', -1, 'utf-8')
        lines = fs.readlines()
        fs.close()
        blocklist = {}
        title = ''
        linecount = len(lines)
        lineindex = 0
        for line in lines:
            lineindex += 1
            #空行或者注释行直接略过
            if len(line) == 0 or line[0] == '#' or line[0] == ' ':
                continue
            if line[0] == '[':
                #遇到下一个title时将上一个title记录下来
                if title != '':
                    self.dataList[title] = blocklist
                    blocklist = {}
                endindex = line.find(']')
                if endindex == -1:
                    #error log!!!
                    return
                title = line[1:endindex]
            else:
                symbolindex = line.find('=')
                endindex = line.find('#')
                key = line[0:symbolindex]
                value =line[symbolindex + 1:endindex]
                blocklist[key] = value

            #把最后的一个title数据记录下来
            if lineindex == linecount:
                if title != '' and len(blocklist) != 0:
                    self.dataList[title] = blocklist

    def readInt(self, title, key):
        if title in self.dataList.keys():
            list = self.dataList[title]
            if key in list.keys():
                return int(list[key])
        return -1

    def readFloat(self, title, key):
        if title in self.dataList.keys():
            list = self.dataList[title]
            if key in list.keys():
                return float(list[key])
        return 0.0

    def readString(self, title, key):
        if title in self.dataList.keys():
            list = self.dataList[title]
            if key in list.keys():
                return list[key]
        return ''
