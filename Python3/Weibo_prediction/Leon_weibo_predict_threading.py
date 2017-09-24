import pandas as pd
import numpy as np
from time import  ctime
import threading
import time
data_test = pd.read_table('D:\\www\\data\\Weibo Data\\Weibo Data\\weibo_predict_data(new)\\weibo_predict_data.txt',
                          sep="\t",
                          header=None, encoding='utf-8')
data_test.columns = ['uid', 'mid', 'time','content']

data_test.drop(['time','content'], axis=1, inplace=True)
data_test['forward_count']=0
data_test['comment_count']=0
data_test['like_count']=0
print(data_test.columns)
data_best_predict = pd.read_table('D:\\www\\data\\Weibo Data\\Weibo Data\\weibo_train_data(new)\\best_uid_fcl_set_0.txt',
                                  sep=" ",
                                  header=None, encoding='utf-8')
data_best_predict.columns = ['uid', 'f', 'c','l',"p"]
data_best_predict_dict ={}


keyIndex = 0
flcSlice = slice(1,4)


for i in range(len(data_best_predict)):
    key = data_best_predict.ix[i][keyIndex]
    value = data_best_predict.ix[i][flcSlice].values
    if key not in data_best_predict_dict.keys():
        data_best_predict_dict[key] = [value]
        # user_dict[key].append(value)
    else:
        data_best_predict_dict[key].append(value)

def get_result(threadName,slices,file_num):

    best_file = open("D:\\www\data\\Weibo Data\\Weibo Data\\weibo_train_data(new)\\best_uid_fcl_predict_"+str(3)+".txt","a",encoding="utf8")
    # data_test1 = data_test[:50000]


    for i in range(len(data_test[slices])):
        i += slices.start
        # print(threadName+"threadName:i"+str(i))
        uid = data_test.ix[i][0]
        min = data_test.ix[i][1]
        if uid not in data_best_predict_dict.keys():
            best_file.write(uid+"\t"+min+"\t"+str(0)+","+str(0)+","+str(0)+"\n")

        else:
            best_file.write(uid+"\t"+min+"\t"+str(data_best_predict_dict[uid][0][0])+","+str( data_best_predict_dict[uid][0][1])+","+str(data_best_predict_dict[uid][0][2])+"\n")
    best_file.flush()
    best_file.close()

exitFlag = 0
class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, name, slices,file_num):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.slices= slices
        self.file_num = file_num
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数

        print ("Starting " + self.name)
        print ("%s: %s" % (self.name, time.ctime(time.time())))


        get_result(self.name,self.slices,self.file_num)
        print ("%s: %s" % (self.name, time.ctime(time.time())))
        print ("Exiting " + self.name)


# 创建新线程

thread1 = myThread(1, "Thread-1",slice(0,500), 1)
thread2 = myThread(2, "Thread-2",slice(500,1000), 2)

# 开启线程
thread1.start()
thread2.start()

print ("Exiting Main Thread")
