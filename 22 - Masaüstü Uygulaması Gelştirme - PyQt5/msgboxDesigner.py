import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from Msgbox import Ui_MainWindow

class MsgBox(QtWidgets.QMainWindow):
    def __init__(self):
        super(MsgBox, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_exit.clicked.connect(self.showDialog)

    def showDialog(self):

        result = QtWidgets.QMessageBox.question(self,'Close Application', 'Are you sure?', QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Ignore,QtWidgets.QMessageBox.Ok)

        if result == QtWidgets.QMessageBox.Ok:
            print('Yes Click.')
            QtWidgets.QApp.quit()
        else:
            pass


















        # msg = QtWidgets.QMessageBox()

        # msg.setWindowTitle('Close Application')
        # msg.setText('Are you sure?')
        # # msg.setIcon(QtWidgets.QMessageBox.Question) # Soru Camı fırlatır.
        # msg.setIcon(QtWidgets.QMessageBox.Warning) # Uyarı Camı fırlatır.
        # msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Ignore)
        # msg.setDefaultButton(QtWidgets.QMessageBox.Ok) # Aktif butonu ele alınır o seçilmiş gelir.
        # msg.setDetailedText('details.... \nClosed....\n %15 \n %25 \n %40)\n %80 \n %99\n ERROR ### ')
        # msg.buttonClicked.connect(self.popup_button) # Buton hakkindaki bilgileri bize verir ve bunları kullandırır.
        # x = msg.exec_()

                    # BU bir yol.
    # def popup_button(self,i):
    #     Tex =i.text()

    #     if Tex == 'OK':
    #         print('Okey... see you than')
    #         QtWidgets.qApp.quit()
    #     elif Tex == 'Cancel':
    #         print('Canceling..')
    #     elif Tex == 'Ignore':
    #         pass










def win():
    app = QtWidgets.QApplication(sys.argv)
    win = MsgBox()

    win.show()
    sys.exit(app.exec_())

win()