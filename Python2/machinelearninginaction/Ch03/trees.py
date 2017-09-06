# -*- coding: utf-8 -*-
'''
Created on Oct 12, 2010
Decision Tree Source Code for Machine Learning in Action Ch. 3
@author: Peter Harrington
'''
from math import log
import operator

def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    #change to discrete values
    return dataSet, labels
# 计算熵
def calcShannonEnt(dataSet):
    numEntries = len(dataSet) #获取数据样本长度 行
    labelCounts = {}          #标签数  每个标签  对应的数量 用于计算概率
    # 计算所有Lable的次数
    for featVec in dataSet: # 遍历每一行（样本）          the the number of unique elements and their occurance
        currentLabel = featVec[-1]# 获取当前行标签  最后一个
        if currentLabel not in labelCounts.keys(): labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2) #log base 2
    return shannonEnt
#     列是属性   行是样本    除去axis列  的数据集


# 信息熵是概率计算   对每一列属性  其中包含的不同值进行划分
#
# 其中的值存在的概率进行计算 统计
# 然后求和  分割数据集 去除最佳  属性，获得 属性值为value的子集
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]     #chop out axis used for splitting
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet
    
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1      #  列 特征数  the last column is used for the labels
    baseEntropy = calcShannonEnt(dataSet) #数据集 基础熵值
    bestInfoGain = 0.0; bestFeature = -1
    for i in range(numFeatures):        #对每一列进行遍历 每个特征 进行计算 求 香浓熵 iterate over all the features
        # 获取列的所有特征值，然后 去重   对每个值进行概率计算
        featList = [example[i] for example in dataSet]  #create a list of all the examples of this feature
        uniqueVals = set(featList)       #get a set of unique values！！！！！！！！！！！！！！！！最快的方法
        newEntropy = 0.0
        for value in uniqueVals: #对i列种存在的每个值进行香浓熵概率计算
            #根据这个值进行划分
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))# 这个值在整体dataset中的概率
            newEntropy += prob * calcShannonEnt(subDataSet)     
        infoGain = baseEntropy - newEntropy     #calculate the info gain; ie reduction in entropy
        if (infoGain > bestInfoGain):       #compare this to the best gain so far
            bestInfoGain = infoGain         #if better than current best, set to best
            bestFeature = i
    return bestFeature                      #returns an integer

def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]#排序后选出 第一个   最多的分类

def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]

    #类别完全相同则停止划分
    if classList.count(classList[0]) == len(classList): 
        return classList[0]#stop splitting when all of the classes are equal
    if len(dataSet[0]) == 1: #stop splitting when there are no more features in dataSet
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])#删除当前最佳分类
    # 得到列表包含所有的属性值  获取属性[bestFeat]的所有值
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    #遍历所有的属性值，建立树
    for value in uniqueVals:
        subLabels = labels[:]       #copy all of labels, so trees don't mess up existing labels
        #                                                                               已经去除了bestFeat的labels
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value),subLabels)
    return myTree                            
    
def classify(inputTree,featLabels,testVec):
    firstStr = inputTree.keys()[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    key = testVec[featIndex]
    valueOfFeat = secondDict[key]
    if isinstance(valueOfFeat, dict): 
        classLabel = classify(valueOfFeat, featLabels, testVec)
    else: classLabel = valueOfFeat
    return classLabel

def storeTree(inputTree,filename):
    import pickle
    fw = open(filename,'w')
    pickle.dump(inputTree,fw)
    fw.close()
    
def grabTree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)
    
