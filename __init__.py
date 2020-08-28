import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from Train import Train
from RvmUI import RvmUI

if __name__ == '__main__':
   a = QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow()
   form = RvmUI()
   form.setupUi(MainWindow)
   MainWindow.show()
   a.exec_()