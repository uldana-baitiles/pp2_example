# Множественное наследование — класс наследует от НЕСКОЛЬКИХ классов

class Father:
    def skill(self):
        print("Driving")

class Mother:
    def hobby(self):
        print("Cooking")

# Ребенок наследует от Father и Mother
class Child(Father, Mother):
    pass

c = Child()
c.skill()  # от Father
c.hobby()  # от Mother
