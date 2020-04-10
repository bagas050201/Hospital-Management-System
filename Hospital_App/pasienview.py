#view
from PyQt5 import QtCore, QtGui, QtWidgets
#controller
from dataformpasien import Ui_dataformpasien
from managementjanjibertemudatabase import Ui_managementjanjibertemudatabase
from aboutus import Ui_aboutus

class Ui_pasienview(object):
    #controller
    def opendataformpasien(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_dataformpasien()
        self.ui.setupUi(self.window)
        self.window.show()

    def openmanagementjanjibertemudatabase(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_managementjanjibertemudatabase()
        self.ui.setupUi(self.window)
        self.window.show()

    def openaboutus(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_aboutus()
        self.ui.setupUi(self.window)
        self.window.show()
    #view
    def setupUi(self, pasienview):
        pasienview.setObjectName("pasienview")
        pasienview.resize(1200, 600)
        self.centralwidget = QtWidgets.QWidget(pasienview)
        self.centralwidget.setObjectName("centralwidget")
        self.pasienview_label = QtWidgets.QLabel(self.centralwidget)
        self.pasienview_label.setGeometry(QtCore.QRect(0, 0, 1201, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pasienview_label.setFont(font)
        self.pasienview_label.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(127, 186, 0)")
        self.pasienview_label.setObjectName("pasienview_label")
        self.aboutus_button = QtWidgets.QPushButton(self.centralwidget)
        self.aboutus_button.setGeometry(QtCore.QRect(1090, 10, 91, 41))
        self.aboutus_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(127, 186, 0)")
        self.aboutus_button.setObjectName("aboutus_button")
        #controller
        self.aboutus_button.clicked.connect(self.openaboutus)
        #----------------------------------------------------------------
        self.permintaanpharmacist_button = QtWidgets.QPushButton(self.centralwidget)
        self.permintaanpharmacist_button.setGeometry(QtCore.QRect(640, 210, 241, 151))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.permintaanpharmacist_button.setFont(font)
        self.permintaanpharmacist_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.permintaanpharmacist_button.setObjectName("permintaanpharmacist_button")
        #controller
        self.permintaanpharmacist_button.clicked.connect(self.opendataformpasien)
        #-------------------------------------------------------------------------------------------
        self.permintaanpharmacist_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.permintaanpharmacist_button_2.setGeometry(QtCore.QRect(310, 210, 241, 151))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.permintaanpharmacist_button_2.setFont(font)
        self.permintaanpharmacist_button_2.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.permintaanpharmacist_button_2.setObjectName("permintaanpharmacist_button_2")
        #con troller
        self.permintaanpharmacist_button_2.clicked.connect(self.openmanagementjanjibertemudatabase)
        #--------------------------------------------------------------------------------------------------------------------
        pasienview.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(pasienview)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        pasienview.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(pasienview)
        self.statusbar.setObjectName("statusbar")
        pasienview.setStatusBar(self.statusbar)

        self.retranslateUi(pasienview)
        QtCore.QMetaObject.connectSlotsByName(pasienview)

    def retranslateUi(self, pasienview):
        _translate = QtCore.QCoreApplication.translate
        pasienview.setWindowTitle(_translate("pasienview", "MainWindow"))
        self.pasienview_label.setText(_translate("pasienview", "  HALLO SELAMAT DATANG DI LAMAN RESMI RUMAH SAKIT"))
        self.aboutus_button.setText(_translate("pasienview", "ABOUT US"))
        self.permintaanpharmacist_button.setText(_translate("pasienview", "PENGISIAN FORM CALON PASIEN"))
        self.permintaanpharmacist_button_2.setText(_translate("pasienview", "CEK JANJI BERTEMU DOKTER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pasienview = QtWidgets.QMainWindow()
    ui = Ui_pasienview()
    ui.setupUi(pasienview)
    pasienview.show()
    sys.exit(app.exec_())
