#view
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
#controller
from aboutus import Ui_aboutus
from pymongo import MongoClient

class Ui_pharmacistdatabase(object):
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
        col = db.DataPharmacist
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
    def setupUi(self, pharmacistdatabase):
        pharmacistdatabase.setObjectName("pharmacistdatabase")
        pharmacistdatabase.resize(1200, 600)
        pharmacistdatabase.setStyleSheet("background-color:rgb(240, 248, 255);")
        self.centralwidget = QtWidgets.QWidget(pharmacistdatabase)
        self.centralwidget.setObjectName("centralwidget")
        self.pharmacist_label = QtWidgets.QLabel(self.centralwidget)
        self.pharmacist_label.setGeometry(QtCore.QRect(0, 0, 1201, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pharmacist_label.setFont(font)
        self.pharmacist_label.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(255, 196, 0)")
        self.pharmacist_label.setObjectName("pharmacist_label")
        self.aboutus_button = QtWidgets.QPushButton(self.centralwidget)
        self.aboutus_button.setGeometry(QtCore.QRect(1090, 10, 91, 41))
        self.aboutus_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(255, 196, 0)")
        self.aboutus_button.setObjectName("aboutus_button")
        #controller
        self.aboutus_button.clicked.connect(self.openaboutus)
         #---------------------------------------------------------------
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(310, 120, 581, 311))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.mainmenu_button = QtWidgets.QPushButton(self.centralwidget)
        self.mainmenu_button.setGeometry(QtCore.QRect(60, 490, 91, 41))
        self.mainmenu_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.mainmenu_button.setObjectName("mainmenu_button")
        #controller
        self.mainmenu_button.clicked.connect(self.closebutton)
        #------------------------------------------------------------------
        self.loaddata_button = QtWidgets.QPushButton(self.centralwidget)
        self.loaddata_button.setGeometry(QtCore.QRect(1020, 490, 91, 41))
        self.loaddata_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.loaddata_button.setObjectName("loaddata_button")

        self.loaddata_button.clicked.connect(self.SHOWdatabase)
        
        pharmacistdatabase.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(pharmacistdatabase)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        pharmacistdatabase.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(pharmacistdatabase)
        self.statusbar.setObjectName("statusbar")
        pharmacistdatabase.setStatusBar(self.statusbar)

        self.retranslateUi(pharmacistdatabase)
        QtCore.QMetaObject.connectSlotsByName(pharmacistdatabase)

    def retranslateUi(self, pharmacistdatabase):
        _translate = QtCore.QCoreApplication.translate
        pharmacistdatabase.setWindowTitle(_translate("pharmacistdatabase", "MainWindow"))
        self.pharmacist_label.setText(_translate("pharmacistdatabase", "   PHARMACIST DATABASE "))
        self.aboutus_button.setText(_translate("pharmacistdatabase", "ABOUT US"))
        self.mainmenu_button.setText(_translate("pharmacistdatabase", "MAIN MENU"))
        self.loaddata_button.setText(_translate("pharmacistdatabase", "LOAD DATA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pharmacistdatabase = QtWidgets.QMainWindow()
    ui = Ui_pharmacistdatabase()
    ui.setupUi(pharmacistdatabase)
    pharmacistdatabase.show()
    sys.exit(app.exec_())
