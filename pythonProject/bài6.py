# vòng for
n=10
for i in range(n):
    print(i)
a=input("nhập vào n: ")
tong =0
for i in range(n+1):
    tong+=i
print(tong)
for i in range(0,10,2):# tăng 2 đơn vi
    print(i)
# vòng lặp đi ngược
for i in range(10,0,-1):
    print(i)
print("----------------------------------")
colors = ["red","green","orange"]
for color in colors:
    print(color)
for i in range(len(colors)):
    print(colors[i])
""" vòng for lồng nhau"""
for i in range(1,11):
    print("2x{0}={1}".format(i,2*i))
print('---------------------------------------')
print("TẠP BẢNG CỬU CHƯƠNG")
for i in range(2,10):
    print("Bảng cửu chương",i)
    for j in range(10) :
        print("{0}x{1}={2}".format(i,j,i*j))