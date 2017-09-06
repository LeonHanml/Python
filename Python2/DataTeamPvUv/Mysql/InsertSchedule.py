#!usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import datetime
import time
import traceback
import pytz
# for i in range(7,-1,-1):

# 获取当前时间
today = datetime.datetime.now(pytz.timezone("Asia/Shanghai")).today()
# 获取下一天时间
oneday = datetime.timedelta(days=+0)#-i
tommorrow = today + oneday
# 时间规整 去除时分秒 strftime 将时间-->字符串   strptime 将字符串-->时间
print tommorrow.strftime("%Y-%m-%d")  # str
tomorrowTime = time.strptime(tommorrow.strftime("%Y-%m-%d" + " 00:00:00"), "%Y-%m-%d %H:%M:%S")
tomorrowTimeSecond = time.mktime(tomorrowTime)
try:
    # db = MySQLdb.connect(“192.168.121.53”,”t1”,”test123”,”test” )
    host = '10.250.100.23'
    port = 3306
    user = 'storm'
    passwd = 'hiWMAtvo8kYkxbjU'
    db = 'realtime'
    conn = MySQLdb.Connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
    cursor = conn.cursor()

    for i in range(60 * 24):
        insertTimeSecond = tomorrowTimeSecond
        insertTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(tomorrowTimeSecond))

        sql = 'insert into shopflow_total_pvuv  (min,date) values ("%s","%s" )' % (insertTime, insertTime[0:10])
        sql2 = 'insert into shopflow_total_incre_pvuv  (min,date) values ("%s","%s")' % (insertTime, insertTime[0:10])
        sql3 = 'insert into shopflow_10000071_pvuv  (min,date) values ("%s","%s" )' % (insertTime, insertTime[0:10])
        cursor.execute(sql)
        cursor.execute(sql2)
        # cursor.execute(sql3)
        if (i % 500 == 0):
            print sql2

        tomorrowTimeSecond = tomorrowTimeSecond + 60

except:
    print traceback.format_exc()
