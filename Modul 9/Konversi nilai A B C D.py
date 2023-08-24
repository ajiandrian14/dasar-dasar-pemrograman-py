nilai_angka = float(input("Masukkan nilai angka: "))  # Langkah 1

if nilai_angka > 85.0 and nilai_angka <= 100.0:  # Langkah 2
    nilai_huruf = "A"
elif nilai_angka > 70.0 and nilai_angka <= 85.0:  # Langkah 3
    nilai_huruf = "B"
elif nilai_angka > 55.0 and nilai_angka <= 70.0:  # Langkah 4
    nilai_huruf = "C"
elif nilai_angka > 45.0 and nilai_angka <= 55.0:  # Langkah 5
    nilai_huruf = "D"
elif nilai_angka > 0 and nilai_angka <= 45.0:  # Langkah 6
    nilai_huruf = "E"

print(f"Nilai angka: {nilai_angka}")
print(f"Nilai huruf: {nilai_huruf}")  # Langkah 7
