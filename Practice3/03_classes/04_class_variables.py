#Example 1
class Person:
    species = "Human"   # переменная класса

    def __init__(self, name):
        self.name = name  # переменная объекта

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.species)
print(p2.species)
