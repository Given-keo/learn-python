# operasi assigment
# operasi ditambah dengan assignment

a = 5
print('nilai a =',a)

# penjumlahan, pengurangan, dan perkalian
a += 1
print('nilai a += 1 menjadi =',a) #a += 1 artinya a = a + 1
a -= 2
print('nilai a -= 2 menjadi =',a) #a -= 1 artinya a = a - 2
a *= 5
print('nilai a *= 5 menjadi =',a,'\n') #a += 1 artinya a = a x 5

# modulus dan floor
b = 10
print('b nilai =',b)

b %= 3
print('nilai b %= 3 menjadi =',b)

b = 10
b //= 3
print('nilai b //= 3 menjadi =',b)

a = 5
print('\nnilai a =',a)

# perpangkatan
a **= 3
print('nilai a **= 3 menjadi =',a,'\n')

# operasi bitwise
# OR
c = True
print('nilai c =',c)
c |= False
print('nilai dari c |= False menjadi =',c)
c = False
print('nilai c =',c)
c |= False
print('nilai dari c |= False menjadi =',c,'\n')

# AND
c = True
print('nilai c =',c)
c &= False
print('nilai dari c &= False menjadi =',c)
c = False
print('nilai c =',c)
c &= False
print('nilai dari c &= False menjadi =',c)
c = True
print('nilai c =',c)
c &= True
print('nilai dari c &= True menjadi =',c)

# SHIFTING
d = 0b01010
print('\nnilai d =',format(d,'04b'))
d >>= 2
print('nilai menjadi =',format(d,'04b'))

d = 0b01010
print('\nnilai d =',format(d,'04b'))
d <<= 2
print('nilai menjadi =',format(d,'04b'))