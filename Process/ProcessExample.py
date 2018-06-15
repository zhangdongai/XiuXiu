#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
演示了创建多个子进程并和主进程间通讯的功能

示例代码中创建了5个子进程，进程入口为processentry函数
同时创建5个Queue，用于和子进程互相通讯

子进程启动后，往queue中塞入一条数据，并开始循环获取来自主进程的消息

主进程往各个queue中塞入stop消息，等待子进程获取

子进程获取到stop消息后，循环结束，入口函数推出

主进程调用子进程的join函数等待子进程结束，子进程只有在收到stop消息后才会退出循环，并完全退出

主进程最后打印出子进程塞入queue中的数据

！！！问题：
进程间通过queue通讯并不是特别好的方法，因为仅仅在这个简单的示例中就遇到了无法解决的问题
如果主进程和子进程互相通讯，即都需要put和get。get是从queue中直接弹出一个消息，所以如果主进程塞入消息后
子进程没有及时get，而主进程首先get，那么主进程将get到自己put的消息，消息将丢失，并且子进程无法获得该消息

如上问题，暂时解决不了
怎么验证上面描述的问题呢：
将下面的示例代码：
for pro in proList:
        pro.join()
移动到time.sleep(5)之前
运行可发现，子进程无法终止，表示主进程put的stop消息被主进程get到
'''

import os
import time
from multiprocessing import Process, Queue

def processentry(queue, args):
    print('processentry' + str(args))
    queue.put(str('process' + str(args)))
    #queue.put('stop')
    #queue.put(str('process again' + str(args)))
    
    while True:
        if queue.get() == 'stop':
            print('stop get' + str(args))
            break
    
if __name__ == '__main__':
    queueList = []
    proList = []
    for i in range(5):
        queue = Queue()
        queueList.append(queue)
        pro = Process(target = processentry, args=(queue, i,))
        pro.start()
        proList.append(pro)

    print('mainprocess')

    for  i in range(5):
        queueList[i].put('stop')

    for pro in proList:
        pro.join()
        
    for  i in range(5):
        for j in range(queueList[i].qsize()):
            print(queueList[i].get())

    
    time.sleep(5)

