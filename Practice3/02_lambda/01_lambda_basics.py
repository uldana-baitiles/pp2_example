# can take any number of arguments, but can only have one expression.

# Syntax
# lambda arguments : expression

#Example 1
x = lambda a, b : a * b
print(x(5, 6)) #30

#Example 2
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11)) #33

#Example 3
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11)) #22 33 
