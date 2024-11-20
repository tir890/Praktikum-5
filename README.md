# Praktikum 5 | Dictionary: Program Sederhana Daftar Nilai Mahasiswa

Nama : Tiara Hayatul Khoir

Kelas : TI.24.A.5

Nim : 312410474

Mata Kuliah : Bahasa pemrograman

## Deklarasi Variabel
`data_mahasiswa` adalah dictionary kosong yang akan digunakan untuk menyimpan data mahasiswa. Kunci dictionary adalah NIM, sedangkan nilainya adalah dictionary yang memuat nama, nilai tugas, nilai UTS, nilai UAS, dan nilai akhir.

## Fungsi-fungsi Utama
a. `hitung_akhir` (tugas, uts, uas)

Fungsi ini menghitung nilai akhir berdasarkan bobot:

•	Tugas: 30%

•	UTS: 35%

•	UAS: 35%

•	Nilai akhir dikembalikan dalam bentuk float.

b. `tampilkan()`

Fungsi ini menampilkan data mahasiswa dalam format tabel.

•	Jika data tersedia, fungsi mencetak setiap data mahasiswa berdasarkan NIM.

•	Jika tidak ada data, pesan "TIDAK ADA DATA" akan ditampilkan.

c. `tambah_ubah(nim=None)`

Fungsi ini digunakan untuk menambahkan atau mengubah data mahasiswa.

•	Jika nim tidak diberikan (untuk penambahan data baru), pengguna akan diminta memasukkan NIM.

•	Nama, nilai tugas, nilai UTS, dan nilai UAS diinputkan oleh pengguna.

•	Nilai akhir dihitung dengan memanggil `hitung_akhir()`.

•	Data disimpan ke dalam dictionary `data_mahasiswa` dengan NIM sebagai kunci.

d. `hapus()`

Fungsi ini menghapus data mahasiswa berdasarkan NIM.

•	Jika NIM ditemukan, data dihapus dari `data_mahasiswa`.

•	Jika NIM tidak ditemukan, pesan kesalahan ditampilkan.

e. `cari()`

Fungsi ini mencari data mahasiswa berdasarkan NIM.

•	Jika ditemukan, data mahasiswa dicetak.

•	Jika tidak ditemukan, pesan kesalahan ditampilkan.

## Menu dan Pengendalian Program

a. Menu

`menu` adalah dictionary yang memetakan pilihan menu ke fungsi yang sesuai:

•	`"l"` untuk menampilkan data `(panggil tampilkan())`.

•	`"t"` untuk menambah data `(panggil tambah_ubah())`.

•	`"u"` untuk mengubah data `(panggil tambah_ubah() dengan NIM tertentu)`.

•	`"h"` untuk menghapus data `(panggil hapus())`.

•	`"c"` untuk mencari data `(panggil cari())`.

b. Pengulangan Utama

Program menggunakan perulangan while untuk menampilkan menu dan meminta input pengguna. Input pengguna:

•	Huruf kecil dari menu pilihan.

•	Jika pengguna memilih "k", program berhenti dan mencetak pesan terima kasih.

•	Jika pilihan tidak valid, pesan kesalahan ditampilkan.

## Cara Kerja Program

Program menampilkan menu kepada pengguna.

Pengguna memilih opsi:

•	Lihat (L): Menampilkan semua data mahasiswa dalam bentuk tabel.

•	Tambah (T): Meminta pengguna untuk memasukkan data baru.

•	Ubah (U): Meminta NIM mahasiswa yang akan diubah, kemudian memungkinkan pengguna memasukkan data baru untuk NIM tersebut.

•	Hapus (H): Meminta pengguna memasukkan NIM yang ingin dihapus dari data.

•	Cari (C): Meminta pengguna memasukkan NIM untuk mencari data mahasiswa.

•	Keluar (K): Menghentikan program.

Program terus berjalan hingga pengguna memilih menu keluar.
