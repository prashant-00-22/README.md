#Task 1: Check if a Number is Even or Odd

x=int(input("enter a number"))

if(x/2==0):
    print(x," is an even number")
else:
    print(x," is a odd number")


# Task 2: Sum of Integers from 1 to 50 Using a Loop

sum=0
for i in range(1,51):
    sum=sum+i
    print("sum of", i,sum )
