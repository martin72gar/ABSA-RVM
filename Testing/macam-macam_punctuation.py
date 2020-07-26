# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 12:56:54 2019

@author: Martin
"""

import re, string, timeit

s = "string. With. Punctuation h4lo 123 (hello), you can't do that"
exclude = set(string.punctuation)
#table = string.maketrans("","")

regex = re.compile('[%s]' % re.escape(string.punctuation))

def test_set(s):
    return ''.join(ch for ch in s if ch not in exclude)

def test_re(s):  # From Vinko's solution, with fix.
    punct = regex.sub('', s)
    return punct

text = test_re(s)
text = str(text)
text
re.sub('[^a-zA-Z]', ' ', s)
#def test_trans(s):
#    return s.translate(table, string.punctuation)

def test_repl(s):  # From S.Lott's solution
    for c in string.punctuation:
        s=s.replace(c,"")
    return s

print("sets      :",timeit.Timer('f(s)', 'from __main__ import s,test_set as f').timeit(1000000))
print("regex     :",timeit.Timer('f(s)', 'from __main__ import s,test_re as f').timeit(1000000))
#print("translate :",timeit.Timer('f(s)', 'from __main__ import s,test_trans as f').timeit(1000000))
print("replace   :",timeit.Timer('f(s)', 'from __main__ import s,test_repl as f').timeit(1000000))