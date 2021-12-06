from PyQt5 import uic
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QLabel, QPushButton, QLineEdit, QTextBrowser

class ConfirmAmountDialogClass(QDialog):
    def __init__(self, windowData, amount, previousWindow):
        super(ConfirmAmountDialogClass, self).__init__()
        self.windowData = windowData
        self.amount = amount
        uic.loadUi("ui/ConfirmAmount.ui", self)

        self.no_btn = self.findChild(QPushButton, "no_btn")
        self.yes_btn = self.findChild(QPushButton, "yes_btn")
        self.amount_tb = self.findChild(QTextBrowser, "amount_tb")
        self.amount_tb.setText("₱ {:,.2f}".format(int(self.amount)))
        self.amount_tb.setAlignment(QtCore.Qt.AlignCenter)
        self.scenario1_lbl = self.findChild(QLabel, "scenario1_lbl")
        self.scenario2_lbl = self.findChild(QLabel, "scenario2_lbl")
        self.show()

        layoutsetter(self)
        self.yes_btn.clicked.connect(lambda :gotofinalWindow(self))
        self.no_btn.clicked.connect(lambda : gotoEnterAmountWindow(self, previousWindow))

def layoutsetter(self):
    import E2b_withdrawResult
    print(self.windowData.finalWindow)
    finalWindow = self.windowData.finalWindow
    print(finalWindow)
    print("LAYOUT SETTER")
    if finalWindow == E2b_withdrawResult.WithdrawResultWindowClass:
        print("WITHDRAW")
        self.scenario1_lbl.setText("Is this the correct amount you withdraw in the ATM?")
        self.scenario2_lbl.setText("*By clicking 'YES' you will proceed to withdraw your available balance in your account")

def gotofinalWindow(self):
    finalwindow = self.windowData.finalWindow
    self.ui = finalwindow(self.windowData, self.amount)
    self.destroy()

def gotoEnterAmountWindow(self, previousWindow):
    previousWindow.show()
    self.destroy()