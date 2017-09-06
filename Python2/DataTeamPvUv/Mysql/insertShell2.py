#!usr/bin/python
# -*- coding: utf-8 -*-
import os

SHELLPATH = "/home/kafkaetl/shopflow_pvuv"
LOGPATH = "/home/kafkaetl/log"
# print os.path.exists(LOGPATH)
if os.path.exists(LOGPATH) == False:
    os.makedirs(LOGPATH)

os.chdir(SHELLPATH)

resultFlag =os.system("nohup /usr/local/bin/python /home/kafkaetl/shopflow_pvuv/InsertSchedule.py 2>&1 | /usr/local/sbin/cronolog /home/kafkaetl/log/InsertPvuvBeforeOneday.log >> /dev/null &")


if resultFlag!=0:

    print "Insert Next Day failed"
