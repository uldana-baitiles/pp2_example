# Example 1: AND operator
# Both conditions must be True
a = 10
b = 5
print(a > 5 and b < 10)  # True

# Example 2: OR operator
# At least one condition must be True
x = -3
print(x > 0 or x == -3)  # True

# Example 3: NOT operator
# Reverses the boolean value
a = True
print(not a)  # False

# Example 4: Combining comparison and boolean operators
age = 20
id = True
print(age >= 18 and id)  # True

# Example 5: Operator precedence 
# NOT has higher priority than AND
a = False
b = True
print(not a and b)  # True