from sklearn.cluster import KMeans
import numpy as np

X = np.array([[1, 2, 3], [1, 4, 3], [1, 0, 3],
              [4, 2, 3], [4, 4, 3], [4, 0, 3]])
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
print(kmeans.labels_)

pre = kmeans.predict([[0, 0, 3], [4, 4, 3]])
print(pre)

print(kmeans.cluster_centers_)


import pandas as pd
from sklearn.cluster import KMeans
class tools ():
    def get_data_train_dataframe(self):
        data_train =[]
        with open(r"D:\\www\\data\\Weibo Data\\Weibo Data\\weibo_train_data(new)\\weibo_train_data.txt",'r',encoding='utf-8') as f:
            while(True):
                line = f.readline()
                if not line:
                    break
                    pass
                array = line.split("\t")
                data_train.append([array[0],int(array[3]),int(array[4]),int(array[5])])

        data_train = pd.DataFrame(data_train,columns=['uid','forward_count','comment_count','like_count'],index=None)
        return data_train

data_train = tools.get_data_train_dataframe(tools)
fclsum = data_train.groupby(by='uid').sum()

fcltotal = fclsum['forward_count']+fclsum['comment_count']+fclsum['like_count']
data = pd.concat([fclsum,pd.DataFrame(fcltotal)],axis=1)

import numpy as np
data_array = np.array(data,dtype=float)

from sklearn.cluster import KMeans
X=data_array
kmeans = KMeans(n_clusters=4, random_state=0).fit(X)

# http://blog.csdn.net/buracag_mc/article/details/75727895
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\msyh.ttc", size=10)
from scipy.spatial.distance import cdist
K=range(1,10)
meandistortions=[]
for k in K:
    kmeans=KMeans(n_clusters=k)
    kmeans.fit(X)
    meandistortions.append(sum(np.min(
        cdist(X,kmeans.cluster_centers_,
              'euclidean'),axis=1))/X.shape[0])
plt.plot(K,meandistortions,'bx-')
plt.xlabel('k')
plt.ylabel(u'平均畸变程度',fontproperties=font)
plt.title(u'用肘部法则来确定最佳的K值 ',fontproperties=font)
plt.show()

