# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\NSCC\Copy\PROG1700_SourceCode\w0425052-MamunA\GUI\FinalProject_Draft - Copy\FinalProject_1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 863)
        self.centralwidgetCountries = QtWidgets.QWidget(MainWindow)
        self.centralwidgetCountries.setObjectName("centralwidgetCountries")
        self.listDisplayCountries = QtWidgets.QListWidget(self.centralwidgetCountries)
        self.listDisplayCountries.setGeometry(QtCore.QRect(60, 130, 351, 571))
        self.listDisplayCountries.setObjectName("listDisplayCountries")
        self.labelChiooseCountries = QtWidgets.QLabel(self.centralwidgetCountries)
        self.labelChiooseCountries.setGeometry(QtCore.QRect(60, 70, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.labelChiooseCountries.setFont(font)
        self.labelChiooseCountries.setObjectName("labelChiooseCountries")
        self.frameDisplay = QtWidgets.QFrame(self.centralwidgetCountries)
        self.frameDisplay.setGeometry(QtCore.QRect(440, 20, 671, 731))
        self.frameDisplay.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameDisplay.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameDisplay.setObjectName("frameDisplay")
        self.lineEditCountryName = QtWidgets.QLineEdit(self.frameDisplay)
        self.lineEditCountryName.setGeometry(QtCore.QRect(180, 30, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditCountryName.setFont(font)
        self.lineEditCountryName.setObjectName("lineEditCountryName")
        self.labelFlag = QtWidgets.QLabel(self.frameDisplay)
        self.labelFlag.setGeometry(QtCore.QRect(150, 110, 301, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelFlag.setFont(font)
        self.labelFlag.setText("")
        self.labelFlag.setObjectName("labelFlag")
        self.lineEditPopulation = QtWidgets.QLineEdit(self.frameDisplay)
        self.lineEditPopulation.setGeometry(QtCore.QRect(298, 286, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditPopulation.setFont(font)
        self.lineEditPopulation.setObjectName("lineEditPopulation")
        self.pushButtonUpdatePopulation = QtWidgets.QPushButton(self.frameDisplay)
        self.pushButtonUpdatePopulation.setGeometry(QtCore.QRect(338, 326, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonUpdatePopulation.setFont(font)
        self.pushButtonUpdatePopulation.setObjectName("pushButtonUpdatePopulation")
        self.labelPopulation = QtWidgets.QLabel(self.frameDisplay)
        self.labelPopulation.setGeometry(QtCore.QRect(98, 286, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelPopulation.setFont(font)
        self.labelPopulation.setObjectName("labelPopulation")
        self.labelDisplayTotalArea = QtWidgets.QLabel(self.frameDisplay)
        self.labelDisplayTotalArea.setGeometry(QtCore.QRect(400, 419, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelDisplayTotalArea.setFont(font)
        self.labelDisplayTotalArea.setText("")
        self.labelDisplayTotalArea.setObjectName("labelDisplayTotalArea")
        self.comboBoxTotalArea = QtWidgets.QComboBox(self.frameDisplay)
        self.comboBoxTotalArea.setGeometry(QtCore.QRect(260, 419, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBoxTotalArea.setFont(font)
        self.comboBoxTotalArea.setObjectName("comboBoxTotalArea")
        self.labelTotalArea = QtWidgets.QLabel(self.frameDisplay)
        self.labelTotalArea.setGeometry(QtCore.QRect(100, 429, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelTotalArea.setFont(font)
        self.labelTotalArea.setObjectName("labelTotalArea")
        self.groupBoxPopulation = QtWidgets.QGroupBox(self.frameDisplay)
        self.groupBoxPopulation.setGeometry(QtCore.QRect(90, 500, 431, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxPopulation.setFont(font)
        self.groupBoxPopulation.setObjectName("groupBoxPopulation")
        self.radioButtonSquareMile = QtWidgets.QRadioButton(self.groupBoxPopulation)
        self.radioButtonSquareMile.setGeometry(QtCore.QRect(10, 20, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButtonSquareMile.setFont(font)
        self.radioButtonSquareMile.setChecked(True)
        self.radioButtonSquareMile.setObjectName("radioButtonSquareMile")
        self.radioButtonSquareKM = QtWidgets.QRadioButton(self.groupBoxPopulation)
        self.radioButtonSquareKM.setGeometry(QtCore.QRect(10, 50, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButtonSquareKM.setFont(font)
        self.radioButtonSquareKM.setObjectName("radioButtonSquareKM")
        self.labelDisplayDensity = QtWidgets.QLabel(self.groupBoxPopulation)
        self.labelDisplayDensity.setGeometry(QtCore.QRect(310, 40, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelDisplayDensity.setFont(font)
        self.labelDisplayDensity.setText("")
        self.labelDisplayDensity.setObjectName("labelDisplayDensity")
        self.labelPercentageOfPopulation = QtWidgets.QLabel(self.frameDisplay)
        self.labelPercentageOfPopulation.setGeometry(QtCore.QRect(420, 614, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelPercentageOfPopulation.setFont(font)
        self.labelPercentageOfPopulation.setText("")
        self.labelPercentageOfPopulation.setObjectName("labelPercentageOfPopulation")
        self.labelPopulationPer = QtWidgets.QLabel(self.frameDisplay)
        self.labelPopulationPer.setGeometry(QtCore.QRect(100, 624, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelPopulationPer.setFont(font)
        self.labelPopulationPer.setObjectName("labelPopulationPer")
        MainWindow.setCentralWidget(self.centralwidgetCountries)
        self.menubarCountries = QtWidgets.QMenuBar(MainWindow)
        self.menubarCountries.setGeometry(QtCore.QRect(0, 0, 1124, 21))
        self.menubarCountries.setObjectName("menubarCountries")
        self.menuFileCountries = QtWidgets.QMenu(self.menubarCountries)
        self.menuFileCountries.setObjectName("menuFileCountries")
        MainWindow.setMenuBar(self.menubarCountries)
        self.statusbarCountries = QtWidgets.QStatusBar(MainWindow)
        self.statusbarCountries.setObjectName("statusbarCountries")
        MainWindow.setStatusBar(self.statusbarCountries)
        self.actionLoad_Countries = QtWidgets.QAction(MainWindow)
        self.actionLoad_Countries.setObjectName("actionLoad_Countries")
        self.actionSave_To_File = QtWidgets.QAction(MainWindow)
        self.actionSave_To_File.setEnabled(False)
        self.actionSave_To_File.setObjectName("actionSave_To_File")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFileCountries.addAction(self.actionLoad_Countries)
        self.menuFileCountries.addAction(self.actionSave_To_File)
        self.menuFileCountries.addAction(self.actionExit)
        self.menubarCountries.addAction(self.menuFileCountries.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Countries of the World"))
        self.labelChiooseCountries.setText(_translate("MainWindow", "Choose a country from the list:"))
        self.pushButtonUpdatePopulation.setText(_translate("MainWindow", "Update Population"))
        self.labelPopulation.setText(_translate("MainWindow", "Population: "))
        self.labelTotalArea.setText(_translate("MainWindow", "Total Area in"))
        self.groupBoxPopulation.setTitle(_translate("MainWindow", "Population Density"))
        self.radioButtonSquareMile.setText(_translate("MainWindow", "Per Square Mile"))
        self.radioButtonSquareKM.setText(_translate("MainWindow", "Per Square KM"))
        self.labelPopulationPer.setText(_translate("MainWindow", "Percentage of World Population: "))
        self.menuFileCountries.setTitle(_translate("MainWindow", "File"))
        self.actionLoad_Countries.setText(_translate("MainWindow", "Load Countries"))
        self.actionSave_To_File.setText(_translate("MainWindow", "Save To File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))