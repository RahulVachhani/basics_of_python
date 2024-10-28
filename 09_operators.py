
# Operators

# 1) Arithemetic Operators ( +, -, /, *, //, **)
# 2) Assignment Operators  (=, +=, -=)
# 3) Logical Operators (and, or, not)
# 4) Comparision Operators (==, <, >, <=, >=, !=)
# 5) Bitwise Operators (&, |, ~, ^, >>, <<)



# 1) Arithemetic Operators ( +, -, /, *, //, **)

a = 10
b = 20

print(a + b)
print(b - a)
print(a * b)
print(b / a)
print(a ** 2)     # Its like squre of a
print(b // a)     # its return Floar value of divide



# 2) Assignment Operators  (=, +=, -=)

a = 100    

a += 200
print(a)

a -= 100
print(a)



# 3) Logical Operators (and, or, not)

a = 10 
b = 20

if a == 10 and b == 20:
    print("Right If Both Condition Are True")


if a == 10 or b == 30:
    print("Right If one of them Condition is True")

if not(False):
    print("Not operator")



# 4) Comparision Operators (==, <, >, <=, >=, !=)

a = 100
b = 200

print(a == b)

print(a >= b)

print(a <= b)

print(a != b)

 
# 5) Bitwise Operators (&, |, ~, ^, <<, >>)     <-- its work on bits

a = 10
b = 20

binary_and = a & b
print(binary_and)

binaru_or = a | b      
print(binaru_or)

print(~a)      # its like -(a+1)   , compliment

print(a ^ b)

print(a<<1)

print(a>>1)