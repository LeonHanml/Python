import pandas as pd
import numpy as np
data_test =[]
with open(r"D:\\www\\data\\Weibo Data\\Weibo Data\\weibo_predict_data(new)\\weibo_predict_data.txt",'r',encoding='utf-8') as f:
    while(True):
        line = f.readline()
        if not line:
            break
            pass
        array = line.split("\t")
        data_test.append([array[0],array[1]])

    



# data_test = pd.read_table('D:\\www\\data\\Weibo Data\\Weibo Data\\weibo_predict_data(new)\\weibo_predict_data.txt',
#                           sep="\t",
#                           header=None, encoding='utf-8')
# data_test.columns = ['uid', 'mid', 'time','content']
#
# data_test.drop(['time','content'], axis=1, inplace=True)
# data_test['forward_count']=0
# data_test['comment_count']=0
# data_test['like_count']=0
# print(data_test.columns)
print(len(data_test))
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


best_file = open("D:\\www\data\\Weibo Data\\Weibo Data\\weibo_predict_data(new)\\best_uid_fcl_predict3_by_allopenfile.txt","w",encoding="utf8")
# data_test1 = data_test[:50000]
for i in range(len(data_test)):
    uid = data_test[i][0]
    min = data_test[i][1]
    if uid not in data_best_predict_dict.keys():
        best_file.write(uid+"\t"+min+"\t"+str(0)+","+str(0)+","+str(0)+"\n")
        # data_test.ix[i][2] = 0
        # data_test.ix[i][3] = 0
        # data_test.ix[i][4] =
    else:
        best_file.write(uid+"\t"+min+"\t"+str(data_best_predict_dict[uid][0][0])+","+str( data_best_predict_dict[uid][0][1])+","+str(data_best_predict_dict[uid][0][2])+"\n")
best_file.flush()
best_file.close()
    # print( data_best_predict_dict[uid][0][0])
    # print( data_best_predict_dict[uid][0][1])
    # print( data_best_predict_dict[uid][0][2])
    # data_test.ix[i]['forward_count','comment_count','like_count'].values =[best_f, best_c, best_l]