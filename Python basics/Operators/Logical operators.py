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
