#Example 1
def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)


#Example 2
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])


#Example 3 Positional-Only Arguments

# With , /, you will get an error if you try to use keyword arguments

def my_function(name, /):
  print("Hello", name)

my_function("Emil")


#Example 4
# With *,, you will get an error if you try to use positional arguments:

def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")


#Example 5
# Arguments before / are positional-only, and arguments after * are keyword-only:


def my_function(a, b, /, *, c, d):
  return a + b + c + d
result = my_function(5, 10, c = 15, d = 20)
print(result)