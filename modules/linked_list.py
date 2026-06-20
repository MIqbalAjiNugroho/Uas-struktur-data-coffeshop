class Node:
    """
    Satu 'kotak' dalam Linked List.
    Setiap Node menyimpan data, dan menyimpan alamat (referensi) ke Node berikutnya.
    """
    def __init__(self, data):
        self.data = data       # data yang disimpan (misal: dictionary transaksi)
        self.next = None       # awalnya belum nyambung ke kotak manapun


class LinkedList:
    """
    Rangkaian Node yang saling terhubung.
    Kita simpan referensi ke Node pertama (head) saja --
    dari head, kita bisa "berjalan" ke node-node berikutnya.
    """
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        """Tambah data baru di AKHIR linked list."""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

        self.size += 1

    def display(self):
        """Tampilkan semua data dari awal sampai akhir."""
        hasil = []
        current = self.head
        while current is not None:
            hasil.append(current.data)
            current = current.next
        return hasil

    def delete(self, key, key_field):
        """
        Hapus node berdasarkan field tertentu.
        """
        if self.head is None:
            return False

        # Jika node pertama yang dicari
        if self.head.data[key_field] == key:
            self.head = self.head.next
            self.size -= 1
            return True

        previous = self.head
        current = self.head.next

        while current is not None:
            if current.data[key_field] == key:
                previous.next = current.next
                self.size -= 1
                return True
            previous = current
            current = current.next

        return False

    def find(self, key, key_field):
        """
        Cari satu data berdasarkan field tertentu.
        Return data jika ditemukan, None jika tidak ada.
        """
        current = self.head
        while current is not None:
            if current.data[key_field] == key:
                return current.data
            current = current.next
        return None