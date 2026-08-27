# class A:
#     def __int__(self):
#         print("A is called")
#     def m1(self):
#         print("m1")
# class B(A):
#     def __int__(self):
#         #super().__init__()
#         print("B is called")
#         super().__init__()
#     def m2(self):
#         print("m2")
# class C(A):
#     def __int__(self):
#         #super().__init__()
#         print("C is called")
#         super().__init__()
#     def m3(self):
#         print("m3")
# obj1=B()
# obj1.m1()
# obj1.m2()

class cab:
    def bike(self,km,price):
        return km*price
    def auto(self,km,price):
        return km*price
    def car(self,km,price):
        return km*price
class Uber(cab):
    bill=0
    def menu(self):
        print("___Uber___")
        print("1. Bike ___ 30/km")
        print("2. Auto ___ 80/km")
        print("3. Car ____ 100/km")
    def booking(self):
        self.menu()
        print("Choose one")
        choice=int(input())
        print("Enter kilometer to travel")
        km=int(input())
        if choice==1:
            Uber.bill+=self.bike(km,30)
        elif choice==2:
            Uber.bill+=self.auto(km,80)
        elif choice==3:
            Uber.bill+=self.car(km,100)
        else:
            print("Invalid Choice")
            return
        self.billing()
    def billing(self):
        print("fare amount is",Uber.bill)
        if Uber.bill>=1000:
            gst=0.1*Uber.bill
            print("GST amount is +",gst)
            Uber.bill+=gst
            discount=0.15*Uber.bill
            print("Discount amount is -",discount)
            Uber.bill-=discount
        print("Total fare amount is ",Uber.bill)
class Ola(cab):
    bill = 0
    def menu(self):
        print("___Ola___")
        print("1. Bike ___ 40/km")
        print("2. Auto ___ 100/km")
        print("3. Car ____ 130/km")
    def booking(self):
        self.menu()
        print("Choose one")
        choice = int(input())
        print("Enter kilometer to travel")
        km = int(input())
        if choice == 1:
            Ola.bill += self.bike(km, 40)
        elif choice == 2:
            Ola.bill += self.auto(km, 100)
        elif choice == 3:
            Ola.bill += self.car(km, 130)
        else:
            print("Invalid Choice")
            return
        self.billing()
    def billing(self):
        print("fare amount is", Ola.bill)
        if Ola.bill >= 1500:
            gst = 0.12 * Ola.bill
            print("GST amount is +", gst)
            Ola.bill += gst
            discount = 0.20 * Ola.bill
            print("Discount amount is -", discount)
            Ola.bill -= discount
        print("Total fare amount is ", Ola.bill)
print("Welcome to Chitti app ")
print("do you want ride with Uber Press 1 or ride with Ola Press 2")
choice=int(input())
if choice==1:
    obj=Uber()
    obj.booking()
elif choice==2:
    obj=Ola()
    obj.booking()
else:
    print("Invalid Choice")