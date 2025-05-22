# input
# menyimpan data berdasarkan inputan data

# secara default tipe data yang diambil adalah string
data_str = input("masukkan nama : ")
print('data =',data_str,', bertipe =',type(data_str))

# cara mengambil data bertipe int
data_int = int(input('masukkan angka : '))
print('data =',data_int,', bertipe =',type(data_int))

# cara mengambil data bertipe float
data_float = float(input('masukkan angka desimal : '))
print('data =',data_float,', bertipe =',type(data_float))

# cara mengambil data bertipe biner(bool)
data_bool = bool(int(input('masukkan angka : ')))
print('data =',data_bool,', bertipe =',type(data_bool))