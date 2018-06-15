#!/usr/bin/python
# -*- coding: utf-8 -*-

import pycurl
import io
from io import StringIO
import time
from threading import Thread

'''
1.txt文件内容为12345，通过pycurl取出的数据为b'12345\n'，是2进制的数据，无法直接通过StringIO.write写入，会报错pycurl.error: (23, 'Failed writing body
所以通过str()函数将返回数据转换成字符串写入
'''
def bufWrite(retBuf):
    buf = StringIO()
    '''http返回的是二进制的字符串，需要转换一下'''
    '''将字符串转换成2进制字符串的函数为str.encode(s)，详见下面的测试代码'''
    retBuf = bytes.decode(retBuf)
    buf.write(retBuf)
    print('return value', retBuf, buf.getvalue())

def httpRequest():
    curl = pycurl.Curl()
    timebegin = time.time()
    curl.setopt(pycurl.URL, 'http://123.57.58.164:8008/php/1.txt')
    curl.setopt(pycurl.WRITEFUNCTION, bufWrite)
    curl.perform()
    print('Httpcode', curl.getinfo(curl.HTTP_CODE))
    print('time elapsed', time.time() - timebegin)
    #print('return value', buf.getvalue())
    #buf.close()
    curl.close()


#httpRequest()

'''
#测试代码，2进制字符串和普通字符串的互相转换
bstr = b'str'
print(bstr)
sstr = 'str'
print(sstr)
ssstr = str.encode(sstr)#普通字符串转换成2进制字符串
print(ssstr)
bbstr = bytes.decode(bstr)#2进制字符串转换成普通字符串
print(bbstr)
'''

class SingleThreadHttp:
    def __init__(self):
        self.curl = pycurl.Curl()

    def __del__(self):
        self.curl.close()

    def httpResponse(self, retBuf):
        #print(retBuf)
        pass

    def httpRequest(self):
        self.curl.setopt(pycurl.URL, 'http://123.57.58.164:8008/php/1.txt')
        self.curl.setopt(pycurl.WRITEFUNCTION, self.httpResponse)
        self.curl.perform()

    def threadStart(self):
        print('threadstart')
        for i in range(1000):
            self.httpRequest()

    def threadCreate(self):
        thread = Thread(target = self.threadStart)
        timebegin = time.time()
        print('thread start, time=', timebegin)
        thread.start()
        thread.join()
        timeend = time.time()
        print('thread finish, time=', timeend)
        print('time elapsed=', timeend - timebegin)
#singleThread = SingleThreadHttp()
#singleThread.threadCreate()

class MutliThreadHttp:
    def __init__(self):
        self.curlList = []
        for i in range(3):
            self.curlList.append(pycurl.Curl())

    def __del__(self):
        self.curl.close()

    def httpResponse(self, retBuf):
        #print(retBuf)
        pass

    def httpRequest(self, index):
        self.curlList[index].setopt(pycurl.URL, 'http://123.57.58.164:8008/php/1.txt')
        self.curlList[index].setopt(pycurl.WRITEFUNCTION, self.httpResponse)
        self.curlList[index].perform()

    def threadStart(self, index):
        print('threadstart', index)
        for i in range(333):
            self.httpRequest(index)

    def threadCreate(self):
        threadList = []
        timebegin = time.time()
        for i in range(3):
            thread = Thread(target = self.threadStart, args = (i,))
            threadList.append(thread)
            thread.start()        
        print('thread start, time=', timebegin)
        for i in range(3):
            threadList[i].join()
        timeend = time.time()
        print('thread finish, time=', timeend)
        print('time elapsed=', timeend - timebegin)
mutliThread = MutliThreadHttp()
mutliThread.threadCreate()
