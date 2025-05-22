# a = 10, a adalah variabel dengan nilai 10

# tipe data : angka satuan (int)
data_int = 1
print('data =',data_int,',bertipe =',type(data_int))

# tipe data : angka desimal (float)
data_float = 1.5
print('data =',data_float,',bertipe =',type(data_float))

# tipe data : kumpulan karakter (str)
data_str = "Given"
print('data =',data_str,',bertipe =',type(data_str))

# tipe data : biner --> True/False (bool)
data_bool = False
print('data =',data_bool,',bertipe =',type(data_bool))

'''
Tipe data khusus
'''

# bilangan kompleks (imajiner)
data_complex = complex(4,7)
print('data =',data_complex,', bertipe =',type(data_complex))

# tipe data dari bahasa c
from ctypes import c_double

data_c_double = c_double(10.4)
print('data =',data_c_double,', bertipe =',type(data_c_double))