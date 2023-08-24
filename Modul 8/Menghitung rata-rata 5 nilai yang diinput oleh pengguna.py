total = 0  # Langkah 1

for i in range(5):  # Langkah 2
    nilai = float(input(f"Masukkan nilai ke-{i+1}: "))  # Langkah 2a
    total += nilai  # Langkah 2b

rata_rata = total / 5  # Langkah 3

print("Rata-rata dari 5 nilai adalah:", rata_rata)  # Langkah 4