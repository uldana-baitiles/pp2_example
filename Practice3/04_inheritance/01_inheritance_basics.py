
# Наследование — это когда один класс (Child) наследует свойства и 
# методы другого (Parent)

# Parent class (родительский класс)
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Child class (дочерний класс)
# Student наследует ВСЁ от Person
class Student(Person):
    pass  # pass используется, если мы ничего не добавляем

# Создаем объект дочернего класса
x = Student("Mike", "Olsen")
x.printname()  # Метод унаследован от Person
