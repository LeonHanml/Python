# -*- coding: utf-8 -*-
#  os.chdir('D:\www\IdeaProject\MLiA_SourceCode\machinelearninginaction\Ch07\')
# print os.getcwd()
from numpy.ma import zeros, array


if __name__ == '__main__':
    print 'hello'
    from numpy import *
    # import operator
    import adaboost

    dataMat ,classLabels = adaboost.loadSimpData()
    print dataMat
    print classLabels
    D = mat(ones((5,1))/5)
    print D
    bestStump,minError,bestClasEst =adaboost.buildStump(dataMat,classLabels,D)
    print bestStump
