#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.Common.GeneralSet import *
from Common.Common.Assert import *

#按照int存储，256个int，64位平台上每个int占用8个字节，32位平台下int占用4个字节
#但是目前统一设置为4个int，最大值为4294967295（默认为无符号），python下8为int的最大值为9223372036854775807
MAX_CHAR_COMMONDATA_NUM = (256 * 4) if X_PLATFROM == '64bit' else (256 * 4)
#MAX_CHAR_COMMONDATA_NUM = (4 * 4) if X_PLATFROM == '64bit' else (4 * 4)
#按照位存储，7个int，64位平台上每个int占用8个字节，32平台上int占用4个字节。每个字节8位
#但是每个字节的最高位必须为0，所以不能使用！
#但是目前统一设置为4个int，即每个字节的最大值为127
#一共有4*7*8=224位，有28位不能使用，剩余196位可以使用
MAX_CHAR_COMMONFLAG_NUM = (7 * 4) if X_PLATFROM == '64bit' else (7 * 4)
#MAX_CHAR_COMMONFLAG_NUM = (2 * 4) if X_PLATFROM == '64bit' else (2 * 4)

#CommonFlag标记定义
CF_FIRSTLOGIN = 0   #第一次登陆
CF_MAX = 224    #最大位数，必须小于这个数

#CommonData标记顶级
CD_FIRST = 0
CD_MAX = 256    #最大个数，必须小于这个数




#参数必须为一个bytearray或者bytes，bytearray和bytes按照字节进行存储，每个索引存储一个字节
#字节print出来表示为\x00，转换为16进制为0x0。
#数据库存储必须按照字节进行存储，因为python的string的不定长特性，bytes和bytearray的特殊表示方法，
#所以决定将每个字节转换成两个字节存入数据库：
#例如：字节\x00，16进制为0x0，用两个字节表示为00
#例如：字节\xc0，16进制为0xc0，用两个字节表示为c0
def Bytes2DBString(bytea):
    if len(bytea) == 0:
        return ''
    retValue = ''
    for i in range(len(bytea)):
        hexbyteValue = hex(bytea[i])
        #16进制为0x0的情况
        if len(hexbyteValue) == 3:
            retValue += '0'
            retValue += hexbyteValue[2]
        #16进制为0xc0的情况
        elif len(hexbyteValue) == 4:
            retValue += hexbyteValue[2]
            retValue += hexbyteValue[3]
    return retValue

def DBString2Bytes(dbstring):
    strLen = len(dbstring)
    ASSERT(strLen % 2 == 0, 'dbstring length can not be dived by 2')
    if len(dbstring) == 0:
        return bytearray()
    retbytes = bytearray(int(strLen / 2))
    for i in range(len(dbstring)):
        byte1 = None
        byte2 = None
        construct = False
        if i % 2 == 0:
            byte1 = dbstring[i]
            byte2 = dbstring[i + 1]
            construct = True

        if construct:
            hexs = ''
            hexs += byte1
            hexs += byte2
            dec = int(hexs, 16)
            retbytes[int(i / 2)] = dec
    return retbytes

########ObjType定义########
OBJTYPE_EMPTY = 0
OBJTYPE_USER = 1
OBJTYPE_NPC = 2
OBJTYPE_MAX = 3 #增加的新类型必须在上面，而且OBJTYPE_MAX也要累加哦

########SceneType定义########
SCENETYPE_MAIN = 0
SCENETYPE_WILD = 1
SCENETYPE_COPY = 2


PLAYERGUIDNEWSCENE = 12 #新手引导场景