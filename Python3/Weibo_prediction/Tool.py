# -*- coding: utf-8 -*-
#coding:utf-8
# import matplotlib.pyplot as plt
# plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingRegressor
from sklearn import linear_model

# axis=0, 表示列。

# axis=1, 表示行。


import pandas as pd
class tools ():
    def get_data_train_dataframe(self):
        data_train =[]
        with open(r"D:\\www\\data\\Weibo Data\\Weibo Data\\weibo_train_data(new)\\weibo_train_data.txt",'r',encoding='utf-8') as f:
            while(True):
                line = f.readline()
                if not line:
                    break
                    pass
                array = line.split("\t")
                data_train.append([array[0],array[3],array[4],array[5]])


        # data_train = pd.read_table('D:\\www\\data\\Weibo Data\\Weibo Data\\weibo_train_data(new)\\weibo_train_data.txt',
        #                            sep="\t",
        #                            header=None, encoding='utf-8')
        # header = ['uid', 'mid', 'time', 'forward_count', 'comment_count', 'like_count', 'content']
        # data_train.columns = header




        # columns=['uid','forward_count','comment_count','like_count',"frequency"]

        data_train = pd.DataFrame(data_train,columns=['uid','forward_count','comment_count','like_count'],index=None)
        return data_train
