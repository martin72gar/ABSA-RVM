# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 23:20:53 2019

@author: Martin
"""
# Relevance Vector Machine (SVM)

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import Dataset
dataset_review = pd.read_csv('D:/Python/ABSA-RVM/Dataset/train_data.csv',encoding = "ISO-8859-1")

# Cleaning kolom review pada dataset
import re
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0, 84):
    review = re.sub('[^a-zA-Z]', ' ', dataset_review['review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('indonesian'))]
    review = ' '.join(review)
    corpus.append(review)

# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
y = dataset_review.iloc[0:84, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Fitting RVM to the Training set
from skrvm import RVC
classifier = RVC(kernel="rbf")
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

#PREPROSESSING
#tokenisasi, lowercase, filtering                                        <---
#import library NLTK
# =============================================================================
# import nltk
# from nltk.corpus import stopwords
# 
# # function stopword removal                                          <--
# def stopword_removal(text):
#     listStopword = set(stopwords.words("indonesian"))
#     removed_sw = []
#     
#     for x in text:
#         if x not in listStopword:
#             removed_sw.append(x)
#   return removed_sw
# =============================================================================
   
# word normalization
# =============================================================================
# character = ['a','b','c','d','e','f','g','h','i','j','k','l',
#              'm','n','o','p','q','r','s','t','u','v','w','x','y','z']                                        
# def word_normalization(text):
# 		for i in range(len(character)):
# 			charac_long = 3
# 			while charac_long>=2:
# 				char = character[i]*charac_long 
# 				text = text.replace(char,character[i])
# 				charac_long -= 1
# 		return text
# 
# =============================================================================
#splitting data training menjadi token per-review berdasarkan \n
#s_reviews = data_review.split("\n")
# =============================================================================
# wordss = [] #variabel penampung hasil casefolding(lower) dan filtering
# for r in s_reviews:
#     #token setiap kata pada setiap baris review
#     r = nltk.word_tokenize(r)
#     words = [w.lower() 
#                 for w in r
#                   if w.isalpha()]
#     #words1 = word_normalization(words)
#     words2 = stopword_removal(words)
#     #words = [word for word in words if word!=[]]
#     wordss.append(words2)
# =============================================================================


# Splitting the dataset into the Training set and Test set
# =============================================================================
# from sklearn.cross_validation import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
# 
# # Feature Scaling
# from sklearn.preprocessing import StandardScaler
# sc = StandardScaler()
# X_train = sc.fit_transform(X_train)
# X_test = sc.transform(X_test)
# =============================================================================

# Pembobotan TF-IDF



# Pelatihan RVM


# Model Pengklasifikasi

#    
