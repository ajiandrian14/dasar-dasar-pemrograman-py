print('Menghitung Rata-rata Tinggi Badan Mahasiswa')
print('------------------------------------------')

# Data tinggi badan mahasiswa
tinggi_badan = [185, 175, 171, 157, 169]

# Menghitung total tinggi badan
total_tinggi = sum(tinggi_badan)

# Menghitung rata-rata tinggi badan
rata2_tinggi = total_tinggi / len(tinggi_badan)

print('Data tinggi badan mahasiswa:')
for i, tinggi in enumerate(tinggi_badan, start=1):
    print(f"Mahasiswa absen {i}, tinggi {tinggi} cm")

print('\nRata-rata tinggi badan mahasiswa: %.2f cm' % rata2_tinggi)
