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
                data_train.append([array[0],array[3],array[4],array[5]])

        data_train = pd.DataFrame(data_train,columns=['uid','forward_count','comment_count','like_count'],index=None)
        return data_train



data_train = tools.get_data_train_dataframe(tools)
fclsum = data_train.groupby(by='uid').sum()
fcltotal = fclsum['forward_count']+fclsum['comment_count']+fclsum['like_count']
data = pd.concat([fclsum,pd.DataFrame(fcltotal)],axis=1)
# data.columns=['forward_count','comment_count','like_count','total_count']
clf = KMeans(n_clusters=4)
s = clf.fit(pd.Series(fcltotal,dtype=float).reshape(-1,1))
print(s)
print("==============================")
print(clf.cluster_centers_)
    # if __name__ == '__main__':
    #     pass
