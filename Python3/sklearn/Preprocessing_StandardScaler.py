import sklearn.preprocessing as preprocessing
import pandas as pd
import numpy as  np
# preprocessing.StandardScaler()
# preprocessing.LabelEncoder()
data_train = pd.read_csv('D:\\www\\data\\Titanic\\train.csv')
df = data_train
'''归一化方法'''
scaler = preprocessing.StandardScaler()
age_scale_param = scaler.fit(df['Age'])
df['Age_scaled'] = scaler.fit_transform(df['Age'], age_scale_param)
fare_scale_param = scaler.fit(df['Fare'])
df['Fare_scaled'] = scaler.fit_transform(df['Fare'], fare_scale_param)

df['Fare_scaled'].values.reshape(-1, 1)
df['Age_scaled'].values.reshape(-1, 1)

df.to_csv("D:\\www\\data\\Titanic\\train_data.csv", index=False)

#convert to numpy array before training
train_s = np.array(data_train)
test_s = np.array(data_train)


#label encode the categorical variables before training
for i in range(train_s.shape[1]):
    lbl = preprocessing.LabelEncoder()
    lbl.fit(list(train_s[:,i]) + list(test_s[:,i]))
    train_s[:,i] = lbl.transform(train_s[:,i])
    test_s[:,i] = lbl.transform(test_s[:,i])

#convert to float before training using xgboost
train_s = train_s.astype(float)
test_s = test_s.astype(float)