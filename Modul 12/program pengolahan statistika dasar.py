import math

def hitung_rata_rata(data):
    jumlah = sum(data)
    rata_rata = jumlah / len(data)
    return rata_rata

def hitung_standar_deviasi(data):
    rata_rata = hitung_rata_rata(data)
    jumlah = sum([(nilai - rata_rata) ** 2 for nilai in data])
    standar_deviasi = math.sqrt(jumlah / (len(data) - 1))
    return standar_deviasi

def hitung_minimum(data):
    minimum = min(data)
    return minimum

def hitung_maksimum(data):
    maksimum = max(data)
    return maksimum

print("Program Pengolahan Statistika Dasar")
print("------------------------------------")

data = []
jumlah_data = int(input("Masukkan jumlah data: "))
for i in range(1, jumlah_data + 1):
    nilai = float(input("Masukkan nilai ke-" + str(i) + ": "))
    data.append(nilai)

print("1. Mencari nilai rata-rata")
print("2. Mencari nilai standar deviasi data")
print("3. Mencari nilai minimum")
print("4. Mencari nilai maksimum")

Pilihan = input("Pilih menu (1/2/3/4): ")

if Pilihan == "1":
    rata_rata = hitung_rata_rata(data)
    print("Rata-rata:", rata_rata)
elif Pilihan == "2":
    standar_deviasi = hitung_standar_deviasi(data)
    print("Standar Deviasi:", standar_deviasi)
elif Pilihan == "3":
    minimum = hitung_minimum(data)
    print("Nilai Minimum:", minimum)
elif Pilihan == "4":
    maksimum = hitung_maksimum(data)
    print("Nilai Maksimum:", maksimum)
else:
    print("Pilihan tidak valid")
