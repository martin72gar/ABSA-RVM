# -*- coding: utf-8 -*-
"""
Created on Thu May 31 10:46:50 2018

@author: Martin
"""

def replace_contractions(text):
    """Replace contractions in string of text"""
    return contractions.fix(text)

sample = replace_contractions(sample)
print(sample)