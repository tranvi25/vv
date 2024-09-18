from student import Student
sv=[]
while True:
    print(''' vui lòng chọn chức năng
    0.thoát
    1.Xem danh sách sinh viên
    2.Thêm sinh viên
    3.xóa sinh viên
    4.sửa sinh viên''')
    choice=input('bạn chọn chức năng nào')
    if choice.isdigit():
        choice=int(choice)
        if choice== 0:
            break
        elif choice==1:
            if len(sv)==0:
                print('hiện chưa có sinh viê nào: ')
            else:
                for i in sv:
                    i.show()
        elif choice ==2:
            id=input('Nhập id sinh viên: ')
            name=input('Nhập tên sinh viên')
            sv.append(Student(id,name))
        elif choice ==3:
            id=input('Nhập id sinh viên muốn xóa')
            for i in sv:
                if i.id==id:
                    sv.remove(i)
        elif choice==4:
            id=input('Nhâ id sinh viên muốn sữa: ')
            for i in sv:
                if i.id==id:
                    i.set_name(input('Nhập tên muốn thay đổi'))

    else:
        print('vui lòng chọn lại')