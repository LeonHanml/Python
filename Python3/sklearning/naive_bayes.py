from sklearning.runTime import runTime
from sklearn import datasets
iris = datasets.load_iris()
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
gnb = GaussianNB()
mnb = MultinomialNB()
bnb = BernoulliNB()
from sklearn import metrics
@runTime
def trainTime(model):
    y_pred = model.fit( X=iris.data,y=iris.target).predict(iris.data)
    report = metrics.classification_report(iris.target,y_pred)
    print(report)


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
    trainTime(gnb)
    trainTime(bnb)
    trainTime(mnb)