# Example 1
score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")


# Example 2
 
x = 7
y = 7
print("Equal") if x == y else print("Not equal")


# Example 3
 
number = -3
print("Positive") if number > 0 else print("Not positive")


# Example 4
 
word = "Python"
print("Long word") if len(word) > 5 else print("Short word")


# Example 5

temperature = 25
is_sunny = True

if temperature > 20 and is_sunny:
  print("Perfect beach weather!")