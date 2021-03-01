# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\NSCC\Copy\PROG1700_SourceCode\w0425052-MamunA\GUI\Final Project\Test_1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWIndow(object):
    def setupUi(self, MainWIndow):
        MainWIndow.setObjectName("MainWIndow")
        MainWIndow.resize(1037, 867)
        self.centralwidget = QtWidgets.QWidget(MainWIndow)
        self.centralwidget.setObjectName("centralwidget")
        self.listChooseCountry = QtWidgets.QListWidget(self.centralwidget)
        self.listChooseCountry.setGeometry(QtCore.QRect(70, 150, 361, 541))
        self.listChooseCountry.setObjectName("listChooseCountry")
        self.labelChooseACountry = QtWidgets.QLabel(self.centralwidget)
        self.labelChooseACountry.setGeometry(QtCore.QRect(70, 60, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelChooseACountry.setFont(font)
        self.labelChooseACountry.setObjectName("labelChooseACountry")
        MainWIndow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWIndow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1037, 21))
        self.menubar.setObjectName("menubar")
        self.menuCountries_of_the_World = QtWidgets.QMenu(self.menubar)
        self.menuCountries_of_the_World.setObjectName("menuCountries_of_the_World")
        MainWIndow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWIndow)
        self.statusbar.setObjectName("statusbar")
        MainWIndow.setStatusBar(self.statusbar)
        self.actionLoad_Countries = QtWidgets.QAction(MainWIndow)
        self.actionLoad_Countries.setObjectName("actionLoad_Countries")
        self.actionSave_to_File = QtWidgets.QAction(MainWIndow)
        self.actionSave_to_File.setCheckable(False)
        self.actionSave_to_File.setEnabled(False)
        self.actionSave_to_File.setObjectName("actionSave_to_File")
        self.actionExit = QtWidgets.QAction(MainWIndow)
        self.actionExit.setObjectName("actionExit")
        self.menuCountries_of_the_World.addAction(self.actionLoad_Countries)
        self.menuCountries_of_the_World.addAction(self.actionSave_to_File)
        self.menuCountries_of_the_World.addAction(self.actionExit)
        self.menubar.addAction(self.menuCountries_of_the_World.menuAction())

        self.retranslateUi(MainWIndow)
        QtCore.QMetaObject.connectSlotsByName(MainWIndow)

    def retranslateUi(self, MainWIndow):
        _translate = QtCore.QCoreApplication.translate
        MainWIndow.setWindowTitle(_translate("MainWIndow", "MainWindow"))
        self.labelChooseACountry.setText(_translate("MainWIndow", "Choose a country from the list: "))
        self.menuCountries_of_the_World.setTitle(_translate("MainWIndow", "File"))
        self.actionLoad_Countries.setText(_translate("MainWIndow", "Load Countries"))
        self.actionSave_to_File.setText(_translate("MainWIndow", "Save to File"))
        self.actionExit.setText(_translate("MainWIndow", "Exit"))
