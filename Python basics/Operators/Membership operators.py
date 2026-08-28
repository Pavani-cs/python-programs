name = "Phone"
print("P" in name)     #in means value is present.
print("p" in name)
print('z' in name)

name = "Python"  
print("P" not in name)   # not in means value is not present
print("Z" not in name)

numbers = [10,20,30,40]
print(10 in numbers)
print(50 in numbers)
print(50 not in numbers, 20 not in numbers)

x = [10]
print(10 in x)
print(10 not in x)

fruits = ["apple","banana"]
print("banana" in fruits)
print("pineapple" not in fruits)

x = [1, 2, 3]
print("1" in x)
print("1" not in x)

x = ["10", "20", "30"]
print(10 in x)
print(10 not in x)
print("10" in x)

subjects = ["C", "Python"]
subject = input("Enter subject:")
print(subject in subjects )
# Membership operator is completed.
# Next operator is bitwise operator.

# Bitwise operators
print(6 & 3)               # &(AND) operator
print(6 | 3)               # |(OR) operator
print(6 ^ 3)               # ^(XOR) operator
print(~3)                  # ~(NOT) operator
print(3 << 2)              # <<(left shift) operator
print(8 >> 2)              # >>(right shift) operator

a = 5; b = 3
print (a & b)

a = 5; b = 3
print(a | b)

a = 5; b = 3
print(a ^ b)

a = 10
print(~a)

a = 5; b = 1
print(a << b)

a = 5; b = 1
print(a >> b)

num = int(input("Enter num:"))
print(~num)

num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))
print(num1 & num2)
print(num1 | num2)
print(num1 ^ num2)
print(num1 << num2)
print(num1 >> num2)

# Operator precedence
print((6 + 3) - (6 + 3))      # parenthesis have the highest precedence
print(100  - 3 ** 3)          # Exponentiation has higher precedence than subtraction        
print(100 + ~3)               # Bitwise NOT has higher precedence than addition
print(+10)
print(-10)

# Unary plus
x = 10
print(+x)
x = -10
print(+x)

# Unary Minus
x = 10
print(-x)
x = -10
print(-x)

# Bitwise Not
x = 5
print(~x)               #~5 = -(5 + 1) = -6

print(100 - 5 * 3)         # suntraction has a lower precedence than multiplication
print(10 +  5 - 3)         # + and - have same precedence
print(10 + 5 * 2)          # addition has a lower precedence than multiplication

print(8 >> 4 - 2)          # bitwise right shift has a lower precedence than subtraction
print(2 + 3 << 1)          # bitwise left shift has a lower precedence than addition

print(2 << 1 & 3)          # << and >> higher precedence than &,^,|
print(2 << 1 ^ 3)
print(2 << 1 | 3)
print(2 >> 1 & 3)
print(2 >> 1 ^ 3)
print(2 >> 1 | 3)
print(6 & 2 + 1)           # bitwise  & has a lower precedence than addition
print(6 ^ 2 + 1)           # bitwise  ^  has a lower precedence than addition  
print(6 | 2 + 1)           # bitwise  | has a lower precedence than addition    

print(not 5 == 5)
print(1 or 2 and 3)
print(4 or 5 + 10 or 8)
print(5 == 4 + 1)
print(5 + 4 - 7 + 3)
print(1 + 2 + 3 == 6)

s = 1 + 2 + 3 + \
    4 + 5 + 6  + \
    7 + 8 + 9
print(s)

s = (1 + 2 + 3 +      # using parentheses
    4 + 5 + 6  +
    7 + 8 + 9)
print(s)

n = ( 1 * 2 * 3 + 7 + 8 + 9)
print(n)

footballer = ['Messi', " NEYMAR", 'SUAREZ']
print(footballer)

x = {1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9}
print(x)

print(4 + 5 * 2 ** 3)
print(10 > 5 and 2 + 3 * 4 > 10)
print((5 + 3) * 2 ** 2 - 4)
print(20 // 3 + 2 ** 3 * 2)
print(10 + 5 * 2 > 15 and 20 - 5 == 15)

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))
e = int(input("Enter e: "))
print(a // b + c ** d * e)

print(int(input()) // int(input()) + int(input()) ** int(input()) * 2)