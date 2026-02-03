# Example 1
x = 5
y = 3

print(x == y)   # False
print(x != y)   # True
print(x > y)    # True
print(x < y)    # False
print(x >= y)   # True
print(x <= y)   # False


# Example 2
x = 5

print(1 < x < 10)           # True
print(1 < x and x < 10)     # True


# Example 3
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x == y)               # True (same values)
print(id(x) == id(z))       # True (same object)
print(id(x) == id(y))       # False (different objects)


# Example 4
text = "Hello World"

print("H" in text)          # True
print("hello" in text)      # False (case-sensitive)
print("z" not in text)      # True


# Example 5
a = "7"
b = 7

print(a == b)               # False (string vs integer)
