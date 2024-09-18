import math

x=input("nhập vào so nguyên: ")
x=int(x)
if x>=0:
    print(x," là số dương")
if x%2==0:
    print(x,"là số chẵn")
else:
    print(x,"là số lẻ")
print(" giải phưng trình bậc 2")
a=float(input("Nhập a: "))
b=float(input("Nhập b: "))
c=float(input("Nhập c: "))
if(a!=0):
    delta = b**2 - 4*a*c
    if(delta <0):
        print("phương trình vô nghiệm")
    elif(delta==0):
        x=-b/(2*a)
        print(" có nghiệm kép x1=x2",x)
    else:
        x1 = (-b-math.sqrt(delta))/(2*a)
        x2 = (-b+math.sqrt(delta))/(2*a)
        print(" có nghiệm kép x1={0} và x2={1}".format(x1,x2))
else:
    print(" không phải phương trình bậc 2: ")

