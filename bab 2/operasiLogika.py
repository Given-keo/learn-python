# operasi logika atau boolean

# not, or, and, xor

# penggunaan not
print('=========== NOT')
a = True
b = not a
print('a =',a)
print('---- NOT ---')
print('b =',b)

# penggunaan or
print('\n=========== OR')
a = True
b = True
hasil = a or b
print(a,'or',b,'=',hasil)

a = True
b = False
hasil = a or b
print(a,'or',b,'=',hasil)

a = False
b = True
hasil = a or b
print(a,'or',b,'=',hasil)

a = False
b = False
hasil = a or b
print(a,'or',b,'=',hasil)
# kesimpulannya ketika ada nilai yang bernilai True maka akan menghasilkan True

# and
print('\n=========== AND')
a = True
b = True
hasil = a and b
print(a,'and',b,'=',hasil)

a = True
b = False
hasil = a and b
print(a,'and',b,'=',hasil)

a = False
b = True
hasil = a and b
print(a,'and',b,'=',hasil)

a = False
b = False
hasil = a and b
print(a,'and',b,'=',hasil)
# kesimpulannya jika dua buah nilai bernilai True maka akan menghasilkan True

# xor
print('\n=========== XOR(^)')
a = True
b = True
hasil = a ^ b
print(a,'xor',b,'=',hasil)

a = True
b = False
hasil = a ^ b
print(a,'xor',b,'=',hasil)

a = False
b = True
hasil = a ^ b
print(a,'xor',b,'=',hasil)

a = False
b = False
hasil = a ^ b
print(a,'xor',b,'=',hasil)
# kesimpulan jika nilai mengandung nilai yang berbeda akan menghasilkan True