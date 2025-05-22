# latihan percabangan
# kalkulator sederhana

print('KALKULATOR SEDERHANA ====================')   
bilangan_pertama = int(input('Masukkan bilangan pertama  : '))
operasi = input('Masukkan operasi (+,-,x,/) : ')
bilangan_kedua = int(input('Masukkan bilangan kedua    : '))

print('-----------------------------------------')
if operasi == '+':
    print(f'hasil dari {bilangan_pertama} + {bilangan_kedua} adalah = {bilangan_pertama + bilangan_kedua}')
elif operasi == '-':
    print(f'hasil dari {bilangan_pertama} - {bilangan_kedua} adalah = {bilangan_pertama - bilangan_kedua}')
elif operasi.lower() == 'x' or operasi == '*':
    print(f'hasil dari {bilangan_pertama} x {bilangan_kedua} adalah = {bilangan_pertama * bilangan_kedua}')
elif operasi == '/':
    print(f'hasil dari {bilangan_pertama} / {bilangan_kedua} adalah = {bilangan_pertama / bilangan_kedua}')
else:
    print('PERINGATAN : operasi yang anda masukkan salah !')
print('-----------------------------------------')
print('PROGRAM TELAH BERAKHIR')
