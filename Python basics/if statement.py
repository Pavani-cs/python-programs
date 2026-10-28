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

# Leap year
year = int(input("Enter Leap Year : "))
if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a Leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")

# Triangle Type
a = int(input("Enter side 1 :"))
b = int(input("Enter side 2:"))
c = int(input("Enter side 3 :"))
if a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle")
elif a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")

#  Month Days
month = int(input("Enter Month:"))
if month == 4 or month == 6 or month == 9 or month == 11:
    print(" 30 days")
elif month == 2:
    print("28 or 29 days")
elif month >= 1 and month <= 12:
    print("31 days")
else:
    print("Invalid month")

# Character Check
ch = input("Enter Character:")
if ch >= 'A' and ch <= 'Z':
    print("Upper case")
elif ch >= 'a' and ch <= 'z':
    print("Lower case")
elif ch >= '0' and ch <= '9':
    print("Digits")
else:
    print("Special character")

# Vowel or Consonent
ch = input("Enter a single alphabet:")
if ch in "aeiouAEIOU":
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
else:
    print("Invalid inputs")
    
#  Python Shorthand if
# one line if statement
name1 = "Dog"
name2 = "Dog"
if name1 == name2: print("Both equal")

a = 2
b = 330
print("A") if a > b else print("B")

a = 10
b = 20
bigger = a if a > b else b 
print("Bigger is",bigger)

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)

age = 12
print("The ticket price is 100") if age < 13 else print("The ticket price is 200")

age = 12
price = 100 if age > 13 else 200
print(price)

# Delivary charges
order_amount= 650
charge = 0 if order_amount >= 500 else 50
print(charge)

# water tank
water_level = 90
print("Tanl almost Full") if water_level >= 80 else print("Tank has Space")

#internet data
data_used = 1.5
data_limit = 1.0
print("data limit exceeded") if data_used > data_limit  else print("Data available")

#electricity Bill
units = 180
rate = 5 if units > 100 else 3
print(rate)

#Number check
number = int(input("Enter Number:"))
print("Divisible") if number % 5 == 0 else print("Not divisible") 

number = int(input("Enter Number:"))
result = "Divisible" if number % 5 == 0 else "Not dvisible"
print(result)

# mobile Battery
Battery =  int(input("Enter battery percentage:"))
print("Low battery") if Battery < 20 else print("Battery ok")

#file name
file_name = input("Enter file name:")
print("python file") if file_name.endswith(".py") else print("Different file type")

#password 
password = input("Enter password:")
print("valid format") if "@" in password else print("Add @ to password")

# python Logical operators
# combining multiple operators
age = 25
is_student = False
has_discount_code = True
if (age < 18 or age > 65) and not is_student or has_discount_code: print("Discount applies!")

ticket = True
id_card = False
print("Entry Allowed" if ticket and id_card else "Entry Denied")

#Library Access
banned = False
print("Access Granted") if not banned else print("Access Denied")

#Food Delivery
restaurant_open = True
online_payment = False
cash_payment = True
print("Place order") if restaurant_open and (online_payment or cash_payment) else print("Cannot order")

#Gaming
has_weapon = True
out_of_health = False
print("Continue Game" if has_weapon and not out_of_health else "Game over")

#weather Alert
rain_expected = False
wind_speed = 65
print("Weather Alert") if rain_expected or wind_speed >= 50 else print('Normal weather')

#smart parking
slot = False
vehicle = True
emergency = True
print("Parking Allowed") if slot and not vehicle or emergency else print("Parking denied")

#Airport security
boarding = True
passport = False
special_clearance = False
print("Proceed") if (boarding and passport) or special_clearance else print("Stop")

# Python Nested if
x = 400
if x > 250:
    print("Above 250,")
    if x > 500:
        print("and also above 500")
    else:
        print("but not above 500.")

# licence
age = 21
has_license = True
if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("you need a license")
else:
    print("you are too young to drive")

















