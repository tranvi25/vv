# exercise 1 For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the
# digits.
import math
n = input("enter the number: ")
y=n[::-1]
k=" ".join(y)
print(k)
# exercise 3: Write a program that will give you the sum of 3 digits
x=int(input(" nhập số của 3 chữ số: "))
a=x%10
num=x//10
b=num%10
c=num//10
print(a)
print(b)
print(c)
"""Excercise 4: Write a program that will reverse a four digit number.Also it checks whether the reverse"""
x=int(input(" nhập số có 4 chữ số: "))
a=x%10
num=x//10
b=num%10
num1=num//10
c=num1%10
d=num1//10
print(a+b+c+d)
red=a*1000+b*100+c*10+d*1
print(red)
if x!=red:
    print('true')
else:
    print('false')
"""Excercise 5: Write a program to find the euclidean distance between two coordinates."""
x1=float(input("x1: "))
y1=float(input("y1: "))
x2=float(input("x2: "))
y2=float(input("y2: "))
x=[x1,y1]
y=[x2,y2]
print("eucledian",round(math.dist(x,y)))
#Excercise 6: Write a program that will tell whether the given number is divisible by 3 & 6
m=int(input("nhập số : "))
if m%3==0 and m%6==0:
    print("số chia ht được cho 3 và 6")
else:
    print("soo ko chia ht cho 3 và 6")
#Excercise 7: Write a program that will take three digits from the user and add the square of each
l=int(input(" Nhập số có 3 chữ số: "))
a1=l%10
num2=l//10
b=num2%10
c=num2//10
rev=a1**2+b**2+c++2
print(rev)
if rev != x:
    print('true')
else:
    print('false')
o=int(input(" nhập số có 4 chữ số: "))
a=o%10
num=o//10
b=num%10
num1=num//10
c=num1%10
d=num//10
red=a*1000+b*100+c*10+d
print(red)
if red != x:
    print("true")
else:
    print("false")


