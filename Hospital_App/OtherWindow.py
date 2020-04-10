#view
from PyQt5 import QtCore, QtGui, QtWidgets
#controler
from SignupWindow import Ui_SignupWindow
from ManagementView import Ui_ManagementView
from pasienview import Ui_pasienview
from pharmacistadminview import Ui_pharmacistadminview
from dokterview import Ui_dokterview
from pymongo import MongoClient

class Ui_OtherWindow(object):

    #controler to view
    def OpenSignupWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SignupWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def signUpCheck(self):
        print(" Sign Up Button Clicked !")
        self.OpenSignupWindow()
        
    def OpenManagementView(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ManagementView()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def OpenPasienView(self):
          self.window = QtWidgets.QMainWindow()
          self.ui = Ui_pasienview()
          self.ui.setupUi(self.window)
          self.window.show()

    def OpenPharmacistadminVew(Self):
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
    def GetDatabase(self):
        client = MongoClient('localhost:27017')
        db = client.aplikasirumahsakit
        col = db.SIGNUP

        LoginUSERNAME = self.username_input_bar.text()
        LoginPASSWORD = self.password_input_bar.text()

        check = col.find_one({"USERNAME":LoginUSERNAME,"PASSWORD": LoginPASSWORD})
        if check != None :
            print("User Found !")
            print("check")
            if (check["TYPE"] == "admin"):
                print("User admin ! ")
                self.OpenManagementView()
            elif(check["TYPE"] == "pengunjung"):
                print("User pengunjung ! ")
                self.OpenPasienView()
            elif(check["TYPE"] == "pharmacist"):
                print("User pharmacist ! ")
                self.OpenPharmacistadminVew()
            elif (check["TYPE"] == "dokter"):
                print("User dokter ! ")
                self.Opendokterview()
        else:
            print("User Not Found !")
            self.showMessageBox('Warning','Invalid Username And Password')
          
    #View 
    def setupUi(self, OtherWindow):
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.resize(1006, 502)
        OtherWindow.setStyleSheet("background-color:rgb(240, 255, 255);\n"
"color:rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(OtherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 40, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgb(0, 191, 255)")
        self.label.setObjectName("label")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(320, 160, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.username_label.setFont(font)
        self.username_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(320, 240, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.password_label.setFont(font)
        self.password_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.password_label.setObjectName("password_label")
        self.username_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.username_input_bar.setGeometry(QtCore.QRect(470, 160, 161, 22))
        self.username_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.username_input_bar.setText("")
        self.username_input_bar.setObjectName("username_input_bar")
        self.password_input_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input_bar.setGeometry(QtCore.QRect(470, 240, 161, 22))
        self.password_input_bar.setStyleSheet("color:rgb(0, 0, 0)")
        self.password_input_bar.setObjectName("password_input_bar")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(360, 370, 93, 28))
        self.login_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.login_button.setObjectName("login_button")
        
        #controler (open ManagementView)
        self.login_button.clicked.connect(self.GetDatabase)
        #------------------------------------------------------------------------
        self.signout_button = QtWidgets.QPushButton(self.centralwidget)
        self.signout_button.setGeometry(QtCore.QRect(530, 370, 93, 28))
        self.signout_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.signout_button.setObjectName("signout_button")
        
        #controler (Open Signup Window)
        self.signout_button.clicked.connect(self.signUpCheck)
         #--------------------------------------------------------------
        OtherWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OtherWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1006, 26))
        self.menubar.setObjectName("menubar")
        OtherWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OtherWindow)
        self.statusbar.setObjectName("statusbar")
        OtherWindow.setStatusBar(self.statusbar)

        self.retranslateUi(OtherWindow)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow)

    def retranslateUi(self, OtherWindow):
        _translate = QtCore.QCoreApplication.translate
        OtherWindow.setWindowTitle(_translate("OtherWindow", "MainWindow"))
        self.label.setText(_translate("OtherWindow", " MANAGEMENT RUMAH SAKIT LOGIN FORM"))
        self.username_label.setText(_translate("OtherWindow", "    USERNAME"))
        self.password_label.setText(_translate("OtherWindow", "    PASSWORD"))
        self.login_button.setText(_translate("OtherWindow", "LOGIN"))
        self.signout_button.setText(_translate("OtherWindow", "SIGN UP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow = QtWidgets.QMainWindow()
    ui = Ui_OtherWindow()
    ui.setupUi(OtherWindow)
    OtherWindow.show()
    sys.exit(app.exec_())
