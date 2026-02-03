# Example 1: Skip number 3
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)


# Example 2: Print only positive numbers
numbers = [2, -1, 4, -3, 6]
i = 0
while i < len(numbers):
    if numbers[i] < 0:
        i += 1
        continue
    print(numbers[i])
    i += 1


# Example 3: Skip zero
nums = [1, 0, 2, 0, 3]
i = 0
while i < len(nums):
    if nums[i] == 0:
        i += 1
        continue
    print(nums[i])
    i += 1


# Example 4: Skip short words
words = ["hi", "hello", "ok", "python"]
i = 0
while i < len(words):
    if len(words[i]) < 3:
        i += 1
        continue
    print(words[i])
    i += 1


# Example 5: Skip even numbers
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    print(n)
