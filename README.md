# Pertemuan 12 File IO

- Nama: Gugun Ramdani  
- NIM: 2225250061
- Kelas: 3A
- Mata Kuliah: Algoritma dan Pemrograman  

## 1. Tujuan
Mempelajari cara membaca, menulis, memvalidasi, mengolah, dan menyimpan data menggunakan file dengan Python.

## 2. Struktur Folder
```text
Pertemuan_12_file_io_2225250061
├── data/
│   ├── catatan.txt
│   ├── nilai.txt
│   └── hasil_rekap.txt
├── latihan/
│   ├── 01_tulis_file.py
│   ├── 02_baca_file.py
│   ├── 03_append_file.py
│   ├── 04_proses_baris.py
│   ├── 05_file_not_found.py
│   └── 06_value_error.py
└── tugas/
│   └── rekap_nilai_file.py
└──kuis formatif_pertemuan 12.docx
├── .gitignore
└── README.md
```
## 3. Format File Input
File `data/nilai.txt` menggunakan format:
```text
NIM,nilai
A001,85
A002,78
A003,92
A004,74
```
## 4. Cara Menjalankan Program
Jalankan program melalui terminal VS Code dari folder utama proyek.
```bash
python latihan/01_tulis_file.py
python latihan/02_baca_file.py
python latihan/03_append_file.py
python latihan/04_proses_baris.py
python latihan/05_file_not_found.py
python latihan/06_value_error.py
python tugas/rekap_nilai_file.py
```
## 5. Error yang Ditangani
- **FileNotFoundError:** Terjadi ketika file yang akan dibuka tidak ditemukan.
- **ValueError:** Terjadi ketika data tidak dapat dikonversi menjadi angka atau format pemisahan data tidak sesuai.

## 6. Hasil Rekap Nilai
Berdasarkan data yang valid, diperoleh:
- Jumlah data valid: 4
- Rata-rata: 82.25
- Minimum: 74.00
- Maksimum: 92.00
- Jumlah lulus: 4

## 7. Test Case
| Kondisi | Hasil |
|---|---|
| Semua data valid | Data berhasil diproses |
| File tidak ditemukan | Pesan error ditampilkan |
| Nilai berupa teks | Baris invalid dilewati |
| Baris kosong | Baris dilewati |
| Nilai sama dengan 60 | Dihitung lulus |

## 8. Refleksi
Melalui praktikum Pertemuan 12, saya memahami bahwa file I/O digunakan untuk menyimpan dan membaca data agar tetap tersedia meskipun program telah selesai dijalankan.
Saya juga mempelajari perbedaan mode file, yaitu `r` untuk membaca, `w` untuk menulis dari awal, dan `a` untuk menambahkan data. Selain itu, saya memahami penggunaan `with` agar file tertutup secara otomatis setelah digunakan.
Kesulitan yang saya temukan adalah ketika program membaca data yang tidak sesuai format, seperti nilai yang berisi teks. Hal tersebut dapat ditangani menggunakan `try-except` dengan exception yang spesifik, seperti `ValueError` dan `FileNotFoundError`.
Dengan praktikum ini, saya menjadi lebih memahami cara mengelola data menggunakan file serta pentingnya validasi dan penanganan error dalam pemrograman Python.
