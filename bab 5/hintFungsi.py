# penggunaan type hint dalam fungsi
def kuadrat(angka:int) ->int:
    return angka ** 2

hasil = kuadrat(3)
print('hasil 3 pangkat 2 =',hasil)

def identitas(nama:str)->str:
    print(nama)

identitas('given')