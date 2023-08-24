import math

def segitiga_siku_siku(a, t):
    L = 0.5 * a * t
    K = a + t + math.sqrt(a*a + t*t)
    return L, K

print('Program Segitiga Siku-siku')
print('--------------------------')

alas = float(input('Masukkan alas: '))
tinggi = float(input('Masukkan tinggi: '))

luas, keliling = segitiga_siku_siku(alas, tinggi)

print('--- Hasil ---')
print('Luas : ' + str(luas))
print('Keliling: ' + str(keliling))
