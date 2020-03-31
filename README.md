# Hospital Management System

Hospital Management System adalah Aplikasi yang meng-integrasikan segala kegiatan yang ada pada rumah sakit kedalam satu Lokasi. Sehingga segala kegiatan yang ada didalam rumah sakit tersebut, dapat dirangkai dan di record kedalam system aplikasi. Hal ini memungkinkan proses kegiatan yang ada pada rumah sakit tersebut menjadi lebih terstruktur, efisien, serta meminimalkan kejadian miss-communication antar proccess yang ada didalam rumah sakit tersebut.

Aplikasi ini memiliki 4 tipe Users yang dapat menggunakannya, yaitu Admin, Pharmacist, Dokter, dan Pengunjung rumah sakit.

Setiap users pada aplikasi ini memiliki kemampuannya masing-masing.Kemampuan masing-masing dari users memiliki batasan pada aksesbilitas pada masing-masing komponen-komponen penting. 

## Admin

* Dapat mengontrol seluruh data pada aplikasi Hospital Management System.
* Aksesbilitas pada database seluruh akun.
* Membuat rangkaian CRUD pada Management Dokter.
* Membuat rangkaian CRUD pada Management pengadaan barang.
* Membuat rangkaian CRUD pada Management Janji Bertemu.

## Pharmacist

* Aksesbilitas pada database Barang berupa pengadaan Obat.
* Membuat rangkaian CRUD pada Kebutuhan Pharmacist.

## Dokter

* Aksesbilitas pada database Janji Bertemu Pasien.
* Aksesbilitas pada database Barang berupa pengadaan Obat.

## Pengunjung

* Membuat rangkaian CRUD pada Form Pasien.
* Aksesbilitas pada database Janji Bertemu Dokter.

### Business Proccess

Firstly

```
Users akan dihadapkan pada tab aplikasi yang meminta users untuk melakukan login atau Sign up kedalam aplikasi Hospital Management System.
```

Secondly

```
Jika users belum memiliki akun, maka users diwajibkan untuk mengisi form Sign up yang telah disediakan aplikasi. Pembagian tipe Users ada pada bagian Sign up.
```

Lastly

```
Setelah membuat akun, Users akan ditampilkan viewing tab pada masing-masing tipe users, pada tab ini users dapat melakukan kegiatan yang berhubungan dengan segala sesuatu yang dapat dilakukan menggunakan akun tersebut.
```


## Authors

* **Muhammad Bagas Pradana** - *Ilmu Komputer Universitas Negeri Jakarta* - [bagas050201](https://github.com/bagas050201)
