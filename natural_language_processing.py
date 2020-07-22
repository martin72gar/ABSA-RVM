# Natural Language Processing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('D:/Python/ABSA-RVM/Dataset/train_data_500.csv', sep = ';')
#dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '')

# Cleaning the texts
import re
#import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0, 504):
    review = re.sub('[^a-zA-Z]', ' ', dataset['review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('indonesian'))]
    review = ' '.join(review)
    corpus.append(review)

# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
y = dataset['food']
z = []

for i in range(0, 504):
    if y[i] == 'positive':
        y[i] = 1
        z.append(y[i])
    else:
        y[i] = 0
        z.append(y[i])


# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, z, test_size = 0.20, random_state = 0)

# Fitting RVM
from skrvm import RVC
classifier = RVC(kernel="rbf")
classifier.fit(X_train, y_train)
classifier.score(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)