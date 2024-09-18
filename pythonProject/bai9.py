# bai1 ifelse và vòng lặp
count=0
for i in range(0,11):
    x=i+count
    count=i
    print(x,end=" ")
# bai2
l1=[4,5,6,7,8,9,3,2,1]
n=int(input(" Nhập số: "))
for i in l1:
    if i==n:
        print("numbet exit")
        break
    else:
        print("number dont exit")

