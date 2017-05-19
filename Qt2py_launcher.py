# -*- coding: utf-8 -*-

# Import packages
import sys, os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow

from ui.Qt2py import *
from src.fonctions import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.setFixedSize(self.size())

        self.pushButton.clicked.connect(self.get_file_path)
        self.pushButton_2.clicked.connect(self.convert_qt_2_py)

    def get_file_path(self):
        get_file_path(self)

    def convert_qt_2_py(self):
        convert_qt_2_py(self.lineEdit.text(), qtver=4)  # TODO: rewrite conversion options
        # TODO: send message after successful convert


if __name__ == "__main__":
    a = QtWidgets.QApplication(sys.argv)
    b = MainWindow()
    b.show()
    a.exec_()
