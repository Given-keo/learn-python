# lanjutan dari operasi string 

#  merubah case dalam string

# merubah semua ke uppercase dan lowercase
teks = 'Hello World!'
print('teks normal =',teks)
print('teks upper case =',teks.upper())
print('teks lower case =',teks.lower(),'\n')

# mengecek is X method
nama = "given" #hasilnya akan boolean
print(nama,'apakah lowercase =',nama.islower())
print(nama,'apakah uppercase =',nama.isupper())

# isalpha() ---> untuk mengecek semuanya huruf
# isalnum() ---> untuk mengecek angka dan huruf
# isdecimal() ---> untuk mengecek angka saja
# isspace() ---> spasi, tab, newline(\n)
# istitle() ---> semua kata yang dimulai dari huruf besar
teks = 'Hello World!'
print('\nteks =',teks)
print('Apakah teksnya kapital di setiap kata =',teks.istitle())

# mengecek kalimat awal dan akhir
teks = 'Hello World!'
print('\nteks =',teks)
print('start dari teks "Hello" =',teks.startswith('Hello'))
print('end dari teks "Hello" =',teks.endswith('Hello'))

# penggabungan teks dan pemisahan
biodata = ["halo","nama","saya","Given"]
gabungan = ' '.join(biodata)
print('biodata =',biodata)
print('biodata dengan join =',gabungan)
gabungan = "halobronamabrosayabrogiven"
print('biodata dengan split kalimat "nama" =', gabungan.split('bro'))

# alokasi karakter rjust(), ljust(), center()
# strip() menghapus elemen karakter

