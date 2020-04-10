#view
from PyQt5 import QtCore, QtGui, QtWidgets
#controller
from OtherWindow import Ui_OtherWindow

class Ui_MainWindow(object):
    #controller
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    #view
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1006, 502)
        MainWindow.setStyleSheet("background-color:rgb(240, 248, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1001, 502))
        self.label.setStyleSheet("background-color:rgb(240, 248, 255);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../ular.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 90, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:rgb(0, 206, 209);\n"
"color:rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.btn_open = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open.setGeometry(QtCore.QRect(810, 400, 141, 51))
        self.btn_open.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 206, 209);")
        self.btn_open.setObjectName("btn_open")

        #controller
        self.btn_open.clicked.connect(self.openWindow)
        #-----------------------------------------------------------
        
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(500, 170, 451, 201))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "   Selamat Datang!"))
        self.btn_open.setText(_translate("MainWindow", "KLIK DISINI"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Open Sans\'; font-size:12pt; color:#00009a; background-color:#ffffff;\">Hospital Management System  Rumah Sakit ILMU KOMPUTER UNJ </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Open Sans\'; font-size:10pt; color:#383838; background-color:#ffffff;\">Aplikasi  ini dimaksudkan sebagai sarana yang </span><span style=\" font-family:\'-apple-system\'; font-size:10pt; color:#383838; background-color:#ffffff;\">meng-integrasikan segala kegiatan yang ada pada rumah sakit kedalam satu Lokasi. Sehingga segala kegiatan yang ada didalam rumah sakit tersebut, dapat dirangkai dan di record kedalam system aplikasi. Hal ini memungkinkan proses kegiatan yang ada pada rumah sakit tersebut menjadi lebih terstruktur, efisien, serta meminimalkan kejadian miss-communication antar proccess yang ada didalam rumah sakit tersebut.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'-apple-system\'; font-size:10pt; color:#383838; background-color:#ffffff;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Open Sans\'; font-size:8pt; color:#666666; background-color:#ffffff;\">Kritik dan saran terhadap kekurangan dan kesalahan yang ada, sangat saya harapkan guna penyempurnaan Aplikasi ini dimasa akan datang. Semoga Aplikasi ini memberikan manfaat bagi kita semua.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Open Sans\'; font-size:8pt; color:#666666; background-color:#ffffff;\">Terima kasih.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Open Sans\'; font-size:8pt; color:#000000; background-color:#ffffff;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Open Sans\'; font-size:10pt; color:#000000; background-color:#ffffff;\">Muhammad Bagas Pradana 1313618015</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
