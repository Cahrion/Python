# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RadioForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(297, 428)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblulke = QtWidgets.QLabel(self.centralwidget)
        self.lblulke.setGeometry(QtCore.QRect(20, 230, 101, 21))
        self.lblulke.setText("")
        self.lblulke.setObjectName("lblulke")
        self.lblEgitim = QtWidgets.QLabel(self.centralwidget)
        self.lblEgitim.setGeometry(QtCore.QRect(160, 230, 111, 21))
        self.lblEgitim.setText("")
        self.lblEgitim.setObjectName("lblEgitim")
        self.Pulke = QtWidgets.QPushButton(self.centralwidget)
        self.Pulke.setGeometry(QtCore.QRect(20, 250, 101, 81))
        self.Pulke.setObjectName("Pulke")
        self.PEgitim = QtWidgets.QPushButton(self.centralwidget)
        self.PEgitim.setGeometry(QtCore.QRect(160, 250, 111, 81))
        self.PEgitim.setObjectName("PEgitim")
        self.UlkeGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.UlkeGroup.setGeometry(QtCore.QRect(20, 0, 101, 221))
        self.UlkeGroup.setObjectName("UlkeGroup")
        self.gridLayoutWidget = QtWidgets.QWidget(self.UlkeGroup)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 40, 82, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.GroUlk = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.GroUlk.setContentsMargins(0, 0, 0, 0)
        self.GroUlk.setObjectName("GroUlk")
        self.UTurkiye = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.UTurkiye.setObjectName("UTurkiye")
        self.GroUlk.addWidget(self.UTurkiye, 0, 0, 1, 1)
        self.UYunanistan = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.UYunanistan.setObjectName("UYunanistan")
        self.GroUlk.addWidget(self.UYunanistan, 3, 0, 1, 1)
        self.UAlmanya = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.UAlmanya.setObjectName("UAlmanya")
        self.GroUlk.addWidget(self.UAlmanya, 2, 0, 1, 1)
        self.UAzerbaycan = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.UAzerbaycan.setObjectName("UAzerbaycan")
        self.GroUlk.addWidget(self.UAzerbaycan, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.UlkeGroup)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.EgitimGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.EgitimGroup.setGeometry(QtCore.QRect(160, 0, 111, 221))
        self.EgitimGroup.setObjectName("EgitimGroup")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.EgitimGroup)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 40, 91, 161))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.EYukseklisans = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.EYukseklisans.setObjectName("EYukseklisans")
        self.gridLayout_2.addWidget(self.EYukseklisans, 3, 0, 1, 1)
        self.EUniversite = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.EUniversite.setObjectName("EUniversite")
        self.gridLayout_2.addWidget(self.EUniversite, 2, 0, 1, 1)
        self.ELise = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.ELise.setObjectName("ELise")
        self.gridLayout_2.addWidget(self.ELise, 1, 0, 1, 1)
        self.EOrtaokul = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.EOrtaokul.setObjectName("EOrtaokul")
        self.gridLayout_2.addWidget(self.EOrtaokul, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.EgitimGroup)
        self.label.setGeometry(QtCore.QRect(10, 20, 82, 15))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.LblOnayUlke = QtWidgets.QLabel(self.centralwidget)
        self.LblOnayUlke.setGeometry(QtCore.QRect(40, 340, 71, 31))
        self.LblOnayUlke.setText("")
        self.LblOnayUlke.setObjectName("LblOnayUlke")
        self.LblOnayEgitim = QtWidgets.QLabel(self.centralwidget)
        self.LblOnayEgitim.setGeometry(QtCore.QRect(180, 340, 71, 31))
        self.LblOnayEgitim.setText("")
        self.LblOnayEgitim.setObjectName("LblOnayEgitim")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 297, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Pulke.setText(_translate("MainWindow", "??lke Se??imi"))
        self.PEgitim.setText(_translate("MainWindow", "E??itim Se??imi"))
        self.UlkeGroup.setTitle(_translate("MainWindow", "??lkeler"))
        self.UTurkiye.setText(_translate("MainWindow", "T??rkiye"))
        self.UYunanistan.setText(_translate("MainWindow", "Yunanistan"))
        self.UAlmanya.setText(_translate("MainWindow", "Almanya"))
        self.UAzerbaycan.setText(_translate("MainWindow", "Azerbaycan"))
        self.label_2.setText(_translate("MainWindow", "Uyruk: "))
        self.EgitimGroup.setTitle(_translate("MainWindow", "E??itim"))
        self.EYukseklisans.setText(_translate("MainWindow", "Y??kseklisans"))
        self.EUniversite.setText(_translate("MainWindow", "??niversite"))
        self.ELise.setText(_translate("MainWindow", "Lise"))
        self.EOrtaokul.setText(_translate("MainWindow", "OrtaOkul"))
        self.label.setText(_translate("MainWindow", "E??itim durumu:"))
