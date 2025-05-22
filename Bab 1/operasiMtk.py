#  OPERASI MATEMATIKA

# operasi pertambahan 
a = 10
b = 3
tambah = a + b
print(a,'+',b,'=',tambah)

# operasi pengurangan
kurang = a - b
print(a,'-',b,'=',kurang)

# operasi perkalian
kali = a * b
print(a,'x',b,'=',kali)

# operasi pembagian
bagi = a / b
print(a,':',b,'=',bagi)

# pangkat
pangkat = a ** b
print(a,'^',b,'=',pangkat)

# modulus 
mod = a % b
print(a,'%',b,'=',mod)

# floor 
floor = a // b
print(a,'//',b,'=',floor)

# PRIORITAS PERHITUNGAN
'''
1. () --> kurung lebih diutamakan
2. eksponen
3. perkalian, pembagian, floor, modulus
4. pertambahan dan pengurangan
'''

a = 5
b = 2

operasi_campuran = (a + b) * b + a
print('(',a,'+',b,') x',b,'+',a,'=',operasi_campuran)

