# Example 1
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Example 2
x = "John"
# is the same as
x = 'John'

a = 4
A = "Sally"
#is the not same 

# Example 3
#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Example 4(Multiple Values)
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Example 5
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# Example 6(Global Variables)
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
#(will print :
#  Python is fantastic Python is awesome)

