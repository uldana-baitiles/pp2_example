names = ["Ali", "Dana", "Aruzhan"]
scores = [90, 85, 88]
nums = [4, 1, 9, 2]

# enumerate → даёт индекс + значение
for i, name in enumerate(names):
    print(i, name)

# zip → соединяет два списка
for name, score in zip(names, scores):
    print(name, score)

# built-in functions
print(len(nums))
print(sum(nums))
print(min(nums))
print(max(nums))
print(sorted(nums))

# type conversion
print(int("5"))
print(float("3.14"))
print(str(100))
print(list("abc"))