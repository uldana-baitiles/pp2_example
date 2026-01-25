# Example 1
print("Hello")
print('Hello')


# Example 2
for x in "banana":
  print(x) 


# Example 3
a = "Hello, World!"
print(len(a))


# Example 4
txt = "The best things in life are free!"
print("free" in txt)


# Example 5
b = "Hello, World!"
print(b[2:5])

# Example 6
a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

a = "Hello, World!"
print(a.replace("H", "J"))


# Example 7 Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

# Example 8 F-Strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt) #The price is 59.00 dollar

txt = f"The price is {20 * 59} dollars"
print(txt) #The price is 1180 dollars
# Example 9
txt = "книга по названию \"Vikings\" ."
