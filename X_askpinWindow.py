import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QLabel, QLineEdit, QPushButton
from PyQt5 import uic

from E2b_withdrawResult import WithdrawResultWindowClass
from E1_balanceWindow import BalanceWindowClass

class AskPinWindowClass(QMainWindow):
    def __init__(self, windowData):
        super(AskPinWindowClass, self).__init__()
        self.windowData = windowData
        print("ASK WINDOW INIT")
        self.account = None
        self.account = self.windowData.accountDATA

        uic.loadUi("ui/enterPinWindow.ui", self)

        self.ok_btn = self.findChild(QPushButton, "ok_pushButton")
        self.cancel_btn = self.findChild(QPushButton, "cancel_pushButton")
        self.askpin_lbl = self.findChild(QLabel, "askpin_lbl")
        self.pinpass_le = self.findChild(QLineEdit, "pinpass_le")
        self.donotmatch_lbl = self.findChild(QLabel, "donotmatch_lbl")
        self.donotmatch_lbl.setHidden(True)
        self.show()

        pinpass = self.account.pin

        askPinPass(self,pinpass)
        self.cancel_btn.clicked.connect(lambda: gotopreviosWindow(self))


def askPinPass(self, pinpass):
    print("askpinPass")

    self.pinpass_le.setText("")
    self.ok_btn.clicked.connect(lambda: checkpass(self, pinpass))


def checkpass(self, pinpass):
    self.donotmatch_lbl.setHidden(True)
    pinpassword = self.pinpass_le.text()

    if pinpass == pinpassword:
        gotonextWindow(self)
    else:
        askPinPass(self,pinpass)
        self.donotmatch_lbl.setHidden(False)



def gotonextWindow(self):
    nextwindow = self.windowData.nextWindow
    self.ui = nextwindow(self.windowData)
    self.destroy()

def gotopreviosWindow(self):
    self.destroy()
    self = self.windowData.previousWindow
    self.show()

"""
def gotoActions(self, action):

        #else 2-4 from withdraw/enteramount to Result, check balance
        if action == 1:
            confirmPinPass(self)
        else:
            askPinPass(self, action)
           # confirmPinPass(self)




    #TODO: check for pin pass if matched
def checkPassPinDatabase(self, action):
    pass

def gotomenu(self):
    self.hide()
    from D_menuWindow import MenuWindowClass
    self.ui = MenuWindowClass()

def gotowithdawResult(self):
    self.destroy()
    self.ui = WithdrawResultWindowClass()

def gotocheckBalanceREsult(self):
    self.destroy()
    self.ui = BalanceWindowClass()


"""

