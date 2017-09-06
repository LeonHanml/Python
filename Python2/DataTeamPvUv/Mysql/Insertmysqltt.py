#!usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import datetime
import time
import traceback
import pytz

# for i in range(7,-1,-1):
day1 = [0, 1]
day2 = [-1, -2, -3, -4, -5, -6, -7]
day3 = [-2, -1, 0, 1, 2]
day = [1, 2]
try:
    host = '10.250.100.23'
    port = 3306
    user = 'storm'
    passwd = 'hiWMAtvo8kYkxbjU'
    db = 'realtime'
    conn = MySQLdb.Connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
    cursor = conn.cursor()
except:
    print traceback.format_exc()
tableNameArray = ('shopflow_tt1_pvuv', "shopflow_tt2_pvuv")
for tableName in tableNameArray:
    for i in day:
        # 获取当前时间
        today = datetime.datetime.now(pytz.timezone("Asia/Shanghai")).today()
        # 获取下一天时间
        oneday = datetime.timedelta(days=+i)  # -i
        tommorrow = today + oneday
        # 时间规整 去除时分秒 strftime 将时间-->字符串   strptime 将字符串-->时间
        print tommorrow.strftime("%Y-%m-%d")  # str
        tomorrowTime = time.strptime(tommorrow.strftime("%Y-%m-%d" + " 00:00:00"), "%Y-%m-%d %H:%M:%S")
        tomorrowTimeSecond = time.mktime(tomorrowTime)

        try:

            # if tableName == "shopflow_tt2_pvuv":
            for i in range(60 * 24):
                insertTimeSecond = tomorrowTimeSecond
                insertTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(tomorrowTimeSecond))

                sql = 'insert into %s  (min,date) values ("%s","%s" )' % (tableName, insertTime, insertTime[0:10])

                cursor.execute(sql)
                #
                if (i % 500 == 0):
                    print sql

                tomorrowTimeSecond = tomorrowTimeSecond + 60

        except:
            print traceback.format_exc()
