#view
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
#controller
from aboutus import Ui_aboutus
from ManagementDokterDatabase import Ui_ManagementDokterDatabase
from pymongo import MongoClient

class Ui_ManagementDokter(object):
    #controller to View
     def openaboutus(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_aboutus()
        self.ui.setupUi(self.window)
        self.window.show()
     def openManagementDokterDatabase(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ManagementDokterDatabase()
        self.ui.setupUi(self.window)
        self.window.show()

     def closebutton(self):
        self.back_button.hide()
        msg = QMessageBox()
        msg.setText("mohon close menggunakan tombol silang merah diatas")
        msg.setIcon(QMessageBox.Critical)
        x = msg.exec_()

     #controller to Model database
     def POSTdatabase(self):
          client = MongoClient('localhost:27017')
          db = client.aplikasirumahsakit
          col = db.DataDokter

          DokterID = self.id_input_bar.text()
          DokterNAMA = self.nama_input_bar.text()
          DokterSPECIALIZATION = self.specialization_input_bar.text()
          DokterCONTACT = self.contact_input_bar.text()

          col.insert_one(
            {
                "ID": DokterID,
                "NAMA":DokterNAMA,
                "SPECIALIZATION":DokterSPECIALIZATION,
                "CONTACT":DokterCONTACT
                })
          print ('\nInserted data successfully\n')

     def UPDATEdatabase(self):
          client = MongoClient('localhost:27017')
          db = client.aplikasirumahsakit
          col = db.DataDokter

          DokterID = self.id_input_bar.text()
          DokterNAMA = self.nama_input_bar.text()
          DokterSPECIALIZATION = self.specialization_input_bar.text()
          DokterCONTACT = self.contact_input_bar.text()

          col.update_one(
	    {"ID": DokterID},
	    {"$set": {"NAMA":DokterNAMA,"SPECIALIZATION":DokterSPECIALIZATION,"CONTACT":DokterCONTACT}})
          print ("\nRecords updated successfully\n")

     def DELETEdatabase(self):
          client = MongoClient('localhost:27017')
          db = client.aplikasirumahsakit
          col = db.DataDokter
          
          DokterID = self.id_input_bar.text()
          col.delete_many({"ID":DokterID})
          print ('\nDeletion successful\n')

     #view
     def setupUi(self, ManagementDokter):
        ManagementDokter.setObjectName("ManagementDokter")
        ManagementDokter.resize(1200, 600)
        ManagementDokter.setStyleSheet("background-color:rgb(240, 248, 255);\n"
"color:rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(ManagementDokter)
        self.centralwidget.setObjectName("centralwidget")
        self.ManagementDokter_label = QtWidgets.QLabel(self.centralwidget)
        self.ManagementDokter_label.setGeometry(QtCore.QRect(0, 0, 1201, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ManagementDokter_label.setFont(font)
        self.ManagementDokter_label.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(246, 61, 19)")
        self.ManagementDokter_label.setObjectName("ManagementDokter_label")
        self.aboutus_button = QtWidgets.QPushButton(self.centralwidget)
        self.aboutus_button.setGeometry(QtCore.QRect(1070, 10, 91, 41))
        self.aboutus_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(246, 61, 19)")
        self.aboutus_button.setObjectName("aboutus_button")

          #controller
        self.aboutus_button.clicked.connect(self.openaboutus)
        #----------------------------------------------------------------
        
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(20, 490, 91, 41))
        self.back_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.back_button.setObjectName("back_button")

          #controller
        self.back_button.clicked.connect(self.closebutton)
         #----------------------------------------------------------
        
        self.id_label = QtWidgets.QLabel(self.centralwidget)
        self.id_label.setGeometry(QtCore.QRect(350, 150, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.id_label.setFont(font)
        self.id_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.id_label.setObjectName("id_label")
        self.id_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.id_input_bar.setGeometry(QtCore.QRect(490, 150, 321, 31))
        self.id_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.id_input_bar.setText("")
        self.id_input_bar.setObjectName("id_input_bar")
        self.nama_label = QtWidgets.QLabel(self.centralwidget)
        self.nama_label.setGeometry(QtCore.QRect(340, 220, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.nama_label.setFont(font)
        self.nama_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.nama_label.setObjectName("nama_label")
        self.nama_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.nama_input_bar.setGeometry(QtCore.QRect(490, 220, 321, 31))
        self.nama_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.nama_input_bar.setObjectName("nama_input_bar")
        self.specialization_label = QtWidgets.QLabel(self.centralwidget)
        self.specialization_label.setGeometry(QtCore.QRect(350, 290, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.specialization_label.setFont(font)
        self.specialization_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.specialization_label.setObjectName("specialization_label")
        self.specialization_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.specialization_input_bar.setGeometry(QtCore.QRect(490, 290, 321, 31))
        self.specialization_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.specialization_input_bar.setObjectName("specialization_input_bar")
        self.contact_label = QtWidgets.QLabel(self.centralwidget)
        self.contact_label.setGeometry(QtCore.QRect(350, 360, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.contact_label.setFont(font)
        self.contact_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.contact_label.setObjectName("contact_label")
        self.contact_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.contact_input_bar.setGeometry(QtCore.QRect(490, 360, 321, 31))
        self.contact_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.contact_input_bar.setObjectName("contact_input_bar")
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setGeometry(QtCore.QRect(390, 440, 91, 41))
        self.delete_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.delete_button.setObjectName("delete_button")

        #controller
        self.delete_button.clicked.connect(self.DELETEdatabase)
        #---------------------------------------------------------------------
        
        self.update_button = QtWidgets.QPushButton(self.centralwidget)
        self.update_button.setGeometry(QtCore.QRect(560, 440, 91, 41))
        self.update_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.update_button.setObjectName("update_button")
        #Controller
        self.update_button.clicked.connect(self.UPDATEdatabase)
        #-------------------------------------------------------------------
        
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(730, 440, 91, 41))
        self.submit_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.submit_button.setObjectName("submit_button")

        #controller
        self.submit_button.clicked.connect(self.POSTdatabase)
        #------------------------------------------------------------------
        
        self.view_button = QtWidgets.QPushButton(self.centralwidget)
        self.view_button.setGeometry(QtCore.QRect(1070, 490, 91, 41))
        self.view_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.view_button.setObjectName("view_button")

        #controller
        self.view_button.clicked.connect(self.openManagementDokterDatabase)
        #--------------------------------------------------------------------------------------
        
        ManagementDokter.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ManagementDokter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        ManagementDokter.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ManagementDokter)
        self.statusbar.setObjectName("statusbar")
        ManagementDokter.setStatusBar(self.statusbar)

        self.retranslateUi(ManagementDokter)
        QtCore.QMetaObject.connectSlotsByName(ManagementDokter)

     def retranslateUi(self, ManagementDokter):
        _translate = QtCore.QCoreApplication.translate
        ManagementDokter.setWindowTitle(_translate("ManagementDokter", "MainWindow"))
        self.ManagementDokter_label.setText(_translate("ManagementDokter", "    MANAGEMENT DOKTER"))
        self.aboutus_button.setText(_translate("ManagementDokter", "ABOUT US"))
        self.back_button.setText(_translate("ManagementDokter", "BACK"))
        self.id_label.setText(_translate("ManagementDokter", " ID"))
        self.nama_label.setText(_translate("ManagementDokter", "   NAMA"))
        self.specialization_label.setText(_translate("ManagementDokter", "SPECIALIZATION"))
        self.contact_label.setText(_translate("ManagementDokter", "CONTACT"))
        self.delete_button.setText(_translate("ManagementDokter", "DELETE"))
        self.update_button.setText(_translate("ManagementDokter", "UPDATE"))
        self.submit_button.setText(_translate("ManagementDokter", "SUBMIT"))
        self.view_button.setText(_translate("ManagementDokter", "VIEW"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ManagementDokter = QtWidgets.QMainWindow()
    ui = Ui_ManagementDokter()
    ui.setupUi(ManagementDokter)
    ManagementDokter.show()
    sys.exit(app.exec_())
