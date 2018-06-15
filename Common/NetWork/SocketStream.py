#!/usr/bin/python
# -*- coding: utf-8 -*-

from Common.NetWork.Socket import *
from Common.Common.Assert import *

MAX_SOCKET_BUFSIZE = (64 * 1024)
PACKET_HEAD_SIZE = (4 + 2)  #消息包头的字节数

class SocketInputStream:
    def __init__(self, socket):
        self.Socket = socket
        self.InputStream = ''

    def __len__(self):
        return len(self.InputStream)

    def Fill(self):
        try:
            self.InputStream = self.Socket.socket.recv(MAX_SOCKET_BUFSIZE)
        except BaseException as err:
            ASSERT(False, 'SocketStream:Fill, ' + str(err))

    def GetHead(self):
        packetHead = self.InputStream[0:PACKET_HEAD_SIZE]
        return packetHead

    def Read(self, packetSize):
        try:
            packetStream = self.InputStream[PACKET_HEAD_SIZE:packetSize]
            # 截取上一个消息包之后的数据，依次读取消息包数据
            self.InputStream = self.InputStream[packetSize:]
            return packetStream
        except BaseException as err:
            ASSERT(False, 'SocketStream:Read, '+ str(err))

class SocketOutputStream:
    def __init__(self, socket):
        self.Socket = socket
        self.OutputStream = b''

    def Write(self, buf):
        self.OutputStream += buf

    def Flush(self):
        try:
            if len(self.OutputStream) == 0:
                return
            self.Socket.socket.sendall(self.OutputStream)
            self.OutputStream = b''
        except BaseException as err:
            ASSERT(False, 'SocketStream:Flush, ' + str(err))
