# belajar tentang lambda
print('BELAJAR MENGGUNAKAN LAMBDA')
print('==========================')
# menggunakan def 
def f_kuadrat(angka)->int:
    return angka ** 2

print('hasil dari 3 pangkat 2 =',f_kuadrat(3))

# menggunakan lambda
# output = lambda argument:expression

kuadrat = lambda angka:angka**2
print(f'Hasil dari 3 pangka 2 =',kuadrat(3))

pangkat = lambda angka,pangkat:angka**pangkat
print(f'Hasil dari 2 pangka 3 =',pangkat(2,3))

# penerapan kegunaan

# 1. sorting biasa
data_list = ['otong','ucup','dudung','zida']
data_list.sort()
print('\ndata sortir biasa =',data_list)

# 2. sorting dengan len(panjang data)
def panjang_nama(nama):
    return len(nama)

data_list.sort(key=panjang_nama)
print('data sortir dengan len =',data_list)

# 3. sortir dengan lambda 
data_nama = ['abdul','rafli','fahmi','agus']
data_nama.sort(key=lambda nama:len(nama))
print('data sortir dengan lambda =',data_nama)

# filter
data_angka = [1,2,2,4,3,5,3,6,3,4,7,8,9,9,9]
def kurang_dari_lima(angka):
    return angka < 5

data_angka_baru = list(filter(kurang_dari_lima,data_angka))
data_lambda_angka = list(filter(lambda angka:angka<=3,data_angka))
print(data_angka_baru)
print(data_lambda_angka)

data_genap = list(filter(lambda angka:angka%2 == 0,data_angka))
print(data_genap)

# anymous 
# currying <- haskel curry
print('\nBELAJAR DENGAN ANYMOUS')
print('======================')

# menggunakan def biasa
def perpangkatan(angka,pangkat):
    return angka**pangkat

hasil = perpangkatan(5,2)
print('Hasil dari 5 pangkat 2 =',hasil)

# menggunakan haskel curry
def eksponen(n):
    return lambda angka:angka**n

pangkat2 = eksponen(2)
print(f'hasil dari 2 pangkat 2 = {pangkat2(2)}')
print(f'hasil dari 3 pangkat 2 = {pangkat2(3)}')
print(f'hasil dari 5 pangkat 3 = {eksponen(3)(5)}')