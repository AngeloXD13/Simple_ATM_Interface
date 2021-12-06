from PyQt5 import uic
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton

from X_enterAmountDialog import EnterAmountDialogClass

class WithdrawWindowClass(QMainWindow):
    def __init__(self, windowData):
        super(WithdrawWindowClass, self).__init__()


        self.windowData = windowData
        self.status = self.windowData.accountDATA.status

        uic.loadUi("ui/WithdrawPage.ui", self)

        self.scenario_lbl = self.findChild(QLabel, "scenario_lbl")

        checkStatus(self)
        self.show()

    def keyPressEvent(self, event):
        print("key event")
        gotonextwindow(self)
    def mousePressEvent(self, event):
        print("mouse event")
        gotonextwindow(self)

def checkStatus(self):
    if self.status == "Unverified":
        self.scenario_lbl.setText("In able to withdraw, please go to the nearest bank in able to VERIFY your account. Thank you...")
    else:
        self.scenario_lbl.setText("The minimum withdraw is 500")

def gotonextwindow(self):
    if self.status == "Unverified":
        goback(self)
    else:
        openEnterAmountWindow(self)

def openEnterAmountWindow(self):
    self.ui = EnterAmountDialogClass(self.windowData)
    self.destroy()
def goback(self):

    self.windowData.previousWindow.show()
    self.destroy()