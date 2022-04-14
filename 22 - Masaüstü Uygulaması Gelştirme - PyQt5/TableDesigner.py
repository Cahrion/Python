import sys
from PyQt5 import QtWidgets
from Table import Ui_MainWindow

class Tables(QtWidgets.QMainWindow):
    def __init__(self):
        super(Tables, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.loadProducts()
        self.ui.Onayla.clicked.connect(self.Updating)
        self.ui.TableProducts.doubleClicked.connect(self.doubleClick)

    def doubleClick(self):
        for item in self.ui.TableProducts.selectedItems():
            print(item.row(), item.column(), item.text())


    def loadProducts(self):

        products = [

            {'name': 'Samsung S5', 'price':2000},
            {'name': 'Samsung S6', 'price':3000},
            {'name': 'Samsung S7', 'price':4000},
            {'name': 'Samsung S8', 'price':5000}

        ]




        self.ui.TableProducts.setRowCount(len(products))
        self.ui.TableProducts.setColumnCount(2)
        self.ui.TableProducts.setHorizontalHeaderLabels(('Name','Price'))
        self.ui.TableProducts.setColumnWidth(0,80)
        self.ui.TableProducts.setColumnWidth(1,50)

        rowIndex = 0
        for product in products:
            self.ui.TableProducts.setItem(rowIndex,0, QtWidgets.QTableWidgetItem(product['name']))
            self.ui.TableProducts.setItem(rowIndex,1, QtWidgets.QTableWidgetItem(str(product['price'])))
            rowIndex +=1

        # self.ui.TableProducts.setItem(0,0, QtWidgets.QTableWidgetItem('Samsung S5'))
        # self.ui.TableProducts.setItem(0,1, QtWidgets.QTableWidgetItem('2000'))
        # # (1) Bölüm satır (1,2) Bölüm Sutun (1,2,3) Bölüm Cümle.
        # self.ui.TableProducts.setItem(1,0, QtWidgets.QTableWidgetItem('Samsung S6'))
        # self.ui.TableProducts.setItem(1,1, QtWidgets.QTableWidgetItem('3000'))
        # self.ui.TableProducts.setItem(2,0, QtWidgets.QTableWidgetItem('Samsung S7'))
        # self.ui.TableProducts.setItem(2,1, QtWidgets.QTableWidgetItem('4000'))
        # self.ui.TableProducts.setItem(3,0, QtWidgets.QTableWidgetItem('Samsung S8'))
        # self.ui.TableProducts.setItem(3,1, QtWidgets.QTableWidgetItem('5000'))

    def Updating(self):
        Names = self.ui.EditName.text()
        Prices = self.ui.EditPrice.text()
        if Names and Prices is not None:
            Rows = self.ui.TableProducts.rowCount() + 1
            self.ui.TableProducts.setRowCount(Rows)
            print(Names + Prices)
            print(Rows)
            self.ui.TableProducts.setItem(Rows-1,0, QtWidgets.QTableWidgetItem(Names))
            self.ui.TableProducts.setItem(Rows-1,1, QtWidgets.QTableWidgetItem(Prices))
            self.ui.lbl_Durum.setText('✅ Başarıyla onaylandı.')
        else:
            self.ui.lbl_Durum.setText('❌ Lütfen Belli \nalanları boş bırakmayınız.')

        

def window():
    app = QtWidgets.QApplication(sys.argv)
    win = Tables()

    win.show()
    sys.exit(app.exec_())

window()