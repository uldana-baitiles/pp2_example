
# super() используется, чтобы вызвать методы родительского класса

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname):
        # super() вызывает __init__ родителя
        super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()
