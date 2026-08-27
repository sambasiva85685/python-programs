#1
from os import name


class student:
    name="Siva"
    age=23
obj=student()
print(obj.name)
print(obj.age)

#2
class student:
    def __init__(self):
        print("constructor called")
obj=student()

#3
class A:
    name="Siva"
    marks=100
    def __init__(self,a,b):
        self.x=a
        self.y=b
obj=A(10,"hii")
print(obj.x,obj.y)
print(A.name,A.marks)
print(obj.name,obj.marks)

