import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import uic
import time, threading

class SplashScreenClass(QDialog):
    def __init__(self):
        super(SplashScreenClass, self).__init__()

        uic.loadUi("ui/splashscreen.ui", self)
        self.show()

        """
          timer = threading.Timer(2.0, self.openHomeScreen())
                timer.start()
        
        """

    def keyPressEvent(self, event):

        print("key event")
        openHomeScreen(self)

    def mousePressEvent(self, event):
        print("mouse event")
        openHomeScreen(self)

def openHomeScreen(self):
    from Ab_HomeWindow import HomeWindowClass
    self.destroy()
    self.ui = HomeWindowClass()


app = QApplication(sys.argv)
splashscreen = SplashScreenClass()
app.exec_()
