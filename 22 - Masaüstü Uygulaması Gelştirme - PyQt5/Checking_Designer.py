from PyQt5 import QtWidgets,QtGui
import sys 
from Checking import Ui_MainWindow

class CheckApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(CheckApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.CbSinema.stateChanged.connect(self.show_state) #Seçili 2' Seçili değilse 0
        self.ui.CbBook.stateChanged.connect(self.show_state) 
        self.ui.CbSpor.stateChanged.connect(self.show_state) 

        self.ui.btn_result_Hobi.clicked.connect(self.clickedTime)
        self.ui.btn_result_Ders.clicked.connect(self.clickedTime)

    def clickedTime(self):
        Senders = self.sender().text()
        if Senders == 'Hobileri Onayla':
            items = self.ui.groupHobiler.findChildren(QtWidgets.QCheckBox)
            result = ''
            for cb in items:
                if cb.isChecked():
                    result  = result + '\n' + ' - ' + cb.text()
            self.ui.lbl_result_Hobi.setText(f'- Seçtikleriniz - {result}')
        elif Senders == 'Dersleri Onayla':
            items = self.ui.grouDersler.findChildren(QtWidgets.QCheckBox)
            result = ''
            for cb in items:
                if cb.isChecked():
                    result  = result + '\n' + ' - ' + cb.text()
            self.ui.lbl_result_Ders.setText(f'- Seçtikleriniz - {result}')



    def show_state(self, value):
        cb = self.sender().text()
        if cb == 'Sinema':
            pass
        if cb == 'Kitap Okuma':
            pass
        if cb == 'Spor':
            pass



def window():
    app = QtWidgets.QApplication(sys.argv)
    win = CheckApp()

    win.show()
    sys.exit(app.exec_())
window()
