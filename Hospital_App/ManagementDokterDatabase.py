# view
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableView
# controller
from aboutus import Ui_aboutus
from pymongo import MongoClient


class Ui_ManagementDokterDatabase(object):
    # controller
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
        col = db.DataDokter
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
    # view

    def setupUi(self, ManagementDokterDatabase):
        ManagementDokterDatabase.setObjectName("ManagementDokterDatabase")
        ManagementDokterDatabase.resize(1200, 600)
        ManagementDokterDatabase.setStyleSheet(
            "background-color:rgb(240, 248, 255);")
        self.centralwidget = QtWidgets.QWidget(ManagementDokterDatabase)
        self.centralwidget.setObjectName("centralwidget")
        self.ManagementDokterDatabase_label = QtWidgets.QLabel(
            self.centralwidget)
        self.ManagementDokterDatabase_label.setGeometry(
            QtCore.QRect(0, 0, 1201, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ManagementDokterDatabase_label.setFont(font)
        self.ManagementDokterDatabase_label.setStyleSheet("color:rgb(255, 255, 255);\n"
                                                          "background-color:rgb(246, 61, 19)")
        self.ManagementDokterDatabase_label.setObjectName(
            "ManagementDokterDatabase_label")
        self.aboutus_button = QtWidgets.QPushButton(self.centralwidget)
        self.aboutus_button.setGeometry(QtCore.QRect(1090, 10, 91, 41))
        self.aboutus_button.setStyleSheet("color:rgb(255, 255, 255);\n"
                                          "background-color:rgb(246, 61, 19)")
        self.aboutus_button.setObjectName("aboutus_button")
        # controller
        self.aboutus_button.clicked.connect(self.openaboutus)
        # ----------------------------------------------------------------
        self.loaddata_button = QtWidgets.QPushButton(self.centralwidget)
        self.loaddata_button.setGeometry(QtCore.QRect(970, 490, 91, 41))
        self.loaddata_button.setStyleSheet("color:rgb(255, 255, 255);\n"
                                           "background-color:rgb(0, 191, 255)")
        self.loaddata_button.setObjectName("loaddata_button")

        self.loaddata_button.clicked.connect(self.SHOWdatabase)

        self.mainmenu_button = QtWidgets.QPushButton(self.centralwidget)
        self.mainmenu_button.setGeometry(QtCore.QRect(110, 490, 91, 41))
        self.mainmenu_button.setStyleSheet("color:rgb(255, 255, 255);\n"
                                           "background-color:rgb(0, 191, 255)")
        self.mainmenu_button.setObjectName("mainmenu_button")
        # controller
        self.mainmenu_button.clicked.connect(self.closebutton)
        # ------------------------------------------------------------------
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(310, 110, 561, 341))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        ManagementDokterDatabase.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ManagementDokterDatabase)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        ManagementDokterDatabase.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ManagementDokterDatabase)
        self.statusbar.setObjectName("statusbar")
        ManagementDokterDatabase.setStatusBar(self.statusbar)

        self.retranslateUi(ManagementDokterDatabase)
        QtCore.QMetaObject.connectSlotsByName(ManagementDokterDatabase)

    def retranslateUi(self, ManagementDokterDatabase):
        _translate = QtCore.QCoreApplication.translate
        ManagementDokterDatabase.setWindowTitle(
            _translate("ManagementDokterDatabase", "MainWindow"))
        self.ManagementDokterDatabase_label.setText(_translate(
            "ManagementDokterDatabase", "    MANAGEMENT DOKTER DATABASE"))
        self.aboutus_button.setText(_translate(
            "ManagementDokterDatabase", "ABOUT US"))
        self.loaddata_button.setText(_translate(
            "ManagementDokterDatabase", "LOAD DATA"))
        self.mainmenu_button.setText(_translate(
            "ManagementDokterDatabase", "MAIN MENU"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ManagementDokterDatabase = QtWidgets.QMainWindow()
    ui = Ui_ManagementDokterDatabase()
    ui.setupUi(ManagementDokterDatabase)
    ManagementDokterDatabase.show()
    sys.exit(app.exec_())
