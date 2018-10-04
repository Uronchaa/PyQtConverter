from PyQt5.QtWidgets import QMessageBox, QSizePolicy
import errno
import traceback


def displayError(e):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setStandardButtons(QMessageBox.Ok)
    name = type(e).__name__
    if issubclass(type(e), OSError):
        text, info, trace = extractOSError(e)
    else:
        text = '\n'.join(e.args)
        trace = '\n'.join(traceback.format_tb(e.__traceback__))

    msg.setWindowTitle("Exception")
    msg.setText(name + ' : ' + text)
    try:
        msg.setInformativeText(info)
    except NameError:
        pass
    msg.setDetailedText(trace)
    msg.exec_()


def extractOSError(e):
    trace = '\n'.join(traceback.format_tb(e.__traceback__))
    errnum = e.errno
    strerror = e.strerror
    winerror = e.winerror
    if errnum == errno.EINVAL:
        errtext = "Invalid Argument"
    elif errnum == errno.ENOTDIR:
        errtext = "Not a directory"

    else:
        errtext = "Unrecognised Error"
    return errtext, "[Winerror {}] {}".format(winerror, strerror), trace


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    a = QApplication(sys.argv)
    try:
        displayError(fds)
    except Exception as e:
        displayError(e)
