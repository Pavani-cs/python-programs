# Getting  the data type
x = 1
print(type(x))
x = "World"
print(type(x))
x = 1.3
print(type(x))
x = 1j
print(type(x))
x = ["apple", "mango"]
print(type(x))
x = ("nirmal", "armoor")
print(type(x))
x = range(6)
print(type(x))
x = {"name" : "john", "age" : 21}
print(type(x))
x = {"school", "bag" ,"basket"}
print(type(x))
x = frozenset( {"air" , "bug", "aim"})
print(type(x))
x = True
print(type(x))
x = b"Hello"
print(type(x))
x = bytearray(5)
print(type(x))
x = memoryview(bytes(5))
print(type(x))
x = None
print(type(x))

# setting the specific data type
x = int(1)
print(x, type(x))
x = str("World")
print(x)
x = float(1.3)
print(x)
x =complex(1j)
print(x)
x = list(("apple", "mango"))
print(x)
x = tuple(("nirmal", "armoor"))
print(x)
x = range(6, 10)
print(x)
print(list(x))
x = dict(name = "john", age = 21)
print(x)
x = set(("school", "bag" ,"basket"))
print(x)
x = frozenset(("air" , "bug", "aim"))
print(x)
x = bool(5)
print(x)
x = bytes(5)
print(x)
x = bytearray(5)
print(x)
x = memoryview(bytes(5))
print(x)
x = None
print(x)

# Python Numbers
x = 1
y = 2.8
z = 1j
print(x)
print(y)
print(z)

# Int
x = 36656222554887711
y = -3255522
print(x) ; print(type(x))
print(y) ; print(type(y))

# Float
x = 1.0
y = -85.59
z = 86e3
a = 12E4
b = -87.7e100
print(x) ; print(type(x))
print(y) ; print(type(y))
print(z) ; print(type(z))
print(a) ; print(type(a))
print(b) ; print(type(b))

# Complex
x = 3+5j
y = -5j
print(x) ; print(type(x))
print(y) ; print(type(y))

a = 5
print("The type of a", type(a))
b = 40.5
print("The type of b",type(b))
print("d is a float",isinstance(40.5,float))
c = 1+3j
print("The type of c",type(c))
print(" c is a complex numbers", isinstance(1+3j, complex))
d = 2.14j
print(d,"The type of d",type(d))
e = 2.0+2.3j
print(e,"The type of e",type(e))

# Type conversion
x = 1
y = 2.8
z = 1j
a = float(x)           # converting from int to float
b = int(y)             # converting from float to int
c = complex(x)         # converting from int to complex
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

a = 5                 # Implicit type conversioh
b = 5.5
sum = a + b
print(sum, type(sum))

a = 5
b = 4
c = a * b
print(c,type(c))

a = 100              # Explicit type conversion
b = "200"
b = int(b)
result = a + b
print(result, type(result))

a = 10
b = str(a)
print(b, type (b))

