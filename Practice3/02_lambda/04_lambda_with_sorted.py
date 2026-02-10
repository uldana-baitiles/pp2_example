# Функция sorted() может использовать лямбда-функцию 
# как ключ для пользовательской сортировки.

#Example 1
students = [("Emil", 25), ("Tobias", 23), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
 #output:
#  [('Tobias', 23), ('Emil', 25), ('Linus', 28)]


#Example 2
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

#output:
# ['pie', 'apple', 'banana', 'cherry']
