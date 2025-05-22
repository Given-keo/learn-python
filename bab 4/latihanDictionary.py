# latihan dictionary

import datetime as waktu
import os
import random
import string

# template data dictionary
template = {
    'nama':'nama',
    'nim':'0000000000',
    'sks lulus':0,
    'lahir':waktu.datetime(1111,1,1)
}

# dictionary penampung
data_mahasiswa = {}

while True:
    # program clear otomatis
    # os.system('cls')
    print('='*70)
    print('\t\tSELAMAT DATANG DI PROGRAM LATIHAN DICTIONARY')
    print('         \t\tMASUKKAN DATA MAHASISWA')
    print('='*70)

    mahasiswa = dict.fromkeys(template.keys())
    mahasiswa['nama'] = input('Masukkan nama : ')
    mahasiswa['nim'] = int(input('Masukkan NIM : '))
    mahasiswa['sks lulus'] = int(input('Masukkan jumlah sks : '))
    TAHUN = int(input('Masukkan tahun lahir(YYYY) : '))
    BULAN = int(input('Masukkan bulan lahir(1-12) : '))
    TANGGAL = int(input('Masukkan tanggal lahir(1-30) : '))
    mahasiswa['lahir'] = waktu.datetime(TAHUN,BULAN,TANGGAL)

    KEY = ''.join(random.choice(string.ascii_uppercase) for i in range(4))
    data_mahasiswa.update({KEY:mahasiswa})

    print('='*70)
    print(f'{'KEY':<6} {'NAMA':<18} {'NIM':<12} {'SKS':<5} {'LAHIR':>11}     ')
    print('='*70)

    for data in data_mahasiswa:
        KEY = data

        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks lulus']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

        print(f'{KEY:<6} {NAMA:<18} {NIM:<12} {SKS:<5}    {LAHIR:>11}')
    
    print()
    
    lanjutan = input('Apakah anda masih ingin lanjut(y/n) : ')
    if lanjutan.upper() == 'N':
        break

print('='*70)
print(f'{'Program telah berakhir':^66}')
print('='*70)