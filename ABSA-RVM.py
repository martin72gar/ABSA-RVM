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
data_review = data_review[0:50]

# Cleaning kolom review pada dataset
corpus = []
for i in range(len(data_review)):
    review = re.sub('[^a-zA-Z]', ' ', data_review['review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('indonesian'))]
    review = ' '.join(review)
    corpus.append(review)

# Creating the Bag of Words model

"""from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=1500)
X = cv.fit_transform(corpus).toarray()
y = data_review.iloc[0:len(data_review), 1].values
"""


from sklearn.feature_extraction.text import TfidfVectorizer
tf = TfidfVectorizer(max_features=1500)
X = tf.fit_transform(corpus).toarray()
y = data_review.iloc[0:len(data_review), 1].values


"""
Xtf = tf.fit_transform(corpus) // Xtf = tf.fit_transform(corpus).toarray

from sklearn.feature_extraction.text import TfidfTransformer
tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)

from sklearn.feature_extraction.text import TfidfTransformer
tf_idf = Tfidftransformer()

listToStr = ' '.join([str(elem) for elem in corpus[0:3]]

from sklearn.feature_extraction.text import TfidfVectorizer
>>> sample = [
...     'This is the first document.',
...     'This document is the second document.',
...     'And this is the third one.',
...     'Is this the first document?',
... ]
>>> vectorizer = TfidfVectorizer()
>>> X = vectorizer.fit_transform(sample)
>>> print(vectorizer.get_feature_names())
['and', 'document', 'first', 'is', 'one', 'second', 'the', 'third', 'this']
>>> print(X.shape)

"""

# Splitting the dataset into the Training set and Test set
# from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

# Fitting RVM to the Training set
from skrvm import RVC
classifier = RVC(verbose=True)
classifier.fit(X_train, y_train)

#simpan model hasil training
# with open("analisisreview.pickle", "wb") as f:
#     pickle.dump(classifier, f)

# LOAD MODEL
pickle_in = open("analisisreview.pickle", "rb")
linear = pickle.load(pickle_in)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

classifier.score(X_train,y_train)

