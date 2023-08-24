print('Menghitung Rata-rata Tinggi Badan Mahasiswa')
print('------------------------------------------')

# Minta pengguna memasukkan jumlah mahasiswa
jumlah_mahasiswa = int(input('Masukkan jumlah mahasiswa: '))

# Inisialisasi list untuk menyimpan tinggi badan
tinggi_badan = []

# Minta pengguna memasukkan tinggi badan setiap mahasiswa
for i in range(jumlah_mahasiswa):
    tinggi = int(input(f"Masukkan tinggi mahasiswa absen {i+1} (cm): "))
    tinggi_badan.append(tinggi)

# Menghitung total tinggi badan
total_tinggi = sum(tinggi_badan)

# Menghitung rata-rata tinggi badan
rata2_tinggi = total_tinggi / jumlah_mahasiswa

print('\nData tinggi badan mahasiswa:')
for i, tinggi in enumerate(tinggi_badan, start=1):
    print(f"Mahasiswa absen {i}, tinggi {tinggi} cm")

print('\nRata-rata tinggi badan mahasiswa: %.2f cm' % rata2_tinggi)
