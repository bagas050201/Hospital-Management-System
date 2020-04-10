#view
from PyQt5 import QtCore, QtGui, QtWidgets
#controler
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox


class Ui_aboutus(object):
    #controler
    def closebutton(self):
        self.back_button.hide()
        msg = QMessageBox()
        msg.setText("mohon close menggunakan tombol silang merah diatas")
        msg.setIcon(QMessageBox.Critical)
        x = msg.exec_()
    #view
    def setupUi(self, aboutus):
        aboutus.setObjectName("aboutus")
        aboutus.resize(1200, 600)
        aboutus.setStyleSheet("background-color:rgb(240, 248, 255);")
        self.centralwidget = QtWidgets.QWidget(aboutus)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(160, 110, 891, 391))
        self.textBrowser.setObjectName("textBrowser")
        self.aboutus_label = QtWidgets.QLabel(self.centralwidget)
        self.aboutus_label.setGeometry(QtCore.QRect(0, 0, 1201, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.aboutus_label.setFont(font)
        self.aboutus_label.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.aboutus_label.setObjectName("aboutus_label")
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(1080, 10, 91, 41))
        self.back_button.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 191, 255)")
        self.back_button.setObjectName("back_button")

        #controler close
        self.back_button.clicked.connect(self.closebutton)
        #-----------------------------------------------------------
        aboutus.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(aboutus)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        aboutus.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(aboutus)
        self.statusbar.setObjectName("statusbar")
        aboutus.setStatusBar(self.statusbar)

        self.retranslateUi(aboutus)
        QtCore.QMetaObject.connectSlotsByName(aboutus)

    def retranslateUi(self, aboutus):
        _translate = QtCore.QCoreApplication.translate
        aboutus.setWindowTitle(_translate("aboutus", "MainWindow"))
        self.textBrowser.setHtml(_translate("aboutus", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:14pt;\">    Nama saya </span><span style=\" font-family:\'Times New Roman\'; font-size:14pt; font-weight:600;\">Muhammad Bagas Pradana</span><span style=\" font-family:\'Times New Roman\'; font-size:14pt;\">, saya saat ini mengenyam Pendidikan di Universitas Negeri Jakarta berkat usaha dan kerja keras saya, akhirnya saya bisa berkuliah disalah satu kampus terbaik di negeri ini. Belajar di kampus tidak harus yang sesuai dengan pilihan yang kita buat diawal, selama kita bisa memanagement waktu kita, kitapun bisa mempelajari banyak hal yang baru diluar bidang studi yang kita pilih ini. Saya berkuliah di jurusan Ilmu Komputer yang pastinya keseharian saya selama berkuliah adalah berinteraksi dengan computer dan juga berinteraksi dengan sesama teman kelas. Saat ini saya mendapatkan kesempatan dimana saya mendapatkan tugas membuat rancangan Aplikasi frontend dan backend menggunakan Python GUI dengan implementasi MVC didalamnya. Memang aplikasi ini belum sempurna,bahkan dikatakan jauh dari kata sempurna. Namun setidaknya saya telah bekerja keras membuat Aplikasi ini dari awal hingga seperti ini. mohon maaf jika masih ada kekurangan pada aplikasi ini, karena sesungguhnya setiap orang berada dalam tahap terus berproses.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Times New Roman\'; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:14pt;\">DIBUAT DENGAN :</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:14pt;\">1. Python 3.6.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:14pt;\">2. PyQT5.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:14pt;\">3. MongoDB.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Times New Roman\'; font-size:14pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:14pt;\">Programmer : Muhammad Bagas Pradana</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:14pt;\">NIM             : 1313618015</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:14pt;\">Prodi            : Ilmu Komputer </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:14pt;\">Mata Kuliah  : Perancangan dan Pemrograman Web 112</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:14pt;\">github           : </span><a href=\"https://github.com/bagas050201\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">https://github.com/bagas050201</span></a></p></body></html>"))
        self.aboutus_label.setText(_translate("aboutus", "   ABOUT MUHAMMAD BAGAS PRADANA"))
        self.back_button.setText(_translate("aboutus", "MAIN MENU"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    aboutus = QtWidgets.QMainWindow()
    ui = Ui_aboutus()
    ui.setupUi(aboutus)
    aboutus.show()
    sys.exit(app.exec_())
