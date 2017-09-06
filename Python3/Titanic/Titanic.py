# pip3 uninstall numpy
# sudo pip3 install scipy
# sudo  pip3 install sklearn
# sudo  pip3 install scipy http://www.lfd.uci.edu/~gohlke/pythonlibs/
# sudo  pip3 install pandas

import pandas as pd
# data = pd.read_csv('/home/hanliang2/www/Titanic/train.csv')
data = pd.read_csv('D:\\www\\data\\Titanic\\train.csv')
#剔除变量
data.drop(['PassengerId','Ticket'],axis=1,inplace=True)
#补全Embarked变量
data.loc[data.Embarked.isnull(),'Embarked']='S'
#one-hot编码
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
#ohe_pclass=OneHotEncoder(sparse=False).fit(data[['Pclass']])
#Pclass_ohe=ohe_pclass.transform(data[['Pclass']])
le_sex=LabelEncoder().fit(data['Sex'])
Sex_label=le_sex.transform(data['Sex'])
ohe_sex=OneHotEncoder(sparse=False).fit(Sex_label.reshape(-1,1))
Sex_ohe=ohe_sex.transform(Sex_label.reshape(-1,1))
le_embarked=LabelEncoder().fit(data['Embarked'])
Embarked_label=le_embarked.transform(data['Embarked'])
ohe_embarked=OneHotEncoder(sparse=False).fit(Embarked_label.reshape(-1,1))
Embarked_ohe=ohe_embarked.transform(Embarked_label.reshape(-1,1))
def replace_name(x):
    if 'Mrs' in x:
        return 'Mrs'
    elif 'Mr' in x:
        return 'Mr'
    else:
        return 'Miss'


data['Name']=data['Name'].map(lambda x:replace_name(x))
le_name=LabelEncoder().fit(data['Name'])
Name_label=le_name.transform(data['Name'])
ohe_name=OneHotEncoder(sparse=False).fit(Name_label.reshape(-1,1))
Name_ohe=ohe_name.transform(Name_label.reshape(-1,1))
data['Sex_0']=Sex_ohe[:,0]
data['Sex_1']=Sex_ohe[:,1]
data['Embarked_0']=Embarked_ohe[:,0]
data['Embarked_1']=Embarked_ohe[:,1]
data['Embarked_2']=Embarked_ohe[:,2]
data['Name_0']=Name_ohe[:,0]
data['Name_1']=Name_ohe[:,1]
data['Name_2']=Name_ohe[:,2]
#归一化处理
from sklearn.preprocessing import StandardScaler
Pclass_scale=StandardScaler().fit(data['Pclass'])
data['Pclass_scaled']=StandardScaler().fit_transform(data['Pclass'].reshape(-1,1),Pclass_scale)
Fare_scale=StandardScaler().fit(data['Fare'])
data['Fare_scaled']=StandardScaler().fit_transform(data['Fare'].reshape(-1,1),Fare_scale)
SibSp_scale=StandardScaler().fit(data['SibSp'])
data['SibSp_scaled']=StandardScaler().fit_transform(data['SibSp'].reshape(-1,1),SibSp_scale)
Parch_scale=StandardScaler().fit(data['Parch'])
data['Parch_scaled']=StandardScaler().fit_transform(data['Parch'].reshape(-1,1),Parch_scale)
#预测年纪并补全
from sklearn.ensemble import RandomForestRegressor
def set_missing_age(data):
    train=data[['Age','SibSp_scaled','Parch_scaled','Name_0','Name_1','Name_2','Sex_0','Sex_1']]
    known_age=train[train.Age.notnull()].as_matrix()
    unknown_age=train[train.Age.isnull()].as_matrix()
    y=known_age[:,0]
    x=known_age[:,1:]
    rf=RandomForestRegressor(random_state=0,n_estimators=200,n_jobs=-1)
    rf.fit(x,y)
    print (rf.score(x,y))
    predictage=rf.predict(unknown_age[:,1:])
    data.loc[data.Age.isnull(),'Age']=predictage
    return data,rf


data,rf=set_missing_age(data)
Age_scale=StandardScaler().fit(data['Age'])
data['Age_scaled']=StandardScaler().fit_transform(data['Age'].reshape(-1,1),Age_scale)
train_x=data[['Sex_0','Sex_1','Embarked_0','Embarked_1','Embarked_2','Name_0','Name_1','Name_2','Pclass_scaled','Age_scaled','Fare_scaled']].as_matrix()
train_y=data['Survived'].as_matrix()