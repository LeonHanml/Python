import pandas as pd
import numpy as np

import pickle

data_train =[]
with open(r"D:\\www\\data\\Weibo Data\\Weibo Data\\weibo_train_data(new)\\weibo_train_data.txt",'r',encoding='utf-8') as f:
    while(True):
        line = f.readline()
        if not line:
            break
            pass
        array = line.split("\t")
        data_train.append([array[0],array[3],array[4],array[5]])

data_train = pd.DataFrame(data_train,columns=['uid','forward_count','comment_count','like_count'],index=None)

def get_unique_uid_fcl_set():

    unique_uid_fcl_set ={}
    groupbyall = data_train.groupby(['uid','forward_count','comment_count','like_count'])
    items = groupbyall.size().items()
    for i in items:
        key = i[0][0]
        forward_count =int(i[0][1])
        comment_count = int(i[0][1])
        like_count = int(i[0][1])
        time = int(i[1])
        if key not  in unique_uid_fcl_set.keys():
            unique_uid_fcl_set[key]=[[forward_count,comment_count,like_count,time]]
        else:
            unique_uid_fcl_set[key].append([forward_count,comment_count,like_count,time])

    return unique_uid_fcl_set