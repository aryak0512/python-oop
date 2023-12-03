# number systems conversion

'''
binary : Ob
hexadecimal : 0x
octal : 0o


a, b = 8, 9
print(a != b)
print("25 in binary ", bin(25))
print("25 in hexadecimal ", hex(25))
print("25 in reverse hexadecimal ", 0x19)
'''

'''
Bitwise operators 
1. Complement
2. AND
3. OR
4. XOR
5. LEFT SHIFT
6. RIGHT SHIFT
'''

'''
COMPLEMENT => 2's complement of a number

5       : 0000 0101
1s comp : 1111 1010 -- LHS

-6 
6       : 0000 1010
1s comp : 1111 0101
2s comp : 1111 0110
'''

print(~5)  # 1111 1010
print("======================")
''''
Bitwise AND

7  : 0000 0111
12 : 0000 1100
a  : 0000 0100
'''
print(7 & 12)
print("======================")
''''
Bitwise OR

7  : 0000 0111
12 : 0000 1100
OR : 0000 1111
'''
print(7 | 12)
print(0b00001111)
print("======================")
''''
EX OR
odd number of 1s give 1 else 0
============
A   B   Y
============
0   0   0
0   1   1
1   0   1
1   1   1
============
2       : 0000 0010
3       : 0000 0011
2 ^ 3   : 0000 0001

'''
print("Expected : ", 0b00000001)
print("ACTUAL : ", 2 ^ 3)
print("======================")

''''
left shift operator

2       : 0000 0010
3       : 0000 0011
2 << 2   : 0000 0001

1st : 0000 0100
2nd : 0000 1000
'''
print("Expected : ", 0b00001000)
print("ACTUAL : ", 2 << 2)
print("======================")
