# Super_Cashier
## Python Project - Agni Pulung Tondo Drawino 

Sistem kasir self-service di supermarket dengan menggunakan bahasa Pyhton. 

## 1. Requirements/ Objectives 

Membuat sistem kasir self service dengan menggunakan feature sebagai berikut : 

a. Membuat proses untuk memasukkan ID Transaksi
b. Membuat proses untuk menambahkan barang yang ini dibeli dan detail jumlah dan harganya
c. Membuat proses untuk mengupdate detail barang yang sudah diinputkan sebelumnya jika ada kesalahan input
d. Membuat proses untuk menghapus salah satu pesanan yang telah diinputkan
e. Membuat proses untuk menghapus seluruh transaksi yang telah diinputkan
f. Membuat proses untuk memeriksa apakah seluruh data yang diinput sudah benar dan lengkap
g. Membuat proses untuk menghitung total belanja yang harus dibayarkan dan diskon yang didapatkan (jika dapat).

## 2. Flowchart 

## 3. Penjelasan Code 

### a. init()
merupakan fungsi inisialisasi untuk class Transaction 

### b. add_item 
merupakan fungsi untuk menambahkan detail item, yang terdiri dari : 
item_name = Nama Barang 
item_qyt = jumlah barang
item_price = harga barang

### c.update_item 
merupakan fungsi untuk mengupdate / mengubah detail item yang diinputkan 

### d.show_order
merupakan fungsi untuk menampilkan daftar pesanan yang sudah diinputkan 

### e.delete_item 
merupakan fungsi untuk menghapus salah satu item/ barang yang sudah diinput

### f.reset_transaction 
Merupakan fungsi untuk menghapus semua item/barang yang telah diinputkan.
 
### g.check_order
Merupakan fungsi untuk untuk memeriksa apakah detail item/barang yang diinputkan sudah lengkap dan benar.

### h.total_price
Merupakan fungsi untuk menghitung total harga yang harus dibayar oleh customer. Setelah dilakukan penghitungan total harga awal (sebelum diskon), terlebih dahulu akan ditentukan apakah customer mendapatkan diskon. Jika mendapat diskon berapa diskon yang didapatkan, dan setelah itu dilakukan perhitungan total harga awal dikurangi diskon, Lalu hasil akhirnya didapatkan harga total setelah diskon


