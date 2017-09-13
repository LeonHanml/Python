import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_table('D:\\www\\data\\Weibo Data\\Weibo Data\\weibo_train_data(new)\\weibo_train_data.txt',sep="\t",
                     header=None,encoding='utf-8',index_col=0)
#header=None:没有每列的column name，可以自己设定
#encoding='gb2312':其他编码中文显示错误
#delim_whitespace=True:用空格来分隔每行的数据
#index_col=0:设置第1列数据作为index
# data.head(1)
# data.info()
header = ['userId','weiboId','datetime','forward_count','comment_count','like_count']
data.columns = header
data.columns
fig = plt.figure()

print(data.userId.head(10))
userId_array = data.userId
print(type(userId_array))
print(len(set(list(userId_array))))
# userMap={}
# for i in userId_array:
#     userMap[i] = 1
# print(len(userMap))
# plt.show()