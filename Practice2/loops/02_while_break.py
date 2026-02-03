# Example 1: Break when number is 3
i = 1
while True:
    if i == 3:
        break
    print(i)
    i += 1


# Example 2:  
while True:
    x = input("Enter q to quit: ")
    if x == "q":
        break
    print("You typed:", x)


# Example 3: Find first even number
numbers = [1, 3, 5, 8, 9]
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        print("First even:", numbers[i])
        break
    i += 1


# Example 4:  
while True:
    password = input("Password: ")
    if password == "1234":
        print("correctly")
        break


# Example 5:  
count = 0
while True:
    print("perfect")
    count += 1
    if count == 5:
        break
