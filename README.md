# ☕ Sistem Manajemen Kasir Coffeeshop

Aplikasi CLI (Command-Line Interface) untuk manajemen kasir coffeeshop, dibangun menggunakan Python dengan implementasi struktur data manual dan database flat-file (.csv). Dibuat sebagai proyek Ujian Akhir Semester (UAS) mata kuliah Struktur Data.

## 📋 Deskripsi Proyek

Aplikasi ini mensimulasikan sistem kasir coffeeshop yang mampu melakukan operasi **CRUD** (Create, Read, Update, Delete) terhadap data menu dan transaksi. Seluruh data disimpan secara persisten dalam file `.csv`, dengan field kompleks (seperti daftar item dalam satu transaksi) diserialisasi menggunakan format JSON agar tetap bisa disimpan dalam satu kolom CSV.

## 🛠️ Persyaratan Teknis

| Aspek | Implementasi |
|---|---|
| Bahasa Pemrograman | Python |
| Struktur Data | Hash Map, Stack, Queue, Tree, Linked List |
| Algoritma Sorting | Bubble Sort |
| Algoritma Searching | Binary Search |
| Database | File `.csv` (`menu.csv` & `transaksi.csv`) dengan field JSON-serialized |
| Antarmuka | Command-Line Interface (CLI) |

## 🧩 Struktur Data yang Digunakan

| Struktur Data | Implementasi | Fungsi |
|---|---|---|
| **Hash Map** (`HashMapMenu`) | `modules/hashmap.py` | Menyimpan & mencari data menu berdasarkan kode menu (key → value), menggantikan pencarian linear |
| **Stack** (`StackTransaksi`) | `modules/stack.py` | Menyimpan riwayat transaksi (LIFO) — transaksi terbaru ditampilkan paling atas |
| **Queue** (`QueuePesanan`) | `modules/queue.py` | Mengelola antrian pesanan pelanggan (FIFO) — pesanan yang masuk duluan diproses duluan |
| **Tree** (`TreeKategori`) | `modules/tree.py` | Mengorganisasi kategori menu secara hierarkis (Menu → Minuman/Makanan → sub-kategori), dijelajahi dan ditampilkan secara rekursif |
| **Linked List** | `modules/linked_list.py` | Menyimpan data pelanggan secara dinamis, dengan operasi tambah, cari, dan hapus |

## 🔍 Algoritma

- **Bubble Sort** (`modules/sorting_searching.py`) — mengurutkan daftar menu berdasarkan kode sebelum dilakukan pencarian, dengan kompleksitas pembanding elemen bersebelahan secara berulang.
- **Binary Search** (`modules/sorting_searching.py`) — mencari menu berdasarkan kode pada data yang sudah terurut, dipakai pada fitur Transaksi untuk pencarian yang efisien dibanding pencarian linear.

## 📂 Struktur Folder

uas-struktur-data-coffeeshop/

├── README.md

├── main.py                       # Entry point aplikasi & seluruh alur CLI

├── data/

│   ├── menu.csv                   # Database menu (persisten)

│   └── transaksi.csv              # Database riwayat transaksi (persisten, JSON-serialized)

├── modules/

│   ├── init.py

│   ├── hashmap.py                 # Implementasi Hash Map untuk data menu

│   ├── stack.py                   # Implementasi Stack untuk riwayat transaksi

│   ├── queue.py                   # Implementasi Queue untuk antrian pesanan

│   ├── tree.py                    # Implementasi Tree untuk kategori menu

│   ├── linked_list.py             # Implementasi Linked List untuk data pelanggan

│   ├── sorting_searching.py       # Bubble Sort & Binary Search

│   └── csv_handler.py             # Baca/tulis CSV untuk menu & transaksi

├── flowchart-menu-utama.png       # Flowchart alur menu utama aplikasi

├── flowchart-transaksi.png        # Flowchart detail alur fitur transaksi

└── .gitignore

## 🚀 Cara Menjalankan

1. **Clone repository ini**
```bash
   git clone https://github.com/MIqbalAjiNugroho/Uas-struktur-data-coffeshop.git
   cd Uas-struktur-data-coffeshop
```

2. **Pastikan Python sudah terinstall** (Python 3.8 ke atas direkomendasikan)
```bash
   python --version
```

3. **Jalankan aplikasi**
```bash
   python main.py
```

## ✨ Fitur Aplikasi

| No | Fitur | Struktur Data Terkait |
|---|---|---|
| 1 | Lihat Menu | Hash Map |
| 2 | Tambah Menu | Hash Map, Tree |
| 3 | Update Stok | Hash Map |
| 4 | Hapus Menu | Hash Map |
| 5 | Transaksi | Hash Map, Bubble Sort, Binary Search, Stack |
| 6 | Riwayat Transaksi | Stack |
| 7 | Lihat Kategori Menu | Tree (traversal rekursif) |
| 8 | Tambah Pesanan ke Antrian | Queue |
| 9 | Proses Pesanan dari Antrian | Queue |
| 10 | Daftar Pelanggan | Linked List |
| 11 | Keluar | — |

## 💾 Database CSV

Aplikasi menggunakan dua file CSV sebagai basis data:

- **`menu.csv`** — menyimpan data menu (kode, nama, harga, stok), dibaca saat program dijalankan dan ditulis ulang setiap ada perubahan (tambah/update/hapus).
- **`transaksi.csv`** — menyimpan riwayat transaksi. Field `items` (daftar barang yang dibeli dalam satu transaksi) diserialisasi ke format JSON menggunakan `json.dumps()` sebelum ditulis ke CSV, dan dibaca kembali dengan `json.loads()` saat program dimuat ulang — sehingga riwayat transaksi tetap tersimpan meskipun program ditutup dan dijalankan kembali.

## 📊 Flowchart

Dua flowchart disediakan untuk menggambarkan alur aplikasi:
- [`flowchart-menu-utama.png`](./flowchart-menu-utama.png) — alur menu utama dari program dimulai hingga setiap fitur.
- [`flowchart-transaksi.png`](./flowchart-transaksi.png) — detail alur fitur Transaksi, mencakup proses Bubble Sort, Binary Search, dan penyimpanan ke Stack.

## 👤 Author

- Nama: M Iqbal Aji Nugroho (25416255201200)
- Mata Kuliah: Struktur Data
- Proyek: UAS — Aplikasi Manajemen dengan Database Flat File (.csv)

## 📄 Lisensi

Proyek ini dibuat untuk keperluan akademik (Ujian Akhir Semester).