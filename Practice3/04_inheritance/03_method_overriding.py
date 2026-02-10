# Переопределение метода — когда у ребенка метод с тем же именем

class Animal:
    def eat(self):
        print("I can eat")

class Dog(Animal):
    # Этот метод ПЕРЕОПРЕДЕЛЯЕТ метод родителя
    def eat(self):
        print("I like to eat bones")

dog = Dog()
dog.eat()  # Вызывается метод Dog, а не Animal
