#Example 1
# Функция map() применяет функцию к каждому 
# элементу в итерируемом объекте.

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

#output:
# [2, 4, 6, 8, 10]
