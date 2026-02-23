#task1
#Write a Python program to convert degree to radian.
"""
import math
degree=int(input())
radian=math.radians(degree)
print(radian)

""" 


#task2
#Write a Python program to calculate the area of a trapezoid.

""" 
height = int(input())
base1 = int(input())
base2 = int(input())

area = (base1 + base2) / 2 * height

print(area)
""" 


#task3
#Write a Python program to calculate the area of regular polygon.

"""
import math

n = int(input())
a = float(input())

area = (n * a * a) / (4 * math.tan(math.pi / n))

print(area)
"""

#task4
#Write a Python program to calculate the area of a parallelogram.
"""
base = float(input())
height = float(input())

area = base * height

print(area)
"""