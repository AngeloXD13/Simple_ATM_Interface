from PyQt5 import uic
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
from utils.AccountDATA import Account

class LogoutWindowClass(QMainWindow):
    def __init__(self, windowData):
        super(LogoutWindowClass, self).__init__()
        self.windowData = windowData
        uic.loadUi("ui/logoutWindow.ui", self)
        #DELETE ALL DATA
        del self.windowData.accountDATA
        self.show()

    def keyPressEvent(self, event):
        print("key event")
        openHomeWindow(self)

    def mousePressEvent(self, event):
        print("mouse event")
        openHomeWindow(self)

def openHomeWindow(self):
    from Ab_HomeWindow import HomeWindowClass
    self.destroy()
    self.ui = HomeWindowClass()