import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QPushButton
from PyQt5 import uic

from C1_loginWindow import LoginWindowClass
from C2a_registerWindow import RegisterWindowClass

class SelectionWindowClass(QMainWindow):
    def __init__(self, windowData):
        super(SelectionWindowClass, self).__init__()
        self.windowData = windowData

        uic.loadUi("ui/selectionWindow.ui", self)

        self.login_btn = self.findChild(QPushButton, "login_btn")
        self.register_btn = self.findChild(QPushButton, "register_btn")

        self.show()

        self.login_btn.clicked.connect(lambda: login(self))
        self.register_btn.clicked.connect(lambda: register(self))


def register(self):
    self.destroy()
    self.ui = RegisterWindowClass(self.windowData)

def login(self):
    self.destroy()
    self.ui = LoginWindowClass(self.windowData)



