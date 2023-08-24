class KonversiSuhu:
    def celcius_ke_fahrenheit(self, suhu_celcius):
        suhu_fahrenheit = (suhu_celcius * 9/5) + 32
        return suhu_fahrenheit

    def celcius_ke_reamur(self, suhu_celcius):
        suhu_reamur = suhu_celcius * 4/5
        return suhu_reamur

# Membuat objek KonversiSuhu
konversi = KonversiSuhu()

# Meminta pengguna untuk memasukkan suhu dalam Celcius
suhu_celcius = float(input("Masukkan suhu dalam Celcius: "))

# Menghitung dan menampilkan hasil konversi
suhu_fahrenheit = konversi.celcius_ke_fahrenheit(suhu_celcius)
suhu_reamur = konversi.celcius_ke_reamur(suhu_celcius)

print(f"{suhu_celcius} Celcius sama dengan {suhu_fahrenheit} Fahrenheit")
print(f"{suhu_celcius} Celcius sama dengan {suhu_reamur} Reamur")

