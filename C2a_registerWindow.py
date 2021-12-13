from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QPlainTextEdit, QTextEdit, QPushButton, QDateEdit, QComboBox
from PyQt5 import uic

from C2b_confirm import ConfirmDialog
from utils.AccountDATA import Account

newAccount = Account()

class RegisterWindowClass(QMainWindow):
    def __init__(self, windowData):
        super(RegisterWindowClass, self).__init__()
        self.windowData = windowData

        # load the ui file
        uic.loadUi("ui/registerWindow.ui", self)

        # define our widgets
        self.check_btn = self.findChild(QPushButton, "check_btn")
        self.submit_btn = self.findChild(QPushButton, "submit_btn")
        self.cancel_btn = self.findChild(QPushButton, "cancel_btn")
        self.submit_btn.setEnabled(False)

        self.submit_btn.setStyleSheet('color: rgb(255, 255, 255);\nbackground-color:rgb(8, 30, 81);')  # false

        self.status_lbl = self.findChild(QLabel, "status_lbl")
        self.status_lbl.setText("Press check to submit")
        self.error_lbl = self.findChild(QLabel, "error_lbl")
        self.error_lbl.setHidden(True)
        self.fname_TE = self.findChild(QPlainTextEdit, "fname_TE")
        self.mname_TE = self.findChild(QPlainTextEdit, "mname_TE")
        self.lname_TE = self.findChild(QTextEdit, "lname_TE")

        self.bday_DE = self.findChild(QDateEdit, "bday_DE")
        self.bday_DE.setMaximumDate(QtCore.QDate(2100, 12, 28))
        self.bday_DE.setMaximumTime(QtCore.QTime(1900, 59, 59))
        self.bday_DE.setCalendarPopup(True)

        self.lothouse_TE = self.findChild(QPlainTextEdit, "lothouse_TE")
        self.barangay_TE = self.findChild(QTextEdit, "barangay_TE")
        self.citymuni_TE = self.findChild(QTextEdit, "citymuni_TE")
        self.province_TE = self.findChild(QPlainTextEdit, "province_TE")
        self.zipcode_TE = self.findChild(QPlainTextEdit, "zipcode_TE")

        self.idtype_CB = self.findChild(QComboBox, "idtype_CB")
        self.idnumber = self.findChild(QPlainTextEdit, "idnumber_TE")

        self.email_TE = self.findChild(QPlainTextEdit, "email_TE")
        self.pnumber_TE = self.findChild(QPlainTextEdit, "pnumber_TE")

        # Do something button
        self.check_btn.clicked.connect(self.check)
        self.cancel_btn.clicked.connect(self.cancel)
        self.submit_btn.clicked.connect(lambda : checkDatabase(self))

        # show the app

        self.show()



    def destroyWindow(self):
        self.destroy()

    def cancel(self):
        from Ab_HomeWindow import HomeWindowClass
        self.destroy()
        self.ui = HomeWindowClass()

    def check(self):
        self.status_lbl.setText("Checking")

        fname = str(self.fname_TE.toPlainText())
        print(fname)
        mname = str(self.mname_TE.toPlainText())
        print(mname)
        lname = str(self.lname_TE.toPlainText())
        print(lname)
        bday = str(self.bday_DE.date().toPyDate())
        print(bday)
        houselot = str(self.lothouse_TE.toPlainText())
        print(houselot)
        barangay = str(self.barangay_TE.toPlainText())
        print(barangay)
        citymuni = str(self.citymuni_TE.toPlainText())
        print(citymuni)
        province = str(self.province_TE.toPlainText())
        print(province)
        zipcode = str(self.zipcode_TE.toPlainText())
        print(zipcode)
        idtype = str(self.idtype_CB.currentText())
        print(idtype)
        idnumber = str(self.idnumber.toPlainText())
        print(idnumber)
        email = str(self.email_TE.toPlainText())
        print(email)
        phonenumber = str(self.pnumber_TE.toPlainText())
        print(phonenumber)

        if fname == "":
            self.status_lbl.setText("First Name field is empty")
        elif mname == "":
            self.status_lbl.setText("Middle Name field is empty")
        elif lname == "":
            self.status_lbl.setText("Last Name field is empty")
        elif houselot == "":
            self.status_lbl.setText("House and Lot field is empty")
        elif barangay == "":
            self.status_lbl.setText("Barangay field is empty")
        elif citymuni == "":
            self.status_lbl.setText("City/Municipality field is empty")
        elif province == "":
            self.status_lbl.setText("Province field is empty")
        elif zipcode == "":
            self.status_lbl.setText("ZipCode field is empty")
        elif idtype == "Select your id---":
            self.status_lbl.setText("Select your ID")
        elif idnumber == "":
            self.status_lbl.setText("ID Number field is empty")
        elif email == "":
            self.status_lbl.setText("Email field is empty")
        elif phonenumber == "":
            self.status_lbl.setText("ID Number field is empty")
        else:
            self.status_lbl.setText("OK")
            self.submit_btn.setEnabled(True)
            self.submit_btn.setStyleSheet('color: rgb(255, 255, 255);\nbackground-color: rgb(24, 93, 255);')  # true



def checkDatabase(self):
    from utils.DatabaseManager import selectData
    isExiting = selectData(self.pnumber_TE.toPlainText(), 3)
    if isExiting == True:
        self.error_lbl.setHidden(False)
    else:
        self.error_lbl.setHidden(True)
        openWindow(self)

def openWindow(self):
    self.hide()
    self.newAccount = getValues(self)
    self.windowData.previousWindow = self
    self.windowData.accountDATA = self.newAccount
    self.ui = ConfirmDialog(self.windowData)

    print("FROM OPEN WINDOW",newAccount.fname)
    print("FROM WINDOWDATA", self.windowData.accountDATA.fname)

    self.ui.fname_TB.setText(newAccount.fname)
    self.ui.mname_TB.setText(newAccount.mname)
    self.ui.lname_TB.setText(newAccount.lname)
    self.ui.bday_TB.setText(str(newAccount.bday))
    self.ui.lothouse_TB.setText(newAccount.lothouse)
    self.ui.barangay_TB.setText(newAccount.barangay)
    self.ui.citymuni_TB.setText(newAccount.citymuni)
    self.ui.province_TB.setText(newAccount.province)
    self.ui.zipcode_TB.setText(newAccount.zipcode)
    self.ui.idtype_TB.setText(newAccount.typeofid)
    self.ui.idnumber_TB.setText(newAccount.idnumber)
    self.ui.email_TB.setText(newAccount.email)
    self.ui.pnumber_TB.setText(newAccount.phonenumber)

def getValues(self):

    fname = self.fname_TE.toPlainText()
    print("FROM TE",fname)
    newAccount.fname = fname
    print("FROM MODEL",newAccount.fname)

    mname = self.mname_TE.toPlainText()
    print(mname)
    newAccount.mname = mname

    lname = self.lname_TE.toPlainText()
    print(lname)
    newAccount.lname = lname

    bday = self.bday_DE.date().toPyDate()
    print(bday)
    newAccount.bday = bday

    houselot = self.lothouse_TE.toPlainText()
    print(houselot)
    newAccount.lothouse = houselot

    barangay = self.barangay_TE.toPlainText()
    print(barangay)
    newAccount.barangay = barangay

    citymuni = self.citymuni_TE.toPlainText()
    print(citymuni)
    newAccount.citymuni = citymuni

    province = self.province_TE.toPlainText()
    print(province)
    newAccount.province = province

    zipcode = self.zipcode_TE.toPlainText()
    print(zipcode)
    newAccount.zipcode = zipcode

    idtype = self.idtype_CB.currentText()
    print(idtype)
    newAccount.typeofid = idtype

    idnumber = self.idnumber.toPlainText()
    print(idnumber)
    newAccount.idnumber = idnumber

    email = self.email_TE.toPlainText()
    print(email)
    newAccount.email = email

    phonenumber = self.pnumber_TE.toPlainText()
    print(phonenumber)
    newAccount.phonenumber = phonenumber

    return newAccount

