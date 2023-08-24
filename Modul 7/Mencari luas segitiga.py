class Segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    
    def hitung_luas(self):
        luas = 0.5 * self.alas * self.tinggi
        return luas

# Membuat objek Segitiga
alas_segitiga = float(input("Masukkan panjang alas segitiga: "))
tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))
segitiga = Segitiga(alas_segitiga, tinggi_segitiga)

# Menghitung dan menampilkan luas segitiga
luas = segitiga.hitung_luas()
print("Luas segitiga:", luas)