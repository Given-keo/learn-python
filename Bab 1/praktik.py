# membuat program konversi suhu sederhana

# program konversi suhu dari celcius ke suhu lainnya 
print("PROGRAM KONEVERSI SUHU DARI CELCIUS")
celcius = int(input('Masukkan suhu dalam celcius : '))

print('\n======= HASIL KONVERSI SUHU =======')
reamur = (4/5) * celcius
kelvin = 273 + celcius
fahrenheit = ((9/5) * celcius) + 32
print('suhu dalam celcius :',celcius,'C')
print('suhu dalam reamur :',reamur,'R')
print('suhu dalam fahrenheit :',fahrenheit,'F')
print('suhu dalam kelvin :',kelvin,'K')