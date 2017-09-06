#!usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import datetime
import time
import traceback
import pytz
import redis


def time():
    # 获取当前时间
    today = datetime.datetime.now(pytz.timezone("Asia/Shanghai")).today()
    # 获取下一天时间
    oneday = datetime.timedelta(days=1)
    tommorrow = today + oneday
    # 时间规整 去除时分秒 strftime 将时间-->字符串   strptime 将字符串-->时间
    tommorrowStr = tommorrow.strftime("%Y-%m-%d")  # str
    # tomorrowTime = time.strptime(tommorrow.strftime("%Y-%m-%d" + " 00:00:00"), "%Y-%m-%d %H:%M:%S")
    # tomorrowTimeSecond = time.mktime(tomorrowTime)

    # 获取当前时间
    today = datetime.datetime.now(pytz.timezone("Asia/Shanghai")).today()
    todayTime = time.strptime(today.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
    todayStamp = time.mktime(todayTime)


def redisConn():
    host = '10.250.100.20'
    port = 6379
    redisTimeout = 30000
    auth = "lenovo-1234"
    db = 14

    pool = redis.ConnectionPool(host=host, password=auth, db=db, port=port)
    r = redis.StrictRedis(connection_pool=pool)

    return r


try:

    r = redisConn()
    # r.set("早上", "你好 ！")
    # print r.get("早上")

    keys = r.keys("*")
    print len(keys)
    for key in keys:
        # if(key[3:13]=='2017-08-11'):

            print str(key)
        # r.delete(key)

except:
    print traceback.format_exc()
