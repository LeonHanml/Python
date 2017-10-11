import pandas as pd
import numpy as np
data_train = pd.read_table('D:\\www\\data\\Weibo Data\\Weibo Data\\weibo_train_data(new)\\weibo_train_data.txt',
                           sep="\t",
                           header=None, encoding='utf-8')
header = ['uid', 'mid', 'time', 'forward_count', 'comment_count', 'like_count', 'content']
data_train.columns = header

data_best_predict = pd.read_table('D:\\www\\data\\Weibo Data\\Weibo Data\\weibo_train_data(new)\\best_uid_fcl_set_0.txt',
                                  sep=" ",
                                  header=None, encoding='utf-8')
data_best_predict.columns = ['uid', 'f', 'c','l',"p"]

def get_unique_uid_fcl_set():
    unique_uid_fcl_set ={}
    groupbyall = data_train.groupby(['uid','forward_count','comment_count','like_count'])
    items = groupbyall.size().items()
    for i in items:
        key = i[0][0]
        if key not  in unique_uid_fcl_set.keys():
            unique_uid_fcl_set[key]=[[i[0][1],i[0][2],i[0][3],i[1]]]
        else:
            unique_uid_fcl_set[key].append([i[0][1],i[0][2],i[0][3],i[1]])
    return unique_uid_fcl_set
unique_uid_fcl_set = get_unique_uid_fcl_set()
def get_data_best_predict_dict():
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
    return data_best_predict_dict
data_best_predict_dict = get_data_best_predict_dict()
def sgn(value):
    if value > 0:
        return 1
    else:
        return 0
def get_precison():
    sum_denom = 0
    sum_number = 0
    for uid in unique_uid_fcl_set.keys():

        best = data_best_predict_dict[uid]
        fp = best[0][0]
        cp = best[0][1]
        lp = best[0][2]
        count_set = unique_uid_fcl_set[uid]
        for list in count_set:
            fr = list[0]
            cr = list[1]
            lr = list[2]
            time = list[3]
            df = np.abs(fp - fr) / (fr + 5.0)
            # if fp!=fr:
            #     print(fp, fr)
            dc = np.abs(cp - cr) / (cr + 3.0)
            dl = np.abs(lp - lr) / (lr + 3.0)
            precision_i = 1 - 0.5 * df - 0.25 * dc - 0.25 * dl

            count_i = fr + cr + lr
            if count_i > 100:
                count_i = 100

            sum_denom += (count_i + 1)*time

            sum_number += (count_i + 1) * sgn(precision_i - 0.8)*time

    precision = sum_number/sum_denom
    print(precision)
#     0.37710680445
get_precison()