# format string

# contoh generic
# contoh string
nama = 'Given'
print(f'halo {nama}')

# contoh angka float
angka = 0.3323
print(f'angka = {angka}')

# contoh boolean
boolean = True
print(f'boolean = {boolean}')

# contoh angka bilangan bulat
angka = 45
bilangan_bulat = f"bilangan bulat = {angka:d}"
print(bilangan_bulat)

# bilangan dengan ordo ribuan
angka = 50000000
uang = f"nominal = {angka:,}"
print(uang)

# desimal dengan batas belakang koma
angka = 1223.232442
koma = f"data float = {angka:.2f}"
print(koma)

# leading zero
angka = 12232421.232442
koma = f"data float = {angka:5.2f}"
print(koma)

# menampilkan tanda + atau -
bil_negatif = -10
bil_positif = +19.233
format_negatif = f"format = {bil_negatif:-d}"
format_positif = f"format = {bil_positif:+.2f}"
print(format_negatif)
print(format_positif)

# format untuk persen
desimal = 0.45
persen = f"format persen = {desimal:.0%}"
print(persen)

# format angka ke angka lain(hex,octal,binary)
angka = 255
binary = f"binary dari {angka} = {bin(angka)}"
octal = f"octal dari {angka} = {oct(angka)}"
hexadesimal = f"hexadesimal dari {angka} = {hex(angka)}"
print(binary)
print(octal)
print(hexadesimal)