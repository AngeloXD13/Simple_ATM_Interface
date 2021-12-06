import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit

class AccountSettingsClass(QMainWindow):
    def __init__(self, windowData):
        super(AccountSettingsClass, self).__init__()

        self.windowData = windowData
        self.phoneNumber = self.windowData.accountDATA.phonenumber
        print("self.phoneNumber", self.phoneNumber)
        uic.loadUi("ui/accountSettings.ui", self)

        self.changepin_btn = self.findChild(QPushButton, "changepin_btn")
        self.convert_btn = self.findChild(QPushButton, "convert_btn")
        self.verify_Account_btn = self.findChild(QPushButton, "verify_btn")
        self.back_btn = self.findChild(QPushButton, "back_btn")

        self.changepin_btn.clicked.connect(lambda : changePin(self))
        self.back_btn.clicked.connect(lambda : menu(self))
        self.convert_btn.clicked.connect(lambda : transferholdtoavail(self))
        self.verify_Account_btn.clicked.connect(lambda: updateStatus(self))


        self.show()


def changePin(self):
    from X_askpinWindow import AskPinWindowClass
    from X_askconfirmPIN import AskConfrimPinWindowClass

    self.windowData.finalWindow = None
    self.windowData.finalWindow = self.windowData.previousWindow
    self.windowData.nextWindow = None
    self.windowData.actions = None
    self.windowData.actions = 1
    self.windowData.nextWindow = AskConfrimPinWindowClass
    self.ui = AskPinWindowClass(self.windowData)
    self.destroy()

def updateStatus(self):
    from utils.DatabaseManager import setAccountStatus
    setAccountStatus(self.phoneNumber,"Verified")
    self.windowData.accountDATA.status = "Verified"
    menu(self)

def menu(self):#refresh menu
    self.windowData.previousWindow.destroy()
    from D_menuWindow import MenuWindowClass
    self.iu = MenuWindowClass(self.phoneNumber)
    self.destroy()

def transferholdtoavail(self):
    from utils.DatabaseManager import updateAvailHoldBalance
    from utils.DatabaseManager import selectData

    account = None
    account = selectData(self.phoneNumber, 2)
    print(account)
    self.available = account.availablebalance
    self.hold = account.onholdbalance

    newavailablebalace = int(self.available) + int(self.hold)

    updateAvailHoldBalance(self.phoneNumber, 0 , newavailablebalace)
    self.available = newavailablebalace

    menu(self)
"""
app = QApplication(sys.argv)
splashscreen = AccountSettingsClass()
app.exec_()
"""