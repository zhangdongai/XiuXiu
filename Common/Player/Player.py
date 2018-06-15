#!/usr/bin/python
# -*- coding: utf-8 -*-


from Common.NetWork.SocketStream import *
import Common.Player.PlayerDefine as PlayerDefine
from Common.NetWork.Packet.PacketFactory import *
from Obj.Obj_Login import *
from Obj.Obj_User import *
import struct
from Log.Log import *
from Common.Common.Assert import *
from Common.Common.XorCrypto import *
from Common.NetWork.Packet.CG_CONNECTED_HEARTBEAT_PAK import *
from Common.NetWork.Packet.GC_CONNECTED_HEARTBEAT_PAK import *
from Common.Common.Config import *

HANDLE_PACKET_COUNT_PERTICK = 12    #每次心跳处理消息包个数
class Player:
    def __init__(self):
        self.Socket = Socket()
        PlayerDefine.PLAYER_ID_GENERATE += 1
        self.Id = PlayerDefine.PLAYER_ID_GENERATE
        self.status = PlayerDefine.PLAYERSTATUS_EMPTY
        #定义消息包收发的对象
        self.SocketInputStream = SocketInputStream(self.Socket)
        self.SocketOutputStream = SocketOutputStream(self.Socket)

        #健康度，客户端和服务器通讯会改变，达到一定阀值后断开连接
        self.healthLevel = 0

        #定义服务器登录Obj玩家对象
        self.ObjLogin = Obj_Login(self)
        self.ObjUser = Obj_User(self)

        # 消息包的处理函数在这儿定义
        # Obj_Login的消息包处理函数定义在这儿
        self.Handler = {PACKET_CG_LOGIN: self.ObjLogin.HandleLogin,
                        PACKET_CG_PING: self.ObjLogin.HandlePing,
                        PACKET_CG_REQ_RANDOMNAME: self.ObjLogin.HandleRandomName,
                        PACKET_CG_CREATEROLE: self.ObjLogin.HandleCreateRole,
                        PACKET_CG_CONNECTED_HEARTBEAT: self.HandleConnectHeartBeat,
                        }

    def __del__(self):
        print('Player del %d' % self.Id)
        Log('Player', 'player del id=%d', self.Id)
        del self.Socket

    def die(self):
        try:
            self.Socket.close()
        except BaseException as err:
            ASSERT(False, 'Player:die, ' + str(err))

    def getId(self):
        return self.Id

    def setStatus(self, status):
        self.status = status

    def getStatus(self):
        return self.status

    def ProcessInput(self):
        try:
            self.SocketInputStream.Fill()
            if len(self.SocketInputStream.InputStream) == 0:
                #接收到空消息，表示连接断开
                #客户端重启，socket失效时走这块
                return  False
            print('receive data %s' % self.SocketInputStream.InputStream)
            Log('Player', 'player id=%d receive data %s', self.Id, self.SocketInputStream.InputStream)
            return True
        except BaseException as err:
            ASSERT('Player:ProcessInput, ' + str(err))
            return False
        return False

    def ProcessOutput(self):
        try:
            self.SocketOutputStream.Flush()
            return True
        except BaseException as err:
            ASSERT(False, 'Player:ProcessOutput, ' + str(err))
            return False
        return False

    def ProcessCommand(self):
        try:
            for i in range(HANDLE_PACKET_COUNT_PERTICK):
                if len(self.SocketInputStream) == 0:
                    break
                #取出消息头
                packetHead = self.SocketInputStream.GetHead()
                if (len(packetHead) != PACKET_HEAD_SIZE):
                    #消息包头过小，数据不完整，跳过
                    break
                print('packetHead = ', packetHead)
                #消息大小占用4个字节
                #消息包大小时消息数据大小和消息头大小的和
                packetSize = packetHead[0:4]
                #将消息大小数据转换成int类型
                packetSizeNum = struct.unpack('i', packetSize)[0]
                print('packetSize = ', packetSizeNum)
                if (len(self.SocketInputStream) < packetSizeNum):
                    #消息没有接收全
                    break
                #消息ID占用2个字节
                packetId = packetHead[4:PACKET_HEAD_SIZE]
                packetId = struct.unpack('h', packetId)[0]
                print('packetId = ', packetId)
                #欲取出的消息包大小是packetSizeNum，[a, b]取数据时是不包含b的
                packetStream = self.SocketInputStream.Read(packetSizeNum)
                print('packetStream = ', packetStream)
                if self.IsCryptoPacket(packetId):
                    #str类型数据先转换成bytes，返回值为bytearray，需要转换回str
                    packetStream = XorDecrypt(packetStream)
                print('packetStream = ', packetStream)
                print('packet Create begin, Id = ', packetId)
                packet = gPacketFactoryManager.CreatePacket(packetId)
                #消息包不够！暂时先这样，别崩溃啊！
                #if packet == None:
                #    continue
                ASSERT(packet != None, 'create packet failed, packetid=%d' % packetId)
                print('packet Create finish, Id = ', packet.GetPacketId())
                #从数据流中反序列化出消息包对象
                packet.PacketData.ParseFromString(packetStream)
                #调用消息包处理函数
                self.Execute(packetId, packet)
            return True
        except BaseException as err:
            ASSERT(False, 'Player:ProcessCommand, ' + str(err))
            return False
        return False

    def ProcessConnection(self):
        try:
            pak = GC_CONNECTED_HEARTBEAT_PAK()
            pak.PacketData.serveransitime = int(time.time())
            self.SendPacket(pak)

            self.healthLevel -= 1
            #ProcessConnectionHealthLimit=30#心跳踢人设置
            return abs(self.healthLevel) < gGameConfig.connectHealthLimit
        except BaseException as err:
            ASSERT(False, 'Player:ProcessConnection, ' + str(err))

    def SendPacket(self, packet):
        try:
            packetSize = packet.GetPacketSize()
            buf = struct.pack('i', packetSize + PACKET_HEAD_SIZE)#大小是消息头和消息包体大小的和
            self.SocketOutputStream.Write(buf[::-1])#字符串需要反转一下，涉及到小端读取和大端读取
            packetId = packet.GetPacketId()
            buf = struct.pack('h', packetId)
            self.SocketOutputStream.Write(buf[::-1])#字符串需要反转一下，涉及到小端读取和大端读取
            buf = packet.PacketData.SerializeToString()
            print('SendPacket%d, %', (packetId, buf))
            if self.IsCryptoPacket(packetId):
                buf = XorEncrypt(buf)
            print('SendPacket%d, %s', (packetId, buf))
            self.SocketOutputStream.Write(buf)#消息包体不需要反转
        except BaseException as err:
            ASSERT(False, 'Player:SendPacket, ' + str(err))

    def Execute(self, packetId, packet):
        try:
            self.Handler[packetId](packet)
        except BaseException as err:
            ASSERT(False, 'Player:Execute, ' + str(err))

    def IsCryptoPacket(self, packetId):
        return False if packetId == PACKET_CG_LOGIN or \
                        packetId == PACKET_GC_LOGIN_RET or \
                        packetId == PACKET_CG_CONNECTED_HEARTBEAT or \
                        packetId == PACKET_GC_CONNECTED_HEARTBEAT \
                else True

    def HandleConnectHeartBeat(self, packet):
        self.healthLevel += 1