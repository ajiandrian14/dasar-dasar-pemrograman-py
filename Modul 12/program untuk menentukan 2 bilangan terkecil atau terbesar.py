def cari_terbesar_terkecil(bilangan1, bilangan2):
    if bilangan1 > bilangan2:
        terbesar = bilangan1
        terkecil = bilangan2
    else:
        terbesar = bilangan2
        terkecil = bilangan1
    return terbesar, terkecil

print("Program Menentukan Bilangan Terbesar dan Terkecil")
bilangan1 = float(input("Masukkan bilangan pertama: "))
bilangan2 = float(input("Masukkan bilangan kedua: "))

bilangan_terbesar, bilangan_terkecil = cari_terbesar_terkecil(bilangan1, bilangan2)

print("Bilangan terbesar:", bilangan_terbesar)
print("Bilangan terkecil:", bilangan_terkecil)
