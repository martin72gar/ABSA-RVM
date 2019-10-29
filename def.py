# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 17:20:17 2019

@author: Martin
"""

def stop_word(kalimat):
    from nltk.corpus import stopwords
    listStopword = set(stopwords.words("indonesian"))
    removed_sw = []
    
    for x in kalimat:
        if x not in listStopword:
            removed_sw.append(x)
    return removed_sw