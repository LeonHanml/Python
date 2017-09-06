# -*- coding: utf-8 -*-
#  os.chdir('D:\www\IdeaProject\MLiA_SourceCode\machinelearninginaction')
# print os.getcwd()
from numpy.ma import zeros, array


if __name__ == '__main__':
    print 'hello'
    import trees
    import treePlotter
    data,lables = trees.createDataSet()
    print data
    print lables
    shannonEnt = trees.calcShannonEnt(data)
    print shannonEnt
    data[0][-1] ='maybe'
    print trees.calcShannonEnt(data)
    print data
    print trees.chooseBestFeatureToSplit(data)
    mytree = trees.createTree(data,lables)
    print mytree
    fr = open('lenses.txt')
    lenses = [inst.strip().split('\t')  for inst in fr.readlines()]
    lensesLables = ['age','prescript','astigmatic','tearRate']
    lensesTree = trees.createTree(lenses,lensesLables)
    print lensesTree
    treePlotter.createPlot(lensesTree)