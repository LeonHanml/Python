#!usr/bin/python
# -*- coding: utf-8 -*-
import os

SHELLPATH = "/home/hanliang3/node/crontabShell"
LOGPATH = "/home/hanliang3/node/crontabShell/log"
# print os.path.exists(LOGPATH)
if os.path.exists(LOGPATH) == False:
    os.makedirs(LOGPATH)

os.chdir(SHELLPATH)

resultFlag =os.system("nohup /usr/local/bin/python /home/hanliang3/node/crontabShell/MonitorMysqlSchedule.py >> /home/hanliang3/node/crontabShell/log/InsertPvuvBeforeOneday.log  2>&1  &")

print resultFlag
if resultFlag!=0:

    print "Insert Next Day failed"
