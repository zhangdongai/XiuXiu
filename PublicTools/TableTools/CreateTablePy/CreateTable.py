# -*- coding: utf-8 -*-

import sys
import os
import shutil
import re

fileFolder = '../ServerTables/'
pyfileFolder = '../../../XiuXiu/Common/Table/'

#判断文件夹是否存在
if not os.path.exists('./py'):
    pass
else:
    shutil.rmtree('./py')
os.makedirs('./py')

for rootDir, dirs, files in os.walk(fileFolder):
    print('go')
    fileList = []
    for txtfile in files:
        abstxtFile = os.path.abspath(txtfile)
        print(abstxtFile)
        #获取文件名
        if '.txt' not in txtfile:
            continue
        #读取txt文件
        txtStream = open(fileFolder + txtfile, 'r', -1, 'utf-16')
        lines = txtStream.readlines()
        #第一行是列名字，第二行时列数据类型，第三列是ServerceTechClient的原表示，暂时不用
        if len(lines) < 3:
            print('Error!!!!lins too shao!')
        #取出第一行
        columnName = lines[0].strip()
        columnNameList = columnName.split('	')
        #取出第二行
        columnType = lines[1].strip()
        columnTypeList = columnType.split('	')
        print(columnTypeList[len(columnTypeList) - 1])
        #检查列数
        nameCount = len(columnNameList)
        typeCount = len(columnTypeList)
        if nameCount != typeCount:
            print('Error!!!!nameCount != typeCount')
            break
        #检查类型
        for ct in columnTypeList:
            if ct != 'STRING' and ct != 'FLOAT' and ct != 'INT':
                print('ERROR!!! column Type', ct.strip())
                break
        txtStream.close()
        #取出文件名
        fileName = txtfile[0:len(txtfile) - 4]
        fileList.append(fileName)
        print(fileName)
        totalfileName = 'py/' + 'Table_' + fileName + '.py'
        print(totalfileName)
        fileStream = open(totalfileName, 'w')
        fileHead = '#!/usr/bin/python\n'
        fileHead += '# -*- coding: utf-8 -*-\n\n'
        fileStream.write(fileHead)
        fileBody = 'class Table_' + fileName + ':\n'
        fileBody += '    def __init__(self):\n'
        #先加一个ID
        fileBody += '        self.__ID__ = 0\n'
        for index in range(nameCount):
            #跳过第二列，是注释你忘了吗
            if index == 1:
                continue
            body = ''
            if columnTypeList[index] == 'STRING':
                body = '        self.' + columnNameList[index] + ' = \'\'\n'
            elif columnTypeList[index] == 'FLOAT':
                body = '        self.' + columnNameList[index] + ' = 0.0\n'
            elif columnTypeList[index] == 'INT':
                body = '        self.' + columnNameList[index] + ' = 0\n'
            fileBody += body
        fileStream.write(fileBody)
        
        fileBody = '\n    def load(self, row):\n'
        fileBody += '        fieldList = row.split('	')\n'
        #先加一个ID
        fileBody += '        self.__ID__ = int(fieldList[0])\n'
        for index in range(nameCount):
            #跳过第二列，是注释你忘了吗
            if index == 1:
                continue
            body = ''
            if columnTypeList[index] == 'STRING':
                body = '        self.' + columnNameList[index] + ' = fieldList[' + str(index) + ']\n'
            elif columnTypeList[index] == 'FLOAT':
                body = '        self.' + columnNameList[index] + ' = float(fieldList[' + str(index) + '])\n'
            elif columnTypeList[index] == 'INT':
                body = '        self.' + columnNameList[index] + ' = int(fieldList[' + str(index) + '])\n'
            fileBody += body
        fileStream.write(fileBody)
        fileStream.close()
        shutil.copy(totalfileName, pyfileFolder)

    #开始创建TableManager了
    mgrStream = open('py/TableManager.py', 'w')
    fileHead = '#!/usr/bin/python\n# -*- coding: utf-8 -*-\n\n'
    mgrStream.write(fileHead)
    classHead = 'class TableManager:\n'
    classHead += '    def __init__(self):\n'
    classHead += '        self.tableList = {}\n'
    importBody = ''
    initBody = '    def initTable(self):\n'
    funcBodyList = []
    for file in fileList:
        importBody += 'from Common.Table.Table_' + file + ' import *\n'
        initBody += '        self.init_' + file + '()\n'
        funcBody = '    def init_' + file + '(self):\n'
        funcBody += '        print(\'begin load table ' + file + '.txt\')\n'
        funcBody += '        file = open(\'./Config/' + file + '.txt\', \'r\', -1, \'utf-8\')\n'
        funcBody += '        lines = file.readlines()\n'
        funcBody += '        rowList = []\n'
        funcBody += '        index = 0\n'
        funcBody += '        for line in lines:\n'
        funcBody += '            index += 1\n'
        funcBody += '            if index <= 4:\n'
        funcBody += '                continue\n'
        funcBody += '            if len(line) == 0:\n'
        funcBody += '                continue\n'
        funcBody += '            table = Table_' + file + '()\n'
        funcBody += '            table.load(line)\n'
        funcBody += '            rowList.append(table)\n'
        funcBody += '        self.tableList[\'' + file + '\'] = rowList\n'
        funcBody += '        print(\'end load table ' + file + '.txt\')\n'
        funcBody += '\n'
        funcBody += '    def get' + file + 'ByIndex(self, index):\n'
        funcBody += '        rowList = self.tableList.get(\'' + file + '\')\n'
        funcBody += '        if rowList == None:\n'
        funcBody += '            return None\n'
        funcBody += '        if index < 0 or index >= len(rowList):\n'
        funcBody += '            return None\n'
        funcBody += '        return rowList[index]\n'
        funcBody += '\n'
        funcBody += '    def get' + file + 'ById(self, id):\n'
        funcBody += '        rowList = self.tableList.get(\'' + file + '\')\n'
        funcBody += '        if rowList == None:\n'
        funcBody += '            return None\n'
        funcBody += '        for row in rowList:\n'
        funcBody += '            if row.__ID__ == id:\n'
        funcBody += '                return row\n'
        funcBody += '        return None\n'
        funcBody += '\n'
        funcBody += '    def get' + file + 'Count(self):\n'
        funcBody += '        rowList = self.tableList.get(\'' + file + '\')\n'
        funcBody += '        if rowList == None:\n'
        funcBody += '            return 0\n'
        funcBody += '        return len(rowList)\n'
        funcBody += '\n'

        funcBodyList.append(funcBody)

    mgrStream.write(importBody)
    mgrStream.write(classHead)
    mgrStream.write(initBody)
    for func in funcBodyList:
        mgrStream.write(func)
    mgrStream.write('gTableManager = TableManager()')
    mgrStream.close()
    shutil.copy('py/TableManager.py', pyfileFolder)
