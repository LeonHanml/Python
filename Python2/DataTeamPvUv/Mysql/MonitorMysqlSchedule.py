#!usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import datetime
import time
import traceback
import pytz

# 获取当前时间
today = datetime.datetime.now(pytz.timezone("Asia/Shanghai")).today()
# 获取下一天时间
oneday = datetime.timedelta(days=+1)
tommorrow = today + oneday
# 时间规整 去除时分秒 strftime 将时间-->字符串   strptime 将字符串-->时间
tommorrowStr = tommorrow.strftime("%Y-%m-%d")  # str
# tomorrowTime = time.strptime(tommorrow.strftime("%Y-%m-%d" + " 00:00:00"), "%Y-%m-%d %H:%M:%S")
# tomorrowTimeSecond = time.mktime(tomorrowTime)

# 获取当前时间
today = datetime.datetime.now(pytz.timezone("Asia/Shanghai")).today()
todayTime = time.strptime(today.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
todayStamp = time.mktime(todayTime)

# 验证两个内容
# 1、下一天的数据是否提前插入
# 2、数据是否更新到当前时间
try:

    host = '10.250.100.23'
    port = 3306
    user = 'storm'
    passwd = 'hiWMAtvo8kYkxbjU'
    db = 'realtime'
    conn = MySQLdb.Connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
    cursor = conn.cursor()
    sqlNewestTime = 'select min from shopflow_total_pvuv where pv>0 order by id desc limit 1'
    # sqlNewestTime = 'select min,pv from shopflow_total_basic_bymin where pv>0 order by id desc limit 1'
    cursor.execute(sqlNewestTime)
    logTime = 0
    for tmp in cursor:
        logTime = tmp[0]
    logTimeStamp = time.mktime(time.strptime(logTime, "%Y-%m-%d %H:%M:%S"))

    # print (todayStamp - logTimeStamp)
    if ((todayStamp - logTimeStamp) > 60 * 5):
        print '当前时间 ：%s' % today
        print '日志时间 ：%s' % str(logTime)
        print '间隔相差：%d 秒' % (todayStamp - logTimeStamp)
    else:
        print '监测正常，时间：%s' % today

    # 定时 早上10点 检测后一天数据
    # print int(today.hour)
    # print int(today.minute)

    hour = int(today.hour)
    if (hour == 10):
        sqlNextDay = 'select date from shopflow_total_pvuv order by id desc limit 1'
        cursor.execute(sqlNextDay)
        date = ""
        for tmp in cursor:
            date = tmp[0]
            print date

        # print  tommorrowStr
        if (tommorrowStr is not date):
            print '未插入下一天基础数据 %s'%tommorrowStr

except:
    print traceback.format_exc()
