# -*- coding: utf-8 -*-

import sys
import os
import subprocess
import shutil
import re

PROJECT_FILE = '../../XiuXiu/Common/NetWork/Packet/'
#判断文件夹是否存在
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')
#Packet文件夹不存在则创建一个，存在的话先删除然后再创建一个
if not os.path.exists('./tmp/Packet'):
    pass
else:
    shutil.rmtree('./tmp/Packet')
os.makedirs('./tmp/Packet')


if os.path.exists('./tmp/PBMessage_pb2.py'):
    os.remove('./tmp/PBMessage_pb2.py')
ret = subprocess.getoutput('protoc -I=./ --python_out=./tmp/ PBMessage.proto')
print(ret)

print('begin copy PBMessage_pb2 file... ...')
shutil.copy('./tmp/PBMessage_pb2.py', PROJECT_FILE)
print('copy PBMessage_pb2 end ... ...')


PAKFILE_HEAD = '#!/usr/bin/python\n# -*- coding: utf-8 -*-\n\n'
file = open('PBMessage.proto', 'r')
content = file.read()
file.close()
cgList = re.findall(r'CG_\w+|GC_\w+', content, re.S)
cgCount = len(cgList)

for i in range(cgCount):
    cg = cgList[i]
    print(cg)
    print(type(cg))
    fileName = './tmp/Packet/' + cg + '_PAK.py'
    print(fileName)
    fileStream = open(fileName, 'w')
    fileStream.write(PAKFILE_HEAD)
    fileBody = 'from Common.NetWork.Packet.PacketDefine import *\n'
    fileBody += 'from Common.NetWork.Packet.PBMessage_pb2 import *\n\n'
    fileStream.write(fileBody)
    classHead = 'class ' + cg + '_PAK:\n'
    fileStream.write(classHead)
    classBody = '    def __init__(self):\n'
    classBody += '        self.PacketData = ' + cg + '()\n\n'
    classBody += '    def GetPacketId(self):\n'
    classBody += '        return PACKET_' + cg + '\n\n'
    classBody += '    def GetPacketSize(self):\n'
    classBody += '        return self.PacketData.ByteSize()\n\n\n'
    fileStream.write(classBody)
    classHead = 'class ' + cg + '_PAKFactory:\n'
    fileStream.write(classHead)
    classBody = '    def __init__(self):\n'
    classBody += '        pass\n\n'
    classBody += '    def GetPacketId(self):\n'
    classBody += '        return PACKET_' + cg + '\n\n'
    classBody += '    def CreatePacket(self):\n'
    classBody += '        return ' + cg + '_PAK()'
    fileStream.write(classBody)
    fileStream.close()
    shutil.copy(fileName, PROJECT_FILE)

fileName = './tmp/Packet/PacketFactory.py'
fileStream = open(fileName, 'w')
fileStream.write(PAKFILE_HEAD)
fileBody = ''
for i in range(cgCount):
    cg = cgList[i]
    fileBody += 'from Common.NetWork.Packet.' + cg + '_PAK import *\n'
fileBody += '\n'
fileBody += 'from Common.Common.Assert import *\n'
fileStream.write(fileBody)
classHead = 'class PacketFactoryManager:\n'
fileStream.write(classHead)
classBody = '    def __init__(self):\n'
classBody += '        self.FactoryList = [0] * PACKET_MAX\n\n'
classBody += '    def Init(self):\n'
for i in range(cgCount):
    cg = cgList[i]
    classBody += '        self.AddFactory(' + cg + '_PAKFactory())\n'
classBody += '\n'
classBody += '    def AddFactory(self, factory):\n'
classBody += '        self.FactoryList[factory.GetPacketId()] = factory\n\n'
classBody += '    def CreatePacket(self, packetId):\n'
classBody += '        try:\n'
classBody += '            ASSERT(packetId < PACKET_MAX, \'packetId is out of range\')\n'
classBody += '            return self.FactoryList[packetId].CreatePacket()\n'
classBody += '        except BaseException as err:\n'
classBody += '            ASSERT(False, \'PacketFactory:CreatePacket, \' + str(err))\n'
classBody += '            return None\n'
classBody += '        return None\n\n'
classBody += 'gPacketFactoryManager = PacketFactoryManager()'
fileStream.write(classBody)
fileStream.close()
shutil.copy(fileName, PROJECT_FILE)

fileName = './tmp/Packet/PacketDefine.py'
fileStream = open(fileName, 'w')
fileStream.write(PAKFILE_HEAD)
fileBody = 'PACKET_NULL = 0\n'
fileBody += 'PACKET_CG_LOGIN = 1\n'
fileBody += 'PACKET_GC_LOGIN_RET = 2\n'
index = 0
print('PacketDefine.py, count', cgCount)
temp_i = 0
for i in range(cgCount):
    cg = cgList[i]
    temp_i += 1
    if cg == 'CG_LOGIN' or cg == 'GC_LOGIN_RET':
        temp_i -= 1
        continue
    index = temp_i + 2
    print('PacketDefine.py, i=', i)
    print('PacketDefine.py, index=', index)
    fileBody += 'PACKET_' + cg + ' = ' + str(index) + '\n'
        
fileBody += 'PACKET_MAX = '
fileBody += str(index + 1)
fileStream.write(fileBody)
fileStream.close()
shutil.copy(fileName, PROJECT_FILE)

