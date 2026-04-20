from datetime import datetime
import pandas as pd

class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    def tampilkan_info_mahasiswa(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")

class Buku:
    def __init__(self, judul,kategori, isbn):
        self.judul = judul
        self.kategori = kategori
        self.isbn = isbn
    def tampilkan_info_buku(self):
        print(f"Judul: {self.judul}")
        print(f"Kategori: {self.kategori}")
        print(f"ISBN: {self.isbn}")

class History:
    def __init__(self):
        self.data = []

    def tambah_history(self, status, mahasiswa, buku):
        date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.data.append([status, date, mahasiswa.nim, buku.isbn])

    def tampilkan_history(self):
        df = pd.DataFrame(self.data, columns=["Status", "Tanggal", "Mahasiswa", "Buku"])
        print(df)

mhs1 = Mahasiswa("Ana Kika N.", "C5208212")
mhs1.tampilkan_info_mahasiswa()
buku1 = Buku("Pemrograman Sea+", "Sains", "071-005-1098-35-8")
buku1.tampilkan_info_buku()

history = History()
history.tambah_history("Peminjaman", mhs1, buku1)
history.tambah_history("Pengembalian", mhs1, buku1)

history.tampilkan_history()