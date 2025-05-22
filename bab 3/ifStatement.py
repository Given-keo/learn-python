# if statement (pengkondisian)
"""
if (kondisi1):
    aksi1
    aksi2
elif (kondisi2):
    aksi1
    aksi2
else:
    aksi3
"""

print('PENGECEKAN BILANGAN GENAP DAN GANJIL')
angka = int(input('Masukkan angka : '))
if angka == 0:
    print(angka,'merupakan bilangan nol')
elif angka % 2 == 0:
    print(angka,'merupakan bilangan genap')
else:
    print(angka,'merupakan bilangan ganjil')

print(' \nPENGECEKAN BILANGAN BULAT POSITIF, NOL, DAN NEGATIF')
angka = int(input('Masukkan angka : '))

if angka == 0:
    print(angka,'merupakan bilangam bulat nol')
elif angka > 0:
    print(angka,'merupakan bilangan bulat positif')
else:
    print(angka,'merupakan bilangan bulat negatif')