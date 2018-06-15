#!/usr/bin/python
# -*- coding: utf-8 -*-

import mysql.connector
'''
conn = mysql.connector.connect(user='ServiceTech', password='U743g3asgvASAa',database='servicetechdb_1', host='123.57.58.164')
cur = conn.cursor(buffered=True)
retlist = cur.execute('call load_charlist(\'1017\')', multi=True)
for cur in retlist:
    if cur.with_rows:
        print(cur.fetchone())

retlist = cur.execute('call load_char_info(28428972647787008)', multi=True)
for cur in retlist:
    if cur.with_rows:
        print(cur.fetchone())
'''
from Common.Table.TableManager import *
from DB.DBConnector.DBConnectorInterface import *

dbConnectorInterface = DBConnectorInterface()
#serverConfig = gTableManager.getServerConfigListById(101)
dbConnectorInterface.connect('ServiceTech',
                             'U743g3asgvASAa',
                             'servicetechdb_1',
                             '123.57.58.164',
                                       3306)
dbConnectorInterface.setQueryComm('call load_charlist(\'1017\')')
dbConnectorInterface.execute()
for i in range(dbConnectorInterface.resultCount):
    dbConnectorInterface.fetch()
    print(dbConnectorInterface.fetchTuple)
dbConnectorInterface.connector.commit()


dbConnectorInterface.setQueryComm('call load_char_info(28428972647785472)')
dbConnectorInterface.execute()
for i in range(dbConnectorInterface.resultCount):
    dbConnectorInterface.fetch()
    print(dbConnectorInterface.fetchTuple)
