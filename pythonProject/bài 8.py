# bài tập 2
#Exercise 1: Accept numbers from a user
from typing import List

name=str(input("nhập tên: "))
print(name)
#Exercise 2: Display three string “Name”, “Is”, “James” as “Name ** Is ** James”
print("name","is","vi",sep="....")
#Exercise 3: Convert Decimal number to octal using print() output formatting
number=15
print(oct(number)[-2:])
#Exercise 4: Display float number with 2 decimal places using print()
num=56.87547
y=float(round(num,2))# round lm tròn số lên 2 đơn vi

print(y)
# in ra các thừa số mà ng dùng đã cho
n=int(input(" nhập thừa số: "))
for i in range(1,n+1):
    if(n%i==0):
        print(i,end=" ")
#end nối các dòng và số lại
#Exercise 6: Accept a list of 5 float numbers as an input from the user
l1=[]
while len(l1)<5:
    n=int(input("nhập các số"))
    l1.append(n)
    print(l1)
l2=[]
for _ in range(len(l2),5):
    f=int(input("nhập số: "))
    l2.append(f)
    print(l2)
