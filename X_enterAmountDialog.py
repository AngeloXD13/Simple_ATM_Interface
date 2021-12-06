from PyQt5 import uic
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QLabel, QPushButton, QLineEdit

from X_askpinWindow import AskPinWindowClass
from E3c_depositResultWindow import DepositResultWindowClass
class EnterAmountDialogClass(QDialog):
    def __init__(self, windowData):
        super(EnterAmountDialogClass, self).__init__()
        self.windowData = windowData

        uic.loadUi("ui/EnterAmountDialog.ui", self)

        self.confirm_btn = self.findChild(QPushButton, "confirm_btn")
        self.cancel_btn = self.findChild(QPushButton, "cancel_btn")
        self.amount_le = self.findChild(QLineEdit, "amount_LE")
        self.status_lbl = self.findChild(QLabel, "status_lbl")

        self.cancel_btn.clicked.connect(lambda : gotopreviosWindow(self))
        askAmount(self)
        self.show()

def askAmount(self):
    print("askamount")
    self.confirm_btn.clicked.connect(lambda : getAmount(self))

def getAmount(self):
    self.amount = None
    self.amount = self.amount_le.text()
    print("enterned amount: ", self.amount)
    if self.amount == "":
        self.status_lbl.setText("Enter Amount")
        askAmount(self)
    if int(self.amount) < 500:
        self.status_lbl.setText("Below Minimum Amount")
        askAmount(self)
    if int(self.amount) <= 0 or int(self.amount) > 999999:
        self.status_lbl.setText("Invalid Amount")
        askAmount(self)
    else: gotonextWindow(self)


def gotonextWindow(self): #goto confirm amount
    nextwindow = None
    nextwindow = self.windowData.nextWindow
    self.ui = nextwindow(self.windowData, self.amount, self)
    self.hide()

def gotopreviosWindow(self):
    self.destroy()
    self = self.windowData.previousWindow
    self.show()
