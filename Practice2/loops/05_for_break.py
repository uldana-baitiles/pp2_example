# Example 1:  
for i in range(1, 6):
    if i == 3:
        break
    print(i)


# Example 2: Stop when word found
words = ["cat", "dog", "stop", "bird"]
for w in words:
    if w == "stop":
        break
    print(w)


# Example 3: Password check
passwords = ["123", "admin", "qwerty"]
for p in passwords:
    if p == "admin":
        print("Correct password")
        break


# Example 4: First positive number
nums = [-3, -2, 4, 6]
for n in nums:
    if n > 0:
        print("First positive:", n)
        break


# Example 5: Exit menu
for option in ["start", "help", "exit"]:
    if option == "exit":
        print("Exit program")
        break
