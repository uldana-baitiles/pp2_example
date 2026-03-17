from functools import reduce

nums = [1, 2, 3, 4, 5]

# map → применяет функцию к каждому элементу
print(list(map(lambda x: x * 2, nums)))

# filter → оставляет только подходящие элементы
print(list(filter(lambda x: x % 2 == 0, nums)))

# reduce → объединяет в одно значение
print(reduce(lambda a, b: a + b, nums))