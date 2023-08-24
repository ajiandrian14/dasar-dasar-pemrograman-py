x = float(input("Masukkan nilai x: "))  # Langkah 1
y = int(input("Masukkan nilai y: "))    # Langkah 2

hasil = 1.0  # Langkah 3
pangkat = y  # Simpan nilai y untuk mencetak hasil

while y > 0:  # Langkah 4
    hasil *= x  # Langkah 4a
    y -= 1      # Langkah 4b

if pangkat > 1:  # Periksa apakah pangkat lebih dari 1
    print(f"{int(x)}^{pangkat} =", hasil)  # Cetak dengan notasi eksponen
else:
    print(f"{int(x)}^{pangkat} =", int(hasil))  # Cetak tanpa notasi eksponen
