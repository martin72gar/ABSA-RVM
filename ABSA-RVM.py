# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 23:20:53 2019

@author: Martin
"""
#open file    
f = open("D:/Python/ABSA-RVM/Dataset/train_data.csv","r")
if f.mode == 'r':
    reviews = f.read()
f.close()

#PREPROSESSING
#tokenisasi, lowercase, filtering                                        <---
#import library NLTK
import nltk
from nltk.corpus import stopwords

# function stopword removal                                          <--
def stopword_removal(text):
    listStopword = set(stopwords.words("indonesian"))
    removed_sw = []
    
    for x in text:
        if x not in listStopword:
            removed_sw.append(x)
    return removed_sw
    
# word normalization
character = ['a','b','c','d','e','f','g','h','i','j','k','l',
             'm','n','o','p','q','r','s','t','u','v','w','x','y','z']                                        
def word_normalization(text):
		for i in range(len(character)):
			charac_long = 3
			while charac_long>=2:
				char = character[i]*charac_long 
				text = text.replace(char,character[i])
				charac_long -= 1
		return text

#splitting data training menjadi token per-review berdasarkan \n
s_reviews = reviews.split("\n")
wordss = [] #variabel penampung hasil casefolding(lower) dan filtering
for r in s_reviews:
    #token setiap kata pada setiap baris review
    r = nltk.word_tokenize(r)
    words = [w.lower() 
                for w in r
                  if w.isalpha()]
    #words1 = word_normalization(words)
    words2 = stopword_removal(words)
    #words = [word for word in words if word!=[]]
    wordss.append(words2)



    
    

#pembobotan TF-I



# Pelatihan RVM


# Model Pengklasifikasi

#    
