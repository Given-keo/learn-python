# operasi komparasi
# setiap hasil dari komparasi adalah boolean

'''
1. >, lebih dari
2. <, kurang dari
3. >=, lebih dari sama dengan
4. <=, kurang dari sama dengan
5. ==, sama dengan
7. !=, tidak sama dengan
8. is
9. is not
'''

a = 5
b = 2

# lebih besar dari, >
print('========= LEBIH BESAR (>)')
hasil = a > b
print(a,'>',b,'=',hasil)

hasil = b > a
print(b,'>',a,'=',hasil,'')

# kurang dari, <
print('========= KURANG DARI (<)')
hasil = a < b
print(a,'<',b,'=',hasil)

hasil = b < a
print(b,'<',a,'=',hasil,'')

# lebih dari sama dengan, >=
a = 10
b = 10
print('========= LEBIH DARI SAMA DENGAN (>=)')
hasil = a >= b
print(a,'>=',b,'=',hasil)

a = 5
b = 4
hasil = b >= a
print(b,'>=',a,'=',hasil,'')

# kurang dari sama dengan, >=
a = 10
b = 10
print('========= KURANG DARI SAMA DENGAN (>=)')
hasil = a <= b
print(a,'<=',b,'=',hasil)

a = 5
b = 4
hasil = a <= b
print(a,'<=',b,'=',hasil,'')

# sama dengan, ==
a = 10
b = 10
print('========= SAMA DENGAN (==)')
hasil = a == b
print(a,'==',b,'=',hasil)

a = 5
b = 4
hasil = a == b
print(a,'==',b,'=',hasil,'')

# tidak sama dengan, !=
a = 10
b = 10
print('========= SAMA DENGAN (!=)')
hasil = a != b
print(a,'!=',b,'=',hasil)

a = 5
b = 4
hasil = a != b
print(a,'!=',b,'=',hasil)

# is sebagai komparasi object identify
print('========= object identify (IS)')
x = 5
y = 5

print('nilai x =',x,', id =',hex(id(x)))
print('nilai y =',y,', id =',hex(id(y)))
hasil = x is 5
print('x is 5 =',hasil)
hasil = x is y
print('x is y =',hasil)

# is not sebagai komparasi object identify
print('========= object identify (IS NOT)')
x = 5
y = 6

print('nilai x =',x,', id =',hex(id(x)))
print('nilai y =',y,', id =',hex(id(y)))
hasil = x is not 5
print('x is 5 =',hasil)
hasil = x is not y
print('x is y =',hasil)