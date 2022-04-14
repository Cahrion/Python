import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui

def window():
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()


    win.setWindowTitle('First Application')
    win.setGeometry(200,200,500,500)
    win.setWindowIcon(QtGui.QIcon('icon.png'))
    win.setToolTip('My ToolTip')

    lbl_name = QtWidgets.QLabel(win)
    lbl_name.setText('Adınız: ')
    lbl_name.move(50,30)

    lbl_surname = QtWidgets.QLabel(win)
    lbl_surname.setText('Soyadınız: ')
    lbl_surname.move(50,70)

    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(150,30)

    
    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(150,70)

    def clicked(self):
        print('Butona tıklandı.')
        print(f'| Name: {txt_name.text()} | Surname: {txt_surname.text()} |')


    btn_save = QtWidgets.QPushButton(win)
    btn_save.setText('Onayla')
    btn_save.move(150,110)
    btn_save.clicked.connect(clicked)
 
    win.show()
    sys.exit(app.exec_())




window()


# QLabel
# QComboBox
# QCheckBox
# QRadioButton
# QPushButton
# QTableWidget
# QLineEdit
# QSlider
# QProgressBar