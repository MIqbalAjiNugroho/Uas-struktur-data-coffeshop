import csv
import os
import json


def load_menu_csv(filepath, menu_map):
    """Baca file CSV menu, masukkan semua datanya ke dalam objek HashMapMenu."""
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        return  # file belum ada isinya, lewati

    with open(filepath, "r", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)

        if not rows:
            return

        for row in rows[1:]:  # lewati header
            if len(row) >= 4:
                kode, nama, harga, stok = row[0], row[1], row[2], row[3]
                menu_map.tambah(kode, nama, harga, stok)


def save_menu_csv(filepath, menu_map):
    """Tulis ulang semua data dari HashMapMenu ke file CSV."""
    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["kode", "nama", "harga", "stok"])

        for kode, info in menu_map.semua().items():
            writer.writerow([kode, info["nama"], info["harga"], info["stok"]])


def save_transaksi_csv(filepath, stack_riwayat):
    """
    Tulis ulang SEMUA riwayat transaksi dari Stack ke file CSV.
    Field 'items' yang berupa list di-serialize ke JSON dulu sebelum ditulis.
    """
    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["items", "total", "bayar", "kembalian"])

        for trx in reversed(stack_riwayat.semua()):
            items_json = json.dumps(trx["items"])
            writer.writerow([items_json, trx["total"], trx["bayar"], trx["kembalian"]])


def load_transaksi_csv(filepath, stack_riwayat):
    """
    Baca file CSV riwayat transaksi, masukkan ke Stack.
    Field 'items' yang berupa teks JSON di-deserialize balik ke list Python.
    """
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        return

    with open(filepath, "r", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)

        if not rows:
            return

        for row in rows[1:]:  # lewati header
            if len(row) >= 4:
                items = json.loads(row[0])
                total = int(row[1])
                bayar = int(row[2])
                kembalian = int(row[3])

                stack_riwayat.push({
                    "items": items,
                    "total": total,
                    "bayar": bayar,
                    "kembalian": kembalian
                })