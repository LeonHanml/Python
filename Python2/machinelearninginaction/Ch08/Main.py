# -*- coding: utf-8 -*-
#  os.chdir('D:\www\IdeaProject\MLiA_SourceCode\machinelearninginaction')
# print os.getcwd()
if __name__ == '__main__':
    import regression
    from numpy import *
    xArr,yArr = regression.loadDataSet('ex0.txt')
    ws = regression.standRegres(xArr,yArr)
    xMat = mat(xArr)
    yMat = mat(yArr)
    yHat = xMat * ws # 预测列

    import matplotlib.pyplot as plt
    fig = plt.figure() #创建画布
    ax = fig.add_subplot(211)
    #ax = fig.add_subplot(349) 参数349的意思是：将画布分割成3行4列，图像画在从左到右从上到下的第9块，
    # 3410是不行的，可以用另一种方式(3,4,10)。
    # ax = fig.add_subplot(2,1,1)
    # ax.plot(x,y)
    # ax = fig.add_subplot(2,2,3)
    # ax.plot(x,y)
    # plt.show()  显示多图
    ax.scatter(xMat[:,1].flatten().A[0],yMat.T[:,0].flatten().A[0])
    xCopy = xMat.copy()
    xCopy.sort(0)
    yHat = xCopy *ws
    ax.plot(xCopy[:,1],yHat)
    print corrcoef(yHat.T,yMat)# 转置 保证都是行向量

    xArrL,yArrL = regression.loadDataSet('ex0.txt')
    yArrL[0]
    regression.lwlr(xArrL[0],xArrL,yArrL,1.0)
    yHatL = regression.lwlrTest(xArrL,xArrL,yArrL,0.01)

    xMatL = mat(xArrL)
    yMatL = mat(yArrL)
    srtInd = xMatL[:, 1].argsort(0)
    xSort = xMatL[srtInd][:,0,:]
    ax = fig.add_subplot(2,1,2)
    ax.scatter(xMatL[:,1].flatten().A[0],yMatL.T[:,0].flatten().A[0])
    ax.plot(xSort[:,1],yHatL[srtInd])
    plt.show()
    print corrcoef(yHatL.T,yMatL)





