from PyQt5 import QtWidgets
import sys
from MainWindow import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_toplama.clicked.connect(self.ClickedAlls)
        self.ui.btn_cikarma.clicked.connect(self.ClickedAlls)
        self.ui.btn_carpma.clicked.connect(self.ClickedAlls)
        self.ui.btn_bolme.clicked.connect(self.ClickedAlls)

    def ClickedAlls(self):
        sender = self.sender().text() #}Farklı noktalarını alır ve onlara göre ayırır yani ; isim etiketini alır.
        try:
            if sender == '+':
                Sonuc = (int(self.ui.lineEdit.text()) + int(self.ui.lineEdit_2.text()))
            elif sender == '-':
                Sonuc = (int(self.ui.lineEdit.text()) - int(self.ui.lineEdit_2.text()))
            elif sender == 'x':
                Sonuc = (int(self.ui.lineEdit.text()) * int(self.ui.lineEdit_2.text()))
            elif sender == '÷':
                 Sonuc = (int(self.ui.lineEdit.text()) / int(self.ui.lineEdit_2.text()))
            self.ui.label_3.setText(f'İsleminizin sonucu: {Sonuc}')
        except Exception:
            self.ui.label_3.setText(f'İsleminizin sonucu: Hata')


def window():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()

    win.show()
    sys.exit(app.exec_())
window()

