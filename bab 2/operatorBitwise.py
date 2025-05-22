# operator bitwise
# operasi biner dan binary
print('OPERATOR BITWISE')

a = 9
b = 5

# bitwise OR(|)
c = a | b
print('========== OR(|)')
print('nilai a =',a,', binary =',format(a,'08b'))
print('nilai b =',b,', binary =',format(b,'08b'))
print('-------------------------------------- (|)')
print('nilai c =',c,', binary =',format(c,'08b'))

# bitwise AND(&)
c = a & b
print('\n========== AND(&)')
print('nilai a =',a,', binary =',format(a,'08b'))
print('nilai b =',b,', binary =',format(b,'08b'))
print('-------------------------------------- (&)')
print('nilai c =',c,', binary =',format(c,'08b'))

# bitwise XOR(^)
c = a ^ b
print('\n========== XOR(^)')
print('nilai a =',a,', binary =',format(a,'08b'))
print('nilai b =',b,', binary =',format(b,'08b'))
print('-------------------------------------- (^)')
print('nilai c =',c,', binary =',format(c,'08b'))

# bitwise NOT(~)
c = ~a
print('\n========== NOT(~)')
print('nilai a =',a,', binary =',format(a,'08b'))
print('-------------------------------------- (~)')
print('nilai c =',c,', binary =',format(c,'08b'))
print('-------------------------------------- (~)')
c = 0b00001001
a = 0b11111111
print('nilai c =',c,', binary =',format(c,'08b'))
print('nilai  xornya =',c^a,', binary =',format(c^a,'08b'))

# shifting (>>)
# menggeser ke arah kanan 

x = 5
y = x >> 1
print('\n========== SHIFTING RIGHT(>>)')
print('nilai x =',x,', binary =',format(x,'08b'))
print('-------------------------------------- (>>)')
print('nilai y =',y,', binary =',format(y,'08b'))

# menggeser ke arah kiri

x = 5
y = x << 5
print('\n========== SHIFTING LEFT(<<)')
print('nilai x =',x,', binary =',format(x,'08b'))
print('-------------------------------------- (<<)')
print('nilai y =',y,', binary =',format(y,'08b'))