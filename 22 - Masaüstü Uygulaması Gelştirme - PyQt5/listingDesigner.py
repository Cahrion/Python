import sys
from PyQt5 import QtWidgets
from listing import Ui_MainWindow


class Listim(QtWidgets.QMainWindow):
    def __init__(self):
        super(Listim, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Load Students
        self.loadStudents()

        # add New Student
        self.ui.Buton_Add.clicked.connect(self.addStudent)

        # edit student
        self.ui.Buton_Edit.clicked.connect(self.editStudent)
        # Delete Student
        self.ui.Buton_Remove.clicked.connect(self.DeleteStudent)

        # Up
        self.ui.Buton_Up.clicked.connect(self.UpStudent)
        # Down

        self.ui.Buton_Down.clicked.connect(self.DownStudent)
        # Sort
        self.ui.Buton_Sort.clicked.connect(self.SortingStudent)
        # Exit
        self.ui.Buton_Exit.clicked.connect(self.Exiting)

    def loadStudents(self):
        self.ui.listItems.addItems(['Ahmet','Ali','Çınar'])
        self.ui.listItems.setCurrentRow(0)

    def addStudent(self):
        currentIndex = self.ui.listItems.currentRow() # Seçili alanın index numarasını alır.
        T1, ok = QtWidgets.QInputDialog.getText(self, 'New Student','Student Name') #Bir dosya firlatip orada yazım işlerini halletme metodu.
        if ok and T1 is not None:
            self.ui.listItems.insertItem(currentIndex, T1) #Ekleme metodu.

    def editStudent(self):
        currentIndex = self.ui.listItems.currentRow()
        item = self.ui.listItems.item(currentIndex)
        if item is not None:
            T1, ok = QtWidgets.QInputDialog.getText(self, 'Edit Student','Student Name', QtWidgets.QLineEdit.Normal, item.text())
            if T1 and ok is not None:
                item.setText(T1)
    
    def DeleteStudent(self):
        currentIndex = self.ui.listItems.currentRow()
        item = self.ui.listItems.item(currentIndex)
        if currentIndex is not None:
            rslt = QtWidgets.QMessageBox.question(self,'Remove Student',('Do you want to remove student ?\nName: ' + item.text()), QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
            if rslt == QtWidgets.QMessageBox.Yes:
                item = self.ui.listItems.takeItem(currentIndex)
                del item

    def UpStudent(self):
        index = self.ui.listItems.currentRow()
        if index > 0:
            item = self.ui.listItems.takeItem(index)
            self.ui.listItems.insertItem(index-1, item)
            self.ui.listItems.setCurrentItem(item)

    def DownStudent(self):
        index = self.ui.listItems.currentRow()
        if index < self.ui.listItems.count() - 1:
            item = self.ui.listItems.takeItem(index)
            self.ui.listItems.insertItem(index + 1, item)
            self.ui.listItems.setCurrentItem(item)
    def SortingStudent(self):
        self.ui.listItems.sortItems()

    def Exiting(self):
        rslt = QtWidgets.QMessageBox.question(self,'Exit',('Çıkmak istediğinize emin misiniz ?'), QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel, QtWidgets.QMessageBox.Ok)
        if rslt == QtWidgets.QMessageBox.Ok:
            QtWidgets.qApp.quit()
def win():
    app = QtWidgets.QApplication(sys.argv)
    win = Listim()

    win.show()
    sys.exit(app.exec())

win()