import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

dataset=pd.read_csv('arcanut.csv')

X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values

"""Encoding categorical data
Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3]) ##why str needs to be at this loc only and not first?
X = onehotencoder.fit_transform(X).toarray()
dummy var trap removal
X=X[:,1:]  ##no need to do this manually lib does it by default..written just for info.
"""

from sklearn.model_selection import cross_val_score
lr = LinearRegression()
lr.fit(X, Y)
cscores = cross_val_score(lr, X, Y, cv=5)
print('Cross Val Score for Regression is ' + str(round(cscores.mean()*100, 2))+', Accuracy score is: '+str(round(lr.score(X,Y)*100, 2)))

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.1, random_state = 0)

regressor = LinearRegression()

regressor.fit(X_train, Y_train)
#predecting test set results

Y_pred = regressor.predict(X_test)
#print(Y_pred)

