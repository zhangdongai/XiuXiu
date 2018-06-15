#!/usr/bin/python
# -*- coding: utf-8 -*-
import _random
def change(arg):
    arg.data = 10

class Test:
    def __init__(self):
        Test.data = 5
        self.ttt = 1

    def normal(self):
        pass

    @classmethod
    def ttt(cls):
        pass

    @staticmethod
    def aaa():
        pass

    @classmethod
    def add(self):
        Test.data += 1

    @staticmethod
    def printdata():
        print(Test.data)

test = Test()
test2 = Test()
test.add()
Test.add()
Test.printdata()
Test.printdata()
test.printdata()
m = {}
m['1'] = test
print(m['1'])
print(test)
test.ttt = 24
print(m['1'].ttt)
m1 = m['1']
del m['1']
print(m1)


def test():
    print('call test')
    raise Exception('test function throw except')


def test2():
    print('call test2')
    try:
        test()
    except BaseException as err:
        print('test2 catch except, ', err)
        raise err
    print('test2 end')

def test3():
    print('call test3')
    try:
        test2()
    except BaseException as err:
        exp = 'test3 catch except, ' + str(err)
        print(exp)
    print('test3 end')

test3()

def TestGo(a, b, c):
    print('i am function testGo, param is ', a, b, c)
    #ran = _random.Random()
    #ran.random()
print('abcd')
TestGo(1,2,3)