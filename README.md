# Hospital Management System

Hospital Management System adalah Aplikasi yang meng-integrasikan segala kegiatan yang ada pada rumah sakit kedalam satu Lokasi. Sehingga segala kegiatan yang ada didalam rumah sakit tersebut, dapat dirangkai dan di record kedalam system aplikasi. Hal ini memungkinkan proses kegiatan yang ada pada rumah sakit tersebut menjadi lebih terstruktur, efisien, serta meminimalkan kejadian miss-communication antar proccess yang ada didalam rumah sakit tersebut.

Aplikasi ini memiliki 4 tipe Users yang dapat menggunakannya, yaitu Admin yang bertugas untuk mengontrol jalannya administrasi rumah sakit, Pharmacist yang bertugas untuk menjalankan roda kegiatan obat rumah sakit, Dokter, dan Pengunjung rumah sakit. Aplikasi ini dibuat menggunakan Windows 10 64 Bit.


## Built With

* [Python 3.6+](https://www.python.org/downloads/) - [[How to Install](https://www.youtube.com/watch?v=ndrCfBJkkvE)]
* [MongoDB](https://www.mongodb.com/download-center) - [[How to Install](https://www.youtube.com/watch?v=FwMwO8pXfq0)]
* [MongoDB Compass](https://www.mongodb.com/download-center/compass) - [[How to Use](https://www.youtube.com/watch?v=gJ82Ifm-VbA)]
* [PyQT5](https://pypi.org/project/PyQt5/) - [pymongo](https://api.mongodb.com/python/current/tutorial.html) - the library used in this program


## Features in the App
1. This application can automatically make changes to the selection of application views to anyone who is logged in using their respective accounts.

2. Each type of users account has capabilities and restrictions that can be done while using this application.

3. The user interface of the application is designed to be as minimal as possible (Keep it Simple), but still leaves a modern and fresh impression so users don't get bored easily with the look of this application.

4. This application can perform CRUD (Create database, Read database, Update database, Delete database) work processes on the MongoDB database which is implemented through a view on the PyQT5 GUI. However, some users cannot access almost the entire MongoDB database, only Admin Users can access the entire database. So that data security cannot be leaked to any users who use this application.

5. Each type of user account can perform CRUD activities. except the doctor's account which can only read the database.

6. A series of program flow made to design this application is made as easy as possible, so it is expected to be easily read by all people who want to use this application, but are curious about how the series of programs used to create this application.


## How to Get Started With This Program
1. Unduh/clone repository ini.
2. Lakukan Installasi tools yang telah disediakan seperti, Python, MongoDB, dan MongoDB Compass.
3. Lakukan Installasi Library PyQT5-nya :
> 1. Yang Pertama
>> Tambahkan Environment Python pada Advance System Setting Komputer anda :
>>> * Open My Computer
>>> * Click Properties
>>> * Click Advance System Setting
>>> * Click Environment Variables
>>> * Cari Variables Path lalu Klik Edit
>>> * Click New lalu masukan directory installasi Python pada Komputer anda. contoh : C:\Users\asus\AppData\Local\Programs\Python\Python36
>>> * Click OK
>>> * Or you can see the tutorial How to add python to windows path : [Manual Setting](https://datatofish.com/add-python-to-windows-path/)

>> Notes : Check apakah pip sudah ter-install pada CMD komputer anda. Tutorial singkat : [Link 1](https://phoenixnap.com/kb/install-pip-windows) - [Link 2](https://pypi.org/project/pip/) - [Link 3](https://www.tecmint.com/install-pip-in-linux/)

> 2. Yang Kedua, Buka Command Prompt lalu Run Administration pada komputer Windows anda, lalu ketik :

```
pip install PyQt5
```

jika ingin lebih lengkap bisa menambahkan
```
pip install pyqt5-tools
```

> Jika sudah selesai mendownload, kita bisa mengecek berhasil atau tidaknya file tersebut berhasil didownload melalui :
```
pip list
```

> Library tersebut bisa dilihat melalui Komputer anda. Lokasinya ada di :
```
 C:\Users\asus\AppData\Local\Programs\Python\Python36\Lib\site-packages
```

4. Setelah berhasil mengunduh program pada repositori ini, maka langkah selanjutnya adalah menjalankan script program Python-nya, jalankan program ```MainWindow.py``` lalu tunggu sebentar sampai GUInya muncul.

5. Jika anda belum memiliki akun untuk memasuki halaman utama pada aplikasi ini, Maka anda diharuskan membuat akun tersebut dengan cara mengklik ```Sign up Button```yang telah ada pada halaman login page.

6. Masukan data diri anda pada kolom yang telah disediakan. 

7. Pada kolom " TYPE " anda diharuskan meimilih, mau masuk menggunakan akun jenis apa. berikut Penjelasannya  :

> 1. Admin

>> * Dapat mengontrol seluruh data pada aplikasi Hospital Management System.
>> * Aksesbilitas pada database seluruh akun.
>> * Membuat rangkaian CRUD pada Management Dokter.
>> * Membuat rangkaian CRUD pada Management pengadaan barang.
>> * Membuat rangkaian CRUD pada Management Janji Bertemu.

> 2. Pharmacist

>> * Aksesbilitas pada database Barang berupa pengadaan Obat.
>> * Membuat rangkaian CRUD pada Kebutuhan Pharmacist.

> 3. Dokter

>> * Aksesbilitas pada database Janji Bertemu Pasien.
>> * Aksesbilitas pada database Barang berupa pengadaan Obat.

> 4. Pengunjung

>> * Membuat rangkaian CRUD pada Form Pasien.
>> * Aksesbilitas pada database Janji Bertemu Dokter.

8. Setelah mendaftarkan akun users, kemudian users akan diarahkan ketampilan halaman utama dari aplikasi yang sedang anda gunakan ini, berdasarkan pilihan type users yang anda pilih.

9. Pada halaman utama ini, Users dapat melakukan kegiatan yang berhubungan dengan segala sesuatu yang dapat dilakukan menggunakan akun tersebut.

10. Untuk segala bentuk pengiriman data database baik Create, Read, Update, dan Delete. Di handle oleh MongoDB Compass. Sehingga, Jika ingin melihat segala macam data yang telah di masukan atau di input kedalam aplikasi, dapat dilihan melalui aplikasi MongoDB Compass.

10. Jika ingin keluar dari aplikasi, tinggal meng-klik tombol "Back" yang telah disediakan.

## A Complete Video Tutorial of This Application
Example to run this applications in Python PyQT5, based on M. Bagas Pradana video: https://www.youtube.com/watch?v=gAoFsqvq_2A&t=397s

## License

This project is licensed under the GNU General Public License v3.0 License - see the [LICENSE](https://github.com/bagas050201/Hospital-Management-System/blob/master/LICENSE) file for details

## Authors

* **Muhammad Bagas Pradana** - *Ilmu Komputer Universitas Negeri Jakarta* - [bagas050201](https://github.com/bagas050201)
