# http://blog.csdn.net/gamer_gyt/article/details/51265347
from sklearn.svm import LinearSVC
# svc   classification  sv   cv  cross validation
# svr   regression
from sklearn.datasets import make_classification
X, y = make_classification(n_features=4, random_state=0)
clf = LinearSVC(random_state=0)
clf.fit(X, y)

print(clf.coef_)

print(clf.intercept_)

print(clf.predict([[0, 0, 0, 0]]))

