# latihan date and time

import datetime as waktu 

hari_ini = waktu.date.today()
print('hari ini tanggal =',hari_ini)
print(f'hari ini hari = {hari_ini:%A}')

tanggal_lahir = waktu.date(2006,3,3)
print('\ntanggal lahir =',tanggal_lahir)
print(f'lahir pada hari = {tanggal_lahir:%A}\n')

print('MASUKKAN TANGGAL, BULAN, DAN TANGGAL LAHIR ANDA')
tahun = int(input('Masukkan tahun   : '))
bulan = int(input('Masukkan bulan   : '))
tanggal = int(input('Masukkan tanggal : '))

tanggal_lahir = waktu.date(tahun,bulan,tanggal)
umur = (waktu.date.today() - tanggal_lahir) // 365

print('Tanggal lahir kamu adalah =',tanggal_lahir)
print('Kamu lahir pada hari',f"{tanggal_lahir:%A}")
print('Berarti saat ini kamu berumur',umur.days,'tahun')
