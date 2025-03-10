# class Student:
#     def __init__(self,name,address):
#         self.stu_name = name
#         self.stu_address = address
#         self.sem = "sem4"
#     def show(self,age):
#         print(f"My name is {self.stu_name} and I am {age} years old")
# stu = Student("Aman","Kol-78")
# print(stu.stu_name)
# print(stu.sem)
# stu1 = Student("Ram","Kol-76")
# print(stu1.stu_address)





# stu = Student()
# stu.name = "Ram"
# stu.address = "Kol-76"
# stu.sem = "sem-4"
# print(stu.address)
# stu1 = Student()
# stu1.name = "Aman"
# stu1.address = "Kol-78"
# stu.sem = "sem-4"
# print(stu1.name)



import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius

    def get_circumference(self):
        return 2 * math.pi * self.radius

radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)
print("Radius of the circle:", circle.get_radius())
print("Circumference of the circle:", circle.get_circumference())
