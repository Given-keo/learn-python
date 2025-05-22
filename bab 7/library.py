import datetime
data_waktu = datetime.datetime.now()
print(f'waktu saat ini =',data_waktu)
print(f'tahun = {data_waktu.year}')
print(f'bulan = {data_waktu.month}')
print(f'hari = {data_waktu.strftime('%A')}')

from collections import Counter

data = ['a','b','c','d','e']
data_count = Counter(data)

print(f'data = {data_count}')
print(f'jumlah a = {data_count['a']}')
print(f'jumlah b = {data_count['b']}')