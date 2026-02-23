#task1
#Create a generator that generates the squares of numbers up to some number N
"""
def sq(n):
    for i in range (1,n+1):
        yield i*i
n=int(input())

for i in sq(n):
    print(i,end=" ")
"""


#task2
#Write a program using generator to print the even numbers 
# between 0 and n in comma separated form where n is input from console.
"""
def even(n):
    for i in range(0,n+1):
        if i%2==0:
            yield i
n=int(input())
print(*even(n),sep=",")
"""


#task3
#Define a function with a generator which can iterate the numbers, 
# which are divisible by 3 and 4, between a given range 0 and n.
"""
def dev(n):
    for i in range(0,n+1):
        if i%12==0:
            yield i
n=int(input())
for i in dev(n):
    print(i,end=" ")
"""

#task4
#Implement a generator called squares to yield the square of all numbers from (a) to (b). 
# Test it with a "for" loop and print each of the yielded values.
"""
def squares(a,b):
    for i in range(a,b+1):
        yield i * i
a,b=map(int,input().split())
for i in squares(a,b):
    print(i,end=" ")
"""
