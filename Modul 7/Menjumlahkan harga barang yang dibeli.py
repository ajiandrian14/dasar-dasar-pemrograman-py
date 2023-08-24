class Pembelian:
    def __init__(self):
        self.daftar_barang = {}
    
    def tambah_barang(self, nama, harga, jumlah):
        self.daftar_barang[nama] = {"harga": harga, "jumlah": jumlah}
    
    def hitung_total(self):
        total = 0
        for barang in self.daftar_barang.values():
            total += barang["harga"] * barang["jumlah"]
        return total

# Membuat objek Pembelian
pembelian = Pembelian()

# Menambahkan barang-barang ke dalam daftar pembelian
while True:
    nama_barang = input("Masukkan nama barang (kosongkan jika selesai): ")
    if not nama_barang:
        break
    harga_barang = float(input("Masukkan harga barang: "))
    jumlah_barang = int(input("Masukkan jumlah barang: "))
    
    pembelian.tambah_barang(nama_barang, harga_barang, jumlah_barang)

# Menghitung dan menampilkan total harga pembelian
total_harga = pembelian.hitung_total()
print("Total harga pembelian:", total_harga)