# LATIHAN FUNGSI
import os

def header():
    os.system('cls')
    print(f'{'-'*50:^50}')
    print(f'{'PROGRAM MENGHITUNG':^50}')
    print(f'{'LUAS DAN KELILING PERSEGI PANJANG':^50}')
    print(f'{'-'*50:^50}')

def input_user():
    lebar = int(input('Masukkan lebar   : '))
    panjang = int(input('Masukkan panjang : '))
    return lebar,panjang

def luas(lebar,panjang):
    return lebar*panjang

def keliling(lebar,panjang):
    return (lebar + panjang)*2

while True:
    header()
    LEBAR,PANJANG = input_user()
    LUAS = luas(LEBAR,PANJANG)
    KELILING = keliling(LEBAR,PANJANG)

    print(f'\n{'-'*50:^50}')
    print(f'{'HASIL PERHITUNGAN':^50}')
    print(f'{'-'*50:^50}')
    print('Hasil luas persegi panjang     =',LUAS,'cm')
    print('Hasil keliling persegi panjang =',KELILING,'cm')

    lanjutan = input('\nApakah kamu mau lanjut(y/n)? ')
    if lanjutan.lower() == 'n':
        break

print('PROGRAM TELAH BERAKHIR, TERIMAKASIH!!!')