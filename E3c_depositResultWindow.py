from PyQt5 import uic
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QLabel, QPushButton, QLineEdit

from X_logoutWindow import LogoutWindowClass


class DepositResultWindowClass(QMainWindow):
    def __init__(self, windowData, amount):
        super(DepositResultWindowClass, self).__init__()
        self.windowData = windowData
        self.account = None
        self.account = self.windowData.accountDATA
        self.phoneNumber = self.account.phonenumber

        self.amount = None
        self.amount = amount
        print("amount" ,amount)
        uic.loadUi("ui/depositResult.ui", self)

        self.yes_btn = self.findChild(QPushButton, "yes_btn")
        self.no_btn = self.findChild(QPushButton, "no_btn")
        self.result_lbl = self.findChild(QLabel, "result_lbl")
        self.result_lbl2 = self.findChild(QLabel, "result_lbl_2")
        self.result_lbl3 = self.findChild(QLabel, "result_lbl_3")



        self.allcurrentbalance = None
        newHOLDbalance = None
        newCurrentBalance = None

        self.allcurrentbalance = int(self.account.onholdbalance) + int(self.account.availablebalance)
        newCurrentBalance = int(self.allcurrentbalance) + int(self.amount)
        newHOLDbalance = int(self.account.onholdbalance) + int(self.amount)
        print("allcurrent balance: ", self.allcurrentbalance)

        result = updatebalance(self,newHOLDbalance)
        if result == True:
            self.result_lbl.setText("Previous current balance: ₱" + str(self.allcurrentbalance))
            self.result_lbl2.setText("Amount will be deposited: ₱" + str(self.amount))
            self.result_lbl3.setText("New current balance: ₱" + str(newCurrentBalance))
            self.account.onholdbalance = newHOLDbalance
        else:
            self.result_lbl.setText("Deposit Transaction Failed")
            self.result_lbl2.setText("")
            self.result_lbl3.setText("Take you money in the machine and try again later")



        self.show()

        self.yes_btn.clicked.connect(lambda: menu(self))
        self.no_btn.clicked.connect(lambda: logout(self))

def editCurrentBalance():
    pass

def logout(self):
    self.destroy()
    self.ui = LogoutWindowClass(self.windowData)


def menu(self):
    self.destroy()
    self = self.windowData.previousWindow
    self.show()

def updatebalance(self , newCurrentBalance):
    from utils.DatabaseManager import updateonHoldBalance
    result = updateonHoldBalance(self.phoneNumber, newCurrentBalance)
    return result
