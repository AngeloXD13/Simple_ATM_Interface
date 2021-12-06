import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QPushButton, QLabel, QLineEdit
from PyQt5 import uic

from D_menuWindow import MenuWindowClass
from utils.AccountDATA import Account

class LoginWindowClass(QMainWindow):
    def __init__(self, windowData):
        super(LoginWindowClass, self).__init__()
        self.windowData = windowData
        self.database = self.windowData.database
        self.windowData.accountDATA = None


        uic.loadUi("ui/loginWindow.ui", self)

        self.phoneNumber_TE = self.findChild(QTextEdit, "phonenumber_TE")
        self.pinpass_LE = self.findChild(QLineEdit, "password_le")
        self.login_btn = self.findChild(QPushButton, "login_btn")
        self.cancel_btn = self.findChild(QPushButton, "cancel_btn")
        self.error_lbl = self.findChild(QLabel, "error_lbl")
        self.error_lbl.setHidden(True)
        self.show()

        button(self)
def button(self):
    self.login_btn.clicked.connect(lambda: getCredentials(self))
    self.cancel_btn.clicked.connect(lambda: gotobackselection(self))

def getCredentials(self):
    self.phonenumber = None
    self.pinpass = None
    self.phonenumber = self.phoneNumber_TE.toPlainText()
    self.pinpass = self.pinpass_LE.text()
    print("Entered: ", self.phonenumber,self.pinpass)
    try: self.login_btn.clicked.disconnect()
    except TypeError:
        pass
    checkdatabase(self)

def checkdatabase(self):
    try:
        from utils.DatabaseManager import selectData
      #  account = Account()
     #   del account
        account = None
        account = selectData(self.phonenumber, 1)
        print(account)
        if account == False:
            self.error_lbl.setHidden(False)
            button(self)
        print(account.pin, self.pinpass )
        if account.pin == self.pinpass:
            login(self, self.phonenumber)
        else:
            self.error_lbl.setHidden(False)
            button(self)

        print("deleting propcedure")
        account = None
        account.pin = None
        del account
        del self.pinpass
    except:
        self.error_lbl.setHidden(False)
        button(self)

def login(self, phonenumber):
    print("def login")
    self.destroy()
    self.ui = MenuWindowClass(phonenumber)

def gotobackselection(self):
    from Ab_HomeWindow import HomeWindowClass
    self.destroy()
    self.ui = HomeWindowClass()
