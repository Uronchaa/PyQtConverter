# -*- coding: utf-8 -*-

# Import packages
import sys, os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from ui.Qt2py import *
from src.fonctions import *
from src import messbox


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
        try:
            convert_qt_2_py(self.lineEdit.text())

        except ChildProcessError as e:
            messbox.displayError(e)
            # FIXME: error does not display correctly
        except ValueError as e:
            messbox.displayError(e)
        except OSError as e:
            messbox.displayError(e)
        except Exception:
            import traceback
            print(traceback.format_exc())

        else:
            self.messagebx()
        # FIXME: no error management!

    def messagebx(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Conversion successful")
        msg.setWindowTitle("Information")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        # TODO: custom reusable message box


if __name__ == "__main__":
    a = QtWidgets.QApplication(sys.argv)
    b = MainWindow()
    b.show()
    a.exec_()
