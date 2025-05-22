# belajar multikeys dan nesting dalam dictionary
import datetime as waktu

mahasiswa1 = {
    'nama':'Abdul Fakri',
    'nim':'1124160003',
    'sks lulus':'19',
    'beasiswa':False,
    'lahir':waktu.datetime(2006,3,3)
}

mahasiswa2 = {
    'nama':'Ivan Jacub',
    'nim':'1124160083',
    'sks lulus':'19',
    'beasiswa':False,
    'lahir':waktu.datetime(2006,10,3)
}

mahasiswa3 = {
    'nama':'Ahmad Bachri',
    'nim':'1124160123',
    'sks lulus':'19',
    'beasiswa':False,
    'lahir':waktu.datetime(2006,5,15)
}

data_mahasiswa = {
    'M101':mahasiswa1,
    'M102':mahasiswa2,
    'M103':mahasiswa3
}

print('='*70)
print(f'{'KEY':<6} {'NAMA':<18} {'NIM':<12} {'SKS':<5}{'BEASISWA':<6} {'LAHIR':>11}     |')
print('='*70)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa

    NAMA = data_mahasiswa[mahasiswa]['nama']
    NIM = data_mahasiswa[mahasiswa]['nim']
    SKS = data_mahasiswa[mahasiswa]['sks lulus']
    BEASISWA = data_mahasiswa[mahasiswa]['beasiswa']
    LAHIR = data_mahasiswa[mahasiswa]['lahir'].strftime("%x")

    print(f'{KEY:<6} {NAMA:<18} {NIM:<12} {SKS:<5} {BEASISWA:^6}    {LAHIR:>11}')
    
print('='*70)