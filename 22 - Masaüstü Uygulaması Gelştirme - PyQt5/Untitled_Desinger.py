from PyQt5 import QtWidgets
import sys
from Untitled import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.ClickedAlls)

    def ClickedAlls(self):
        sender = self.sender().text() #}Farklı noktalarını alır ve onlara göre ayırır yani ; isim etiketini alır.
        if sender == '+':
            pass
        elif sender =='Kaydet':
            self.ui.progressBar.setProperty("value", 100)

# İlk Progress Bar kullanımı ve mükemmel görünüm hayran kaldım beya :D

def window():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()

    win.show()
    sys.exit(app.exec_())
window()