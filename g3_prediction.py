# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 07:32:27 2019

@author: Martin
"""

import pandas as pd
import numpy as np
import sklearn 
from sklearn import linear_model

import pickle

data = pd.read_csv("Dataset/student/student-mat.csv", sep=";")

data = data[["G1","G2","G3","studytime","failures","absences"]]

predict = "G3"

X = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X,y, test_size=0.1)

#linear model
linear = linear_model.LinearRegression()
linear.fit(x_train, y_train)
linear_acc = linear.score(x_test, y_test)
print("Linear Acc :", linear_acc)

#RVM model
from skrvm import RVR
rvm = RVR(kernel='linear')
rvm.fit(x_train, y_train)
rvm_acc = rvm.score(x_train, y_train)
print("RVM Acc :", rvm_acc)


with open("studentmodel.pickle", "wb") as f:
    pickle.dump(linear, f)
    
pickle_in = open("studentmodel.pickle", "rb")

print("Coefficient: \n", linear.coef_)
print("Intercept: \n", linear.intercept_)

predictions = linear.predict(x_test)
predictions_rvm = rvm.predict(x_test)

print("By Linear Regression")
print("No", "Prediksi", "Fitur", "Target")
for x in range(len(predictions)):
    print(x, predictions[x], x_test[x], y_test[x])

print("\n")    
print("By RVM Regression")
print("No", "Prediksi", "Fitur", "Target")
for x in range(len(predictions_rvm)):
    print(x, predictions_rvm[x], x_test[x], y_test[x])
    