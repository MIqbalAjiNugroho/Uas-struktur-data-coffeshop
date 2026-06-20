class StackTransaksi:
    """
    Menyimpan riwayat transaksi dengan prinsip LIFO (Last In, First Out).
    Transaksi paling baru selalu ada di posisi paling atas.
    """
    def __init__(self):
        self.items = []   # gunakan list Python sebagai "tempat" tumpukan

    def push(self, data_transaksi):
        """Tambahkan transaksi baru ke ATAS tumpukan."""
        self.items.append(data_transaksi)

    def pop(self):
        """
        Ambil & hapus transaksi paling atas (paling baru).
        Return None kalau tumpukan kosong.
        """
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        """
        Lihat transaksi paling atas TANPA menghapusnya.
        Return None kalau tumpukan kosong.
        """
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        """Cek apakah tumpukan kosong."""
        return len(self.items) == 0

    def semua(self):
        """
        Return semua riwayat transaksi, dari yang TERBARU ke TERLAMA
        (urutan terbalik dari urutan push, karena yang terakhir push ada di atas).
        """
        return list(reversed(self.items))

    def jumlah(self):
        """Return jumlah total transaksi dalam riwayat."""
        return len(self.items)