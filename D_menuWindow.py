from PyQt5 import uic
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton

from E2a_withdrawWindow import WithdrawWindowClass
from E3a_depositWindow import DepositWindowClass
from X_logoutWindow import LogoutWindowClass
from X_askpinWindow import AskPinWindowClass

from utils.WindowDATA import WindowDatas
from utils.DatabaseManager import DatabaseManagerClass

class MenuWindowClass(QMainWindow):
    def __init__(self, phonenumber):
        super(MenuWindowClass, self).__init__()
        self.windowData = WindowDatas()
        from utils.DatabaseManager import selectData
        self.windowData.accountDATA = None
        self.windowData.accountDATA = selectData(phonenumber, 2)
        self.account = None
        self.account = self.windowData.accountDATA
        print("GET FRESH VALUE FOR DATABASE")
        print("MemuWindow: " ,self.account.fname)

        uic.loadUi("ui/menuWindow.ui", self)

        self.withdraw_btn = self.findChild(QPushButton, "withdraw_btn")
        self.deposit_btn = self.findChild(QPushButton, "deposit_btn")
        self.checkBalance_btn = self.findChild(QPushButton, "checkbalance_btn")
        self.accountSettings_btn = self.findChild(QPushButton, "accountsettings_btn")
        self.logout_btn = self.findChild(QPushButton, "logout_btn")
        self.name_lbl = self.findChild(QLabel, "name_lbl")
        self.accStatus_lbl = self.findChild(QLabel, "accountstatus_lbl")

        self.name_lbl.setText(self.account.fname)
        self.accStatus_lbl.setText(self.account.status)

        self.withdraw_btn.clicked.connect(lambda: withdraw(self))
        self.deposit_btn.clicked.connect(lambda : deposit(self))
        self.logout_btn.clicked.connect(lambda : logout(self))
        self.checkBalance_btn.clicked.connect(lambda : checkbalance(self))
        self.accountSettings_btn.clicked.connect(lambda : openAccountSettings(self))
        self.show()

    def saveAccountData(self, account):
        from utils.DatabaseManager import updatePinPassword
        updatePinPassword(account.phonenumber, account.pin)
        self.show()


def withdraw(self):
    from E2b_withdrawResult import WithdrawResultWindowClass
    from X_confirmAmountDialog import ConfirmAmountDialogClass

    self.windowData.nextWindow = None
    self.windowData.nextWindow = ConfirmAmountDialogClass
    self.windowData.previousWindow = None
    self.windowData.previousWindow = self
    self.windowData.finalWindow = None
    self.windowData.finalWindow = WithdrawResultWindowClass
    self.ui = WithdrawWindowClass(self.windowData)
    self.hide()


def deposit(self):
    from E3c_depositResultWindow import DepositResultWindowClass
    from X_confirmAmountDialog import ConfirmAmountDialogClass

    self.windowData.finalWindow = None
    self.windowData.finalWindow = DepositResultWindowClass
    self.windowData.nextWindow = None
    self.windowData.nextWindow = ConfirmAmountDialogClass
    self.windowData.previousWindow = None
    self.windowData.previousWindow = self
    self.ui = DepositWindowClass(self.windowData)
    self.hide()

def logout(self):
    self.ui = None
    self.ui = LogoutWindowClass(self.windowData)
    self.destroy()

def checkbalance(self):
    from E1_balanceWindow import BalanceWindowClass
    self.windowData.nextWindow = None
    self.windowData.nextWindow = BalanceWindowClass
    self.windowData.previousWindow = None
    self.windowData.previousWindow = self
    self.ui = AskPinWindowClass(self.windowData)
    self.hide()

def openAccountSettings(self):
    from AccountSettings import AccountSettingsClass
    self.windowData.previousWindow = None
    self.windowData.previousWindow = self
    self.ui = AccountSettingsClass(self.windowData)
    self.hide()

##SAve pin pass

