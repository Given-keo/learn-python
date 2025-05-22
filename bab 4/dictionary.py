# BELAJAR DICTIONARY
'''
data_dictionary = {
    key1 : value1,
    key2 : value2
}
'''
print('BELAJAR DICTIONARY')
print('==================')
list_angka = [0,1,2,3]

data_diri = {
    'nama':'given',
    'umur':18,
    'tinggi badan':165.45,
    'ktp':True,
    'data list':list_angka
}

print('data diri',data_diri,'\n')

# OPERASI DICTIONARY
print('OPERASI DICTIONARY')
print('==================')
data_dictionary = {
    'nama1':'ahmad',
    'nama2':'firdaus',
    'nama3':'asep'
}
print('data awal =',data_dictionary)

# panjang dictionary
LENDICT = len(data_dictionary)
print('panjang data dictionary =',LENDICT)

# pengecekan key 
KEY = 'nama1'
CHECKKEY = KEY in data_dictionary
print('key nama1 berada dalam data dictionary =',CHECKKEY)

# mengakses value dengan get
print('data nama =',data_dictionary['nama2'])
print('data get =',data_dictionary.get('nama3'))
print('data get =',data_dictionary.get('nama5','nama tidak terdaftar dalam data'))

# memperbarui data (update data)
print('nama1 =',data_dictionary['nama1'])
data_dictionary.update({'nama1':'udin'})
print('nama1 setelah di update =',data_dictionary['nama1'])

# menghapus data dalam dictionary
del data_dictionary['nama3']
print(data_dictionary,'\n')

# LOOPING DALAM DICTIONARY
print('LOOPING DALAM DICTIONARY')
print('========================')
teman = {
    'bar':'akbar',
    'kri':'fikri',
    'dul':'abdul',
    'han':'johan'
}
print('data looping =',teman)

# looping dengan menggunakan get
for data in teman:
    print('nama =',teman.get(data))

print()

# looping dengan menggunkan values()
for data in teman.values():
    print('data =',data)

print()

# pengambilan item
for key,values in teman.items():
    print(f'key = {key}, value = {values}')
