#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import subprocess

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
    folderPath = str(os.path.dirname(fileName))  # get path without file name
    justFileName = str(os.path.basename(fileName))  # get just file name from complete path
    command = "cd/d " + folderPath + " && pyuic5 -x " + justFileName + " -o " + justFileName[:-2] + "py"  # shell command
    # TODO: try fix for class names in ui to py files
    # FIXME: cd/d not found in linux
    os.popen(command)

#     process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=None)
# # FIXME: crash after launch process
#     # launch the shell command
#     output = process.communicate()
