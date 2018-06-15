#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import Common.Common.GeneralSet as GeneralSet
import TestExample.Test as Test
from Common.Common.ProcessDefine import *
 
def MainRun():
    Cmd()
    Test.TestGo()
    
def Cmd():
    if (len(sys.argv) != 3):
        print('error cmdargument count!')
        return

    cmd = sys.argv[1]
    if cmd != '-serverid':
        print('error cmdargument!')
        return
    cmdvalue = sys.argv[2]
    if not cmdvalue.isdigit():
        print('error cmdargument type!')
        return
    GeneralSet.gServerId = int(cmdvalue)
    print(GeneralSet.gServerId)
