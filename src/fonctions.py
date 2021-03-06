#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
import subprocess
import traceback

from PyQt5.QtWidgets import QFileDialog


def get_file_path(Window):
    """
    This function is used to print the selected file path in the QLineEdit interface widget
    :param Window:
    :return: None
    """
    folderPath = os.getcwd()
    openFileName = QFileDialog.getOpenFileName(Window, 'Select file', folderPath, filter='QtFile (*.ui)')[0]
    Window.lineEdit.setText(openFileName)


def convert_qt_2_py(filepath):
    """
    This function is used to convert the selected .ui file
    :param filepath:
    :return:
    """
    fileName = str(filepath)  # get file name with path
    if fileName == "":
        raise ValueError("Field is empty")
    folderPath = str(os.path.dirname(fileName))  # get path without file name
    justFileName = str(os.path.basename(fileName))  # get just file name from complete path
    command_name = "pyuic5"
    if sys.platform == "win32":
        command_name = command_name + ".bat"
    command = [command_name, "-x", justFileName, "-o", justFileName[:-2] + "py"]
    # TODO: try fix for class names in ui to py files

    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False, cwd=folderPath)
    except OSError:
        raise
    # except Exception as e:
    #     import traceback
    #     print(traceback.format_exc())
    else:
        output, err = process.communicate()
        if process.returncode != 0:
            raise ChildProcessError(err.decode('UTF-8'))
