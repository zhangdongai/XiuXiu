#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import socket
import select
from Common.Common.Assert import *
from Common.Common.BaseDefine import *

class Socket:
    def __init__(self):
        self.socket = INVALID_ID
        self.addr = ()

    def __del__(self):
        print('Socket del')
        if self.socket != INVALID_ID:
            self.close()

    def create(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            ASSERT(self.socket != INVALID_ID, 'create socket failed')
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        except BaseException as err:
            print('except occur file=%s, function=%s, line=%s, err=%s' % 
                  (FILEFRAME().f_code.co_filename, 
                  FILEFRAME().f_code.co_name, 
                  FILEFRAME().f_lineno, 
                  err))

    def close(self):
        try:
            ASSERT(self.socket != INVALID_ID, 'invalid socket')
            self.socket.close()
            self.socket = INVALID_ID
        except BaseException as err:
            print('except occur file=%s, function=%s, line=%s, err=%s' % 
                  (FILEFRAME().f_code.co_filename, 
                  FILEFRAME().f_code.co_name, 
                  FILEFRAME().f_lineno, 
                  err))

    def bind(self, port):
        try:
            ASSERT(self.socket != INVALID_ID, 'invalid socket')
            self.socket.bind(('', port))
        except BaseException as err:
            print('except occur file=%s, function=%s, line=%s, err=%s' % 
                  (FILEFRAME().f_code.co_filename, 
                  FILEFRAME().f_code.co_name, 
                  FILEFRAME().f_lineno, 
                  err))

    def listen(self):
        try:
            ASSERT(self.socket != INVALID_ID, 'invalid socket')
            self.socket.listen(128)
        except BaseException as err:
            print('except occur file=%s, function=%s, line=%s, err=%s' % 
                  (FILEFRAME().f_code.co_filename, 
                  FILEFRAME().f_code.co_name, 
                  FILEFRAME().f_lineno, 
                  err))

    def accept(self):
        try:
            ASSERT(self.socket != INVALID_ID, 'invalid socket')
            return self.socket.accept()
        except BaseException as err:
            print('except occur file=%s, function=%s, line=%s, err=%s' % 
                  (FILEFRAME().f_code.co_filename, 
                  FILEFRAME().f_code.co_name, 
                  FILEFRAME().f_lineno, 
                  err))
            return INVALID_ID, ()

    def setblocking(self, flag):
        try:
            ASSERT(self.socket != INVALID_ID, 'invalid socket')
            self.socket.setblocking(flag)
        except BaseException as err:
            print('except occur file=%s, function=%s, line=%s, err=%s' % 
                  (FILEFRAME().f_code.co_filename, 
                  FILEFRAME().f_code.co_name, 
                  FILEFRAME().f_lineno, 
                  err))
            return INVALID_ID, ()

class ServerSocket:
    def __init__(self):
        self.Socket = Socket()
        self.Socket.create()
        self.Socket.bind(2143)
        self.Socket.listen()

    def __del__(self):
        print('ServerSocket del')
        del self.Socket

    def isHaveNewAccept(self):
        readlist, writelist, errlist = select.select([self.Socket.socket,], [], [], 0)
        if len(readlist) != 0:
            return True
        return False

    def accept(self, Socket):
        try:
            Socket.socket, Socket.addr = self.Socket.accept()
            print(str(Socket.socket.getpeername()), str(Socket.addr))
        except BaseException as err:
            ASSERT('Socket:accept, ' + str(err))

'''
class Player:
    def __init__(self):
        self.Socket = Socket()
'''
'''
player = Player()
serverSocket = ServerSocket()
serverSocket.accept(player.Socket)
print('external', str(player.Socket.socket.getpeername()), str(player.Socket.addr))
'''
'''
timebegin = time.time()
player = Player()
serverSocket = ServerSocket()
try:
    while True:
        if serverSocket.isHaveNewAccept():
            serverSocket.accept(player.Socket)
            print('external', str(player.Socket.socket.getpeername()), str(player.Socket.addr))
        timeend = time.time()
        if timeend - timebegin >= 1:
            print('elapsed one second, waiting new accept')
            timebegin = timeend
except BaseException as err:
    print('except occured')
    del serverSocket
'''
