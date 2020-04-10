#view
from PyQt5 import QtCore, QtGui, QtWidgets
#controller
from  ManagementView import Ui_ManagementView
from pasienview import Ui_pasienview
from pharmacistadminview import Ui_pharmacistadminview
from dokterview import Ui_dokterview
from pymongo import MongoClient

class Ui_SignupWindow(object):
     #controller to view
     def OpenWindow(self):
          self.window = QtWidgets.QMainWindow()
          self.ui = Ui_ManagementView()
          self.ui.setupUi(self.window)
          self.window.show()

     def OpenPasienView(self):
          self.window = QtWidgets.QMainWindow()
          self.ui = Ui_pasienview()
          self.ui.setupUi(self.window)
          self.window.show()

     def OpenPharmacistadminvVew(self):
          self.window = QtWidgets.QMainWindow()
          self.ui = Ui_pharmacistadminview()
          self.ui.setupUi(self.window)
          self.window.show()

     def Opendokterview(self):
          self.window = QtWidgets.QMainWindow()
          self.ui = Ui_dokterview()
          self.ui.setupUi(self.window)
          self.window.show()

     #controller to Model
     def POSTdatabase(self):
          client = MongoClient('localhost:27017')
          db = client.aplikasirumahsakit
          col = db.SIGNUP
          
          SignupNAME = self.name_input_bar.text()
          SignupTYPE = self.type_input_bar.text()
          SignupALAMAT = self.alamat_input_bar.text()
          SignupUSERNAME = self.username_input_bar.text()
          SignupGENDER = self.gender_input_bar.text()
          SignupPASSWORD = self.password_input_bar.text()

          col.insert_one(
            {
                "NAME": SignupNAME,
                "TYPE":SignupTYPE,
                "ALAMAT":SignupALAMAT,
                "USERNAME":SignupUSERNAME,
                "GENDER": SignupGENDER,
                "PASSWORD": SignupPASSWORD,
                })
          print ('\nInserted data successfully\n')

          if (SignupTYPE == "admin"):
               self.OpenWindow()
          elif(SignupTYPE == "pengunjung"):
               self.OpenPasienView()
          elif(SignupTYPE == "pharmacist"):
               self.OpenPharmacistadminvVew()
          elif (SignupTYPE == "dokter"):
               self.Opendokterview()
               
     #view
     def setupUi(self, SignupWindow):
        SignupWindow.setObjectName("SignupWindow")
        SignupWindow.resize(1007, 502)
        SignupWindow.setStyleSheet("background-color:rgb(240, 248, 255);\n"
"color:rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(SignupWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.signup_label = QtWidgets.QLabel(self.centralwidget)
        self.signup_label.setGeometry(QtCore.QRect(310, 20, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.signup_label.setFont(font)
        self.signup_label.setStyleSheet("background-color:rgb(0, 191, 255)")
        self.signup_label.setObjectName("signup_label")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(30, 120, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.name_label.setFont(font)
        self.name_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.name_label.setObjectName("name_label")
        self.name_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.name_input_bar.setGeometry(QtCore.QRect(50, 170, 321, 31))
        self.name_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.name_input_bar.setText("")
        self.name_input_bar.setObjectName("name_input_bar")
        self.type_label = QtWidgets.QLabel(self.centralwidget)
        self.type_label.setGeometry(QtCore.QRect(30, 230, 350, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.type_label.setFont(font)
        self.type_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.type_label.setObjectName("type_label")
        self.type_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.type_input_bar.setGeometry(QtCore.QRect(50, 280, 321, 31))
        self.type_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.type_input_bar.setObjectName("type_input_bar")
        self.alamat_label = QtWidgets.QLabel(self.centralwidget)
        self.alamat_label.setGeometry(QtCore.QRect(50, 330, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.alamat_label.setFont(font)
        self.alamat_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.alamat_label.setObjectName("alamat_label")
        self.alamat_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.alamat_input_bar.setGeometry(QtCore.QRect(50, 370, 321, 31))
        self.alamat_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.alamat_input_bar.setObjectName("alamat_input_bar")
        self.law_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.law_radio.setGeometry(QtCore.QRect(40, 420, 461, 31))
        self.law_radio.setStyleSheet("color:rgb(0, 0, 0);")
        self.law_radio.setObjectName("law_radio")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(530, 130, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.username_label.setFont(font)
        self.username_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.username_label.setObjectName("username_label")
        self.username_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.username_input_bar.setGeometry(QtCore.QRect(550, 170, 321, 31))
        self.username_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.username_input_bar.setObjectName("username_input_bar")
        self.gender_label = QtWidgets.QLabel(self.centralwidget)
        self.gender_label.setGeometry(QtCore.QRect(530, 230, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.gender_label.setFont(font)
        self.gender_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.gender_label.setObjectName("gender_label")
        self.gender_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.gender_input_bar.setGeometry(QtCore.QRect(550, 280, 321, 31))
        self.gender_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.gender_input_bar.setObjectName("gender_input_bar")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(550, 330, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.password_label.setFont(font)
        self.password_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.password_label.setObjectName("password_label")
        self.password_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input_bar.setGeometry(QtCore.QRect(550, 370, 321, 31))
        self.password_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.password_input_bar.setObjectName("password_input_bar")
        self.create_button = QtWidgets.QPushButton(self.centralwidget)
        self.create_button.setGeometry(QtCore.QRect(780, 420, 93, 28))
        self.create_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.create_button.setObjectName("create_button")
          #controller
        self.create_button.clicked.connect(self.POSTdatabase)
        #---------------------------------------------------------------
        SignupWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SignupWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1007, 26))
        self.menubar.setObjectName("menubar")
        SignupWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SignupWindow)
        self.statusbar.setObjectName("statusbar")
        SignupWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SignupWindow)
        QtCore.QMetaObject.connectSlotsByName(SignupWindow)

     def retranslateUi(self, SignupWindow):
        _translate = QtCore.QCoreApplication.translate
        SignupWindow.setWindowTitle(_translate("SignupWindow", "MainWindow"))
        self.signup_label.setText(_translate("SignupWindow", "                        SIGN UP FORM"))
        self.name_label.setText(_translate("SignupWindow", "    NAME"))
        self.type_label.setText(_translate("SignupWindow", "    TYPE : admin / pengunjung / pharmacist / dokter"))
        self.alamat_label.setText(_translate("SignupWindow", "ALAMAT"))
        self.law_radio.setText(_translate("SignupWindow", "SAYA MEMATUHI SEGALA PERATURAN YANG ADA PADA RUMAH SAKIT INI"))
        self.username_label.setText(_translate("SignupWindow", "    USERNAME"))
        self.gender_label.setText(_translate("SignupWindow", "    GENDER"))
        self.password_label.setText(_translate("SignupWindow", "PASSWORD"))
        self.create_button.setText(_translate("SignupWindow", "CREATE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignupWindow = QtWidgets.QMainWindow()
    ui = Ui_SignupWindow()
    ui.setupUi(SignupWindow)
    SignupWindow.show()
    sys.exit(app.exec_())
