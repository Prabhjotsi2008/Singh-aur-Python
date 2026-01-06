x = 2
y = 3
z = 4

# ARITHMETIC OPERATORS

print(x + y * z) # 14 # low readability
print((x + y) * z) # 20 # High readability

# it is a bad practice to add different datatypes
print(40 + 2.23) # 42.43 
# print('Prabhjot' + 3) # TypeError


# explicit conversion of values
print(40 + int(2.23)) # 42
print(float(40)) # 40.0


print('chai' + 'code') # concatenate using + operator


print((x+1,y%2,z**3)) # tuple (3,1,64) # (add,remainder,power)

result = 1/3.0
print(result)

# SELF-STUDY
repr('chai')
str('chai')
print('chai')


# COMPARISON OPERATORS
print(1<2) # True 
print(int(1<2)) # 1

print(y>=3) #True

print(x < y < z) # True # not a good practice # still works # short-hand
print(x<y and y<z) # True # same as above

print(1 == 2<3) # False


# COMPLEX-NUMBERS
n1 = 2 + 1j
print(n1*3) # 6 + 3j

# OCTAL-NUMBERS
octal = 0o20
print(octal) # 2*8 + 0*1 = 16 + 0 = 16 

# HEXAL-NUMBERS
hexal = 0xff # same as 0xFF
print(hexal) # 15*16 + 15*1 = 240 + 15 = 255

# BINARY-NUMBERS
binary = 0b1010
print(binary) # 1*8 + 0*4 + 1*2 + 0*1 = 8 + 0 + 2 + 0 = 10


# CONVERSIONS # oct() # hex() # bin()
print(oct(64)) # 0o100 # DEC -> OCT
print(hex(64)) # 0x40 # DEC -> HEX
print(bin(64)) # 0b1000000 # DEC -> BINARY


# ANOTHER METHOD FOR CONVERSION # OTHER_BASE --> DECIMAL
# int("value in string", base_of_the_value_in_string)
print(int('64', base=8)) # 52 # OCT --> DEC
print(int('1AF4E', base=16)) # 110414 # HEX --> DEC
print(int('011010', base=2)) # 26 # BIN --> DEC


# BIT-WISE OPERATIONS
x = 1 # 0b1
print(x << 2) # left-shift # 0b1 << 2 --> 0b100 --> 1*4 + 0*2 + 0*0 = 4
print(x | 2) # bitwise-or
print(x & 2) # bitwise-and

# CONFUSION :
print(0.1 + 0.1 + 0.1 - 0.3) # it should be 0 but isn't
# SOLUTION :
# >>> from decimal import Decimal
# >>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1')            
# Decimal('0.3')
# >>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
# Decimal('0.0')


# SETS # UNIQUE VALUES ARE STORED
my_set = {1,2,3,4,1}
print('my_set = ',my_set) # {1,2,3,4}
setone = {1,2,3,4}
print(setone)

# INTERSECTION OF SETS # COMMON VALUES
print(setone & {1,3,5}) # {1,3}

# UNION OF SETS # COMBINED UNIQUE VALUES
print(setone | {1,3,5}) # {1,2,3,4,5}

# DIFF. OF SETS # REMOVE COMMON VALUE FROM FIRST SET
print(setone - {1,3,5}) # {1,2,3,4} - {1,3,5} = {2,4}
print({1,3,5} - setone) # {1,3,5} - {1,2,3,4}= {5}
print(setone - {1,2,3,4}) # set() # not {} # as {} is empty dict, not empty set
# lets check
print(type({})) # dict


# BOOLEAN
print(type(True)) # bool

print(True == 1) # True
print(True is 1) # False

print(True + 4) # 5