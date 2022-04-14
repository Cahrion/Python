import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui

class Color(QtWidgets.QWidget):
    def __init__(self,color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(color))
        self.setPalette(palette)

# Üsteki Color Classı bir bütün colorları alabilmemiz için ekstra ve asbit bir box kutucugudur.

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100,100,500,500)
        """
                # layout = QtWidgets.QVBoxLayout() # Kutucular açar Önde (V) olması dikey box açılıyor
                        # Vertical = Dikey (V)
                
                layout = QtWidgets.QHBoxLayout() # Kutucuklar açar ve (H) olması yatay açıyor.
                        # Horizontal = Yatay (H)

                layout.addWidget(Color('red'))
                layout.addWidget(Color('blue'))
                layout.addWidget(Color('green'))
                layout.addWidget(Color('yellow'))
        """

        hlayout1 = QtWidgets.QHBoxLayout()

        hlayout1.addWidget(Color('red'))
        hlayout1.addWidget(Color('blue'))
        hlayout1.addWidget(Color('green'))
        # hlayout1.setContentsMargins(50,0,0,0) # sol, üst, sağ, alt
        hlayout1.setSpacing(50) # Aralık ekler birbiriyle .

        hlayout2 = QtWidgets.QHBoxLayout()

        hlayout2.addWidget(Color('red'))
        hlayout2.addWidget(Color('green'))
        hlayout2.setSpacing(50)


        vlayout = QtWidgets.QVBoxLayout()
        vlayout.addLayout(hlayout1)
        vlayout.addLayout(hlayout2)



        # layout = QtWidgets.QGridLayout()

        # layout.addWidget(Color('red'),0,0)
        # layout.addWidget(Color('yellow'),1,0)
        # layout.addWidget(Color('green'),0,2)
        # layout.addWidget(Color('blue'),3,3)



        widget = QtWidgets.QWidget()
        widget.setLayout(vlayout)

        self.setCentralWidget(widget)


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

app()