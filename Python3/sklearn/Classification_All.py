import time
from sklearn import metrics
import pickle as pickle
import pandas as pd

# Multinomial Naive Bayes Classifier
def naive_bayes_classifier(train_x,train_y):
    from sklearn.naive_bayes import MultinomialNB
    module = MultinomialNB(alpha=0.01)
    module.fit(train_x,train_y)
    return module

# KNN Classifier
def knn_classifier(train_x,train_y):
    from sklearn.neighbors import KNeighborsClassifier
    module = KNeighborsClassifier()
    module.fit(train_x,train_y)
    return module

# Logistic Regression Classifier
def logistic_regression_classifier(train_x,train_y):
    from sklearn.linear_model.logistic import LogisticRegression
    module = LogisticRegression(penalty='l2')
    module.fit(train_x,train_y)
    return  module
# Decision Tree
def decision_tree_classifier(train_x,train_y):
    from sklearn import tree
    module = tree.DecisionTreeClassifier()
    module.fit(train_x,train_y)
    return module

# Random Forest Classifier
def random_forest_classifier(train_x,train_y):
    # Ensemble learning(集成学习)
    from sklearn.ensemble.forest import RandomForestClassifier
    module = RandomForestClassifier(n_estimators=8)
    module.fit(train_x,train_y)
    return module

def svm_classifier(train_x,train_y):
    from sklearn.svm import SVC
    model = SVC(kernel='rbf',probability=True)
    model.fit(train_x,train_y)
    return model

# GBDT(Gradient Boosting Decision Tree) Classifier
def gradient_boosting_classifier(train_x,train_y):
    from sklearn.ensemble.gradient_boosting import GradientBoostingClassifier
    model = GradientBoostingClassifier
    model.fit(train_x,train_y)
    return model























