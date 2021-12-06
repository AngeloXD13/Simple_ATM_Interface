from PyQt5 import uic
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton

from X_logoutWindow import LogoutWindowClass

class WithdrawResultWindowClass(QMainWindow):
    def __init__(self, windowData, amount):
        super(WithdrawResultWindowClass, self).__init__()
        self.windowData = windowData
        self.account = None
        self.account = self.windowData.accountDATA
        self.phoneNumber = self.account.phonenumber

        self.amount = None
        self.amount = amount
        print("amount", amount)

        uic.loadUi("ui/WithdrawResultWindow.ui", self)

        self.yes_btn = self.findChild(QPushButton, "yes_btn")
        self.no_btn = self.findChild(QPushButton, "no_btn")
        self.resultTitle_lbl = self.findChild(QLabel, "resultTitle_lbl")
        self.result_lbl = self.findChild(QLabel, "result_lbl")
        self.result_lbl2 = self.findChild(QLabel, "result_lbl_2")
        self.result_lbl3 = self.findChild(QLabel, "result_lbl_3")

        self.show()

        self.yes_btn.clicked.connect(lambda: menu(self))
        self.no_btn.clicked.connect(lambda : logout(self))
        getcheckAvailablebalance(self)

def getcheckAvailablebalance(self):
    #get updated available balance
    from utils.DatabaseManager import selectData
    account = selectData(self.account.phonenumber, 2)
    self.available = account.availablebalance
    #if amount above availabe balance FAILED if not SUCCESS then update database
    print("self.available: ", self.available)
    print("self.amount: ", self.amount)
    if int(self.amount) <= int(self.available):
        successAndUpdatadatabse(self)
    else:
        failedAndCancel(self, "Insufficient Balance")
def successAndUpdatadatabse(self):
    print("successAndUpdatadatabse")
    newavailableBalance = int(self.available) - int(self.amount)
    from utils.DatabaseManager import updateAvailBalance
    result = updateAvailBalance(self.account.phonenumber, newavailableBalance)
    if result == True:
        self.result_lbl.setText("Previous Available Balance: "+ str("₱ {:,.2f}".format(int(self.available))))
        self.result_lbl2.setText("Amount you Withdraw: " + str("₱ {:,.2f}".format(int(self.amount))))
        self.result_lbl3.setText("New Available Balance: " + str("₱ {:,.2f}".format(int(newavailableBalance))))
        self.account.availablebalance = newavailableBalance
    else:
        failedAndCancel(self, "Database Error")


def failedAndCancel(self, reason):
    print("failedAndCancel")

    self.resultTitle_lbl.setText("CANCELED")
    if reason == "Database Error":
        self.result_lbl.setText("Database Error")
        self.result_lbl2.setText("Please Try Again Later...")
        self.result_lbl3.setText("Transaction Cancelled")
    else:
        self.result_lbl.setText("Insufficient Balance")
        self.result_lbl2.setText("Previous Available Balance: "+ str("₱ {:,.2f}".format(int(self.available))))
        self.result_lbl3.setText("Transaction Cancelled")

def logout(self):
    self.ui = LogoutWindowClass(self.windowData)
    self.destroy()

def menu(self):
    self.destroy()
    self = self.windowData.previousWindow
    self.show()
