#view
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
#controller
from pharmacistdatabase import Ui_pharmacistdatabase
from managementstokbarang import Ui_managementstokbarang
from aboutus import Ui_aboutus

class Ui_managementpharmacist(object):
    #controller
    def openaboutus(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_aboutus()
        self.ui.setupUi(self.window)
        self.window.show()

    def openmanagementstokbarang(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_managementstokbarang()
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

    #view
    def setupUi(self, managementpharmacist):
        managementpharmacist.setObjectName("managementpharmacist")
        managementpharmacist.resize(1200, 600)
        self.centralwidget = QtWidgets.QWidget(managementpharmacist)
        self.centralwidget.setObjectName("centralwidget")
        self.Managementpharmacist_label = QtWidgets.QLabel(self.centralwidget)
        self.Managementpharmacist_label.setGeometry(QtCore.QRect(0, 0, 1201, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Managementpharmacist_label.setFont(font)
        self.Managementpharmacist_label.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(255, 196, 0)")
        self.Managementpharmacist_label.setObjectName("Managementpharmacist_label")
        self.aboutus_button = QtWidgets.QPushButton(self.centralwidget)
        self.aboutus_button.setGeometry(QtCore.QRect(1090, 10, 91, 41))
        self.aboutus_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(255, 196, 0)")
        self.aboutus_button.setObjectName("aboutus_button")

        #controller
        self.aboutus_button.clicked.connect(self.openaboutus)
        #----------------------------------------------------------------
        
        self.stokbarang_button = QtWidgets.QPushButton(self.centralwidget)
        self.stokbarang_button.setGeometry(QtCore.QRect(340, 210, 221, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stokbarang_button.setFont(font)
        self.stokbarang_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.stokbarang_button.setObjectName("stokbarang_button")

        #controller
        self.stokbarang_button.clicked.connect(self.openmanagementstokbarang)
        #--------------------------------------------------------------------------------------
        self.permintaanpharmacist_button = QtWidgets.QPushButton(self.centralwidget)
        self.permintaanpharmacist_button.setGeometry(QtCore.QRect(640, 210, 221, 151))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.permintaanpharmacist_button.setFont(font)
        self.permintaanpharmacist_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.permintaanpharmacist_button.setObjectName("permintaanpharmacist_button")

        #controller
        self.permintaanpharmacist_button.clicked.connect(self.openpharmacistdatabase)
        #------------------------------------------------------------------------------------------------
        
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(50, 470, 91, 41))
        self.back_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.back_button.setObjectName("back_button")

        #controller
        self.back_button.clicked.connect(self.closebutton)
        #------------------------------------------------------------
        managementpharmacist.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(managementpharmacist)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        managementpharmacist.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(managementpharmacist)
        self.statusbar.setObjectName("statusbar")
        managementpharmacist.setStatusBar(self.statusbar)

        self.retranslateUi(managementpharmacist)
        QtCore.QMetaObject.connectSlotsByName(managementpharmacist)

    def retranslateUi(self, managementpharmacist):
        _translate = QtCore.QCoreApplication.translate
        managementpharmacist.setWindowTitle(_translate("managementpharmacist", "MainWindow"))
        self.Managementpharmacist_label.setText(_translate("managementpharmacist", "    MANAGEMENT PHARMACIST"))
        self.aboutus_button.setText(_translate("managementpharmacist", "ABOUT US"))
        self.stokbarang_button.setText(_translate("managementpharmacist", "STOK BARANG"))
        self.permintaanpharmacist_button.setText(_translate("managementpharmacist", "PERMINTAAN PHARMACIST"))
        self.back_button.setText(_translate("managementpharmacist", "BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    managementpharmacist = QtWidgets.QMainWindow()
    ui = Ui_managementpharmacist()
    ui.setupUi(managementpharmacist)
    managementpharmacist.show()
    sys.exit(app.exec_())
