x = 10
y = x            
print(x is y)            # Checks whether both are the same object

x = 10
y = 20
print(x is not y)        # Checks whether both are different objects

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)            # checks whether values are equal
print(x is y)

x = 5
y = 6
print(x is y)
print(x is not y)
print(x == y)

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1, 2, 3]
y3 = [1, 2, 3]
print(x1 is not y1)
print(x2 is y2)
print(x3 is y3)
print(x3 == y3)
print(x2 == y2)
print(x1 == y1)