# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dating.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 372)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.StartYearTime = QtWidgets.QDateEdit(self.centralwidget)
        self.StartYearTime.setGeometry(QtCore.QRect(60, 120, 151, 71))
        self.StartYearTime.setCalendarPopup(True)
        self.StartYearTime.setObjectName("StartYearTime")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 431, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.HourTime = QtWidgets.QDateTimeEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HourTime.sizePolicy().hasHeightForWidth())
        self.HourTime.setSizePolicy(sizePolicy)
        self.HourTime.setCalendarPopup(True)
        self.HourTime.setObjectName("HourTime")
        self.horizontalLayout.addWidget(self.HourTime)
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.StopYearTime = QtWidgets.QDateEdit(self.horizontalLayoutWidget)
        self.StopYearTime.setObjectName("StopYearTime")
        self.horizontalLayout.addWidget(self.StopYearTime)
        self.PusOnay = QtWidgets.QPushButton(self.centralwidget)
        self.PusOnay.setGeometry(QtCore.QRect(70, 240, 111, 61))
        self.PusOnay.setObjectName("PusOnay")
        self.MinuteTimeForeign = QtWidgets.QTimeEdit(self.centralwidget)
        self.MinuteTimeForeign.setGeometry(QtCore.QRect(260, 120, 151, 81))
        self.MinuteTimeForeign.setObjectName("MinuteTimeForeign")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 531, 20))
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
        self.PusOnay.setText(_translate("MainWindow", "Onay"))
