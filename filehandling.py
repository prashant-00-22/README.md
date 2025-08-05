#Task 1: Read a File and Handle Errors

f=open("sample.txt","r")
content=f.read()
print(content)
f.close()

try:
    open("sample.txt")
except FileNotFoundError:
    print("file not found ")


#Task 2: Write and Append Data to a File

f=open("output.txt","w")
f.write("hello world")
f.close()

f=open("output.txt","a")
f.write("hello world")
f.close()
f=open("output.txt","a+")
content=f.read()
print(content)
f.close()


