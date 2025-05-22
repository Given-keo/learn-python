# MEMBUAT MODULE MATEMATIKA

def tambah(*args):
    hasil = 0

    for i in args:
        hasil += i

    return hasil

def kali(*args):
    hasil = 1

    for i in args:
        hasil *= i

    return hasil


def pangkat(angka,pangkat):
    return angka**pangkat
