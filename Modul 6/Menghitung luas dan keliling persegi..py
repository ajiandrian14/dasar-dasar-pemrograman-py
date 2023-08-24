class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi
    
    def hitung_luas(self):
        luas = self.sisi ** 2
        return luas
    
    def hitung_keliling(self):
        keliling = 4 * self.sisi
        return keliling

# Membuat objek Persegi
sisi_persegi = float(input("Masukkan panjang sisi persegi: "))
persegi = Persegi(sisi_persegi)

# Menghitung luas dan keliling
luas = persegi.hitung_luas()
keliling = persegi.hitung_keliling()

print("Luas persegi:", luas)
print("Keliling persegi:", keliling)
