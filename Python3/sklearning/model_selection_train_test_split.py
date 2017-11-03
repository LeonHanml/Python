import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.cross_validation import train_test_split
# http://scikit-learn.org/stable/modules/cross_validation.html#cross-validation-iterators-for-i-i-d-data
from sklearn.model_selection import  train_test_split
from sklearn import metrics
# model = ExtraTreesClassifier()
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import cross_val_score


iris = datasets.load_iris()
iris.data.shape, iris.target.shape
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.4, random_state=0)

X_train.shape, y_train.shape

X_test.shape, y_test.shape


clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
clf.score(X_test, y_test)

from sklearn.model_selection import cross_validate
from sklearn.metrics import recall_score
scoring = ['precision_macro', 'recall_macro']
clf = svm.SVC(kernel='linear', C=1, random_state=0)
scores = cross_validate(clf, iris.data, iris.target, scoring=scoring,
                        cv=5, return_train_score=False)
sorted(scores.keys())

scores['test_recall_macro']

clf = svm.SVC(kernel='linear', C=1)
scores = cross_val_score(clf, iris.data, iris.target, cv=5)
scores

from sklearn import preprocessing
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.4, random_state=0)
scaler = preprocessing.StandardScaler().fit(X_train)
X_train_transformed = scaler.transform(X_train)
clf = svm.SVC(C=1).fit(X_train_transformed, y_train)
X_test_transformed = scaler.transform(X_test)
clf.score(X_test_transformed, y_test)


from sklearn.model_selection import cross_val_predict
predicted = cross_val_predict(clf, iris.data, iris.target, cv=10)
metrics.accuracy_score(iris.target, predicted)



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




