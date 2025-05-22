# BELAJAR COPY DICTIONARY

teman = {
    'bar':'akbar',
    'kri':'fikri',
    'han':'johan',
    'dul':'abdul'
}

print('data teman =',teman,'\n')

# copy dictionary
data_copy = teman.copy()

print('data asli =',teman)
print('data copy =',data_copy,'\n')

teman['kri'] = 'bachri'
print('data teman asli =',teman)
print('data copy teman =',data_copy,'\n')

# pop dictionary (berdasarkan key)
print('data copy awal =',data_copy)
data_abdul = data_copy.pop('dul')
print('data copy di pop =',data_copy)
print('data abdul =',data_abdul)

print('data pop kri =',data_copy.pop('kri'))
print('data copy =',data_copy,'\n')

# pop item dictionary (berdasarkan data terakhir)
print('data awal =',teman)
data_terakhir = teman.popitem()
print('sekarang datanya menjadi =',teman)
