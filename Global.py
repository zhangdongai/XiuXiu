#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
本文件会导入在C++中需要引用到python文件
该文件在C++初始化程序时即导入，省略程序过程中再次导入模块
'''
import sys
import os
import time

#导入MainModule
from MainModule import *
