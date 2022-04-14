import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui


# Üstte olanlar bir birlerinin içindeki dosyaları almak için dosyalar arasında yaptıgımız gezinti

def window():
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()

    win.setWindowTitle('First Application')
    win.setGeometry(200,200,500,500)
    win.setWindowIcon(QtGui.QIcon('icon.png'))
    win.setToolTip('My ToolTip')

    win.show()
    sys.exit(app.exec_())

window()