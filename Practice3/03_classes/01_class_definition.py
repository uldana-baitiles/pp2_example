# class ClassName:
    # class definition

    
#Example 1
class Bike: #Bike- the name of the class
    name = ""
    gear = 0
 # name/gear- variables inside the class with default values ”” and 0,

#Note: The variables inside a class are called attributes.
 

 #Example 2
 # create class
class Bike:
    name = ""
    gear = 0
# create objects of class
bike1 = Bike()

#Example 3
class MyClass:
    x = 5
print(MyClass) 
p1 = MyClass()
print(p1.x)

#You can delete objects by using the del keyword:
del p1
print(p1)

#Multiple Objects You can create multiple objects from the same class:
class MyClass:
  x = 5

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

#Example 4
# class cannot be empty,but if you want a class with no content,put pass 

class Person:
  pass