#view
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableView
#controller
from aboutus import Ui_aboutus
from pymongo import MongoClient

class Ui_databasepasien(object):
    #controller
    def openaboutus(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_aboutus()
        self.ui.setupUi(self.window)
        self.window.show()

    def closebutton(self):
        self.mainmenu_button.hide()
        msg = QMessageBox()
        msg.setText("mohon close menggunakan tombol merah diatas")
        msg.setIcon(QMessageBox.Critical)
        x = msg.exec_()

    #Model Database
    def SHOWdatabase(self):
        client = MongoClient('localhost:27017')
        db = client.aplikasirumahsakit
        col = db.DataPasien
        print("database connected")

        datas = list(col.find())
        self.tableWidget.setRowCount(21)

        # print pala tabel
        keys = datas[0].keys()
        for index, key in enumerate(keys):
            # print(type(key), key)
            self.tableWidget.setItem(
                0, index, QtWidgets.QTableWidgetItem(key))

        # print data dke tabel
        for row_index, data in enumerate(datas):
            for col_index, key in enumerate(data.keys()):
                # tambah 1 karena tambah pala
                self.tableWidget.setItem(
                    row_index + 1, col_index,  QtWidgets.QTableWidgetItem(str(data[key])))

    #view
    def setupUi(self, databasepasien):
        databasepasien.setObjectName("databasepasien")
        databasepasien.resize(1200, 600)
        databasepasien.setStyleSheet("background-color:rgb(240, 248, 255);")
        self.centralwidget = QtWidgets.QWidget(databasepasien)
        self.centralwidget.setObjectName("centralwidget")
        self.databasepasien_label = QtWidgets.QLabel(self.centralwidget)
        self.databasepasien_label.setGeometry(QtCore.QRect(0, 0, 1201, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.databasepasien_label.setFont(font)
        self.databasepasien_label.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(127, 186, 0)")
        self.databasepasien_label.setObjectName("databasepasien_label")
        self.aboutus_button = QtWidgets.QPushButton(self.centralwidget)
        self.aboutus_button.setGeometry(QtCore.QRect(1090, 10, 91, 41))
        self.aboutus_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(127, 186, 0)")
        self.aboutus_button.setObjectName("aboutus_button")
        #controller
        self.aboutus_button.clicked.connect(self.openaboutus)
        #-----------------------------------------------------------------
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(80, 110, 1051, 411))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.loaddata_button = QtWidgets.QPushButton(self.centralwidget)
        self.loaddata_button.setGeometry(QtCore.QRect(940, 10, 91, 41))
        self.loaddata_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(127, 186, 0)")
        self.loaddata_button.setObjectName("loaddata_button")

        self.loaddata_button.clicked.connect(self.SHOWdatabase)
        
        self.mainmenu_button = QtWidgets.QPushButton(self.centralwidget)
        self.mainmenu_button.setGeometry(QtCore.QRect(790, 10, 91, 41))
        self.mainmenu_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(127, 186, 0)")
        self.mainmenu_button.setObjectName("mainmenu_button")
        #controller
        self.mainmenu_button.clicked.connect(self.closebutton)
        #----------------------------------------------------------------
        databasepasien.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(databasepasien)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        databasepasien.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(databasepasien)
        self.statusbar.setObjectName("statusbar")
        databasepasien.setStatusBar(self.statusbar)

        self.retranslateUi(databasepasien)
        QtCore.QMetaObject.connectSlotsByName(databasepasien)

    def retranslateUi(self, databasepasien):
        _translate = QtCore.QCoreApplication.translate
        databasepasien.setWindowTitle(_translate("databasepasien", "MainWindow"))
        self.databasepasien_label.setText(_translate("databasepasien", "   DATABASE PASIEN"))
        self.aboutus_button.setText(_translate("databasepasien", "ABOUT US"))
        self.loaddata_button.setText(_translate("databasepasien", "LOAD DATA"))
        self.mainmenu_button.setText(_translate("databasepasien", "MAIN MENU"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    databasepasien = QtWidgets.QMainWindow()
    ui = Ui_databasepasien()
    ui.setupUi(databasepasien)
    databasepasien.show()
    sys.exit(app.exec_())
