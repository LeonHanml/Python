# -*- coding: utf-8 -*-
#coding:utf-8
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#有中文出现的情况，需要u'内容'
#  os.chdir('D:\www\IdeaProject\MLiA_SourceCode\machinelearninginaction')
# print os.getcwd()

import matplotlib.pyplot as plt
import pandas as pd #数据分析
import numpy as np #科学计算
from pandas import Series,DataFrame
import pandas as pd
# data = pd.read_csv('/home/hanliang2/www/Titanic/train.csv')
data_train = pd.read_csv('D:\\www\\data\\Titanic\\train.csv')
fig = plt.figure()
fig.set(alpha=0.2)  # 设定图表颜色alpha参数

plt.subplot2grid((2,3),(0,0), colspan=2)
data_train.Age.plot(kind='line')
# data_train.Age[data_train.Pclass == 1].plot(kind='kde')
# data_train.Age[data_train.Pclass == 2].plot(kind='kde')
# data_train.Age[data_train.Pclass == 3].plot(kind='kde')


plt.xlabel(u"年龄")# plots an axis lable
plt.ylabel(u"密度")
plt.title(u"各等级的乘客年龄分布")
plt.legend((u'头等舱', u'2等舱',u'3等舱'),loc='best') # sets our legend for our graph.


plt.show()