print('meo','cho','cun',sep='ma')#sep để ngăn cách
# end kết thúc
#file tên tập tin
#flush đẩy dữ liệu lên
a =5
b=6
c = a+b
print(c)
a =input("nhập dữ liệu vào a: ")
a =int(a)+2
print(a);
print('rrrr')
#ffffffff ghi chú trên 1 dòng
""" để ghi chú trên nhiều dòng """
print('xin ','chào',end =':')
print('vĩ')
# format truyền dữ liệu vào
print('ten ={0},ho ={1}'.format('vi','tran'))
c=input('nhap vao c')
print('c={0}'.format(c))
# xử lý ngoại lệ đâù vào
try:
 so1 = int(input('nhập vào a: '))
 so2 = int(input('nhập vào b: '))
except:
    print("định dng ko hợp leej")
# hệ thập phân xuất ra bát phân
sothapphan = int(input())
print("số thaapj phân %d trong hệ bt phân là %o" %(sothapphan,sothapphan))
giatri= input()
try:
    sothapphan = int(giatri)
    print("so thap phan %d sang he bat phan %o" %(sothapphan,sothapphan))
except:
    print("định dạng đầu vào ko hợp lệ")



