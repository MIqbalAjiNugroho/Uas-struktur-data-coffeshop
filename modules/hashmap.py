class HashMapMenu:
    """
    Wrapper di atas dict Python untuk menyimpan data menu.
    Konsepnya tetap Hash Map: setiap menu diakses lewat KEY (kode menu),
    """ 
    def __init__(self):
        self.data = {}   # contoh isi: { "K001": {"nama":"Espresso","harga":15000,"stok":50} }
    
    def tambah(self, kode, nama, harga, stok):
        """Tambah menu baru. Jika kode sudah ada, akan menimpa (overwrite)."""
        self.data[kode] = {
            "nama": nama,
            "harga": int(harga),
            "stok": int(stok)
        }

    def cari(self, kode):
        """
        Cari menu berdasarkan kode -- INI YANG MENGGANTIKAN loop di kode lama.
        dict.get() ini O(1), beda jauh dengan 'for r in menu: if r[0]==kode'.
        Return None kalau kode tidak ditemukan.
        """
        return self.data.get(kode)

    def update_stok(self, kode, stok_baru):
        """Update stok menu tertentu. Return True kalau berhasil, False kalau kode tidak ada."""
        if kode in self.data:
            self.data[kode]["stok"] = int(stok_baru)
            return True
        return False

    def hapus(self, kode):
        """Hapus menu berdasarkan kode. Return True kalau berhasil, False kalau tidak ada."""
        if kode in self.data:
            del self.data[kode]
            return True
        return False

    def semua(self):
        """Return semua data menu (untuk ditampilkan atau diolah lebih lanjut)."""
        return self.data