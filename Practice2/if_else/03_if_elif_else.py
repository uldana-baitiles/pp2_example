# Example 1
number = 0
if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")


# Example 2
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
else:
    print("Grade: F")


# Example 3
temperature = 18
if temperature > 30:
    print("Hot weather")
elif temperature >= 15:
    print("Warm weather")
else:
    print("Cold weather")


# Example 4
word = "Python"
if len(word) < 4:
    print("Short word")
elif len(word) <= 6:
    print("Medium word")
else:
    print("Long word")


# Example 5
is_raining = True
is_cold = False

if is_raining and is_cold:
    print("Wear a jacket and take an umbrella")
elif is_raining:
    print("Take an umbrella")
elif is_cold:
    print("Wear a jacket")
else:
    print("Weather is good")
