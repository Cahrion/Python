import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui


class MainForm(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()

        self.setWindowTitle('Calculator')
        self.setGeometry(200,200,500,500)
        self.initUI()
    def initUI(self):
        self.lbl_sayi1 = QtWidgets.QLabel(self)
        self.lbl_sayi1.setText('Sayı 1: ')
        self.lbl_sayi1.move(100,30)   

        self.lbl_Text1 = QtWidgets.QLineEdit(self)
        self.lbl_Text1.move(150,30)
        self.lbl_Text1.resize(150,30)
        
        self.lbl_sayi1 = QtWidgets.QLabel(self)
        self.lbl_sayi1.setText('Sayı 2: ')
        self.lbl_sayi1.move(100,80)

        self.lbl_Text2 = QtWidgets.QLineEdit(self)
        self.lbl_Text2.move(150,80)
        self.lbl_Text2.resize(150,30)

        self.lbl_button_Top = QtWidgets.QPushButton(self)
        self.lbl_button_Top.move(150,130)
        self.lbl_button_Top.resize(30,30)
        self.lbl_button_Top.setText('+')

        self.lbl_button_Cık = QtWidgets.QPushButton(self)
        self.lbl_button_Cık.move(190,130)
        self.lbl_button_Cık.resize(30,30)
        self.lbl_button_Cık.setText('-')

        self.lbl_button_Carp = QtWidgets.QPushButton(self)
        self.lbl_button_Carp.move(230,130)
        self.lbl_button_Carp.resize(30,30)
        self.lbl_button_Carp.setText('x')

        self.lbl_button_Bol = QtWidgets.QPushButton(self)
        self.lbl_button_Bol.move(270,130)
        self.lbl_button_Bol.resize(30,30)
        self.lbl_button_Bol.setText('÷')

        self.lbl_yer = QtWidgets.QLabel(self)
        self.lbl_yer.move(150,200)
        self.lbl_yer.resize(150,30)

        # self.lbl_button_Top.clicked.connect(self.clickedTop)
        # self.lbl_button_Cık.clicked.connect(self.clickedCik)
        # self.lbl_button_Carp.clicked.connect(self.clickedCarp)
        # self.lbl_button_Bol.clicked.connect(self.clickedBol)

        self.lbl_button_Top.clicked.connect(self.ClickedAll)
        self.lbl_button_Cık.clicked.connect(self.ClickedAll)
        self.lbl_button_Carp.clicked.connect(self.ClickedAll)
        self.lbl_button_Bol.clicked.connect(self.ClickedAll)


    def clickedTop(self):
        try:
            Sonuc = (int(self.lbl_Text1.text()) + int(self.lbl_Text2.text()))
            self.lbl_yer.setText(f'İşleminizin sonucu: {Sonuc}')
        except Exception:
            self.lbl_yer.setText(f'İşleminizin sonucu: Hata')
    def clickedCik(self):
        try:
            Sonuc = (int(self.lbl_Text1.text()) - int(self.lbl_Text2.text()))
            self.lbl_yer.setText(f'İşleminizin sonucu: {Sonuc}')
        except Exception:
            self.lbl_yer.setText(f'İşleminizin sonucu: Hata')
    def clickedCarp(self):
        try:
            Sonuc = (int(self.lbl_Text1.text()) * int(self.lbl_Text2.text()))
            self.lbl_yer.setText(f'İşleminizin sonucu: {Sonuc}')
        except Exception:
            self.lbl_yer.setText(f'İşleminizin sonucu: Hata')
    def clickedBol(self):
        try:
            Sonuc = (int(self.lbl_Text1.text()) / int(self.lbl_Text2.text()))
            self.lbl_yer.setText(f'İşleminizin sonucu: {Sonuc}')
        except Exception:
            self.lbl_yer.setText(f'İşleminizin sonucu: Hata')

    def ClickedAll(self):
        sender = self.sender() #}Farklı noktalarını alır ve onlara göre ayırır yani ; isim etiketini alır.
        if sender.text() == '+':
            try:
                Sonuc = (int(self.lbl_Text1.text()) + int(self.lbl_Text2.text()))
                self.lbl_yer.setText(f'İşleminizin sonucu: {Sonuc}')
            except Exception:
                self.lbl_yer.setText(f'İşleminizin sonucu: Hata')
        elif sender.text() == '-':
            try:
                Sonuc = (int(self.lbl_Text1.text()) - int(self.lbl_Text2.text()))
                self.lbl_yer.setText(f'İşleminizin sonucu: {Sonuc}')
            except Exception:
                self.lbl_yer.setText(f'İşleminizin sonucu: Hata')    
        elif sender.text() == 'x':
            try:
                Sonuc = (int(self.lbl_Text1.text()) * int(self.lbl_Text2.text()))
                self.lbl_yer.setText(f'İşleminizin sonucu: {Sonuc}')
            except Exception:
                self.lbl_yer.setText(f'İşleminizin sonucu: Hata')        
        elif sender.text() == '÷':
            try:
                Sonuc = (int(self.lbl_Text1.text()) / int(self.lbl_Text2.text()))
                self.lbl_yer.setText(f'İşleminizin sonucu: {Sonuc}')
            except Exception:
                self.lbl_yer.setText(f'İşleminizin sonucu: Hata')

def window():
    app = QtWidgets.QApplication(sys.argv)
    win = MainForm()

    win.show()
    sys.exit(app.exec_())
window()