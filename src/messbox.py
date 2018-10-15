from PyQt5.QtWidgets import QMessageBox
import errno
import traceback


# def displayError(e):
#     msg = QMessageBox()
#     msg.setIcon(QMessageBox.Critical)
#     msg.setStandardButtons(QMessageBox.Ok)
#     name = type(e).__name__
#     if issubclass(type(e), OSError):
#         text, info, trace = extractOSError(e)
#     else:
#         text = '\n'.join(e.args)
#         trace = '\n'.join(traceback.format_tb(e.__traceback__))
#
#     msg.setWindowTitle("Exception")
#     msg.setText(name + ' : ' + text)
#     try:
#         msg.setInformativeText(info)
#     except NameError:
#         pass
#     msg.setDetailedText(trace)
#     msg.exec_()


def displayError(name=None, errtext=None, info=None, trace=None, crit=True):
    msg = QMessageBox()
    if crit:
        msg.setIcon(QMessageBox.Critical)
    else:
        msg.setIcon(QMessageBox.Information)
    msg.setStandardButtons(QMessageBox.Ok)
    if name is not None:
        msg.setWindowTitle(name)
    else:
        msg.setWindowTitle("Exception")
    msg.setText(errtext)
    if info is not None:
        msg.setInformativeText(info)
    if trace is not None:
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
    return {'errtext': errtext,
            'info': "[Winerror {}] {}".format(winerror, strerror),
            'trace': trace}


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    a = QApplication(sys.argv)
    try:
        displayError(fds)
    except Exception as e:
        displayError(e)
