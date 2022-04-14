import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from ComboBoxCitys import Ui_MainWindow

class ComboX(QtWidgets.QMainWindow):
    def __init__(self):
        super(ComboX, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # combo = self.ui.CbBox
        # List = ['Edirne','Bursa']
        # combo.addItem('Ankara')
        # combo.addItem('Adana')
        # combo.addItem('İstanbul')
        # combo.addItems(List) #Coğul bir liste alınır

        self.ui.btnLoadItem.clicked.connect(self.LoadItems)
        self.ui.btnGetItem.clicked.connect(self.GetItems)
        self.ui.btnClearItems.clicked.connect(self.GetingClears)

        # self.ui.CbBox.currentIndexChanged.connect(self.selectedChangedIndex) # Eğer eklenmezse sayısı gelir.
        # self.ui.CbBox.currentIndexChanged[str].connect(self.selectedChangedText) # Str eklenirse text bilgisi


    def LoadItems(self):
        Sehirler = ['Edirne','Bursa','Rize','İstanbul','Adana']
        combo = self.ui.CbBox
        combo.addItems(Sehirler)

    def GetItems(self):
        Names = self.ui.CbBox.currentText()
        Count = self.ui.CbBox.count()
        self.ui.lbl_one.setText(f'{Count}/1 Seçilen: {Names} ✔')
    def GetingClears(self):
        self.ui.CbBox.clear()# Temizleme uygulaması Direkt Cleardir.




    def selectedChangedIndex(self, index):
        print(index)
    def selectedChangedText(self, text):
        print(text)


def win():
    app = QtWidgets.QApplication(sys.argv)
    win = ComboX()

    win.show()
    sys.exit(app.exec_())

win()