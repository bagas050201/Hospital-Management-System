#view
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableView
#controler
from aboutus import Ui_aboutus
from pymongo import MongoClient

class Ui_managementjanjibertemudatabase(object):
    #controler
    def openaboutus(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_aboutus()
        self.ui.setupUi(self.window)
        self.window.show()

    def closebutton(self):
        self.mainmenu_button.hide()
        msg = QMessageBox()
        msg.setText("mohon close menggunakan tombol silang merah diatas")
        msg.setIcon(QMessageBox.Critical)
        x = msg.exec_()

     #Model Database
    def SHOWdatabase(self):
        client = MongoClient('localhost:27017')
        db = client.aplikasirumahsakit
        col = db.DataJanjiBertemu
        print("database connected")

        datas = list(col.find())
        self.tableWidget.setRowCount(21)

        # print pada tabel
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
    def setupUi(self, managementjanjibertemudatabase):
        managementjanjibertemudatabase.setObjectName("managementjanjibertemudatabase")
        managementjanjibertemudatabase.resize(1200, 600)
        managementjanjibertemudatabase.setStyleSheet("background-color:rgb(240, 248, 255);")
        self.centralwidget = QtWidgets.QWidget(managementjanjibertemudatabase)
        self.centralwidget.setObjectName("centralwidget")
        self.ManagementDokterDatabase_label = QtWidgets.QLabel(self.centralwidget)
        self.ManagementDokterDatabase_label.setGeometry(QtCore.QRect(0, 0, 1201, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ManagementDokterDatabase_label.setFont(font)
        self.ManagementDokterDatabase_label.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.ManagementDokterDatabase_label.setObjectName("ManagementDokterDatabase_label")
        self.aboutus_button = QtWidgets.QPushButton(self.centralwidget)
        self.aboutus_button.setGeometry(QtCore.QRect(1090, 10, 91, 41))
        self.aboutus_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.aboutus_button.setObjectName("aboutus_button")

        #controler (openaboutus)
        self.aboutus_button.clicked.connect(self.openaboutus)
        #-----------------------------------------------------------------
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(80, 100, 1051, 411))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.mainmenu_button = QtWidgets.QPushButton(self.centralwidget)
        self.mainmenu_button.setGeometry(QtCore.QRect(830, 10, 91, 41))
        self.mainmenu_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.mainmenu_button.setObjectName("mainmenu_button")

        #controler
        self.mainmenu_button.clicked.connect(self.closebutton)
        #-----------------------------------------------------------------
        self.loaddata_button = QtWidgets.QPushButton(self.centralwidget)
        self.loaddata_button.setGeometry(QtCore.QRect(960, 10, 91, 41))
        self.loaddata_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.loaddata_button.setObjectName("loaddata_button")

        self.loaddata_button.clicked.connect(self.SHOWdatabase)
        
        managementjanjibertemudatabase.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(managementjanjibertemudatabase)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        managementjanjibertemudatabase.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(managementjanjibertemudatabase)
        self.statusbar.setObjectName("statusbar")
        managementjanjibertemudatabase.setStatusBar(self.statusbar)

        self.retranslateUi(managementjanjibertemudatabase)
        QtCore.QMetaObject.connectSlotsByName(managementjanjibertemudatabase)

    def retranslateUi(self, managementjanjibertemudatabase):
        _translate = QtCore.QCoreApplication.translate
        managementjanjibertemudatabase.setWindowTitle(_translate("managementjanjibertemudatabase", "MainWindow"))
        self.ManagementDokterDatabase_label.setText(_translate("managementjanjibertemudatabase", "    MANAGEMENT JANJI BERTEMU DATABASE"))
        self.aboutus_button.setText(_translate("managementjanjibertemudatabase", "ABOUT US"))
        self.mainmenu_button.setText(_translate("managementjanjibertemudatabase", "MAIN MENU"))
        self.loaddata_button.setText(_translate("managementjanjibertemudatabase", "LOAD DATA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    managementjanjibertemudatabase = QtWidgets.QMainWindow()
    ui = Ui_managementjanjibertemudatabase()
    ui.setupUi(managementjanjibertemudatabase)
    managementjanjibertemudatabase.show()
    sys.exit(app.exec_())
