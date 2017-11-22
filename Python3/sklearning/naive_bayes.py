from sklearning.runTime import runTime
from sklearn import datasets
iris = datasets.load_iris()

from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import cross_val_score
from sklearn import cross_validation

from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
gnb = GaussianNB()
mnb = MultinomialNB()
bnb = BernoulliNB()
from sklearn import metrics
import numpy as np
target = set(iris.target)
print(target)
@runTime
def trainTime(model):
    y_pred = model.fit( X=iris.data,y=iris.target).predict(iris.data)
    model.partial_fit( X=iris.data,y=iris.target).predict(iris.data)
    report = metrics.classification_report(iris.target,y_pred)
    mean_squ_err = metrics.mean_squared_error(iris.target, y_pred)
    # print(report)
    # print(mean_squ_err)
    print ("贝叶斯分类器20折交叉验证得分:model ", np.mean(cross_val_score(model,iris.data,iris.target,cv=20,n_jobs=3)))


'''
y_pred = gnb.fit( X=iris.data,y=iris.target).predict(iris.data)
y_pred_mnb = mnb.fit( X=iris.data,y=iris.target).predict(iris.data)
y_pred_bnb = bnb.fit( X=iris.data,y=iris.target).predict(iris.data)

right_num = (iris.target == y_pred).sum()
print("Total testing num :%d , naive bayes accuracy :%f" %(iris.data.shape[0], float(right_num)/iris.data.shape[0]))




gnbTrainModel = gnb.fit(iris.data,iris.target)
pred_y = gnbTrainModel.predict(iris.data)

report = metrics.classification_report(iris.target,pred_y)
report_mnb = metrics.classification_report(iris.target,y_pred_mnb)
report_bnb = metrics.classification_report(iris.target,y_pred_bnb)

report1 = metrics.mean_squared_error(iris.target, pred_y)

print(report)
print(report_mnb)
print(report_bnb)
'''
if __name__ == '__main__':
    # trainTime(gnb)
    # trainTime(mnb)
    # trainTime(bnb)


    # scoring='roc_auc',只适用于二分类？

    print ("多项式贝叶斯分类器20折交叉验证得分: ", np.mean(cross_val_score(gnb,iris.data,iris.target,cv=20,n_jobs=3)))