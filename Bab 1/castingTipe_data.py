# casting 
# merubah tipe data menjadi tipe data lain
# tipe data = int,str,bool,float

## INTEGER
print('===== INTEGER =====')
data_int = 3
print('data =',data_int,', bertipe =',type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #akan false jika int = 0

print('data =',data_float,', bertipe =',type(data_float))
print('data =',data_str,', bertipe =',type(data_str))
print('data =',data_bool,', bertipe =',type(data_bool))

## FLOAT
print('===== FLOAT =====')
data_float = 6.5
print('data =',data_float,', bertipe =',type(data_float))

data_int = int(data_float) #akan dibulatkan kebawah
data_str = str(data_float)
data_bool = bool(data_float) #akan false jika int = 0

print('data =',data_int,', bertipe =',type(data_int))
print('data =',data_str,', bertipe =',type(data_str))
print('data =',data_bool,', bertipe =',type(data_bool))

## BOOL
print('===== BOOLEAN =====')
data_bool = False
print('data =',data_bool,', bertipe =',type(data_bool))

data_int = int(data_bool) #akan dibulatkan kebawah
data_str = str(data_bool)
data_float = float(data_bool) #akan false jika int = 0

print('data =',data_int,', bertipe =',type(data_int))
print('data =',data_str,', bertipe =',type(data_str))
print('data =',data_float,', bertipe =',type(data_float))

## STRING
print('===== STRING =====')
data_str = '120' #jika str berupa tulisan maka akan error saat casting float dan int
print('data =',data_str,', bertipe =',type(data_str))

data_int = int(data_str) #akan dibulatkan kebawah
data_bool = bool(data_str)
data_float = float(data_str) #akan false jika int = 0

print('data =',data_int,', bertipe =',type(data_int))
print('data =',data_bool,', bertipe =',type(data_bool))
print('data =',data_float,', bertipe =',type(data_float))