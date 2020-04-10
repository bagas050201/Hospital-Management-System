#view
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
#controler
from aboutus import Ui_aboutus
from pharmacistdatabase import Ui_pharmacistdatabase
from pymongo import MongoClient

class Ui_kebutuhanpharmacist(object):
    #controller to view
    def openaboutus(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_aboutus()
        self.ui.setupUi(self.window)
        self.window.show()

    def openpharmacistdatabase(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_pharmacistdatabase()
        self.ui.setupUi(self.window)
        self.window.show()

    def closebutton(self):
        self.back_button.hide()
        msg = QMessageBox()
        msg.setText("mohon close menggunakan tombol silang merah diatas")
        msg.setIcon(QMessageBox.Critical)
        x = msg.exec_()

    #Controller to Model database
    def POSTdatabase(self):
          client = MongoClient('localhost:27017')
          db = client.aplikasirumahsakit
          col = db.DataPharmacist

          ButuhID = self.id_input_bar.text()
          ButuhNAMA = self.namabarang_input_bar.text()
          ButuhSTOK = self.stokkebutuhan_input_bar.text()
          ButuhTANGGAL = self.tanggalready_input_bar.text()

          col.insert_one(
            {
                "ID": ButuhID,
                "NAMA BARANG": ButuhNAMA,
                "STOK KEBUTUHAN": ButuhSTOK,
                "TANGGAL READY":ButuhTANGGAL
                })
          print ('\nInserted data successfully\n')

    def UPDATEdatabase(self):
          client = MongoClient('localhost:27017')
          db = client.aplikasirumahsakit
          col = db.DataPharmacist

          ButuhID = self.id_input_bar.text()
          ButuhNAMA = self.namabarang_input_bar.text()
          ButuhSTOK = self.stokkebutuhan_input_bar.text()
          ButuhTANGGAL = self.tanggalready_input_bar.text()

          col.update_one(
	    {"ID": ButuhID},
	    {"$set": {"NAMA BARANG":ButuhNAMA,"STOK KEBUTUHAN": ButuhSTOK,"TANGGAL READY":ButuhTANGGAL}})
          print ("\nRecords updated successfully\n")

    def DELETEdatabase(self):
          client = MongoClient('localhost:27017')
          db = client.aplikasirumahsakit
          col = db.DataPharmacist
          
          ButuhID = self.id_input_bar.text()
          col.delete_many({"ID":ButuhID})
          print ('\nDeletion successful\n')

    #view
    def setupUi(self, kebutuhanpharmacist):
        kebutuhanpharmacist.setObjectName("kebutuhanpharmacist")
        kebutuhanpharmacist.resize(1200, 600)
        kebutuhanpharmacist.setStyleSheet("background-color:rgb(240, 248, 255);")
        self.centralwidget = QtWidgets.QWidget(kebutuhanpharmacist)
        self.centralwidget.setObjectName("centralwidget")
        self.Managementstokbarang_label = QtWidgets.QLabel(self.centralwidget)
        self.Managementstokbarang_label.setGeometry(QtCore.QRect(0, 0, 1201, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Managementstokbarang_label.setFont(font)
        self.Managementstokbarang_label.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(255, 196, 0)")
        self.Managementstokbarang_label.setObjectName("Managementstokbarang_label")
        self.id_label = QtWidgets.QLabel(self.centralwidget)
        self.id_label.setGeometry(QtCore.QRect(300, 110, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.id_label.setFont(font)
        self.id_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.id_label.setObjectName("id_label")
        self.id_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.id_input_bar.setGeometry(QtCore.QRect(460, 110, 321, 31))
        self.id_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.id_input_bar.setText("")
        self.id_input_bar.setObjectName("id_input_bar")
        self.namabarang_label = QtWidgets.QLabel(self.centralwidget)
        self.namabarang_label.setGeometry(QtCore.QRect(290, 170, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.namabarang_label.setFont(font)
        self.namabarang_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.namabarang_label.setObjectName("namabarang_label")
        self.namabarang_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.namabarang_input_bar.setGeometry(QtCore.QRect(460, 170, 321, 31))
        self.namabarang_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.namabarang_input_bar.setObjectName("namabarang_input_bar")
        self.stokkebutuhan_label = QtWidgets.QLabel(self.centralwidget)
        self.stokkebutuhan_label.setGeometry(QtCore.QRect(290, 230, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.stokkebutuhan_label.setFont(font)
        self.stokkebutuhan_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.stokkebutuhan_label.setObjectName("stokkebutuhan_label")
        self.stokkebutuhan_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.stokkebutuhan_input_bar.setGeometry(QtCore.QRect(460, 230, 321, 31))
        self.stokkebutuhan_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.stokkebutuhan_input_bar.setObjectName("stokkebutuhan_input_bar")
        self.tanggalready_label = QtWidgets.QLabel(self.centralwidget)
        self.tanggalready_label.setGeometry(QtCore.QRect(290, 290, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tanggalready_label.setFont(font)
        self.tanggalready_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.tanggalready_label.setObjectName("tanggalready_label")
        self.tanggalready_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.tanggalready_input_bar.setGeometry(QtCore.QRect(460, 290, 321, 31))
        self.tanggalready_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.tanggalready_input_bar.setObjectName("tanggalready_input_bar")
        self.update_button = QtWidgets.QPushButton(self.centralwidget)
        self.update_button.setGeometry(QtCore.QRect(520, 390, 91, 41))
        self.update_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.update_button.setObjectName("update_button")

        #controller
        self.update_button.clicked.connect(self.UPDATEdatabase)
         #-------------------------------------------------------------
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(700, 390, 91, 41))
        self.submit_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.submit_button.setObjectName("submit_button")

        #controller
        self.submit_button.clicked.connect(self.POSTdatabase)
         #------------------------------------------------------------------
         
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setGeometry(QtCore.QRect(340, 390, 91, 41))
        self.delete_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.delete_button.setObjectName("delete_button")

        #controller
        self.delete_button.clicked.connect(self.DELETEdatabase)
         #--------------------------------------------------------------------
         
        self.view_button = QtWidgets.QPushButton(self.centralwidget)
        self.view_button.setGeometry(QtCore.QRect(1000, 490, 91, 41))
        self.view_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.view_button.setObjectName("view_button")

        #controller
        self.view_button.clicked.connect(self.openpharmacistdatabase)
        #--------------------------------------------------------------------------
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(40, 490, 91, 41))
        self.back_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.back_button.setObjectName("back_button")

        #controleer
        self.back_button.clicked.connect(self.closebutton)
        #------------------------------------------------------------
        self.aboutus_button = QtWidgets.QPushButton(self.centralwidget)
        self.aboutus_button.setGeometry(QtCore.QRect(1080, 10, 91, 41))
        self.aboutus_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(255, 196, 0)")
        self.aboutus_button.setObjectName("aboutus_button")

        #controller
        self.aboutus_button.clicked.connect(self.openaboutus)
        #----------------------------------------------------------------
        
        kebutuhanpharmacist.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(kebutuhanpharmacist)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        kebutuhanpharmacist.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(kebutuhanpharmacist)
        self.statusbar.setObjectName("statusbar")
        kebutuhanpharmacist.setStatusBar(self.statusbar)

        self.retranslateUi(kebutuhanpharmacist)
        QtCore.QMetaObject.connectSlotsByName(kebutuhanpharmacist)

    def retranslateUi(self, kebutuhanpharmacist):
        _translate = QtCore.QCoreApplication.translate
        kebutuhanpharmacist.setWindowTitle(_translate("kebutuhanpharmacist", "MainWindow"))
        self.Managementstokbarang_label.setText(_translate("kebutuhanpharmacist", "   KEBUTUHAN PHARMACIST "))
        self.id_label.setText(_translate("kebutuhanpharmacist", " ID"))
        self.namabarang_label.setText(_translate("kebutuhanpharmacist", "   NAMA BARANG"))
        self.stokkebutuhan_label.setText(_translate("kebutuhanpharmacist", "   STOK KEBUTUHAN"))
        self.tanggalready_label.setText(_translate("kebutuhanpharmacist", "   TANGGAL READY"))
        self.update_button.setText(_translate("kebutuhanpharmacist", "UPDATE"))
        self.submit_button.setText(_translate("kebutuhanpharmacist", "SUBMIT"))
        self.delete_button.setText(_translate("kebutuhanpharmacist", "DELETE"))
        self.view_button.setText(_translate("kebutuhanpharmacist", "VIEW"))
        self.back_button.setText(_translate("kebutuhanpharmacist", "BACK"))
        self.aboutus_button.setText(_translate("kebutuhanpharmacist", "ABOUT US"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    kebutuhanpharmacist = QtWidgets.QMainWindow()
    ui = Ui_kebutuhanpharmacist()
    ui.setupUi(kebutuhanpharmacist)
    kebutuhanpharmacist.show()
    sys.exit(app.exec_())
