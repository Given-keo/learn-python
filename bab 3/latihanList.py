# praktek membuat program list 
# membuat daftar buku

list_buku = []
print('MASUKKAN DATA BUKU')
print('------------------')
while True:
    judul = input('masukkan judul : ')
    penulis = input('masukkan nama penulis : ')

    data_buku = [judul,penulis]
    list_buku.append(data_buku)


    lanjutan = input('\napakah masih ingin melanjutkan(y/n) : ')
    if lanjutan.lower() == 'n':
        break

print('\nDAFTAR BUKU')
print('-----------')
for index,buku in enumerate(list_buku):
    print(f'{index + 1}. nama buku = {buku[0]}, penulis = {buku[1]}')

print('\nPROGRAM TELAH BERAKHIR')