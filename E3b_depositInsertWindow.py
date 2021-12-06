from PyQt5 import uic
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QLabel, QPushButton

from X_enterAmountDialog import EnterAmountDialogClass
class DepositInsertWindowClass(QDialog):
    def __init__(self, windowData):
        super(DepositInsertWindowClass, self).__init__()
        self.windowData = windowData

        uic.loadUi("ui/depositPage2.ui", self)

        self.show()

    def keyPressEvent(self, event):
        print("key event")
        openaskAmountwindow(self)

    def mousePressEvent(self, event):
        print("mouse event")
        openaskAmountwindow(self)

def openaskAmountwindow(self):
    self.ui = EnterAmountDialogClass(self.windowData)
    self.destroy()