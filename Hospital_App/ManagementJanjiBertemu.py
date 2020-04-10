#view
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
#controller
from aboutus import Ui_aboutus
from managementjanjibertemudatabase import Ui_managementjanjibertemudatabase
from pymongo import MongoClient

class Ui_ManagementJanjiBertemu(object):
    #controller to view
    def openaboutus(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_aboutus()
        self.ui.setupUi(self.window)
        self.window.show()

    def openmanagementjanjibertemudatabase(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_managementjanjibertemudatabase()
        self.ui.setupUi(self.window)
        self.window.show()

    def closebutton(self):
        self.back_button.hide()
        msg = QMessageBox()
        msg.setText("mohon close menggunakan tombol silang merah diatas")
        msg.setIcon(QMessageBox.Critical)
        x = msg.exec_()

    #controller to Model
    def POSTdatabase(self):
        client = MongoClient('localhost:27017')
        db = client.aplikasirumahsakit
        col = db.DataJanjiBertemu

        JanjiID = self.iddokter_input_bar.text()
        JanjiNAMA = self.namadokter_input_bar.text()
        JanjiSPECIALIZATION = self.specialization_input_bar.text()
        JanjiHARI = self.harikerja_input_bar.text()
        JanjiJAM = self.jamkerja_input_bar.text()
        JanjiPASIEN1 = self.namapasien1_input_bar.text()
        JanjiPASIEN2 = self.namapasien2_input_bar.text()
        JanjiPASIEN3 = self.namapasien3_input_bar.text()

        col.insert_one(
        {
            "ID": JanjiID,
            "NAMA DOKTER":JanjiNAMA,
            "SPECIALIZATION": JanjiSPECIALIZATION,
            "HARI KERJA":JanjiHARI,
            "JAM KERJA": JanjiJAM,
            "NAMA PASIEN 1": JanjiPASIEN1,
            "NAMA PASIEN 2": JanjiPASIEN2,
            "NAMA PASIEN 3": JanjiPASIEN3
            })
        print ('\nInserted data successfully\n')

    def UPDATEdatabase(self):
        client = MongoClient('localhost:27017')
        db = client.aplikasirumahsakit
        col = db.DataJanjiBertemu

        JanjiID = self.iddokter_input_bar.text()
        JanjiNAMA = self.namadokter_input_bar.text()
        JanjiSPECIALIZATION = self.specialization_input_bar.text()
        JanjiHARI = self.harikerja_input_bar.text()
        JanjiJAM = self.jamkerja_input_bar.text()
        JanjiPASIEN1 = self.namapasien1_input_bar.text()
        JanjiPASIEN2 = self.namapasien2_input_bar.text()
        JanjiPASIEN3 = self.namapasien3_input_bar.text()

        col.update_one(
	{"ID": JanjiID},
	{"$set": {"NAMA DOKTER":JanjiNAMA,"SPECIALIZATION":JanjiSPECIALIZATION,"HARI KERJA":JanjiHARI,"JAM KERJA":JanjiJAM,"NAMA PASIEN 1":JanjiPASIEN1,"NAMA PASIEN 2":JanjiPASIEN2,"NAMA PASIEN 3":JanjiPASIEN3}})
        print ("\nRecords updated successfully\n")

    def DELETEdatabase(self):
          client = MongoClient('localhost:27017')
          db = client.aplikasirumahsakit
          col = db.DataBJanjiBertemu
          
          JanjiID = self.id_input_bar.text()
          col.delete_many({"ID":JanjiID})
          print ('\nDeletion successful\n')
          
    #view
    def setupUi(self, ManagementJanjiBertemu):
        ManagementJanjiBertemu.setObjectName("ManagementJanjiBertemu")
        ManagementJanjiBertemu.resize(1200, 600)
        ManagementJanjiBertemu.setStyleSheet("background-color:rgb(240, 248, 255);\n"
"color:rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(ManagementJanjiBertemu)
        self.centralwidget.setObjectName("centralwidget")
        self.ManagementDokter_label = QtWidgets.QLabel(self.centralwidget)
        self.ManagementDokter_label.setGeometry(QtCore.QRect(0, 0, 1201, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ManagementDokter_label.setFont(font)
        self.ManagementDokter_label.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.ManagementDokter_label.setObjectName("ManagementDokter_label")
        self.aboutus_button = QtWidgets.QPushButton(self.centralwidget)
        self.aboutus_button.setGeometry(QtCore.QRect(1090, 10, 91, 41))
        self.aboutus_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.aboutus_button.setObjectName("aboutus_button")

        #controller
        self.aboutus_button.clicked.connect(self.openaboutus)
        #-----------------------------------------------------------------
        
        self.iddokter_label = QtWidgets.QLabel(self.centralwidget)
        self.iddokter_label.setGeometry(QtCore.QRect(60, 110, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.iddokter_label.setFont(font)
        self.iddokter_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.iddokter_label.setObjectName("iddokter_label")
        self.iddokter_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.iddokter_input_bar.setGeometry(QtCore.QRect(60, 150, 321, 31))
        self.iddokter_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.iddokter_input_bar.setText("")
        self.iddokter_input_bar.setObjectName("iddokter_input_bar")
        self.namadokter_label = QtWidgets.QLabel(self.centralwidget)
        self.namadokter_label.setGeometry(QtCore.QRect(50, 200, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.namadokter_label.setFont(font)
        self.namadokter_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.namadokter_label.setObjectName("namadokter_label")
        self.namadokter_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.namadokter_input_bar.setGeometry(QtCore.QRect(60, 240, 321, 31))
        self.namadokter_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.namadokter_input_bar.setObjectName("namadokter_input_bar")
        self.specialization_label = QtWidgets.QLabel(self.centralwidget)
        self.specialization_label.setGeometry(QtCore.QRect(60, 290, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.specialization_label.setFont(font)
        self.specialization_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.specialization_label.setObjectName("specialization_label")
        self.specialization_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.specialization_input_bar.setGeometry(QtCore.QRect(60, 330, 321, 31))
        self.specialization_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.specialization_input_bar.setObjectName("specialization_input_bar")
        self.harikerja_label = QtWidgets.QLabel(self.centralwidget)
        self.harikerja_label.setGeometry(QtCore.QRect(60, 380, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.harikerja_label.setFont(font)
        self.harikerja_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.harikerja_label.setObjectName("harikerja_label")
        self.harikerja_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.harikerja_input_bar.setGeometry(QtCore.QRect(60, 420, 321, 31))
        self.harikerja_input_bar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.harikerja_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.harikerja_input_bar.setText("")
        self.harikerja_input_bar.setObjectName("harikerja_input_bar")
        self.jamkerja_label = QtWidgets.QLabel(self.centralwidget)
        self.jamkerja_label.setGeometry(QtCore.QRect(650, 110, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.jamkerja_label.setFont(font)
        self.jamkerja_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.jamkerja_label.setObjectName("jamkerja_label")
        self.jamkerja_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.jamkerja_input_bar.setGeometry(QtCore.QRect(650, 150, 321, 31))
        self.jamkerja_input_bar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.jamkerja_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.jamkerja_input_bar.setText("")
        self.jamkerja_input_bar.setObjectName("jamkerja_input_bar")
        self.namapasien1_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.namapasien1_input_bar.setGeometry(QtCore.QRect(650, 240, 321, 31))
        self.namapasien1_input_bar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.namapasien1_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.namapasien1_input_bar.setText("")
        self.namapasien1_input_bar.setObjectName("namapasien1_input_bar")
        self.namapasien1_label = QtWidgets.QLabel(self.centralwidget)
        self.namapasien1_label.setGeometry(QtCore.QRect(650, 200, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.namapasien1_label.setFont(font)
        self.namapasien1_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.namapasien1_label.setObjectName("namapasien1_label")
        self.namapasien2_label = QtWidgets.QLabel(self.centralwidget)
        self.namapasien2_label.setGeometry(QtCore.QRect(650, 290, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.namapasien2_label.setFont(font)
        self.namapasien2_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.namapasien2_label.setObjectName("namapasien2_label")
        self.namapasien2_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.namapasien2_input_bar.setGeometry(QtCore.QRect(650, 330, 321, 31))
        self.namapasien2_input_bar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.namapasien2_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.namapasien2_input_bar.setText("")
        self.namapasien2_input_bar.setObjectName("namapasien2_input_bar")
        self.namapasien3_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.namapasien3_input_bar.setGeometry(QtCore.QRect(650, 420, 321, 31))
        self.namapasien3_input_bar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.namapasien3_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.namapasien3_input_bar.setText("")
        self.namapasien3_input_bar.setObjectName("namapasien3_input_bar")
        self.namapasien3_label = QtWidgets.QLabel(self.centralwidget)
        self.namapasien3_label.setGeometry(QtCore.QRect(650, 380, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.namapasien3_label.setFont(font)
        self.namapasien3_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.namapasien3_label.setObjectName("namapasien3_label")
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setGeometry(QtCore.QRect(290, 500, 91, 41))
        self.delete_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.delete_button.setObjectName("delete_button")

        #controller
        self.delete_button.clicked.connect(self.DELETEdatabase)
        #--------------------------------------------------------------------
        self.update_button = QtWidgets.QPushButton(self.centralwidget)
        self.update_button.setGeometry(QtCore.QRect(490, 500, 91, 41))
        self.update_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.update_button.setObjectName("update_button")

        #controller
        self.update_button.clicked.connect(self.UPDATEdatabase)
        #----------------------------------------------------------------------
        
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(700, 500, 91, 41))
        self.submit_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.submit_button.setObjectName("submit_button")

        #Controller
        self.submit_button.clicked.connect(self.POSTdatabase)
         #-----------------------------------------------------------------
        self.view_button = QtWidgets.QPushButton(self.centralwidget)
        self.view_button.setGeometry(QtCore.QRect(980, 500, 91, 41))
        self.view_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.view_button.setObjectName("view_button")

        #controller
        self.view_button.clicked.connect(self.openmanagementjanjibertemudatabase)
         #-------------------------------------------------------------------------------------------
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(30, 500, 91, 41))
        self.back_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.back_button.setObjectName("back_button")

        #controller
        self.back_button.clicked.connect(self.closebutton)
        #-----------------------------------------------------------
        ManagementJanjiBertemu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ManagementJanjiBertemu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        ManagementJanjiBertemu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ManagementJanjiBertemu)
        self.statusbar.setObjectName("statusbar")
        ManagementJanjiBertemu.setStatusBar(self.statusbar)

        self.retranslateUi(ManagementJanjiBertemu)
        QtCore.QMetaObject.connectSlotsByName(ManagementJanjiBertemu)

    def retranslateUi(self, ManagementJanjiBertemu):
        _translate = QtCore.QCoreApplication.translate
        ManagementJanjiBertemu.setWindowTitle(_translate("ManagementJanjiBertemu", "MainWindow"))
        self.ManagementDokter_label.setText(_translate("ManagementJanjiBertemu", "    MANAGEMENT JANJI BERTEMU"))
        self.aboutus_button.setText(_translate("ManagementJanjiBertemu", "ABOUT US"))
        self.iddokter_label.setText(_translate("ManagementJanjiBertemu", "ID DOKTER"))
        self.namadokter_label.setText(_translate("ManagementJanjiBertemu", "   NAMA DOKTER"))
        self.specialization_label.setText(_translate("ManagementJanjiBertemu", "SPECIALIZATION"))
        self.harikerja_label.setText(_translate("ManagementJanjiBertemu", "HARI KERJA"))
        self.jamkerja_label.setText(_translate("ManagementJanjiBertemu", "JAM KERJA"))
        self.namapasien1_label.setText(_translate("ManagementJanjiBertemu", "NAMA PASIEN 1"))
        self.namapasien2_label.setText(_translate("ManagementJanjiBertemu", "NAMA PASIEN 2"))
        self.namapasien3_label.setText(_translate("ManagementJanjiBertemu", "NAMA PASIEN 3"))
        self.delete_button.setText(_translate("ManagementJanjiBertemu", "DELETE"))
        self.update_button.setText(_translate("ManagementJanjiBertemu", "UPDATE"))
        self.submit_button.setText(_translate("ManagementJanjiBertemu", "SUBMIT"))
        self.view_button.setText(_translate("ManagementJanjiBertemu", "VIEW"))
        self.back_button.setText(_translate("ManagementJanjiBertemu", "BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ManagementJanjiBertemu = QtWidgets.QMainWindow()
    ui = Ui_ManagementJanjiBertemu()
    ui.setupUi(ManagementJanjiBertemu)
    ManagementJanjiBertemu.show()
    sys.exit(app.exec_())
