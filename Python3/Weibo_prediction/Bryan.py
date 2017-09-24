# -*- coding: utf-8 -*-
# coding:utf-8
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
'''

暴力破解
'''
import pandas as pd
import numpy as np
'''
导入训练数据
添加每个dataframe的列名称
'''
data_train = pd.read_table('D:\\www\\data\\Weibo Data\\Weibo Data\\weibo_train_data(new)\\weibo_train_data.txt',
                           sep="\t",
                           header=None, encoding='utf-8')
# header=None:没有每列的column name，可以自己设定
# encoding='gb2312':其他编码中文显示错误
# delim_whitespace=True:用空格来分隔每行的数据
# index_col=0:设置第1列数据作为index
# data.head(1)
# data.info()
header = ['userId', 'weiboId', 'datetime', 'forward_count', 'comment_count', 'like_count', 'content']
data_train.columns = header
'''
导入去重后的 userId数据
'''

user_train = pd.read_table('D:\\www\\data\\Weibo Data\\Weibo Data\\weibo_train_data(new)\\userId.txt',
                           header=None, encoding='utf-8')
user_train.columns = ['userId']
user_unique_dict =set( user_train.values)

'''
导入训练数据
添加每个dataframe的列名称
'''
data_test = pd.read_table('D:\\www\\data\\Weibo Data\\Weibo Data\\weibo_predict_data(new)\\weibo_predict_data.txt',
                          sep="\t",
                          header=None, encoding='utf-8')
data_test.columns = ['userId', 'weiboId', 'datetime','content']

'''
将训练数据中相同用户的（F,C,L）数据聚合
Map（key= userId,value=[ [F,C,L],
                         [F,C,L],
                        ]
'''
# user_dict={}
# keyIndex = 0
# flcSlice = slice(3,6)
# for i in range(data_train.size):
#     key = data_train.ix[i][keyIndex]
#     value = data_train.ix[i][flcSlice].values
#     if key not in user_dict.keys():
#         user_dict[key] = [value]
#     else:
#         user_dict[key].append(value)


# groupbyall = data_train.groupby(['userId','forward_count','comment_count','like_count'])
# groupbyall.size()
# for i in range(data_train.size):
#     key = data_train.ix[i][keyIndex]
#     value = data_train.ix[i][flcSlice].values
#     if key not in user_dict.keys():
#         user_dict[key] = [value]
#     else:
#         user_dict[key].append(value)
#
# print(len(user_dict))


def get_best_set(user_unique_dict,user_dict):
    best_set ={}
    best_f = 0
    best_c = 0
    best_l = 0
    max_precision = 0
    for userId in user_unique_dict:
        count_lists = user_dict[userId]
        print(len(user_dict[userId]))
        count_set = set(count_lists)
        # precision_sum

        for unique in count_set:
            fp = unique[0]
            cp = unique[1]
            lp = unique[2]
            sum_denom = 0
            sum_number = 0
            for list in count_lists:

                fr = list[0]
                cr = list[1]
                lr = list[2]
                df = np.abs(fp - fr) / (fr + 5)
                dc = np.abs(cp - cr) / (cr + 3)
                dl = np.abs(lp - lr) / (lr + 3)
                precision_i = 1 - 0.5 * df - 0.25 * dc - 0.25 * dl

                count_i = fr + cr + lr
                if count_i > 100:
                    count_i = 100

                sum_denom += count_i + 1
                sum_number += (count_i + 1) * sgn(precision_i - 0.8)

            precision = sum_number / sum_denom
            if (precision > max_precision):
                best_f = fp
                best_c = cp
                best_l = lp
                max_precision = precision
            best_set[unique]=(best_f, best_c, best_l)

    return best_set



def fit(userId,user_dict):
    best_set ={}
    best_f = 0
    best_c = 0
    best_l = 0
    max_precision = 0
    count_lists = user_dict[userId]
    print(len(user_dict[userId]))
    count_set = set(count_lists)
    # precision_sum

    for unique in count_set:
        fp = unique[0]
        cp = unique[1]
        lp = unique[2]
        sum_denom = 0
        sum_number = 0
        for list in count_lists:

            fr = list[0]
            cr = list[1]
            lr = list[2]
            df = np.abs(fp - fr) / (fr + 5)
            dc = np.abs(cp - cr) / (cr + 3)
            dl = np.abs(lp - lr) / (lr + 3)
            precision_i = 1 - 0.5 * df - 0.25 * dc - 0.25 * dl

            count_i = fr + cr + lr
            if count_i > 100:
                count_i = 100

            sum_denom += count_i + 1
            sum_number += (count_i + 1) * sgn(precision_i - 0.8)

        precision = sum_number / sum_denom
        if (precision > max_precision):
            best_f = fp
            best_c = cp
            best_l = lp
            max_precision = precision
        best_set[unique]=(best_f, best_c, best_l)

        return best_set



def sgn(value):
    if value > 0:
        return 1
    else:
        return 0

def get_user_dict ():
    user_dict={}
    keyIndex = 0
    flcSlice = slice(3,6)
    for i in range(data_train.size):
        key = data_train.ix[i][keyIndex]
        value = data_train.ix[i][flcSlice].values
        if key not in user_dict.keys():
            user_dict[key] = [value]
            # user_dict[key].append(value)
        else:
            user_dict[key].append(value)
    return user_dict
user_dict = get_user_dict()
def get_user_predict  ():
    best_set = fit()
    data_test.drop(['datetime','content'], axis=1, inplace=True)
    data_test['forward_count', 'comment_count', 'like_count']=(0,0,0)
    for i in range(data_test.size):
        userId = data_test.ix[i][0]
        min = data_test.ix[i][1]
        best_f, best_c, best_l = fit(userId,user_dict)
        data_test.ix[i]['forward_count','comment_count','like_count'].values =[best_f, best_c, best_l]

    return data_test
data_test_result = get_user_predict()
data_test_result.to_csv(r'D:\\www\\data\\Weibo Data\\Weibo Data\\weibo_predict_data(new)\\weibo_predict_data(new).txt',sep='\t', index=False, header=False)
data_test_result.to_excel(r'D:\\www\\data\\Weibo Data\\Weibo Data\\weibo_predict_data(new)\\weibo_predict_data(new).xls',sheet_name='Sheet1')


