#!usr/bin/python
# -*- coding: utf-8 -*-
import os

SHELLPATH = "/home/hanliang3/node/crontabShell"
LOGPATH = "/home/hanliang3/node/crontabShell/log"
# print os.path.exists(LOGPATH)
if os.path.exists(LOGPATH) == False:
    os.makedirs(LOGPATH)

os.chdir(SHELLPATH)

resultFlag =os.system("nohup /usr/local/bin/python /home/hanliang3/node/crontabShell/InsertSchedule.py 2>&1  /home/hanliang3/node/crontabShell/log/InsertPvuvBeforeOneday.log >> /dev/null &")

print resultFlag
if resultFlag!=0:

    print "Insert Next Day failed"
