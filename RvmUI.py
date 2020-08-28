# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

import re
import pickle

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

import pandas as pd

class RvmUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 678)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pBtnLoadData = QtWidgets.QPushButton(self.centralwidget)
        self.pBtnLoadData.setGeometry(QtCore.QRect(20, 600, 250, 32))
        self.pBtnLoadData.setObjectName("pBtnLoadData")

        self.pBtnLoadReview = QtWidgets.QPushButton(self.centralwidget)
        self.pBtnLoadReview.setGeometry(QtCore.QRect(280, 600, 250, 32))
        self.pBtnLoadReview.setObjectName("pBtnLoadReview")

        self.pBtnProses = QtWidgets.QPushButton(self.centralwidget)
        self.pBtnProses.setGeometry(QtCore.QRect(530, 600, 250, 32))
        self.pBtnProses.setObjectName("pBtnProses")

        self.tableWRaw = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWRaw.setGeometry(QtCore.QRect(30, 20, 750, 141))
        self.tableWRaw.setObjectName("tableWRaw")
        self.tableWRaw.setColumnCount(6)
        self.tableWRaw.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWRaw.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWRaw.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWRaw.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWRaw.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWRaw.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWRaw.setHorizontalHeaderItem(5, item)

        self.tableWPrepro = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWPrepro.setGeometry(QtCore.QRect(30, 180, 750, 161))
        self.tableWPrepro.setObjectName("tableWPrepro")
        self.tableWPrepro.setColumnCount(6)
        self.tableWPrepro.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWPrepro.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWPrepro.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWPrepro.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWPrepro.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWPrepro.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWPrepro.setHorizontalHeaderItem(5, item)

        self.tableWClassify = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWClassify.setGeometry(QtCore.QRect(30, 360, 750, 201))
        self.tableWClassify.setObjectName("tableWClassify")
        self.tableWClassify.setColumnCount(6)
        self.tableWClassify.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWClassify.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWClassify.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWClassify.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWClassify.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWClassify.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWClassify.setHorizontalHeaderItem(5, item)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 0, 60, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 160, 131, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 340, 111, 16))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(560, 570, 60, 16))
        self.label_4.setObjectName("label_4")

        self.labelHasilAkurasi = QtWidgets.QLabel(self.centralwidget)
        self.labelHasilAkurasi.setGeometry(QtCore.QRect(630, 570, 60, 16))
        self.labelHasilAkurasi.setObjectName("labelHasilAkurasi")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBuka_Data_Latih = QtWidgets.QAction(MainWindow)
        self.actionBuka_Data_Latih.setObjectName("actionBuka_Data_Latih")
        self.actionBuka_Kalimat_Review = QtWidgets.QAction(MainWindow)
        self.actionBuka_Kalimat_Review.setObjectName("actionBuka_Kalimat_Review")
        self.menuFile.addAction(self.actionBuka_Data_Latih)
        self.menuFile.addAction(self.actionBuka_Kalimat_Review)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pBtnLoadData.setText(_translate("MainWindow", "Load Data Latih"))
        self.pBtnLoadReview.setText(_translate("MainWindow", "Load Review"))
        self.pBtnProses.setText(_translate("MainWindow", "Proses"))
        item = self.tableWRaw.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Kalimat Review"))
        item = self.tableWRaw.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Food"))
        item = self.tableWRaw.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Service"))
        item = self.tableWRaw.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWRaw.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Place"))
        item = self.tableWRaw.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Other"))
        item = self.tableWPrepro.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Kalimat Review"))
        item = self.tableWPrepro.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Food"))
        item = self.tableWPrepro.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Service"))
        item = self.tableWPrepro.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWPrepro.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Place"))
        item = self.tableWPrepro.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Other"))
        item = self.tableWClassify.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Kalimat Review"))
        item = self.tableWClassify.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Food"))
        item = self.tableWClassify.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Service"))
        item = self.tableWClassify.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWClassify.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Place"))
        item = self.tableWClassify.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Other"))
        self.label.setText(_translate("MainWindow", "Data Raw"))
        self.label_2.setText(_translate("MainWindow", "Hasil Preprosesing"))
        self.label_3.setText(_translate("MainWindow", "Hasil Klasifikasi"))
        self.label_4.setText(_translate("MainWindow", "Akurasi : "))
        self.labelHasilAkurasi.setText(_translate("MainWindow", "0 %"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionBuka_Data_Latih.setText(_translate("MainWindow", "Buka Data Latih"))
        self.actionBuka_Kalimat_Review.setText(_translate("MainWindow", "Buka Kalimat Review"))

        self.pBtnLoadData.clicked.connect(self.openDataLatih)
        self.pBtnProses.clicked.connect(self.prosesRVM)

    def openDataLatih(self):
        data_latih = pd.read_csv('Dataset/train_data.csv', sep=";", encoding="ISO-8859-1")
        # return data_latih
        row = len(data_latih)
        self.tableWRaw.setColumnCount(6)
        self.tableWRaw.setRowCount(row)
        columnHeaders = ['Kalimat Review', 'Food', 'Service', 'Price', 'Place', 'Others']
        self.tableWRaw.setHorizontalHeaderLabels(columnHeaders)
        #tampilkan ke table
        list_review = []
        for i in range(row):
            list_review.append([data_latih["review"][i],
                                data_latih["food"][i],
                                data_latih["service"][i],
                                data_latih["price"][i],
                                data_latih["place"][i],
                                data_latih["other"][i]])
            self.addRow(i, list_review[i])


    def addRow(self, row, itemLabels=[]):
        for i in range(0, 6):
            item = QTableWidgetItem()
            item.setText(str(itemLabels[i]))
            self.tableWRaw.setItem(row, i, item)

    def preprocessing(self):
        data_review = pd.read_csv('Dataset/train_data.csv', sep=";", encoding="ISO-8859-1")
        corpus = []
        for i in range(len(data_review)):
            review = re.sub('[^a-zA-Z]', ' ', data_review['review'][i])
            review = review.lower()
            review = review.split()
            ps = PorterStemmer()
            review = [ps.stem(word) for word in review if not word in set(stopwords.words('indonesian'))]
            review = ' '.join(review)
            corpus.append(review)

        row = len(corpus)
        self.tableWPrepro.setColumnCount(1)
        self.tableWPrepro.setRowCount(row)
        columnHeaders = ['Kalimat Review']
        self.tableWPrepro.setHorizontalHeaderLabels(columnHeaders)
        #tampilkan ke table
        for i in range(row):
            item = QTableWidgetItem()
            item.setText(str(corpus[i]))
            self.tableWPrepro.setItem(i,0,item)

    def pembobotanTfIdf(self, data_review=[], corpus=[]):
        tf = TfidfVectorizer(max_features=500)
        X = tf.fit_transform(corpus).toarray()
        y = data_review.iloc[0:len(data_review), 1].values
        return

    def prosesRVM(self):
        self.preprocessing()
        # Preprosesing
        data_review = pd.read_csv('Dataset/train_data.csv', sep=";", encoding="ISO-8859-1")
        data_review = data_review[0:200]

        corpus = []
        for i in range(len(data_review)):
            review = re.sub('[^a-zA-Z]', ' ', data_review['review'][i])
            review = review.lower()
            review = review.split()
            ps = PorterStemmer()
            review = [ps.stem(word) for word in review if not word in set(stopwords.words('indonesian'))]
            review = ' '.join(review)
            corpus.append(review)

        # Pembobotan TFIDF
        from sklearn.feature_extraction.text import TfidfVectorizer
        tf = TfidfVectorizer(max_features=500)
        X = tf.fit_transform(corpus).toarray()
        # ambil nilai target food
        ''' Target Negative(0) vs All(Positive(1) dan Netral(1))'''
        yfood1 = data_review.iloc[0:len(data_review), 1].values
        # for i in range(len(yfood1)):
        #     if (yfood1[i] == 'negative'):
        #         yfood1[i] = '0'
        #     else:
        #         yfood1[i] = '1'

        ''' Target Positive(1) vs All(Negative(2) dan Netral(2))'''
        yfood2 = data_review.iloc[0:len(data_review), 1].values
        # for i in range(len(yfood2)):
        #     if (yfood2[i] == 'positive'):
        #         yfood2[i] = '1'
        #     else:
        #         yfood2[i] = '2'

        ''' Target Netral(2) vs All(Negative(0) dan Netral(0))'''
        yfood3 = data_review.iloc[0:len(data_review), 1].values
        # for i in range(len(yfood3)):
        #     if (yfood3[i] != 'positive' and 'negative'):
        #         yfood3[i] = '2'
        #     else:
        #         yfood3[i] = '0'

        # Splitting the dataset into the Training set and Test set
        from sklearn.model_selection import train_test_split
        ''' Target Negative(0) vs All(Positive(1) dan Netral(1))'''
        X_train1, X_test1, y_train1, y_test1 = train_test_split(X, yfood1, test_size=0.20, random_state=0)
        ''' Target Positive(1) vs All(Negative(2) dan Netral(2))'''
        X_train2, X_test2, y_train2, y_test2 = train_test_split(X, yfood2, test_size=0.20, random_state=0)
        ''' Target Netral(2) vs All(Negative(0) dan Netral(0))'''
        X_train3, X_test3, y_train3, y_test3 = train_test_split(X, yfood3, test_size=0.20, random_state=0)


        # Fitting RVM to the Training set
        from skrvm import RVC
        # classifier1 = RVC(verbose=True)
        # classifier1.fit(X_train1, y_train1)
        #
        # classifier2 = RVC(verbose=True)
        # classifier2.fit(X_train2, y_train2)
        #
        # classifier3 = RVC(verbose=True)
        # classifier3.fit(X_train3, y_train3)

        # Simpan model hasil training
        # with open("model200targetyfood1new.pickle", "wb") as f:
        #     pickle.dump(classifier1, f)
        # with open("model200targetyfood2new.pickle", "wb") as f:
        #     pickle.dump(classifier2, f)
        # with open("model200targetyfood3new.pickle", "wb") as f:
        #     pickle.dump(classifier3, f)

        # LOAD MODEL
        pickle_in = open("model200targetyfood1new.pickle", "rb")
        classifier1 = pickle.load(pickle_in)
        pickle_in = open("model200targetyfood2new.pickle", "rb")
        classifier2 = pickle.load(pickle_in)
        pickle_in = open("model200targetyfood3new.pickle", "rb")
        classifier3 = pickle.load(pickle_in)

        # Predicting the Test set results
        y_predict1 = classifier1.predict(X_test1)
        y_predict2 = classifier2.predict(X_test2)
        y_predict3 = classifier3.predict(X_test3)

        # Making the Confusion Matrix
        from sklearn.metrics import confusion_matrix
        cm1 = confusion_matrix(y_test1, y_predict1)
        cm2 = confusion_matrix(y_test2, y_predict2)
        cm3 = confusion_matrix(y_test3, y_predict3)

        akurasi1 = classifier1.score(X_train1, y_train1)
        akurasi2 = classifier2.score(X_train2, y_train2)
        akurasi3 = classifier3.score(X_train3, y_train3)

        self.labelHasilAkurasi.setText(str(akurasi1))

        row = len(corpus)
        self.tableWPrepro.setColumnCount(1)
        self.tableWPrepro.setRowCount(row)
        columnHeaders = ['Kalimat Review']
        self.tableWClassify.setHorizontalHeaderLabels(columnHeaders)
        # tampilkan ke table
        for i in range(row):
            item = QTableWidgetItem()
            item.setText(str(corpus[i]))
            self.tableWClassify.setItem(i, 0, item)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = RvmUI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

