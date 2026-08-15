x = 10                        # Returns true if both statements are true
print(x > 5 and x < 15)
x = 5
print(x < 0 and x > 10 )

x = 10                        # Returns true if one of the statements is true
print(x > 5 or x < 15)
x = 5
print(x < 5 or x > 10)

x = 10                        # reverse the result, returns false if the result is true
print(not (x > 5 and x < 15))
x = 5
print(not(x < 5 and x > 10))

# Examples
x =int(input("Enter num1:"))
y =int(input("Enter num2:"))
print(x > 0 and y > 0)

age = int(input("enter age:"))
print(age >= 18 and age <= 60)

a = int(input("enter a:"))
b = int(input("enter b:"))
print(a > 100 or b > 100)

username = input("Enter username:")
password = input("Enter password:")
print( username == "Parvathi" and password == "1234" )

num = int(input("Enter num:"))
print(not num == 0)

num = int(input("Enter num:"))   # Check whether a number is positive and even
print(x > 0 and x % 2 == 0 )

num = int(input("Enter num:"))   # Check whether a number is negative or greater than 100
print(num < 0 or num > 100)

number = int(input("Enter number:"))    # check whether number is between 1 and 100 but not equal to 50
print(number >= 1 and number <= 100 and not number == 50 )