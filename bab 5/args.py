# penggunaan args dalam fungsi
print('PENGGUNAAN *ARGS')
print('================')

def pembuka(*args):
    nama = args[0]
    print(f'Halo selamat malam {nama}')

pembuka('abdul')

def mahasiswa(*data):
    nama = data[0]
    nim = data[1]
    jurusan = data[2]
    return nama,nim,jurusan

hasil = mahasiswa('given',1223,'TI')
print(hasil)

# penggunaan kwargs
print('\nPENGGUNAAN **KWARGS')
print('===================')

def data_mahasiswa(**kwargs):
    nama = kwargs['nama']
    nim = kwargs['nim']
    jurusan = kwargs['jurusan']
    print('DATA MAHASISWA :')
    print(f'nama = {nama}\nnim = {nim}\njurusan = {jurusan}')

data_mahasiswa(nama='jepri',nim=123456,jurusan='matematika murni')

# penggunaan gabungan 
print('\nPENGGUNAAN GABUNGAN')
print('===================')
def kalkulator(*args,**kwargs):
    output = 0
    if kwargs['option'] == 'tambah':
        for angka in args:
            output += angka
        print(f'Hasil tambah = {output}')

    elif kwargs['option'] == 'kali':
        awalan = 1
        for angka in args:
            awalan *= angka
        print(f'Hasil kali = {awalan}')

hasil = kalkulator(5,2,3,option='tambah')
