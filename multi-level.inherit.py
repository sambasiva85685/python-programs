#1
# class A:
#     def __init__(self,name):
#         self.name=name
#     def m1(self):
#         print("Class A")
# class B(A):
#     def __init__(self,marks,name):
#         self.marks=marks
#         super().__init__(name)
#     def m2(self):
#         print("class B")
# class C(B):
#     def __init__(self,marks,name):
#         print(marks,name)
#         super().__init__(marks,name)
# obj=C(100,"siva")
# #print(obj.marks,obj.name)
# obj.m1()
# obj.m2()

#2
# class Restaurant:
#     def menu(self,item):
#         if item==1:
#             return 120
#         elif item==2:
#             return 250
#         elif item==3:
#             return 100
#         else:
#             return 0
# class FoodCourt(Restaurant):
#     bill=0
#     def display_menu(self):
#         print("**********--samba siva restaurant--********")
#         print("1.chicken briyani")
#         print("2.mutton briyani")
#         print("3.veg fried rice")
#     def order(self):
#         self.display_menu()
#         item=int(input("Enter the item:"))
#         quan=int(input("Enter the quantity:"))
#         FoodCourt.bill+=quan*self.menu(item)
#         print("if you continue order press 1 do you want to bill enter any key")
#         ch=input()
#         if ch=="1":
#             self.order()
#         else:
#             self.billing()
#     def billing(self):
#         print("bill amount is__",self.bill)
#         print("packing chargrs is 20")
#         print("Total bill amount is__",self.bill+20)
# class customer(FoodCourt):
#     pass
# c1=customer()
# c1.order()
#
# #3
# class Movie:
#     def ticket(self,movie):
#         if movie==1:
#             return 250
#         elif movie==2:
#             return 150
#         elif movie==3:
#             return 75
#         elif movie==4:
#             return 50
#         else:
#             return 0
# class Booking(Movie):
#     bill=0
#     def moviess(self):
#         print("1.varansi")
#         print("2.Dragon")
#         print("3.ramayan")
#         print("4.irumudi")
#     def selection(self):
#         self.moviess()
#         movie=int(input("choose movie name:"))
#         quan=int(input("enter quantity:"))
#         Booking.bill+=quan*self.ticket(movie)
#         print("if you continue order press 1 do you want to bill enter any key")
#         ch=input()
#         if ch=="1":
#             self.selection()
#         else:
#             self.billing()
#     def billing(self):
#         print("packing charges is 30")
#         print("total bill amount is__",self.bill+30)
# class Customer(Booking):
#     pass
# obj=Customer()
# obj.selection()
#
# #4
class course:
    def fee(self,course):
        if course==1:
            return 10000
        elif course==2:
            return 20000
        elif course==3:
            return 30000
        else:
            return 0
class academy(course):
    bill=0
    def courses(self):
        print("1 cse")
        print("2 inf")
        print("3 ece")
    def enroll(self):
        self.courses()
        a=int(input("Enter a course:"))
        academy.bill+=self.fee(a)
        print("enter the course 1 and if you want multiple courses any key")
        ch=input()
        if ch=="1":
            self.enroll()
        else:
            self.billing()
    def billing(self):
        print("total fee___",academy.bill)
        print("registration fee is $100")
        print("final total fee___",self.bill+100)
class student(academy):
    pass
obj=student()
obj.enroll()







