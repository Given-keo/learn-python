# latihan operasi komparasi dan operasi logika
# membuat gabungan area rentang dari angka

# ++++3------10++++
print('======= PENGECEKAN BILANGAN')
print('Untuk bilangan --> \nkurang dari 3 atau lebih dari 10')
bilangan = int(input('Masukkan angka : '))
cek = bilangan < 3 or bilangan > 10
print('bilangan bernilai =',cek)

# ----3+++++++10-----
print('\n======= PENGECEKAN BILANGAN')
print('Untuk bilangan --> \nlebih dari 3 dan kurang dari 10')
bilangan = int(input('Masukkan angka : '))
cek = bilangan > 3 and bilangan < 10
print('bilangan bernilai =',cek)

# +++++=5------10=+++++
print('\n======= PENGECEKAN BILANGAN')
print('Untuk bilangan --> \n1.kurang dari sama dengan 5 \n2.lebih dari sama dengan 10')
bilangan = int(input('Masukkan angka : '))
cek = bilangan <= 5 or bilangan >= 10
print('bilangan bernilai =',cek)

# -----5=+++++=10------
print('\n======= PENGECEKAN BILANGAN')
print('Untuk bilangan --> \n1.lebih dari sama dengan 5,dan\n2.kurang dari sama dengan 10')
bilangan = int(input('Masukkan angka : '))
cek = bilangan >= 5 and bilangan <= 10
print('bilangan bernilai =',cek)

# ------0++++++5-----8+++++11-----
print('\n======= PENGECEKAN BILANGAN')
print('Untuk bilangan --> \n1.lebih dari sama dengan 0,dan\n2.kurang dari sama dengan 5')
print('3.lebih dari sama dengan 8,dan\n4.kurang dari sama dengan 11')
bilangan = int(input('Masukkan angka : '))
cek = (bilangan >= 0 and bilangan <= 5) or (bilangan >= 8 and bilangan <= 11)
print('bilangan bernilai =',cek)
