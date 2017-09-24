import pandas as pd
import numpy as np

import pickle

data_train = pd.read_table('D:\\www\\data\\Weibo Data\\Weibo Data\\weibo_train_data(new)\\weibo_train_data.txt',
                           sep="\t",
                           header=None, encoding='utf-8')
header = ['uid', 'mid', 'time', 'forward_count', 'comment_count', 'like_count', 'content']
data_train.columns = header

# data_test = pd.read_table('D:\\www\\data\\Weibo Data\\Weibo Data\\weibo_predict_data(new)\\weibo_predict_data.txt',
#                           sep="\t",
#                           header=None, encoding='utf-8')
# data_test.columns = ['uid', 'mid', 'time','content']
#
#
# uid_train = pd.read_table('D:\\www\\data\\Weibo Data\\Weibo Data\\weibo_train_data(new)\\userId.txt',
#                            header=None, encoding='utf-8')
# uid_train.columns = ['uid']
# uid_list = uid_train.values

#


columns=['uid','forward_count','comment_count','like_count',"frequency"]

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
#
# unique_uid_fcl_set.keys()
def sgn(value):
    if value > 0:
        return 1
    else:
        return 0




def get_best_set(unique_uid_fcl_set):
    best_uid_fcl_set ={}
    # 选取一个用户
    for uid in unique_uid_fcl_set.keys():
        # print(uid,unique_uid_fcl_set[uid])
        # 获取该用户 的所有互动类型及其频数
        count_set = unique_uid_fcl_set[uid]
        # 求该用户最好的fcl
        best_f = 0
        best_c = 0
        best_l = 0
        max_precision = 0
        # 选取一个互动类型作为预测结果
        for unique in count_set:
            # print(unique)
            fp = unique[0]
            cp = unique[1]
            lp = unique[2]
            # time = unique[3]
            sum_denom = 0
            sum_number = 0
            # 计算unique 作 预测结果时 整个用户的准确度
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
                # if precision_i <1:
                #     print(precision_i)
                count_i = fr + cr + lr
                if count_i > 100:
                    count_i = 100

                sum_denom += (count_i + 1)*time

                sum_number += (count_i + 1) * sgn(precision_i - 0.8)*time

            precision = sum_number / sum_denom
            # print(precision)
            if (precision > max_precision):
                best_f = fp
                best_c = cp
                best_l = lp
                max_precision = precision
        best_uid_fcl_set[uid]=[best_f, best_c, best_l,max_precision]

    return best_uid_fcl_set


if __name__ == '__main__':

    # get_unique_uid_fcl_set = get_unique_uid_fcl_set()

    best_uid_fcl_set = get_best_set(get_unique_uid_fcl_set())


    best_uid_fcl_set_file = open("D:\\www\data\\Weibo Data\\Weibo Data\\weibo_train_data(new)\\best_uid_fcl_set_0.txt","w",encoding="utf8")
    for i in best_uid_fcl_set.keys():
    #     if (best_uid_fcl_set[i][3]<1):
        best_uid_fcl_set_file.write(i+" "+str(best_uid_fcl_set[i][0])+" "+str(best_uid_fcl_set[i][1])+" "+str(best_uid_fcl_set[i][2])+" "+str(best_uid_fcl_set[i][3])+"\n")


    # pickle.dump(best_uid_fcl_set,best_uid_fcl_set_file)
    best_uid_fcl_set_file.close()


