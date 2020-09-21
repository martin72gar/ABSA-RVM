# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 23:20:53 2019

@author: Martin
"""

""" Importing the libraries """
import pandas as pd
import re
import pickle
import numpy as np
import matplotlib.pyplot as plt
import nltk

#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Import Dataset
data_review = pd.read_csv('Dataset/train_data.csv', sep=";", encoding="ISO-8859-1")
data_review = data_review[0:200]

# Preprosesing
corpus = []
for i in range(len(data_review)):
    review = re.sub('[^a-zA-Z]', ' ', data_review['review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('indonesian'))]
    review = ' '.join(review)
    corpus.append(review)

# Pembobotan TFIDF
from sklearn.feature_extraction.text import TfidfVectorizer
tf = TfidfVectorizer(max_features=500)
X = tf.fit_transform(corpus).toarray()
#ambil nilai target food
''' Target Negative(0) vs All(Positive(1) dan Netral(1))'''
yprice = data_review.iloc[0:len(data_review), 3].values

y = yprice
''' Target Positive(1) vs All(Negative(2) dan Netral(2))'''
# yfood2 = data_review.iloc[0:len(data_review), 1].values
# for i in range(len(yfood2)):
#     if (yfood2[i] == 'positive'):
#         yfood2[i] = '1'
#     else:
#         yfood2[i] = '2'
#
# y = yfood2

''' Target Netral(2) vs All(Negative(0) dan Netral(0))'''
# yfood3 = data_review.iloc[0:len(data_review), 1].values
# for i in range(len(yfood3)):
#     if (yfood3[i] != 'positive' and 'negative'):
#         yfood3[i] = '2'
#     else:
#         yfood3[i] = '0'
#
# y = yfood3


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

# Fitting RVM to the Training set
from skrvm import RVC
classifier = RVC(verbose=True)
classifier.fit(X_train, y_train)

# Simpan model hasil training
with open("model200targetysprice.pickle", "wb") as f:
    pickle.dump(classifier, f)

# LOAD MODEL
# pickle_in = open("model200targetyservice.pickle", "rb")
# classifier = pickle.load(pickle_in)


# Predicting the Test set results
y_predict = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_predict)

akurasi = classifier.score(X_train,y_train)

