n = int(input("Masukkan nilai n: "))  # Langkah 1

faktorial = 1  # Langkah 2
original_n = n  # Simpan nilai n untuk mencetak n! pada hasil

while n > 1:  # Langkah 3
    faktorial *= n  # Langkah 3a
    n -= 1  # Langkah 3b

print(f"{original_n}! =", faktorial)  # Langkah 4