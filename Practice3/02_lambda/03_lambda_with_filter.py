# Функция filter() создаёт список элементов,
# для которых функция возвращает True.

#Example 1
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

#output:
# [2, 4, 6, 8, 10]