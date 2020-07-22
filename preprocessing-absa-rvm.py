# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 12:30:54 2019

@author: Martin
"""
# Relevance Vector Machine (SVM)
#Preprocessing

# Importing the libraries
import pandas as pd
import re, string

# Import Dataset
data_review = pd.read_csv('D:/Python/ABSA-RVM/Dataset/train_data_500.csv', sep=";", encoding="ISO-8859-1")
data_review = data_review[0:1]

#Fungsi CaseFolding
def case_folding(s):
    hasil_casefolding = s.lower()
    return hasil_casefolding

#Fungsi Filtering
def filtering(s):
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    s = regex.sub(' ', s)
    hasil_filtering = re.sub('[^a-zA-Z]', ' ', s)
    return hasil_filtering

#Fungsi Tokenization
def tokenization(s):
    hasil_token = s.split()
    return hasil_token

from nltk.corpus import stopwords
#Fungsi stopword removal                                          <--
def stopword_removal(s):
    listStopword = set(stopwords.words("indonesian"))
    hasil_stopword_rem = []
    
    for x in s:
        if x not in listStopword:
            hasil_stopword_rem.append(x)
    return hasil_stopword_rem


#Fungsi Preprocessing
def preprocessing(review):
    cf = case_folding(review)
    fl = filtering(cf)
    tk = tokenization(fl)
    sr = stopword_removal(tk)
    hasil_prepro = sr
    return hasil_prepro

