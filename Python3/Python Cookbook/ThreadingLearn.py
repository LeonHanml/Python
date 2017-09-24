#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding:utf-8
from time import  ctime
import threading
def function1():
    pass
def function2():
    pass
threads = []
t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2())
threads.append(t1)
threads.append(t2)
if __name__ =='__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()

    t.join()
    print ("all over %s" %ctime())

import threading
import time

exitFlag = 0

class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print ("Starting " + self.name)
        print_time(self.name, self.counter, 5)
        print ("Exiting " + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threading.Thread.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启线程
thread1.start()
thread2.start()

print ("Exiting Main Thread")