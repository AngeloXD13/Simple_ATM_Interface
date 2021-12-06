import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QWidget
from PyQt5 import uic

from utils.WindowDATA import WindowDatas
from utils.DatabaseManager import DatabaseManagerClass

class HomeWindowClass(QMainWindow):
    def __init__(self):
        super(HomeWindowClass, self).__init__()
        self.windowData = WindowDatas()
        self.databaseManager = DatabaseManagerClass()
        self.windowData.database = self.databaseManager
        uic.loadUi("ui/HomeWindow.ui", self)
        self.centralWidget1 = self.findChild(QWidget, "centralwidget")
        self.show()

    def keyPressEvent(self, event):
        print("key event")
        openSelectionWindow(self)

    def mousePressEvent(self, event):
        print("mouse event")
        openSelectionWindow(self)


def openSelectionWindow(self):
    from B_selectionWindow import SelectionWindowClass
    self.destroy()
    self.ui = SelectionWindowClass(self.windowData)


