import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QTextBrowser, QCheckBox, QDialogButtonBox
from PyQt5 import uic

#from X_askpinWindow import AskPinWindowClass
from X_askconfirmPIN import AskConfrimPinWindowClass

class ConfirmDialog(QDialog):
    def __init__(self, windowData):
        super(ConfirmDialog, self).__init__()
        self.windowData = windowData
        self.account = self.windowData.accountDATA
        print("FROM CONFIRMDIALOG", self.account.fname)
        Address = self.account.lothouse + ", " +self.account.barangay + ", " +self.account.citymuni + ", " +self.account.province + ", " +self.account.zipcode
        self.fullAddress = str(Address)
        print(self.fullAddress)

        uic.loadUi("ui/confirm.ui",self)

        self.fname_TB = self.findChild(QTextBrowser, "fname_TB")
        self.mname_TB = self.findChild(QTextBrowser, "mname_TB")
        self.lname_TB = self.findChild(QTextBrowser, "lname_TB")
        self.bday_TB = self.findChild(QTextBrowser, "bday_TB")
        self.lothouse_TB = self.findChild(QTextBrowser, "lothouse_TB")
        self.barangay_TB = self.findChild(QTextBrowser, "barangay_TB")
        self.citymuni_TB = self.findChild(QTextBrowser, "citymuni_TB")
        self.province_TB = self.findChild(QTextBrowser, "province_TB")
        self.zipcode_TB = self.findChild(QTextBrowser, "zipcode_TB")
        self.idtype_TB = self.findChild(QTextBrowser, "typeid_TB")
        self.idnumber = self.findChild(QTextBrowser, "idnumber_TB")
        self.email_TB = self.findChild(QTextBrowser, "email_TB")
        self.pnumber_TB = self.findChild(QTextBrowser, "phoneNum_TB")

        self.button_box = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        self.button_box = self.findChild(QDialogButtonBox, "buttonBox")

        self.button_box.accepted.connect(self.askpin)
        self.button_box.rejected.connect(self.goback)


        self.show()

    def goback(self):
        self.windowData.previousWindow.show()

    def askpin(self):
        self.windowData.previousWindow = self
        self.windowData.actions = 1
        self.ui = AskConfrimPinWindowClass(self.windowData)

    def saveAccountData(self, account):
        self.databasemanager = self.windowData.database
        #self.windowData.database = self.databasemanager
        self.databasemanager.insertData(self.account.fname, self.account.mname, self.account.lname, self.account.bday, self.fullAddress, self.account.typeofid, self.account.idnumber, self.account.email, self.account.phonenumber,"Unverified", 0.00, 0.00, self.account.pin)
        gotomenu(self)


def gotomenu(self):
    self.hide()
    from D_menuWindow import MenuWindowClass
    self.ui = MenuWindowClass(self.account.phonenumber)
