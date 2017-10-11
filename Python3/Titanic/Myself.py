from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

### 使用 RandomForestClassifier 填补缺失的年龄属性
# Survived       891 non-null int64
# Pclass         891 non-null int64
# Name           891 non-null object
# Sex            891 non-null object
# Age            714 non-null float64
# SibSp          891 non-null int64
# Parch          891 non-null int64
# Ticket         891 non-null object
# Fare           891 non-null float64
# Cabin          204 non-null object
# Embarked       889 non-null object
# dtypes: float64(2), int64(5), object(5)

# PassengerId => 乘客ID
# Pclass => 乘客等级(1/2/3等舱位)
# Name => 乘客姓名
# Sex => 性别
# Age => 年龄
# SibSp => 堂兄弟/妹个数
# Parch => 父母与小孩个数
# Ticket => 船票信息
# Fare => 票价
# Cabin => 客舱
# Embarked => 登船港口

import numpy as np  # 科学计算
from pandas import Series, DataFrame
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.cross_validation import train_test_split
from sklearn import metrics
# model = ExtraTreesClassifier()
def setMissingData():
    # display the relative importance of each attribute
    data_train = pd.read_csv('D:\\www\\data\\Titanic\\train.csv')
    # 把已有的数值型特征取出来丢进Random Forest Regressor中
    age_df = data_train[['Age','Fare', 'Parch', 'SibSp', 'Pclass']]

    # 乘客分成已知年龄和未知年龄两部分
    known_age = age_df[age_df.Age.notnull()].as_matrix()
    unknown_age = age_df[age_df.Age.isnull()].as_matrix()

    # y即目标年龄
    y = known_age[:, 0]
    x = known_age[:,1:]
    # X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.33, random_state=42)
    x_train ,x_test,y_train,y_test = train_test_split(x,y,test_size=0.33, random_state=42)
    #  metrics.mean_squared_error(y_test, y_test_predicted)=147.275271966   test_size=0.33
    #  metrics.mean_squared_error(y_test, y_test_predicted)=173.8745414   test_size=0.1
    rfr = RandomForestRegressor(random_state=0, n_estimators=2000, n_jobs=-1)

    rfr.fit(x_train,y_train)
    y_test_predicted = rfr.predict(x_test)
    score = rfr.score(x_test,y_test)
    # model.fit(x_train,y_train)

    report = metrics.mean_squared_error(y_test, y_test_predicted)
    report2 = metrics.mean_absolute_error(y_test, y_test_predicted)
    print(score)
    print(report)
    print(report2)

    import matplotlib.pyplot as plt
    plt.figure()


    # df = pd.DataFrame({'x':x_test,'y':y_test,'y_predicted':y_test_predicted})
    # plt.scatter(range(len(y_test)),y_test_predicted)
    # plt.scatter(range(len(y_test)),y_test)

    plt.plot(range(len(y_test)),y_test_predicted)
    plt.plot(range(len(y_test)),y_test)
    # plt.plot(y_test-y_test_predicted)
    # loss =np.square (y_test-y_test_predicted)/len(y_test)
    # print(loss)
    # df.plot(kind='line',stacked=True)

    plt.show()
    # X即特征属性值
    # X = known_age[:, 1:]

    # fit到RandomForestRegressor之中

    # rfr.fit(X, y)
    #
    # # 用得到的模型进行未知年龄结果预测
    # predictedAges = rfr.predict(unknown_age[:, 1::])
    #
    # # 用得到的预测结果填补原缺失数据
    # df.loc[ (df.Age.isnull()), 'Age' ] = predictedAges
    #
    # return df, rfr

def set_Cabin_type(df):
    df.loc[ (df.Cabin.notnull()), 'Cabin' ] = "Yes"
    df.loc[ (df.Cabin.isnull()), 'Cabin' ] = "No"
    return df
setMissingData()