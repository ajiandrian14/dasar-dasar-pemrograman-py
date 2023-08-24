n = int(input("Masukkan nilai n: "))  # Langkah 1
m = int(input("Masukkan nilai m: "))  # Langkah 2

if n > m:  # Langkah 3
    n, m = m, n

angka = n + 1  # Langkah 4

print("Angka yang lebih besar dari", n, "dan lebih kecil dari", m, "adalah:")
while angka < m:  # Langkah 5
    print(angka)  # Langkah 5a
    angka += 1  # Langkah 5b
