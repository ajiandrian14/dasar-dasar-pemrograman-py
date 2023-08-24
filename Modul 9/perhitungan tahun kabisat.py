tahun = int(input("Masukkan tahun: "))  # Langkah 1

if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):  # Langkah 2
    print(f"{tahun} adalah tahun kabisat.")  # Langkah 4
else:  # Langkah 3
    print(f"{tahun} bukan tahun kabisat.")  # Langkah 4