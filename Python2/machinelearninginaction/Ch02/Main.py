# -*- coding: utf-8 -*-
#  os.chdir('D:\www\IdeaProject\MLiA_SourceCode\machinelearninginaction')
# print os.getcwd()
from numpy.ma import zeros, array


if __name__ == '__main__':
    print 'hello'
    # from numpy import *
    # import operator
    import kNN
    # group ,lables = kNN.createDataSet()
    # print kNN.classify0([0,0],group,lables,3)
    # dataMat ,dataLables = kNN.file2matrix('datingTestSet2.txt')
    # print dataMat
    # import  matplotlib
    # import matplotlib.pyplot as plt
    # fig = plt.figure()
    # ax = fig.add_subplot(211)
    # ax.scatter(dataMat[:,1],dataMat[:,2],15.0*array(dataLables),15.0*array(dataLables))
    # ax = fig.add_subplot(212)
    # ax.scatter(dataMat[:,0],dataMat[:,1],15.0*array(dataLables),15.0*array(dataLables))
    # plt.show()
    # # kNN.datingClassTest()

    kNN.handwritingClassTest()