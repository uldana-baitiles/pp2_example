#Example 1 *args {tuple}
# if you do not know how many arguments will be passed into your function,
#  add a * before the parameter name.

def my_function(*args):
    print("Type:", type(args))
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")
# output:
# Type: <class 'tuple'>
# First argument: Emil
# Second argument: Tobias
# All arguments: ('Emil', 'Tobias', 'Linus')

#Example 2
def my_function(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))


#Example 3 **kwargs {dict}
# If you do not know how many keyword arguments will be passed into your function, 
# add two asterisks ** before the parameter name.
def my_function(**myvar):
    print("Type:", type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("All data:", myvar)

my_function(name="Tobias", age=30, city="Bergen")
 #output:
# Type: <class 'dict'>
# Name: Tobias
# Age: 30
# All data: {'name': 'Tobias', 'age': 30, 'city': 'Bergen'}
  


#Example 4
# The order must be:
# regular parameters
# *args
# **kwargs

def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

#output:
# Title: User Info
# Positional arguments: ('Emil', 'Tobias')
# Keyword arguments: {'age': 25, 'city': 'Oslo'}

#Example 5
def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)

#Example 6 
def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")