total_belanja = float(input("Masukkan total belanja: "))  # Langkah 1

if total_belanja > 500000:  # Langkah 2a
    diskon = 0.1 * total_belanja
elif total_belanja > 250000:  # Langkah 2b
    diskon = 0.05 * total_belanja
else:  # Langkah 2c
    diskon = 0

total_bayar = total_belanja - diskon  # Langkah 3

print(f"Total belanja: Rp. {total_belanja:,.2f}")
print(f"Diskon: Rp. {diskon:,.2f}")
print(f"Total bayar: Rp. {total_bayar:,.2f}")  # Langkah 4