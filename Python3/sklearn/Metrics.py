from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import recall_score
import pandas as pd
# python + sklearn ︱分类效果评估——acc、recall、F1、ROC、回归、距离
# http://www.itkeyword.com/doc/0270518652490011093/python-sklearn-roc
from sklearn.model_selection import  train_test_split
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