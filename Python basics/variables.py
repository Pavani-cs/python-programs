# A variable is a name used to store a value
name = "python"
age = 20
print(name)
print(age)
print(name, age)
print(age, name)

a = 10; b = 90; print(a, b)

NAME = "P"
print(NAME)

_Num = 10; print(_Num)

x = 5
x = "hello"
print(x)

#variables are case sensitive
a = 7
A = "key"
print(a)
print(A)

a1 = 80
a2 = 40
print(a1,a2)

roll = 1; name = "Ashwitha"
print("Roll No:", roll)
print("Name:", name)
print("Roll No:", roll ,"Name:", name)

year = 2026
print("Welcome to the year", year)

Apples = 10
print("I have",Apples,"apples.")

# Many values to multiple variables
x, y, z = "orange", "apple", "cherry"
print(x)
print(y)
print(z)

lang1, lang2, lang3 = "Python", "C", "Java"
print(lang1, lang2, lang3)
print(lang1 + " " + lang2 + " " + lang3)    # also use the + operator to print multiple variables

x = "Pen "
y = "Pencil "
z = "Book"
print(x + y + z)

#one value to multiple variables
x = y = z = "Laptop"
print(x)
print(y)
print(z)

# local variables
def show_name():
    name = "Post"
    print(name)
show_name()

def add():
    a = 10
    b = 5
    c = a + b
    print("The sum is:", c)
add()

def value():
    num = 50
    print(num)
value()
num = 100
print(num)

def area_of_the_rectangle():
    length = 8
    width = 5
    print("Area of rectangle:", length * width)
area_of_the_rectangle()

def language():
    first = 'Python'
    second = 'Programming'
    print(first + " " + second)
    print(first, second)
language()

# Global variables
x = 200
def number():
    print("x:", x)
number()

x = "awesome"
def myfun():
    print("Python is", x)
    print("Python is " + x)
myfun()

x = "awesome"
def myfun():
    x = "fantastic"
    print(x)
myfun()
print(x)

def myfun():                      # Global keyword
    global x
    x = "python"
myfun()
print("Programming language:"+ " "+ x)

x = "cat"
def myfun():
    global x
    x = "fan"
myfun()
print(x)

x = 101
def mainFunction():
    global x
    print(x)
    x = "Welcome to Hyderabad"
    print(x)
mainFunction()
print(x)

def mainfunction():
    global num
    num = 100
    print(num)
mainfunction()
print(num)

# swapping two variables without using a third variable
a = 1
b = 2
a,b=b,a
print("a =", a)
print("b =", b)

name1 = "Bat"; name2 = "Kite"
temp = name1
name1 = name2
name2 = temp
print(name1 , name2)

# Take an integer input from the user
a = int(input("enter a: "))
print(a)

# Take a string (text) input from the user
a = input("Enter a: ")
print(a)

num = input("Enter number:")
print(num)
name1 = input("Enter name:")
print(name1)