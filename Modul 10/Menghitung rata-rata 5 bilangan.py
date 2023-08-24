print('Masukkan 5 Buah Bilangan')
print('------------------------')
jml = 0
bil = []
for i in range(5):
    print('Bilangan ke-%d :' % (i+1))
    x = int(input(' '))
    jml = jml + x
    bil.append(x)
rata2 = jml / 5
print('Data yang diinputkan : ')
print(bil)
print('\nRata-rata : %f \n' % rata2)
