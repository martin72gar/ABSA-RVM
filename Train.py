
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import *

from PandasModel import PandasModel
import pandas as pd
import sys

class Train(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.btnLdDtLatih = QtWidgets.QPushButton(self.centralwidget)
        self.btnLdDtLatih.setGeometry(QtCore.QRect(450, 450, 142, 32))
        self.btnLdDtLatih.setObjectName("btnLdDtLatih")

        self.btnLdReview = QtWidgets.QPushButton(self.centralwidget)
        self.btnLdReview.setGeometry(QtCore.QRect(600, 450, 142, 32))
        self.btnLdReview.setObjectName("btnLdReview")

        self.btnProses = QtWidgets.QPushButton(self.centralwidget)
        self.btnProses.setGeometry(QtCore.QRect(600, 170, 142, 32))
        self.btnProses.setObjectName("btnProses")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(80, 150, 104, 79))
        self.textEdit.setObjectName("textEdit")

        self.labelLoaded = QtWidgets.QLabel(self.centralwidget)
        self.labelLoaded.setGeometry(QtCore.QRect(450, 490, 142, 32))
        self.labelLoaded.setObjectName("labelLoaded")

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

        self.btnLdDtLatih.clicked.connect(self.openButtonDataLatih)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnLdDtLatih.setText(_translate("MainWindow", "Load Data Latih"))
        self.btnLdReview.setText(_translate("MainWindow", "Load Review"))
        self.btnProses.setText(_translate("MainWindow", "Proses"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionBuka_Data_Latih.setText(_translate("MainWindow", "Buka Data Latih"))
        self.actionBuka_Kalimat_Review.setText(_translate("MainWindow", "Buka Kalimat Review"))


    def openDataLatih(self, data):
        data_latih = pd.read_csv(data, sep=";", encoding="ISO-8859-1")
        return data_latih

    def openButtonDataLatih(self):
        # data_latih = self.openDataLatih()
        # model = PandasModel(data_latih)
        # view = QTableView()
        # view.setModel(model)
        # view.resize(800, 600)
        # view.show()
        self.openDialogBox()

    def openDialogBox(self):
        filename = QFileDialog.getOpenFileName()
        filename = filename[0]
        self.labelLoaded.setText(filename)
        data_latih = self.openDataLatih(filename)
        model = PandasModel(data_latih)
        view = QTableView()
        view.setModel(model)
        view.resize(800, 600)
        view.show()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Train()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

