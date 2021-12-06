from PyQt5 import uic
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton

from E3b_depositInsertWindow import DepositInsertWindowClass

class DepositWindowClass(QMainWindow):
    def __init__(self, windowData):
        super(DepositWindowClass, self).__init__()
        self.windowData = windowData

        uic.loadUi("ui/depositPage.ui", self)

        self.show()

    def keyPressEvent(self, event):
        print("key event")
        openDeposit2window(self)

    def mousePressEvent(self, event):
        print("mouse event")
        openDeposit2window(self)

def openDeposit2window(self):
    self.ui = DepositInsertWindowClass(self.windowData)
    self.destroy()
