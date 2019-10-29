# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 17:19:00 2019

@author: Martin
"""

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
