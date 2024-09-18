class Student:
    count=0
    # hàm khởi tạo
    def __init__(self, id, name):
        self.id = id
        self.name = name
        Student.count+=1
    def set_id(self,id):
        self.id=id
    def get_id(self):
        return self.id
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name

    def show(self):
        print(f'ID: {self.id}')
        print(f'Name: {self.name}')

# Tạo một đối tượng sinh viên và thêm thông tin
s = Student('001','python')
s2= Student('002','vi')
s3= Student('003','nam')
print(Student.count)
s.show()

