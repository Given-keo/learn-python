# BELAJAR TENTANG FUNGSI

'''
def namaDef(parameter):
    isi dari fungsi
'''

# FUNGSI TANPA PARAMETER
# fungsi menyapa
print('FUNGSI TANPA PARAMETER')
print('======================')
def menyapa():
    print('hello world')

# memanggil fungsi dari menyapa
menyapa()

# FUNGSI DENGAN PARAMETER
print('\nFUNGSI DENGAN PARAMETER')
print('=======================')
def sapaan(nama):
    print(f'Halo bagaimana kabarmu? {nama}')

sapaan('joko')

# program pertambahan 
def jumlah(angka1,angka2):
    print(f'{angka1} + {angka2} = {angka1 + angka2}')

jumlah(2,3)
jumlah(10,5)

def anggota(peserta):
    for nama in peserta:
        print(f'halo {nama}, selamat datang di kompetisi!!')

anggota_peserta = ['given','mail','upin']
anggota(anggota_peserta)

# DEF DENGAN RETURN(PENGEMBALIAN NILAI)
print('\nFUNGSI DENGAN PENGEMBALIAN NILAI')
print('================================')
def tambah(angka1,angka2):
    jumlah = angka1 + angka2

hasil = tambah(3,5)
print(hasil) #ketika kita print, maka akan menghasilkan nilai none
# karena itu kita perlu untuk melakukan pengembalian nilai dengan return

def kurang(angka1,angka2):
    kurang = angka1 - angka2
    return kurang

hasil = kurang(10,3)
print(10,'-',3,'=',hasil)

def kali(angka1,angka2):
    return angka1 * angka2

hasil = kali(2,3)
print(2,'x',3,'=',hasil)

def operasi_matematika(angka1,angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2
    return tambah,kurang,kali,tambah

jumlah,kurang,kali,bagi = operasi_matematika(10,5)
print(f'\nhasil tambah = {jumlah}')
print(f'hasil kurang = {kurang}')
print(f'hasil kali = {kali}')
print(f'hasil bagi = {bagi}')


# FUNGSI DENGAN DEFAULT ARGUMEN
print('\nFUNGSI DENGAN DEFAULT ARGUMEN ATAU PARAMETER')
print('=============================================')

def sapa(nama,sapa='hello'):
    print(f'{sapa}, selamat malam! {nama}')

sapa('Given','Hai')
sapa('Jeffrey')

def pangkat(angka,pangkat):
    pangkat = angka**pangkat
    return pangkat

hasil = pangkat(2,3)
print('hasil pangkat =',hasil)

hasil = pangkat(angka=5,pangkat=2)
print('hasil pangkat =',hasil)

