# Calculate Factorial Using a Function


def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)
n = int(input("enter number"))
a=fact(n)
print(a)

#Using the Math Module for Calculations

import math

n=int(input("enter a number"))
a=math.sqrt(n)
print(a)
a=math.log(n)
print(a)
a=math.sin(n)
print(a)