# -*- coding: utf-8 -*-
"""Bank Customer Churn Model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rkq7mL7zgjF3P7eOJjH2WDHhYWW6r9c2
"""

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

"""Import **Dataset**"""

df = pd.read_csv("https://raw.githubusercontent.com/YBI-Foundation/Dataset/main/Bank%20Churn%20Modelling.csv")

df.head()

df.info()

df.duplicated('CustomerId').sum()

df = df.set_index('CustomerId')

df.info()

"""**Encoding**"""

df['Geography'].value_counts()

df.replace({'Geography' : {'France': 2, 'Germany': 1, 'Spain': 0}}, inplace = True)

df['Gender'].value_counts()

df.replace({'Gender' : {'Male': 0, 'Female': 1}}, inplace = True)

df['Num Of Products'].value_counts()

df.replace({'Gender' : {1: 0, 2: 1,3: 1,4: 1}}, inplace = True)

df['Has Credit Card'].value_counts()

df['Is Active Member'].value_counts()

df.loc[(df['Balance']==0),'Churn'].value_counts()

df['Zero Balance'] = np.where(df['Balance']>0,1,0)

df['Zero Balance'].hist()

df.groupby(['Churn','Geography']).count()

"""**Label and Functions**"""

df.columns

X = df.drop(['Surname','Churn'],axis=1)

y = df['Churn']

sns.countplot(x = 'Churn', data  = df);

X.shape,y.shape

"""**Under Sampling**"""

from imblearn.under_sampling import RandomUnderSampler

rus = RandomUnderSampler(random_state = 2529)

X_rus, y_rus = rus.fit_resample(X, y)

X_rus.shape , y_rus.shape , X.shape,y.shape

y.value_counts()

y_rus.value_counts()

y_rus.plot(kind = 'hist')

from imblearn.over_sampling import RandomOverSampler

ros = RandomOverSampler(random_state = 2529)

X_ros, y_ros = ros.fit_resample(X, y)

X_ros.shape , y_ros.shape , X.shape,y.shape

y.value_counts()

y_ros.value_counts()

y_ros.plot(kind = 'hist')

"""**Train Test Split**"""

from sklearn.model_selection import train_test_split

"""**Split Original Data**"""

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=2529)

"""**Under Sample Data**"""

X_train_rus, X_test_rus, y_train_rus, y_test_rus = train_test_split(X_rus,y_rus,test_size=0.3,random_state=2529)

"""**Over Sample Data**"""

X_train_ros, X_test_ros, y_train_ros, y_test_ros = train_test_split(X_ros,y_ros,test_size=0.3,random_state=2529)

"""**Standardize Features**"""

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

"""**Standardize Original Data**"""

X_train[['CreditScore','Age','Tenure','Balance','Estimated Salary']] = sc.fit_transform(X_train[['CreditScore','Age','Tenure','Balance','Estimated Salary']])

X_test[['CreditScore','Age','Tenure','Balance','Estimated Salary']] = sc.fit_transform(X_test[['CreditScore','Age','Tenure','Balance','Estimated Salary']])

"""**Standardize Under Sample Data**"""

X_train_rus[['CreditScore','Age','Tenure','Balance','Estimated Salary']] = sc.fit_transform(X_train_rus[['CreditScore','Age','Tenure','Balance','Estimated Salary']])

X_test_rus[['CreditScore','Age','Tenure','Balance','Estimated Salary']] = sc.fit_transform(X_test_rus[['CreditScore','Age','Tenure','Balance','Estimated Salary']])

"""**Standardize Over Sample Data**"""

X_train_ros[['CreditScore','Age','Tenure','Balance','Estimated Salary']] = sc.fit_transform(X_train_ros[['CreditScore','Age','Tenure','Balance','Estimated Salary']])

X_test_ros[['CreditScore','Age','Tenure','Balance','Estimated Salary']] = sc.fit_transform(X_test_ros[['CreditScore','Age','Tenure','Balance','Estimated Salary']])

"""**Support Vector Machine Classifier**"""

from sklearn.svm import SVC

svc = SVC()

"""**Original Data**"""

svc.fit(X_train,y_train)

y_pred = svc.predict(X_test)

"""Under Sampled Data"""

svc.fit(X_train_rus,y_train_rus)

y_pred_rus = svc.predict(X_test_rus)

"""**Over Sampled Data**"""

svc.fit(X_train_ros,y_train_ros)

y_pred_ros = svc.predict(X_test_ros)

"""**Model Accuracy**"""

from sklearn.metrics import confusion_matrix , classification_report

confusion_matrix(y_test, y_pred)

print(classification_report(y_test,y_pred))

print(classification_report(y_test_rus,y_pred_rus))

print(classification_report(y_test_ros,y_pred_ros))