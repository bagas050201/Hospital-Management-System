#view
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
#controller
from databasepasien import Ui_databasepasien
from aboutus import Ui_aboutus
from pymongo import MongoClient

class Ui_dataformpasien(object):
    #controller
    def openaboutus(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_aboutus()
        self.ui.setupUi(self.window)
        self.window.show()
        
        
    def closebutton(self):
        self.back_button.hide()
        msg = QMessageBox()
        msg.setText("mohon close menggunakan tombol merah diatas")
        msg.setIcon(QMessageBox.Critical)
        x = msg.exec_()

    #Controller to Model database
    def POSTdatabase(self):
        client = MongoClient('localhost:27017')
        db = client.aplikasirumahsakit
        col = db.DataPasien

        PasienNAMA = self.namapasien_input_bar.text()
        PasienUMUR = self.umur_input_bar.text()
        PasienJENISKELAMIN = self.jeniskelamin_input_bar.text()
        PasienDIAGNOSA = self.diagnosapenyakit_input_bar.text()
        PasienALAMAT = self.alamat_input_bar.text()
        PasienKK = self.kartukesehatan_input_bar.text()
        PasienTELEPON = self.nomortelepon_input_bar.text()
        PasienKTP = self.nomorktp_input_bar.text()

        col.insert_one(
        {
            "NAMA PASIEN": PasienNAMA,
            "UMUR ":PasienUMUR,
            "JENIS KELAMIN": PasienJENISKELAMIN,
            "DIAGNOSA PENYAKIT":PasienDIAGNOSA,
            "ALAMAT": PasienALAMAT,
            "KARTU KESEHATAN": PasienKK,
            "NOMOR TELEPON": PasienTELEPON,
            "NOMOR KTP": PasienKTP
            })
        print ('\nInserted data successfully\n')

    def UPDATEdatabase(self):
        client = MongoClient('localhost:27017')
        db = client.aplikasirumahsakit
        col = db.DataPasien

        PasienNAMA = self.namapasien_input_bar.text()
        PasienUMUR = self.umur_input_bar.text()
        PasienJENISKELAMIN = self.jeniskelamin_input_bar.text()
        PasienDIAGNOSA = self.diagnosapenyakit_input_bar.text()
        PasienALAMAT = self.alamat_input_bar.text()
        PasienKK = self.kartukesehatan_input_bar.text()
        PasienTELEPON = self.nomortelepon_input_bar.text()
        PasienKTP = self.nomorktp_input_bar.text()

        col.update_one(
	{"NAMA PASIEN":  PasienNAMA},
	{"$set": {"UMUR": PasienUMUR,"JENIS KELAMIN":PasienJENISKELAMIN,"DIAGNOSA PENYAKIT":PasienDIAGNOSA,"ALAMAT":PasienALAMAT,"KARTU KESEHATAN":PasienKK,"NOMOR TELEPON":PasienTELEPON,"NOMOR KTP":PasienKTP}})
        print ("\nRecords updated successfully\n")

    def DELETEdatabase(self):
          client = MongoClient('localhost:27017')
          db = client.aplikasirumahsakit
          col = db.DataPasien
          
          PasienNAMA = self.namapasien_input_bar.text()
          col.delete_many({"NAMA PASIEN":PasienNAMA})
          print ('\nDeletion successful\n')
          
    
    #view
    def setupUi(self, dataformpasien):
        dataformpasien.setObjectName("dataformpasien")
        dataformpasien.resize(1200, 600)
        dataformpasien.setStyleSheet("background-color:rgb(240, 248, 255);")
        self.centralwidget = QtWidgets.QWidget(dataformpasien)
        self.centralwidget.setObjectName("centralwidget")
        self.dataformpasien_label = QtWidgets.QLabel(self.centralwidget)
        self.dataformpasien_label.setGeometry(QtCore.QRect(0, 0, 1201, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dataformpasien_label.setFont(font)
        self.dataformpasien_label.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(127, 186, 0)")
        self.dataformpasien_label.setObjectName("dataformpasien_label")
        self.aboutus_button = QtWidgets.QPushButton(self.centralwidget)
        self.aboutus_button.setGeometry(QtCore.QRect(1080, 10, 91, 41))
        self.aboutus_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(127, 186, 0)")
        self.aboutus_button.setObjectName("aboutus_button")
        #controller
        self.aboutus_button.clicked.connect(self.openaboutus)
        #-----------------------------------------------------------------
        self.namapasien_label = QtWidgets.QLabel(self.centralwidget)
        self.namapasien_label.setGeometry(QtCore.QRect(40, 110, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.namapasien_label.setFont(font)
        self.namapasien_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.namapasien_label.setObjectName("namapasien_label")
        self.namapasien_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.namapasien_input_bar.setGeometry(QtCore.QRect(40, 150, 321, 31))
        self.namapasien_input_bar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.namapasien_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.namapasien_input_bar.setText("")
        self.namapasien_input_bar.setObjectName("namapasien_input_bar")
        self.umur_label = QtWidgets.QLabel(self.centralwidget)
        self.umur_label.setGeometry(QtCore.QRect(30, 200, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.umur_label.setFont(font)
        self.umur_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.umur_label.setObjectName("umur_label")
        self.umur_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.umur_input_bar.setGeometry(QtCore.QRect(40, 240, 321, 31))
        self.umur_input_bar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.umur_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.umur_input_bar.setText("")
        self.umur_input_bar.setObjectName("umur_input_bar")
        self.jeniskelamin_label = QtWidgets.QLabel(self.centralwidget)
        self.jeniskelamin_label.setGeometry(QtCore.QRect(30, 290, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.jeniskelamin_label.setFont(font)
        self.jeniskelamin_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.jeniskelamin_label.setObjectName("jeniskelamin_label")
        self.jeniskelamin_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.jeniskelamin_input_bar.setGeometry(QtCore.QRect(40, 330, 321, 31))
        self.jeniskelamin_input_bar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.jeniskelamin_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.jeniskelamin_input_bar.setText("")
        self.jeniskelamin_input_bar.setObjectName("jeniskelamin_input_bar")
        self.diagnosapenyakit_label = QtWidgets.QLabel(self.centralwidget)
        self.diagnosapenyakit_label.setGeometry(QtCore.QRect(30, 380, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.diagnosapenyakit_label.setFont(font)
        self.diagnosapenyakit_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.diagnosapenyakit_label.setObjectName("diagnosapenyakit_label")
        self.diagnosapenyakit_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.diagnosapenyakit_input_bar.setGeometry(QtCore.QRect(40, 420, 321, 31))
        self.diagnosapenyakit_input_bar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.diagnosapenyakit_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.diagnosapenyakit_input_bar.setText("")
        self.diagnosapenyakit_input_bar.setObjectName("diagnosapenyakit_input_bar")
        self.alamat_label = QtWidgets.QLabel(self.centralwidget)
        self.alamat_label.setGeometry(QtCore.QRect(630, 110, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.alamat_label.setFont(font)
        self.alamat_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.alamat_label.setObjectName("alamat_label")
        self.alamat_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.alamat_input_bar.setGeometry(QtCore.QRect(630, 150, 321, 31))
        self.alamat_input_bar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.alamat_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.alamat_input_bar.setText("")
        self.alamat_input_bar.setObjectName("alamat_input_bar")
        self.kartukesehatan_label = QtWidgets.QLabel(self.centralwidget)
        self.kartukesehatan_label.setGeometry(QtCore.QRect(630, 200, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.kartukesehatan_label.setFont(font)
        self.kartukesehatan_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.kartukesehatan_label.setObjectName("kartukesehatan_label")
        self.kartukesehatan_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.kartukesehatan_input_bar.setGeometry(QtCore.QRect(630, 240, 321, 31))
        self.kartukesehatan_input_bar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.kartukesehatan_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.kartukesehatan_input_bar.setText("")
        self.kartukesehatan_input_bar.setObjectName("kartukesehatan_input_bar")
        self.nomortelepon_label = QtWidgets.QLabel(self.centralwidget)
        self.nomortelepon_label.setGeometry(QtCore.QRect(630, 290, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.nomortelepon_label.setFont(font)
        self.nomortelepon_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.nomortelepon_label.setObjectName("nomortelepon_label")
        self.nomortelepon_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.nomortelepon_input_bar.setGeometry(QtCore.QRect(630, 330, 321, 31))
        self.nomortelepon_input_bar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.nomortelepon_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.nomortelepon_input_bar.setText("")
        self.nomortelepon_input_bar.setObjectName("nomortelepon_input_bar")
        self.nomorktp_label = QtWidgets.QLabel(self.centralwidget)
        self.nomorktp_label.setGeometry(QtCore.QRect(630, 380, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.nomorktp_label.setFont(font)
        self.nomorktp_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.nomorktp_label.setObjectName("nomorktp_label")
        self.nomorktp_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.nomorktp_input_bar.setGeometry(QtCore.QRect(630, 420, 321, 31))
        self.nomorktp_input_bar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.nomorktp_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.nomorktp_input_bar.setText("")
        self.nomorktp_input_bar.setObjectName("nomorktp_input_bar")
        self.update_button = QtWidgets.QPushButton(self.centralwidget)
        self.update_button.setGeometry(QtCore.QRect(480, 480, 91, 41))
        self.update_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.update_button.setObjectName("update_button")

        #controller
        self.update_button.clicked.connect(self.UPDATEdatabase)
        #-----------------------------------------------------------------------
        
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(700, 480, 91, 41))
        self.submit_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.submit_button.setObjectName("submit_button")

        #controller
        self.submit_button.clicked.connect(self.POSTdatabase)
        #-----------------------------------------------------------------
        
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setGeometry(QtCore.QRect(270, 480, 91, 41))
        self.delete_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.delete_button.setObjectName("delete_button")
        #controller
        self.delete_button.clicked.connect(self.DELETEdatabase)
        #---------------------------------------------------------------------
        
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(40, 480, 91, 41))
        self.back_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.back_button.setObjectName("back_button")
        #controller
        self.back_button.clicked.connect(self.closebutton)
        #-----------------------------------------------------------
        
        dataformpasien.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(dataformpasien)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        dataformpasien.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(dataformpasien)
        self.statusbar.setObjectName("statusbar")
        dataformpasien.setStatusBar(self.statusbar)

        self.retranslateUi(dataformpasien)
        QtCore.QMetaObject.connectSlotsByName(dataformpasien)

    def retranslateUi(self, dataformpasien):
        _translate = QtCore.QCoreApplication.translate
        dataformpasien.setWindowTitle(_translate("dataformpasien", "MainWindow"))
        self.dataformpasien_label.setText(_translate("dataformpasien", "  DATA FORM PASIEN"))
        self.aboutus_button.setText(_translate("dataformpasien", "ABOUT US"))
        self.namapasien_label.setText(_translate("dataformpasien", "NAMA PASIEN"))
        self.umur_label.setText(_translate("dataformpasien", "  UMUR"))
        self.jeniskelamin_label.setText(_translate("dataformpasien", "  JENIS KELAMIN"))
        self.diagnosapenyakit_label.setText(_translate("dataformpasien", "  DIAGNOSA PENYAKIT"))
        self.alamat_label.setText(_translate("dataformpasien", "ALAMAT"))
        self.kartukesehatan_label.setText(_translate("dataformpasien", "KARTU KESEHATAN (JAMKESMAS/ASKES/UMUM)"))
        self.nomortelepon_label.setText(_translate("dataformpasien", "NOMOR TELEPON"))
        self.nomorktp_label.setText(_translate("dataformpasien", "NOMOR KTP"))
        self.update_button.setText(_translate("dataformpasien", "UPDATE"))
        self.submit_button.setText(_translate("dataformpasien", "SUBMIT"))
        self.delete_button.setText(_translate("dataformpasien", "DELETE"))
        self.back_button.setText(_translate("dataformpasien", "BACK"))

    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dataformpasien = QtWidgets.QMainWindow()
    ui = Ui_dataformpasien()
    ui.setupUi(dataformpasien)
    dataformpasien.show()
    sys.exit(app.exec_())
