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

# if else statement
a = 33; b = 33
if a > b:
    print("a is greater than b")
else:
    print("both are equal")

number = 7
if number % 2 == 0:
    print("even")
else:
    print("odd")

username = "Pavani"
if len(username) > 0:
    print(f"welcome, {username}")
else:
    print("Error: Username cannot be empty")

# number is positive or negative
num = int(input("Enter num:"))
if num >= 0 :
    print("positive")
else:
    print("Negative")

# number is even or odd
number = int(input("enter number: "))
if number % 2 == 0:
    print("even")
else:
    print("odd")

# greater of two numbers
a = int(input("enter a:"))
b = int(input("enter b:"))
if a > b:
    print("a is greater")
else:
    print("b is greater")

# leap year
year = int(input("Enter year:"))
if year % 4 == 0:
    print("Leap year")
else:
    print("Not leap year")

# ATM withdrawal
balance = int(input("Enter balance:"))
amount = int(input("Enter amount:"))
if amount <= balance:
    print("withdrawal successful")
else:
    print("Insufficient balance")
 
# Movie ticket
age = int(input("Enter age:"))
if age >= 18:
    print("Adult ticket")
else:
    print("Child ticket")

# online shopping
shopping_amount = int(input("Enter Shopping amount : "))
if shopping_amount >= 1000:
    print("Free Delivery")
else:
    print("Delivery charge ₹50")

# Bus seat
seat = input("enter seat:")
if seat == "yes":
    print("Seat available")
else:
    print("Bus is full")

# Password Strength
length = int(input("Enter length:"))
if length >= 8:
    print("Strong password")
else:
    print("Weak password")

password = input("Enter password:")
if len(password) >= 8:
    print("Strong password")
else:
    print("Weak password")

# Bank Loan
age = int(input("Enter Age:"))
salary = int(input("Enter salary:"))
if age >= 21 and salary >= 25000:
    print("Loan eligible")
else:
    print("Loan not eligible")

# Elif Statement
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("both are equal")

score = 70
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")

day = int(input("Enter day: "))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
else:
    print("Weekends")

temperature = 2
if temperature > 30:
    print("It's hot outside")
elif temperature > 20:
    print("It's warm outside")
else:
    print("It's cold outside")

marks = int(input("Enter marks:"))
if marks > 85 and marks <= 100:
    print("excellent")
elif marks > 50 and marks <= 80:
    print("Good")
else:
    print("Study hard")

# ATM Withdrawal
balance = int(input("Enter Balance: "))
amount = int(input("Enter Amount: "))
if amount > balance:
    print("Insufficient balance")
elif amount == balance:
    print("Account balance will become zero")
else:
    print("Withdrawal successful")

# Electricity Bill
Units  = int(input("Enter Units : "))
if Units > 300:
    print("High usage")
elif Units >= 100 and Units <= 300:
    print("Medium usage")
else:
    print("Low usage")

# Movie ticket
age = int(input("Enter Age : "))
StudentID = input("Do you have a studentID?")
if age < 18:
    print("Child ticket")
elif age >= 18 and StudentID  == "Yes":
    print("Student Discount")
else:
    print("Regular ticket")

# Simple calculator
num1 = float(input("Enter num1 :"))
num2 = float(input("Enter num2 :"))
operator = input("Enter operator (+,-,*,/):")
if operator == "+":
    print("Result :",num1 + num2)
elif operator == "-":
    print("Result :", num1 - num2)
elif operator == "*":
    print("Result :", num1 * num2)
elif operator == "/":
    print("Result :", num1 / num2)
elif operator == "/" and num2 == 0:
    print(" cannot divisible by zero")
else:
    print("Invalid operator")
    









