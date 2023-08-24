def hitung_luas_keliling_bujur_sangkar(sisi):
    luas = sisi * sisi
    keliling = 4 * sisi
    return luas, keliling

def hitung_luas_keliling_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

def hitung_luas_keliling_segitiga(alas, tinggi, sisi1, sisi2, sisi3):
    luas = 0.5 * alas * tinggi
    keliling = sisi1 + sisi2 + sisi3
    return luas, keliling

def hitung_luas_keliling_lingkaran(jari_jari):
    luas = 3.14 * jari_jari * jari_jari
    keliling = 2 * 3.14 * jari_jari
    return luas, keliling

print("Program Menghitung Luas dan Keliling Bidang Datar")
print("---------------------------------------------")

print("1. Bujur Sangkar")
print("2. Persegi Panjang")
print("3. Segitiga")
print("4. Lingkaran")

Pilihan = input("Pilih menu (1/2/3/4): ")

if Pilihan == "1":
    sisi = float(input("Masukkan panjang sisi: "))
    luas, keliling = hitung_luas_keliling_bujur_sangkar(sisi)
    print("Luas:", luas)
    print("Keliling:", keliling)
elif Pilihan == "2":
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    luas, keliling = hitung_luas_keliling_persegi_panjang(panjang, lebar)
    print("Luas:", luas)
    print("Keliling:", keliling)
elif Pilihan == "3":
    alas = float(input("Masukkan alas: "))
    tinggi = float(input("Masukkan tinggi: "))
    sisi1 = float(input("Masukkan panjang sisi 1: "))
    sisi2 = float(input("Masukkan panjang sisi 2: "))
    sisi3 = float(input("Masukkan panjang sisi 3: "))
    luas, keliling = hitung_luas_keliling_segitiga(alas, tinggi, sisi1, sisi2, sisi3)
    print("Luas:", luas)
    print("Keliling:", keliling)
elif Pilihan == "4":
    jari_jari = float(input("Masukkan jari-jari: "))
    luas, keliling = hitung_luas_keliling_lingkaran(jari_jari)
    print("Luas:", luas)
    print("Keliling:", keliling)
else:
    print("Pilihan tidak valid")
