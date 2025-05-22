# latihan looping
# membuat perkalian 5 - 10 dengan looping

# 1. menggunakan for loop
print('MENGGUNAKAN FOR')
for i in range(10):
    print('5 x',i+1,'=',(i+1)*5)

# 2. menggunakan while loop
print('\nMENGGUNAKAN WHILE')
angka = 0
while angka < 10:
    angka += 1
    print('5 x',angka,'=',5*angka)

print('='*15,'(MODE TERBALIK)')
# mode terbalik
for i in range(10,0,-1):
    print('5 x',i,'=',5*i)

print()

angka = 10
while angka > 0:
    print('5 x',angka,'=',5*angka)
    angka -= 1

print('='*15,'(GAMBAR SEGITIGA DENGAN LOOP)')
print('MENGGUNAKAN FOR')
for i in range(5):
    print('*'*(i+1))

print('\nMENGGUNAKAN WHILE')
angka = 0
while angka < 5:
    angka += 1
    print('*'*angka)

print('='*15,'(MODE TERBALIK)')
# pake for
for i in range(5,0,-1):
    print('*'*(i))

print()

# menggunakan while
angka = 5
while angka > 0:
    print('*'*angka)
    angka -= 1

print('='*15,'(GAMBAR SEGITIGA UTUH)')
