from PyQt5 import uic
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton

from X_logoutWindow import LogoutWindowClass

class BalanceWindowClass(QMainWindow):
    def __init__(self, windowData):
        super(BalanceWindowClass, self).__init__()
        self.windowData = windowData
        print("Balance window INIT")
        self.account = None
        self.account = self.windowData.accountDATA

        uic.loadUi("ui/balanceWindow.ui", self)

        self.yes_btn = self.findChild(QPushButton, "yes_btn")
        self.no_btn = self.findChild(QPushButton, "no_btn")
        self.availbalance_lbl = self.findChild(QLabel, "availbal_lbl")
        self.currentbalance_lbl = self.findChild(QLabel, "currentbal_lbl")

        self.allcurrentbalance = int(self.account.onholdbalance) + int(self.account.availablebalance)
        self.availbalance_lbl.setText("₱ "+ str(self.account.availablebalance))
        self.currentbalance_lbl.setText("₱ "+ str(self.allcurrentbalance))


        self.yes_btn.clicked.connect(lambda : menu(self))
        self.no_btn.clicked.connect(lambda : logout(self))
        self.show()

def logout(self):
    self.destroy()
    self.ui = LogoutWindowClass(self.windowData)


def menu(self):
    self.destroy()
    self = self.windowData.previousWindow
    self.show()
