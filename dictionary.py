#Task 1: Create a Dictionary of Student Marks
my_dict={
    "aryan":25,
    "aarav":30,
    "aditya":35
}

name= input("enter your name")

if name in my_dict.keys():
    print(my_dict[name])
else:
    print("name not found")


#Task 2: Demonstrate List Slicing

list=[1,2,3,4,5,6,7,8,9,10]
l=(list[0:5])
print(l)
y=(l[::-1])
print(y)