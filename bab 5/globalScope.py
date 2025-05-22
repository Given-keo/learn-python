# GLOBAL DAN LOCAL SCOPE
# 1.VARIABEL GLOBAL SCOPE
print('PNEGGUNAAN VAR GLOBAL')
print('=====================')
var_global = 'ini variabel global' #ini variabel global

# akses var global dalam def
def fungsi():
    print(f'menampilkan var global : {var_global}')

fungsi()

# akses var global dengan loop
for i in range(0,5):
    print(f'loop {i} = print {var_global}')

# percabangan 
if True:
    print(var_global)

# 2.VARIABEL LOCAL SCOPE
print('\nPENGGUNAAN LOCAL SCOPE')
print('======================')
def fungsi2():
    var_local = 'ini variabel local' #ini adalah variabel local
    print(var_local)

fungsi2()

# 1. contoh akses penggunaan
def sapa():
    print(f'halo, selamat sore {nama}')

nama = 'given'
sapa()

# 2. merubah variabel global
angka = 0
name = 'asep'

def ubah_angka(nilai_baru,nama_baru):
    global angka #mengubah variabel menjadi global sehingga dapat diakses secara bebas
    global name
    angka = nilai_baru
    name = nama_baru

print(f'sebelum di rubah angka = {angka}, nama : {name}')
ubah_angka(10,'given')
print(f'sesudah diubah angka = {angka}, nama : {name}')

