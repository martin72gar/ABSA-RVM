# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 14:47:23 2019

@author: Martin
"""

from nltk.corpus import stopwords

listStopword = set(stopwords.words("indonesian"))

removed_sw = []
temp = []
i = 0
while i < (len(wordss)-999):
    for x in wordss[i]:
        if x not in listStopword:
            removed_sw.append(x)
        r = removed_sw
    temp.append(r)
    print(i)
    i += 1