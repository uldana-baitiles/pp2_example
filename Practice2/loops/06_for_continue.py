# Example 1:  
for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# Example 2: 
numbers = [2, -1, 3, -4, 5]
for n in numbers:
    if n < 0:
        continue
    print(n)


# Example 3:  
words = ["hi", "python", "ok", "code"]
for w in words:
    if len(w) < 3:
        continue
    print(w)


# Example 4:  
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)


# Example 5:  
values = [1, 0, 2, 0, 3]
for v in values:
    if v == 0:
        continue
    print(v)