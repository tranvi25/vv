colors = ["red","green","orange"]
print(colors)
studentList = ["an","binh","ngân","vy"]
print(studentList[2])
print(studentList[0:2])
# dùng append để thêm vào
studentList.append("vĩ")
print(studentList)
# dùng insert để chèn vào
studentList.insert(2,"hiền")
print(studentList)
# len độ dài của mảng
print(len(studentList))
# đếm số lượng phần tử
print(studentList.count("vĩ"))
# remove xóa phần tử khỏi list
studentList.remove("ngân")
print(studentList)
#pop xóa phần tử bằng vị trí
studentList.pop(0)
print(studentList)
#sort sắp xếp list
studentList.sort()
print(studentList)
numbers = [7,5,1,9,0,5,7]
numbers.sort()
print(numbers)
#reverse sắp xếp ngược
studentList.reverse()
print(studentList)
