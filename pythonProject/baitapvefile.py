# tao file
with open('input file','r') as file:
    content=file.read()
    print(content)
with open('outputfile','w') as file:
    file.write("hello,world/n")
    file.write(" this is a test file")
# kiểm tra file có rỗng hay ko
import os
size=os.stat("outputfile").st_size
if size == 0:
    print("file is empty")
else:
    print("file is not empty")
# dùng try và except
filename="outputfile"
try:
    with open(filename) as f:
        content=f.read()
        print(content)
except FileNotFoundError:
    print(f"dearuser {filename} may be this")
#
x=int(input("enter the number: "))
y=int(input("enter the nuber: "))
try:
    result=x/y
except ZeroDivisionError:
    print("can not")
else:
    print(result)