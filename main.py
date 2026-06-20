import os
from modules.hashmap import HashMapMenu
from modules.csv_handler import load_menu_csv, save_menu_csv, load_transaksi_csv, save_transaksi_csv
from modules.sorting_searching import bubble_sort_menu, binary_search_menu
from modules.stack import StackTransaksi
from modules.queue import QueuePesanan
from modules.linked_list import LinkedList
from modules.tree import TreeKategori

file_menu = os.path.join(os.path.dirname(__file__), "data", "menu.csv")
file_transaksi = os.path.join(os.path.dirname(__file__), "data", "transaksi.csv")

menu_map = HashMapMenu()
load_menu_csv(file_menu, menu_map)

stack_riwayat = StackTransaksi()
load_transaksi_csv(file_transaksi, stack_riwayat)

queue_pesanan = QueuePesanan()
daftar_pelanggan = LinkedList()

# Bangun struktur kategori (Tree)
kategori = TreeKategori("Menu")
minuman = kategori.root.tambah_anak("Minuman")
makanan = kategori.root.tambah_anak("Makanan")
minuman.tambah_anak("Kopi")
minuman.tambah_anak("Non-Kopi")
makanan.tambah_anak("Roti")
makanan.tambah_anak("Snack")


while True:

    print("\n=== COFFEESHOP ===")
    print("1. Lihat Menu")
    print("2. Tambah Menu")
    print("3. Update Stok")
    print("4. Hapus Menu")
    print("5. Transaksi")
    print("6. Riwayat Transaksi")
    print("7. Lihat Kategori Menu")
    print("8. Tambah Pesanan ke Antrian")
    print("9. Proses Pesanan dari Antrian")
    print("10. Daftar Pelanggan")
    print("11. Keluar")

    p = input("Pilih : ")

    if p == "1":
        print("\n=== MENU ===")
        for kode, info in menu_map.semua().items():
            print(kode, "|", info["nama"], "| Rp", info["harga"], "| Stok", info["stok"])

    elif p == "2":
        kode = input("Kode : ")
        nama = input("Nama : ")
        harga = input("Harga : ")
        stok = input("Stok : ")

        menu_map.tambah(kode, nama, harga, stok)
        save_menu_csv(file_menu, menu_map)

        nama_kategori = input("Masukkan ke kategori (Kopi/Non-Kopi/Roti/Snack) : ")
        if kategori.tambah_menu_ke_kategori(nama_kategori, kode):
            print("Menu ditambah & dikaitkan ke kategori", nama_kategori)
        else:
            print("Menu ditambah, tapi kategori tidak ditemukan")

    elif p == "3":
        kode = input("Kode : ")
        stok_baru = input("Stok baru : ")

        if menu_map.update_stok(kode, stok_baru):
            save_menu_csv(file_menu, menu_map)
            print("Stok diupdate")
        else:
            print("Kode tidak ditemukan")

    elif p == "4":
        kode = input("Kode : ")

        if menu_map.hapus(kode):
            save_menu_csv(file_menu, menu_map)
            print("Menu dihapus")
        else:
            print("Kode tidak ditemukan")

    elif p == "5":
        for kode, info in menu_map.semua().items():
            info["kode"] = kode

        daftar_menu = list(menu_map.semua().values())
        daftar_menu = bubble_sort_menu(daftar_menu, key="kode")

        total = 0
        struk = []

        while True:
            kode = input("Kode menu (0 selesai) : ")

            if kode == "0":
                break

            hasil = binary_search_menu(daftar_menu, kode, key="kode")

            if hasil is None:
                print("Kode menu tidak ditemukan")
                continue

            qty = int(input("Jumlah : "))

            if qty > hasil["stok"]:
                print("Stok tidak cukup, sisa stok:", hasil["stok"])
                continue

            sub = hasil["harga"] * qty
            total += sub

            hasil["stok"] -= qty
            menu_map.update_stok(kode, hasil["stok"])

            struk.append([hasil["nama"], qty, sub])

        if not struk:
            print("Tidak ada transaksi")
        else:
            bayar = int(input("Bayar : "))
            kembali = bayar - total

            print("\n===== STRUK =====")
            for s in struk:
                print(s[0], "x", s[1], "= Rp", s[2])
            print("----------------")
            print("Total     :", total)
            print("Bayar     :", bayar)
            print("Kembalian :", kembali)

            data_transaksi = {
                "items": struk,
                "total": total,
                "bayar": bayar,
                "kembalian": kembali
            }
            stack_riwayat.push(data_transaksi)

            save_menu_csv(file_menu, menu_map)
            save_transaksi_csv(file_transaksi, stack_riwayat)

    elif p == "6":
        print("\n=== RIWAYAT TRANSAKSI (terbaru di atas) ===")

        if stack_riwayat.is_empty():
            print("Belum ada transaksi")
        else:
            for i, trx in enumerate(stack_riwayat.semua(), start=1):
                print(f"\nTransaksi #{i}")
                for item in trx["items"]:
                    print(" -", item[0], "x", item[1], "= Rp", item[2])
                print(" Total    :", trx["total"])
                print(" Bayar    :", trx["bayar"])
                print(" Kembali  :", trx["kembalian"])

    elif p == "7":
        print("\n=== STRUKTUR KATEGORI MENU ===")
        kategori.tampilkan()

    elif p == "8":
        nama_pelanggan = input("Nama pelanggan : ")
        kode_menu = input("Kode menu dipesan : ")
        qty = input("Jumlah : ")

        data_pesanan = {
            "nama_pelanggan": nama_pelanggan,
            "kode_menu": kode_menu,
            "qty": qty
        }
        queue_pesanan.enqueue(data_pesanan)
        print("Pesanan masuk antrian. Posisi antrian sekarang:", queue_pesanan.jumlah())

    elif p == "9":
        if queue_pesanan.is_empty():
            print("Tidak ada pesanan dalam antrian")
        else:
            pesanan = queue_pesanan.dequeue()
            print("Memproses pesanan dari:", pesanan["nama_pelanggan"])
            print(" Menu  :", pesanan["kode_menu"])
            print(" Qty   :", pesanan["qty"])
            print("Sisa antrian:", queue_pesanan.jumlah())

    elif p == "10":
        sub = input("1. Tambah Pelanggan | 2. Lihat Daftar Pelanggan | Pilih : ")

        if sub == "1":
            nama = input("Nama pelanggan : ")
            no_hp = input("No HP : ")
            daftar_pelanggan.append({"nama": nama, "no_hp": no_hp})
            print("Pelanggan ditambahkan")

        elif sub == "2":
            print("\n=== DAFTAR PELANGGAN ===")
            for p_data in daftar_pelanggan.display():
                print("-", p_data["nama"], "|", p_data["no_hp"])

    elif p == "11":
        break

    else:
        print("Pilihan salah")