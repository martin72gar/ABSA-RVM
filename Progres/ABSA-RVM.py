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
s_reviews = s_reviews[1:5]
i = 0
sr = []
while i < len(s_reviews):
    review = s_reviews[i].split(";")
    sre = review[0]
    sr.append(sre)
    i += 1
s_reviews = sr
s_reviews
 
wordss = [] #variabel penampung hasil casefolding(lower) dan filtering
for rv in s_reviews:
    #token setiap kata pada setiap baris review
    rv = nltk.word_tokenize(rv)
    words = [w.lower() 
                for w in rv
                  if w.isalpha()]
    #words1 = word_normalization(words)
    words2 = stopword_removal(words)
    #words = [word for word in words if word!=[]]
    wordss.append(words2)


#membuat BagOfWords
bow = []
for kata in wordss:
    bow.extend(kata)
  
bow = set(bow)

#pembobotan TF-IDF
#TF
i = 0
wordDict = []
while i < len(wordss):
    wordDict.append(dict.fromkeys(bow, 0))#membuat dict, variabel untuk menampung tf
    i += 1
    
wD = []
i = 0
while i < len(wordss):
    for word in wordss[i]:
        wd = wordDict[i]
        if word in wd:
            wd[word]+=1
    wD.append(wd)
    i +=1
    
#IDF
df = 0
i=0
while i < len(wD):
    
    for word in bow:
        tk = wD[i]
        if tk[word] != 0:
            df = 1
        df += df
        print('DF ',word,':', tk[word],'di dokumen -',i)
    i+=1
    


   
import math
tfReview1 = wD[0]
tf = tfReview1["cantik"]
df = 1
idf = math.log10(len(wordss)/df)
    
bobot = tf * idf
print("Bobot Term 'cantik' :",bobot)    
# Pelatihan RVM
# Model Pengklasifikasi

#    
