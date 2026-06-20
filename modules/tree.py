class NodeKategori:
    """
    Satu node dalam Tree, merepresentasikan satu kategori.
    Setiap node punya nama, daftar children (sub-kategori), dan daftar menu yang ada di kategori ini.
    """
    def __init__(self, nama):
        self.nama = nama
        self.children = []      # list berisi NodeKategori lain (sub-kategori)
        self.daftar_menu = []   # list kode menu yang termasuk kategori ini

    def tambah_anak(self, nama_anak):
        """Buat node kategori baru sebagai anak dari node ini, lalu return node barunya."""
        anak_baru = NodeKategori(nama_anak)
        self.children.append(anak_baru)
        return anak_baru


class TreeKategori:
    """
    Mengelola seluruh struktur Tree kategori menu, dimulai dari root.
    """
    def __init__(self, nama_root="Menu"):
        self.root = NodeKategori(nama_root)

    def cari_kategori(self, nama_kategori, node=None):
        """
        Cari node kategori berdasarkan nama, di seluruh Tree (termasuk children-nya).
        """
        if node is None:
            node = self.root

        if node.nama == nama_kategori:
            return node

        for anak in node.children:
            hasil = self.cari_kategori(nama_kategori, anak)
            if hasil is not None:
                return hasil

        return None

    def tampilkan(self, node=None, level=0):
        """
        Tampilkan seluruh struktur Tree secara berjenjang (pakai indentasi).
        """
        if node is None:
            node = self.root

        print("  " * level + node.nama)

        for anak in node.children:
            self.tampilkan(anak, level + 1)

    def tambah_menu_ke_kategori(self, nama_kategori, kode_menu):
        """
        Tambahkan kode menu ke kategori tertentu.
        Return True kalau kategori ditemukan & berhasil, False kalau kategori tidak ada.
        """
        kategori = self.cari_kategori(nama_kategori)
        if kategori is None:
            return False
        kategori.daftar_menu.append(kode_menu)
        return True