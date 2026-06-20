def bubble_sort_menu(daftar_menu, key="kode"):
    """
    Mengurutkan daftar menu menggunakan Bubble Sort.
    """
    n = len(daftar_menu)
    for i in range(n - 1):  # jumlah putaran
        for j in range(n - 1 - i):  # bandingkan elemen bersebelahan
            if daftar_menu[j][key] > daftar_menu[j + 1][key]:
                # tukar posisi
                daftar_menu[j], daftar_menu[j + 1] = (
                    daftar_menu[j + 1],
                    daftar_menu[j]
                )
    return daftar_menu


def binary_search_menu(daftar_menu, kode_dicari, key="kode"):
    """
    Mencari menu berdasarkan kode menggunakan Binary Search.
    SYARAT: daftar_menu HARUS sudah terurut berdasarkan 'key' sebelum dipanggil
    (gunakan bubble_sort_menu() dulu).
    """
    low = 0
    high = len(daftar_menu) - 1
    while low <= high:
        mid = (low + high) // 2
        if daftar_menu[mid][key] == kode_dicari:
            return daftar_menu[mid]  # data ditemukan
        elif daftar_menu[mid][key] < kode_dicari:
            low = mid + 1  # cari di kanan
        else:
            high = mid - 1  # cari di kiri
    return None  # tidak ditemukan