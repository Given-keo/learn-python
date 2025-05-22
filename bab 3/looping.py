# looping (perulangan)

# 1. for loop
'''
for (kondisi):
    aksi1
    aksi2
'''
# for loop dengan list
angka = [1,2,3,4,5] #ini adalah list
print('angka =',angka)

print('---------------------')
print('MENGGUNAKAN FOR LOOP')
print('---------------------')
for i in angka:
    print('i sekarang --->',i)
print('PROGRAM PERTAMA BERAKHIR\n')

# for loop dengan range
for i in range(5):
    print('i sekarang --->',i)
print('PROGRAM KEDUA BERAKHIR\n')

# for loop dengan data string
data_str = 'PYTHON'
for i in data_str:
    print(i)
print('PROGRAM KETIGA BERAKHIR\n')

# 2. while loop
'''
while (kondisi):
    aksi1
    aksi2
    dst...
'''
print('----------------------')
print('MENGGUNAKAN WHILE LOOP')
print('----------------------')
angka = 0

while angka < 5:
    print('indeks --->',angka,'Hello Python')
    angka += 1
print('PROGRAM BERAKHIR\n')

# penggunaan continue,pass,dan break
# 1. pass ---> berfungsi untuk kodingan sementara supaya tidak menyebabkan error
for i in range(5):
    pass

print('PENGGUNAAN DARI CONTINUE')
# 2. continue ---> berfungsi untuk melompati program dibawahnya
for i in range(6):
    if i == 3 or i == 5:
        continue
    print('i sekarang --->',i)

# 3. break ---> berfungsi untuk menghentikan program di suatu kondisi
print('\nPENGGUNAAN BREAK')
angka = 0

while angka < 5:
    if angka == 3:
        break
    print('angka =',angka,'---> PYTHON')
    angka += 1