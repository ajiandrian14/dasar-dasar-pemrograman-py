def konversi_nilai_ke_huruf(nilai_angka):
    if 85 < nilai_angka <= 100:
        return "A"
    elif 70 < nilai_angka <= 85:
        return "B"
    elif 55 < nilai_angka <= 70:
        return "C"
    elif 45 < nilai_angka <= 55:
        return "D"
    elif 0 <= nilai_angka <= 45:
        return "E"
    else:
        return "Nilai tidak valid"

print("Program Konversi Nilai Angka ke Huruf")
nilai_angka = float(input("Masukkan nilai angka: "))
hasil_konversi = konversi_nilai_ke_huruf(nilai_angka)
print("Nilai Huruf:", hasil_konversi)
