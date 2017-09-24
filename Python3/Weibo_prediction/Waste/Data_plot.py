import pandas as pd
import matplotlib.pyplot as plt
data_train = pd.read_table('D:\\www\\data\\Weibo Data\\Weibo Data\\weibo_train_data(new)\\weibo_train_data.txt',sep="\t",
                     header=None,encoding='utf-8')
#header=None:没有每列的column name，可以自己设定
#encoding='gb2312':其他编码中文显示错误
#delim_whitespace=True:用空格来分隔每行的数据
#index_col=0:设置第1列数据作为index
# data.head(1)
# data.info()
header = ['userId','weiboId','datetime','forward_count','comment_count','like_count','content']
data_train.columns = header
# DataFrame

# userId_array = data_train.userId
# print(type(userId_array))
# print(len(set(list(userId_array)))) #共有多少用户




# # 计算一下 总共有多少人发微博 即userid 数量
# userid_counts = data_train.userId.value_counts()
# userid_counts.count()
#
# # 同时也可以得出每个user 发的微博数量
# userid_counts_frame = userid_counts.to_frame()
# userid_counts_frame.describe()
#
# # 计算只有一条数据的用户数
# userid_counts_frame = userid_counts.to_frame()
#
#
# userid_counts_frame.columns = ['wbcount']
# userid_counts_frame[userid_counts_frame['wbcount']==1]
# len(userid_counts_frame[userid_counts_frame['wbcount']==1])
print(data_train.describe())
'''
 # 密度分布图

fig = plt.figure()
data_train["forward_count"].plot(kind="kde")
data_train["comment_count"].plot(kind="kde")
data_train["like_count"].plot(kind="kde")
plt.xlabel("Count")# plots an axis lable
plt.ylabel("Density")
plt.title("Density of FCL")
plt.legend((u'1 Forward_count', u'2 Comment_count',u'3 Like_count'),loc='best') # sets our legend for our graph.
plt.show()
'''
fc0=data_train["forward_count"][data_train["forward_count"] == 0].count()
cc0=data_train["comment_count"][data_train["forward_count"] == 0].count()
lc0=data_train["like_count"][data_train["forward_count"] == 0].count()



'''
fig = plt.figure()
[data_train["forward_count"] != 0]

data_train["forward_count"][data_train["forward_count"] == 0].value_counts()()
data_train["comment_count"][data_train["comment_count"] == 0].count()
data_train["like_count"][data_train["like_count"] == 0].count()

userId_sum = data_train.groupby(by="userId").sum()
userId_sum.to_excel(r'D:\\www\\data\\Weibo Data\\Weibo Data\\weibo_train_data(new)\\userId_sum.xls',sheet_name='Sheet1')
userId_sum.columns#Index(['forward_count', 'comment_count', 'like_count'], dtype='object')
userId_sum[userId_sum.forward_count==0].count()#25259
userId_sum[userId_sum.comment_count==0].count()#19877
userId_sum[userId_sum.like_count==0].count()#19303
userId_sum[userId_sum.forward_count==0][userId_sum.comment_count==0][userId_sum.like_count==0]#15366

'''
'''
import  matplotlib.pyplot as plt
fig = plt.figure()
data_train["forward_count"].value_counts().plt()
plt.show()

'''
















