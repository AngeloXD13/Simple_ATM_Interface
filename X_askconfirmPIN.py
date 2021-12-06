import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QLabel, QLineEdit, QPushButton
from PyQt5 import uic

from E2b_withdrawResult import WithdrawResultWindowClass
from E1_balanceWindow import BalanceWindowClass

class AskConfrimPinWindowClass(QMainWindow):
    def __init__(self, windowData):
        super(AskConfrimPinWindowClass, self).__init__()
        self.windowData = windowData

        uic.loadUi("ui/enterPinWindowV2.ui", self)

        self.ok_btn = self.findChild(QPushButton, "ok_pushButton")
        self.cancel_btn = self.findChild(QPushButton, "cancel_pushButton")
        self.pinpass_le = self.findChild(QLineEdit, "pinpass_le")
        self.pinpass_le2 = self.findChild(QLineEdit, "pinpass_le_2")
        self.donotmatch_lbl = self.findChild(QLabel, "donotmatch_lbl")
        self.donotmatch_lbl.setHidden(True)
        self.show()

        action = self.windowData.actions
        gotoActions(self, action)

        self.pinpass_le.textChanged.connect(lambda : clearerrorLBL(self))
        self.pinpass_le2.textChanged.connect(lambda : clearerrorLBL(self))

def gotoActions(self, action):

        #if 1 from register to confirming password
        #else 2-4 from withdraw/enteramount to Result, check balance
        if action == 1:
            confirmPinPass(self) #ONLY FOR RECONFIRMING PASSWORD/PIN

def confirmPinPass(self):
    print("confirmPinPass")
   # self.donotmatch_lbl.setHidden(True)
    self.cancel_btn.setEnabled(False)
    self.ok_btn.clicked.connect(lambda: reconfirmPinPass(self))

def reconfirmPinPass(self):
    print("reconfirmPinPass")
    pinpassword = self.pinpass_le.text()
    pinpassword2 = self.pinpass_le2.text()

    print("pinpass2: ", pinpassword2, "pinpass: ",  pinpassword)

    if pinpassword2 != pinpassword:
        self.donotmatch_lbl.setHidden(False)
        confirmPinPass(self)

    else:
        self.account = self.windowData.accountDATA
        print("sendingpass: ", pinpassword2)

        self.account.pin = pinpassword2
        self.windowData.previousWindow.saveAccountData(self.account)
        self.destroy()

def clearerrorLBL(self):
    self.donotmatch_lbl.setHidden(True)
