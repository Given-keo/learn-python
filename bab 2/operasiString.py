# operasi dan manipulasi string 

# 1. menyambung string (concatenate)
nama_pertama = 'Given'
nama_kedua = 'Ezra'
nama_ketiga = 'D.K'

nama_lengkap = nama_pertama + ' ' + nama_kedua + ' ' + nama_ketiga
print(nama_lengkap)

# 2. menghitung panjang string
print('panjang nama =',str(len(nama_lengkap)))

# 3. operator untuk string

# memeriksa komponen suatu char dalam string
d = 'G'
status = d in nama_lengkap
print('apakah ada "G" didalam variabel nama_lengkap =',status)

d = 'G'
status = d not in nama_lengkap
print('apakah ada "G" didalam variabel nama_lengkap =',status)

# mengulang string 
print('wk'*10)

# indexing
print('index ke-0 = '+ nama_lengkap[0])
print('index ke-1 = '+ nama_lengkap[1])
print('index ke-(-1) = '+ nama_lengkap[-1])
print('index ke-(-2) = '+ nama_lengkap[-2])
print('index ke-(-3) = '+ nama_lengkap[-3])
print('index ke-(0:3) = '+ nama_lengkap[0:3])
print('index ke-(7:10) = '+ nama_lengkap[6:10])
print('index ke-(0:10:2) = '+ nama_lengkap[0:10:2])

# item paling kecil
print('item terkecil dari variabel nama_lengkap = ' + min(nama_lengkap))

# item paling besar
print('item terbesar dari variabel nama_lengkap = ' + max(nama_lengkap))


# ascii code
ascii_code = ord(" ")
print('ASCII code untuk spasi adalah =',str(ascii_code))
ascii_code = 113
print('ASCII code untuk spasi adalah =',chr(ascii_code))

# 4. Operator dalam bentuk method
nama = 'Abdul Rahmat Karim'
print('Banyak char "a" dalam variabel nama =',nama.count('a'))