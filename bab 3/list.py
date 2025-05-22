# BELAJAR LIST
# list itu adalah tempat menampung sekumpulan data

# list kumpulan numbers
data_angka = [1,2,3,4,5]
print('data list angka =',data_angka)

# list kumpulan string
data_string = ['abdul','ahmad','catharina']
print('data list string =',data_string)

# list kumpulan data boolean
data_bool = [True,False,True]
print('data list boolean =',data_bool)

# list data campuran
data_campuran = [1,2,'Hamdah','Akmal',True,False]
print('data list campuran =',data_campuran)

## cara alternatif dalam membuat list
data_range = range(0,10,2)
data_list = list(data_range)
print('data list =',data_list)

# membuat data list dengan perulangan for
list_for = [i+1 for i in range(0,5)]
print('list menggunakan for loop =',list_for)

# membuat list dengan for dan if
list_for_if = [i for i in range(6) if i != 3 and i != 0]
print('list menggunakan for dan if =',list_for_if)

# MANIPULASI LIST
# operasi dalam list
'''
        index-0,index-1
list = ['asep','python']
'''
print('\nBELAJAR MANIPULASI STRING')
print('==========================')
# list buah
list_buah = ['melon','pisang','semanggka']
print('list buah =',list_buah)

# mengambil salah satu data dari sebuah string
buah_pertama = list_buah[0]
print('buah pertama =',buah_pertama)

buah_terakhir = list_buah[-1]
print('buah terakhir =',buah_terakhir)

# mengecek panjang data 
panjang_list = len(list_buah)
print('banyak data list =',panjang_list)

# menambah data list berdasarkan posisi
list_buah.insert(1,'jeruk')
print('sesudah ditambahkan =',list_buah)

# menambahkan item di posisi paling terakhir
list_buah.append('alpukat')
print('menambahkan item di posisi terakhir =',list_buah)

# menambahkan list dengan list
data_baru = ['belimbing','jambu']
print('data baru =',data_baru)
list_buah.extend(data_baru)
print('data gabungan =',list_buah)

# mengubah nilai data didalam list
list_buah[0] = 'strawberry'
list_buah[1] = 'anggur'
print('data list terbaru =',list_buah)

# cara menghapus item dalam sebuah list
list_buah.remove('alpukat')
list_buah.remove('pisang')
print('data list dihapus =',list_buah)

# cara menghapus data paling terakhir
list_buah.pop()
print('data list terakhir dihapus =',list_buah)


# OPERASI LIST
print('\nOPERASI LIST')
print('=============')

data = [5,1,1,3,3,2,4,4,5,5,6,6]
print('data =',data)

# count data/menghitung data
data_4 = data.count(4)
data_5 = data.count(5)
print('banyak data 4 =',data_4)
print('banyak data 5 =',data_5)

# mengecek posisi
data_peserta = ['abdul','johan','rahmat']
print('data peserta =',data_peserta)
data_johan = data_peserta.index("johan")
data_rahmat = data_peserta.index("rahmat")
print('johan berada pada index-ke =',data_johan)
print('rahmat berada pada index-ke =',data_rahmat)

# mengurutkan data dalam sebuah list
data.sort()
print('data di sortir =',data)

# membalik urutan dalam sebuah list
data.reverse()
print('data dibalik =',data)

## DUPLIKAT LIST(COPY LIST)
print('\nDUPLIKAT LIST')
print('==============')

a = ['given','jeffrey','ulil']
b = a
print('anggota a =',a)
print('anggota b =',b)

# kita akan merubah data dari a
a[2] = 'sulaiman'
a.sort()
print('anggota a sekarang jadi =',a)
print('anggota b sekarang jadi =',b)
print('address id a =',hex(id(a)))
print('address id b =',hex(id(b)))
# kesimpulannya maka data yang ada di b akan ikut berubah

# menduplikat list dengan copy
c = a.copy()
print('\nanggota a =',a)
print('anggota b =',b)
print('anggota c =',c)
print('address id a =',hex(id(a)))
print('address id b =',hex(id(b)))
print('address id c =',hex(id(c)))

print('\ndata[0] c diubah jadi = "anto"\n')
c[0] = 'anto'
print('anggota a =',a)
print('anggota b =',b)
print('anggota c =',c)

print('\ndata[0] a diubah jadi = "erpan"\n')
a[0] = 'erpan'
print('anggota a =',a)
print('anggota b =',b)
print('anggota c =',c)

# NESTED LIST
# LIST BERSARANG
print('\nNESTED LIST')
print("============")

data_angka_biasa = [1,2,3,4]
data_angka1 = [1,2]
data_angka2 = [3,4]
data_angka_gabungan = [data_angka1,data_angka2] #nested list

print('data angka biasa =',data_angka_biasa)
print('data angka pertama =',data_angka1)
print('data angka kedua =',data_angka2)
print('data angka gabungan =',data_angka_gabungan)

# penerapan dari nested list
data1 = ['Sulaiman',16,'Jakarta']
data2 = ['Fahmi',18,'Tangerang']
data3 = ['Asep',15,'Lampung']
data_peserta = [data1,data2,data3]

print('\ndata peserta')
print('------------- ')
for data in data_peserta:
        print('nama =',data[0])
        print('umur =',data[1])
        print('asal =',data[2],'\n')

# dengan references
list_copy = data1.copy()
print('data asli =',data1)
print('data copy =',list_copy)
print('addres data asli =',hex(id(data1)))
print('addres data copy =',hex(id(list_copy)))
print('\ndata index[0] diubah jadi = "Owen"\n')
data1[0] = 'Owen'
print('data asli =',data1)
print('data copy =',list_copy,'\n')

# BELAJAR DEEP COPY
# cara mengambil data dari nested list
data_angka = [[1,2],[3,4]]
print('data angka =',data_angka)
print('mengambil data indeks-0 =',data_angka[0])
print('mengambil data indeks-0 dari dalam list pertama =',data_angka[0][0])
print('mengambil data indeks-1 dari dalam list pertama =',data_angka[0][1])

# duplikat dari nested list
copy_data = data_angka.copy()
print('address dari nested list asli =',hex(id(data_angka)))
print('address dari nested list copy =',hex(id(copy_data)))
print('\nmengecek data address indeks 1 dalam list')
print('addres indeks ke-1 asli =',hex(id(data_angka[0])))
print('addres indeks ke-1 copy =',hex(id(copy_data[0])))

# maka cara kita mengatasinya yaitu dengan cara menggunaka deep copy
from copy import deepcopy
print('\nMENGUNAKAN DEEP COPY UNTUK DUPLIKAT NESTED LIST')
print('================================================')
data_angka = [[1,2],[3,4]]
copy_data = deepcopy(data_angka)

print('address dari nested list asli =',hex(id(data_angka)))
print('address dari nested list copy =',hex(id(copy_data)))
print('\nmengecek data address indeks 1 dalam list')
print('addres indeks ke-1 asli =',hex(id(data_angka[0])))
print('addres indeks ke-1 copy =',hex(id(copy_data[0])))

# cara me-looping list
# 1. for loop
print('\nMELAKUKAN LOOPING PADA LIST')
print('============================')

data_angka = [1,2,3,4]
print('data angka =',data_angka)
for data in data_angka:
        print('angka =',data)

print()

data_peserta = ['given','messi','ronaldo']
print('data peserta =',data_peserta)
for peserta in data_peserta:
        print('nama =',peserta)

# 2. menggunakan for loop dan range
print('\nmenggunakan for')
kumpulan_angka = [1,4,2,6,2]
print('kumpulan angka =',kumpulan_angka)
panjang = len(kumpulan_angka)

for i in range(panjang):
        print('angka =',kumpulan_angka[i])

# 3. menggunakan while
print('\nmenggunakan while')
kumpulan_angka = [1,4,2,6,2]
print('kumpulan angka =',kumpulan_angka)
i = 0

while i < len(kumpulan_angka):
        print('angka =',kumpulan_angka[i])
        i += 1

# 4. menggunakan enumerate
print('\nmenggunakan enumerate')
data = [1,2,'given',True,"abdul"]
for index,data in enumerate(data):
        print('data ke',index,', data =',data)

# 5. list comphrehensin
print('\nmenggunakan list komprehensif')
data = [1,2,'given',True,"abdul"]
[print(f"data = {i}") for i in data]
