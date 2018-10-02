from PyQt5.QtWidgets import QMessageBox, QSizePolicy
from PyQt5 import QtGui
import traceback


def displayError(e):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setWindowTitle("Exception")
    msg.setText(type(e).__name__ + '\n' + '\n'.join(e.args))
    # msg.setInformativeText('\n'.join(e.args))
    msg.setDetailedText('\n'.join(traceback.format_tb(e.__traceback__)))
    msg.exec_()


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    a = QApplication(sys.argv)
    try:
        displayError(fds)
    except Exception as e:
        displayError(e)
