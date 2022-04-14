from PyQt5 import QtWidgets
from PyQt5 import QtGui
from RadioForm import Ui_MainWindow
import sys

class RadioClass(QtWidgets.QMainWindow):
    def __init__(self):
        super(RadioClass, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.UTurkiye.setChecked(True) #Otomatik seçim ypar setChecked. kodu.
        self.ui.ELise.setChecked(True)

        self.ui.UTurkiye.toggled.connect(self.ClickedTime)
        self.ui.UAzerbaycan.toggled.connect(self.ClickedTime)
        self.ui.UAlmanya.toggled.connect(self.ClickedTime)
        self.ui.UYunanistan.toggled.connect(self.ClickedTime)

        self.ui.ELise.toggled.connect(self.ClickedTimes)
        self.ui.EUniversite.toggled.connect(self.ClickedTimes)
        self.ui.EOrtaokul.toggled.connect(self.ClickedTimes)
        self.ui.EYukseklisans.toggled.connect(self.ClickedTimes)

        self.ui.Pulke.clicked.connect(self.PushSelecting)
        self.ui.PEgitim.clicked.connect(self.PushSelecting)

    def ClickedTime(self):
        send = self.sender().text()

        self.ui.lblulke.setText(f'Şuanda: {send}')

    def ClickedTimes(self):
        send = self.sender().text()

        self.ui.lblEgitim.setText(f'Şuanda: {send}')

    def PushSelecting(self):
        senders = self.sender().text()
        if senders == 'Ülke Seçimi':
            items = self.ui.UlkeGroup.findChildren(QtWidgets.QRadioButton)
            for rb in items:
                if rb.isChecked():
                    self.ui.LblOnayUlke.setText(f'✅ {rb.text()} ')
        else:
            items = self.ui.EgitimGroup.findChildren(QtWidgets.QRadioButton)
            for rb in items:
                if rb.isChecked():
                    self.ui.LblOnayEgitim.setText(f'✅ {rb.text()} ')


def win():
    app = QtWidgets.QApplication(sys.argv)
    win = RadioClass()


    win.show()
    sys.exit(app.exec_())

win()