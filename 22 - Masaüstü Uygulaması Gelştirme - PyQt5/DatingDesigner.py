import sys
from PyQt5 import QtWidgets
from Dating import Ui_MainWindow
from PyQt5 import QtCore
class Datetim(QtWidgets.QMainWindow):
    def __init__(self):
        super(Datetim, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.PusOnay.clicked.connect(self.TimerTime)
    
    def TimerTime(self):
        start = self.ui.StartYearTime.date() 
        stop = self.ui.StopYearTime.date()

        print('Days in month: {0}'.format(start.daysInMonth()))
        print('Days in Year: {0}'.format(start.daysInYear()))

        print('Total Days: {0}'.format(start.daysTo(stop))) # İçteki bilgiyi ilkden çıkarır ve başlangıçtan çıkarır.

        now = QtCore.QDate.currentDate() #x Şimdiki zamanı ele alır.
        print('Total Days from now: {0}'.format(start.daysTo(now))) 


def win():
    app = QtWidgets.QApplication(sys.argv)
    win = Datetim()

    win.show()
    sys.exit(app.exec_())
win()