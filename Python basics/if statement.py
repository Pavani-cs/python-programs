a = 10
b = 5
if a > b:
    print("a is greater than b")

number = 1000
if number > 0:
    print("number is positive")

# Multiple statements in if block
    age = 18
    if age >= 18:
        print("You are an adult")
        print("You can vote")
        print("You have full legal rights")

is_logged_in = True
if is_logged_in:
    print("Welcome back!")

# Even number
num = 8
if num % 2 == 0:
    print("Number is even")

# odd number
num = int(input("Enter number:"))
if num % 2 != 0:
    print("The number is odd")

# check number is greater than 10
num = int(input("enter number:"))
if num > 10:
    print("The number is greater than 10")

# Students marks
students_marks = int(input("enter marks: "))
if students_marks >= 40:
    print("passed")

# Divisible by 5
num = 15
if num % 5 == 0:
    print("the number is divisible by 5")

char = input("Enter character:")
if char == "A":
    print("The character is A")

# check two numbers are equal
num1 = int(input("enter num1:"))
num2 = int(input("enter num2:"))
if num1 == num2:
    print("Both are equal")

num = 2
if num > 0 and num % 2 == 0:
    print("The number is positive and even")

age = int(input("Enter age:"))
if age >= 18 and age <= 60:
    print("Age is between 18 and 60")

num = 15
if num % 3 == 0 and num % 5 == 0:
    print("It divisible by both 3 and 5")

username = input("Enter username: ")
if username == "admin":
    print("Welcome admin")

password = input("Enter password:")
if password == "1234":
    print("correct password")

num = int(input("enter num:"))
if num != 0:
    print("The number is not equal to zero")

marks1 = int(input("Enter marks1: "))
marks2 = int(input("Enter marks2: "))
marks3 = int(input("Enter marks3: "))
if marks1 >= 35 and marks2 >= 35 and marks3 >= 35:
    print("Student passed")

num = int(input("Enter num:"))
if num > 0:
    print("Positive")
if num < 0:
    print("Negative")
if num == 0:
    print("Zero")

# Take two numbers and print the greater number
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
if num1 > num2:
    print("First number greater")
if num2 > num1:
    print("Second number greater")

age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")
if age < 18:
    print("Not eligible to vote")

num = (int(input("Enter num:")))
if num % 2 == 0 or num % 3 == 0:
    print("Number is divisible by 2 or 3")

# largest of the three numbers
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))
if a > b and a > c:
    print("a is large")
if b > a and b > c:
    print("b is large")
if c > a and c > b:
    print("c is greater")