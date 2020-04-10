#view
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
#controller
from aboutus import Ui_aboutus
from stokbarangdatabase import Ui_stokbarangdatabase
from pymongo import MongoClient

class Ui_managementstokbarang(object):
    
    #controller to view
    def openaboutus(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_aboutus()
        self.ui.setupUi(self.window)
        self.window.show()

    def openstokbarangdatabase(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_stokbarangdatabase()
        self.ui.setupUi(self.window)
        self.window.show()

    def closebutton(self):
        self.back_button.hide()
        msg = QMessageBox()
        msg.setText("mohon close menggunakan tombol silang merah diatas")
        msg.setIcon(QMessageBox.Critical)
        x = msg.exec_()

    #controller to model 
    def POSTdatabase(self):
          client = MongoClient('localhost:27017')
          db = client.aplikasirumahsakit
          col = db.DataBarang

          BarangID = self.id_input_bar.text()
          BarangSUPPLIER = self.supplier_input_bar.text()
          BarangNAMA = self.namabarang_input_bar.text()
          BarangHARGA = self.hargabarang_input_bar.text()
          BarangSTOK = self.stokbarang_input_bar.text()
          BarangKEMASAN = self.kemasan_input_bar.text()
          BarangTANGGALMASUK = self.tanggalmasuk_input_bar.text()

          col.insert_one(
            {
                "ID": BarangID,
                "SUPPLIER":BarangSUPPLIER,
                "NAMA": BarangNAMA,
                "HARGA":BarangHARGA,
                "STOK": BarangSTOK,
                "KEMASAN": BarangKEMASAN,
                "TANGGALMASUK": BarangTANGGALMASUK
                })
          print ('\nInserted data successfully\n')

    def UPDATEdatabase(self):
          client = MongoClient('localhost:27017')
          db = client.aplikasirumahsakit
          col = db.DataBarang

          BarangID = self.id_input_bar.text()
          BarangSUPPLIER = self.supplier_input_bar.text()
          BarangNAMA = self.namabarang_input_bar.text()
          BarangHARGA = self.hargabarang_input_bar.text()
          BarangSTOK = self.stokbarang_input_bar.text()
          BarangKEMASAN = self.kemasan_input_bar.text()
          BarangTANGGALMASUK = self.tanggalmasuk_input_bar.text()

          col.update_one(
	    {"ID": BarangID},
	    {"$set": {"SUPPLIER":BarangSUPPLIER,"NAMA":BarangNAMA,"HARGA":BarangHARGA,"STOK":BarangSTOK,"KEMASAN":BarangKEMASAN,"TANGGALMASUK":BarangTANGGALMASUK}})
          print ("\nRecords updated successfully\n")

    def DELETEdatabase(self):
          client = MongoClient('localhost:27017')
          db = client.aplikasirumahsakit
          col = db.DataBarang
          
          BarangID = self.id_input_bar.text()
          col.delete_many({"ID":BarangID})
          print ('\nDeletion successful\n')

    #view
    def setupUi(self, managementstokbarang):
        managementstokbarang.setObjectName("managementstokbarang")
        managementstokbarang.resize(1200, 600)
        managementstokbarang.setStyleSheet("background-color:rgb(240, 248, 255);\n"
"color:rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(managementstokbarang)
        self.centralwidget.setObjectName("centralwidget")
        self.Managementstokbarang_label = QtWidgets.QLabel(self.centralwidget)
        self.Managementstokbarang_label.setGeometry(QtCore.QRect(0, 0, 1201, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Managementstokbarang_label.setFont(font)
        self.Managementstokbarang_label.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(255, 196, 0)")
        self.Managementstokbarang_label.setObjectName("Managementstokbarang_label")
        self.aboutus_button = QtWidgets.QPushButton(self.centralwidget)
        self.aboutus_button.setGeometry(QtCore.QRect(1090, 10, 91, 41))
        self.aboutus_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(255, 196, 0)")
        self.aboutus_button.setObjectName("aboutus_button")

        #controller
        self.aboutus_button.clicked.connect(self.openaboutus)
        #----------------------------------------------------------------
        
        self.id_label = QtWidgets.QLabel(self.centralwidget)
        self.id_label.setGeometry(QtCore.QRect(330, 130, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.id_label.setFont(font)
        self.id_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.id_label.setObjectName("id_label")
        self.id_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.id_input_bar.setGeometry(QtCore.QRect(480, 130, 321, 31))
        self.id_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.id_input_bar.setText("")
        self.id_input_bar.setObjectName("id_input_bar")
        self.supplier_label = QtWidgets.QLabel(self.centralwidget)
        self.supplier_label.setGeometry(QtCore.QRect(320, 190, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.supplier_label.setFont(font)
        self.supplier_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.supplier_label.setObjectName("supplier_label")
        self.supplier_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.supplier_input_bar.setGeometry(QtCore.QRect(480, 190, 321, 31))
        self.supplier_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.supplier_input_bar.setObjectName("supplier_input_bar")
        self.namabarang_label = QtWidgets.QLabel(self.centralwidget)
        self.namabarang_label.setGeometry(QtCore.QRect(320, 250, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.namabarang_label.setFont(font)
        self.namabarang_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.namabarang_label.setObjectName("namabarang_label")
        self.namabarang_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.namabarang_input_bar.setGeometry(QtCore.QRect(480, 250, 321, 31))
        self.namabarang_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.namabarang_input_bar.setObjectName("namabarang_input_bar")
        self.hargabarang_label = QtWidgets.QLabel(self.centralwidget)
        self.hargabarang_label.setGeometry(QtCore.QRect(330, 310, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.hargabarang_label.setFont(font)
        self.hargabarang_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.hargabarang_label.setObjectName("hargabarang_label")
        self.hargabarang_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.hargabarang_input_bar.setGeometry(QtCore.QRect(480, 310, 321, 31))
        self.hargabarang_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.hargabarang_input_bar.setObjectName("hargabarang_input_bar")
        self.stokbarang_label = QtWidgets.QLabel(self.centralwidget)
        self.stokbarang_label.setGeometry(QtCore.QRect(320, 370, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.stokbarang_label.setFont(font)
        self.stokbarang_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.stokbarang_label.setObjectName("stokbarang_label")
        self.stokbarang_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.stokbarang_input_bar.setGeometry(QtCore.QRect(480, 370, 321, 31))
        self.stokbarang_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.stokbarang_input_bar.setObjectName("stokbarang_input_bar")
        self.kemasan_label = QtWidgets.QLabel(self.centralwidget)
        self.kemasan_label.setGeometry(QtCore.QRect(320, 430, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.kemasan_label.setFont(font)
        self.kemasan_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.kemasan_label.setObjectName("kemasan_label")
        self.kemasan_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.kemasan_input_bar.setGeometry(QtCore.QRect(480, 430, 321, 31))
        self.kemasan_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.kemasan_input_bar.setObjectName("kemasan_input_bar")
        self.tanggalmasuk_label = QtWidgets.QLabel(self.centralwidget)
        self.tanggalmasuk_label.setGeometry(QtCore.QRect(320, 480, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tanggalmasuk_label.setFont(font)
        self.tanggalmasuk_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.tanggalmasuk_label.setObjectName("tanggalmasuk_label")
        self.tanggalmasuk_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.tanggalmasuk_input_bar.setGeometry(QtCore.QRect(480, 480, 321, 31))
        self.tanggalmasuk_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.tanggalmasuk_input_bar.setObjectName("tanggalmasuk_input_bar")
        self.update_button = QtWidgets.QPushButton(self.centralwidget)
        self.update_button.setGeometry(QtCore.QRect(1090, 130, 91, 41))
        self.update_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.update_button.setObjectName("update_button")

        #controller
        self.update_button.clicked.connect(self.UPDATEdatabase)
        #----------------------------------------------------------------------
        
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(1090, 190, 91, 41))
        self.submit_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.submit_button.setObjectName("submit_button")

        #controller
        self.submit_button.clicked.connect(self.POSTdatabase)
        #------------------------------------------------------------------
        
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setGeometry(QtCore.QRect(1090, 250, 91, 41))
        self.delete_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.delete_button.setObjectName("delete_button")

        #controller
        self.delete_button.clicked.connect(self.DELETEdatabase)
        #--------------------------------------------------------------------
        
        self.view_button = QtWidgets.QPushButton(self.centralwidget)
        self.view_button.setGeometry(QtCore.QRect(1090, 320, 91, 41))
        self.view_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.view_button.setObjectName("view_button")

        #controller
        self.view_button.clicked.connect(self.openstokbarangdatabase)
        #---------------------------------------------------------------------------
        
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(30, 80, 91, 41))
        self.back_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.back_button.setObjectName("back_button")

        #controller
        self.back_button.clicked.connect(self.closebutton)
        #-----------------------------------------------------------
        managementstokbarang.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(managementstokbarang)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        managementstokbarang.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(managementstokbarang)
        self.statusbar.setObjectName("statusbar")
        managementstokbarang.setStatusBar(self.statusbar)

        self.retranslateUi(managementstokbarang)
        QtCore.QMetaObject.connectSlotsByName(managementstokbarang)

    def retranslateUi(self, managementstokbarang):
        _translate = QtCore.QCoreApplication.translate
        managementstokbarang.setWindowTitle(_translate("managementstokbarang", "MainWindow"))
        self.Managementstokbarang_label.setText(_translate("managementstokbarang", "    MANAGEMENT STOK BARANG"))
        self.aboutus_button.setText(_translate("managementstokbarang", "ABOUT US"))
        self.id_label.setText(_translate("managementstokbarang", " ID"))
        self.supplier_label.setText(_translate("managementstokbarang", "   SUPPLIER"))
        self.namabarang_label.setText(_translate("managementstokbarang", "   NAMA BARANG"))
        self.hargabarang_label.setText(_translate("managementstokbarang", " HARGA BARANG"))
        self.stokbarang_label.setText(_translate("managementstokbarang", "   STOK BARANG"))
        self.kemasan_label.setText(_translate("managementstokbarang", "   KEMASAN"))
        self.tanggalmasuk_label.setText(_translate("managementstokbarang", "   TANGGAL MASUK"))
        self.update_button.setText(_translate("managementstokbarang", "UPDATE"))
        self.submit_button.setText(_translate("managementstokbarang", "SUBMIT"))
        self.delete_button.setText(_translate("managementstokbarang", "DELETE"))
        self.view_button.setText(_translate("managementstokbarang", "VIEW"))
        self.back_button.setText(_translate("managementstokbarang", "BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    managementstokbarang = QtWidgets.QMainWindow()
    ui = Ui_managementstokbarang()
    ui.setupUi(managementstokbarang)
    managementstokbarang.show()
    sys.exit(app.exec_())
