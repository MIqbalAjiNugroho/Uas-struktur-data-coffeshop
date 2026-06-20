class QueuePesanan:
    """
    Menyimpan antrian pesanan dengan prinsip FIFO (First In, First Out).
    Pesanan yang masuk duluan, diproses duluan.
    """
    def __init__(self):
        self.items = []

    def enqueue(self, data_pesanan):
        """Tambahkan pesanan baru ke BELAKANG antrian."""
        self.items.append(data_pesanan)

    def dequeue(self):
        """
        Ambil & hapus pesanan dari paling DEPAN antrian.
        Return None kalau antrian kosong.
        """
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        """
        Lihat pesanan paling depan TANPA menghapusnya.
        Return None kalau antrian kosong.
        """
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        """Cek apakah antrian kosong."""
        return len(self.items) == 0

    def semua(self):
        """Return semua pesanan dalam antrian, urutan dari depan ke belakang."""
        return self.items

    def jumlah(self):
        """Return jumlah pesanan dalam antrian."""
        return len(self.items)