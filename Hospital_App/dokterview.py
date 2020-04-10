
from PyQt5 import QtCore, QtGui, QtWidgets
from stokbarangdatabase import Ui_stokbarangdatabase
from aboutus import Ui_aboutus
from  managementjanjibertemudatabase import  Ui_managementjanjibertemudatabase

class Ui_dokterview(object):

     #controller to view
     def openaboutus(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_aboutus()
        self.ui.setupUi(self.window)
        self.window.show()

     def Opendaftarobatdatabase(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_stokbarangdatabase()
        self.ui.setupUi(self.window)
        self.window.show()

     def Openjanjibertemudokterpasiendatabase(self):
        self.window = QtWidgets.QMainWindow()
        self.ui =  Ui_managementjanjibertemudatabase()
        self.ui.setupUi(self.window)
        self.window.show()

     #view
     def setupUi(self, dokterview):
        dokterview.setObjectName("dokterview")
        dokterview.resize(1200, 600)
        dokterview.setStyleSheet("background-color:rgb(240, 248, 255);")
        self.centralwidget = QtWidgets.QWidget(dokterview)
        self.centralwidget.setObjectName("centralwidget")
        self.dokterview_label = QtWidgets.QLabel(self.centralwidget)
        self.dokterview_label.setGeometry(QtCore.QRect(0, 0, 1201, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dokterview_label.setFont(font)
        self.dokterview_label.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(72, 209, 204)")
        self.dokterview_label.setObjectName("dokterview_label")
        self.aboutus_button = QtWidgets.QPushButton(self.centralwidget)
        self.aboutus_button.setGeometry(QtCore.QRect(1090, 10, 91, 41))
        self.aboutus_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(176, 196, 222)")
        self.aboutus_button.setObjectName("aboutus_button")

        #controller
        self.aboutus_button.clicked.connect(self.openaboutus)
        #----------------------------------------------------------------
        
        self.cekdaftarobat_button = QtWidgets.QPushButton(self.centralwidget)
        self.cekdaftarobat_button.setGeometry(QtCore.QRect(640, 200, 241, 151))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.cekdaftarobat_button.setFont(font)
        self.cekdaftarobat_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(176, 196, 222)")
        self.cekdaftarobat_button.setObjectName("cekdaftarobat_button")

        #controller
        self.cekdaftarobat_button.clicked.connect(self.Opendaftarobatdatabase)
        #---------------------------------------------------------------------------------------
        
        self.cekjanji_button = QtWidgets.QPushButton(self.centralwidget)
        self.cekjanji_button.setGeometry(QtCore.QRect(330, 200, 241, 151))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.cekjanji_button.setFont(font)
        self.cekjanji_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(176, 196, 222)")
        self.cekjanji_button.setObjectName("cekjanji_button")

        #controller
        self.cekjanji_button.clicked.connect(self.Openjanjibertemudokterpasiendatabase)
        #---------------------------------------------------------------------------------------------------
        
        dokterview.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(dokterview)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        dokterview.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(dokterview)
        self.statusbar.setObjectName("statusbar")
        dokterview.setStatusBar(self.statusbar)

        self.retranslateUi(dokterview)
        QtCore.QMetaObject.connectSlotsByName(dokterview)

     def retranslateUi(self, dokterview):
        _translate = QtCore.QCoreApplication.translate
        dokterview.setWindowTitle(_translate("dokterview", "MainWindow"))
        self.dokterview_label.setText(_translate("dokterview", "  SELAMAT DATANG BAPAK DAN IBU DOKTER YANG KAMI BANGGAKAN"))
        self.aboutus_button.setText(_translate("dokterview", "ABOUT US"))
        self.cekdaftarobat_button.setText(_translate("dokterview", "DAFTAR OBAT RUMAH SAKIT"))
        self.cekjanji_button.setText(_translate("dokterview", "LIHAT JANJI BERTEMU PASIEN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dokterview = QtWidgets.QMainWindow()
    ui = Ui_dokterview()
    ui.setupUi(dokterview)
    dokterview.show()
    sys.exit(app.exec_())
