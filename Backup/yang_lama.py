# PREPROSESSING
# tokenisasi, lowercase, filtering                                        <---
# import library NLTK
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
# splitting data training menjadi token per-review berdasarkan \n
# s_reviews = data_review.split("\n")
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


"""
Xtf = tf.fit_transform(corpus) // Xtf = tf.fit_transform(corpus).toarray

from sklearn.feature_extraction.text import TfidfTransformer
tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)

from sklearn.feature_extraction.text import TfidfTransformer
tf_idf = Tfidftransformer()

listToStr = ' '.join([str(elem) for elem in corpus[0:3]]

from sklearn.feature_extraction.text import TfidfVectorizer
>>> sample = [
...     'This is the first document.',
...     'This document is the second document.',
...     'And this is the third one.',
...     'Is this the first document?',
... ]
>>> vectorizer = TfidfVectorizer()
>>> X = vectorizer.fit_transform(sample)
print(vectorizer.get_feature_names())
['and', 'document', 'first', 'is', 'one', 'second', 'the', 'third', 'this']
>>> print(X.shape)

"""

"""from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=1500)
X = cv.fit_transform(corpus).toarray()
y = data_review.iloc[0:len(data_review), 1].values
"""