# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 08:17:34 2019

@author: Martin
"""

from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

factory = StopWordRemoverFactory()
stopwords = factory.get_stop_words()
print(stopwords)
stopword = factory.create_stop_word_remover()
kalimat = 'tempatnya enak buat santai pengunjung kebanyakan anak muda mudah di akses'
stop = stopword.remove(kalimat)
print(stop)

from nltk.tokenize import word_tokenize
stop = word_tokenize(stop)
