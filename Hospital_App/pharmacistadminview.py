#view
from PyQt5 import QtCore, QtGui, QtWidgets
#controller
from aboutus import Ui_aboutus
from kebutuhanpharmacist import Ui_kebutuhanpharmacist
from stokbarangdatabase import Ui_stokbarangdatabase

class Ui_pharmacistadminview(object):
    #controller
    def openaboutus(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_aboutus()
        self.ui.setupUi(self.window)
        self.window.show()

    def openkebutuhanpharmacist(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_kebutuhanpharmacist()
        self.ui.setupUi(self.window)
        self.window.show()

    def openstokbarangdatabase(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_stokbarangdatabase()
        self.ui.setupUi(self.window)
        self.window.show()
    #view
    def setupUi(self, pharmacistadminview):
        pharmacistadminview.setObjectName("pharmacistadminview")
        pharmacistadminview.resize(1200, 600)
        self.centralwidget = QtWidgets.QWidget(pharmacistadminview)
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
        self.cekstokbarang_button = QtWidgets.QPushButton(self.centralwidget)
        self.cekstokbarang_button.setGeometry(QtCore.QRect(340, 210, 221, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cekstokbarang_button.setFont(font)
        self.cekstokbarang_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.cekstokbarang_button.setObjectName("cekstokbarang_button")
        #controller
        self.cekstokbarang_button.clicked.connect(self.openstokbarangdatabase)
        #---------------------------------------------------------------------------------------
        self.permintaanpharmacist_button = QtWidgets.QPushButton(self.centralwidget)
        self.permintaanpharmacist_button.setGeometry(QtCore.QRect(640, 210, 221, 151))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.permintaanpharmacist_button.setFont(font)
        self.permintaanpharmacist_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.permintaanpharmacist_button.setObjectName("permintaanpharmacist_button")
        #controller
        self.permintaanpharmacist_button.clicked.connect(self.openkebutuhanpharmacist)
        #--------------------------------------------------------------------------------------------------
        pharmacistadminview.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(pharmacistadminview)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        pharmacistadminview.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(pharmacistadminview)
        self.statusbar.setObjectName("statusbar")
        pharmacistadminview.setStatusBar(self.statusbar)

        self.retranslateUi(pharmacistadminview)
        QtCore.QMetaObject.connectSlotsByName(pharmacistadminview)

    def retranslateUi(self, pharmacistadminview):
        _translate = QtCore.QCoreApplication.translate
        pharmacistadminview.setWindowTitle(_translate("pharmacistadminview", "MainWindow"))
        self.Managementpharmacist_label.setText(_translate("pharmacistadminview", "    MANAGEMENT PHARMACIST"))
        self.aboutus_button.setText(_translate("pharmacistadminview", "ABOUT US"))
        self.cekstokbarang_button.setText(_translate("pharmacistadminview", "CEK STOK BARANG"))
        self.permintaanpharmacist_button.setText(_translate("pharmacistadminview", "PERMINTAAN PHARMACIST"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pharmacistadminview = QtWidgets.QMainWindow()
    ui = Ui_pharmacistadminview()
    ui.setupUi(pharmacistadminview)
    pharmacistadminview.show()
    sys.exit(app.exec_())
