#view
from PyQt5 import QtCore, QtGui, QtWidgets
#controller
from aboutus import Ui_aboutus
from ManagementDokter import Ui_ManagementDokter
from ManagementJanjiBertemu import Ui_ManagementJanjiBertemu
from managementpharmacist import Ui_managementpharmacist
from databasepasien import Ui_databasepasien

class Ui_ManagementView(object):
    #controller
    def openaboutus(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_aboutus()
        self.ui.setupUi(self.window)
        self.window.show()

    def openManagementDokter(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ManagementDokter()
        self.ui.setupUi(self.window)
        self.window.show()

    def openManagementJanjiBertemu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ManagementJanjiBertemu()
        self.ui.setupUi(self.window)
        self.window.show()

    def opendatabasepasien(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_databasepasien()
        self.ui.setupUi(self.window)
        self.window.show()

    def openmanagementpharmacist(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_managementpharmacist()
        self.ui.setupUi(self.window)
        self.window.show()
    #view
    def setupUi(self, ManagementView):
        ManagementView.setObjectName("ManagementView")
        ManagementView.resize(1200, 600)
        ManagementView.setStyleSheet("background-color:rgb(240, 248, 255);\n"
"color:rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(ManagementView)
        self.centralwidget.setObjectName("centralwidget")
        self.signup_label = QtWidgets.QLabel(self.centralwidget)
        self.signup_label.setGeometry(QtCore.QRect(0, 0, 1201, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.signup_label.setFont(font)
        self.signup_label.setStyleSheet("background-color:rgb(0, 191, 255)")
        self.signup_label.setObjectName("signup_label")
        self.create_button = QtWidgets.QPushButton(self.centralwidget)
        self.create_button.setGeometry(QtCore.QRect(1080, 10, 91, 41))
        self.create_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.create_button.setObjectName("create_button")
        #controller
        self.create_button.clicked.connect(self.openaboutus)
         #--------------------------------------------------------------
        self.create_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.create_button_2.setGeometry(QtCore.QRect(410, 140, 181, 141))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.create_button_2.setFont(font)
        self.create_button_2.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(246, 61, 19)")
        self.create_button_2.setObjectName("create_button_2")
        #controller
        self.create_button_2.clicked.connect(self.openManagementDokter)
        #--------------------------------------------------------------------------------
        self.create_button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.create_button_3.setGeometry(QtCore.QRect(600, 140, 181, 141))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.create_button_3.setFont(font)
        self.create_button_3.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(105, 225, 0)")
        self.create_button_3.setObjectName("create_button_3")
        #controller
        self.create_button_3.clicked.connect(self. opendatabasepasien)
         #---------------------------------------------------------------------------
        self.create_button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.create_button_4.setGeometry(QtCore.QRect(600, 290, 181, 141))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.create_button_4.setFont(font)
        self.create_button_4.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(255, 187, 0)")
        self.create_button_4.setObjectName("create_button_4")
        #controller
        self.create_button_4.clicked.connect(self.openmanagementpharmacist)
        #-----------------------------------------------------------------------------------
        self.create_button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.create_button_5.setGeometry(QtCore.QRect(410, 290, 181, 141))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.create_button_5.setFont(font)
        self.create_button_5.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 212, 255)")
        self.create_button_5.setObjectName("create_button_5")
        #controller
        self.create_button_5.clicked.connect(self.openManagementJanjiBertemu)
        #----------------------------------------------------------------------------------------
        ManagementView.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ManagementView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        ManagementView.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ManagementView)
        self.statusbar.setObjectName("statusbar")
        ManagementView.setStatusBar(self.statusbar)

        self.retranslateUi(ManagementView)
        QtCore.QMetaObject.connectSlotsByName(ManagementView)

    def retranslateUi(self, ManagementView):
        _translate = QtCore.QCoreApplication.translate
        ManagementView.setWindowTitle(_translate("ManagementView", "MainWindow"))
        self.signup_label.setText(_translate("ManagementView", "    MANAGEMENT RUMAH SAKIT"))
        self.create_button.setText(_translate("ManagementView", "ABOUT US"))
        self.create_button_2.setText(_translate("ManagementView", "DOKTER"))
        self.create_button_3.setText(_translate("ManagementView", "PASIEN"))
        self.create_button_4.setText(_translate("ManagementView", "PHARMACIST"))
        self.create_button_5.setText(_translate("ManagementView", "JANJI BERTEMU"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ManagementView = QtWidgets.QMainWindow()
    ui = Ui_ManagementView()
    ui.setupUi(ManagementView)
    ManagementView.show()
    sys.exit(app.exec_())
